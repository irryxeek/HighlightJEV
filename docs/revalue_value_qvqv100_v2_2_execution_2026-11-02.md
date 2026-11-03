# ReVALUE v2.2 固定100条 Q/Q+V 对照执行记录

## Material Passport

- Origin Skill：academic-research-suite / experiment-agent，run。
- 时间：2026-11-02，北京时间12:34启动；本文件为启动快照，最终状态以运行目录完成收据为准。
- 已授权任务：事实与证据绑定修复，固定100条query的Q/Q+V测试。

## 修复与已完成验证

生成约束绑定事实总数、连续ID和来源区域。每条事实只能来自同一区域；明确判断只能引用已存在的候选内事实，unknown仍可为空或使用上下文事实。原八条事实容量、JSON结构、状态含义、CPU依赖/时序/scope检查不变，无事后删改失败。

96项CPU测试、139候选语法、1360次字符串检查和30次真实Qwen token检查通过。旧212条合法解析相同，旧66条无效仍拒绝。重新冻结278个请求，新增格式提示每条21 token，最小上下文余量4761 token；98份像素文件哈希、真实PTS和帧顺序不变。

## 已启动及边界

- GPU 0，UUID GPU-52bc8c91-36c3-e8a6-29d7-855731f40568，启动前验证空闲及物理映射。
- CPU supervisor PID 52209，CPU finalizer PID 52210；PID为启动快照，不可据此终止其他进程。
- 共278次、零重试、28顺序worker，同时一卡；绝对token上限3,416,064，每worker600秒、累计16,800秒。
- 历史预算独立；不追加候选、回看、边界修改或其他数据集。所有worker退出后一次评价，并自动与v2.1对照、保存报告和归档。
- 当前尚无整批效果结论；技术合法不等于事实正确，重点同时比较TP、FP、召回与insufficient。

## 产物

- [协议](revalue_value_qvqv100_v2_2_protocol_2026-11-02.md)
- 运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_2_2026-11-02`
- 结果报告（完成后生成）：`docs/revalue_value_qvqv100_v2_2_results_2026-11-02.md`
- 准备与审查：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_2_preparation_2026-11-02`
- manifest SHA256：`6588699cd0ed31bd3422f0884a00494974bbdd6c27c6d91cb2008c83831a5235`
- authorization SHA256：`eab30077fb9b6994b43f721210d1646488bd3998235bb7879a790ea29460ed83`

运行器与收尾器可在会话结束后继续执行；异常保留现场，不自动重试。
