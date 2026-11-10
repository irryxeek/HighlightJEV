"""Post-hoc low-AP diagnostics on the completed 8B new40 only; no inference."""

import importlib.util
import json
import math
import os
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
PREVIOUS = OUT.parent / 'revalue_generic_highlight_tvsum_27b_cases_2026-11-10'
spec = importlib.util.spec_from_file_location('case_helpers', PREVIOUS / 'analyze_cases.py')
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)
ROOT, read, sha, weights, order = helpers.ROOT, helpers.read, helpers.sha, helpers.weights, helpers.order


def describe(index, vid, predictions, segments, means, votes, ranks):
    ww = weights(index, segments)
    for p in predictions.values():
        if 'window_scores' in p[vid]:
            assert math.isclose(sum(p[vid]['window_scores'][i] * w for i, w in ww.items()),
                                p[vid]['scores_2s'][index], abs_tol=1e-12)
    return {'clip_index': index, 'seconds': [2 * index, 2 * index + 2],
            'mean_annotation': float(means[index]), 'positive_annotators_of_20': int(votes[index]),
            'scores': {m: p[vid]['scores_2s'][index] for m, p in predictions.items()},
            'ranks': {m: r[index] for m, r in ranks.items()},
            'source_windows': [{'index': i, 'seconds': segments[i], 'weight': w,
                                'scores': {m: p[vid]['window_scores'][i] for m, p in predictions.items() if 'window_scores' in p[vid]}}
                               for i, w in ww.items()]}


