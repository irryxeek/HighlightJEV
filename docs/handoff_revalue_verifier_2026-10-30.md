# ReVALUE 当前任务交接：REZE Direct + 区间 Verifier

**交接快照：2026-10-30 20:17:22，北京时间。后台实验仍在运行。**

本文件保存当前有效任务状态，不是追加实验授权。新会话必须先核对最新用户指令与实时产物；本文件中的进度、PID 和临时账本哈希会过时。当前请求仅为整理 handoff，本次整理没有启动实验模型、分配 GPU、修改运行中源码或推送远程；既有后台实验继续推进。

## 1. 当前目标与用户已作出的决定

1. 主线是 **query 驱动的时序 grounding**：定位目标事件、核查语义与起止边界。排序、HD 分数、减少 tie 均不是当前成功标准。
2. 用户已选择 **REZE 论文 Direct 协议重建**作为 base。它读取整视频采样帧，一次输出匹配区间；不是 REZE 的局部 Yes/No 密集扫描，也不是完整 ReVALUE Agent。
3. 当前模块是 **单区间 verifier**：用 query 相关度、五类价值证据和边界检查筛查 Direct 的潜在错误。第一阶段只验证能否发现反例和控制误报，不改区间、不重排、不新增回看。
4. 用户原话“启动验证”已经授权冻结的 v1.1 运行，授权已写入实时 `authorization.json`，无需再次询问同一轮许可。它不授权新版本、额外请求、重试或扩大样本。

依据：[grounding 主线](temporal_grounding_mainline_2026-10-29.md)、[当前协议](revalue_direct_verifier_plan_v1_1_2026-10-30.md)、[启动记录](revalue_direct_verifier_execution_2026-10-30.md)。旧文档的制定时状态保留为历史快照。

## 2. 已确认事实：基线结果

REZE Direct QV100 已完成 100 次请求，98 条有有效区间，共 **139 个区间**；qid 9160、2498 的零长度输出被原解析规则删除，保留为两条 base 空预测。完整 100 条是 QVHighlights **train 开发诊断集**，不是未查看过的测试集。

| 指标（%，完整100条） | 旧自定义 Direct | REZE Direct |
|---|---:|---:|
| 首个有效区间 R1@0.5 | 42.00 | 39.00 |
| 首个有效区间 R1@0.7 | 28.00 | 30.00 |
| MR mAP@0.5:0.05:0.95 | 24.72 | 26.48 |
| 任一区间命中 recall@0.5（不是R1） | 42.00 | 44.00 |

**有效结论：替换方案没有带来一致提升。** 用户仍选择它作为后续 base。旧52个合法低IoU反例中，9个被新首区间修正，同时15个旧命中样本退步；不能只展示改善案例。

REZE Direct 使用 Qwen3-VL-8B-Instruct BF16，整视频2 FPS，实际242–300帧；greedy、128输出token、最多保留10个完整区间。视觉尺寸、采样相位和保序分数是本地重建约定，不能声称严格复现论文成绩。生成序号导出分数 `1/(rank+1)` 不是模型置信度。

来源：[REZE Direct 完整结果](reze_direct_grounding_qv100_results_2026-10-30.md)。原自定义 QV20 grounding 的70%/50%来自不同样本，不应与本轮100条直接作提升对照。更早的整表同分、时间键、单目标评分实验属于机制诊断，不能算新 grounding 成绩。

## 3. 已确认事实：正在执行的 verifier

### 3.1 方法和固定条件

```text
冻结的139个Direct区间 + 原query
→ 复用旧2FPS帧：区间内≤16张，前4秒≤4张，后4秒≤4张
→ 每区间一次Qwen请求：可见事实、query匹配、五类价值、起止边界
→ CPU检查来源ID、区域和原query引文
→ flagged / supported / insufficient；契约失败单列invalid
→ 全部退出后冻结响应，再读GT评价反例筛查
```

