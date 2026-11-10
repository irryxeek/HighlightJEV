# 通用高光评分 v1：TVSum val10 与 REZE 配对测试协议

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run
- Origin Date: 2026-11-10
- Verification Status: UNVERIFIED（此文件为运行前冻结协议，结果另存）
- Version Label: generic_highlight_tvsum_val10_v1
- 用户授权原文：在tvsum上先测10条，跟reze结果对比一下。

## 固定范围与对照

使用旧 REZE full50 的官方 UMT val10，按旧 full50 清单顺序筛选，不按指标或反例选择：`J0nA4VgnoCo`、`cjibtmSLxQ4`、`JgHubY5Vw3Y`、`Bhxk-O1Y7Ho`、`sTEELN-vY30`、`Yi4Ij2NM7U4`、`E11zDS9XGzg`、`Se3oxnaPsz0`、`JKpqYvAdIsw`、`fWutDQy1nnY`。它们此前已用于开发，不能视为未接触的独立测试集。

- 基线：复用旧 REZE 在同一 10 视频上的原始预测与概率记录，不重新推理。
- 新条件：`generic_highlight`，以可见观看价值代替原动作核验问题。
- 同一 Qwen3-VL-8B-Instruct BF16 权重，revision `0c351dd01ed87e9c1b53cbc748cba10e6187ff3b`；3 秒窗口、2 fps、单 token Yes/No、同样的 top-20 概率读数和 1 秒→2 秒导出。
- 旧 Top-5、REZE 分数、标签、标题、语音、事实或价值记忆均不进入新评分器。
- 本轮没有五维独立评分或加权，没有回看和边界修正。新提示包含五类可选证据示例，因此检验的是任务提示整体，不是某一个价值维度的独立贡献。
- 保留原多模态检查；旧运行器跳过 profiling 的启动选项不复制，启动成本不作完全匹配声明。

## CPU 审查与冻结

复用上一轮已通过的26项 CPU 测试，因为本次源码快照与其逐文件相同。核对模型资产、旧 REZE 权重文件状态、所有10条视频字节哈希。运行前对每视频首/中/末窗口做原生处理器预检，检查两种提示的上下文和旧 REZE 的像素/PTS一致性；实际推理每个窗口再次检查上下文，完成后逐窗口核对旧输入哈希。

所有输出保留原始批次与逐窗口响应。先冻结完整预测，再读取 GT。输入或源码不匹配、上下文超限、推理/解析异常即停止后续派发；不自动修改提示或重试。

## 本轮独立运行边界

用户已授权10视频测试。以下数值由助手按完整清单设置为本轮执行上限，不表述为用户逐项指定数值，也不挪用任何旧账：

| 项目 | 本轮上限 |
|---|---:|
| 完整视频 | 10 |
| 正式窗口尝试 | 1,260 |
| 额外故障调用／重试 | 0／0 |
| 绝对 token 预留 | 5,160,960 |
| GPU | 同时1张；启动时再次确认空闲 |
| GPU 生命周期 | 3,600秒，含启动、推理及5秒清理预留 |
| 实验 worker 启动 | 1 |

每次调用先预留4096 token，成功记实际 input+output，失败／未决保留预留。退出和所属进程组清理有独立收据。未开始、失败与证据不足不得通过删除视频改善分母；本次没有其他数据集任务或扩到50条的权限。

## 评价与科学结论

主评价为完整10条 UMT Top-5 mAP；按视频给出新方法−REZE差值和10,000次配对 bootstrap（seed=42）。区间仅描述这个已见开发集，小样本不证明泛化。

完整分数缺任何窗口时，新方法该视频为不可用预测，主指标记零失败信用并单列；不回填旧B0。另报告成功率、常数视频、概率分布、Yes缺失回退、同分、Top-5变化和累计token/GPU时间。保留所有负结果，不根据中途指标调整或扩样。

产物目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_val10_v1_2026-11-10`。小型审计资料保存在 [docs/artifacts/revalue_generic_highlight_tvsum_val10_2026-11-10](artifacts/revalue_generic_highlight_tvsum_val10_2026-11-10/selection_receipt.json)。

参考：[评分实现与前次 CPU 验证](revalue_generic_highlight_scoring_v1_2026-11-10.md)、评分器说明（本地资料：`$MERIT_ROOT/experiments/revalue_generic_highlight_scoring_v1/README.md`）。
