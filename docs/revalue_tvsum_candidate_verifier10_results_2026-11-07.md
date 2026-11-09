# TVSum固定10条候选核验：诊断结果

状态：**complete**。完整分母10条视频、50对候选，每臂50个请求，共100个请求槽位。
两臂预测已在读取TVSum标注前冻结。原native/F_local分数、区间和排序保持原样；本轮仅诊断，不重排、不产生新的clip分数，也不报告高光mAP收益。

| 核验臂 | 合法 | invalid | runtime error | 中断未提交 | 未尝试 | A | B | tie | insufficient | incomparable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C_verify | 50 | 0 | 0 | 0 | 0 | 14 | 16 | 6 | 6 | 8 |
| V_verify | 50 | 0 | 0 | 0 | 0 | 19 | 15 | 4 | 8 | 4 |

| 核验臂 | A/B偏好coverage | A/B偏好与20人标注一致率 | A/B/tie已决coverage | A/B/tie标注一致率 | 全分母A/B匹配产出率 |
|---|---:|---:|---:|---:|---:|
| C_verify | 30/50 (60.00%) | 236/600 (39.33%) | 36/50 (72.00%) | 287/720 (39.86%) | 236/1000 (23.60%) |
| V_verify | 34/50 (68.00%) | 286/680 (42.06%) | 38/50 (76.00%) | 327/760 (43.03%) | 286/1000 (28.60%) |

每位原标注者用对应2秒clip的重要性评分分别产生A/B/tie；保留全部20人及其分歧，不多数投票，不把均分偏好当作唯一真值。A/B一致率分母为20×该臂A/B判断数，标注者平分仍在分母内且不匹配A/B。A/B/tie一致率另列。
全分母A/B匹配产出率分母固定为50×20=1000；tie、insufficient、incomparable及任何技术失败都贡献0个A/B匹配。该指标是覆盖率与条件一致性的联合产出，不是独立语义准确率。没有决定时条件一致率未定义。
标注者完全一致的pair：0/50；有分歧：50/50。

逐视频结果保留全部5对，不删除失败或弃权：

| 视频 | C A/B coverage | V A/B coverage | C标注一致率 | V标注一致率 |
|---|---:|---:|---:|---:|
| WxtbjNsCQ8A | 4/5 (80.00%) | 5/5 (100.00%) | 46/80 (57.50%) | 58/100 (58.00%) |
| GsAD1KT1xo8 | 1/5 (20.00%) | 2/5 (40.00%) | 7/20 (35.00%) | 17/40 (42.50%) |
| i3wAGJaaktw | 4/5 (80.00%) | 4/5 (80.00%) | 26/80 (32.50%) | 28/80 (35.00%) |
| XkqCExn6_Us | 3/5 (60.00%) | 2/5 (40.00%) | 28/60 (46.67%) | 22/40 (55.00%) |
| AwmHb44_ouw | 2/5 (40.00%) | 2/5 (40.00%) | 22/40 (55.00%) | 30/40 (75.00%) |
| z_6gVvQb2d0 | 2/5 (40.00%) | 1/5 (20.00%) | 21/40 (52.50%) | 15/20 (75.00%) |
| iVt07TCkFM0 | 2/5 (40.00%) | 5/5 (100.00%) | 22/40 (55.00%) | 33/100 (33.00%) |
| gzDbaEs1Rlg | 4/5 (80.00%) | 5/5 (100.00%) | 25/80 (31.25%) | 39/100 (39.00%) |
| XzYM3PfTM4w | 4/5 (80.00%) | 4/5 (80.00%) | 28/80 (35.00%) | 33/80 (41.25%) |
| kLxoNp-UchI | 4/5 (80.00%) | 4/5 (80.00%) | 11/80 (13.75%) | 11/80 (13.75%) |

按视频配对bootstrap：固定10个视频block、seed 42、10000次。以下差值为V−C，单位百分点，仅作描述：

- definite_preference_coverage_V_minus_C_pp: +8.000，95%区间 [-4.0, 22.0]。
- full_denominator_preference_match_yield_V_minus_C_pp: +5.000，95%区间 [0.6999999999999995, 9.2]。
- full_denominator_resolved_match_yield_V_minus_C_pp: +4.000，95%区间 [-2.9999999999999987, 10.2]。
- common_definite_agreement_V_minus_C_pp: +0.000，95%区间 [0.0, 0.0]。
- 共同A/B决定比较仅使用两臂均有确定偏好的同一pair，pair分母25/50，标注者-pair分母500；bootstrap空分母次数0，均保留为不可估计。

候选事件状态、观看贡献和旧理由核验分开记录：

- C_verify: 可用候选判断100/100；event_state {'supported': 87, 'contradicted': 2, 'insufficient': 11}；contribution {'supported': 80, 'contradicted': 0, 'insufficient': 20}；reason_check {'supported': 41, 'contradicted': 5, 'insufficient': 3, 'not_provided': 51}；旧理由contradicted报警 5/49 (10.20%)。
- V_verify: 可用候选判断100/100；event_state {'supported': 86, 'contradicted': 2, 'insufficient': 12}；contribution {'supported': 71, 'contradicted': 0, 'insufficient': 29}；reason_check {'supported': 41, 'contradicted': 6, 'insufficient': 2, 'not_provided': 51}；旧理由contradicted报警 6/49 (12.24%)。

reason_check报警表示模型质疑给定旧理由；contribution表示模型对观看贡献的判断。两者都不能合并为事实真错。TVSum重要性偏好不提供独立的事实/时间/语义真值；schema与引用通过只证明机械契约。本轮10条为已查看的开发视频，不能声称独立语义准确率或高光mAP提升。

新增成本独立记账：尝试100/100，已知实际token 492778，记账token 492778/1638400，未知完成token的预留请求0；GPU生命周期 11647.924/28800 GPU秒；worker 2/2；重试0；残留所属进程0。
中断且无已提交返回的请求保留完整token预留。未入账的请求文件仅作准备记录，不算模型调用；失败/缺失不转成负例，不重试、不补样、不重排。评价模型调用0。

完整逐pair/逐视频JSON、CSV和所有冻结哈希见 `$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_candidate_verifier10_27b_v1_2026-11-07`。
