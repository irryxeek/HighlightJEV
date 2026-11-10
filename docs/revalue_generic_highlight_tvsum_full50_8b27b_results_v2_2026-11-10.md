# TVSum 全50：固定背景下的价值标准与模型对照

先冻结所有合并预测，再读取固定标注。各范围均保留完整视频分母；失败视频记零失败信用，不伪造分数。

**无完整预测时，表中0分及相关差值仅用于失败分母记账，不是模型性能；含技术失败的差值不能直接解释为模型优劣。**

本报告27B阶段：`scoring27_v2`；报告目录：`all_models_report_v2`。

REZE_8B 为原8B迁移对照；context 为原具体规则加背景，revised 为最新贡献门槛规则加同一背景。**没有27B REZE对照。**

| 范围 | 方法 | Top-5 mAP (%) | 95%区间 | 完成/分母 | 解释 |
|---|---|---:|---|---:|---|
| dev10 | REZE_8B | 61.3167 | [49.3151, 71.5347] | 10/10 | 完整模型结果 |
| dev10 | context_8B | 59.3434 | [42.6228, 74.3771] | 10/10 | 完整模型结果 |
| dev10 | revised_8B | 65.5021 | [55.2552, 74.7160] | 10/10 | 完整模型结果 |
| dev10 | context_27B | 55.7760 | [47.0551, 63.5451] | 10/10 | 完整模型结果 |
| dev10 | revised_27B | 58.3670 | [46.5960, 69.2708] | 10/10 | 完整模型结果 |
| new40 | REZE_8B | 53.2858 | [49.0129, 57.2505] | 40/40 | 完整模型结果 |
| new40 | context_8B | 52.0726 | [46.4926, 57.7245] | 40/40 | 完整模型结果 |
| new40 | revised_8B | 53.5694 | [48.3356, 58.7242] | 40/40 | 完整模型结果 |
| new40 | context_27B | 55.4771 | [50.5566, 60.2696] | 40/40 | 完整模型结果 |
| new40 | revised_27B | 55.7359 | [51.2316, 60.0337] | 40/40 | 完整模型结果 |
| full50 | REZE_8B | 54.8919 | [50.8330, 58.8615] | 50/50 | 完整模型结果 |
| full50 | context_8B | 53.5267 | [47.9608, 59.0196] | 50/50 | 完整模型结果 |
| full50 | revised_8B | 55.9560 | [51.2237, 60.6106] | 50/50 | 完整模型结果 |
| full50 | context_27B | 55.5369 | [51.2600, 59.5788] | 50/50 | 完整模型结果 |
| full50 | revised_27B | 56.2622 | [52.0020, 60.3446] | 50/50 | 完整模型结果 |

| 范围 | 配对差值：前者−后者 | 差值(pp) | 95%区间 | 提升/下降/相同 |
|---|---|---:|---|---:|
| dev10 | context_8B_minus_REZE_8B | -1.9733 | [-16.5507, +9.7508] | 6/4/0 |
| dev10 | revised_8B_minus_REZE_8B | +4.1854 | [-7.8406, +16.9236] | 6/4/0 |
| dev10 | revised_8B_minus_context_8B | +6.1587 | [-4.9881, +21.0618] | 6/4/0 |
| dev10 | context_27B_minus_context_8B | -3.5674 | [-16.6922, +11.2937] | 3/7/0 |
| dev10 | revised_27B_minus_revised_8B | -7.1351 | [-18.4875, +3.2850] | 3/7/0 |
| dev10 | revised_27B_minus_context_27B | +2.5910 | [-3.3532, +11.3160] | 4/5/1 |
| new40 | context_8B_minus_REZE_8B | -1.2132 | [-6.8243, +4.3892] | 21/19/0 |
| new40 | revised_8B_minus_REZE_8B | +0.2837 | [-4.9419, +5.2979] | 23/17/0 |
| new40 | revised_8B_minus_context_8B | +1.4969 | [-1.7763, +4.6743] | 24/16/0 |
| new40 | context_27B_minus_context_8B | +3.4045 | [-2.5390, +9.5089] | 23/17/0 |
| new40 | revised_27B_minus_revised_8B | +2.1665 | [-3.3845, +7.9928] | 20/20/0 |
| new40 | revised_27B_minus_context_27B | +0.2589 | [-1.2283, +1.7459] | 21/16/3 |
| full50 | context_8B_minus_REZE_8B | -1.3652 | [-6.5894, +3.6700] | 27/23/0 |
| full50 | revised_8B_minus_REZE_8B | +1.0640 | [-3.7397, +5.7352] | 29/21/0 |
| full50 | revised_8B_minus_context_8B | +2.4292 | [-1.0446, +6.3432] | 30/20/0 |
| full50 | context_27B_minus_context_8B | +2.0101 | [-3.6382, +7.6818] | 26/24/0 |
| full50 | revised_27B_minus_revised_8B | +0.3062 | [-4.7945, +5.4572] | 23/27/0 |
| full50 | revised_27B_minus_context_27B | +0.7253 | [-1.0132, +2.9205] | 25/21/4 |

