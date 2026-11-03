# ReVALUE Q/Q+V v2.1：字段联动修复的固定 QV100 对照

## 授权与范围

日期：2026-11-01。Origin Skill：academic-research-suite / experiment-agent，run。
最新用户指令：“测试一下，看看效果”。该指令授权测试此前已完成的 state/unknown_reason 生成约束修复。数值上限是按完整既定样本设定的实施边界，不冒充用户逐字提供的数值。

原 v2 与修复准备记录中的未授权状态均保留，不能用旧准备状态覆盖本次新指令，也不将旧预算转入本轮。无推送、训练、依赖/模型变更或其他数据集补跑。

## 唯一科学干预

在原相同 100 条 query 上执行 Q、QV 各 139 个候选，共 278 次。两条原 base 无候选 query（9160、2498）保留在 100 条总清单，不造候选。沿用原清单顺序和交替先后顺序；不按 GT、旧表现或无效类别挑子集。

唯一修改是生成 JSON schema 内 state/unknown_reason 的关联：supported/contradicted 只允许 null，unknown 只允许既有具体原因。已通过 66 项 CPU 测试、139 候选语法检查、真实 Qwen token 检查。修复的 contract.py 与已有 CPU 修复收据绑定。

相对于旧 v2，所有请求字段逐项相等，仅 output_schema 和包含它的 request_sha256 改变。保留 query 条件、提示文本及长度、旧像素/PTS/区域/次序、模型版本、采样、事实与引用规则、依赖逻辑、区间/分数/排序、评价。新的运行路径、授权绑定、协议文档和完成后旧/新比较是运行管理差异，不进入模型输入。约束解码可能改变随后生成的状态和事实，不能将效果仅解释为格式修补，更不能把 CPU 接受性当成新预测。

本轮仍为语义 verifier，无边界修改、回看、记忆、ROI、音频、价值体系重写或新的 query 条件。

## 独立资源上限

| 项目 | 上限 |
|---|---:|
| 正式尝试，含失败 | 278（Q 139，QV 139） |
| 重试 / 额外故障请求 | 0 / 0 |
| 绝对 token | 3,416,064 |
| 每请求上下文 / 最多输出 | 12,288 / 2,048 |
| 同时 GPU | 1 张空闲 RTX 4090 |
| worker 启动 | 28；每个 10 次，最后 8 次；失败启动计数 |
| 每 worker GPU 生命周期 | 600 秒，含加载、生成、清理 |
| 累计 GPU 生命周期 | 16,800 秒 |
| 一次队列期限 | 86,400 秒，每 30 秒检查；不重置 |

沿用 Qwen3-VL-8B-Instruct 修订 0c351dd01ed87e9c1b53cbc748cba10e6187ff3b、vLLM 0.12.0、bf16、单卡 eager、temperature=0、seed=0、thinking 关闭和旧引擎参数。已存在的本地环境与权重，不下载或新增付费 API。

每次先预留输入与输出上限，实际 token 可核实时按实际计账；未知失败保留预留。剩余 token/GPU 不换成额外请求。旧 v2 保持 278/278、28 worker、1,336,978 token、5,008.974413305987 GPU 秒；所有其他旧账独立。

## 执行与停止

先完成 CPU 输入对照、源码复核和快照冻结，再将当前指令绑定新 manifest 与上限。prepare 不读取 GT 或旧模型响应；仅对历史结果文件做哈希保护。runtime 仍检查源文件/输入/模型/环境和请求摘要，只有冻结 source_snapshot 入口可运行。

GPU 必须无计算进程、显存低于 512 MiB、利用率低于 5%，且 PCI/UUID 映射一致。没有空卡只做 CPU 等待；不干预其他进程。单次队列与防重复锁，不启动重复实验。

源码/输入/配置漂移、OOM/运行异常、启动失败、累计或单 worker 超时、所属进程清理不确定时停止，保留失败，不重试或降级。普通输出 invalid 保存后继续固定清单；不按指标提前挑选或追加样本。

## 评价与修复前后比较

所有 worker 退出且预测、账本冻结后，CPU 评价一次，并与原 v2 已冻结评价配对。旧结果只读；不修写旧 invalid，也不重新调用旧评价器。

完整报告两臂各 139 个候选、100 条 query 的合法率、各失败类别、supported/insufficient/flagged、IoU<0.5 代理 precision/recall/误报及既有敏感性指标。特别分开 old invalid→new valid 和两轮均合法的语义变化，不能把恢复输出直接称为新增正确反例。保留运行失败和未尝试项；未完整执行时明确部分结果。

原探索门槛原样保留：至少 138/139 合法、precision≥80%且高于错误基率、recall≥30%、误报≤10%、insufficient≤40%、至少 20 个报警。另检查格式矛盾是否减少、是否只增加 unknown、确定判断与代理筛查是否改善。无独立人工语义标签，低 IoU 不等于真实事件错误，不声称定位或内在价值判断准确率提高。

## 独立产物

- 原始目录：$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_1_2026-11-01
- 开发源码：$MERIT_ROOT/experiments/revalue_value_ablation_v2_1
- 准备记录：$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_1_preparation_2026-11-01
- 完成归档：$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_1_2026-11-01
- 完成报告：$MERIT_ROOT/docs/revalue_value_qvqv100_v2_1_results_2026-11-01.md

后台 CPU 收尾器自动生成本轮评价、修复前后比较和归档；失败不重复运行。准备或排队不称为已有实验效果。
