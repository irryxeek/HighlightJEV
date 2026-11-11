# 文档索引

## 最新：VideoJev-4B Agent 框架与设计讨论（2026-11-12）

- [v4 框架图与说明：官方 Cached＋0–5 六档](../projects/videojev_agent_framework_20261112_v4/README.md)：[可编辑 SVG](../projects/videojev_agent_framework_20261112_v4/videojev_agent_framework_v4.svg)、[矢量 PDF](../projects/videojev_agent_framework_20261112_v4/videojev_agent_framework_v4.pdf)、[PNG 预览](../projects/videojev_agent_framework_20261112_v4/videojev_agent_framework_v4.png)及[生成源码](../projects/videojev_agent_framework_20261112_v4/create_diagram.py)。每个维度采用六个价值等级和独立的未知选项，输出完整概率及连续评分。
- [HighlightJEV：整片上下文、分维度判断与预算选片](highlightjev_design_discussion_2026-11-11.md)：同步官方 Cached 源码依据、七选项等级定义、0–5 期望公式、未知处理、计算量及待验证事项。
- [此前 v2 图稿](../projects/videojev_agent_framework_20261112_v2/README.md)保留历史内容；当前设计以上述 v4 为准。
- [此前的整片输入、记忆与 Jev 验证方案](revalue_fullvideo_memory_jev_next_plan_2026-11-10.md)及[来源核查记录](artifacts/revalue_fullvideo_memory_jev_plan_2026-11-10/source_audit.json)。历史计划保留原日期；后续讨论以 HighlightJEV 方案与框架图为准。

本次为图稿与文档发布。官方已有 Cached 实现，本项目的 4B 接入、七选项价值判断和回看策略尚待运行验证；没有新增实验推理或 GPU 任务。此前同日发布的 [TVSum 最新实验查看器说明](revalue_trace_viewer_tvsum_latest_2026-11-10.md)和[官方重要性标注参考说明](revalue_trace_viewer_tvsum_ground_truth_2026-11-10.md)继续保留；其中端口、测试和验证路径是 11 月 10 日的本地运行记录，不代表本次重新运行或已发布完整查看器源码。

## 此前：高光评分与本周组会汇报（2026-11-10）

- [十页可编辑PPT](presentations/ReVALUE_组会汇报_2026-11-10.pptx) · [两段汇报及范围说明](revalue_group_update_2026-11-10.md) · [讲稿、源页面与核验](presentations/revalue_weekly_highlight_20261110/README.md)。
- [TVSum全50条8B／27B对照](revalue_generic_highlight_tvsum_full50_8b27b_results_v2_2026-11-10.md)：修订8B55.9560、修订27B56.2622、REZE8B54.8919 Top-5 mAP，配对区间跨零；没有27B REZE对照。
- [最新关键贡献版后40条](revalue_generic_highlight_tvsum_new40_core_value_results_2026-11-10.md)、[mAP15／mAP50](revalue_generic_highlight_tvsum_core_map15_map50_2026-11-10.md)：Top-5为55.8007；完整同版本全50尚未完成。[补齐失败记账](revalue_generic_highlight_tvsum_full50_core_value_results_2026-11-10.md)不能当作新的全50模型性能。
- [Mr.HiSum十条评分迁移](revalue_generic_highlight_mrhisum10_core_results_2026-11-10.md)、[SVHighlights十四场27B结果](revalue_svhighlights_expand14_27b_results_2026-11-09.md)与[匹配比较](revalue_svhighlights_expand14_27b_comparison_2026-11-09.md)。

本次同步PPT、讲稿、全部新增根报告，以及所链接的小型结果表和案例材料。历史计划保留其日期；本次发布不运行实验，也不代表整个研究工作区的实验源码已全部同步。

<details>
<summary>本次同步的35份实验报告、分析与协议</summary>

