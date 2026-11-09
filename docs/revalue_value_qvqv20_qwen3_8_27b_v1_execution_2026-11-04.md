# Qwen3.8-27B 固定20条 Q / Q+V 执行记录（当前四卡运行）

日期：2026-11-04。用户指令“启动推理”。范围沿用最新32B实验：原固定清单前20条query、37个REZE Direct候选、74次Q/Q+V请求。候选、源像素/PTS、query条件、价值rubric、任务文本、schema与v2.4验收完全继承；新模型原生tokenizer/模板/处理器及运行环境变化均已记录。

## 准备与审查

模型为官方BF16 Qwen3.8-27B，revision `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`。下载18个权重分片，启动前重新核对32个文件SHA256。独立环境PyTorch2.10.0+cu128、Transformers5.8.0、vLLM0.19.1；185项依赖检查通过，旧环境未修改。

9项CPU回归通过；74个原始输入的视觉网格不变，Q/Q+V各对处理后的像素一致。最大输入5479token、输出上限2048、上下文8192，最小余量665。37套schema在CPU编译通过。禁止推理读取GT；每个固定请求在调用前记账，原文与引用去重审计保留。

## 三卡失败与四卡恢复

最初四卡v1完成准备，未派发。共享服务器当时只余三卡，因此v1.1以PP3、层数23/22/19在GPU0/1/3启动，权重加载成功且没有OOM。但首条正式请求出现反复`Failed to advance FSM`和`grammar rejected tokens`，未产出完整可提交响应。已停止派发、仅终止身份核实的本任务worker，全部所属进程退出。

该症状与[vLLM上游PP+结构化输出问题](https://github.com/vllm-project/vllm/issues/45014)高度吻合；不能将它解释为27B语义能力下降。三卡日志、源码、ledger与失败评价均保留。失败评价的零指标只是完整分母下技术失败处理，不能与模型正常预测的指标作能力比较。

三卡独立失败成本：1次尝试，无成功预测；实际token未收到完整usage，以6105token预留记账；GPU生命周期1012.900527837秒；1个worker，零自动重试。`actual_tokens=0`只代表已确认usage合计为0，不代表这次失败没有生成token或没有消耗。

北京时间00:30，GPU0–3已空闲，恢复原先冻结且从未执行过的四卡v1配置：TP4/PP1、BF16、单序列、eager、prefill512、显存比例0.85，无量化或CPU权重卸载。原四卡源码、输入和授权哈希不变。该变化绕开PP执行路径；其有效性以真实输出和运行日志为准。三卡失败成本单列保留，不并入或清零旧QV/TVSum/Direct账本。

## 输出与解释

当前四卡计划74次、每请求一次。三卡故障请求不作为有效预测拼接进当前结果。当前成功轮次与故障轮次的成本需合并披露；若四卡完成全部74次，本次启动工作的总尝试数为75（含故障1次）。没有额外语义提示、抽帧、回看或区间修改。

仅flagged算报警；insufficient为弃权，invalid为技术/契约失败。IoU<0.5仅是定位错误代理，人工语义核验为0。全部37候选/臂保持分母，不能把报警能力当作grounding区间提升。

所有GPU进程退出后自动冻结预测、CPU评价并生成同20条8B/32B/27B对照。此文为执行记录，当前完成数请读取实时status/ledger，不把启动记录当成实验完成证据。

## 产物

- 当前四卡运行：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv20_qwen3_8_27b_v1_2026-11-04`。
- 实时状态：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv20_qwen3_8_27b_v1_2026-11-04/status.json`。
- 请求与原始响应：`ledger.json`、`records/`。
- 日志：`worker_0/worker.log`。
- 运行恢复依据及旧成本：`runtime_recovery.json`。
- 三卡失败：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv20_qwen3_8_27b_v1_1_2026-11-04`。
- 完成后自动报告：`docs/revalue_value_qvqv20_qwen3_8_27b_v1_results_2026-11-04.md`。

本轮未推送远程。

## 正式输出启动核验

北京时间00:34:30，四卡首条 `qv_2781_w01__Q` 正常完成，4057个输入token、556个输出token、61.11秒；原始响应及去重/引用审计已保存，输出契约通过，CPU与运行时输入token绑定一致。后续Q+V已派发，任务继续后台运行。核验时没有出现三卡的FSM报错；此项仅确认运行正常，不代表科学指标已通过。启动收据：当前运行目录 `startup_verified.json`。
