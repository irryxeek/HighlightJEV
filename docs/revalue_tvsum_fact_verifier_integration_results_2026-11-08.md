# TVSum：事实记忆＋后置价值 verifier 接入结果

## Material Passport

- 来源：academic-research-suite / experiment-agent / run；2026-11-08。
- 仅 CPU 接入与评价，复用旧 10 视频／50 对／100 次模型响应；新增模型调用、实验 token 和 GPU 消耗均为 0。
- 所有旧模型响应、事实记忆和基线保留；本轮新建排序结果并在读取标签前冻结。
- 这是已反复查看的开发样本上的事后分析；复用的 C/V 响应早于 v3 原子修复。

## 方法

仅事实记忆 F-local 生成初始 Top-5；verifier 读取旧局部帧和事实记忆。C 作普通复核，V 增加详细五维价值标准；均不读取价值记忆库。双方事件与贡献均支持、片内引用对应且明确选择备选时，才交换固定候选位置。其余情况保持原选择。
主导出使用固定完整排名位置交换，排名编码只是评价用分数。F-local 对照的完整排名及每位标注者 AP 与原输出完全一致。数值交换敏感性另报。

## 完整 10 视频结果

| 条件 | Top-5 mAP | 相对 F-local |
|---|---:|---:|
| F_local | 56.6465 | +0.0000 pp |
| F_Cverify | 59.8750 | +3.2285 pp |
| F_Vverify | 59.7396 | +3.0931 pp |

固定 10 视频旧参照：D-1fps 69.2479，FV-local（选片前价值记忆）59.7007，REZE B0 51.8542。D 的视觉输入量和成本不同；FV-local 与后置 verifier 的调用结构也不同，不能只归因于价值模块位置。

## 配对差值与完整保留

| 差值 | 均值 pp | 描述性 95% 区间 | 升／降／平 |
|---|---:|---|---|
| F_Vverify_minus_F_Cverify | -0.1354 | [-0.5118, +0.0875] | 2/1/7 |
| F_Cverify_minus_F_local | +3.2285 | [+0.0000, +7.7094] | 3/0/7 |
| F_Vverify_minus_F_local | +3.0931 | [+0.0271, +7.7969] | 4/0/6 |

固定 10 个视频为重采样单位，10000 次、seed42；用于描述开发结果，不作确认性泛化声明。

## 替换与弃判

| 条件 | 接受替换／50 | 保留原因 |
|---|---:|---|
| F_Cverify | 5/50 | `{"preferred_base": 25, "accepted_alternative": 5, "undecided_tie": 6, "undecided_incomparable": 8, "undecided_insufficient": 6}` |
| F_Vverify | 5/50 | `{"preferred_base": 28, "accepted_alternative": 5, "undecided_insufficient": 8, "undecided_tie": 4, "undecided_incomparable": 4, "event_not_supported_B": 1}` |

完整 50 对中的 tie、insufficient、incomparable、技术失败或不满足准入条件均保留原候选。保留原结果不算 verifier 成功。全部替换记录在 all_accepted_replacements.json；逐次单独替换的 AP 差值不能相加作为联合替换贡献。

## 全部逐视频结果

| 视频 | F-local | 普通 verifier | 价值 verifier |
|---|---:|---:|---:|
| WxtbjNsCQ8A | 58.2222 | 65.2743 | 65.2743 |
| GsAD1KT1xo8 | 52.8194 | 52.8194 | 52.8194 |
| i3wAGJaaktw | 30.6389 | 30.6389 | 30.6389 |
| XkqCExn6_Us | 74.1771 | 78.4132 | 76.6771 |
| AwmHb44_ouw | 78.1771 | 78.1771 | 78.1771 |
| z_6gVvQb2d0 | 28.1042 | 28.1042 | 28.1042 |
| iVt07TCkFM0 | 78.4792 | 78.4792 | 78.4792 |
| gzDbaEs1Rlg | 69.9306 | 69.9306 | 70.0208 |
| XzYM3PfTM4w | 44.8958 | 65.8924 | 66.1840 |
| kLxoNp-UchI | 51.0208 | 51.0208 | 51.0208 |

## 预设的数值交换敏感性

| 条件 | 直接交换原分数 mAP |
|---|---:|
| F_local | 56.6465 |
| F_Cverify | 59.1698 |
| F_Vverify | 59.0344 |

相等分数与旧排序的并列处理可能使数值交换无法实现目标片段替换，详情保留在 evaluation.json。主规则在生成新指标前已固定，不按指标选择导出方式。

## 科学边界与成本

- 输出合法、片内引用和相对偏好不等于事实可靠；旧错误动作仍可能进入核验。没有将 8 对 v3 规则混入这 50 对。
- 这是“只用事实记忆、在 verifier 中作价值判断”的可执行接入结果；尚不是修好视觉幻觉的新模型实验，也不是原 40 视频结果。
- C 已有一般观看贡献判断；C/V 的区别是详细价值标准，不能解释为有价值与完全无价值的比较。
- 模型输入保持旧像素、PTS、事实及上限；本轮没有新帧、模型调用、回看、训练或边界改写。
- 缓存核验原成本：100 次、492778 token、11647.924 GPU 秒；新 CPU 接入实验消耗为 0 模型请求／0 GPU 秒。缓存复用不代表实际部署没有 verifier 成本。
- 16 项冻结源码 CPU 回归通过，官方 UMT 与独立指标核对通过；406 份历史绑定不变。

- [冻结协议](revalue_tvsum_fact_verifier_integration_protocol_2026-11-08.md)
- 逐视频 CSV（本地资料：`$MERIT_ROOT/comparisons/tvsum_fact_verifier10_integration_v1_2026-11-08/per_video.csv`）
- 全部替换（本地资料：`$MERIT_ROOT/comparisons/tvsum_fact_verifier10_integration_v1_2026-11-08/all_accepted_replacements.json`）
- 完整评价（本地资料：`$MERIT_ROOT/comparisons/tvsum_fact_verifier10_integration_v1_2026-11-08/evaluation.json`）
- 可运行源码（本地资料：`$MERIT_ROOT/experiments/revalue_tvsum_fact_verifier10_integration_v1`）