def main():
    assert os.environ.get('CUDA_VISIBLE_DEVICES') == '' and not torch.cuda.is_initialized()
    prior = read(PREVIOUS / 'analysis.json')
    before = dict(prior['frozen_after'])
    before[str(PREVIOUS / 'analysis.json')] = sha(PREVIOUS / 'analysis.json')
    before[str(PREVIOUS / 'analyze_cases.py')] = sha(PREVIOUS / 'analyze_cases.py')
    assert all(sha(Path(p)) == h for p, h in before.items())
    predictions = read(ROOT / 'all_models_report_v2/merged_predictions.json')
    binding = read(ROOT / 'comparison_binding.json')
    annotations = read(Path(binding['annotation_path']))
    cache = read(ROOT / 'cache50/cache_index.json')
    backgrounds = read(ROOT / 'backgrounds50.json')
    rows = [r for r in prior['all50'] if r['split'] == 'new40']
    assert len(rows) == 40 and {r['vid'] for r in rows} == set(binding['new_ids'])
    lowest = sorted(rows, key=lambda r: (r['revised_8B'], r['vid']))[:3]
    declines = sorted(rows, key=lambda r: (r['revised_8B'] - r['REZE_8B'], r['vid']))[:3]
    selected = list(dict.fromkeys(r['vid'] for r in lowest + declines))
    totals, record_hashes, cases = {}, {}, []
    for condition in ('context', 'revised'):
        generated, modes = Counter(), Counter()
        for row in rows:
            vid = row['vid']
            shard = binding['new_ids'].index(vid) % 2
            stage = ROOT / f'{condition}8b40_{shard}'
            for filename in ['manifest.json', 'prediction_freeze.json', 'predictions.json', 'worker_exit.json']:
                path = stage / filename
                before[str(path)] = sha(path)
            for i, expected in enumerate(predictions[condition + '_8B'][vid]['window_scores']):
                path = stage / f'requests/{vid}/{i:06d}.result.json'
                rec = read(path)
                assert rec['status'] == 'complete' and rec['vid'] == vid and rec['window_index'] == i
                assert rec['output_tokens'] == 1
                lp = {x['id']: x['logprob'] for x in rec['top20']}
                assert 9454 in lp and 2753 in lp
                m = max(lp[9454], lp[2753])
                value = math.exp(lp[9454] - m) / (math.exp(lp[9454] - m) + math.exp(lp[2753] - m))
                assert math.isclose(value, expected, abs_tol=1e-12)
                generated[rec['generated_text']] += 1
                modes['two_way'] += 1
                record_hashes[str(path)] = sha(path)
        assert sum(generated.values()) == 2953
        totals[condition] = {'windows': 2953, 'generated': dict(generated), 'readout': dict(modes)}
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 17)
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
    for vid in selected:
        row = next(r for r in rows if r['vid'] == vid)
        labels = np.asarray(annotations[vid]['anno'], dtype=np.float32)
        median = np.sort(labels, axis=0)[(len(labels) - 1) // 2]
        votes, means = (labels > median).sum(axis=1), labels.mean(axis=1)
        orders = {m: order(p[vid]['scores_2s']) for m, p in predictions.items()}
        ranks = {m: {i: rank for rank, i in enumerate(indices, 1)} for m, indices in orders.items()}
        segments = predictions['revised_27B'][vid]['segments']
        gt = sorted(range(len(labels)), key=lambda i: (-int(votes[i]), -float(means[i]), i))[:5]
        for m, p in predictions.items():
            assert math.isclose(helpers.video_metrics(p[vid]['scores_2s'], annotations[vid]['anno'])['Top5_AP'], row[m], abs_tol=1e-9)
        case = {'vid': vid, 'split': 'new40', 'title_posthoc_only': annotations[vid]['title'],
                'domain': annotations[vid]['domain'], 'metrics': row, 'background_used_in_both_models': backgrounds[vid],
                'top5': {m: [describe(i, vid, predictions, segments, means, votes, ranks) for i in o[:5]] for m, o in orders.items()},
                'annotation_highest_votes_then_mean': [describe(i, vid, predictions, segments, means, votes, ranks) for i in gt],
                'audited_windows': [], 'sheets': []}
        tags = {}
        for model in ('revised_8B', 'REZE_8B', 'revised_27B'):
            n = 5 if model == 'revised_8B' else 2
            for rank, index in enumerate(orders[model][:n], 1):
                for wi in weights(index, segments):
                    tags.setdefault(wi, []).append(f'{model} rank{rank}@{2*index}s')
        for rank, index in enumerate(gt[:2], 1):
            for wi in weights(index, segments):
                tags.setdefault(wi, []).append(f'label rank{rank}@{2*index}s')
        indices = sorted(tags)
        for page, start in enumerate(range(0, len(indices), 5), 1):
            page_ids = indices[start:start + 5]
            canvas = Image.new('RGB', (1320, 70 + 225 * len(page_ids)), 'white')
            draw = ImageDraw.Draw(canvas)
            draw.text((10, 8), f'{vid}: {case["title_posthoc_only"][:95]}', fill='#17334a', font=font)
            draw.text((10, 35), 'Original model frames; 8/27 = revised P(Yes); assistant visual audit, no audio.', fill='#42576b', font=small)
            for ri, wi in enumerate(page_ids):
                entry, y = cache[vid][wi], 70 + ri * 225
                path = Path(entry['path'])
                assert sha(path) == entry['file_sha256']
                pixels = np.load(path, allow_pickle=False)
                assert str(pixels.dtype) == 'uint8' and list(pixels.shape) == entry['shape']
                assert hashlib_pixels(pixels) == entry['model_rgb_sha256']
                p8, p27 = predictions['revised_8B'][vid]['window_scores'][wi], predictions['revised_27B'][vid]['window_scores'][wi]
                draw.text((10, y), f'w{wi} [{segments[wi][0]:g},{segments[wi][1]:g}s]  8={p8:.7f}  27={p27:.7f}', fill='#17334a', font=font)
                draw.text((10, y + 23), ' / '.join(tags[wi])[:165], fill='#9b421f', font=small)
                for col, frame in enumerate(pixels):
                    image = Image.fromarray(frame)
                    image.thumbnail((216, 145))
                    canvas.paste(image, (col * 220 + 2, y + 49))
                    draw.text((col * 220 + 4, y + 199), f'{entry["frame_timestamps"][col][0]:.3f}s', fill='#17334a', font=small)
                case['audited_windows'].append({'index': wi, 'file_sha256': entry['file_sha256'],
                                                'model_rgb_sha256': entry['model_rgb_sha256'],
                                                'frame_timestamps': entry['frame_timestamps'], 'tags': tags[wi]})
            path = OUT / f'{vid}_page{page}.jpg'
            if path.exists():
                raise FileExistsError(path)
            canvas.save(path, quality=93)
            case['sheets'].append({'path': str(path), 'sha256': sha(path)})
        cases.append(case)
    after = {p: sha(Path(p)) for p in before}
    assert before == after and not torch.cuda.is_initialized()
    analysis = {'kind': 'posthoc descriptive diagnosis, not new predictions', 'scope': 'new40_only',
                'selection': 'lowest three revised_8B AP plus three largest declines versus REZE_8B; deduplicate, diagnostic only',
                'selected': selected, 'lowest_three': [r['vid'] for r in lowest], 'largest_decline_three': [r['vid'] for r in declines],
                'all40': rows, 'cases': cases, 'raw_output_totals_new40': totals,
                'new_experiment_model_calls': 0, 'new_experiment_tokens': 0, 'gpu_allocation': 0,
                'frozen_before': before, 'frozen_after': after, 'source_sha256': sha(Path(__file__))}
    for name, value in [('analysis.json', analysis), ('raw_result_hashes.json', record_hashes)]:
        with (OUT / name).open('x') as stream:
            json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
            stream.write('\n')
    print(json.dumps({'selected': selected, 'raw_output_totals_new40': totals,
                      'images': [s['path'] for c in cases for s in c['sheets']], 'output': str(OUT / 'analysis.json')}, indent=2))


def hashlib_pixels(pixels):
    import hashlib
    return hashlib.sha256(pixels.tobytes()).hexdigest()


if __name__ == '__main__':
    main()