- [Mr.HiSum 固定10条：8B新版价值评分小规模迁移协议](revalue_generic_highlight_mrhisum10_core_protocol_2026-11-10.md)
- [Mr.HiSum 固定10条：8B关键贡献价值评分迁移](revalue_generic_highlight_mrhisum10_core_results_2026-11-10.md)
- [Mr.HiSum 8B 固定10条：负样本与漏检案例审查](revalue_generic_highlight_mrhisum10_negative_cases_2026-11-10.md)
- [通用高光评分：10窗口结构化价值规则审计协议 v1](revalue_generic_highlight_rule_audit10_protocol_2026-11-10.md)
- [高光评分中间输出：10窗口规则审计结果](revalue_generic_highlight_rule_audit10_results_2026-11-10.md)
- [REZE 启发的通用高光密集评分 v1：实现与 CPU 验证](revalue_generic_highlight_scoring_v1_2026-11-10.md)
- [TVSum 27B：低 AP 案例诊断](revalue_generic_highlight_tvsum_27b_low_ap_cases_2026-11-10.md)
- [TVSum 8B：低 AP 根因复核与改进优先级](revalue_generic_highlight_tvsum_8b_improvement_diagnosis_2026-11-10.md)
- [TVSum 8B 新增40条：低 AP 案例与失败机制](revalue_generic_highlight_tvsum_8b_new40_low_ap_cases_2026-11-10.md)
- [TVSum val10：具体五维评分＋固定全片背景协议 v1](revalue_generic_highlight_tvsum_context10_protocol_2026-11-10.md)
- [TVSum val10：具体五维评分加入全片背景的结果](revalue_generic_highlight_tvsum_context10_results_2026-11-10.md)
- [TVSum 最新8B方法：mAP15 / mAP50补充结果](revalue_generic_highlight_tvsum_core_map15_map50_2026-11-10.md)
- [TVSum val10：具体五维标准密集评分对照协议 v1](revalue_generic_highlight_tvsum_detailed10_protocol_2026-11-10.md)
- [TVSum val10：具体五维标准评分结果](revalue_generic_highlight_tvsum_detailed10_results_2026-11-10.md)
- [TVSum 通用高光评分 v1：失败案例与下一步改进](revalue_generic_highlight_tvsum_failure_analysis_2026-11-10.md)
- [TVSum 全50视频：背景版与修订版，8B／27B执行协议 v1](revalue_generic_highlight_tvsum_full50_8b27b_protocol_2026-11-10.md)
- [TVSum 全50：固定背景下的价值标准与模型对照](revalue_generic_highlight_tvsum_full50_8b27b_results_2026-11-10.md)
- [TVSum 全50：固定背景下的价值标准与模型对照](revalue_generic_highlight_tvsum_full50_8b27b_results_v2_2026-11-10.md)
- [TVSum 全50：固定背景下的价值标准与模型对照](revalue_generic_highlight_tvsum_full50_8b_results_2026-11-10.md)
- [TVSum 最新8B关键贡献版：补齐10条并统一评全50](revalue_generic_highlight_tvsum_full50_core_value_protocol_2026-11-10.md)
- [TVSum 最新8B关键贡献版：补齐10条并统一评全50](revalue_generic_highlight_tvsum_full50_core_value_protocol_v2_2026-11-10.md)
- [TVSum 最新8B关键贡献版：全50条统一评价](revalue_generic_highlight_tvsum_full50_core_value_results_2026-11-10.md)
- [TVSum全50两版及27B：执行快照](revalue_generic_highlight_tvsum_full50_execution_2026-11-10.md)
- [TVSum50 27B启动修订 v2：保留零请求失败，继续原任务](revalue_generic_highlight_tvsum_full50_runtime_amendment_v2_2026-11-10.md)
- [TVSum 后40：关键贡献与品牌/场景门槛联合验证协议](revalue_generic_highlight_tvsum_new40_core_value_protocol_2026-11-10.md)
- [TVSum 后40：关键贡献目标与品牌/场景门槛实验](revalue_generic_highlight_tvsum_new40_core_value_results_2026-11-10.md)
- [通用高光评分 v1：TVSum val10 与 REZE 配对测试协议](revalue_generic_highlight_tvsum_val10_protocol_2026-11-10.md)
- [通用高光评分 v1：TVSum val10 与 REZE 配对结果](revalue_generic_highlight_tvsum_val10_results_2026-11-10.md)
- [TVSum val10：最新价值标准完整评分对照协议 v1](revalue_generic_highlight_tvsum_value_gate10_protocol_2026-11-10.md)
- [TVSum val10：最新价值标准完整评分结果](revalue_generic_highlight_tvsum_value_gate10_results_2026-11-10.md)
- [通用高光：弱线索降权与单维充分贡献判定协议 v1](revalue_generic_highlight_value_gate10_protocol_2026-11-10.md)
- [弱线索降权与单维充分贡献：10窗口诊断结果](revalue_generic_highlight_value_gate10_results_2026-11-10.md)
- [SVHighlights 十四视频扩测：27B 稀疏记忆与核验](revalue_svhighlights_expand14_27b_comparison_2026-11-09.md)
- [SVHighlights 稀疏事实记忆与核验：十四视频27B测试结果](revalue_svhighlights_expand14_27b_results_2026-11-09.md)
- [TVSum mAP15 / mAP50 补充评价结果（2026-11-10）](revalue_tvsum_map15_map50_supplement_2026-11-10.md)

</details>


## 此前：按会议纪要重整的本周汇报（2026-11-10制作）

- [会议对照修订报告](revalue_weekly_progress_2026-11-03_to_2026-11-09_meeting_revision.md) · [16页可编辑PPT](presentations/ReVALUE_实验进度汇报_2026-11-03至11-09_会议对照修订版.pptx) · [讲稿与源页面](presentations/revalue_weekly_meeting_revision_20261110/README.md)。
- [SVHighlights七视频结果](revalue_svhighlights_sparse7_v1_1_results_2026-11-09.md)、[七视频协议](revalue_svhighlights_sparse7_protocol_2026-11-09.md)、[v1.1执行记录](revalue_svhighlights_sparse7_execution_v1_1_2026-11-09.md)、[启动恢复记录](revalue_svhighlights_sparse7_startup_recovery_v1_1_2026-11-09.md)。
- [十四视频27B扩测协议](revalue_svhighlights_expand14_27b_protocol_2026-11-09.md)、[执行快照](revalue_svhighlights_expand14_27b_execution_2026-11-09.md)。快照保留原日期，尚无本轮最终结果，不能视作当前实时监控。
- 历史七视频[初版执行](revalue_svhighlights_sparse7_execution_2026-11-09.md)与[初版结果记录](revalue_svhighlights_sparse7_results_2026-11-09.md)保留；完成结论以上述v1.1结果为准。

本次一并补齐9份新增报告和完整汇报材料。没有新增实验推理，也没有改变现有实验；已有未发布实验源码仍是独立的代码发布事项。


## 同周期初稿：本周记忆与价值核验进展（2026-11-03–09）

- [本周总结报告](revalue_weekly_progress_2026-11-03_to_2026-11-09.md) · [16页可编辑PPT](presentations/ReVALUE_组会汇报_2026-11-03至11-09.pptx) · [讲稿、源页面与精选帧证据](presentations/revalue_weekly_20261109/README.md)。
- [固定40视频／200对核验结果](revalue_tvsum_value15_consistency40_results_2026-11-09.md)、[原50对合法率下降诊断](revalue_tvsum_value15_consistency50_diagnosis_2026-11-09.md)。
- [事实保真与时间绑定结果](revalue_tvsum_fact_local_40v_results_2026-11-07.md)、[价值读取诊断](revalue_tvsum_value_read_40v_diagnosis_2026-11-07.md)、[初版全50视频结果](revalue_tvsum_relative_full50_27b_v1_results_2026-11-05.md)。
- [QFVS固定40查询](revalue_qfvs_memory_read_results_2026-11-06.md)、[Mr.HiSum固定40视频](revalue_mrhisum_memory_read_results_2026-11-06.md)、[通用高光详细价值标准](revalue_generic_highlight_value_v4_2026-11-06.md)。

当前没有稳定超过无文字记忆Direct参照的证据，详细V15未超过普通核验。固定40视频是多轮开发范围，QFVS／Mr.HiSum也不是全量；旧val10与当前40条前10条不同。初版全50汇总包含原train40和val10，不是独立官方test50。最新500次调用已结束，历史执行快照保留原日期；下一步建议尚待审阅。

本次发布PPT、讲稿、页面源文件、精选证据及以下82份尚未发布的相关报告。实验源码、模型、完整视频和运行缓存不属于本次文档交付；明确标注的本地资料不冒充已上传附件。

<details>
<summary>本次补齐的82份详细报告、方案和历史执行记录</summary>