- 五类价值：`outcome / information / emotion / action / sensory`，对应结果、信息、情感、动作、感官。不是旧四种 cue 的改名。
- 候选内为 `[start,end)`，前后上下文各4秒；固定等分格中点选帧、按源帧ID去重，不复制帧补数。逐图像输入实际PTS和区域标签，未新增采样、裁剪、音频或源视频回看。
- 原query直接进入请求，不使用旧TaskSpec对象抽取器。输出需引用query原文子串；字面合法不等于语义覆盖正确。
- 每条事实只能引用同一区域。query明确支持/反证须完全来自片内；截断判断需片内锚点、正确方向的片外证据和“同一次事件”支持。
- `flagged` 由query明确反证或明确边界缺陷触发；query和两端均支持才为 `supported`，其余合法判断为 `insufficient`。**价值低、没庆祝、没情绪不能直接否定正确grounding。**
- 事实与判断同次生成，是 `query_conditioned_observation`，并未实现原ReVALUE的query盲独立事实记忆。此轮没有四态成对比较、全视频记忆或完整Agent闭环。

### 3.2 20:17:22 的只读快照

| 项目 | 已核对值 |
|---|---|
| 已开始尝试 | 80/139 |
| 已返回 / 正在生成 | 79 / 1 |
| 通过契约 / 引用或格式无效 | 47 / 32 |
| 合法输出中的 flagged / supported / insufficient | 28 / 7 / 12 |
| 模型worker已启动 / 已正常终止 | 8 / 7 |
| 已终止worker | 全部退出0、所属进程为空 |
| 已终止部分 GPU 生命周期 | 1,659.706310409秒；**尚不包含当前worker最终成本** |
| 当前token记账 | 379,389，含正在生成请求的最大预留；不是最终实际总量 |
| 终态、预测冻结、评价收据 | 均尚未生成 |

**28个 flagged 是模型报警，尚不能称为28个真实反例。** 还没有当前verifier的precision、recall、误报率、定位提升或独立人工语义验证结论。

32个无效输出的已核对来源：

| 契约失败类别 | 次数 |
|---|---:|
| query直接证据并非全部片内 | 20 |
| 缺失或重复事实引用 | 8 |
| query引文不属于原请求 | 2 |
| 单条事实混合片内和片外帧 | 1 |
| end=supported缺少片内证据 | 1 |

79个返回记录的 `finish_reason` 均为 `stop`，当前这些无效输出不是已观察到的输出截断或OOM。这里只能确认契约失败，不能把所有失败归结为某一提示或视觉理解机制。

**确定结论：至少138/139合法的技术门槛已经不可能通过。** 按冻结协议，引用无效保留且不重试，继续固定清单；OOM、运行错误、输入漂移或预算不足才停止后续请求。不能为提高合法率修改旧预测、放宽校验或选择性补跑。

