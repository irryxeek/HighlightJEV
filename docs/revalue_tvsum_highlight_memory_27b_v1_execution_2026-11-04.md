# TVSum高光价值与记忆：27B三臂实验执行记录

## Material Passport

- Origin Skill / Mode：academic-research-suite / experiment-agent，run。
- 日期：2026-11-04（北京时间）；状态：已冻结、已启动，结果待完成。
- 用户授权：“按该方案开始执行推进”。依据[修订方案](revalue_next_experiment_plan_2026-11-04.md)，独立执行TVSum完整固定val10。
- 原方案及其plan-only收据保持不变；新运行的`authorization.json`明确为true，并绑定本次源码、输入和manifest。

## 本轮检验什么

三组使用同一Qwen3.8-27B、同一批全片／候选帧、相同高光任务与导出规则：D为Direct-HD，F添加事实／事件记忆，FV添加同一F及五维价值证据。主比较为FV−F；事实记忆的系统增益由F−D辅助观察。

每条视频初始8次分块观察，联合生成事实与价值记录；三组最终各1次重新选片。总计划80次初始化＋30次选择＝110次，不新增smoke、不自动重试。初始化实际共享执行一次，独立方法成本仍应分别计入F与FV。

最终可选择全片任意完整2秒clip，不限原Top-5；允许空推荐与并列。推荐前移后赋回B0原分数多重集，其余保持B0相对顺序。该D是新的高光任务接口，不把旧Direct的MR区间成绩当成HD成绩。

## 已完成的CPU准备

- 固定十视频全部到位；从B0已观察时刻按真实PTS等距选64点，加旧Top-5各至多4帧并去重，每视频79–84帧。
- 重新解码只用于来源核验；RGB／PTS与B0一致，候选像素与旧缓存一致。全片84个旧chunk、两个binding和两个inference文件均与早于本轮的冻结收据匹配，未新增模型所见源时刻。
- 原37个QV候选的审阅队列已保存，人工判断栏均为空：qv37_review_queue.csv（本地资料：`$MERIT_ROOT/comparisons/revalue_plan_2026-11-04/qv37_review_queue.csv`）。没有把旧低IoU代理转写为人工高光标签。
- 36项CPU回归通过，包括引用去重、伪造引用、unknown、合法弃权、候选外晋升、分数多重集、时间绑定、标签隔离、进程清理与截断写盘故障。
- 71套结构化输出schema在CPU编译通过。最长请求按F/V和输出保守预留为23,532token，低于32,768；真实F/V生成后仍逐请求CPU计量并核对运行时token哈希。
- F与FV事实逐字相同，活动F与V各至多1,024原生token，保留完整bank与全部装箱遗漏原因；最低时间覆盖或不确定性信息不能静默删除。

协作代码审查发现并修复：监督器中断时的所属进程清理，响应写盘／ledger提交中断的隔离，历史chunk来源绑定，已提交文件缺失时阻止通过，以及逐UUID空闲核验。该审查使用共享上下文，不是独立人工语义验证。

## 运行配置与进度入口

模型为官方BF16 Qwen3.8-27B，revision `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`。沿用已建立的独立环境和既有完整权重校验凭证；本轮核对文件大小／mtime及凭证，未声称再次全量重哈希权重。

配置为TP4/PP1、32,768上下文、单序列、eager、chunked prefill512；初始化输出至多1,024token，最终选择至多512token。只选启动时无其他计算进程的GPU，CUDA/NVML UUID核对后才加载。2026-11-04 **14:01:55**，后台监督器在GPU **0–3**启动四卡worker。

不恢复用户此前取消的任意累计token／GPU硬额度；固定110个正式请求身份、每个最多一次。15秒检查进程与账本，90秒无变化仅记录提示；无自动重启。SIGTERM/SIGINT及监控异常执行所属进程清理；SIGKILL或主机断电无法由Python收尾保证恢复，不能声称具备断电后自动续跑。

运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_highlight_memory_27b_v1_2026-11-04/`。

- 冻结源码：`source_snapshot/`；输入：`rows.json`、`requests.json`、`frames/`。
- CPU与来源凭证：`media_preparation.json`、`media_parent_binding.json`、`context_capacity_check.json`、`runner_review.json`。
- 进度：`status.json`、`heartbeat.json`、`ledger.json`。
- 原始请求／响应：`requests_sent/`、`records/`；事实与价值记忆：`memory/`。
- 模型日志：`worker_0/worker.log`；进程与退出收据：`worker_0/process.json`、`worker_0/exit.json`。

启动快照不代表模型已完成响应；实时完成数和健康状态以账本、响应哈希及退出收据为准。

## 完成后的评价与解释

全部所属GPU进程退出后，先冻结预测，再在旧CPU环境用未修改UMT评价器计算Top-5 mAP，并与独立AP交叉核对，保留原float32同分行为；完整十视频及技术回退均保留在分母中。

报告FV−F、F−D、FV−D及逐视频改善／退化，另报实际进入原生Top-5的候选外片段、移出片段及其标注评分，区别于模型推荐数量。合法来源与时间相邻不代表语义真实，独立人工证据核验仍待完成；不以减少unknown、NA或tie作为成功。

自动结果报告预定为`docs/revalue_tvsum_highlight_memory_27b_v1_results_2026-11-04.md`。本轮不改旧Q/Q+V预测、不重跑旧QV或TVSum协议，不加入ASR／回看／训练，也不推送。所有旧账本和失败成本保持原样。

## 后续状态：v1启动失败，当前转入v1.1

本文件以上为最初启动快照。v1首条在`SamplingParams`参数求值时发生NameError，尚未进入`engine.generate`，没有原始模型响应或usage；旧record的`model_called=true`在参数求值前写入，不能作为API已调用的凭证。该条预留尝试、2,998记账token和1,578.298624 GPU秒均保留，不作为模型效果结果。

原监督器的环境标记核验无法识别部分vLLM子进程。另行核对同UID、PGID、SID、完整祖先链至token／路径确认的根进程，并在发信号前逐PID复核启动时间，已释放全部7个所属进程；未操作其他任务。实际退出码不可由外部清理者取得，收据中保留null，不编造退出0。旧`status.json=generating`保持历史，终结状态以`manual_cleanup_receipt.json`和`manual_campaign_end.json`为准。

修复后的[当前v1.1执行记录](revalue_tvsum_highlight_memory_27b_v1_1_execution_2026-11-04.md)为后续进度入口。旧冻结源码、请求、账本和失败均未覆盖；v1.1在启动前逐项验证全部110份定义、rows、引擎、提示与契约保持一致。这是无模型输出可重采样的派发前实现修订，不是按实验成绩重跑。
