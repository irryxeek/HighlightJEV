# ReVALUE v2.2 Q/Q+V 多卡续接执行记录

## Material Passport

- Origin Skill：academic-research-suite / experiment-agent，run。
- 日期：2026-11-02，北京时间13:28启动多卡续接。
- 用户授权：空闲GPU可用于并行处理。

## 已完成交接

原单卡在第14个worker正常完成后交接：140次请求、683,770token、3,096.689241344051 GPU秒全部继承。没有中断模型调用或重试。原CPU调度器的SIGTERM/KeyboardInterrupt终态保留，属于明确记录的调度交接；后续进度应读取新的续接目录。

124项CPU测试通过，包含四进程真实CPU账本竞争、重复调用防护、预算、稀疏失败评价及交接暂停/恢复。所有输入字节、request_sha256、提示、图像、模型与schema与单卡v2.2相同。

## 当前运行

- GPU 0–3：四个worker并行，物理UUID均已核验；其他卡有任务时不分配。
- 继续剩余138次请求；总上限仍为278次、零重试、28worker、3,416,064token、16,800 GPU秒，包含继承消耗。
- 通过文件锁预留/提交账本；每个候选的Q/QV仍同批同卡按原顺序执行。
- 若更多RTX4090变为空闲，调度器可使用它们，最多8卡；不增加样本或调用。
- 自动CPU收尾器等待所有继承及新增worker退出后，仅评价一次并与v2.1比较。

按原worker平均耗时约221秒估算，交接时剩余14个worker单卡约52分钟，四卡预计15–25分钟。该估计不是已经测得的加速比。

## 路径与审计

- [调度补充协议](revalue_value_qvqv100_v2_2_parallel_amendment_2026-11-02.md)
- 当前运行：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_2_parallel_2026-11-02`
- 完成结果：`docs/revalue_value_qvqv100_v2_2_parallel_results_2026-11-02.md`（完成后生成）。
- 准备/交接记录：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_2_parallel_preparation_2026-11-02`
- manifest SHA256：`188e337053b782afa414d8a4445c64b59b8a37281fbf3640d7d1098bc3b517ac`
- 本文件是启动快照，当前状态以新运行目录status.json、ledger.json及终态收据为准。