- [当前高光价值提示词：已有细化与尚未验证的部分](highlight_value_prompt_current_2026-11-06.md)
- [Qwen3.8-27B 权重下载记录](qwen3_8_27b_download_2026-11-03.md)
- [反证误用诊断与下一步修复方案 v2](revalue_counterevidence_logic_repair_plan_v2_2026-11-08.md)
- [ReVALUE 事实—价值联合记忆：近期工作对照与下一步设计](revalue_fact_value_memory_design_2026-11-06.md)
- [通用高光价值判断 v4：细化标准、证据记忆与 TVSum40 对照](revalue_generic_highlight_value_v4_2026-11-06.md)
- [ReVALUE 当前记忆机制与相关工作调研](revalue_memory_mechanism_and_related_work_2026-11-06.md)
- [Mr.HiSum固定40视频实验：事实记忆、读取与摘要导出诊断](revalue_mrhisum_memory_diagnosis_2026-11-07.md)
- [Mr.HiSum 40视频记忆读取实验启动记录](revalue_mrhisum_memory_read_execution_2026-11-06.md)
- [Mr.HiSum 固定40视频：事实记忆读取迁移协议 v1](revalue_mrhisum_memory_read_protocol_2026-11-06.md)
- [Mr.HiSum 固定40视频：事实记忆读取策略迁移结果](revalue_mrhisum_memory_read_results_2026-11-06.md)
- [Mr.HiSum固定40视频：运行中输出预览](revalue_mrhisum_partial_outputs_20261106_174216.md)
- [ReVALUE 下一步实验方案：高光价值证据与全视频记忆](revalue_next_experiment_plan_2026-11-04.md)
- [QFVS 40查询记忆读取对照：启动记录](revalue_qfvs_memory_read_execution_2026-11-06.md)
- [QFVS固定40查询：事实记忆读取策略对照协议 v1](revalue_qfvs_memory_read_protocol_2026-11-06.md)
- [QFVS 固定40查询：事实记忆读取策略迁移结果](revalue_qfvs_memory_read_results_2026-11-06.md)
- [ReVALUE 当前实验结果分析与下一步方案](revalue_results_analysis_and_next_plan_2026-11-07.md)
- [TVSum 样本接入 ReVALUE 前端对比页面](revalue_trace_viewer_tvsum_2026-11-06.md)
- [TVSum 固定 8 对：原子可观察性与动作前提 v3 验证分析](revalue_tvsum_atom_observability8_analysis_2026-11-08.md)
- [TVSum 原子可观察性 v3：执行收据](revalue_tvsum_atom_observability8_execution_2026-11-08.md)
- [TVSum 原子可观察性与动作前提 v3：固定 8 对验证协议](revalue_tvsum_atom_observability8_protocol_2026-11-08.md)
- [TVSum 固定 8 例原子可观察性与前提依赖 v3：运行结果](revalue_tvsum_atom_observability8_results_2026-11-08.md)
- [TVSum候选复核对照：结果分析与案例结论](revalue_tvsum_candidate_verifier10_analysis_2026-11-07.md)
- [TVSum 固定10视频：普通复核与详细价值复核执行记录](revalue_tvsum_candidate_verifier10_execution_2026-11-07.md)
- [TVSum候选复核：增益来源、替代质量与证据问题](revalue_tvsum_candidate_verifier10_failure_diagnosis_2026-11-07.md)
- [TVSum固定10条候选核验：诊断结果](revalue_tvsum_candidate_verifier10_results_2026-11-07.md)
- [TVSum 反证修复 v2：固定 8 例结果与失败定位](revalue_tvsum_counterevidence8_analysis_2026-11-08.md)
- [TVSum 固定 8 例反证修复 v2：执行收据](revalue_tvsum_counterevidence8_execution_2026-11-08.md)
- [TVSum 原子反证修复 v2：固定 8 例执行协议](revalue_tvsum_counterevidence8_protocol_2026-11-08.md)
- [TVSum 固定 8 例原子反证修复 v2：运行结果](revalue_tvsum_counterevidence8_results_2026-11-08.md)
- [TVSum 固定10条：D-1fps 对照执行记录](revalue_tvsum_dense_direct_10v_execution_2026-11-07.md)
- [TVSum 固定10条：D-1fps 与事实/价值记忆对照](revalue_tvsum_dense_direct_10v_results_2026-11-07.md)
- [TVSum 1 fps 记忆测试：固定10条执行记录](revalue_tvsum_dense_memory_10v_execution_2026-11-06.md)
- [TVSum 1 fps 记忆测试：固定原40清单前10条](revalue_tvsum_dense_memory_10v_results_2026-11-06.md)
- [TVSum 固定10条：1 fps事实／价值记忆结果诊断](revalue_tvsum_dense_memory_diagnosis_2026-11-07.md)
- [TVSum固定40条：事实保真与时间绑定改进执行记录](revalue_tvsum_fact_local_40v_execution_2026-11-07.md)
- [TVSum固定40条：事实保真与时间绑定模块对照结果](revalue_tvsum_fact_local_40v_results_2026-11-07.md)
- [事实记忆＋后置价值 verifier：接入分析与下一步](revalue_tvsum_fact_verifier_integration_analysis_2026-11-08.md)
- [TVSum：仅事实记忆＋后置价值 verifier 的离线接入协议 v1](revalue_tvsum_fact_verifier_integration_protocol_2026-11-08.md)
- [TVSum：事实记忆＋后置价值 verifier 接入结果](revalue_tvsum_fact_verifier_integration_results_2026-11-08.md)
- [TVSum固定六案例：事实、时间与观看理由审计](revalue_tvsum_fixed6_case_audit_2026-11-07.md)
- [TVSum 全50视频结果分析与下一步实验方案](revalue_tvsum_full50_analysis_and_next_plan_2026-11-06.md)
- [TVSum高光价值与记忆：27B三臂实验当前执行记录v1.1](revalue_tvsum_highlight_memory_27b_v1_1_execution_2026-11-04.md)
- [ReVALUE TVSum：27B Direct-HD与事实／价值记忆对照](revalue_tvsum_highlight_memory_27b_v1_1_results_2026-11-04.md)
- [TVSum高光价值与记忆：27B三臂实验执行记录](revalue_tvsum_highlight_memory_27b_v1_execution_2026-11-04.md)
- [TVSum 固定十视频三组对照：11月5日启动记录](revalue_tvsum_highlight_memory_27b_v2_1_execution_2026-11-05.md)
- [ReVALUE TVSum v2.1：相同修复条件下重新启动三臂对照](revalue_tvsum_highlight_memory_27b_v2_1_results_2026-11-05.md)
- [TVSum 固定十视频：引用时间与截断修复、三组重跑](revalue_tvsum_highlight_memory_27b_v2_repair_and_execution_2026-11-04.md)
- [ReVALUE TVSum v2：时间引用与输出长度修复后的三臂对照](revalue_tvsum_highlight_memory_27b_v2_results_2026-11-04.md)
- [ReVALUE TVSum：相对高光选片 F-relative / FV-relative 对照](revalue_tvsum_highlight_relative_27b_v1_results_2026-11-05.md)
- [TVSum 事实读取对照执行记录](revalue_tvsum_memory_read_execution_2026-11-06.md)
- [TVSum 原40视频：仅改变事实读取策略](revalue_tvsum_memory_read_protocol_2026-11-06.md)
- [TVSum 原40视频：事实记忆读取策略对照结果](revalue_tvsum_memory_read_results_2026-11-06.md)
- [TVSum 八小时自动执行安排](revalue_tvsum_overnight_execution_2026-11-06.md)
- [TVSum 八小时自动任务结果](revalue_tvsum_overnight_results_2026-11-06.md)
- [TVSum 原 10 条：反证约束修复与旧理由可见性对照](revalue_tvsum_reason_visibility10_analysis_2026-11-08.md)
- [TVSum 旧理由可见性对照：执行记录](revalue_tvsum_reason_visibility10_execution_2026-11-08.md)
- [TVSum：反证约束修复后的旧理由可见性对照 v1](revalue_tvsum_reason_visibility10_protocol_2026-11-08.md)
- [TVSum固定10条：旧选片理由可见性对照](revalue_tvsum_reason_visibility10_results_2026-11-08.md)
- [ReVALUE TVSum 全 50 视频：F-relative / FV-relative](revalue_tvsum_relative_full50_27b_v1_results_2026-11-05.md)
- [TVSum全50视频：F-relative／FV-relative执行记录](revalue_tvsum_relative_full50_execution_2026-11-05.md)
- [TVSum 固定十视频：F / FV 离线案例审计](revalue_tvsum_relative_offline_audit_2026-11-05.md)
- [TVSum：相对价值判据的固定十视频对照](revalue_tvsum_relative_plan_and_execution_2026-11-05.md)
- [TVSum 40视频：V15一致性修复对照执行记录](revalue_tvsum_value15_consistency40_execution_2026-11-09.md)
- [TVSum40：V15一致性与负向依赖修复对照 v2](revalue_tvsum_value15_consistency40_protocol_2026-11-09.md)
- [TVSum固定40条：V15一致性修复与三组核验对照](revalue_tvsum_value15_consistency40_results_2026-11-09.md)
- [TVSum V15修复后合法率下降：原50对诊断与下一步修复方案](revalue_tvsum_value15_consistency50_diagnosis_2026-11-09.md)
- [TVSum V15：17条无效响应、选片差异与下一步修复方案](revalue_tvsum_value15_verifier10_diagnosis_2026-11-09.md)
- [TVSum10：逐项 15 问价值 verifier 对照执行记录](revalue_tvsum_value15_verifier10_execution_2026-11-08.md)
- [TVSum10：逐项 15 问价值 verifier 与普通 verifier 对照 v1](revalue_tvsum_value15_verifier10_protocol_2026-11-08.md)
- [TVSum固定10条：普通核验与15题逐项价值核验结果](revalue_tvsum_value15_verifier10_results_2026-11-08.md)
- [TVSum40 详细价值记忆对照：执行记录](revalue_tvsum_value_detail_execution_2026-11-06.md)
- [TVSum 原40视频：详细价值判据与简短判据的配对结果](revalue_tvsum_value_detail_results_2026-11-06.md)
- [TVSum固定10条：价值记忆读取修复执行记录](revalue_tvsum_value_read_10v_execution_2026-11-07.md)
- [TVSum固定10条：价值记忆读取修复对照](revalue_tvsum_value_read_10v_results_2026-11-07.md)
- [TVSum固定40视频：价值记忆读取对照诊断](revalue_tvsum_value_read_40v_diagnosis_2026-11-07.md)
- [TVSum固定40条：1 fps记忆与V读取扩展执行记录](revalue_tvsum_value_read_40v_execution_2026-11-07.md)
- [TVSum固定40条：1 fps记忆与价值读取扩展结果](revalue_tvsum_value_read_40v_results_2026-11-07.md)
- [Qwen3.8-27B 固定20条 Q / Q+V 启动记录](revalue_value_qvqv20_qwen3_8_27b_v1_1_execution_2026-11-04.md)
- [Qwen3.8-27B 固定20条 Q/Q+V 结果](revalue_value_qvqv20_qwen3_8_27b_v1_1_results_2026-11-04.md)
- [Qwen3.8-27B 固定20条 Q / Q+V 执行记录（当前四卡运行）](revalue_value_qvqv20_qwen3_8_27b_v1_execution_2026-11-04.md)
- [Qwen3.8-27B 固定20条 Q/Q+V 结果](revalue_value_qvqv20_qwen3_8_27b_v1_results_2026-11-04.md)
- [ReVALUE 本周实验进度与结果](revalue_weekly_progress_2026-11-03_to_2026-11-09.md)

