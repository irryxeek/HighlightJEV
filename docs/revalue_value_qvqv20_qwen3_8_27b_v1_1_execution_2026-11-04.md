# Qwen3.8-27B 固定20条 Q / Q+V 启动记录

2026-11-04。用户要求“启动推理”；本轮沿用最新32B固定20条query的比较范围，37个REZE Direct候选、74次Q/Q+V判断。此文是启动快照，实时状态以运行目录中的status.json、ledger.json、worker退出收据为准。

## 已完成准备

- 官方BF16权重18分片、总32文件已下载；启动前重新核对全部文件SHA256，没有反序列化加载到CPU/GPU。
- 独立环境：PyTorch2.10.0+cu128、Transformers5.8.0、vLLM0.19.1。185项依赖检查通过；复用旧环境同版本CUDA库的独立副本，旧环境未修改。
- 冻结源码及输入后，9项CPU回归通过，包括固定清单、禁止重复调用、GT隔离、引用验收及仅flagged算报警。
- 原始像素、PTS、候选、query、条件、价值rubric、任务提示与v2.4契约不变。74/74视觉网格与旧输入一致，Q与Q+V每对处理后的像素张量一致。
- 新模型原生tokenizer/聊天模板/处理器使用记录保留。最大输入5479token，输出上限2048、上下文8192，最小余量665；37套schema CPU编译通过。

## 当前运行配置

四卡v1准备已冻结但未启动，正式请求为0，原目录保留。由于共享服务器空闲情况变化，本轮v1.1采用物理GPU0、1、3三卡PP=3/TP=1、层数23/22/19、BF16、单序列、eager、prefill512、KV512MiB/rank，无CPU权重卸载或量化。模型输入与四卡准备完全一致；运行配置的变化在manifest中逐项记录。

北京时间00:23后台supervisor和worker已启动，GPU UUID与NVML检查通过，模型架构正确识别为Qwen3_5ForConditionalGeneration。记录此启动快照时仍在权重加载阶段，不能据此宣称已完成任何正式预测或已有性能结果。

## 结果与使用记录

每个固定请求只执行一次，零自动重试；沿用取消资源额度的用户偏好，完整记录实际token及多卡生命周期，不挪用旧实验账本。invalid保留并继续，真实运行错误停止；没有准确率触发的筛选。所有GPU进程退出后自动冻结响应、CPU评价及与同20条8B/32B比较。

仅flagged计错误报警，insufficient为弃权；IoU<0.5仍只是定位错误代理，独立人工语义核验为0。verifier不会修改Direct边界，不能将报警率变化当成grounding提升。

## 产物

- 运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv20_qwen3_8_27b_v1_1_2026-11-04`。
- 实时状态：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv20_qwen3_8_27b_v1_1_2026-11-04/status.json`。
- 逐请求账本和原始响应：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv20_qwen3_8_27b_v1_1_2026-11-04/ledger.json`、`records/`。
- 模型日志：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv20_qwen3_8_27b_v1_1_2026-11-04/worker_0/worker.log`。
- 冻结协议：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv20_qwen3_8_27b_v1_1_2026-11-04/source_snapshot/protocol.md`。
- 源码：`$MERIT_ROOT/experiments/revalue_value_ablation_qwen3_8_27b_v1_1/`。
- 完成后自动生成：`docs/revalue_value_qvqv20_qwen3_8_27b_v1_1_results_2026-11-04.md`。

本轮未推送远程。
