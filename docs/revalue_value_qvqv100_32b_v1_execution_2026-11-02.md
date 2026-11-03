# ReVALUE 32B 固定100条验证：执行状态

快照时间：2026-11-02 22:35:26（北京时间）。**准备及后台调度已完成，当前排队，实际模型推理尚未开始。**

## 本轮范围

- 使用已下载并完成14/14权重分片校验的Qwen3-VL-32B-Instruct BF16。
- 原固定100query，139个REZE base区间，Q与Q+V共278次正式请求，零重试。
- 旧帧、像素、PTS、query contract、候选、提示词、schema、价值rubric及去重契约不变；不改边界或排序。
- CPU重新处理278请求，token IDs全部与8B相同；最长5532输入+2048输出，8192上下文尚余612。
- 模型/必要运行参数改变是本次条件；不能解释为参数数量的纯因果实验。

## 验证与冻结

145项CPU测试、Ruff及独立源码审查通过；23个源码文件的测试/审查/manifest哈希一致。
保留2946个历史文件的哈希，原8B账本及评价未变；本轮建立独立账本。

- Manifest SHA256：`783bc2af7c5d11d1111fa930b4b71d3e6c2f7fb31dfee3fb10c366ad516add79`。
- 冻结协议（本地资料：`$MERIT_ROOT/experiments/revalue_value_ablation_32b_v1/protocol.md`）
- CPU准备收据（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_preparation_2026-11-02/cpu_input_freeze_receipt.json`）
- 源码审查（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_preparation_2026-11-02/runtime_source_review.md`）
- 队列准入快照（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_preparation_2026-11-02/queue_admission_receipt.json`）

## 当前调度

GPU2、3空闲，其余卡有占用；尚不足三卡组。CPU supervisor PID5721、CPU finalizer PID5722均独立后台会话存活。
本快照新增模型调用0、token0、GPU分配/秒0、模型worker0、重试0。
三张卡同时符合空闲条件后自动启动一个TP1/PP3组；分层固定21/22/21。六张符合条件时最多两组，不抢占其他用户。
排队期限为首次dispatch起24小时；超时结束，不自动续期或重启。

独立上限：278尝试，2,277,376 token，14 worker，每worker3卡/1500墙钟秒，最多6卡并发，累计63,000 GPU秒。
这些是上限而非预期消耗。每组加载、推理、退出/清理按墙钟×3计费；OOM或运行失败停止新请求，无自动配置回退/重试。

## 结果与限制

真实32B装载、PP通信和效果尚未验证；CPU通过不代表三卡一定不OOM。
完成并确认所属模型进程退出后，自动冻结预测、读取GT、评价一次，生成Q/QV及8B同政策对照报告。
完整分母保留失败/未尝试；IoU仅作错误代理。没有新增推理样本、旧预算转移或远程推送。

运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_32b_v1_2026-11-02`。
预计结果文件：`$MERIT_ROOT/docs/revalue_value_qvqv100_32b_v1_results_2026-11-02.md`（本快照尚未产生）。
实时状态以运行目录的status.json及账本为准，本文件是不可回填成成功的启动快照。
