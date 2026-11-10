# TVSum val10：具体五维标准密集评分对照协议 v1

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run
- Origin Date: 2026-11-10
- Verification Status: UNVERIFIED（运行前冻结协议；结果另存）
- Version Label: generic_highlight_tvsum_val10_detailed_v1
- 用户授权：在前一轮明确提出同10条、同输入、仅具体规则替换的方案后，用户说“那用这个标准重新测试”。

## 问题、唯一干预及边界

检验原有具体价值标准能否改善密集局部评分，主比较为 detailed−brief，REZE 为次要缓存对照。固定完整官方 UMT val10及原顺序：J0nA4VgnoCo、cjibtmSLxQ4、JgHubY5Vw3Y、Bhxk-O1Y7Ho、sTEELN-vY30、Yi4Ij2NM7U4、E11zDS9XGzg、Se3oxnaPsz0、JKpqYvAdIsw、fWutDQy1nnY。这些视频已有多次开发结果和案例审阅，不能称为盲测或独立测试集，不根据旧得分筛选样本。

同一 Qwen3-VL-8B-Instruct BF16、revision `0c351dd01ed87e9c1b53cbc748cba10e6187ff3b`，3秒窗口、2 fps、完整窗口6帧、同一像素/实际PTS、单个Yes/No token、top-20读数、1秒→2秒导出与官方UMT评价。运行器、模型配置和调度代码与上一轮相同；两个对照均复用冻结预测，新增基线调用0。

仅替换用户提示中的五类简略例子段落，系统提示、总体任务、原禁止规则及尾部任务说明均保留。新段落逐字引用旧 `generic_highlight_value_v4_2026-11-06` 的五维15题及支持、反证、unknown、禁止推断规则；来源为 `experiments/revalue_tvsum_value15_consistency_v2/value_rubric.json`，复制哈希单列。

局部评分适配说明：区分事实可见、观看贡献和相对优先；只考虑适用维度，不计支持题数，不要求五维全通过。无其他片段时相对比较可未知，不编造参照，也不把相对优先作为局部价值必需条件。unknown不是反证。旧规则中的解释/引用要求是内部判断依据，本轮不输出逐题状态、解释或引用，仍为同一单token答案。因此这是**具体规则提示包**实验，不能声称完整V15逐题核验，也不能直接观察每维是否被正确执行。

不加入全片主题、记忆、候选比较、回看、ASR、额外采样、边界修改或打分权重。不放入视频标题、已知失败例、人工标注和旧分数。提示长度与注意力分配变化是干预不可避免的共同变化；不宣称纯概念因果识别。允许同分、全否和负结果，不为制造分差更改输出。

## 审查、冻结与运行

建立独立源码目录及运行目录，旧预测、规则、源码快照、失败和协议不改。核对原26项CPU测试所覆盖的运行代码哈希一致，新增5项规则/输入契约测试；对10视频首中末共30窗口做原生CPU处理器预检，检查详细提示、原简略提示及REZE的上下文长度，并逐帧对齐旧像素/PTS。运行中每个实际请求再次检查上下文；若超4096 input+output即停止，不截断规则或视频、不追加重试。

预测完整冻结后读取GT评价。当前研究者已见旧标签和失败分析，此次冻结用于防止运行中调参，不代表未接触标签。逐窗口原始概率、批次、帧轨迹、派发预留和退出收据均保留。

## 独立上限与停止规则

用户授权了同10条重测；下列数值是助手据完整清单设置的本轮执行边界，不能表述为用户逐项报出的预算。

| 项目 | 本轮上限 |
|---|---:|
| 视频／正式窗口尝试 | 10／1,260 |
| 额外故障调用／重试 | 0／0 |
| 绝对 token | 5,160,960（每窗口4096保守预留） |
| 同时GPU／worker启动 | 1／1 |
| GPU生命周期 | 3,600秒，包含启动与清理 |
| 旧对照新增调用 | 0 |

不转移任何旧QV、TVSum、Direct或上一轮简略评分余额。超预算、输入/源码不符、推理或解析错误停止后续派发；只清理本轮所属进程组，不影响其他用户进程。不新增worker重试，不自动扩至50条。未尝试/失败视频留在完整10条分母，预测为不可用，主指标记零失败信用，不伪造分数或回填旧基线。

## 评价与报告

主指标：完整10条UMT Top-5 mAP，detailed−brief配对差值及10,000次视频级bootstrap、seed=42；同样报告相对REZE差值。区间仅描述这个开发集，不以是否跨零决定删除样本或追加调用。

预先固定辅助诊断：逐视频AP；Top-1正例标注比例；Top-5正例比例和平均人工重要性；全时间轴分数与人工均值的Spearman；常数视频、分数分布、top-20缺失回退、非Yes/No输出、Top-5边界同分和前五变化。辅助指标不替代主指标。若失败，完整分母主指标仍报告；关联性等不可定义诊断保留缺失，不能仅报告成功子集改善。

技术完成要求为1,260窗口与10条预测完整、输入和预算契约通过。科学收益与技术成功分开；未超过简略版或REZE、全否/同分均原样报告，不声称规则有效。

运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_val10_detailed_v1_2026-11-10`。

源码：具体规则评分器（本地资料：`$MERIT_ROOT/experiments/revalue_generic_highlight_scoring_detail_v1/README.md`）。对照：[简略版结果](revalue_generic_highlight_tvsum_val10_results_2026-11-10.md)、[事后失败分析](revalue_generic_highlight_tvsum_failure_analysis_2026-11-10.md)。本轮不推送远程。
