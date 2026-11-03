# ReVALUE Q/Q+V v2.1 修复验证执行记录

北京时间 2026-11-01 22:56 已启动独立后台队列和 CPU 收尾器。最新用户指令：“测试一下，看看效果”。

## 当前快照

状态：**等待空闲 GPU**。已确认 supervisor 和 finalizer 进程存活；当时 8 张 GPU 均在使用中。
请求 **0/278**，模型 worker **0/28**，GPU 分配 **0**，尚无新预测或修复效果指标。排队状态不能称为完成实验。

拿到空闲卡后自动开始，单卡顺序执行。依据上轮约 84 分钟的实际 GPU 生命周期，预计运行约 80–100 分钟；等待 GPU 的时间不计入该估计。队列仅一次，最长 24 小时，不自动续期。

## 固定范围

完整保留 100 条 query，其中 98 条有 139 个原 REZE Direct 候选，Q/QV 各调用一次。两条无候选 query 保留在总体分母。不选择性重跑失败项。

唯一科学变量是 state/unknown_reason 生成 schema 联动。278 条提示文本、token 元数据、像素/PTS/区域、query 条件、候选区间和顺序、模型、采样、引用/逻辑校验、原评价均保持一致。worker、supervisor 和 evaluator 与 v2 逐字相同，运行目录/当前授权绑定及完成后比较模块单独版本化。

## 已完成准备

- 完整 CPU 测试 **76/76 通过**；Ruff 检查、格式检查通过。
- 复用已通过的 139 候选语法与真实 Qwen token CPU 验证，源码哈希一致。
- 278 条请求逐项核验仅 output_schema 与 request_sha256 改变。
- 98 份旧像素数组哈希一致；855 份历史源文件、预测、账本和结果受哈希保护。
- 最大输出 2,048 token，最小上下文余量 4,782；完整输入加最大输出预留 1,770,626 token。
- 新源码与输入已冻结，当前用户指令绑定 manifest；旧未授权准备快照保留。

## 资源与自动收尾

独立上限：278 次尝试、零重试/额外故障调用、3,416,064 token、28 次 worker 启动、同时最多 1 卡、单 worker 600 秒、累计 GPU 生命周期 16,800 秒。无旧额度转入，不干预其他进程。

全部终止、账本及响应冻结后，CPU 评价器执行一次；随后与旧 v2 的冻结评价比较，自动归档。报告包括两臂修复前后的合法率、invalid/insufficient/supported、报警/TP/FP、召回与误报，并单列 invalid→合法恢复和两轮均合法的语义变化。IoU 是错误代理，恢复合法不等于语义变准。未完成时保留完整失败分母，不报告虚假的完成结果。

## 路径

- [本轮协议](revalue_value_qvqv100_v2_1_protocol_2026-11-01.md)
- 准备与收据（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_1_preparation_2026-11-01`）
- 原始运行：$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_1_2026-11-01
- 完成后报告：$MERIT_ROOT/docs/revalue_value_qvqv100_v2_1_results_2026-11-01.md
- 完成后归档：$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_1_2026-11-01

本记录是启动时快照。后续进度以运行目录 status.json、ledger.json、退出与完成收据为准，不根据此静态快照重复启动。没有推送远程。
