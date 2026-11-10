# TVSum val10：最新价值标准完整评分对照协议 v1

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run / validate
- Origin Date: 2026-11-10
- Verification Status: PREPARED（结果另存，不修改本轮标准）
- 用户原文：“那就用最新修订版在同样的10条视频上完整跑一遍，其他设置不变，跟REZE、原五维版和加背景版对比一下mAP。”

## 完整范围与比较

固定之前官方UMT val10全部视频及顺序：J0nA4VgnoCo、cjibtmSLxQ4、JgHubY5Vw3Y、Bhxk-O1Y7Ho、sTEELN-vY30、Yi4Ij2NM7U4、E11zDS9XGzg、Se3oxnaPsz0、JKpqYvAdIsw、fWutDQy1nnY。完整推理1,260个原3秒窗口，覆盖全部时间轴。Top-5仅为评价指标中的前五个2秒片段，不限制推理范围。

主比较：最新价值标准＋原固定背景，减原具体五维＋同一背景。另并列比较原具体五维无背景与REZE本地适配。三组控制复用全部冻结预测，新增对照调用0。研究者已看过这些开发视频和其中失败案例，不能将本轮视为独立测试或无开发反馈验证。

## 唯一输入干预与固定项

直接使用已完成10窗口诊断的修订规则：弱普通线索不能单独构成观看贡献；任一充分支持的贡献维度可Yes；其他维度缺失不能单独导致No。I2、E2、S2与判定总则逐字节复用，不再调规则。没有数值权重或强制分差。

本轮回到与三个全量评分控制一致的输出方式：单个Yes/No token及top-20概率读数，不把结构化诊断的Yes/No替代连续分数，不生成新增解释调用。具体规则文本参与判断，但本轮没有逐维输出。10窗口诊断是公开依据的另一次判断，不是这轮评分内部过程。

以下全部固定：Qwen3-VL-8B-Instruct的原权重/revision、BF16 TP1、GPU引擎配置、4096上下文、temperature=0、最多1输出token、原3秒窗口、2fps原像素／帧索引／真实PTS、窗口到1秒再2秒分数映射、同分处理及UMT评价代码。背景10份逐字节复用，不重新生成；不增加视频标题、类别、音频、采样、记忆、回看或比较器。评分前不读取GT或旧分数作为模型输入。

相对原加背景版，只改变价值规则包及其不可避免的提示长度／注意力分配；不能分别归因于微笑门槛或Yes/No聚合规则。相对无背景具体版和REZE存在额外提示与背景差别，仅作整体方法比较。REZE是本地TVSum适配缓存，运行数值环境并非全部同时重跑，不能称官方论文TVSum成绩。

## CPU审查与冻结

新增4项CPU契约覆盖：与最新修订规则/renderer字节相同、与原加背景提示只差三条问题和总则、单token输出保留、引擎/媒体/概率/导出/评价实现与原冻结源相同。另核验每视频首中末共30窗口的原生输入、像素、PTS和上下文预算；运行时对全部1,260窗口再次验证。

冻结源码、全部视频清单、背景、原输入引用、三组控制哈希和标注文件哈希绑定。标注内容仅在预测冻结后CPU评价读取。保存提示源码和原始输出，保留全部旧协议、诊断、预测、账本与失败记录。

## 本轮独立运行预算

用户授权完整同10视频推理；助手按该范围设置上限：最多1,260次正式尝试、额外故障调用0、重试0、总token上限5,160,960、同时最多一张空闲GPU、1次worker、GPU生命周期最多1,800秒（含加载与清理，留5秒退出清理）。每请求最多预留4096token，失败保留预留成本。

旧背景、评分、诊断等预算不转移；本轮背景生成和控制重跑均为0。遇到输入不一致、缺概率、上下文不符、模型/解析错误或预算上限即停止，保留全部10条分母、未尝试与失败窗口，不重试、不回填旧分数。失败视频主指标计零失败信用，缺失预测保持空值。不扩到50视频、不推送、不修改依赖或服务。

## 评价与解释

主指标为完整10条的UMT Top-5 mAP，独立实现与固定原UMT函数交叉验证。报告四组总体及逐视频成绩，最新标准相对三个控制的差值（百分点）、提升／下降／相同数量。每项差值使用10,000次视频级配对bootstrap、seed42，分别给出95%描述区间；不是联合置信保证，也不进行窗口级伪独立推断。

辅助项沿用已有定义：Top-1/Top-5正例标注比例、前五平均人工重要性、全时间轴Spearman、常数视频、概率读数缺失或回退、Top-5边界同分、概率分布、前五位置变化、token与GPU成本。所有视频保留，不因指标或前轮失败表现改变分析子集，不根据本轮输出再调提示。

## 路径

- 源码：`experiments/revalue_generic_highlight_scoring_gate_v1/`。
- 新运行：`$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_val10_value_gate_v1_2026-11-10/`。
- 可携带产物：`docs/artifacts/revalue_generic_highlight_tvsum_value_gate10_2026-11-10/`。
- 最新规则来源：`$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_value_gate10_v1_2026-11-10/source_snapshot/`。
- 加背景控制：`$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_val10_context_v1_2026-11-10/scoring/`。
