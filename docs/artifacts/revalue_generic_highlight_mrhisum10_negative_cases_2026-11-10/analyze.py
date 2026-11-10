"""Post-hoc negative-case audit of frozen Mr.HiSum10; CPU and old frames only."""
import hashlib
import math
import os
import sys
from collections import Counter
from pathlib import Path

import h5py
import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont

ROOT = Path('$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_mrhisum10_core_v1_2026-11-10')
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'driver_snapshot'))
from background import verify_trace
from core import read_json, sha256, window_readout, write_new
from historical import helpers
from media import StreamVideo
from native_metrics_frozen import _official_helpers


def order(values):
    return torch.argsort(torch.tensor(values, dtype=torch.float32), descending=True).tolist()


def range_rank(values, index):
    a = np.asarray(values, dtype=np.float32)
    return [int((a > a[index]).sum()) + 1, int((a >= a[index]).sum())]


def weights(index, n_seconds, segments):
    result = {}
    seconds = list(range(index * 5, min(index * 5 + 5, n_seconds)))
    for second in seconds:
        hits = [i for i, (a, b) in enumerate(segments) if int(a) <= second <= int(b)]
        if not hits:
            raise ValueError('Explicitly audit nearest-tail extrapolation if encountered')
        for i in hits:
            result[i] = result.get(i, 0.0) + 1 / len(seconds) / len(hits)
    return result


