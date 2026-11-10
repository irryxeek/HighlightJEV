"""One fixed CPU-only spacing diagnostic; never rescore or call a model."""

import hashlib
import json
import math
import os
import sys
from pathlib import Path

import numpy as np
import torch

ROOT = Path('$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_full50_8b27b_v1_2026-11-10')
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'scoring27_v2/source_snapshot'))
from metrics import ap_of_ranked_binary, bootstrap_mean  # noqa: E402

ARMS = ('REZE_8B', 'context_8B', 'revised_8B')
MIN_START_GAP_SECONDS = 6
K = 5


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(name, value):
    with (OUT / name).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')


def top5_ap(indices, label):
    return 100 * float(np.mean([ap_of_ranked_binary(label[indices, j].tolist()) for j in range(20)]))


def main():
    assert os.environ.get('CUDA_VISIBLE_DEVICES') == ''
    assert not torch.cuda.is_initialized()
    binding_path = ROOT / 'comparison_binding.json'
    pred_path = ROOT / 'all_models_report_v2/merged_predictions.json'
    report_path = ROOT / 'all_models_report_v2/report.json'
    prior_path = Path('$MERIT_ROOT/docs/artifacts/revalue_generic_highlight_tvsum_8b_new40_cases_2026-11-10/analysis.json')
    before = {str(p): sha(p) for p in (binding_path, pred_path, report_path, prior_path)}
    binding = read(binding_path)
    predictions = read(pred_path)
    ids = binding['new_ids']
    assert len(ids) == len(set(ids)) == 40 and not set(ids) & set(binding['development_ids'])
    selection = {}
    for model in ARMS:
        selection[model] = {}
        for vid in ids:
            p = predictions[model][vid]
            assert p['status'] == 'complete'
            scores = torch.tensor(p['scores_2s'], dtype=torch.float32)
            order = torch.argsort(scores, descending=True).tolist()
            spaced = []
            for i in order:
                if all(abs(2 * i - 2 * j) >= MIN_START_GAP_SECONDS for j in spaced):
                    spaced.append(i)
                    if len(spaced) == K:
                        break
            assert len(spaced) == K
            assert all(abs(2 * i - 2 * j) >= 6 for n, i in enumerate(spaced) for j in spaced[n + 1:])
            assert spaced[0] == order[0]
            selection[model][vid] = {'original_top5': order[:5], 'spaced_top5': spaced,
                                     'original_scores_unchanged': True}
    save('selection_freeze.json', {'scope': 'all original new40', 'videos': ids, 'arms': ARMS,
                                  'selection_rule': 'greedy original float32 descending order; >=6s between 2s clip starts; stop at five',
                                  'reason_for_6s': 'two original 3s windows; fixed for this one posthoc diagnostic, no parameter search',
                                  'selections': selection, 'annotation_read_during_selection': False,
                                  'posthoc_exploration': True, 'prior_results_and_cases_known': True,
                                  'models_loaded': False, 'new_model_calls': 0,
                                  'input_hashes': before, 'source_sha256': sha(Path(__file__))})
    # All candidates are frozen before this script opens GT. This is explicitly
    # post-hoc; it does not turn the already examined new40 into held-out data.
    ann_path = Path(binding['annotation_path'])
    assert sha(ann_path) == binding['annotation_sha256']
    annotations = read(ann_path)
    old_details = {r['vid']: r for r in read(prior_path)['all40']}
    all_details, summary = {}, {}
    for model in ARMS:
        details = []
        for vid in ids:
            label = torch.tensor(annotations[vid]['anno'], dtype=torch.float32)
            binary = (label > label.median(dim=0).values).to(torch.float32).numpy()
            means = label.mean(dim=1).numpy()
            old, new = selection[model][vid]['original_top5'], selection[model][vid]['spaced_top5']
            old_ap, new_ap = top5_ap(old, binary), top5_ap(new, binary)
            assert math.isclose(old_ap, old_details[vid][model], abs_tol=1e-9)
            details.append({'vid': vid, 'original_ap': old_ap, 'spaced_ap': new_ap,
                            'delta_pp': new_ap - old_ap, 'original_top5': old, 'spaced_top5': new,
                            'original_positive_votes_of_100': int(binary[old].sum()),
                            'spaced_positive_votes_of_100': int(binary[new].sum()),
                            'original_top5_gt_mean': float(means[old].mean()),
                            'spaced_top5_gt_mean': float(means[new].mean())})
        summary[model] = {'original_mean_AP': float(np.mean([d['original_ap'] for d in details])),
                          'spaced_mean_AP': float(np.mean([d['spaced_ap'] for d in details])),
                          'paired_delta': bootstrap_mean([d['delta_pp'] for d in details]),
                          'improved': sum(d['delta_pp'] > 1e-9 for d in details),
                          'worsened': sum(d['delta_pp'] < -1e-9 for d in details),
                          'same': sum(abs(d['delta_pp']) <= 1e-9 for d in details),
                          'original_positive_percent': float(np.mean([d['original_positive_votes_of_100'] for d in details])),
                          'spaced_positive_percent': float(np.mean([d['spaced_positive_votes_of_100'] for d in details])),
                          'denominator': 40}
        all_details[model] = details
    assert all(sha(Path(p)) == h for p, h in before.items())
    assert not torch.cuda.is_initialized()
    result = {'scope': 'new40 only', 'interpretation': 'offline top-five selection diagnostic, not new model scores or replacement official baseline',
              'summary': summary, 'per_video': all_details,
              'selection_freeze_sha256': sha(OUT / 'selection_freeze.json'), 'source_sha256': sha(Path(__file__)),
              'input_hashes_before_and_after_equal': before, 'annotation_sha256': sha(ann_path),
              'parameter_values_tried': [6], 'new_experiment_model_calls': 0,
              'new_experiment_tokens': 0, 'gpu_allocations': 0, 'cuda_initialized': False,
              'multiple_comparison_correction': 'none; exploratory diagnostic only'}
    save('analysis.json', result)
    print(json.dumps(summary, indent=2))
    selected = ['jcoYJXDG9sw', 'i3wAGJaaktw', '-esJrBWj2d8', 'xxdtq8mxegs', 'byxOvuiIJV0']
    print('PREVIOUS_CASES', json.dumps([d for d in all_details['revised_8B'] if d['vid'] in selected]))


if __name__ == '__main__':
    main()