证据包：快照JSON（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/revalue_verifier_handoff_2026-10-30/snapshot.json`）、账本副本（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/revalue_verifier_handoff_2026-10-30/ledger_snapshot.json`）、所属进程快照（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/revalue_verifier_handoff_2026-10-30/owned_process_snapshot.txt`）。这些快照不会自动刷新。

## 4. 验证过什么，尚未验证什么

**已经验证：**

- 原139个CPU输入均准备完成，真实图像processor处理；最大prompt 4,865 token，输出上限1,536，上下文8,192，最小余量1,791。
- 冻结运行器22项CPU契约测试通过；独立只读审查提出问题后由主助手修复并验证，最终review由主助手签署，不能冒称独立代理执行过测试。
- CPU收尾程序另有5项通过：未终止阻断、不确定退出阻断、重复评价阻断、失败不重试、合成结果归档。它们不是5次模型实验。
- 本次交接重新执行冻结 `common.verify(require_execution=True)` 通过，源码、输入、授权、依赖和116个base保护文件一致；已提交响应与账本哈希一致。
- 前7个worker实际完成，证明这些批次的运行兼容性；不代表后续一定成功。准备时 `runner_review.json` 中GPU未测试字段是历史事实。

**尚未验证：**

- 最终全量筛查指标，以及合法引用背后的视觉事实真假。
- 正确定位但低价值的事件是否会被误判、边界缺陷是否属于同一次事件。
- 五类价值相对于query-only的独立贡献；当前联合提示单臂无法给出该因果结论。
- 回看、记忆、边界修正或完整Agent能否提高grounding。此轮都未实现或未运行。
- 独立人工语义审阅数量仍为0；助手查看不等于独立人工真值。

## 5. 假设与待检验解释（不要写成结论）

| 假设 | 目前支持它的观察 | 尚缺证据 |
|---|---|---|
| 片外上下文干扰片内判断 | 20个query证据区域违规 | 需核对原响应与选中帧，区分引用失误、事实错配和真实跨边界事件 |
| 同次事实生成与判断使引用依赖不稳定 | 8个缺失/重复引用 | 需离线核对事实ID及schema；不能仅凭计数认定根因 |
| 多维输出增加任务负担 | 输出同时含事实、query、价值和边界 | 没有同输入query-only对照，不能声称价值模块拖累效果 |
| 同一模型验证自身会共享视觉错误 | base与verifier使用同一Qwen权重 | 需独立语义审阅或新的受控对照；当前只是方法风险 |
| 某些低IoU属于标注范围/重复事件切分问题 | 历史Direct案例已出现此现象 | 当前flagged样本仍需逐例核查，不能全部归咎于标注 |

## 6. 执行约束、预算及评价口径

### 当前独立授权

`139次尝试；零重试；零额外故障请求；1,138,688 token；14个顺序模型worker；同时最多一卡；每worker生命周期≤300秒；累计≤4,200 GPU秒。`

每批10次，末批9次。生命周期包含加载、执行、退出及失败；不得把未使用token/GPU时间折算为额外请求。用户允许使用空闲GPU，但本协议并发上限仍是一卡。实际已使用物理GPU4；每批由supervisor检查空闲卡，禁止干扰其他用户进程。

模型为 `$DATA_PARENT/MemDreamer/models/Qwen3-VL-8B-Instruct`，revision `0c351dd01ed87e9c1b53cbc748cba10e6187ff3b`，BF16、TP=1、greedy。环境为 `$LONGVT_ARTIFACT_ROOT/env/inference/bin/python`；不更新依赖、不下载模型、不启动新服务。

### 旧账独立保留，余额不转移

| 旧轮次 | 尝试 | token记账 | GPU生命周期 |
|---|---:|---:|---:|
| QV旧诊断 | 797/1000 | 398,929 | 0.5395204532 GPUh |
| TVSum transfer | 670/670 | 1,106,932 | 2,102.263978秒 |
| 原Direct pilot | 26/30，25成功1OOM | 140,457，含失败预留 | 280.481364秒 |
| 时间键QV20 | 20/20 | 115,759 | 395.601399秒 |
| 单目标评分QV20 | 40/40 | 204,992 | 150.434879614秒 |
| Direct grounding QV20 | 20/20 | 102,212 | 70.206870820秒 |
| 旧自定义grounding QV100 | 96/100 | 494,459 | 361.064442033秒 |
| REZE Direct QV100 | 100/100 | 2,306,138 | 4,312.483284708秒，含2次启动失败 |

以上旧数值来自各轮结果报告，本次未重新跑旧实验或重新评价。原QV余203、Direct pilot余4、其他余额都不授权本轮新条件；TVSum补跑仍不在范围内。

### GT隔离与完整分母

- 推理完成并确认全部所属模型进程退出，先冻结所有响应，再读取GT。运行中不要手动提前评价或查看当前候选的GT来调整方案。
- 主要错误代理为每候选对任一独立GT最大IoU<0.5；补报0.3/0.7、query宏平均与10,000次源视频聚类bootstrap。
- 完整139候选与100 query均保留；invalid、insufficient、未尝试及中断不从错误召回分母删去。两条base空预测不算verifier发现。
- 预设探索门槛：合法≥138/139，precision≥80%且高于错误基率，recall≥30%，正确区间误报≤10%，insufficient≤40%，flags≥20。门槛不是统计显著性或语义真值证明。
- 不按结果筛有利子集、不强迫分差/胜负、不回写base。此轮不产生新的grounding输出，不能报告虚构的定位提升。

## 7. 产物、运行入口与容易误读的状态

### 运行与代码

| 内容 | 绝对路径 |
|---|---|
| 当前工作区 | `$MERIT_ROOT` |
| 当前正式run | `$ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_1_2026-10-30/` |
| GPU执行源码 | 上述run的 `source_snapshot/`；运行中不得编辑 |
| 开发代码 | `$MERIT_ROOT/experiments/revalue_verifier/` |
| 仅CPU收尾源码 | 当前run的 `cpu_postprocess_source/finalize_cpu.py` |
| Base正式run | `$ZEROSHOT_ARTIFACT_ROOT/reze_direct_grounding_qv100_v1_2_2026-10-30/` |
| Base旧帧数组 | `$ZEROSHOT_ARTIFACT_ROOT/reze_direct_grounding_qv100_v1_2026-10-30/frames/`；v1路径仍被使用，不得清理 |
| 准备/审查/ARS包 | `$MERIT_ROOT/comparisons/qwen_direct/revalue_verifier_preparation_2026-10-30/` |
| 当前交接证据包 | `$MERIT_ROOT/comparisons/qwen_direct/revalue_verifier_handoff_2026-10-30/` |

快照时supervisor PID=2452，CPU finalizer PID=10327；均核对了实际命令行。**后续需重新核对命令、启动记录、PGID和是否已退出，不能只凭旧PID或 `/proc` 存在判定。** 禁止把正常等待的CPU收尾程序当作推理服务重启。

CPU finalizer已在运行，等待终态收据，最多等待4500秒。它只调用一次冻结评价器，CUDA不可见；异常则写失败收据，不自动重试、重启推理或终止模型。完成后预期生成：

- `$MERIT_ROOT/docs/revalue_direct_verifier_results_2026-10-30.md`
- `$MERIT_ROOT/comparisons/qwen_direct/revalue_verifier_v1_1_2026-10-30/`
- run下 `prediction_freeze.json`、`evaluation.json`、`candidate_audit.csv`、`evaluation_complete.json`、`cpu_finalizer_complete.json`；失败时查 `cpu_finalizer_failure.json`。

**20:17快照时以上结果尚未生成。** 自动报告仍须人工读取核对，脚本退出0不能直接认定结论正确。

### 历史快照陷阱

- run根目录 `status.json` 仍写 `prepared_not_authorized`；它是准备快照，实际授权已true，实验正在运行。以授权、实时账本、worker收据和进程为准，不为“修复状态”重跑任务。
- 准备文档、`frozen_v1_1/authorization.json` 和 `cpu_readiness_receipt.json` 的false/零调用是当时事实，不能覆盖成当前状态，也不能以它们否认已批准执行。
- run里的 `handoff_progress.json` 是19:54的21次快照；ARS账本run计数仍是此前20次/3worker的记录，不是实时进度。
- 旧v1准备目录只作历史保留，禁止误启动。任何冻结记录都不清除、不覆写以掩盖失败。
- 退出日志出现nanobind/reference-count提示时，应结合退出码、收据和实际进程判断；提示本身不是重启依据。

### 固定哈希与审计

| 对象 | SHA256 |
|---|---|
| 当前manifest | `1e2972b27c68956e9636d3e7cd4dcb4f5ac0eaf8113b68e55bb8227dad2151f4` |
| 当前inputs | `35f3c3297eed02b36ef32b98bdca1ac93b8e6ffdaa2113f6d379ee1f85b52f8a` |
| 已批准authorization | `dbd21cd4d8a37d1dce1a98f540775a3d2b24fd9e311e6312e0dc579cc83a038e` |
| Base最终ledger | `8fb3140ee26f8d0f785b65c244ac87dbc5213254b38d39aa5ad5ad7106615d8b` |
| 本交接账本副本 | `03e3c356d3ec556a68b8c726b4cc0928d6e2ba1c9668873935cca3e6709c096a` |
| 本交接snapshot.json | `14189eae54131b9d9162d529c4657850ffc1f92966de2b60bf52793e7c7689b8` |

运行中ledger会合法增长，不能用本交接副本哈希要求实时账本不变。源码/输入/base保护文件则应保持冻结。

ARS来源为 `$WORKSPACE_PARENT/.codex/skills/academic-research-suite/SKILL.md` 的experiment-agent。已有passport是准备包的 `plan.md`，账本为 `plan_run_ledger.yaml`。只用技能的 `ars/scripts/run_ledger.py append/show/report` 读写账本，不手改YAML。最近检查13条记录链有效，执行checkpoint已关闭，没有待确认问题。曾有一次记录工具因command数组类型拒绝写入，改字符串后成功；不是实验重试。阶段结束后需补真实运行/评价收据，不能把启动收据当完成收据。

### Git与发布

研究工作区 `$MERIT_ROOT` 本身没有Git元数据；发布checkout为 `$PUBLICATION_ROOT`，origin=`git@github.com:irryxeek/MERIT-based-method.git`。本轮未请求推送，因此不推送。以后获指令推送时，按用户既有偏好包含本轮报告、方案与索引；不要提交模型、视频、帧数组、环境或凭据。现有 `AGENTS.md` 保留不改。

## 8. 新会话的下一步

1. **先读再核对，不重新启动。** 读取本文件、当前协议和真实run，先检查更新的用户指令。只读查看ledger、`campaign_exit.json`、worker退出收据、两个管理进程的实际命令行和finalizer终态。
2. **若仍在运行：** 继续只读监控，不运行 `prepare.py`、`supervise.py`、`worker.py`，不抢先启动评价。若用户只问状态，报告实际计数和科学门槛，不改实验。
3. **若模型已结束、CPU finalizer仍活跃：** 等待既有收尾；不得并发运行第二个 `evaluate.py`。若有最终报告，核对其结果哈希、全部退出收据、账本成本和原base未改。
4. **若发生失败：** 保留全部账本、原始响应和未尝试分母；进行CPU诊断。不要自动补跑未完成区间、重启worker、删除freeze或绕过终态检查。CPU评价失败也先查失败收据和已冻结产物，不盲目重复单次入口。
5. **完成后分析：** 分开报告运行健康、契约合法率、报警质量和真实语义错误。优先统计五类引用问题，审查flagged、supported、insufficient与invalid，不只挑成功例子。输出至少包括正确报警、误报/可能标注问题、漏报/证据不足的具体例子，并明确视觉审查者身份。
6. **待结果支持后再提下一版：** 可先做不调用模型的契约诊断；若要比较query-only与价值提示或修改引用输出形式，准备独立、最小变量协议。不能同时加入ROI、新帧、记忆、回看或边界重写，也不能将当前失败响应修写成新预测。任何新增模型轮次需明确的新预算和授权。
7. 更新实际结果报告、执行记录、文档索引和ARS阶段收据。保留这份交接快照；新的结果应注明日期/版本。未获推送指令时仅保存本地。

## 9. 新会话启动提示词

直接复制以下内容；不需要粘贴完整旧对话：

```text
请接续 $MERIT_ROOT 的当前 ReVALUE grounding 任务。