</details>

## 此前：Verifier 与 32B 同样本结果（2026-11-03）

- [最新汇报](revalue_progress_and_results_2026-11-03.md) · [15 页可编辑 PPT](presentations/ReVALUE_实验进度与结果_2026-11-03_更新版.pptx) · [PDF 预览](presentations/ReVALUE_实验进度与结果_2026-11-03_更新版.pdf)。
- [相关工作到价值判断单页](presentations/ReVALUE_相关工作到价值判断设计_2026-11-03.pdf) · [逐页讲稿与源页面](presentations/revalue_progress_20261103/README.md)。
- [8B 完整 100 条结果](revalue_value_qvqv100_v2_4_results_2026-11-02.md)、[32B 前 20 条与 8B 配对结果](revalue_value_qvqv20_32b_v1_2_results_2026-11-03.md)、[32B 事实生成诊断](revalue_32b_fact_generation_diagnosis_2026-11-03.md)。
- [相关工作调研](revalue_value_verification_related_work_2026-10-31.md)、[价值判断设计 v2](revalue_value_judgement_design_v2_2026-10-31.md)、[GT / Direct 视频审查](revalue_trace_viewer_video_playback_2026-11-03.md)。

8B Q/Q+V v2.4 完成固定 100 条 query 的 278 次判断，273 条合法；错误召回率为 7.06% / 9.41%。32B 已完成原清单前 20 条（37 候选、74 次），同样本 Q/Q+V 错误召回率为 4% / 0%，65/74 次为证据不足；尚未证明检错或 grounding 提升。新增文献到价值判断的设计来源、32B 事实生成诊断和 GT / Direct 视频审查说明。

