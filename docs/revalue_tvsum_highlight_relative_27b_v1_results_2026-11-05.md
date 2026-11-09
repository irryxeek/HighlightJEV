# ReVALUE TVSum：相对高光选片 F-relative / FV-relative 对照

## Material Passport

- Origin Skill / Mode: academic-research-suite / experiment-agent，run。
- Verification Status: UNVERIFIED；运行和 CPU 机械检查完成，独立语义核验尚未完成。

固定 UMT val10 的完整十视频；只新增 20 次选片请求，复用父轮完整事实／价值记忆。
模型、帧、choice_map、输出接受契约、分数 multiset 和原生评价规则保持冻结。
主比较为 FV-relative − F-relative；父 D/F/FV 单列为历史参照，不是本轮新预测。

| 本轮条件 | 原生 Top-5 mAP (%) | 稳定同分敏感性 (%) | 合法输出 |
|---|---:|---:|---:|
| B0 | 61.3167 | 61.3288 | 缓存基线 |
| F-relative | 59.7625 | 60.0608 | 10/10 |
| FV-relative | 62.9247 | 62.8132 | 10/10 |

主差值 **+3.1622 pp**；逐视频改善／下降／持平：7/2/1。按视频配对 bootstrap 95% 区间：[0.12222222222222712, 6.274331597222221]。

## 历史参照与描述性变化

| 父轮条件 | 原生 Top-5 mAP (%) |
|---|---:|
| 父轮 D | 51.5878 |
| 父轮 F | 57.1878 |
| 父轮 FV | 56.3288 |

F-relative_minus_parent_F：+2.5747 pp；改善／下降／持平 3/5/2。

FV-relative_minus_parent_FV：+6.5958 pp；改善／下降／持平 10/0/0。

历史变化仅描述此开发集上的结果，不替代本轮 F/FV 配对比较，也不证明独立泛化。

## 选片变化与完整分母

相对原生 B0 的 Top-5 成员／顺序变化统计：`{'F': {'score_vectors_changed': 10, 'top5_members_changed': 10, 'top5_order_changed': 10, 'top5_order_only_changed': 0}, 'FV': {'score_vectors_changed': 10, 'top5_members_changed': 10, 'top5_order_changed': 10, 'top5_order_only_changed': 0}}`。
技术无效分类：`{}`。技术失败／未尝试均回退 B0；合法空推荐记为弃权。完整十视频全部进入评价；固定同分规则另作敏感性结果，未挑选有利指标。

## 成本

本轮实际新增尝试 **20 次**；已知 token **486791**，含未结算预留的计账 token **486791**；GPU 生命周期 **3437.986 秒**。零模型重试。
父轮共享建库为 **80 次／208,128 token**，本轮直接使用缓存，实际新增建库调用为 **0**。

| 独立方法成本口径 | 本轮选片请求 | 历史建库请求 | 合计请求（含缓存建库） | 合计计账 token |
|---|---:|---:|---:|---:|
| F-relative | 10 | 80 | 90 | 446718 |
| FV-relative | 10 | 80 | 90 | 456329 |

上述独立方法口径分别计一次建库成本，不能将两臂的共享建库再加到本轮实耗中。原 REZE B0 的缓存初始化成本另保存在机器结果，不是本轮新增调用。
父轮修复系列累计保留：模型尝试 218 次，含预派发失败的账本预留 219 次，1697518 计账 token，31318.962 GPU 秒。
加入本轮后，该系列累计模型尝试 238 次，预留 239 次，2184309 计账 token，34756.948 GPU 秒。
旧 v1.1、预派发失败、v2 初始化失败及父 v2.1 实耗分别保存在 cost_accounting；没有重置或删除。

## 门槛与结论边界

数值门槛：`{'final_valid_count': 20, 'expected': 20, 'at_least_95pct': True, 'primary_gain_at_least_1pp': True, 'semantic_evidence_review': 'pending', 'automatic_expansion_authorized': False, 'numerical_gates_passed': True}`。
合法输出至少 19/20 且主差值至少 +1 pp 才通过数值门槛；独立语义审阅仍为 pending。来源／时间契约合法不等于画面语义或高光价值真实；没有自动扩样、扩大预算或新增回看。

逐视频结果、预测冻结、原响应、来源记忆、账本和退出收据：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_highlight_relative_27b_v1_2026-11-05`。
