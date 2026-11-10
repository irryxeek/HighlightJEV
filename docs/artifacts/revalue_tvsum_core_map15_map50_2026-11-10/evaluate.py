"""CPU-only extension of the existing TVSum percentage-AP protocol to core_8B."""

import csv
import hashlib
import importlib.util
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
MERIT = Path('$MERIT_ROOT')
ROOT = Path('$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_new40_core_value_v1_2026-11-10')
PREVIOUS = MERIT / 'docs/artifacts/revalue_tvsum_map15_map50_2026-11-10'
TOP5 = ROOT / 'driver_snapshot/metrics.py'
REPORT = MERIT / 'docs/revalue_generic_highlight_tvsum_core_map15_map50_2026-11-10.md'
ARMS = ('REZE_8B', 'revised_8B', 'core_8B')
ZERO = dict(model_requests=0, model_tokens=0, model_workers=0, retries=0,
            gpu_allocations=0, gpu_seconds=0)


def read(path):
    return json.loads(Path(path).read_text())


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def csv_write(path, rows):
    with Path(path).open('x', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def request_counts():
    return {s: {k: len(list((ROOT/s/'requests').rglob('*.'+k+'.json')))
                for k in ('reserved', 'result')}
            for s in ('shard0', 'shard1')}


def main():
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '':
        raise RuntimeError('Run with CUDA_VISIBLE_DEVICES empty')
    if (HERE/'source_manifest.json').exists():
        raise FileExistsError('Audit already prepared; inspect receipts before any repeat')
    started = time.monotonic()
    binding = read(ROOT/'comparison_binding.json')
    freeze = read(ROOT/'comparison/merge_freeze.json')
    complete = read(ROOT/'complete.json')
    original = read(ROOT/'comparison/report.json')
    old_manifest = read(PREVIOUS/'source_manifest.json')
    old_receipt = read(PREVIOUS/'completion_receipt.json')
    tests = read(PREVIOUS/'test_receipt.json')
    assert tests['exit_code'] == 0
    assert sha(PREVIOUS/'metrics.py') == tests['files_sha256']['metrics.py']
    assert sha(PREVIOUS/'test_metrics.py') == tests['files_sha256']['test_metrics.py']
    previous_results_hash = next(v for k,v in old_receipt['output_sha256'].items()
                                 if k.endswith('/results.json'))
    assert sha(PREVIOUS/'results.json') == previous_results_hash
    assert sha(PREVIOUS/'source_manifest.json') == old_receipt['source_manifest_sha256']
    assert sha(PREVIOUS/'PROTOCOL.md') == read(PREVIOUS/'results.json')['protocol_sha256']
    assert sha(binding['annotation_path']) == binding['annotation_sha256']
    assert sha(old_manifest['label_path']) == binding['annotation_sha256']
    assert sha(ROOT/'comparison/merged_predictions.json') == freeze['merged_predictions_sha256']
    assert freeze['labels_read'] is False
    assert sha(ROOT/'comparison/report.json') == complete['report_json_sha256']
    assert sha(complete['project_report_path']) == complete['project_report_sha256']
    ids = binding['new_ids']
    assert len(ids) == len(set(ids)) == 40 and ids == freeze['video_ids']
    assert ids == old_manifest['scopes']['scoring50']['new40']
    campaign = read(ROOT/'campaign_manifest.json')
    for name in ('metrics.py', 'vendor/umt_tvsum.py'):
        assert sha(ROOT/'driver_snapshot'/name) == campaign['driver_sha256'][name]
    files = [ROOT/name for name in ('campaign_manifest.json', 'authorization.json', 'complete.json',
             'comparison_binding.json', 'comparison/merge_freeze.json', 'comparison/report.json',
             'comparison/merged_predictions.json', 'controls.json', 'rows40.json')]
    files += [Path(binding['annotation_path']), Path(complete['project_report_path']),
              Path(old_manifest['label_path']), TOP5, TOP5.parent/'vendor/umt_tvsum.py']
    files += [PREVIOUS/name for name in ('metrics.py', 'test_metrics.py', 'test_receipt.json',
              'source_manifest.json', 'completion_receipt.json', 'results.json', 'PROTOCOL.md')]
    exits = {}
    for stage in ('shard0', 'shard1'):
        files += [ROOT/stage/name for name in ('manifest.json', 'worker_exit.json', 'prediction_freeze.json')]
        exits[stage] = read(ROOT/stage/'worker_exit.json')
        assert exits[stage]['exit_code'] == 0 and not exits[stage]['owned_live_processes_remaining']
    old_hashes = {str(p): sha(p) for p in files}
    counts_before = request_counts()
    assert sum(c['reserved'] for c in counts_before.values()) == original['cost']['attempted_requests'] == 2953
    assert all(c['reserved'] == c['result'] for c in counts_before.values())
    manifest = dict(created_at=datetime.now(timezone.utc).isoformat(), request='测一下我们新方法在tvsum上的map15和map50',
        videos=ids, arms=ARMS, grid_seconds=2, current_condition='core_8B', denominator=40,
        previous_metric_protocol=str(PREVIOUS/'PROTOCOL.md'),
        files_sha256=old_hashes, new_source_sha256={n: sha(HERE/n) for n in ('PROTOCOL.md','evaluate.py')},
        request_counts=counts_before, new_experimental_consumption=ZERO,
        official_hivid_protocol_reproduction=False, independent_unseen_test=False)
    write(HERE/'source_manifest.json', manifest)

    import numpy as np
    import sklearn
    import torch
    torch.set_num_threads(1)
    assert not torch.cuda.is_initialized()
    metric = load('frozen_percentage_metrics', PREVIOUS/'metrics.py')
    top5 = load('frozen_original_top5', TOP5)
    predictions = read(ROOT/'comparison/merged_predictions.json')
    labels = read(binding['annotation_path'])
    previous = read(PREVIOUS/'results.json')['per_video']['scoring50']['native']
    details, summary, flat, validation = {}, [], [], []
    for arm in ARMS:
        assert set(predictions[arm]) == set(ids)
        details[arm] = {}
        for vid in ids:
            item = predictions[arm][vid]
            assert item['status'] == 'complete'
            scores = item['scores_2s']
            got = metric.video_metrics(scores, labels[vid]['anno'])
            original_top5 = top5.video_metrics(scores, labels[vid]['anno'])
            assert abs(original_top5['Top5_AP'] - original['per_video'][arm][vid]['Top5_AP']) < 1e-10
            assert np.allclose(original_top5['annotator_AP'], original['per_video'][arm][vid]['annotator_AP'], atol=1e-10, rtol=0)
            if arm in previous:
                for rule in ('primary','per_annotator','inclusive_boundary'):
                    for key in ('mAP15','mAP50'):
                        assert abs(got[rule][key] - previous[arm][vid][rule][key]) < 1e-10
            got['Top5_AP'] = original_top5['Top5_AP']
            details[arm][vid] = got
            flat.append(dict(arm=arm, vid=vid, Top5_AP=got['Top5_AP'],
                mAP15=got['primary']['mAP15'], mAP50=got['primary']['mAP50'],
                per_annotator_mAP15=got['per_annotator']['mAP15'],
                per_annotator_mAP50=got['per_annotator']['mAP50'],
                inclusive_mAP15=got['inclusive_boundary']['mAP15'],
                inclusive_mAP50=got['inclusive_boundary']['mAP50'],
                n_clips=got['n_clips'], gt15_boundary_tie=got['targets']['15']['boundary_tie'],
                gt50_boundary_tie=got['targets']['50']['boundary_tie'],
                positive15=got['targets']['15']['positives'], positive50=got['targets']['50']['positives'],
                inclusive_positive15=got['targets']['15']['inclusive_positives'],
                inclusive_positive50=got['targets']['50']['inclusive_positives']))
            validation.append(dict(arm=arm, vid=vid, top5_and_20_annotators_match=True,
                percentage_control_matches_previous=arm in previous, sklearn_independent_AP_match=True))
        author = top5.author_top5_map({v:predictions[arm][v]['scores_2s'] for v in ids}, labels)
        average_top5 = float(np.mean([details[arm][v]['Top5_AP'] for v in ids]))
        assert abs(author-average_top5) < .00051
        row = dict(arm=arm, denominator=40, complete=40, Top5_mAP=average_top5)
        for rule in ('primary','per_annotator','inclusive_boundary'):
            for key in ('mAP15','mAP50'):
                row[rule+'_'+key] = float(np.mean([details[arm][v][rule][key] for v in ids]))
        summary.append(row)
    paired = []
    for control in ('REZE_8B','revised_8B'):
        for rule in ('primary','per_annotator','inclusive_boundary'):
            for key in ('mAP15','mAP50'):
                delta = [details['core_8B'][v][rule][key]-details[control][v][rule][key] for v in ids]
                paired.append(dict(contrast='core_8B - '+control, rule=rule, metric=key, **metric.bootstrap(delta)))
    assert not torch.cuda.is_initialized()
    assert old_hashes == {p:sha(p) for p in old_hashes}
    assert counts_before == request_counts()
    result = dict(summary=summary, paired=paired, per_video=details, video_ids=ids,
        denominator=40, new_experimental_consumption=ZERO,
        source_manifest_sha256=sha(HERE/'source_manifest.json'),
        official_hivid_protocol_reproduction=False, previous_tests_reused_and_hash_checked=True,
        original_top5_120_video_arm_checks=True, old_control_percentage_checks=80,
        old_sources_and_requests_unchanged=True,
        gt_boundary_tie_video_counts={str(p):sum(details['core_8B'][v]['targets'][str(p)]['boundary_tie'] for v in ids) for p in (15,50)})
    write(HERE/'results.json', result)
    csv_write(HERE/'summary.csv', summary)
    csv_write(HERE/'per_video.csv', flat)
    write(HERE/'validation.json', dict(status='passed', checks=validation, source_hashes_unchanged=True,
        CUDA_initialized=False, original_tests_receipt_sha256=sha(PREVIOUS/'test_receipt.json'),
        old_request_counts_unchanged=counts_before, old_costs_unchanged=original['cost'],
        numpy=np.__version__, sklearn=sklearn.__version__, torch=torch.__version__))

    lines = ['# TVSum 最新8B方法：mAP15 / mAP50补充结果', '',
        '2026-11-10。仅CPU读取已冻结预测；新增模型调用、实验token、GPU和worker均为0。', '',
        '## 范围与主结果', '',
        '最新版本为 core_8B：修改最终决策目标为主线关键贡献，同时收紧品牌、身份和一般场景价值。固定原后40条，三组全部40/40；这40条已用于开发诊断。最新版本未覆盖旧10条，不能混合报告为全50条。', '',
        '| 方法 | Top-5 mAP (%) | mAP15 (%) | mAP50 (%) |',
        '|---|---:|---:|---:|']
    names = {'REZE_8B':'REZE 8B','revised_8B':'上一修订版 8B','core_8B':'最新关键贡献版 8B'}
    for r in summary:
        lines.append(f"| {names[r['arm']]} | {r['Top5_mAP']:.4f} | {r['primary_mAP15']:.4f} | {r['primary_mAP50']:.4f} |")
    lines += ['', '## 配对差值', '', '| 最新版相对 | 指标 | 差值(pp) | 视频配对95%区间 | 升/降/同 |',
              '|---|---|---:|---|---|']
    for p in paired:
        if p['rule'] != 'primary':
            continue
        lines.append(f"| {p['contrast']} | {p['metric']} | {p['mean']:+.4f} | [{p['ci95'][0]:+.4f}, {p['ci95'][1]:+.4f}] | {p['improved']}/{p['worse']}/{p['unchanged']} |")
    lines += ['', '视频为配对单位；bootstrap 10000次、seed42。未经多重比较校正；补充指标与已用开发样本不能支撑独立测试结论。', '',
        '## 指标定义与比较边界', '',
        '沿用既有百分比评价协议：原2秒网格上，20人评分均值作为GT；取GT最高floor(15%×N)/floor(50%×N)为正例，同分按时间索引升序；完整float32预测序列计算非插值AP，再按视频等权平均。预测并列保持。15/50不是预测片段个数，也不是IoU阈值。', '',
        '本轮没有平滑、改分或新采样。该口径是TVSum补充评价，不能冒称与HiVid论文或Mr.HiSum原生5秒协议完全一致；原UMT Top-5 mAP仍按旧实现保留。', '',
        '## 同时报告的敏感性', '', '| 方法 | 每人分别mAP15 | 每人分别mAP50 | 含GT边界同分mAP15 | 含GT边界同分mAP50 |',
        '|---|---:|---:|---:|---:|']
    for r in summary:
        lines.append(f"| {names[r['arm']]} | {r['per_annotator_mAP15']:.4f} | {r['per_annotator_mAP50']:.4f} | {r['inclusive_boundary_mAP15']:.4f} | {r['inclusive_boundary_mAP50']:.4f} |")
    ties = result['gt_boundary_tie_video_counts']
    lines += ['', f"15%与50%边界分别有{ties['15']}和{ties['50']}/40条视频发生GT同分。包含全部边界同分的口径可能超过目标正例比例；逐视频数量与所有配对敏感性见JSON。", '',
        '## CPU核验与产物', '',
        '- 复用且核对已有6项指标测试的源码哈希；所有实际AP由sklearn与独立阈值分组AP实现交叉核对。',
        '- 120条视频×方法的原Top-5及20人分项复现；3组均通过作者UMT实现交叉核对；80条旧对照的百分比主指标与两项敏感性复现。',
        '- 旧预测、来源报告、完成收据及请求账本数量均未变；旧实验仍为2953次、7,250,867 token、1238.170375 GPU秒。本次新增均为0。',
        f'- [协议]({HERE}/PROTOCOL.md)；[完整结果]({HERE}/results.json)；[逐视频CSV]({HERE}/per_video.csv)。',
        f'- [运行脚本]({HERE}/evaluate.py)；[来源哈希]({HERE}/source_manifest.json)；[核验]({HERE}/validation.json)；[完成收据]({HERE}/completion_receipt.json)。',
        '- 保留全部旧报告；未推送。']
    with REPORT.open('x') as stream:
        stream.write('\n'.join(lines)+'\n')
    outputs = [HERE/n for n in ('source_manifest.json','results.json','summary.csv','per_video.csv','validation.json')]+[REPORT]
    write(HERE/'completion_receipt.json', dict(status='complete',
        completed_at=datetime.now(timezone.utc).isoformat(), cpu_wall_seconds=time.monotonic()-started,
        new_experimental_consumption=ZERO, old_sources_and_ledgers_unchanged=True,
        output_sha256={str(p):sha(p) for p in outputs}))
    print(json.dumps(dict(summary=summary, primary_paired=[p for p in paired if p['rule']=='primary'],
                         report_path=str(REPORT)),ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
