# ReVALUE v2.2：事实与证据绑定修复的固定 QV100 对照

## Material Passport

- Origin Skill：academic-research-suite / experiment-agent；Mode：run。
- 日期：2026-11-02；版本：value_qvqv100_v2_2。
- 用户指令：继续修复事实与证据引用的绑定问题，再在固定100条query上跑一下Q和Q+V对照，看看效果。
- 本指令授权实现及整批测试。以下数值是沿用上轮规模设定的执行上限，不是用户逐字指定的预算。旧轮次及所有失败保持原样，额度不转入本轮。

## 已知问题与本轮干预

v2.1 共278次，66条无效；首个失败类别中，28条事实跨区域、21条明确判断缺少区间内非空引用、4条重复或未定义引用。统计不等于视觉根因：例如引用技术上合法，事实内容仍可能错误。

本轮保留共享事实池及八条事实上限，生成 schema 枚举事实总数 N 和候选内事实数 I（0≤I≤N≤8）。事实按候选内在前、上下文在后序列化，ID连续为e1…eN；每条事实只能引用同一区域的已提供帧。明确判断只可引用e1…eI且非空；unknown可引用全部已生成事实或不引用。N=0/I=0时保留unknown途径，不强迫产生事实、分差或胜负。

原始JSON结构、事实文字、帧ID及输出解析保持原样，没有事后删除引用、修写失败或将invalid改成unknown。原CPU校验继续检查重复引用、事件依赖、query scope、时序锚点及真实PTS。生成约束不保证视觉事实为真，也不保证所有剩余契约错误都消失。

提示词仅新增一句格式说明：`Serialize inside facts first, then context facts; assign consecutive IDs e1..eN in that order. `。因此渲染提示及token摘要重新冻结；提示长度、事实顺序和约束解码路径共同变化，不能称为纯单字段因果实验。Q与Q+V同时采用这一修复，价值提示内容不改。

## 固定输入与评价

保持原100条query、139个有效候选，每臂139次。原无候选query 9160、2498仍列入完整100条清单。沿用原顺序及Q/QV交替次序，不按GT、旧分数或失败类别挑样本。

保留原图像像素、真实PTS、区域、输入帧顺序、模型修订、query契约、价值rubric、采样及输出上限。原区间、分数、排序均不改；无新增采样、回看、记忆、ROI、训练、其他数据集、下载或推送。

输入逐项对照仅允许output_schema、rendered_prompt、prompt_tokens_cpu、prompt_ids_sha256、request_sha256变化。prepare只读取旧输入并哈希旧结果；worker不得访问GT或旧评价。源码、模型、依赖及输入检查全部保留。

所有worker退出、账本和预测冻结后仅评价一次。与已完成v2.1评价配对，保留全部失败和未尝试分母；分别报告技术合法率、失败类别、supported/insufficient/flagged、IoU代理TP/FP/precision/recall，以及旧invalid→合法和两轮均合法的变化。低IoU不是独立人工语义错误标签；不据此声称新的grounding或高光排序提升。

## 独立资源与停止规则

| 项目 | 本轮上限 |
|---|---:|
| 尝试（含故障） | 278，Q/QV各139 |
| 重试 / 额外故障调用 | 0 / 0 |
| 绝对token | 3,416,064 |
| 上下文 / 输出token | 12,288 / 2,048 |
| 并发GPU | 1张空闲RTX 4090 |
| worker启动 | 28，每批10次，末批8次 |
| 每worker / 累计GPU生命周期 | 600 / 16,800秒 |
| 一次等待队列 | 86,400秒，每30秒检查 |

Qwen3-VL-8B-Instruct修订0c351dd01ed87e9c1b53cbc748cba10e6187ff3b，vLLM0.12.0、bf16、单卡、eager、temperature=0、seed=0、thinking关闭，沿用既有环境。每次调用前预留token，已知用量按实际结算，未知失败保留预留；未用资源不兑换额外请求。

GPU须无计算进程、显存低于512MiB、利用率低于5%，核验UUID和PCI映射；不干预其他进程。源码/输入/环境漂移、运行异常/OOM、启动失败、超时、所属进程退出不确定均停止并留存失败，不重试或降级。普通invalid继续原清单。

原探索门槛不变：≥138/139合法、precision≥80%且高于错误基率、recall≥30%、误报≤10%、insufficient≤40%、报警≥20。技术改善与科学收益分开报告；未过门槛不得自动扩展下一实验。

## 产物与历史对照

- 新运行：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_2_2026-11-02`。
- 新源码：`experiments/revalue_value_ablation_v2_2/`；准备记录：`comparisons/qwen_direct/value_qvqv100_v2_2_preparation_2026-11-02/`。
- 自动结果：`docs/revalue_value_qvqv100_v2_2_results_2026-11-02.md`；归档：`comparisons/qwen_direct/value_qvqv100_v2_2_2026-11-02/`。
- 历史v2.1：278次、28worker、1,336,268token、5,015.231375909061 GPU秒，已完成。历史v2：278次、28worker、1,336,978token、5,008.974413305987 GPU秒。其余QV/TVSum/Direct账本独立，全部不重置、不挪用。

先完成CPU语法/原校验等价性/真实token检查及源码审查，再绑定本次指令启动。完成后的CPU收尾器负责一次评价、历史配对和归档；排队、运行中和技术通过不称为效果已验证。
