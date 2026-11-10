"""Post-hoc CPU diagnostics and exact-input contact sheets; never runs inference."""

import hashlib
import json
import math
import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.stats import spearmanr

RUN = Path('$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_val10_v1_2026-11-10')
OUT = Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, payload):
    with path.open('x') as stream:
        json.dump(payload, stream, indent=2, ensure_ascii=False)
        stream.write('\n')


def source_weights(index, segments):
    weights = {}
    for second in (2 * index, 2 * index + 1):
        hits = [i for i, (start, end) in enumerate(segments) if int(start) <= second <= int(end)]
        if not hits:
            raise ValueError('Uncovered evaluation second')
        for i in hits:
            weights[i] = weights.get(i, 0) + 0.5 / len(hits)
    return weights


def main():
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '':
        raise ValueError('CPU-only audit requires CUDA_VISIBLE_DEVICES empty')
    sys.path.insert(0, str(RUN / 'source_snapshot'))
    from media import StreamVideo
    from metrics import two_second_scores

    freeze = read(RUN / 'prediction_freeze.json')
    assert sha(RUN / 'predictions.json') == freeze['predictions_sha256']
    before = {name: sha(RUN / name) for name in ('manifest.json', 'predictions.json', 'prediction_freeze.json', 'worker_exit.json')}
    comparison = read(RUN / 'comparison.json')
    binding = read(RUN / 'comparison_binding.json')
    predictions = read(RUN / 'predictions.json')
    rows = read(RUN / 'rows.json')
    assert sha(Path(binding['annotation_path'])) == binding['annotation_sha256']
    annotations = read(Path(binding['annotation_path']))
    negative = sorted(comparison['per_video'], key=lambda d: (d['delta_pp'], d['vid']))[:3]
    positive = sorted(comparison['per_video'], key=lambda d: (-d['delta_pp'], d['vid']))[:2]
    selected = [d['vid'] for d in negative + positive]
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 17)
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
    videos = []
    for row in rows:
        vid = row['vid']
        old_path = Path(binding['baseline'][vid]['path'])
        assert sha(old_path) == binding['baseline'][vid]['sha256']
        segments = read(RUN / 'media' / f'{vid}.json')['segments']
        old_scores = two_second_scores(read(old_path)['second_scores'], int(row['duration'] / 2))
        new_scores = predictions[vid]['scores_2s']
        old_windows = [item['pyes'] for p in sorted((old_path.parent.parent / 'chunks' / vid).glob('*.json')) for item in read(p)['records']]
        new_windows = predictions[vid]['window_scores']
        labels = np.asarray(annotations[vid]['anno'], dtype=np.float32)
        # Author's torch.median uses the lower of the two central values.
        medians = np.sort(labels, axis=0)[(len(labels) - 1) // 2]
        positive_votes = (labels > medians).sum(axis=1)
        gt_mean = labels.mean(axis=1)
        detail = next(d for d in comparison['per_video'] if d['vid'] == vid)
        item = {'vid': vid, 'title_for_posthoc_context_only': annotations[vid]['title'],
                'domain': annotations[vid]['domain'], 'delta_pp': detail['delta_pp'],
                'all_clip_spearman_to_mean_annotation': {
                    'baseline': float(spearmanr(old_scores, gt_mean).statistic),
                    'generic': float(spearmanr(new_scores, gt_mean).statistic)},
                'clips': {}, 'sheets': [], 'audited_source_windows': []}
        tags = {}
        for arm, key in [('baseline', 'old_top5'), ('generic', 'new_top5')]:
            entries = []
            for rank, index in enumerate(detail[key], 1):
                weights = source_weights(index, segments)
                for scores, windows in [(old_scores, old_windows), (new_scores, new_windows)]:
                    assert math.isclose(sum(windows[i] * w for i, w in weights.items()), scores[index], abs_tol=1e-12)
                entry = {'rank': rank, 'clip_index': index, 'seconds': [2 * index, 2 * index + 2],
                         'baseline_score': old_scores[index], 'generic_score': new_scores[index],
                         'mean_annotation_1_to_5': float(gt_mean[index]),
                         'positive_annotators_of_20': int(positive_votes[index]),
                         'source_windows': [{'index': i, 'seconds': segments[i], 'weight': w,
                                             'baseline_score': old_windows[i], 'generic_score': new_windows[i]} for i, w in weights.items()]}
                entries.append(entry)
                for i in weights:
                    tags.setdefault(i, []).append(f'{arm[0].upper()}{rank}@{2 * index}s')
            item['clips'][arm] = entries
        if vid in selected:
            stream = StreamVideo(row)
            window_indices = sorted(tags)
            for page, start in enumerate(range(0, len(window_indices), 6), 1):
                indices = window_indices[start:start + 6]
                canvas = Image.new('RGB', (1320, 72 + 213 * len(indices)), '#ffffff')
                draw = ImageDraw.Draw(canvas)
                draw.text((12, 8), f'{vid} | {item["title_for_posthoc_context_only"][:85]}', fill='#18344b', font=font)
                draw.text((12, 36), 'Exact model frames; B=REZE top5, G=generic top5. Visible review only; audio not inspected.', fill='#42576b', font=small)
                for row_i, index in enumerate(indices):
                    clips, trace = stream.read(index, 1)
                    batch = next(p for p in (RUN / 'traces' / vid).glob('*.json') if int(p.stem) <= index < int(p.stem) + len(read(p)['model_rgb_sha256']))
                    original = read(batch)
                    offset = index - int(batch.stem)
                    assert clips[0]['rgb_sha256'] == original['model_rgb_sha256'][offset]
                    assert trace['frame_timestamps'][0] == original['frame_timestamps'][offset]
                    y = 72 + row_i * 213
                    left, right = segments[index]
                    draw.text((12, y), f'w{index:03d} [{left:g},{right:g}s]  B={old_windows[index]:.6f}  G={new_windows[index]:.6f}', fill='#18344b', font=font)
                    draw.text((12, y + 23), ', '.join(tags[index]), fill='#a3481c', font=small)
                    for col, pixels in enumerate(clips[0]['video']):
                        image = Image.fromarray(pixels)
                        image.thumbnail((216, 144))
                        canvas.paste(image, (col * 220 + 2, y + 48))
                        timestamp = trace['frame_timestamps'][0][col][0]
                        draw.text((col * 220 + 4, y + 193), f'{timestamp:.3f}s', fill='#18344b', font=small)
                    item['audited_source_windows'].append({'index': index, 'model_rgb_sha256': clips[0]['rgb_sha256'], 'original_hash_match': True})
                path = OUT / f'{vid}_page{page}.jpg'
                if path.exists():
                    raise FileExistsError(path)
                canvas.save(path, quality=92)
                item['sheets'].append({'path': str(path), 'sha256': sha(path)})
        videos.append(item)
        print(vid, item['title_for_posthoc_context_only'], 'delta', item['delta_pp'], flush=True)
    after = {name: sha(RUN / name) for name in before}
    assert before == after
    result = {'audit_kind': 'posthoc descriptive CPU analysis; not new model predictions',
              'selection_rule': 'three largest AP declines and two largest AP improvements, diagnostic only; full10 statistics retained',
              'selected_visual_cases': selected, 'videos': videos, 'frozen_run_files_before': before,
              'frozen_run_files_after': after, 'analysis_source_sha256': sha(Path(__file__)),
              'new_experiment_model_calls': 0, 'new_experiment_tokens': 0,
              'gpu_allocation': 0, 'reference_annotation': binding['annotation_path'],
              'annotation_sha256': binding['annotation_sha256']}
    save(OUT / 'analysis.json', result)
    print('DONE', OUT / 'analysis.json')


if __name__ == '__main__':
    main()