先完整读取 $MERIT_ROOT/docs/handoff_revalue_verifier_2026-10-30.md，
再按需读取其中的冻结协议、运行收据和 academic-research-suite 技能。
当前base是REZE Direct协议重建，任务是单区间verifier反例筛查，主线是grounding而不是排序。

用户已授权并启动revalue_direct_verifier_v1_1_2026-10-30；不要重复询问该轮授权，也不要重新启动。
先只读核对 $ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_1_2026-10-30/
中的实时ledger、campaign_exit、worker退出收据、CPU finalizer状态及对应进程实际命令行。
handoff进度和PID只是带时间的快照；根status.json、准备包授权和ARS计数可能陈旧。

若仍在运行，保留既有supervisor和CPU收尾，不提前读取GT、不启动重复评价。
若已结束，核对自动结果与哈希，整理契约失败、筛查指标和代表性案例；事实、假设、标注疑点分开。
若失败，仅做CPU诊断并保留完整分母，不补跑、不重试、不删freeze或绕过检查。

沿用139次尝试、零重试、1,138,688 token、14个顺序worker、同时一卡、每worker300秒、累计4200 GPU秒的独立上限。
不挪用旧额度，不补跑TVSum，不追加模型实验，不改冻结输入/提示/源码/预测，不更新依赖或干预其他进程，不推送。
新模型条件必须单独提出可审阅协议和预算，等待明确授权。

先向我简要报告当前真实状态、已确认结论与未解决问题，再完成既有结果的核查和本地报告整理。
如本会话还有更新的暂停、取消或范围调整，优先遵守最新指令。
```