本次同时补齐以下详细报告与历史执行快照。原文中的“本轮未推送”描述撰写当时状态；此次发布以用户后续推送指令为准。大视频、模型、输入帧缓存和未选公开的运行记录仍保留本地，本地资料引用已明确标注。

- [后续主线确认：Query 驱动的时序 Grounding](temporal_grounding_mainline_2026-10-29.md)
- [REZE Direct：固定 QV100 定位对照结果](reze_direct_grounding_qv100_results_2026-10-30.md)
- [REZE-Direct：固定 QV100 定位协议 v1](reze_direct_grounding_qv100_protocol_v1_2_2026-10-30.md)
- [REZE-Direct：固定 QV100 定位协议 v1](reze_direct_grounding_qv100_protocol_v1_2026-10-30.md)
- [REZE-Direct：固定 QV100 定位协议 v1](reze_direct_grounding_qv100_protocol_v1_1_2026-10-30.md)
- [REZE Direct：固定 QV100 执行记录](reze_direct_grounding_qv100_execution_2026-10-30.md)
- [ReVALUE Verifier 下一步改进分析与建议方案](revalue_verifier_improvement_plan_2026-10-31.md)
- [多维价值判断与区间验证：相关工作调研](revalue_value_verification_related_work_2026-10-31.md)
- [ReVALUE verifier v2.1：状态与未知原因联动修复](revalue_value_state_schema_fix_v2_1_2026-11-01.md)
- [ReVALUE verifier v2.3：重复引用与未确认依赖修复](revalue_value_reference_dependency_fix_v2_3_2026-11-02.md)
- [ReVALUE verifier v2.4：引用去重修改与离线重验](revalue_value_reference_dedup_v2_4_2026-11-02.md)
- [ReVALUE 32B：原清单前20条query的Q/QV结果](revalue_value_qvqv20_32b_v1_2_results_2026-11-03.md)
- [ReVALUE 32B：前20条query运行范围更新](revalue_value_qvqv20_32b_v1_2_execution_2026-11-03.md)
- [ReVALUE verifier v2.4：依赖约束与引用去重的固定 QV100 配对实验结果](revalue_value_qvqv100_v2_4_results_2026-11-02.md)
- [ReVALUE v2.2：事实与证据绑定修复的固定 QV100 对照](revalue_value_qvqv100_v2_2_protocol_2026-11-02.md)
- [ReVALUE verifier v2.2：事实与证据引用绑定修复的固定 QV100 配对实验结果（多卡续接）](revalue_value_qvqv100_v2_2_parallel_results_2026-11-02.md)
- [ReVALUE v2.2 Q/Q+V 多卡续接执行记录](revalue_value_qvqv100_v2_2_parallel_execution_2026-11-02.md)
- [ReVALUE v2.2 Q/Q+V：多卡调度补充协议](revalue_value_qvqv100_v2_2_parallel_amendment_2026-11-02.md)
- [ReVALUE v2.2 固定100条 Q/Q+V 对照执行记录](revalue_value_qvqv100_v2_2_execution_2026-11-02.md)
- [ReVALUE verifier v2.1：字段联动修复后的固定 QV100 配对实验结果](revalue_value_qvqv100_v2_1_results_2026-11-01.md)
- [ReVALUE Q/Q+V v2.1：字段联动修复的固定 QV100 对照](revalue_value_qvqv100_v2_1_protocol_2026-11-01.md)
- [ReVALUE Q/Q+V v2.1 修复验证执行记录](revalue_value_qvqv100_v2_1_execution_2026-11-01.md)
- [ReVALUE 价值提示 Q/QV：固定 QV100 配对实验结果](revalue_value_qvqv100_results_2026-10-31.md)
- [ReVALUE Q vs Q+V：固定 QV100 价值引导对照 v2](revalue_value_qvqv100_protocol_2026-10-31.md)
- [ReVALUE Q / Q+V 固定 QV100：实现、冻结与排队记录](revalue_value_qvqv100_execution_2026-10-31.md)
- [ReVALUE 32B 固定100条验证：执行状态](revalue_value_qvqv100_32b_v1_execution_2026-11-02.md)
- [ReVALUE verifier 32B v1.2：取消资源额度后的固定 QV100 重跑结果](revalue_value_qvqv100_32b_v1_2_results_2026-11-03.md)
- [ReVALUE 32B Q/QV：取消额度后固定100条重跑记录](revalue_value_qvqv100_32b_v1_2_execution_2026-11-03.md)
- [ReVALUE verifier 32B v1.1：固定 QV100 的 Q/QV 模型对照结果](revalue_value_qvqv100_32b_v1_1_results_2026-11-03.md)
- [ReVALUE 32B 固定 QV100：三卡恢复执行记录 v1.1](revalue_value_qvqv100_32b_v1_1_execution_2026-11-03.md)
- [ReVALUE 价值判断设计 v2：面向 Query 的可核查价值证据](revalue_value_judgement_design_v2_2026-10-31.md)
- [GT 标注与 Qwen Direct 预测的视频回放](revalue_trace_viewer_video_playback_2026-11-03.md)
- [前端新增 Direct 与 Verifier 对照](revalue_trace_viewer_direct_comparison_2026-11-03.md)
- [ReVALUE 推理过程查看页面](revalue_trace_viewer_2026-10-30.md)
- [ReVALUE 最新实验进度与结果](revalue_progress_and_results_2026-11-03.md)
- [ReVALUE 当前实验进度与结果](revalue_progress_and_results_2026-11-02.md)
- [ReVALUE 后续实验的 GPU 调度偏好](revalue_gpu_scheduling_preference_2026-11-02.md)
- [ReVALUE 区间 Verifier v1.1：固定 QV100 验证结果](revalue_direct_verifier_results_2026-10-30.md)
- [REZE Direct + ReVALUE Verifier：实现与CPU准备收据](revalue_direct_verifier_preparation_2026-10-30.md)
- [ReVALUE 区间 Verifier：REZE Direct 固定 QV100 协议 v1](revalue_direct_verifier_plan_v1_2026-10-30.md)
- [ReVALUE 区间 Verifier：REZE Direct 固定 QV100 协议 v1.1](revalue_direct_verifier_plan_v1_1_2026-10-30.md)
- [ReVALUE Direct Verifier 离线诊断 v1](revalue_direct_verifier_offline_diagnosis_v1_2026-10-30.md)
- [ReVALUE 区间 Verifier v1.1 执行记录](revalue_direct_verifier_execution_2026-10-30.md)
- [32B 与 8B 事实生成差异：离线核查](revalue_32b_fact_generation_diagnosis_2026-11-03.md)
- [ReVALUE 当前任务交接：REZE Direct + 区间 Verifier](handoff_revalue_verifier_2026-10-30.md)

