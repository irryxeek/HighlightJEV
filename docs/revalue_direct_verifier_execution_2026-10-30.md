# ReVALUE 区间 Verifier v1.1 执行记录

## 最终状态：2026-10-30 20:40完成

139/139次请求均返回，14/14个worker退出0，零重试，所有所属推理进程已退出。20:40:59完成响应冻结、CPU评价和归档；20:51再次核对实时进程、冻结源码/输入/base、原始响应、账本、评价、报告以及296个归档文件的哈希，全部通过。后文的“正在生成”等文字是启动/中途快照。

实际成本：656,389 token，3,283.347139 GPU秒（54.72分钟），均在独立上限内。旧预算没有转入，没有新请求或重跑评价。

科学验收未通过：81个输出通过结构/引用契约，58个无效；合法输出54个flagged、10个supported、17个insufficient。按最大GT IoU<0.5的错误代理，54个报警中29个命中、25个误报，precision=53.70%、recall=34.12%、正确区间误报率=46.30%。固定CPU时长规则的对应值为77.50%/36.47%/16.67%，当前点估计没有显示verifier优势。尚无独立人工语义审阅，不能把29个指标命中称为29个已确认真实反例。

58个无效输出中，39个query直接证据并非全部片内，11个事实引用缺失或重复，其余8个属于query引文或事实/边界区域约束问题。全部139个响应正常stop，没有输出长度截断；这些契约失败不能写成OOM或重试失败。

完整[结果报告](revalue_direct_verifier_results_2026-10-30.md)与归档（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/revalue_verifier_v1_1_2026-10-30/README.md`）已生成。最终ledger SHA256：`dd00c703ba9b2b06ce17686484bd2b7a9f42134744a7a24644a43bec8d372cb8`。本轮不扩大运行、不修改既有预测，未推送远程。

## 授权与冻结

用户在原会话明确回复“启动验证”，执行此前已审查的[固定协议 v1.1](revalue_direct_verifier_plan_v1_1_2026-10-30.md)。授权已绑定 manifest；原未授权收据与 CPU 准备快照保留。

- 启动时间：2026-10-30 19:46:07（北京时间）。
- 固定范围：原 QV100 的 139 个有效 REZE Direct 区间；原预测、排序和边界不变。
- 输入：冻结的旧帧、实际 PTS 与原 query；每区间一次验证，不增加源视频观察。
- 独立上限：139 次尝试、零重试、1,138,688 token、14 个顺序 worker、同时最多一卡、每 worker 300 秒、累计 4,200 GPU 秒。所有旧额度均不转移。
- 启动前：22 项 CPU 契约检查已通过；本次再次核验源码、输入、依赖、base 与授权哈希。没有重复跑准备实验。
- manifest SHA256：`1e2972b27c68956e9636d3e7cd4dcb4f5ac0eaf8113b68e55bb8227dad2151f4`。
- inputs SHA256：`35f3c3297eed02b36ef32b98bdca1ac93b8e6ffdaa2113f6d379ee1f85b52f8a`。

## 执行入口与观察

```bash
$LONGVT_ARTIFACT_ROOT/env/inference/bin/python $ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_1_2026-10-30/source_snapshot/supervise.py --run $ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_1_2026-10-30
```

运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_1_2026-10-30/`。首次 supervisor PID 2452，首个 worker 选用当时空闲的物理 GPU 4。后续由冻结 supervisor 逐批检查空闲卡，不占用其他用户进程。

当前段落为启动快照：已完成模型加载，正在生成。实际进度以 `ledger.json` 为准；最终终止和成本以 `campaign_exit.json`、各 worker 的 `exit.json` 为准。后台单次分派与独立预算守卫已启用，不自动重启失败请求。

## 评价与结论边界

所有所属 worker 确认退出、响应冻结后，才使用冻结 CPU 评价器读取 GT。报告反例筛查精确率、召回率、误报、有效不确定与技术错误，完整保留 139 个候选分母及 100 条 query 总体。两个 base 空预测单列，不冒充 verifier 检出。

低 IoU 是错误代理，不能自动等同于真正的语义定位错误；没有独立人工审阅时明确记为 0。该轮不改定位输出，也不检验五类价值的独立贡献。结果产生前不声称 verifier 有效或定位性能提升。

ARS 账本已记录本次原话授权和启动；一次账本工具调用因 `command` 字段使用数组被拒绝，改为字符串后写入。这是记录格式修正，没有重启 worker 或新增实验调用。原被拒绝的输入 JSON 保留供审计。

## 自动收尾（CPU）

2026-10-30 19:53 启动独立 CPU 收尾程序。它等待本轮 `campaign_exit.json`，确认全部模型 worker 终止后，仅调用一次已冻结的 `source_snapshot/evaluate.py`。评价器还会实时核对所属进程已退出，冻结响应，然后读取 GT。未确认退出、已有响应冻结、评价失败均停止，不重试、不启动任何模型、不干预实验进程。

收尾脚本为 `experiments/revalue_verifier/finalize_cpu.py`，另存至运行目录的 `cpu_postprocess_source/`；没有修改 GPU 实验源码快照、manifest、输入、提示或预算。5 项新增 CPU 测试通过，覆盖未终止阻断、退出不确定阻断、重复评价阻断、失败零重试和合成结果归档。测试没有读取真实标签或调用实验模型。

完成后自动生成：

- `docs/revalue_direct_verifier_results_2026-10-30.md`：完整计数、筛查指标、状态/价值分布、预设门槛、成本与结论限制。
- `comparisons/qwen_direct/revalue_verifier_v1_1_2026-10-30/`：输入、原始输出、引用失败、源码、账本、退出收据与 CPU 评价；帧数组和模型保留 SSD，不复制。
- 原运行目录 `cpu_finalizer_complete.json` 或 `cpu_finalizer_failure.json`：CPU 收尾最终状态。

上述结果路径在运行结束前尚无正式结果。初步快照（19:53）：19 个请求已返回、1 个生成中；14 个通过契约、5 个无效。首 worker 10 个请求正常结束、225.50 GPU 秒，无所属残留进程。引用无效已超过“至少138/139合法”的预设门槛，不能因运行健康而宣称科学验收通过。继续完整清单是冻结协议对引用无效的预定处理，不追加请求或调整提示。
