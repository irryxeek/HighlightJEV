# QFVS固定40查询：事实记忆读取策略对照协议 v1

## Material Passport

- Origin Skill / Mode：academic-research-suite / experiment-agent，run + validate。
- 日期：2026-11-06；Verification Status：执行前CPU准备；效果尚未知。
- 授权依据：用户“在QFVS上也测试一下”，范围答复“先40个查询，每视频10个（推荐）”。
- 本轮范围包含必要的4条视频共享建库与三组匹配对照；不使用旧QV、TVSum、Direct预算，不推送、不安装依赖。

## 研究问题与固定范围

将TVSum已实现的候选时序覆盖读取规则迁移至QFVS，检验同一事实库下F-read是否比旧F改善query-focused summary。主比较为F-read−F；D仅为无文本记忆参考，B0与Uniform为CPU缓存/确定性参照。不得按结果选条件或子集。

固定历史`reze_qfvs_full180_2026-10-23/baseline_gpu5/inference.jsonl`中每视频原顺序前10条，4×10=40。完整qid在`scope_freeze.json`，于读取新结果及标签前冻结。四条源视频和部分查询已用于开发，不构成未见测试集。原B0必须从缓存原始概率按冻结REZE导出重新核对一致，不补跑模型。

保留QFVS原生语义：两个概念是OR，任一相关即可；原生5秒shot，摘要长度`floor(n_shots*0.02)`。P01/P02/P03/P04分别55/73/43/71个shot，不用TVSum Top-5长度或mAP。

## 输入、候选与共享记忆

每查询固定84候选：完整旧B0摘要集合，加从剩余原生shot按`floor((j+0.5)*N_remaining/N_extra)`均匀选取的补充，最后按时间排序。三组均看84个候选的同一局部帧，帧选取规则是该shot内距中点最近、已被历史REZE实际观察的帧，平局取更早者。所有像素与真实PTS对照历史完整窗口哈希核验。模型不知道候选B0身份或分值，表格顺序不是分数顺序。

每视频从历史已观察瞬间的首尾区间均匀取64个最近旧帧，8组×8帧，使用未改动的TVSum记忆写入提示/schema建库。4视频共32次，query无关，每视频库供10个query共同使用。所有F/V、来源与失败保留，但选片只读F；不做新增价值条件。64帧覆盖约3–5小时极稀疏，不能等同全事件覆盖。

- D：84候选旧帧，无文本记忆。
- F：同一84帧，加旧group round-robin读取视图；每非空组首事实与最早不确定条目优先，全条目装入1024 token上限。
- F-read：同一库、84帧和1024 token上限；保留同样最低覆盖骨架，再依次优先新增B0 Top-5局部来源覆盖、相邻已观察时刻、事件类别、来源帧，再按距离与fact ID破同序。局部范围为原生5秒shot±0.5秒，只按实际PTS判定，不把两稀疏帧中间整段当证据。最终按原事实顺序渲染。

F与F-read只改变F文本及与其一致的允许fact-ID词表，实际token数可以不同；提示任务、模型、图像、解码与评价固定。读取锚点仍是原B0最高5个shot，不增加query词检索、embedding、价值重写或回看。D与F相比还少了通过共享库传入的64个全局观察，因此F−D不能解释为纯文本记忆效应。

## 模型与输出契约

固定`Qwen3.8-27B`修订`1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`，与TVSum同一native环境、BF16 TP4、上下文32768、温度0、seed0、前缀缓存关闭、一次worker。图像原像素320×480，禁重采样。建库输出上限1024 token；选片1536；F上限1024。CPU预先核验所有实际图像、prompt token、xgrammar、完整legal compact输出长度；动态F模板预留1024+128 token边界余量，调用前再次核验。

三组共同输出紧凑JSON：`selection_state`、`selected_choice_ids`、`fact_ids`（最多4）、`missing_evidence`（至多120 ASCII字符）。selected必须恰k个不同合法choice；abstain必须空choices和非空缺证原因。不强迫分差或胜负，允许弃权，不输出逐shot理由或长思考。候选ID预绑定shot/局部帧，禁止新时间戳。重复事实引用可审计去重；重复选择是无效输出，不补齐、不伪造预测。

每query三组顺序由qid哈希循环移位决定。先完成全部32建库调用，再完成120选片调用。建库某组非法则该视频共享库不可用，D照常；依赖F/F-read记为dependency_failed并保留完整分母，不用模型重试。packing失败同理。运行错误停止新派发，不重启worker；其它尚未调用样本仍在完整清单中。

## 评价、失败与停止条件

所有模型进程退出、完整预测冻结后，CPU才读取GT。原生semantic maximum-weight matching的Oracle P/R/F1为主，三用户各自F1后均值为辅，逐query/逐视频报告。主配对F-read−F，次级F-read−D、F−D。bootstrap以整条源视频为cluster（4群组、10000次、seed42），不将40查询当40独立视频；小群组区间仅供开发诊断。

全40分母；invalid、runtime、dependency_failed、未尝试和abstain均回退冻结B0并显式列出状态/成本。回退不是新模型预测，不单独筛合法输出报告主成绩。Uniform为全视频均匀2%CPU参照，不受84池约束。B0来自旧Qwen3-VL-8B密集REZE，模型和输入覆盖不同于新27B三组，B0比较仅作系统参照；旧全180成绩不是本轮40成绩。

本轮最大152次新尝试=32建库+120选片，零重试，一个4卡worker；单worker主生命周期10800秒，退出余量60秒，GPU生命周期累计43440秒。绝对token上限由CPU逐条预留输入+输出求和确定为2,588,659（写入authorization），低于152×32768=4,980,736；不能以未用token/GPU秒追加调用。运行时按实际token记账，失败未返回token按该请求上限预留。

启动前要求完整输入、源码、模型环境、历史哈希及CPU审查通过；仅选实时空闲4卡，核对CUDA/NVML UUID、进程UID/PGID/SID/starttime。OOM、运行错误、输入/来源漂移、上下文溢出或期限届满停止；仅清理本次拥有的进程。原始响应/失败不可修写，不自动扩到180查询、不据成绩重选子集。

## 产物与结论边界

新目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_qfvs_memory_read_40q_27b_v1_2026-11-06`。保留source_snapshot、scope/rows、64全局和84候选索引、frame stores、requests/requests_sent、memory/read_views、records、ledger、process/exit、prediction_freeze、evaluation与report。自动报告保存到项目docs。

这轮能够检验同一共享库与固定候选池内的读取策略迁移；不能证明完整长视频检索、query语义检索、价值模块、低采样建库充分性或新视频泛化。若F视图没变化，照实报告无干预实际差别；若负结果或技术失败，不自动扩大实验。
