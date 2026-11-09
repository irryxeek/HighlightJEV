# Qwen3.8-27B 固定20条 Q/Q+V 结果

运行状态：failed。原清单前20条query、37个候选/臂，共74个预定请求。

| 模型/条件 | 合法 | supported | insufficient | flagged | precision | recall |
|---|---:|---:|---:|---:|---:|---:|
| 8B Q | 36/37 | 23 | 11 | 2 | 100.00% | 8.00% |
| 8B QV | 37/37 | 17 | 16 | 4 | 100.00% | 16.00% |
| 32B Q | 33/37 | 0 | 32 | 1 | 100.00% | 4.00% |
| 32B QV | 33/37 | 0 | 33 | 0 | 未定义 | 0.00% |
| Qwen3.8-27B Q | 0/37 | 0 | 0 | 0 | 未定义 | 0.00% |
| Qwen3.8-27B QV | 0/37 | 0 | 0 | 0 | 未定义 | 0.00% |

本轮尝试1次；实际已知token 0，含失败预留计账6105；GPU生命周期1012.901秒。零重试，旧实验账本哈希不变。

仅flagged计报警，insufficient为弃权；IoU<0.5是错误代理，独立人工语义标签仍为0。无效、失败和未尝试保留全分母。候选边界未改变，不能声称grounding性能提升。

新模型使用原生tokenizer/processor及新推理环境，任务提示、schema、候选和源像素/PTS保持一致；处理器差异见context_capacity_check.json。

原始产物：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv20_qwen3_8_27b_v1_1_2026-11-04`。