def main():
    assert os.environ.get('CUDA_VISIBLE_DEVICES') == '' and not torch.cuda.is_initialized()
    torch.set_num_threads(2)
    report = read_json(ROOT / 'comparison/report.json')
    prediction = read_json(ROOT / 'comparison/predictions.json')
    rows = read_json(ROOT / 'rows10.json')
    evaluation = read_json(ROOT / 'evaluation_binding.json')
    references = read_json(ROOT / 'input_reference.json')
    backgrounds = read_json(ROOT / 'backgrounds10.json')
    protected = [ROOT / p for p in ('campaign_manifest.json', 'authorization.json', 'complete.json',
        'comparison/report.json', 'comparison/predictions.json', 'comparison/prediction_freeze.json',
        'rows10.json', 'controls.json', 'backgrounds10.json', 'input_reference.json')]
    for name in ('background0', 'background1', 'scoring0', 'scoring1'):
        protected += [ROOT / name / p for p in ('manifest.json', 'worker_exit.json')]
    before = {str(p): sha256(p) for p in protected}
    ids = [r['vid'] for r in rows]
    deltas = {m: {v: report['evaluation']['per_video']['core_8B'][v][m] -
                     report['evaluation']['per_video']['REZE_8B'][v][m] for v in ids}
              for m in ('mAP50', 'mAP15', 'F1')}
    chosen = []
    reasons = {}
    for metric in ('mAP50', 'mAP15', 'F1'):
        vid = min(ids, key=lambda v: (deltas[metric][v], v))
        reasons.setdefault(vid, []).append('largest decline in ' + metric)
        if vid not in chosen:
            chosen.append(vid)
    write_new(OUT / 'selection.json', dict(kind='posthoc explanatory case selection; not a new test subset',
        rule='union of worst core-minus-REZE video for each of mAP50/mAP15/F1; ties by ID',
        selected=chosen, reasons=reasons, retain_full_ten_in_descriptive_tables=True))
    native = _official_helpers()
    all10, cases, raw_hashes, emission_totals = [], [], {}, Counter()
    label_path = Path(evaluation['label_root']) / 'mr_hisum.h5'
    assert sha256(label_path) == evaluation['labels_sha256']['mr_hisum.h5']
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 17)
    small = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
    with h5py.File(label_path, 'r') as label_file:
        for ri, row in enumerate(rows):
            vid, n = row['vid'], row['n_seconds']
            group = label_file[vid]
            gt, cps, gt_summary = group['gtscore'][:], group['change_points'][:], group['gt_summary'][:]
            data = {a: native['hd_metrics'](prediction[a][vid]['scores_1s'], gt) for a in ('REZE_8B', 'core_8B')}
            orders = {a: order(d['official_normalized_scores']) for a, d in data.items()}
            gt_order = order(data['core_8B']['gt_5s_scores'])
            summaries = {a: native['summary_metric'](prediction[a][vid]['scores_1s'], cps, gt_summary)
                         for a in ('REZE_8B', 'core_8B')}
            stage = ROOT / f'scoring{ri % 2}'
            current = read_json(stage / 'predictions.json')[vid]
            segments = current['segments']
            emitted = Counter()
            for wi, expected in enumerate(current['window_scores']):
                path = stage / 'requests' / vid / f'{wi:06d}.result.json'
                r = read_json(path)
                decoded = window_readout(r, 9454, 2753)
                assert decoded['score_mode'] == 'two_way' and math.isclose(decoded['score'], expected, abs_tol=1e-12)
                emitted[r['generated_text']] += 1
                raw_hashes[str(path)] = sha256(path)
            emission_totals.update(emitted)
            negatives = {}
            for a, d in data.items():
                for fraction in ('50', '15'):
                    assert abs(d['AP' + fraction] - report['evaluation']['per_video'][a][vid]['mAP' + fraction]) < 1e-9
                    k = d['gt_positive_count_' + fraction]
                    ranked = orders[a][:k]
                    negatives[a + '_top' + fraction] = dict(k=k,
                        nonpositive_count=sum(d['gt_binary'][fraction][j] == 0 for j in ranked),
                        boundary_tie=d['official_normalized_scores'][orders[a][k - 1]] == d['official_normalized_scores'][orders[a][k]])
            table = dict(vid=vid, metric_deltas={m: deltas[m][vid] for m in deltas},
                         metrics={a: report['evaluation']['per_video'][a][vid] for a in data},
                         native_bins=len(gt_order), ranked_nonpositives=negatives, emissions=dict(emitted),
                         raw_windows=len(current['window_scores']),
                         summary_selected_seconds={a: s['selected_seconds'] for a, s in summaries.items()})
            all10.append(table)
            if vid not in chosen:
                continue
            fraction = '50' if 'largest decline in mAP50' in reasons[vid] else '15'
            gt_binary = data['core_8B']['gt_binary'][fraction]
            k = sum(gt_binary)
            fp = next(j for j in orders['core_8B'] if gt_binary[j] == 0)
            missed = next((j for j in gt_order if gt_binary[j] and j not in orders['core_8B'][:k]), None)
            if missed is None:
                missed = next(j for j in gt_order if gt_binary[j])
            selections = [('highest_ranked_nonpositive', fp), ('highest_GT_missed_positive', missed)]
            clips, tags = [], {}
            for role, index in selections:
                ww = weights(index, n, segments)
                combined = sum(current['window_scores'][w] * weight for w, weight in ww.items())
                assert math.isclose(combined, data['core_8B']['pred_5s_scores'][index], abs_tol=2e-7)
                entry = dict(role=role, bin_index=index, seconds=[5 * index, min(5 * index + 5, n)],
                    gt_score=data['core_8B']['gt_5s_scores'][index], gt_rank=gt_order.index(index) + 1,
                    labels={f: data['core_8B']['gt_binary'][f][index] for f in ('50', '15')},
                    scores={a: d['pred_5s_scores'][index] for a, d in data.items()},
                    ranks={a: range_rank(d['official_normalized_scores'], index) for a, d in data.items()},
                    source_windows=[dict(index=w, seconds=segments[w], mean_weight=weight,
                                         score=current['window_scores'][w]) for w, weight in ww.items()])
                clips.append(entry)
                for w in ww:
                    tags.setdefault(w, []).append(f'{role} {5*index}-{min(5*index+5,n)}s')
            case = dict(**table, reasons=reasons[vid], reference_fraction=fraction, background=backgrounds[vid],
                        examined_native_bins=clips, sheets=[], audited_windows=[],
                        native_summary={a: s['summary'] for a, s in summaries.items()})
            assert sha256(row['video_path']) == row['media_sha256']
            decoder = StreamVideo(row)
            indices = sorted(tags)
            for page, start in enumerate(range(0, len(indices), 4), 1):
                page_ids = indices[start:start + 4]
                canvas = Image.new('RGB', (1320, 60 + 220 * len(page_ids)), 'white')
                draw = ImageDraw.Draw(canvas)
                draw.text((10, 8), f'{vid} | native top{fraction}% negative / missed positive | original input frames', font=font, fill='#17334a')
                draw.text((10, 32), 'CPU re-decode; every model RGB hash, frame index and PTS matches frozen inputs. No audio.', font=small, fill='#42576b')
                for index_in_page, wi in enumerate(page_ids):
                    decoded, trace = decoder.read(wi, 1)
                    verify_trace(trace, references[vid], wi)
                    pixels = decoded[0]['video']
                    y = 60 + index_in_page * 220
                    draw.text((10, y), f'w{wi} [{segments[wi][0]:g},{segments[wi][1]:g}s]  core P(Yes)={current["window_scores"][wi]:.7f}', font=font, fill='#17334a')
                    draw.text((10, y + 23), ' / '.join(tags[wi]), font=small, fill='#9b421f')
                    for col, frame in enumerate(pixels):
                        image = Image.fromarray(frame)
                        image.thumbnail((216, 142))
                        canvas.paste(image, (col * 220 + 2, y + 48))
                        draw.text((col * 220 + 4, y + 194), f'{trace["frame_timestamps"][0][col][0]:.3f}s', font=small, fill='#17334a')
                    case['audited_windows'].append(dict(index=wi, model_rgb_sha256=hashlib.sha256(pixels.tobytes()).hexdigest(),
                        frame_timestamps=trace['frame_timestamps'][0], tags=tags[wi]))
                path = OUT / f'{vid}_page{page}.jpg'
                if path.exists():
                    raise FileExistsError(path)
                canvas.save(path, quality=94)
                case['sheets'].append(dict(path=str(path), sha256=sha256(path)))
            cases.append(case)
            del decoder
    after = {p: sha256(p) for p in before}
    assert before == after and not torch.cuda.is_initialized()
    write_new(OUT / 'raw_result_hashes.json', raw_hashes)
    write_new(OUT / 'analysis.json', dict(all10=all10, cases=cases, selection=read_json(OUT / 'selection.json'),
        overall_emissions=dict(emission_totals), old_records_before=before, old_records_after=after,
        labels_sha256=evaluation['labels_sha256'], source_sha256=sha256(__file__),
        new_experiment_model_calls=0, new_experiment_tokens=0, gpu_allocation=0,
        limitations='Labels used only for posthoc diagnosis, not new predictions; negatives are native relative labels, not proof of no semantic value. Single-token probabilities do not reveal causal rule use.'))
    print({'selected': chosen, 'all10': [{k: r[k] for k in ('vid', 'ranked_nonpositives', 'emissions')} for r in all10],
           'cases': [{'vid': c['vid'], 'clips': c['examined_native_bins'], 'sheets': c['sheets']} for c in cases]})


if __name__ == '__main__':
    main()
