# TVSum固定10条：旧选片理由可见性对照

状态：**partial_or_invalid**。完整分母10条视频、50对候选，每臂50个请求，共100个请求槽位。
R_keep保留原理由，R_hide隐藏双方原理由；两臂使用同一详细V标准、同一候选/帧/PTS/F与同一schema。共同修复证据不足被判为反驳的问题：事件观察仅supported/insufficient；reason_check/contribution的contradicted须有明确命题、正面冲突观察与严格片内帧。
两臂预测已在读取TVSum标注前冻结。原native/F_local分数、区间和排序保持原样；本轮仅诊断，不重排、不产生新的clip分数，也不报告高光mAP收益。

| 核验臂 | 合法 | invalid | runtime error | 中断未提交 | 未尝试 | A | B | tie | insufficient | incomparable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R_keep | 49 | 1 | 0 | 0 | 0 | 6 | 3 | 13 | 26 | 1 |
| R_hide | 50 | 0 | 0 | 0 | 0 | 11 | 8 | 11 | 20 | 0 |

| 核验臂 | A/B偏好coverage | A/B偏好与20人标注一致率 | A/B/tie已决coverage | A/B/tie标注一致率 | 全分母A/B匹配产出率 |
|---|---:|---:|---:|---:|---:|
| R_keep | 9/50 (18.00%) | 71/180 (39.44%) | 22/50 (44.00%) | 167/440 (37.95%) | 71/1000 (7.10%) |
| R_hide | 19/50 (38.00%) | 156/380 (41.05%) | 30/50 (60.00%) | 234/600 (39.00%) | 156/1000 (15.60%) |

每位原标注者用对应2秒clip的重要性评分分别产生A/B/tie；保留全部20人及其分歧，不多数投票，不把均分偏好当作唯一真值。A/B一致率分母为20×该臂A/B判断数，标注者平分仍在分母内且不匹配A/B。A/B/tie一致率另列。
全分母A/B匹配产出率分母固定为50×20=1000；tie、insufficient、incomparable及任何技术失败都贡献0个A/B匹配。该指标是覆盖率与条件一致性的联合产出，不是独立语义准确率。没有决定时条件一致率未定义。
标注者完全一致的pair：0/50；有分歧：50/50。

逐视频结果保留全部5对，不删除失败或弃权：

| 视频 | R_keep A/B coverage | R_hide A/B coverage | R_keep标注一致率 | R_hide标注一致率 |
|---|---:|---:|---:|---:|
| WxtbjNsCQ8A | 2/5 (40.00%) | 2/5 (40.00%) | 20/40 (50.00%) | 20/40 (50.00%) |
| GsAD1KT1xo8 | 0/5 (0.00%) | 1/5 (20.00%) | 0/0 (未定义) | 10/20 (50.00%) |
| i3wAGJaaktw | 1/5 (20.00%) | 0/5 (0.00%) | 8/20 (40.00%) | 0/0 (未定义) |
| XkqCExn6_Us | 2/5 (40.00%) | 3/5 (60.00%) | 19/40 (47.50%) | 39/60 (65.00%) |
| AwmHb44_ouw | 0/5 (0.00%) | 2/5 (40.00%) | 0/0 (未定义) | 15/40 (37.50%) |
| z_6gVvQb2d0 | 0/5 (0.00%) | 0/5 (0.00%) | 0/0 (未定义) | 0/0 (未定义) |
| iVt07TCkFM0 | 0/5 (0.00%) | 1/5 (20.00%) | 0/0 (未定义) | 13/20 (65.00%) |
| gzDbaEs1Rlg | 1/5 (20.00%) | 3/5 (60.00%) | 4/20 (20.00%) | 19/60 (31.67%) |
| XzYM3PfTM4w | 2/5 (40.00%) | 5/5 (100.00%) | 17/40 (42.50%) | 36/100 (36.00%) |
| kLxoNp-UchI | 1/5 (20.00%) | 2/5 (40.00%) | 3/20 (15.00%) | 4/40 (10.00%) |

主对照为H−K，即R_hide−R_keep；主指标使用完整50对的A/B匹配产出率。按视频配对bootstrap保留固定10个视频block、seed 42、10000次；所有区间仅作描述。以下差值单位百分点：

- definite_preference_coverage_H_minus_K_pp: +20.000，95%区间 [6.0, 34.0]。
- full_denominator_preference_match_yield_H_minus_K_pp: +8.500，95%区间 [2.797500000000002, 13.9]。
- full_denominator_resolved_match_yield_H_minus_K_pp: +6.700，95%区间 [-0.19999999999999982, 12.9]。
- undecided_keep_base_vote_match_change_H_minus_K_pp: +0.400，95%区间 [0.0, 1.0]。
- common_definite_agreement_H_minus_K_pp: +0.000，95%区间 [0.0, 0.0]。
- 共同A/B决定比较仅使用两臂均有确定偏好的同一pair，pair分母7/50，标注者-pair分母140；bootstrap空分母次数6，均保留为不可估计。