## 此前：组会后 Direct 与 Grounding 进展（2026-10-28–30）

- [工作总结](progress_after_meeting_2026-10-27_to_2026-10-30.md)、[12 页可编辑 PPT](presentations/ReVALUE_Grounding实验进展_2026-10-28至10-30.pptx)、[PDF 预览](presentations/ReVALUE_Grounding实验进展_2026-10-28至10-30.pdf)、[讲稿与可编辑源页面](presentations/revalue_grounding_progress_20261030/README.md)。
- [Grounding 反例单页 PPT：qid448](presentations/Grounding反例_qid448_单页介绍_2026-10-30.pptx)、[讲稿与原帧证据](presentations/qv_grounding_counterexample_qid448_20261030/README.md)：标注 92–112 秒为鸡舍，预测 130–145 秒落到道路与花景，IoU=0。属于助手初筛案例；条件核验与重新定位的修正收益尚未验证。
- [Grounding 主线确认](temporal_grounding_mainline_2026-10-29.md)：以匹配 query 的事件起止区间为主要任务；定位 R1 与高光排序 mAP 分开。
- [Direct pilot 结果](qwen_direct_pilot_results_2026-10-28.md)：QV20 与 TVSum5 的有效整表输出全部视频内同分；[原协议](qwen_direct_pilot_protocol_v1_2026-10-28.md)、[启动兼容修订](qwen_direct_pilot_runtime_amendment_v1_1_2026-10-28.md)、[OOM 来源链](qwen_direct_oom_diagnosis_2026-10-28.md)。TVSum Direct 仍为 5/10，未补跑。
- [显式时间键结果](qwen_direct_temporal_results_2026-10-28.md)：20/20 完成，仍在视频内同分；[冻结协议](qwen_direct_temporal_output_protocol_v1_2026-10-28.md)、[准备收据](qwen_direct_temporal_preparation_receipt_v1_2026-10-28.md)。
- [单目标粒度结果](qwen_direct_granularity_results_2026-10-29.md)：40 次完成，20 对固定目标中 11 对分值不同；该比例不是准确率，未计算新全网格指标。见[冻结协议](qwen_direct_granularity_protocol_v1_2026-10-28.md)。
- [Grounding QV20 结果](qwen_direct_grounding_results_2026-10-29.md)：20/20 合法，R1@0.5 / R1@0.7 为 70% / 50%；[冻结协议](qwen_direct_grounding_protocol_v1_2026-10-29.md)。
- [新增 100 条结果](qwen_direct_grounding_expand100_results_2026-10-29.md)：96 次尝试、94 条合法，1 OOM、1 非法区间、4 未尝试；完整分母 R1 为 42% / 28%，52 条合法反例。见[原协议](qwen_direct_grounding_expand100_protocol_v1_2026-10-29.md)、[冷启动分批修订](qwen_direct_grounding_expand100_runtime_amendment_v1_1_2026-10-29.md)及[初始结果审阅](qwen_direct_grounding_expand100_review_2026-10-29.md)。两批均为 train 开发诊断，不是官方全量验证。
- [52 条反例的语义核查](qwen_direct_grounding_52_counterexample_analysis_2026-10-29.md)：助手初筛 22 条较明确错误、15 条标注／范围疑点、10 条混合、5 条证据不足；[逐例数据与五组代表证据](../comparisons/qwen_direct/grounding_expand100_case_audit_2026-10-29/README.md)。发布 GT 与原指标未更改，仍待独立人工复核，尚无 Agent 修复收益。

本次同步 18 份本阶段报告与方案，以及 PPT、PDF、讲稿和页面源文件；仅更新文档和精选证据，未新增实验。原始运行缓存、模型、完整视频和新运行器代码不属于这次汇报交付；相关引用明确标为本地材料。历史协议中的待授权状态按原日期保留，后续执行事实以对应结果报告为准。

## 上次组会及历史阶段记录

- [本周实验进度报告（2026-10-21–27）](weekly_experiment_progress_2026-10-21_to_2026-10-27.md)、[更新版 15 页 PPT](presentations/ReVALUE_实验进度汇报_2026-10-21至10-27_v2_TaskSpec补充.pptx)及[原 14 页 PPT](presentations/ReVALUE_实验进度汇报_2026-10-21至10-27.pptx)：更新版增加 TaskSpec 介绍，讲稿见[交付目录](presentations/revalue_weekly_2026-10-21_to_2026-10-27/README.md)。

- [四态比较器诊断记录（2026-10-27）](revalue_four_state_comparator_diagnosis_2026-10-27.md)：QV / TVSum 的状态分布、双向胜负、回看触发和待验证原因；基于既有记录，未新增实验模型调用。

- [TVSum 离线诊断 v1（2026-10-27）](revalue_tvsum_offline_diagnosis_v1_2026-10-27.md)：零新增调用；400 份旧比较、448 条事实来源核验；分解草稿遗漏与容量驱逐，19 项 CPU 测试通过。[TaskSpec 单变量协议](revalue_tvsum_taskspec_protocol_v1_2026-10-27.md)仅准备，400 次/2,457,600 token/1 GPUh 为待授权独立建议。

- [ReVALUE / TVSum val10 跨数据集结果（2026-10-27）](revalue_tvsum_transfer_results_2026-10-27.md)：四组、670 次完成；B0 61.32、P_pair 58.38，C_direct4/E_memory 与 B0 逐项相同。含逐视频结果、同分敏感性、成本与证据问题；[冻结协议](revalue_tvsum_transfer_protocol_2026-10-27.md)。

- [阶段实验成果与问题总结（2026-10-27）](experimental_progress_and_issues_2026-10-27.md)：全量候选复评收益、ReVALUE 记忆与回看结果、跨数据集成绩、可靠性瓶颈和下一步顺序。

- [SVHighlights 七场结果](reze_svhighlights_pilot7_results_2026-10-27.md)：补齐已于 10 月 23 日完成的原方法测试，HL-mAP 16.27；输入与预算限制单列。

