# TVSum 1 fps 记忆测试：固定10条执行记录

## 最新范围

用户要求增加观察密度，并明确“刚启动的那组就不保留了，用1fps记忆测试”，随后将原40条范围缩为“先测10条”。本轮取原40冻结清单前10条，不按指标或成功状态筛选，不自动扩到40条。

## 三组与输入

| 组 | 最终选择器读取 |
|---|---|
| D-detail | 原有图片、原B0候选提示，无文字记忆 |
| F-1fps | 相同图片和候选＋1fps建立的事实记忆 |
| FV-detail-1fps | 相同图片和候选＋同一事实记忆＋详细价值记忆 |

三组共用详细价值判据、模型和导出规则；F/FV的事实完全共享。模型仍为原Qwen3.8-27B，BF16、TP4。每秒采一帧，旧8个时间组按旧相邻组的观察中点分界；共2,024帧，每视频105–354帧，每组13–45帧。1fps组用于建库，最终选片仍使用原64全片采样及旧候选图像，像素和顺序不变。

事实和价值写入输出各1024token，最终选择1536；读取F/V各1024，上下文32768。提高密度增加实际输入token、读帧量和GPU耗时，不能称总计算量不变。原事实写入器还会返回简短价值字段，保留以维持原契约，但最终FV使用后续详细价值写入结果。

## 执行

最多190次尝试＝80事实写入＋80详细价值写入＋30选片，零重试，一次四卡worker，等待真正空闲GPU；worker最多10800秒另60秒清理。总token经CPU全量检查后写入独立authorization.json；所有旧轮次账本不挪用。素材CPU审计与48项单元测试已通过；本条为准备快照，后续状态以实际status.json为准。

结束后自动冻结预测、确认所属进程退出，再用CPU评价。完整10条分母，报告原生Top-5 mAP、排序及同分敏感性、配对区间、各臂合法率、记忆保留条目及成本。失败/未尝试/弃权保留B0并单列；允许负结果，不强迫高光或胜负。

## 被替换的旧任务

旧稀疏价值对照按用户指令中止：110/720次尝试，已知实际740,014token，含中断预留计744,639token；GPU生命周期11,805.439588秒，所属进程已退出。旧监督器自动finalizer将状态写成complete/completed720，这是收尾/回退导出完成，不是完成720次推理；新增user_cancellation_receipt.json明确该实验不完整，不用于本轮主比较。没有修改旧预测、账本或失败输出。Mr.HiSum既有任务继续运行。

40条版本仅开始CPU素材准备、未加载模型；缩到10条后结束其CPU任务，保留superseded_before_inference.json。该40条准备新增模型调用、GPU秒均为0。

## 结论边界

主比较FV−D，次比较F−D、FV−F。对D的差值是“密集观察＋记忆”的系统收益，D没有同样的密集建库成本；不能声称同读帧量的纯记忆结构收益。旧F-read/FV仅作描述性参照，其选片判据也与本轮不同，不能将差异都归因于1fps。旧8组、记忆容量及候选域保持不变，压缩和候选覆盖仍可能限制效果。10条属于已用于开发的子集，不能代表TVSum全量泛化。

- 固定协议（本地资料：`$MERIT_ROOT/experiments/revalue_tvsum_dense_memory_v1/protocol.md`）
- 运行目录（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_dense_memory_10v_27b_v1_2026-11-06`）
- 旧轮次中止收据（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_detail_40v_27b_v1_2026-11-06/user_cancellation_receipt.json`）

预定结果报告：`$MERIT_ROOT/docs/revalue_tvsum_dense_memory_10v_results_2026-11-06.md`。本次未推送远程。

## 启动收据

2026-11-06 20:47（北京时间）已启动独立监督进程PID 36633，使用GPU 4,5,6,7，开始加载27B模型。48项冻结源码CPU测试通过，108个schema编译通过，最大上下文29674；本轮绝对token预留2,193,447。源码与输入已冻结，未复用被中止任务的剩余额度。

本记录为启动快照，不是完成报告。实际请求进度见status.json（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_dense_memory_10v_27b_v1_2026-11-06/status.json`），实际成本见ledger.json（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_dense_memory_10v_27b_v1_2026-11-06/ledger.json`）。
