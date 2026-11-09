# TVSum 八小时自动执行安排

## Material Passport

- Origin Skill / Mode：academic-research-suite / experiment-agent，run + validate。
- 用户授权：“我现在准备睡觉，请你安排接下来8h的任务并自动化执行”。该指令更新此前仅规划状态。
- 窗口：北京时间 **2026-11-06 01:27:06—09:27:06**，包含准备时间；提前完成即停止并释放GPU。
- 参考：[结果分析与下一步方案](revalue_tvsum_full50_analysis_and_next_plan_2026-11-06.md)。历史方案和结果保持原样。
- 模型：原Qwen3.8-27B、同revision，TP4/PP1。初始检查0–3卡空闲，4–7卡有其他作业；调度时重新检查空闲状态和设备UUID。

## 自动任务顺序

| 顺序 | 任务 | 新模型请求 | 结束条件 |
|---|---|---:|---|
| 0 | 来源与运行器审查、实际CPU输入检查 | 0 | 全部通过再允许推理 |
| 1 | 全50旧F/FV输出的rank-faithful导出分析 | 0 | 保留旧native/stable，冻结独立诊断预测再评价 |
| 2 | 完整原new40的D-relative无记忆对照 | 40 | 每视频一次，旧F/FV复用；正常退出后评价 |
| 3 | 条件性旧val10绝对/带参照价值表示对照 | 0或40 | 仅固定门槛通过才准备并启动 |
| 4 | 自动汇总指标、成本、异常与后续方向 | 0 | 生成Markdown报告与完成收据，结束任务 |

条件性阶段要求D正常退出、40次计划尝试完成、至少38个合法输出；native和rank-faithful两口径F−D均至少+1pp，且两口径FV−F均不大于0。该条件是研发调度条件，不是显著性或泛化证明。若不满足，不运行新的价值模型条件，保留源码与诊断结果供后续审阅。

价值小试采用完整旧val10，每视频两次V生成和两次最终选择，共40次；两臂共同F/旧帧/schema/预算/选择器相同，差异是价值定义是否要求可引用的相对证据。允许unknown、NA、并列及无比较；不禁止标题，不强迫胜负，不补语音、采帧或边界。

## 已完成的准备与待执行状态

- 新隔离实现：`$MERIT_ROOT/experiments/revalue_tvsum_overnight_v1/`。
- **57项CPU测试通过**，覆盖分数导出、实际请求绑定、价值来源/装箱、请求范围/重复保护、截止时间与进程身份、失败收尾。
- 只读源码复核通过；修复了价值分支失败仍显示完成、残留进程状态展示不同步、准备阶段历史来源绑定不足三处问题，均在任何新模型调用前完成。
- 来源/CPU收据覆盖全部20个源文件；实际像素、token、上下文检查正在准备阶段执行，结果以stage的`context_capacity_check.json`和`runner_review.json`为准。
- 本节记录的是启动前状态；实际执行进度以运行目录带时间戳的状态和账本为准。

## 自动化与退出机制

后台协调器独立于Codex/VS Code交互连接，按阶段顺序执行。每阶段使用单独ledger、worker与退出收据；最多两个实验worker生命周期，模型请求总数为40或条件允许时最多80，零自动重试、零额外smoke、不重复旧结果。缓存减少本轮新增消耗，不免除F/FV方法本身的初始化成本。

准备、模型加载前、每次请求派发和后台监督循环均检查09:27绝对截止时间。到时停止派发并清理本轮已确认UID/session/token/start-time的进程；不按利用率为0抢用已占显存的卡，不干预其他用户进程。停滞只记提醒，不据此反复启动模型。主机断电、操作系统或设备不可恢复故障不能由本脚本保证避免。

技术失败、未尝试、依赖失败保留完整分母与B0回退，原始响应和失败记录不修写；异常不会通过自动重试掩盖。原token/GPU任意总配额不恢复，本次实际消耗另记，不挪用旧QV/TVSum/Direct账本。

本轮不推送、不改依赖/权重，不进入其他数据集；不会为用满8小时重复测试。预计实验部分约1–2小时，取决于闲卡和条件分支；截止时间是最长运行窗口。

## 进度与结果路径

运行根：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_overnight_27b_v1_2026-11-06/`。

- 全局：`status.json`、`heartbeat.json`、`coordinator_started.json`、`step_receipts/`。
- D：`direct40/status.json`、`direct40/ledger.json`、`direct40/worker_0/worker.log`。
- 自动分支依据：`decision.json`、`branch_activation.json`。
- 导出诊断：`p0_rank_export/report.md`；D/价值对照：`direct40/report.md`、条件性的`value10/report.md`。
- 收尾：`overnight_complete.json`。
- 预计自动写入的总结：`$MERIT_ROOT/docs/revalue_tvsum_overnight_results_2026-11-06.md`。

冻结后的后台入口为运行根`source_snapshot/coordinator.py`，在CPU验收完成后仅启动一次。历史实验、已完成分析、报告及旧账本哈希保持不变。

## 实际启动记录（北京时间02:03）

- 40条D输入已完成CPU准备，像素、图像网格及上下文检查通过；`direct40/runner_review.json`通过验收。
- 02:02:20启动独立后台协调器，PID 47913，session 47913；启动后已脱离交互进程，PPID为1。
- P0导出诊断已完成，CPU退出0：新40视频的rank-faithful F为52.6418、FV为50.1183，FV−F为−2.5234pp；修正导出并未消除该批价值条件的负收益。
- D-relative worker已启动，在0–3卡加载原27B模型。本记录不是推理完成声明，实时状态和最终收据见上述路径。
- ARS来源与执行账本：运行根`passport.md`、`passport_run_ledger.yaml`；实验请求仍按各stage独立账本记录。

02:04启动健康检查：首条D模型请求已完成，耗时45.3秒、实际24,898 token；第二条正在运行，无失败记录。协调器PPID仍为1，监督器和模型worker存活。核验快照保存在运行根`launch_health_receipt.json`；此后任务由后台协调器继续执行。
