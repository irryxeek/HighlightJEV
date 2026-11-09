# SVHighlights 稀疏记忆测试执行记录 v1.1

更新时间：2026-11-09T14:23:23.544946+00:00。三路已经进入真实生成；本条是启动收据，最终结果以本目录 `complete.json` 为准。

- 模型：Qwen3-VL-8B-Instruct。物理GPU：0、2、3，每卡一个独立视频worker；首批为美式足球、棒球、冰球。
- 范围：原七场固定视频、每场64个稀疏全局时刻；D/F共用84张选片图片。最多140个原定生成槽位。
- 组别：缓存B0、D、F、F+C、F+V15。已有事实/价值标准不改，不生成价值记忆库；详细价值判断在核验阶段使用。
- 当前已保存响应：27；状态：{'complete': 27}；已知实际token：71157。这些是运行健康度，不是科学结论。
- 验证：17项CPU回归通过；复用原140项CPU上下文/schema检查及全部输入。
- 源码与输入manifest SHA256：`35c40d137aca3e87884a3734256a5311ea354dcf8aa301760340b1aff0c75e96`。
- 调度器PID：54219。运行根：`$ZEROSHOT_ARTIFACT_ROOT/revalue_svhighlights_sparse7_8b_v1_1_2026-11-09`。

## 启动故障与恢复

v1使用GPU UUID作为可见设备掩码，当前vLLM 0.12在解析时要求整数，三路未进入generate便退出。原记录保留；0模型请求/0token，约35.452144 GPU秒。v1全回退指标等于B0，不是方法结果。

v1.1仅修复启动器：验证NVML与PCI顺序后使用数字编号，仍在加载前检查实际物理UUID。未重采样、未改提示、未更换候选。失败成本不清零：恢复阶段最多12558 GPU秒，连同旧失败仍在12600秒内；累计最多3次失败初始化加7个视频worker。没有模型输出重试。

## 查看进度与结果

- `$ZEROSHOT_ARTIFACT_ROOT/revalue_svhighlights_sparse7_8b_v1_1_2026-11-09/status.json`
- `$ZEROSHOT_ARTIFACT_ROOT/revalue_svhighlights_sparse7_8b_v1_1_2026-11-09/workers/<vid>/ledger.json`
- `$ZEROSHOT_ARTIFACT_ROOT/revalue_svhighlights_sparse7_8b_v1_1_2026-11-09/workers/<vid>/fact_memory.json`
- `$ZEROSHOT_ARTIFACT_ROOT/revalue_svhighlights_sparse7_8b_v1_1_2026-11-09/workers/<vid>/requests/`、`records/`、`pairs.json`
- 完成后：`$ZEROSHOT_ARTIFACT_ROOT/revalue_svhighlights_sparse7_8b_v1_1_2026-11-09/evaluation.json`、`results.md`、`complete.json`
- 项目结果文档：`docs/revalue_svhighlights_sparse7_v1_1_results_2026-11-09.md`，由CPU最终汇总自动生成。

最终报告将保留全七场分母，列出回退、无效输出与核验替换数；仅七场开发诊断，不视为SVHighlights全量或端到端Agent结果。当前未推送远程。