局部建议替换及“未决保留base”的CPU反事实：

| 臂 | 建议替换/50 | 局部票差正/负/零 | 替换票差合计/1000 | 恒保留base匹配 | 反事实匹配 | 相对base变化/1000 |
|---|---:|---:|---:|---:|---:|---:|
| R_keep | 4/50 | 3/1/0 | 24/1000 (2.40%) | 360/1000 (36.00%) | 384/1000 (38.40%) | 24/1000 (2.40%) |
| R_hide | 5/50 | 4/1/0 | 28/1000 (2.80%) | 360/1000 (36.00%) | 388/1000 (38.80%) | 28/1000 (2.80%) |

局部票差定义为20位原标注者中“替代候选优于base”的票数减去“base优于替代候选”的票数；平票单列。只在合法A/B明确选择替代候选时假设替换；合法选择base、tie、insufficient、incomparable、无效、中断及未尝试均保留base。未决保留base对相对base票匹配变化贡献0，不能算作核验成功。反事实只描述固定候选对，不建立新排序，也不计算mAP。

以下列出全部建议替换，不按票差筛选；完整50对（含未建议替换）及20位标注者逐人评分差见JSON/CSV。

| 臂 | pair | base clip | 替代clip | base票 | 替代票 | 平票 | 替代−base票差 |
|---|---|---:|---:|---:|---:|---:|---:|
| R_keep | WxtbjNsCQ8A__pair01 | 1 | 38 | 4 | 12 | 4 | 8 |
| R_hide | WxtbjNsCQ8A__pair01 | 1 | 38 | 4 | 12 | 4 | 8 |
| R_keep | XkqCExn6_Us__pair02 | 44 | 39 | 4 | 13 | 3 | 9 |
| R_hide | XkqCExn6_Us__pair02 | 44 | 39 | 4 | 13 | 3 | 9 |
| R_keep | XkqCExn6_Us__pair04 | 2 | 70 | 7 | 6 | 7 | -1 |
| R_keep | XzYM3PfTM4w__pair00 | 0 | 24 | 4 | 12 | 4 | 8 |
| R_hide | XzYM3PfTM4w__pair00 | 0 | 24 | 4 | 12 | 4 | 8 |
| R_hide | XzYM3PfTM4w__pair03 | 26 | 27 | 4 | 3 | 13 | -1 |
| R_hide | XzYM3PfTM4w__pair04 | 41 | 22 | 4 | 8 | 8 | 4 |

候选事件状态、观看贡献和旧理由核验分开记录：

- R_keep: 可用候选判断98/100；可见输入理由49，已校验可见理由判断48；event_state {'supported': 83, 'insufficient': 15}；contribution {'supported': 82, 'contradicted': 0, 'insufficient': 16}；reason_check {'supported': 41, 'contradicted': 5, 'insufficient': 2, 'not_provided': 50}；旧理由contradicted报警 5/48 (10.42%)；理由/贡献正面反证对象5/0；命中明确缺证措辞守卫的请求1/50，按invalid保留。
- R_hide: 可用候选判断100/100；可见输入理由0，已校验可见理由判断0；event_state {'supported': 89, 'insufficient': 11}；contribution {'supported': 89, 'contradicted': 0, 'insufficient': 11}；reason_check {'supported': 0, 'contradicted': 0, 'insufficient': 0, 'not_provided': 100}；旧理由contradicted报警 0/0 (未定义)；理由/贡献正面反证对象0/0；命中明确缺证措辞守卫的请求0/50，按invalid保留。

R_hide的可见旧理由分母为0，因此理由报警率未定义；来源文件保留的理由不会被当作该臂已见输入。逐候选JSON完整保留contribution_claim、reason_counter和contribution_counter。
reason_check报警表示模型质疑给定旧理由；contribution表示模型对观看贡献的判断。两者都不能合并为事实真错。TVSum重要性偏好不提供独立的事实/时间/语义真值；schema与引用通过只证明机械契约。本轮10条为已查看的开发视频，不能声称独立语义准确率或高光mAP提升。

新增成本独立记账：尝试100/100，已知实际token 575015，记账token 575015/1638400，未知完成token的预留请求0；GPU生命周期 15175.394/28800 GPU秒；worker 2/2；重试0；残留所属进程0。
中断且无已提交返回的请求保留完整token预留。未入账的请求文件仅作准备记录，不算模型调用；失败/缺失不转成负例，不重试、不补样、不重排。评价模型调用0。

完整逐pair/逐视频JSON、CSV和所有冻结哈希见 `$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_reason_visibility10_27b_v1_2026-11-08`。
