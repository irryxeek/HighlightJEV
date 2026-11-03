# ReVALUE Q / Q+V 固定 QV100：实现、冻结与排队记录

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent，run。
- 日期：2026-10-31；本记录为启动时快照，不是最终结果。
- 最新真人授权：“按这个方案实现，先在固定的100条query上跑一下Q和Q+V的对照测试。”
- 状态：**实现和 CPU 准备完成；最初排队核验为 0/278，随后 GPU 4 释放，已进入真实推理。**
- 科学效果仍未验证。原候选、旧帧、旧预测和所有旧预算保持独立。

## 1. 本轮实际实现

源码目录（本地资料：`$MERIT_ROOT/experiments/revalue_value_ablation`）包含共享条件/证据契约、Q/QV 提示、CPU 准备、受限运行器、一次性队列、退出后评价及自动归档。

- 固定 100 个 query；98 个有候选，共 139 个原 REZE Direct 区间。两臂各 139 次，总计 278；空 base 的 9160、2498 保留在总体统计。
- 原 query 的条件清单共 302 项、153 条依赖边、最多每条 5 项。由助手仅依据 query 编写并复核；**不是独立人工语义标注**。原文歧义及修订来源保存在编写记录（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_preparation_2026-10-31/query_contract_authoring_review.md`）。
- 按清单映射，action/sensory/information/emotion/outcome 分别适用于 83/53/27/5/5 个 query。不能为增加维度覆盖而新增要求。
- Q 与 QV 使用相同候选、像素、帧次序、PTS、条件、输出 schema、模型和控制器；QV 只附加已适用维度的证据判断细则。
- qid 448、1869 没有适用的五维条件，两臂提示完全相同。仍各调用一次，作为预先确定的一致性参照，不计算有利子集成绩。
- 不新增边界判断、回看、记忆、ROI 或重排，不改 Direct 的区间和分数。

## 2. CPU 验证与冻结

64 项合成/CPU 测试通过，Ruff 检查通过。覆盖完整分母、三值逻辑、引用与依赖、同输入配对、队列防重复、预算、退出归属、GT 读取时机及失败保留。另有 XGrammar 编译与 mock worker 集成检查；这些不代替真实 GPU 运行。

对 139 个候选完成实际本地 processor 的双臂输入测量，全部 schema 检查通过。未加载模型权重、未初始化 CUDA、未新增源视频帧，未读取 GT。

| 准备项 | 实测值 |
|---|---:|
| Q 总输入 token | 585,622 |
| QV 总输入 token | 615,660 |
| 每请求输出上限 | 2,048 |
| 完整运行输入+最大输出预留 | 1,770,626 token |
| 最小上下文余量 | 4,782 token |
| 受保护旧产物 | 274 个，哈希一致 |

在运行前的 CPU 审查中发现 16,384 上下文超过旧 2 GiB KV 配置的理论容量，已改成 12,288。没有为这项修订发生模型尝试或 OOM。初次 lint 的 3 项 import 排序问题已在冻结前修复；最终 64 项测试与实际快照哈希一致。

- 冻结 manifest：`6199daee1ec802629781e72fb1b09b86705ff35b1b28a2c6ccc14dc24e40d656`。
- 授权绑定：`91a2227206256086ba30e1347df036aecedff3f4d3afea370557d6c54e78abef`。
- CPU 准备及冻结收据（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_preparation_2026-10-31/cpu_freeze_receipt.json`）。
- 源码复核（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_preparation_2026-10-31/runtime_independent_review.json`）与追加复核（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_preparation_2026-10-31/review_addendum.json`）。

## 3. 授权、排队与自动收尾

2026-10-31 03:43:26 UTC（北京时间 11:43:26）启动本地 CPU supervisor（PID 1962）和 CPU finalizer（PID 1963），均已脱离终端并确认存活。启动核验时全部 GPU 被占用，状态为 `queued_waiting_for_idle_gpu`，无模型 worker、无推理账本、无实验 token/GPU 消耗。

运行器每 30 秒检查空闲卡。只有显存和占用符合协议且设备身份核验通过才派发，最多同时一卡。单次队列最多等待 24 小时；不能重复启动、重置或自动重试。等待期间不会加载权重或占用 GPU。

续记：03:44:28 UTC（北京时间 11:44:28）GPU 4 释放，第一批 worker 自动开始。加载前实际 CUDA UUID 与目标一致；模型成功加载，vLLM 实报 KV 容量 14,560 token，与 CPU 估算一致。首批已产生真实输出；`complete` 只表示通过契约，`invalid` 原样保留并继续固定清单，不在运行中修提示或重问。此处不是最终进度；以运行账本和终态收据为准。

独立硬上限：278 次尝试、零额外故障尝试/零重试、3,416,064 token、28 个 worker、每 worker 600 秒、累计 GPU 生命周期 16,800 秒。它们是实现完整已授权范围的运行上限；没有挪用旧 QV/TVSum/Direct/verifier 余额。

完成或发生终止事件后，CPU 收尾程序要求所属 worker 退出有据，先冻结响应，再读取 GT 并单次评价。它会保存两臂筛查指标、状态与条件变化、成本、相同提示一致性、完整失败和 100-query 清单。没有模型派发的队列到期只保存未执行报告，不伪造结果。

## 4. 查看真实进度与续接

运行目录：revalue_value_qvqv100_v2_2026-10-31（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_2026-10-31`）。优先读取 `status.json`、`supervisor_started.json`、`ledger.json`（派发后才有）、`worker_*/exit.json`、`campaign_exit.json` 与 `cpu_finalizer_complete.json`。不要把本文件的 0/278 或准备快照里的 false 当作未来实时状态。

已有排队/收尾进程，**不要再次运行启动命令**。若进程失败，先保留退出/失败证据并诊断，不能复用已经尝试的请求或自动重启。同名目录及锁防止重复运行。

完成后预定生成：

- 报告：`$MERIT_ROOT/docs/revalue_value_qvqv100_results_2026-10-31.md`。
- 归档：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_2026-10-31/`。

[完整冻结协议](revalue_value_qvqv100_protocol_2026-10-31.md)。IoU 是错误代理，不是独立语义真值；原区间未修改，不能据此宣称 grounding 性能提升。此次未推送。
