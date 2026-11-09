# TVSum 旧理由可见性对照：执行记录

日期：2026-11-08。状态：100 次调用及 CPU 汇总全部结束；99 条合法、1 条规则拦截，零重试。原启动记录保留如下。

## 已完成的运行前验证

- 40 项 CPU 测试通过（19 项契约 + 21 项收尾/评价），独立测试退出 0。
- 两分片共 17 个源码文件，冻结哈希完全相同；旧 rows/pairs 逐字节复用。
- 50 对候选 × 两组 = 100 个冻结请求。所有旧输入帧像素、processor 网格、PTS、F 与五维价值 rubric 一致。
- 原生提示 4512–5800 token，输出最多 1536，总上限 16384；无需截断或新增帧。
- 运行前新增模型调用与 GPU 秒均为 0；本轮不挪用旧额度。

## 启动与上限

- 主进程启动收据：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_reason_visibility10_27b_v1_2026-11-08/launch_receipt.json`。
- 北京时间 2026-11-08 00:37:57 启动；0–3、4–7 两组空闲 GPU 分别运行原 5 条视频。
- 总计最多 100 次尝试、零重试、1638400 token、2 个 TP4 worker。每个 worker 含退出最多 3600 秒；累计 28800 GPU 秒。
- 原候选位置和排序保持不变；不扩展 30 条，不导出新排名或 mAP，不推送。

## 冻结摘要

| 分片 | Manifest SHA256 | CPU review SHA256 |
|---|---|---|
| verify_0 | aae40d3a6e05561a534aa60d007b3644acab92601601832d191190bd3f7946d2 | 1781379d09b2e7914d4d7dda73b46cf9da15ba7d51b5e9d9bbff88699536411b |
| verify_1 | e73654c5e32856ad1929db9ba6e528e9024890fb4928c0a25c039a86911213a4 | b6fccb6c48e44bae80150830c7a5fe49c827ee8188a3bd8bf6defae5960df704 |

## 独立审查与预设案例

- 审查：`comparisons/tvsum_reason_visibility10_v1_2026-11-08/source_review.json`。
- 运行前固定 8 个历史问题片段：`comparisons/tvsum_reason_visibility10_v1_2026-11-08/case_review_plan.json`。包含全部 6 个旧理由报警片段和 2 个 GsAD 事实错误片段；不按新成绩选案例。
- 结构修复不能证明视觉事实正确；保留理由还会增加理由核验及可能的反证输出负担，隐藏组并非移除 F 中所有相关叙述。

## 完成收据

- 两个 worker 均退出 0，无所属进程残留；100 次额度已用尽。
- 实际 575015 token、15175.393978 GPU 秒。
- 正式结果保留 partial_or_invalid 标记（1 条 guard invalid），无未尝试请求。
- 112 个历史／输入哈希复核通过；CPU 收尾新增模型调用为 0。
- 分析与语义边界见 [实验分析](revalue_tvsum_reason_visibility10_analysis_2026-11-08.md)。
