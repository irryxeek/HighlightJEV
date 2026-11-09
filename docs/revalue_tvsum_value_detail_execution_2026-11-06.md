# TVSum40 详细价值记忆对照：执行记录

## Material Passport

- 工作流：academic-research-suite / experiment-agent，run + validate。
- 实施依据：[详细标准与对照方案](revalue_generic_highlight_value_v4_2026-11-06.md)。
- 2026-11-06 19:16（北京时间）：已启动独立监督进程，状态为 `waiting_for_four_idle_gpus`；本记录时模型调用、实验token、GPU生命周期消耗均为0。
- 这是启动快照；后续进度以运行目录的 `status.json`、`ledger.json` 和完成收据为准，不能把本记录误作最终结果。

## 已完成

1. 五类价值各有三项核查问题，并补齐支持、反证、缺证及禁止推断；直接由版本化JSON生成提示。
2. 记忆保留具体问题ID、观察/贡献/比较回答、支持与对照来源、观看理由、缺证和原始响应。
3. 两组复用同一份 F-read，不修改事实。简短组和详细组仅在价值写入提示不同；共用详细选片器、引用规则和装箱策略。
4. 固定原40视频，核对全部320个旧8帧组及真实PTS；最终选片像素、帧序、候选和模型引擎保持一致。
5. 冻结源码70项CPU测试全部通过；321个实际输出schema编译通过。独立执行的代码审查通过，但该审查共享研究背景，不是独立人工语义标注。

## 冻结范围与成本

| 项目 | 本轮设置 |
|---|---|
| 模型 | 原Qwen3.8-27B revision，BF16，TP4 |
| 正式请求上限 | 720：两组各320次价值写入＋40次选片 |
| 重试 | 0 |
| 写入输出 / 选片输出 | 1024 / 1536 token，沿用原上限 |
| F / V视图 | 各1024 token，沿用原FV的分视图上限；不代表与旧仅F输入等长 |
| 上下文上限 | 32768；全量CPU最大预留29989 |
| 独立绝对token预留 | 5,451,504，含输出预留；实际用量另报 |
| 调度 | 一次四卡worker，等待四张真正空闲GPU，最长排队12小时 |
| 生命周期 | worker最多21600秒＋60秒清理；最多86640 GPU秒 |

原40次F-read及其他历史轮次的成本不并入、不清零、不转移。按旧TVSum写入/选片耗时估算，启动后约5–6小时；这不是完成时间保证，排队另计。

## 自动执行与结果

监督进程PID：`45909`，已与当前交互会话分离。当前GPU 0–3仍属于既有Mr.HiSum任务，4–7有其他任务；监督进程不抢占、不终止它们。出现空闲四卡后才加载本轮模型。

结束后自动确认所属进程退出、冻结预测，再用CPU读取标签评价。主比较为 FV-detail−FV-brief 的完整40视频Top-5 mAP，附排序敏感性、配对区间、合法率、状态分布与成本。失败/弃权保留全分母并沿用B0回退，不伪装成有效新预测。不会自动扩样、重试或启动其他分支。

- 运行目录（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_detail_40v_27b_v1_2026-11-06`）
- 固定协议（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_detail_40v_27b_v1_2026-11-06/source_snapshot/protocol.md`）
- CPU输入检查（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_detail_40v_27b_v1_2026-11-06/context_capacity_check.json`）
- 运行器验收（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_detail_40v_27b_v1_2026-11-06/runner_review.json`）
- 实际状态（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_value_detail_40v_27b_v1_2026-11-06/status.json`）

完成后报告将生成到 `$MERIT_ROOT/docs/revalue_tvsum_value_detail_results_2026-11-06.md`；本记录时尚未生成新实验结果，也未推送远程。
