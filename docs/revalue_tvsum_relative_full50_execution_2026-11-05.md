# TVSum全50视频：F-relative／FV-relative执行记录

## 授权与范围

用户要求“跑一下100条测试”，澄清后明确选择“TVSum全50视频，两组共100条输出”。本轮复用已完成10视频的20份最终输出，仅对其余40视频新增320次建库和80次选片，最多400次新模型尝试，零自动重试。

完整50视频按历史REZE B0计划顺序冻结，不根据标签、旧成绩或价值类别挑样本。原10条是UMT val10且已反复查看；其余40条属于该UMT划分的train。本轮分别报告 `reused_val10`、`new40_official_train`、`all50_zero_shot`；全50汇总不称为官方test50。新增验证的主读数为新40视频FV-relative−F-relative。

## 保持的方法

继续使用Qwen3.8-27B BF16原revision与四卡TP4／PP1配置。相对价值规则、五维rubric、建库提示与条件schema、F/V完整条目装箱、unknown、候选表、0.5秒机械引用容差、1536token选片输出、分数多重集导出及原生UMT评价均不改。

每个新视频仅使用旧B0已经观察过的时间点：64个全片等距PTS点，加旧Top-5候选视图，去重后最多84张。64个全片点分为8组，每组8帧生成共同事实与价值记录；F和FV最终判断看到相同帧、相同事实，只差附加的V。没有新增ASR、回看、训练、采样时间或标签输入。

## CPU验证与冻结

- 原10视频的候选IDs、源帧IDs／PTS、全局64点、8组划分、choice_map、B0曲线和成本均与已完成实验一致；未重复解码或运行原10。
- 新40视频精确复原203／203个旧数据块，核对17,633个旧帧观察；保存3,221帧，每视频78–83帧。514个旧来源文件结束时哈希不变。
- 媒体CPU准备耗时231.534秒，新增实验模型调用、GPU时间及新源时间均为0。
- 相关CPU测试70项通过；全部400个原生输入／模板及194个结构化schema检查通过。最大预留上下文28,998／32,768，无需改变分辨率或上下文配置。
- 清单SHA256：`5df70cdd33f57c74ccbb7538fec5ca4ba599fea78490384f05503ba8830db52d`。
- 19文件源码映射SHA256：`73f9b274b3f9976f945bbad874fd5831933328fb9c1b2ba0afc065bc1a601f93`。

结构检查和助手代码复核不代替独立人工语义核验；旧实验中的事实／事件误关联仍是方法限制，本轮不同时修改这些机制。

## 启动和监控

北京时间2026-11-05 12:07，后台监督器PID57872启动，使用0–3号四卡和27B。启动前确认卡无计算进程、显存小于512MiB、利用率小于5%，并在worker中复核CUDA／NVML UUID。没有占用或干预其他用户作业。

按之前实测建库和选片速度估算，新增400次约需3–4小时；这是时间估计，不是恢复已取消的任意token／GPU硬配额。实际消耗、失败预留、worker生命周期和全部历史成本均继续分账记录。

监督器独立于当前会话运行，监控所属进程与账本；停滞只作提醒，终止故障保留失败并清理核验属于本轮的进程，不重试模型预测。正常结束后释放GPU，自动进行CPU汇总。SIGKILL、主机或电源故障仍超出Python清理保证。

## 最终评价与边界

先核验committed建库原文、帧来源、实际装箱及动态提示，再冻结新40＋缓存10的完整预测，之后才读取标签和旧指标。原生float32 Top-5 mAP与独立AP交叉核验，并报告稳定同分敏感性、逐视频配对差值、成员／排序变化和全部失败分母。

新40的探索门槛为最终输出至少76／80合法、FV-relative−F-relative至少+1pp；原20份成功缓存不得稀释新失败。技术失败／依赖失败按原协议回退B0，不删除视频、不修写响应。独立语义核验仍为pending，不自动扩样或执行额外模型分支。

新账本只包含本轮最多400次。复用的20次相对选片、原10视频80次建库以及更早启动／复现失败单列保留，不重置、不转移旧额度，也不重复记成新实耗。每种方法的独立成本口径另列共享初始化。

## 产物入口

- 运行说明（本地资料：`$MERIT_ROOT/experiments/revalue_tvsum_relative_full50_v1/README.md`）、冻结协议（本地资料：`$MERIT_ROOT/experiments/revalue_tvsum_relative_full50_v1/protocol.md`）。
- 运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_relative_full50_27b_v1_2026-11-05`。
- 准备收据：`media_cpu_receipt.json`、`media_preparation.json`、`context_capacity_check.json`、`runner_review.json`、`manifest.json`。
- 进度：`status.json`、`ledger.json`、`worker_0/worker.log`、`heartbeat.json`。
- 自动结果：`predictions.json`、`evaluation.json`、`per_video_results.csv`、`complete.json`。
- 自动Markdown报告：`$MERIT_ROOT/docs/revalue_tvsum_relative_full50_27b_v1_results_2026-11-05.md`。

本轮不推送远程，不修改旧冻结输入、预测、账本或报告。

## 首个新视频运行核验

北京时间12:14，首个新视频 `WxtbjNsCQ8A` 的8次建库及F／FV两次选片均合法完成，随后进入第二个视频。另以空CUDA掩码做一次纯CPU来源契约核对：从8条实际committed建库原文重建F/V，与本轮保存记忆一致；F为971token、V为803token，核对本身新增实验调用／GPU时间均为0。

首个完整流程通过不代表全部40条或科学门槛已通过。最终结果以400次计划执行后的分组评价和完成收据为准，后台保持原配置继续执行。
