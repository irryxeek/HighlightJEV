# TVSum高光价值与记忆：27B三臂实验当前执行记录v1.1

## Material Passport

- Origin Skill / Mode：academic-research-suite / experiment-agent，run，2026-11-04。
- 用户指令：“按该方案开始执行推进”。依据[11月4日修订方案](revalue_next_experiment_plan_2026-11-04.md)。
- 当前状态：CPU审查、来源与输入冻结完成，修订版后台监督器已启动；最终结果未完成。

## 范围与对照

完整固定TVSum val10，三组共用Qwen3.8-27B BF16、同一批79–84张旧帧／真实PTS、通用高光任务及输出规则：

| 条件 | 记忆输入 | 最终选择请求 |
|---|---|---:|
| D | 无文本记忆 | 10 |
| F | 事实／事件上下文 | 10 |
| FV | 同一F＋五维价值证据 | 10 |

共享初始化为每视频8次、共80次，总计划110次。主比较FV−F；不把相对历史8B B0的差值单独归因于记忆。三组均可从全片2秒网格重新选片，允许原Top-5之外的片段、并列和合法弃权。

## 已通过的准备与修复

全片64采样点与原候选帧均来自B0已见源时刻；RGB／PTS逐项核对，通过84个旧chunk及其历史冻结收据绑定。未重新采样新的源时刻，未加入音频、标题或标签。

v1.1实际CPU冻结已证明：**全部110份请求定义与rows、引擎配置逐项等于v1；prompts.py和contract.py逐字节相同**。71套schema编译通过；最长上下文保守预留23,532/32,768token。

41项CPU回归通过，包括模拟真实`worker.call → engine.generate`调用路径、采样类型解析、进程祖先归属、已登记启动时间、PID复用拒绝、终结故障标记清理、未提交／截断响应隔离及三臂输入与评分契约。此模拟使用CPU mock，**不是新增模型预测**。

派发前导入作用域错误已修复；采样类型在实际调用函数内解析、预留前构造。监督器以祖先关系及启动时间识别所属进程，不再要求每个vLLM子进程保留可读环境标记。代码审查为共享上下文协作审查，独立人工语义验证仍未完成。

## 旧失败与记账

[旧v1启动记录](revalue_tvsum_highlight_memory_27b_v1_execution_2026-11-04.md)及原始产物完整保留。v1在`engine.generate`调用前NameError，没有实验模型API调用或响应；其旧record的提前`model_called`标志不表示实际派发。

旧预留尝试为1次、2,998记账token、1,578.298624 GPU秒、1个加载worker；外部核验后全部7个所属进程释放，退出码未知如实记null。v1.1另建账本，正式模型调用至多110次、零模型输出重试；合计披露时必须包含旧加载开销，不能只报新轮。没有挪用旧QV、TVSum或Direct资源账本，也没有重新设置用户已取消的任意token／GPU硬额度。

## 当前入口与完成产物

当前运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_highlight_memory_27b_v1_1_2026-11-04/`。

- `manifest.json`、`authorization.json`、`runner_review.json`：绑定用户授权、完整输入与当前源码。
- `pre_dispatch_failure_preservation.json`：旧失败与成本、110份输入等价凭证。
- `status.json`、`heartbeat.json`、`ledger.json`：实时进度与实际请求；不能用旧v1的generating判断当前运行。
- `records/`、`requests_sent/`、`memory/`：原文、请求与事实／价值bank及保留／遗漏审计。
- `worker_0/worker.log`、`worker_0/owned_process_identities.json`、`worker_0/exit.json`：日志、所属进程身份和退出情况。

模型使用TP4/PP1、32,768上下文、单序列、chunked prefill512；初始化／选择输出至多1,024／512token。监督器脱离SSH终端，运行时错误停止派发，不自动重新启动。仅使用启动时核实空闲的四张卡，不干预其他任务。

所有所属GPU进程退出后，先冻结预测，再用旧CPU环境中的未修改UMT评价器与独立AP交叉核对；正式主指标为完整十视频的Top-5 mAP。技术失败回退B0并保留分母；报告实际候选外晋升、移出与对应标注，不将更多推荐或少量unknown当成收益。

自动报告预定为`docs/revalue_tvsum_highlight_memory_27b_v1_1_results_2026-11-04.md`。本轮未推送，未扩展到其他数据集或工具分支。

## 首条正式输出核验

北京时间14:16:53进入修订版首条正式建库请求，约50.42秒后正常返回：1974个输入token、487个输出token，原始JSON、普通引用去重审计与ledger哈希绑定已保存，输出契约通过。后续请求继续派发；这只确认真实建库调用可用，完整视频三臂选片及科学收益仍待完成。启动收据为当前运行目录的`startup_verified.json`。