- [ReVALUE 定向物体核查结果（2026-10-27）](revalue_object_presence_results_2026-10-27.md)：60/60 次完成，两臂状态完全相同；14 个明确正例全部保留，但六个模糊例均未弃答，内容关未通过。见[冻结协议](revalue_object_presence_protocol_2026-10-26.md)。

- [ReVALUE 来源压缩与观察输出探针结果（2026-10-26）](revalue_memory_compaction_results_2026-10-26.md)：14 视图节省 25.30% token，累计补回 104 个旧事实 ID；37/37 输出对照完成，135 项 CPU 测试通过。句子完整性改善但观察内容未通过，暂停 A/B/C 比较。见[CPU 协议](revalue_memory_compaction_protocol_2026-10-26.md)及[输出探针协议](revalue_observer_output_probe_protocol_2026-10-26.md)。

- [ReVALUE 下一轮实验计划：来源压缩与旧证据保留（2026-10-26）](revalue_next_experiment_plan_2026-10-26.md)：保留原设计快照；本轮已完成 CPU 容量与 37 次输出探针，后续审查将内容关前置于 A/B/C 比较，实际决定见最新结果。

- [ReVALUE 来源绑定修复与单帧验证（2026-10-26）](revalue_frame_grounding_repair_results_2026-10-26.md)：672/672 次完成，86 项测试通过；来源接口和空事实过滤已修复，单帧观察仍为诊断用途，尚无新 HD 指标。见[冻结协议](revalue_frame_grounding_repair_protocol_2026-10-26.md)。

- [ReVALUE 离线诊断与 28 次观察对照结果（2026-10-26）](revalue_r2_observation_probe_results_2026-10-26.md)：已执行下一步，技术检查通过，查询盲观察仍有来源/时间错配，未晋级评分重跑；[逐案例诊断](revalue_r2_offline_diagnosis_2026-10-26.md)、[冻结协议](revalue_r2_observation_probe_protocol_2026-10-26.md)。

- [ReVALUE 现阶段实验方案（2026-10-26）](revalue_current_experiment_plan_2026-10-26.md)：上午整理快照；完整框架、R2 结果、R3 功能验收与扩大条件。后续已完成诊断，下一轮细化安排见本页顶部。

- [ReVALUE R2 修复启动记录（2026-10-26）](revalue_r2_repair_execution_2026-10-26.md)：保留启动快照；现已完成 100/100、零技术回退、7 条配对观察，精度未过门槛，结果见上方方案。[诊断](revalue_r2_diagnosis_2026-10-26.md)、[修复协议](revalue_r2_repair_protocol_v3_2026-10-26.md)。

- [ReVALUE R2 旧轮启动记录（2026-10-25）](revalue_r2_execution_2026-10-25.md)：v2 启动快照；该轮现已完成，问题与修复见上方新记录。

- [ReVALUE R1 结果（2026-10-25）](revalue_r1_results_2026-10-25.md)：20/20 完成；决策记忆与直接比较持平，尚未证明记忆收益。

- [ReVALUE R2 执行协议（2026-10-25）](revalue_r2_protocol_2026-10-25.md)：100 条、五条件、配对观察、940 次缓存核验与共享多卡预算。

- [GPU 使用约定（2026-10-25）](gpu_resource_policy_2026-10-25.md)：后续新运行使用任意空闲卡，可拆分任务优先并行；不修改现有冻结运行。

- [ReVALUE R0 故障修复与验证（2026-10-25）](revalue_r0_repair_results_2026-10-25.md)：v1 故障根因、紧凑输出、引用约束与显存修复；当时 37 项测试与原 20 条检查通过，v5 修正全 unknown 退化；R1 启动段落为历史快照。

- [工程修复协议 v2](revalue_r0_repair_protocol_v2_2026-10-25.md)：160 次严格复用、140 次新验证及不重置的累计预算。

- [ReVALUE R0/R1 启动记录（2026-10-25）](revalue_r01_execution_2026-10-25.md)：保留 v1 准备快照，当前状态见上方修复报告。

- [QFVS 全量 180 查询结果（2026-10-25）](reze_qfvs_full_results_2026-10-25.md)：两组全量完成；180/176 查询五组对照、成本和结论边界。

- [ReVALUE 执行方案 v3（2026-10-23）](revalue_execution_plan_v3_2026-10-23.md)：总体设计基线；对齐原版图解的五类价值、两层记忆、四态比较、四类补看、事件选择和完整边界。原预算、门槛与冻结内容保留，当前顺序见上方现阶段方案。

- [QFVS 全量验证执行记录（2026-10-23）](reze_qfvs_full_validation_2026-10-23.md)：全部 180 查询的冻结配置、双卡分工、五组对照、176 条单独报告与自动恢复。

- [下一阶段执行记录（2026-10-23）](reze_next_stage_execution_status_2026-10-23.md)：前一轮启动快照；QFVS 四查询、SVHighlights 七场及 QV V1 已完成，Agent 四组尚未运行。

- [历史执行方案 v2（2026-10-23）](reze_next_stage_execution_plan_v2_2026-10-23.md)：保留原实验引用；未启动的 Agent 部分由 v3 替代，文中的进度和五类价值待定描述属于历史快照。

- [数据集特点、输入输出与评价指标](datasets_inputs_outputs_metrics_2026-10-22.md)：六个数据集的任务区别、标注含义、当前适配协议与实验范围。

- [QFVS 概念提示与时间选择优化](reze_qfvs_adaptation_2026-10-22.md)：固定四查询的配对消融；原分数时间选择 F1 为 40.41，新提示运行与 GPU 迁移见最新执行记录。

更新日期：2026-10-27。R2 观察组仍为 mAP / Hit@1 44.41 / 71.00。最新完成 60 次定向物体核查：两臂均与助手参考一致 24/30，未通过内容关。此前压缩容量通过；尚无新 HD 指标，未启动 A/B/C、100 条复核或 R3/R4。历史计划与启动快照按原日期保留。

- [实验实现与复现入口](reproduction_index.md)：代码、配置、数据条件、测试与结果对应表。
- [仓库代码补齐报告](repository_completion_2026-10-22.md)：新增实现、部署修复、验证结果和发布边界。

- [实验结果汇总报告](experimental_results_report_2026-10-22.md)：完整实验、开发对照、跨数据集结果、成本和适配分析。
- [会议纪要后的推进计划](next_steps_after_meeting_2026-10-22.md)：候选覆盖、同预算定向补证、长视频粗到细及模块消融，新实验尚未启动。
- [报告同步发布约定](report_publication_workflow.md)：以后每次推送包含新增或修改的报告、方案和索引；[来源及公开文件哈希](report_publication_manifest.json)记录本次覆盖范围。

