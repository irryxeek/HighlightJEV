# TVSum：反证约束修复后的旧理由可见性对照 v1

日期：2026-11-08。用户已授权原 10 条视频、最多 100 次调用；本协议不扩大既定任务。

## 问题与对照

旧实验把未见运动、未见第一视角骑行者等“不足以支持”写成反证。此次先在两组共同修复判断契约，再比较 `R_keep`（显示旧 initial_reason）与 `R_hide`（该字符串置空）。两组使用同一个详细五维价值 rubric，唯一组间输入改动是两个候选的显式旧理由字段；不删除 F 中可能重合的叙述，不改变事实库，不修正旧事实。

修复后，模型自己的 observation.state 只允许 supported / insufficient。reason_check 针对提供的原理由，contribution 针对明确的单条 contribution_claim；二者判 contradicted 必须给出正面可见、与同一主体和时刻的该命题冲突的 counter。反证须原样绑定目标命题、引用候选片内且已作为观察依据的帧。隐藏或本来没有旧理由时必须 not_provided，不能从 F 重建原理由。

只有双方观察和贡献均已建立，才允许 A/B/tie/incomparable；一侧贡献未知不能作为另一侧获胜的依据。旧理由不确定并不禁止基于独立贡献比较。不强迫分差、胜负或正价值。缺证据措辞守卫只检查 counter.observation，保留命中原文；结构通过和词法通过都不保证事实真实。契约失败保留原响应并计入完整分母，不改写为“证据不足”。

## 固定内容

原运行：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_candidate_verifier10_27b_v1_2026-11-07`。逐字节复用各 shard 的 rows/pairs，共 10 视频、50 对、每对两次；固定候选、A/B、调用先后规则、8–12 张旧图片像素/PTS、相同 F（最多 1024 token）。旧 6 案例审计直接复用。准备与推理禁止读 GT 和旧指标；两个模型退出、预测冻结后才 CPU 评价。

模型继续用本地 Qwen3.8-27B，相同 revision、BF16、TP4、种子 0、温度 0、processor、依赖和引擎。`value_rubric.json` 与旧快照逐字节相同。

## 契约、预算与停止

每请求总上限 16384 token，输出 1536 token；原 observation/why/missing/basis 字数上限不变，不同时修改截断策略。新 counter 与 contribution_claim 增加共同输出负担；keep 组还可能额外生成 reason_counter。输入长度随理由是否存在变化，保持的是上限而非实际 token 数相等。

100 次正式/故障总尝试，零重试，最多 1638400 token；两个独立 TP4 worker，每个最多 50 次、819200 token、一次启动，活动 3540 秒＋退出 60 秒，累计最多 28800 GPU 秒（按 4 卡乘生命周期）。仅使用空闲 4090；忙时排队最多 3600 秒，不影响其他进程。模型异常、OOM、源码/输入/原生像素或 token 绑定失败停止该 worker，不重启；不合格响应记 invalid 后可继续不同的已冻结请求。未完成请求也保留在完整分母。旧预算不转入。

## 评价和结论边界

主对照为 hide−keep：合法率、A/B/tie/insufficient/incomparable，明确选择在所有 50 对/1000 人类评分位置上的吻合产出、已作选择的条件吻合、逐视频配对差值及描述性 bootstrap。保留所有平局、失败和未尝试；人类等分不记模型胜。对旧理由报警的分母仅为确实提供理由的候选；hide 分母为 0、比率未定义，不能宣称其报警减少是改进。

同时记录局部替换建议票差、未知保留基线的 CPU 反事实和具体坏例；不应用替换、不输出新排序、区间、mAP。旧 V 与新 keep 的比较仅为共同修复后的历史描述，不是单变量结果。10 视频无独立语义人工复核；不能把规则通过当视觉事实正确、把缺少旧理由的影响完全解释成暗示效应、或声称总体高光性能已提高。没有扩展剩余 30 视频的自动许可。

## 产物与复现

新根目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_reason_visibility10_27b_v1_2026-11-08`。

先在 CPU 完成测试和 native processor / xgrammar 上下文检查，再冻结 source_snapshot、requests、旧产物哈希与独立源码审查；supervise 只允许执行冻结源码。所有新请求/原始响应/失败/预测/账本独立保存，旧产物保持不变。完成后追加报告与 ARS 收据；不推送。
