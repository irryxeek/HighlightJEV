# TVSum固定10条：价值记忆读取修复执行记录

2026-11-07，用户授权只修复V读取，复用现有事实与价值记忆，保持模型、输入帧和token预算，在原10视频重跑FV，与已有D-1fps、F、旧FV比较。监督程序已于北京时间13:08启动；此文件记录执行条件，实际完成状态以运行账本和完成收据为准。

## 本轮唯一修改

原读取器优先把所有时间组的outcome、information装入V预算，后续维度大量未被读到。新读取器保留原正向／不确定／负向／比较记录的最低覆盖规则，再从仍能完整放入的记录中，依次按“已读维度数量最少、已读时间组数量最少、记录ID字典序”选择下一条。

记录原文、状态、来源事实、比较引用和最终按时间组显示的顺序不改。F文本和完整事实／价值库逐值保持一致。没有重新建库，没有新增取帧，没有改价值判据或让模型强制输出正向。

## CPU验收结果

13项回归测试在工作源码及冻结源码均通过；10条原生processor检查、grammar编译与执行前审查通过。每条完整提示与旧FV相比，只有V块变化；schema、图像像素处理结果、图片顺序、F和全部输入上限相同。

| 价值维度 | 旧FV读入记录 | 新FV-read读入记录 | 旧supported | 新supported |
|---|---:|---:|---:|---:|
| outcome | 80 | 31 | 13 | 2 |
| information | 75 | 35 | 38 | 21 |
| emotion | 9 | 40 | 0 | 2 |
| action | 8 | 40 | 1 | 15 |
| sensory | 1 | 31 | 0 | 10 |
| 合计 | 173 | 177 | 52 | 50 |

每视频均覆盖五维和全部8个时间组。supported是旧模型判断，不是人工正例；新策略没有以提高正向记录数为目标。旧V总token为9994，新V为10016，各视频仍≤1024；实际长度变化是读取内容变化的结果，没有提高预算。这些是CPU读取统计，不能视为准确率改善。

## 固定输入与执行边界

- 视频与顺序：WxtbjNsCQ8A、GsAD1KT1xo8、i3wAGJaaktw、XkqCExn6_Us、AwmHb44_ouw、z_6gVvQb2d0、iVt07TCkFM0、gzDbaEs1Rlg、XzYM3PfTM4w、kLxoNp-UchI。
- 同一Qwen3.8-27B revision、BF16、TP4、temperature=0、seed=0，原32768上下文引擎。新旧FV均用原78–83张选片图片；1fps观察信息来自已冻结记忆库，本轮未把新密集帧加给选择器。
- F≤1024、V≤1024、输出≤1536；逐视频输入token ceiling逐项沿用旧FV，十条总上限280357 token。只新增10次FV-read选择，零重试，不重跑对照。
- 一个四卡worker，运维墙钟上限1800秒另60秒清理，最多7440 GPU秒；只使用真正空闲GPU。不挪用旧实验额度。
- 旧记忆轮次190次／2024827 token／23765.300708 GPU秒，D-1fps轮次10次／627598 token／3317.211573 GPU秒，各自独立保留。本轮只单记新增选择成本。

## 自动收尾与比较

所属worker退出后，先冻结全10条预测再读标签，自动核验旧预测与指标完全一致。主比较FV-read−旧FV；次比较FV-read−F、FV-read−D-1fps。保存原生Top5mAP、rank-faithful及stable-tie敏感性、视频配对bootstrap与逐视频表。失败、未尝试及弃权保留全10分母并单列，不按结果换子集、改提示或自动扩样。

D-1fps仍一次读取144–394张源图片，其上下文长度与呈现不同；对它的差值是系统比较。新旧FV之间才是本次V读取策略的直接对照。

## 路径

- 冻结前源代码（本地资料：`$MERIT_ROOT/experiments/revalue_tvsum_value_read_v1`）
- 协议（本地资料：`$MERIT_ROOT/experiments/revalue_tvsum_value_read_v1/protocol.md`）
- 运行目录（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_read_10v_27b_v1_2026-11-07`）
- CPU输入检查（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_read_10v_27b_v1_2026-11-07/capacity.json`）
- 执行前验收（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_read_10v_27b_v1_2026-11-07/runner_review.json`）

结果报告预定为`$MERIT_ROOT/docs/revalue_tvsum_value_read_10v_results_2026-11-07.md`。未推送远程，原预测、源码、报告与账本均保留。

## 完成收据（13:16北京时间）

10/10次选择全部合法，finish_reason均为stop，无输出截断、无重试。worker退出0，所属进程组无残留；新增265856/280357 token，worker墙钟497.608秒，GPU生命周期1990.430秒。结束后重新核验6个完成产物与483个旧文件，哈希均一致，旧对照预测和指标精确复现。

原生Top-5 mAP：D-1fps 69.2479，F 57.3875，旧FV 54.4566，**FV-read 56.0212**。新旧FV差值+1.5646pp，6升1降3平，配对95%区间[−0.1597, 3.3549]；保留排序导出差值+1.5934pp，区间同样跨0。读取覆盖偏差已修复，但这批结果尚未证明稳定精度收益，点估计仍低于F和D-1fps。

- [完整结果报告](revalue_tvsum_value_read_10v_results_2026-11-07.md)
- 完成核验（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_read_10v_27b_v1_2026-11-07/completion_review.json`）

未自动启动下一轮实验，未改写本轮或旧轮预测，未推送远程。
