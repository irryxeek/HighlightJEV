> **发布说明：本文件为未完成运行的失败记账快照。缺失预测的零完成信用不是模型性能；最新方案的完整全量结果尚未获得。**

# TVSum 最新8B关键贡献版：全50条统一评价

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run + validate；2026-11-10
- Verification Status: ANALYZED；一次模型运行，CPU核验，不是重复模型复现。

## 全50条结果

最新 core_8B 原只覆盖40条，本轮以完全相同的冻结模型、提示和价值规则补齐旧10条。主结果统一统计全50条，旧10与后40只作分组诊断。全部视频已参与开发或诊断，不是独立未见测试集。

| 方法 | 完成/总数 | Top-5 mAP (%) | mAP15 (%) | mAP50 (%) |
|---|---:|---:|---:|---:|
| REZE 8B | 50/50 | 54.8919 | 34.9280 | 68.4963 |
| 上一修订版8B | 50/50 | 55.9560 | 35.4147 | 70.4712 |
| 最新关键贡献版8B | 40/50 | 44.6406 | 28.0960 | 56.3949 |

## 配对差值与置信区间

| 比较 | 指标 | 差值(pp) | 95%配对区间 | 升/降/同 |
|---|---|---:|---|---|
| core_8B - REZE_8B | mAP15 | -6.8320 | [-12.9613, -1.2445] | 26/24/0 |
| core_8B - REZE_8B | mAP50 | -12.1014 | [-20.8735, -4.1529] | 26/24/0 |
| core_8B - revised_8B | mAP15 | -7.3187 | [-12.8453, -2.4558] | 19/31/0 |
| core_8B - revised_8B | mAP50 | -14.0763 | [-23.3034, -5.8458] | 23/27/0 |

区间针对“新版−对照”的差值，不是mAP本身。以视频为配对单位，从同一50条中有放回抽样50条、重复10000次（seed42），取差值均值分布的2.5%和97.5%分位数。区间包含0表示当前数据仍与无改善及一定程度的下降/提升相容；不能证明两方法相同，也不能说mAP为0。
这些区间描述视频样本变动，不包含重新运行模型的随机性；未作多重比较校正，已用开发集不能作为独立测试显著性证明。

## 评价口径

Top-5沿用冻结作者UMT实现。mAP15/mAP50沿用已冻结补充协议：原2秒网格上20人均值为GT，取GT最高floor(15%×N)/floor(50%×N)为正例，GT同分按时间升序；完整float32预测序列算非插值AP，再按视频等权平均。没有平滑或修改分数。该补充口径尚未与HiVid论文或Mr.HiSum原生5秒协议完全对齐。

每人分别评价、GT边界全部同分计正例两项敏感性及10/40分组数据同时保存在JSON，不择优报告。

## 新增成本与核验

- 新增尝试 0/1260，成功 0；token 0/5,160,960；GPU生命周期 21.618523/1800秒；worker 1/1；重试0。
- 旧40条、背景与REZE/上一版对照均0新增调用；不挪用旧预算。模型输出、源帧/PTS、概率读出和每视频分母保留。
- 新窗口轨迹核对 0；旧完成产物与账本哈希不变；原Top-5和已有对照百分比指标经CPU复现核对。
- 原始运行：`$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_full50_core_value_v2_2026-11-10`；失败曲线保持null，不用上一版替代。

- [完整结果](artifacts/revalue_generic_highlight_tvsum_full50_core_value_v2_2026-11-10/report.json)；[逐视频CSV](artifacts/revalue_generic_highlight_tvsum_full50_core_value_v2_2026-11-10/per_video.csv)；[新10条完成收据](artifacts/revalue_generic_highlight_tvsum_full50_core_value_v2_2026-11-10/prediction_freeze.json)。
- [全50预测冻结](artifacts/revalue_generic_highlight_tvsum_full50_core_value_v2_2026-11-10/merge_freeze.json)；[运行协议](revalue_generic_highlight_tvsum_full50_core_value_protocol_v2_2026-11-10.md)。
- 未推送。
