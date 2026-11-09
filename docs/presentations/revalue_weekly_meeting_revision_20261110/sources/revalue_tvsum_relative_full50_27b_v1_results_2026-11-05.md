# ReVALUE TVSum 全 50 视频：F-relative / FV-relative

## Material Passport

- Origin Skill / Mode: academic-research-suite / experiment-agent，run。
- Verification Status: UNVERIFIED；CPU 来源与评价检查完成，独立语义审阅 pending。

固定原 REZE full50 的顺序与完整范围。旧 val10 的 20 个相对选片输出逐字节复用；其余 40 个视频仅执行冻结的 8 组建库与 F/FV 选片，最多新增 400 次调用。
新 40 条属于 UMT 原 official train；本工作不训练模型。本轮主确认看新 40 条 FV−F，全 50 条仅为扩展零样本汇总，不能称为官方 test50；旧 10 条是开发集复用结果。

| 范围 | 视频数 | 条件 | 原生 Top-5 mAP (%) | 稳定同分敏感性 (%) | 合法输出 |
|---|---:|---|---:|---:|---:|
| 旧 val10（复用） | 10 | B0 | 61.3167 | 61.3288 | 缓存基线 |
| 旧 val10（复用） | 10 | F-relative | 59.7625 | 60.0608 | 10/10 |
| 旧 val10（复用） | 10 | FV-relative | 62.9247 | 62.8132 | 10/10 |
| 新 40（原 official train） | 40 | B0 | 53.2858 | 53.7594 | 缓存基线 |
| 新 40（原 official train） | 40 | F-relative | 52.6220 | 52.3843 | 40/40 |
| 新 40（原 official train） | 40 | FV-relative | 50.6473 | 50.2771 | 40/40 |
| 全部 50（零样本汇总） | 50 | B0 | 54.8919 | 55.2733 | 缓存基线 |
| 全部 50（零样本汇总） | 50 | F-relative | 54.0501 | 53.9196 | 50/50 |
| 全部 50（零样本汇总） | 50 | FV-relative | 53.1028 | 52.7843 | 50/50 |

新 40 条主差值 **-1.9747 pp**；改善／下降／持平 20/19/1；逐视频配对 bootstrap 95% 区间 [-5.588491753472224, 1.1279752604166629]。

## 失败、选片变化与结论边界

失败分类：`{'memory': {}, 'selection': {}}`。
无效建库不补造记忆；依赖失败的选片记录 model_called=false，不进入 API 调用账本。技术失败、未尝试和依赖失败均保留 B0 回退，完整分母不减少；合法空选片单独记作弃权。
新 40 的 Top-5 成员／顺序变化：`{'F': {'score_vectors_changed': 40, 'top5_members_changed': 38, 'top5_order_changed': 40, 'top5_order_only_changed': 2}, 'FV': {'score_vectors_changed': 40, 'top5_members_changed': 39, 'top5_order_changed': 40, 'top5_order_only_changed': 1}}`。
数值门槛：`{'primary_scope': 'new40_official_train', 'final_valid_new_count': 80, 'expected_new': 80, 'final_valid_full50_count': 100, 'expected_full50': 100, 'at_least_95pct_new': True, 'primary_gain_at_least_1pp': False, 'numerical_gates_passed': False, 'semantic_evidence_review': 'pending', 'automatic_expansion_authorized': False}`。来源与时间契约合法不证明画面语义真实；不自动扩样，不将旧开发集收益当作新 40 条收益。

## 调用与成本分账

本轮实际新增尝试 **400 次**；已知 token **2874679**，计账 token **2874679**；GPU 生命周期 **48075.816 秒**。
新增建库／F 选片／FV 选片：`{'memory': {'requests': 320, 'actual_known_tokens': 870953, 'charged_tokens': 870953}, 'F': {'requests': 40, 'actual_known_tokens': 983577, 'charged_tokens': 983577}, 'FV': {'requests': 40, 'actual_known_tokens': 1020149, 'charged_tokens': 1020149}}`。零自动重试。
旧 val10 的 **80 次建库／208,128 token** 与 **20 次相对选片**分别复用，复用输出的新增调用为 0。
| 独立方法成本口径 | 已记录调用（含缓存） | 已知 token（含缓存） | 计账 token（含缓存） |
|---|---:|---:|---:|
| F-relative | 450 | 2301248 | 2301248 |
| FV-relative | 450 | 2347431 | 2347431 |

每个独立方法在完整成功时计 400 次建库和 50 次选片；两臂共享建库，上述独立方法口径不能相加作为真实总消耗。REZE 缓存初始化另列，未记入本轮新增。
保留所有旧启动失败与修复轮次后，该研究系列累计模型尝试 638 次，含预派发失败的预留 639 次，5058988 计账 token，82832.764 GPU 秒。
完整旧账本口径保存在 cost_accounting.preserved_prior_accounting，没有重置或覆盖。

逐视频结果、完整预测、来源审计与退出收据：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_relative_full50_27b_v1_2026-11-05`。
