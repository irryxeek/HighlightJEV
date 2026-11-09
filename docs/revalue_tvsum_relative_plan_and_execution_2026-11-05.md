# TVSum：相对价值判据的固定十视频对照

## Material Passport

- Origin Skill / Mode：academic-research-suite / experiment-agent，run。
- 用户授权：先完成全部离线案例审计，再在原固定十视频运行 F-relative／FV-relative 共20次；资源不足可用8B。
- 本轮优先27B，保持父轮模型。结构和数值核验不替代独立人工语义核验。

## 已完成的离线审计

[审计报告](revalue_tvsum_relative_offline_audit_2026-11-05.md)及完成收据（本地资料：`$MERIT_ROOT/comparisons/tvsum_relative_offline_audit_2026-11-05/audit_complete.json`）覆盖全部10视频、100个F/FV推荐、400条原始价值记录及20张冻结帧拼图。助手审阅有共享对话上下文，不能称独立人工盲评。

- 原169条supported中，92条实际进入V视图。76条因关联事实不在活跃F中未入箱，只有1条明确因V预算拒绝。不能把全部损失归因于NA占位。
- 100个推荐中，19个只引用远处上下文，12个无事实引用。远上下文不必然错误，空引用也不等于没有图像依据。
- 旧帧支持部分事件阶段错配案例，以及普通动作／视觉特色被直接升级为高光理由的情况；这些是相对价值假设的支持案例，尚非性能退化的因果证明。
- 同tier导出及原分数同分会改变排序，个别输出还改变最终Top-5成员。保留原规则，不借本轮修分。

审计新增实验模型调用、GPU时间与新源视频帧均为0；不重新评价父轮。审计产物与标签侧指标不进入模型输入。

## 本轮唯一提示干预

两臂共同加入同一 `RELATIVE_VALUE_RULE`：对象、动作、外观或群体的存在是事实，不自动代表高光优先级；候选需要相对于其他已观察时刻，提供有证据的关键变化／结果、新信息、突出动作、反应或感官事件。supported字段是价值假设，不是重要性分数；没有明确差异时允许并列或弃权，不强迫选满。

| 条件 | 最终模型输入 | 新调用 |
| --- | --- | ---: |
| F-relative | 原共同帧、候选表及F，加相对价值判据 | 10 |
| FV-relative | 同一输入及F，加原V与相同判据 | 10 |

原64个全片采样点与旧Top-5候选视图、像素／PTS、choice表、模型revision／engine、五类rubric、1536token上限、0.5秒机械引用容差、分数多重集及原生评价均保持不变。全部10份memory JSON逐字节复用，包括NA、unknown及既有装箱，不再调用80次建库。

CPU将新渲染提示去掉唯一新增段落后，必须恢复父轮实际发送提示；新处理像素／图像网格必须与父轮一致。长度和注意力焦点随提示变化，这是旧新差异的解释边界。

## 执行和评价

固定原10视频顺序，两臂按父轮相对顺序运行，各一次，共20次，无额外smoke或自动重试。27B沿用四卡TP4／PP1；8B仅在资源不足时另行冻结同模型两臂，不在冻结后静默切换。

主比较为FV-relative−F-relative的原生Top-5 mAP；另报相对旧F／FV的描述性差值、完整十视频逐例变化、稳定同分敏感性、成员与顺序变化、失败和实际成本。技术失败按原协议回退B0并保留全分母。预测冻结并确认GPU进程退出后，才在原CPU评价环境读取标签。

探索门槛沿用合法率至少95%（19／20）及主差值至少+1pp；仍需独立语义核验。若只改善共同提示而没有V额外增益，不能称价值记忆贡献；未超过历史B0也不能称最终性能突破。没有自动扩样或下一模型分支。

新实耗仅20次最终判断；历史建库80次／208,128token及所有旧启动失败、旧轮消耗单列，不重复计入本轮实耗。用户取消的任意总token／GPU配额不恢复，实际账本、worker生命周期和失败仍保留。

## 实现与产物

北京时间2026-11-05 03:15已启动后台监督器PID57835，使用0–3号四卡和原27B，未启用8B回退。60项CPU测试覆盖通过；20条原生输入、父提示恢复、像素／网格和10个schema检查通过，最大上下文29,128／32,768。清单SHA256为 `eaf9615215873908d3efc21e068a6a798fd38dc7c60fa0c6e6dcea6bf5fc3100`，17文件源码映射SHA256为 `857afb823668af95a97ec3a0669aa37d74633a1c5f8cf2397c1875ba25a3c954`。

- 运行协议（本地资料：`$MERIT_ROOT/experiments/revalue_highlight_relative_v1/protocol.md`）。
- 运行说明（本地资料：`$MERIT_ROOT/experiments/revalue_highlight_relative_v1/README.md`）。
- 独立27B目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_highlight_relative_27b_v1_2026-11-05`。
- 准备：`manifest.json`、`parent_binding.json`、`offline_audit_binding.json`、`context_capacity_check.json`、`runner_review.json`。
- 过程：`status.json`、`ledger.json`、`requests_sent/`、`records/`、`worker_0/worker.log`。
- 退出与评价：`worker_0/exit.json`、`campaign_end.json`、`prediction_freeze.json`、`evaluation.json`、`complete.json`。
- 自动结果报告：`$MERIT_ROOT/docs/revalue_tvsum_highlight_relative_27b_v1_results_2026-11-05.md`。

本轮不修改旧产物，不推送远程。启动状态与结果以新运行目录的时间戳和完成收据为准。

## 完成记录

北京时间2026-11-05 03:29:58完成自动评价，状态 `complete`。20次实际调用全部合法，零截断、零机械时间引用失败、零重试；本轮新增建库0次。实际486,791token，单worker墙钟859.497秒（约14.32分钟），四卡GPU生命周期3,437.986秒，所属进程全部退出，0–3号卡已释放。

| 条件 | 原生Top-5 mAP | 稳定同分敏感性 |
| --- | ---: | ---: |
| 历史B0 | 61.3167 | 61.3288 |
| F-relative | 59.7625 | 60.0608 |
| FV-relative | 62.9247 | 62.8132 |

主差值FV-relative−F-relative为+3.1622pp（7视频改善、2下降、1持平），稳定同分口径同向为+2.7524pp。FV-relative较历史B0高1.6080pp；F-relative相对旧F高2.5747pp，FV-relative相对旧FV高6.5958pp。全部十视频保留；没有技术回退驱动本轮差值。

预设数值门槛通过；独立语义核验仍待完成。这是反复查看的同十视频开发结果，不能宣称未见视频泛化或独立证实价值理解。主差值的视频bootstrap区间为[0.1222,6.2743]pp，仅作开发描述；FV-relative相对B0的区间仍跨0。没有自动扩样或继续消耗。

完成收据、ledger、evaluation、predictions、报告哈希及20条原始响应提交哈希已核对；旧父轮ledger／complete及离线审计收据保持不变。正式冻结结果见[本轮结果报告](revalue_tvsum_highlight_relative_27b_v1_results_2026-11-05.md)。
