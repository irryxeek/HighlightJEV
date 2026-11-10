"""Read frozen TVSum50 results and inspect cached pixels; CPU only, no inference."""

import csv
import hashlib
import json
import math
import os
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont

ROOT = Path('$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_full50_8b27b_v1_2026-11-10')
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'scoring27_v2/source_snapshot'
sys.path.insert(0, str(SOURCE))
from metrics import video_metrics  # noqa: E402


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(name, value):
    with (OUT / name).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')


def weights(index, segments):
    result = {}
    for second in (2 * index, 2 * index + 1):
        hits = [i for i, (a, b) in enumerate(segments) if int(a) <= second <= int(b)]
        if not hits:
            raise ValueError('Unexpected uncovered second')
        for i in hits:
            result[i] = result.get(i, 0) + .5 / len(hits)
    return result


def order(scores):
    return torch.argsort(torch.tensor(scores, dtype=torch.float32), descending=True).tolist()


def main():
    assert os.environ.get('CUDA_VISIBLE_DEVICES') == ''
    assert not torch.cuda.is_initialized()
    report = ROOT / 'all_models_report_v2'
    binding = read(ROOT / 'comparison_binding.json')
    annotation_path = Path(binding['annotation_path'])
    assert sha(annotation_path) == binding['annotation_sha256']
    protected = [ROOT / p for p in [
        'campaign_manifest.json', 'rows50.json', 'backgrounds50.json', 'cache50/cache_index.json',
        'scoring27_v2/manifest.json', 'scoring27_v2/prediction_freeze.json',
        'scoring27_v2/predictions_context.json', 'scoring27_v2/predictions_revised.json',
        'scoring27_v2/worker_exit.json', 'all_models_report_v2/merged_predictions.json',
        'all_models_report_v2/report.json', 'all_models_report_v2/per_video.csv',
    ]] + [annotation_path]
    before = {str(p): sha(p) for p in protected}
    predictions = read(report / 'merged_predictions.json')
    annotations = read(annotation_path)
    cache = read(ROOT / 'cache50/cache_index.json')
    backgrounds = read(ROOT / 'backgrounds50.json')
    scores = {}
    with (report / 'per_video.csv').open() as stream:
        for row in csv.DictReader(stream):
            assert row['status'] == 'complete'
            scores.setdefault(row['vid'], {'vid': row['vid'], 'split': row['split']})[row['model']] = float(row['Top5_AP_or_zero_failure_credit'])
    selected = [x['vid'] for x in sorted(scores.values(), key=lambda x: (x['revised_27B'], x['vid']))[:3]]
    summaries = []
    cases = []
    record_hashes = {}
    raw_totals = {c: {'generated': Counter(), 'readout': Counter(), 'windows': 0} for c in ('context', 'revised')}
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 17)
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
    for vid, ap in scores.items():
        label = np.asarray(annotations[vid]['anno'], dtype=np.float32)
        median = np.sort(label, axis=0)[(len(label) - 1) // 2]
        votes = (label > median).sum(axis=1)
        means = label.mean(axis=1)
        orders = {model: order(items[vid]['scores_2s']) for model, items in predictions.items()}
        ranks = {m: {j: rank for rank, j in enumerate(indices, 1)} for m, indices in orders.items()}
        summary = dict(ap)
        summary['diagnostics'] = {}
        for model, items in predictions.items():
            p = items[vid]
            top = orders[model][:5]
            d = {'top5_indices': top, 'top5_mean_annotation': float(means[top].mean()),
                 'top5_positive_votes_of_100': int(votes[top].sum()),
                 'top5_boundary_tie_float32': bool(np.float32(p['scores_2s'][orders[model][4]]) == np.float32(p['scores_2s'][orders[model][5]]))}
            if 'window_scores' in p:
                ws = np.asarray(p['window_scores'])
                d.update({'window_count': len(ws), 'window_pyes_min': float(ws.min()),
                          'window_pyes_max': float(ws.max()), 'window_pyes_median': float(np.median(ws)),
                          'window_pyes_ge_half': int((ws >= .5).sum()),
                          'window_pyes_ge_095': int((ws >= .95).sum())})
            if model.endswith('_27B'):
                condition = model.split('_')[0]
                generated, modes = Counter(), Counter()
                for i, score in enumerate(p['window_scores']):
                    path = ROOT / f'scoring27_v2/requests/{condition}/{vid}/{i:06d}.result.json'
                    rec = read(path)
                    record_hashes[str(path)] = sha(path)
                    assert rec['status'] == 'complete' and rec['vid'] == vid and rec['condition'] == condition
                    assert rec['output_tokens'] == 1 and rec['window_index'] == i
                    assert math.isclose(rec['readout']['score'], score, abs_tol=1e-14)
                    generated[rec['generated_text']] += 1
                    modes[rec['readout']['score_mode']] += 1
                d['generated_labels'] = dict(generated)
                d['readout_modes'] = dict(modes)
                raw_totals[condition]['generated'].update(generated)
                raw_totals[condition]['readout'].update(modes)
                raw_totals[condition]['windows'] += len(p['window_scores'])
            summary['diagnostics'][model] = d
        summaries.append(summary)
        if vid not in selected:
            continue
        for model, items in predictions.items():
            assert math.isclose(video_metrics(items[vid]['scores_2s'], annotations[vid]['anno'])['Top5_AP'], ap[model], abs_tol=1e-9)
        segments = predictions['revised_27B'][vid]['segments']

        def describe(index):
            ww = weights(index, segments)
            for model, items in predictions.items():
                if 'window_scores' in items[vid]:
                    combined = sum(items[vid]['window_scores'][i] * w for i, w in ww.items())
                    assert math.isclose(combined, items[vid]['scores_2s'][index], abs_tol=1e-12)
            return {'clip_index': index, 'seconds': [2 * index, 2 * index + 2],
                    'mean_annotation': float(means[index]), 'positive_annotators_of_20': int(votes[index]),
                    'scores': {m: p[vid]['scores_2s'][index] for m, p in predictions.items()},
                    'ranks': {m: r[index] for m, r in ranks.items()},
                    'source_windows': [{'index': i, 'seconds': segments[i], 'weight': w,
                                        'scores': {m: p[vid]['window_scores'][i] for m, p in predictions.items() if 'window_scores' in p[vid]}}
                                       for i, w in ww.items()]}

        gt = sorted(range(len(label)), key=lambda i: (-int(votes[i]), -float(means[i]), i))[:5]
        case = {'vid': vid, 'title_posthoc_only': annotations[vid]['title'], 'domain': annotations[vid]['domain'],
                'metrics': summary, 'background_used_in_both_models': backgrounds[vid],
                'top5': {m: [describe(i) for i in o[:5]] for m, o in orders.items()},
                'annotation_highest_votes_then_mean': [describe(i) for i in gt], 'audited_windows': [], 'sheets': []}
        tags = {}
        for model in ('revised_27B', 'revised_8B', 'REZE_8B'):
            n = 5 if model == 'revised_27B' else 2
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
            draw.text((10, 35), 'Frozen model input frames; 27/8 = revised P(Yes); assistant visual audit, no audio.', fill='#42576b', font=small)
            for ri, wi in enumerate(page_ids):
                entry = cache[vid][wi]
                path = Path(entry['path'])
                assert sha(path) == entry['file_sha256']
                pixels = np.load(path, allow_pickle=False)
                assert str(pixels.dtype) == 'uint8' and list(pixels.shape) == entry['shape']
                assert hashlib.sha256(pixels.tobytes()).hexdigest() == entry['model_rgb_sha256']
                y = 70 + ri * 225
                score27 = predictions['revised_27B'][vid]['window_scores'][wi]
                score8 = predictions['revised_8B'][vid]['window_scores'][wi]
                draw.text((10, y), f'w{wi} [{segments[wi][0]:g},{segments[wi][1]:g}s]  27={score27:.7f}  8={score8:.7f}', fill='#17334a', font=font)
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
    after = {str(p): sha(p) for p in protected}
    assert before == after
    for condition in raw_totals:
        raw_totals[condition]['generated'] = dict(raw_totals[condition]['generated'])
        raw_totals[condition]['readout'] = dict(raw_totals[condition]['readout'])
        assert raw_totals[condition]['windows'] == 4213
    assert not torch.cuda.is_initialized()
    write_new('analysis.json', {'kind': 'posthoc descriptive diagnosis, not new predictions',
                              'selection': 'lowest three revised_27B Top5 AP, ties by video ID; not representative',
                              'selected': selected, 'all50': summaries, 'cases': cases,
                              'raw_output_totals': raw_totals, 'new_experiment_model_calls': 0,
                              'new_experiment_tokens': 0, 'gpu_allocation': 0, 'cuda_initialized': False,
                              'frozen_before': before, 'frozen_after': after, 'source_sha256': sha(Path(__file__))})
    write_new('raw_result_hashes.json', record_hashes)
    print(json.dumps({'selected': selected, 'raw_output_totals': raw_totals,
                      'images': [s['path'] for c in cases for s in c['sheets']], 'output': str(OUT / 'analysis.json')}, indent=2))


if __name__ == '__main__':
    main()
