# ReVALUE 32B Q/QV：取消额度后固定100条重跑记录

> **最新更新：用户已将本轮缩小为原清单前20条query（37候选、74次判断）。** 已启动独立CPU停止控制器，保留当前推理进度；主结果以20条报告为准。下文100条为早先启动记录。


用户最新指令：**“请取消额度限制，重新跑一下该任务，跑100条”**。本次为新目录内完整重跑，不拼接旧20条部分结果，不重置历史成本。

## 当前状态

北京时间2026-11-03 **11:45:04** 启动后台调度和CPU自动收尾；11:45:13已核验GPU **0、2、3** 的UUID及顺序，开始加载模型。此段是启动快照，不代表完整100条已完成；后续收据以本报告末尾与运行目录为准。

- 模型：Qwen3-VL-32B-Instruct BF16，TP1/PP3，一个持续运行worker。
- 任务：固定100条query清单，139个合法base候选×Q/QV=278次判断。2条无合法base区间的query保留在100条分母中，不创造额外区间。
- 取消请求额度、累计token额度、worker启动额度、单worker/累计GPU时限、排队时限；不因用量阈值自动中止。
- 保持原8192上下文、2048输出上限、prompt/schema、旧帧、query契约、价值rubric、去重与验收规则；这些是实验条件，不是累计资源额度。
- 按固定清单结束；模型错误、文件漂移或所属进程异常仍保留失败并停止，无自动重试、不干预其他用户进程。

## CPU验证与冻结

152项CPU测试通过，ruff通过。回归包括模拟worker运行100001秒、累计300003 GPU秒仍能完成，以及全部278请求、防重复、真实CPU子进程归属及退出竞态。全278条token IDs/视觉网格与原版本一致，98份旧帧数组完成哈希核对，最小上下文余量612token。模型26份文件完成SHA核验，没有在CPU准备时载入权重。

合同、rubric、评价与8B比较代码字节不变。全部3125个历史文件/收据哈希核验通过，原预测、源码、账本和结果报告保留。CPU审查由主助手完成，不声称独立审查。

## 独立记账

| 运行 | 已记录请求 | token | GPU生命周期 |
|---|---:|---:|---:|
| 历史32B v1启动失败 | 0 | 0 | 实际未知；原账保守4500 GPU秒 |
| 历史32B v1.1部分完成 | 20（19合法、1invalid） | 82736 | 9393.103510 GPU秒 |
| 本轮v1.2 | 后台持续记录 | 后台持续记录 | 三卡完整墙钟×3，无额度中止 |

旧QV、TVSum、Direct及8B等记录保持独立。取消本轮额度不抹去任何历史成本。按上次20次调用平均约152.5秒粗估，本轮完整278次约12小时；这是估算，不是超时阈值，实际受输出长度和服务器负载影响。

## 自动收尾与产物

所有所属进程退出后，后台CPU finalizer冻结响应/账本并评价一次，自动保存Q/QV合法率、报警precision/recall、配对变化、与冻结8B对比、完整失败及实际成本。IoU为错误代理，独立人工语义标签为0；本实验没有修改grounding边界，不称为定位精度提升。

- 重跑协议（本地资料：`$MERIT_ROOT/experiments/revalue_value_ablation_32b_v1_2/protocol.md`）
- CPU审查（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_2_preparation_2026-11-03/runner_review.md`）
- CPU测试收据（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_2_preparation_2026-11-03/cpu_test_receipt.json`）
- 运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_32b_v1_2_2026-11-03`
- 结束后结果报告：`docs/revalue_value_qvqv100_32b_v1_2_results_2026-11-03.md`（生成前不是已完成结果）
- 结束后完整归档：`comparisons/qwen_direct/value_qvqv100_32b_v1_2_2026-11-03`

调度PID28562，CPU收尾PID28563，模型worker PID29742；PID仅作启动快照，实际归属以运行目录收据和创建时间核对。
冻结manifest SHA256：`834b15b9a02cc1c14564132cc092b5d317ea0dfc6e65dfb2fc4b4b659e050962`。
本轮未推送远程。

## 首条实机响应核验（11:49，北京时间）

首条 `qv_2781_w01__Q` 已完成且通过契约，输入4031token、输出758token、实际推理181.17秒，以stop正常结束。随后第2条QV也已完成并通过契约，保存核验收据时第3条正在生成。此次为实际模型结果，不是CPU模拟；当前尚未完成全278次，不能据此给出完整Q/QV指标。

后台supervisor及CPU finalizer存活且PPID=1，三卡UUID、模型worker和所属子进程心跳正常。时限与累计额度字段全部null，冻结源码未变，输入文件与32B v1.1字节相同，旧32B账本哈希未变。首条核验收据（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_2_preparation_2026-11-03/first_generation_receipt.json`）。