## REZE 完整结果与原执行方案

| 文档 | 用途 |
|---|---|
| [完整 validation 结果](reze_fullval_results_2026-10-20.md) | 1,550 查询，B0 / P_abs / P_pair 的 VeryGood mAP 为 42.99 / 43.57 / 43.76，Hit@1 为 71.68 / 74.06 / 76.84。 |
| [结果包与 CPU 复算](../comparisons/qvhighlights/reze_fullval_2026-10-20/README.md) | 预测、逐查询比较、成本、冻结代码与来源哈希。 |
| [全量执行记录](reze_fullval_execution_2026-10-20.md) | 完成状态、范围、冻结配置和成本记录。 |
| [A 阶段结果](reze_stage_a_results_2026-10-19.md) | 固定 explore100 未通过原门槛的历史结论。 |
| [A 阶段执行状态](reze_execution_status_2026-10-19.md) | 工程修复、检查和当时的停止决定。 |
| [原执行方案 v1](reze_execution_plan_2026-10-19.md) | A/B/C 阶段设计、确认集、预算和门槛。 |
| [原研究方向](reze_research_directions_2026-10-19.md) | 比较、事件证据、记忆与回看的假设。 |
| [冻结参数](../comparisons/qvhighlights/reze_fullval_2026-10-20/stage_a/plan.json)、[原方案发布清单](reze_plan_publication_2026-10-20.json) | 原始方案参数与发布凭证，保持原样。 |

原 v1 制定于 2026-10-19，公开版本附截至 2026-10-20 的执行状态。A 阶段及单独授权的全量评分扩展已完成；A 阶段未通过原门槛，B/C 与 confirm100 尚未执行。新的会议推进计划单独记录，不改写原停止决定。

## 跨数据集结果与数据准备

| 文档 | 范围与结论 |
|---|---|
| [跨数据集结果与适配分析](reze_cross_dataset_results_analysis_2026-10-22.md) | 任务目标、摘要选择诊断及适配优先级。 |
| [TVSum 完整结果](reze_tvsum_execution_2026-10-22.md) | 50 条完成，固定 val10 / all50 Top-5 mAP 为 61.32 / 54.89。 |
| [MR.HiSum 可用全量结果](reze_mrhisum_full_execution_2026-10-21.md) | 1,888/2,000，mAP50 / mAP15 / F1 为 57.00 / 23.90 / 38.27。 |
| [MR.HiSum pilot100](reze_mrhisum_execution_2026-10-21.md) | 先前固定 100 条，保留独立运行记录。 |
| [QFVS 结果分析](reze_qfvs_analysis_2026-10-20.md) | 四查询 F1 38.63，低于同预算均匀/随机选片。 |
| [QFVS 推理记录](reze_qfvs_execution_2026-10-20.md) | 四条完整视频、固定查询与原生评价。 |
| [跨数据集与 SVHighlights 计划](reze_cross_dataset_2026-10-20.md) | 含 10 月 22 日状态更正：七场启动失败，无有效 REZE 指标。 |
| [QFVS 原始视频记录](qfvs_raw_videos_2026-10-20.md) | 下载、检查及标注网格边界。 |
| [TVSum / MR.HiSum 数据记录](tvsum_mrhisum_download_2026-10-20.md) | 下载范围、失败补试及可用性。 |
| [TVHighlights 数据核查](tvhighlights_download_2026-10-21.md) | 尚无本地可用视频和标注，与 TVSum 分开记录。 |

## MERIT 适配与开发实验

| 文档 | 内容 |
|---|---|
| [原 QVHighlights 适配](merit_qvhighlights_adaptation.md) | 三键检索、时间邻域与完整 2 秒评分。 |
| [密集评分适配](merit_hd_adapter_implementation_2026-10-16.md) | M0 / D0 / H1 与固定 train100。 |
| [方法新增内容](merit_method_additions_2026-10-16.md) | 区分设计目标、原型与待验证贡献。 |
| [高光证据研究方案](highlight_evidence_research_2026-10-16.md) | 四类 cue、事件关系和定向查证设计。 |
| [证据 pilot](highlight_evidence_pilot_2026-10-16.md) | 固定 train20 的 E1/E2/E3 及回退。 |
| [记忆粒度](highlight_memory_granularity_2026-10-16.md) | 固定候选与输入帧的 C10/F2 对照。 |
| [可靠性修复](highlight_memory_repair_2026-10-16.md) | 结构化输出、失败诊断与同样本复测。 |
| [评分输入消融](highlight_memory_ablation_2026-10-16.md) | 帧、描述、cue 和图边对照。 |
| [完整 2 秒纯记忆评分](highlight_memory_only_2026-10-16.md) | 完整时间轴描述与 cue 读取。 |
| [纯记忆评分分析](highlight_memory_only_analysis_2026-10-17.md) | 同分、证据利用和读取问题。 |
| [R1/R2 方案](highlight_memory_reader_plan_2026-10-17.md) | 冻结的读取修复与停止规则。 |
| [R1 结果](highlight_memory_reader_run_2026-10-17.md) | R1 已完成，R2 按规则未运行。 |

## 相邻零样本项目报告

| 文档 | 内容 |
|---|---|
| [CLIP / VTG-GPT 结果](zeroshot_baselines/RESULTS_2026-10-19.md) | 两种对照的结果及文本复用边界。 |
| [CLIP / VTG-GPT 协议](zeroshot_baselines/PROTOCOL.md) | 数据、模型和评分流程。 |
| [REZE 基线结果](zeroshot_baselines/REZE_RESULTS_2026-10-19.md) | 原 B0 独立实现的结果、修复和成本。 |
| [REZE 基线协议](zeroshot_baselines/REZE_PROTOCOL.md) | 采样、概率评分与时间网格。 |

## 历史完整结果与记录

- [此前实验总汇](reproduction_results_summary_2026-10-19.md)：MERIT、LongVT、VideoARM 的完整集、成功子集与开发结果。
- [统一分析](../comparisons/qvhighlights/analysis_2026-10-15/README.md)、[对比数据索引](../comparisons/qvhighlights/README.md)：精选归档及初始化审计。
- [后续方向摘要](research_directions_summary_2026-10-15.md)、[方案详版](research_directions_2026-10-15.md)：历史研究记录。
- [原执行快照](execution_status.md)、[原自动恢复说明](automation.md)：历史运行与配置，不表示任务当前仍在运行。