视频级配对 bootstrap：10,000次、seed=42；完整成功子集的独立AP与冻结UMT作者函数交叉核对。区间为描述性结果，未作多重比较校正。

dev10 已用于方法开发并复用8B缓存；new40 是本轮新增条件推理，不意味着这些视频从未被研究者审阅。full50 包含既有UMT训练划分的40条，不能称作独立官方 test50。

27B（若纳入）与8B使用相同背景及原像素缓存；更换模型也包含其原生处理器/模板差异。后处理新增模型/API调用和GPU消耗均为0。

复核文件：`merge_freeze.json`、`merged_predictions.json`、`report.json`、`summary.csv`、`paired.csv`、`per_video.csv`。

## 启动故障与成本

首个27B worker因GPU编号字符串与vLLM不兼容而退出：0请求、0token，8.266716秒墙钟／33.066865卡秒。失败源码、日志和全分母缺失记录保留；旧报告中的失败零信用不是模型性能。本报告使用独立scoring27_v2结果，未覆盖旧记录。

恢复只改数字GPU掩码及PCI_BUS_ID启动映射，沿用原UUID核验；模型、两版规则、帧、背景、原生处理参数及评价不变。旧8,426份CPU输入契约经字节等价核验后复用；没有重新生成背景或重跑8B。

| 阶段 | 尝试 | token（含失败预留） | GPU卡秒 | worker墙钟秒 |
|---|---:|---:|---:|---:|
| background40_0 | 130 | 105970 | 258.196 | 258.196 |
| background40_1 | 130 | 105338 | 255.701 | 255.701 |
| background40_2 | 130 | 104948 | 259.873 | 259.873 |
| background40_3 | 130 | 104376 | 263.105 | 263.105 |
| context8b40_0 | 1515 | 3030261 | 557.851 | 557.851 |
| context8b40_1 | 1438 | 2874038 | 514.485 | 514.485 |
| revised8b40_0 | 1515 | 3301446 | 578.257 | 578.257 |
| revised8b40_1 | 1438 | 3131440 | 553.429 | 553.429 |
| paired27b50 | 0 | 0 | 33.067 | 8.267 |
| paired27b50_recovery_v2 | 8426 | 17833056 | 51253.279 | 12813.320 |

本轮累计14,852次模型尝试、30,590,873token、54527.241卡秒（15.146456GPUh），包括失败启动。27B累计两次worker启动、一次技术恢复，模型推理零自动重试。旧预算不转移。

- [运行修订](revalue_generic_highlight_tvsum_full50_runtime_amendment_v2_2026-11-10.md)
- [原协议](revalue_generic_highlight_tvsum_full50_8b27b_protocol_2026-11-10.md)
- [统计风险检查（11/11）](artifacts/revalue_generic_highlight_tvsum_full50_8b27b_2026-11-10/statistical_checks.md)
- [完整JSON](artifacts/revalue_generic_highlight_tvsum_full50_8b27b_2026-11-10/all_models_report_v2/report.json)；[逐视频CSV](artifacts/revalue_generic_highlight_tvsum_full50_8b27b_2026-11-10/all_models_report_v2/per_video.csv)
- 原始运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_full50_8b27b_v1_2026-11-10`
