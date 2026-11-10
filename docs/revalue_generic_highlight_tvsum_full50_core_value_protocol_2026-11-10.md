# TVSum 最新8B关键贡献版：补齐10条并统一评全50

## Material Passport

- academic-research-suite / experiment-agent；run + validate；2026-11-10。
- 用户原话：“50条一起评，什么叫置信区间跨0？”
- 本轮落实完整50条统一评价；旧core_8B只完成40条，必须补齐缺少的10条，不能混入上一版结果。

## 固定方法与范围

保留已完成后40条的冻结模型、评分源码、提示、五维规则、背景用法、帧采样、分数转换和原2秒导出。使用Qwen3-VL-8B-Instruct，本地BF16/TP1，seed0、temperature0、输出单token Yes/No。完全复用已生成的背景和原帧/真实PTS；不再修改决策目标或规则，不加平滑、解释、回看、训练或新采样。

新评分仅覆盖原10条：J0nA4VgnoCo、cjibtmSLxQ4、JgHubY5Vw3Y、Bhxk-O1Y7Ho、sTEELN-vY30、Yi4Ij2NM7U4、E11zDS9XGzg、Se3oxnaPsz0、JKpqYvAdIsw、fWutDQy1nnY。共1260个原3秒窗口。背景逐字节、输入像素/PTS按冻结参考核对。

新增10与旧40不重叠，合并为原50条、4213窗口。对照沿用已有完整50条REZE_8B与revised_8B。所有样本已经参与开发或诊断；完整50不等于独立官方测试集。

## 独立执行边界

| 项目 | 上限 |
|---|---:|
| 新正式尝试 | 1260 |
| 重试/额外探针 | 0 |
| 新总token（含失败预留） | 5,160,960 |
| 新worker | 1 |
| 单GPU生命周期（含加载和清理） | 1800秒 |
| 同时GPU | 1，启动前检查空闲0号卡 |

额度为本轮完整50条用户请求下，仅补齐缺失10条的有限执行范围；不使用任何旧实验剩余额度。每请求先预留4096 token，成功按实际输入+输出计账。旧40、背景、两个对照的新增模型调用均为0。禁止自动重试；异常保留，硬超时只清理本轮所属进程。

## 审查与评价

先做新10条CPU原生处理器检查（每视频首/中/尾）、上下文检查及冻结源码审查，再启动单次worker。旧worker与媒体实现逐字节复用；正式运行逐请求核对原帧/PTS。不得添加skip检查参数。新输出、原始概率、请求账本和预测冻结先保存，然后CPU评价读取标注。

主表统一报告全50的Top-5 mAP、mAP15、mAP50。另保留10/40分组；不得按结果挑子集。补充mAP沿用此前已冻结的TVSum2秒协议：20人评分均值取GT最高floor(15%×N)/floor(50%×N)，同分按时间索引；全曲线非插值AP，视频等权平均。每人分别AP、边界全部同分两项敏感性同时保留。不能直接当作HiVid同协议或Mr.HiSum原生5秒结果。

视频级配对bootstrap10000次、seed42，报告“新版−对照”的区间；区间跨0表示尚不足以确认稳定改善，不能解释成模型mAP为0或已证明没有效果。未作多重比较校正。

技术完成要求50/50、1260次新请求、帧/概率/冻结核对、预算内且worker退出。失败和未尝试曲线保持null，完整分母中仅记零完成信用，不伪造模型曲线或用上一版填补。科学结论不影响中途执行和停止。

## 路径

- 源码：`$MERIT_ROOT/experiments/revalue_generic_highlight_core_full50_v1`
- 运行：`$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_full50_core_value_v1_2026-11-10`
- 审计：`$MERIT_ROOT/docs/artifacts/revalue_generic_highlight_tvsum_full50_core_value_2026-11-10`
- 保留全部旧实验产物和报告，不推送。
