"""Three-way CPU comparison after detailed predictions are frozen."""

import csv
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

RUN = Path('$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_val10_detailed_v1_2026-11-10')
OUT = Path(__file__).resolve().parent


def distribution(values):
    values = [v for v in values if v is not None]
    if not values:
        return None
    return dict(count=len(values), mean=float(np.mean(values)), minimum=min(values), maximum=max(values),
                unique=len(set(values)), ge_095=sum(v >= .95 for v in values), ge_050=sum(v >= .5 for v in values))


def main():
    sys.path.insert(0, str(RUN / 'source_snapshot'))
    import metrics
    from core import load_preparation, read_json, sha256, write_new

    manifest, rows = load_preparation(RUN)
    freeze = read_json(RUN / 'prediction_freeze.json')
    assert freeze['predictions_sha256'] == sha256(RUN / 'predictions.json')
    assert freeze['manifest_sha256'] == sha256(RUN / 'manifest.json')
    assert freeze['labels_read'] is False
    assert read_json(RUN / 'driver_exit.json')['cpu_evaluation_exit'] == 0
    binding = read_json(RUN / 'comparison_binding.json')
    brief_root = Path(binding['brief_control']['root'])
    assert sha256(brief_root / 'predictions.json') == binding['brief_control']['predictions_sha256']
    assert sha256(brief_root / 'prediction_freeze.json') == binding['brief_control']['freeze_sha256']
    assert sha256(brief_root / 'manifest.json') == binding['brief_control']['manifest_sha256']
    detailed = read_json(RUN / 'predictions.json')
    brief = read_json(brief_root / 'predictions.json')
    predictions = {'REZE': {}, 'brief': {}, 'detailed': {}}
    window_values = {arm: [] for arm in predictions}
    modes = {arm: Counter() for arm in predictions}
    input_parity = []
    all_records = {'brief': [], 'detailed': []}
    for row in rows:
        vid = row['vid']
        ref = binding['baseline'][vid]
        baseline_path = Path(ref['path'])
        assert sha256(baseline_path) == ref['sha256']
        baseline = read_json(baseline_path)
        predictions['REZE'][vid] = metrics.two_second_scores(baseline['second_scores'], int(row['duration'] / 2))
        predictions['brief'][vid] = brief[vid]['scores_2s']
        predictions['detailed'][vid] = detailed[vid]['scores_2s']
        checked = 0
        for path in sorted((RUN / 'traces' / vid).glob('*.json')):
            new_trace = read_json(path)
            old_trace = read_json(brief_root / 'traces' / vid / path.name)
            reze_trace = read_json(baseline_path.parent.parent / 'chunks' / vid / path.name)['trace']
            for key in ('model_rgb_sha256', 'frame_timestamps', 'frame_indices'):
                assert new_trace[key] == old_trace[key] == reze_trace[key], (vid, path.name, key)
            checked += len(new_trace['model_rgb_sha256'])
        if detailed[vid]['status'] == 'complete':
            assert checked == len(detailed[vid]['window_scores'])
        input_parity.append(dict(vid=vid, matched_windows=checked, comparison='detailed/brief/REZE exact pixel hash, index and PTS'))
        for arm, root, blob in [('brief', brief_root, brief), ('detailed', RUN, detailed)]:
            window_values[arm].extend(blob[vid]['window_scores'])
            modes[arm].update(blob[vid]['score_modes'])
            all_records[arm].extend(read_json(p) for p in (root / 'requests' / vid).glob('*.result.json'))
        for path in (baseline_path.parent.parent / 'chunks' / vid).glob('*.json'):
            for record in read_json(path)['records']:
                window_values['REZE'].append(record['pyes'])
                modes['REZE'][record['score_mode']] += 1
    parity = dict(status='passed', videos=input_parity,
                  total_matched_windows=sum(v['matched_windows'] for v in input_parity),
                  labels_read=False)
    write_new(RUN / 'runtime_input_parity.json', parity)

    # Labels enter only after source/prediction freeze and all-input parity checks.
    assert sha256(binding['annotation_path']) == binding['annotation_sha256']
    annotations = read_json(binding['annotation_path'])
    per_video = []
    for row in rows:
        vid = row['vid']
        labels = np.asarray(annotations[vid]['anno'], dtype=np.float32)
        medians = np.sort(labels, axis=0)[(len(labels) - 1) // 2]
        positives = labels > medians
        entry = dict(vid=vid, methods={})
        for arm in predictions:
            scores = predictions[arm][vid]
            if scores is None:
                entry['methods'][arm] = dict(status='incomplete', Top5_AP_failure_credit=0)
                continue
            details = metrics.video_metrics(scores, annotations[vid]['anno'])
            ids = details['top5_indices']
            correlation = None if len(set(scores)) == 1 else float(spearmanr(scores, labels.mean(axis=1)).statistic)
            details.update(status='complete', Top1_positive_annotator_percent=100 * float(positives[ids[0]].mean()),
                           Top5_positive_annotator_percent=100 * float(positives[ids].mean()),
                           Top5_mean_annotation=float(labels[ids].mean()),
                           all_clip_spearman_to_mean_annotation=correlation)
            entry['methods'][arm] = details
        per_video.append(entry)
    summaries, paired = {}, {}
    for arm in predictions:
        complete = [v['methods'][arm] for v in per_video if v['methods'][arm]['status'] == 'complete']
        valid_predictions = {vid: s for vid, s in predictions[arm].items() if s is not None}
        main = sum(v['Top5_AP'] for v in complete) / len(rows)
        official = metrics.author_top5_map(valid_predictions, annotations) if valid_predictions else None
        if complete:
            assert abs(official - np.mean([v['Top5_AP'] for v in complete])) <= .00051
        auxiliary = {}
        for field in ('Top1_positive_annotator_percent', 'Top5_positive_annotator_percent', 'Top5_mean_annotation', 'all_clip_spearman_to_mean_annotation'):
            values = [v[field] for v in complete if v[field] is not None]
            auxiliary[field] = {'mean': float(np.mean(values)) if values else None, 'valid_videos': len(values)}
        summaries[arm] = dict(Top5_mAP_full_denominator=main, denominator=len(rows), complete_videos=len(complete),
                              official_UMT_complete_subset=official, diagnostic_complete_subset_only=auxiliary,
                              constant_videos=[v['vid'] for v in per_video if v['methods'][arm].get('unique_scores') == 1],
                              top5_boundary_ties=sum(v['top5_boundary_tie'] for v in complete),
                              window_distribution=distribution(window_values[arm]), readout_modes=dict(modes[arm]))
    for control in ('brief', 'REZE'):
        delta = []
        for v in per_video:
            d = v['methods']['detailed'].get('Top5_AP', 0) - v['methods'][control].get('Top5_AP', 0)
            v['detailed_minus_' + control + '_pp'] = d
            delta.append(d)
        paired['detailed_minus_' + control] = dict(**metrics.bootstrap_mean(delta),
                                                  improved=sum(d > 1e-10 for d in delta),
                                                  worsened=sum(d < -1e-10 for d in delta),
                                                  unchanged=sum(abs(d) <= 1e-10 for d in delta))
    cost = {}
    for arm, root in [('brief', brief_root), ('detailed', RUN)]:
        raw = all_records[arm]
        cost[arm] = dict(prediction_freeze=read_json(root / 'prediction_freeze.json'),
                         gpu_lifecycle=read_json(root / 'worker_exit.json'),
                         emitted_labels=dict(Counter(r['generated_text'].strip() for r in raw)),
                         observed_prompt_tokens_min=min((r['prompt_tokens'] for r in raw), default=None),
                         observed_prompt_tokens_max=max((r['prompt_tokens'] for r in raw), default=None))
    result = dict(scope='same complete official UMT val10, previously seen development data',
                  summaries=summaries, paired=paired, per_video=per_video, cost=cost,
                  runtime_input_parity=parity, manifest_sha256=sha256(RUN / 'manifest.json'),
                  predictions_sha256=freeze['predictions_sha256'], annotation_sha256=binding['annotation_sha256'],
                  analysis_source_sha256=sha256(Path(__file__)), baseline_new_calls=0, analysis_model_calls=0,
                  intervention='Historical detailed criteria and local single-token adapter replace brief examples; longer input is inherent')
    write_new(RUN / 'comparison.json', result)
    write_new(OUT / 'comparison.json', result)
    with (OUT / 'per_video.csv').open('x') as f:
        writer = csv.writer(f)
        writer.writerow(['vid', 'REZE', 'brief', 'detailed', 'detailed_minus_brief_pp', 'detailed_minus_REZE_pp'])
        for v in per_video:
            writer.writerow([v['vid']] + [v['methods'][arm].get('Top5_AP') for arm in predictions] +
                            [v['detailed_minus_brief_pp'], v['detailed_minus_REZE_pp']])
    print(json.dumps({'scores': {k: v['Top5_mAP_full_denominator'] for k, v in summaries.items()}, 'paired': paired}, ensure_ascii=False))


if __name__ == '__main__':
    main()
