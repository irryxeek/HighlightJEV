# TVSum 固定十视频：F / FV 离线案例审计

日期：2026-11-05。使用 academic-research-suite 的现有实验工作流，仅审计已经冻结的产物。

**结论：当前问题同时存在于价值判断、事实引用与评分导出，不能概括成“价值全为空”或“NA 挤掉了有效记忆”。** 下一轮只改变两臂共同选片提示中的相对价值判据，是可解释的单变量验证；它能否改善结果仍待实验，不能预先宣称能修复事件错配。

## 范围与来源核验

父轮为 `$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_highlight_memory_27b_v2_1_2026-11-05`。按父轮原顺序纳入全部 **10 视频、100 个 F/FV 推荐、400 条原始价值条目**，无成功子集筛选。规则先存入 `audit_rules.json`；未修改旧预测、阈值、源快照或协议，未调用父轮评价器或 finalize。

核对了 complete → ledger / evaluation / predictions、prediction_freeze → 110 条 records / 退出收据、实际 requests_sent → 冻结请求定义、源快照、10 份 memory、冻结帧文件及实际装箱文本的哈希链。F/FV 均为 10/10 complete；父轮唯一无效输出是 `Yi4Ij2NM7U4` 的 D，不应混称为 F/FV 失败。来源清单共 283 个文件，结束时再次核验不变。

| 父轮产物 | SHA-256 |
|---|---|
| evaluation.json | `0c06d8772e16482dc1fba2d203585a87b72baec073b0647d6670defc82016b95` |
| ledger.json | `e6f291c05a3b17d3cf24317eb79eb40dd0e137a3d30bc57cad00546db488729a` |
| predictions.json | `2d49d32e3a14e1c152b3e568bc6b9d6026c56f18a542048aead57a0de1cde19c` |

## 已证实的机械事实

### 1. 记忆有内容，但完整原 bank 不等于模型实际收到的记忆

| V 状态 | 原 bank | 实际装箱 | 未装箱原因 |
|---|---:|---:|---|
| supported | 169 | 92 | 76 条的关联事实未进入 F；1 条因 V token 预算 |
| unknown | 10 | 10 | 0 |
| not_applicable（NA） | 221 | 219 | 2 条因 V token 预算 |
| 合计 | 400 | 321 | 79 |

F 从 186 条事实保留 114 条。装箱规则要求 V 的全部来源事实均在活跃 F 中；因此 **76 条 supported 损失发生于来源资格检查**，不能说是被 NA 直接挤掉。固定顺序和事实长度可能影响这一选择，但其下游精度因果未验证。

CPU 原生 tokenizer 复核 F/V/FV token 数全部一致。仅用于计量，将已装箱 NA 文本从字符串中移除后的 token 差分为 **5,660 / 原 V 合计 9,551**；这不是重装箱结果或新模型输入。`Bhxk-O1Y7Ho` 保留 30 条 NA，其差分为 830 token；唯一直接因 V 预算被拒绝的 supported 为 `g02.v.sensory`。有容量占用事实，不等于已证明删 NA 能提升指标。

### 2. 合法锚点不保证事实解释正确

100 个 choice 均符合冻结的 0.5 秒边界容差。逐条保留 choice / clip 区间 / 本地帧 PTS / fact_ids / 原始事实来源 PTS：

| 来源情况 | 选择数 |
|---|---:|
| 所引事实同时包含本地与上下文来源 | 53 |
| 所引事实仅包含本地来源 | 16 |
| 全部事实来源均为非局部上下文 | 19 |
| fact_ids 为空 | 12 |

“本地”采用 `[2×clip−0.5, 2×(clip+1)+0.5]`；上下文允许跨片段。**19 条非局部引用不能当成 19 条错误；12 条空引用也不等于缺少图像证据。** 例如 JK 的 77 秒红衣舞者引用 57.48–70 秒同一表演，旧帧仍支持；跑酷 46.98 秒跳跃引用更早/更晚跑酷事实，锚帧也支持其动作。

### 3. 推荐顺序与最终评价顺序有两层差异

父轮 `contract.py:394` 先按 B0 顺序排列同 tier 候选，再把原 B0 分数多重集分配到新排序。16/20 个选片响应含同 tier，12/20 的原始推荐顺序因此发生变化。再受原分数同分及原生排序影响，4/20 的 native Top5 顺序与该中间排序不同。

20 个 F/FV native Top5 均改变了 B0 成员。仅 `sTEELN-vY30/F` 的推荐成员没有全部进入 native Top5：推荐 clip 67 被同分 clip 5 替代。既有 native 与固定 clip-id 稳定同分顺序在 7/20 个输出上不同，其中 2 个改变 Top5 成员：`sTEELN-vY30/FV` 的 50 ↔ 5，`cjibtmSLxQ4/FV` 的 102 ↔ 96。没有为此改分、强迫胜负或重新评价。

## 全部十视频逐例审查

下表按冻结顺序。Δ 为**直接抄录父轮已有评价**的 FV−F Top5 AP 百分点，仅提供结果背景；不是此次新增测量。S 为原 bank supported → 实际装箱 supported；远处引用列为 F/FV 各自“全部来源非局部”的数量。

| 视频 | S | 远处引用 F/FV | Δ pp | 旧帧与完整理由审查要点 |
|---|---:|---:|---:|---|
| JKpqYvAdIsw | 20→12 | 1/0 | −7.0313 | FV 加入 2.48s 道路帽子并列 tier 0；帽子确实可见，但 distinctive setup 没有给出胜过舞蹈的理由。77s 远上下文舞蹈引用可合理成立。 |
| JgHubY5Vw3Y | 18→9 | 0/1 | +26.0208 | U 锁和钢缆步骤有支持；FV 将 51.99s 俯身拆轮写成 56.99–61.49s 携轮步行，存在阶段错配支持案例。 |
| sTEELN-vY30 | 25→16 | 0/0 | −2.7361 | 受损车/地点地图有支持；原 V 的 moving train 与所引 stopped 事实不一致（该项未入箱）。采访 distress 的强度尚未独立核验；同分改变第 5 位。 |
| Yi4Ij2NM7U4 | 17→9 | 3/2 | −0.2778 | 两臂选片成员相同；FV 的 255s 锚点是放入香肠，却写加入洋葱青椒，借用了 263.5s 的后续步骤。371s 成品引用邻近后续帧则不必然错误。 |
| fWutDQy1nnY | 18→8 | 1/1 | +11.3889 | 两臂推荐成员完全相同，收益对应 tier/排序改变；舞龙舞狮有支持。标题、路边针筒为何值得优先观看没有相对依据。 |
| Bhxk-O1Y7Ho | 8→5 | 0/0 | +0.3125 | 流水冲垫、抚摸犬毛、室外走路均真实可见；“distinctive”主要复述普通事实。存在唯一直接 V 预算拒绝项，但未验证其指标影响。 |
| Se3oxnaPsz0 | 17→9 | 1/1 | −31.9444 | FV 在白猪锚帧 48.5s 上使用蜂群理由/52.5–55s 事实；F 在 83.5s 男子采访帧使用 72.5–74.5s 粉衣人物伸手描述。内容错配跨两臂存在。 |
| cjibtmSLxQ4 | 16→9 | 1/1 | −3.5833 | 倒立、跳跃、攀墙有旧帧支持；g06 action/sensory 的屋顶理由却引用室内采访事实，原 bank 已误关联且装箱保留。4 条 unknown 全部保留。 |
| J0nA4VgnoCo | 15→6 | 1/1 | +3.2917 | 双拇指、滑板、换胎动作可见；F 27.99s 写 missing wheel，而锚帧可见后轮仍装在车上。若干远处轮胎工作引用可作上下文，不能证明具体拧紧阶段。 |
| E11zDS9XGzg | 15→9 | 2/2 | −4.0313 | FV 强调横幅、号码、犬种文字；事实存在不等于相对高光。F 48.5s 采访锚帧写成与 Rottweiler 合影，借用了更早 40.5s 内容。 |

每个视频的全部 10 个选择均有独立记录，见 `semantic_reviews.json`；100 行完整引用表为 `selections.csv`。40×10 原始 V 的状态、理由、来源及保留情况均在 `values.csv` / `cases.json`，没有只保存上述示例。

## 关键来源链与结论边界

- **值与事实误关联已在 bank 中存在：** 跑酷 `g06.v.action` / `g06.v.sensory` 说屋顶动作，却只引用 `g06.f00`（492.99–513.48s 室内采访）；正确室外素材位于另一事实 `g06.f01`（523.99/544.48/554.49s，标为 uncertain）。装箱是完整保留已有条目，并未凭空产生这段文字。源字段不匹配可核对，视觉判断仍属助手旧帧审阅。
- **有效事实被用错锚点：** 蜂害视频 `g03.f00` 的蜂群在 52.5/55s 确实可见，FV 却选择 `c0024_f0022`（48.5s 白猪）并沿用蜂群理由。这不是证据全空；choice 时间绑定正确与解释正确是两个检查层级。
- **普通事实到价值的跳跃：** 帽子摆在道路、骑车、流水冲垫、普通步行等被描述为 distinctive / crucial。存在性有视觉支持，相比全片其他候选为什么更值得观看往往没有给出。此为支持“相对价值判据”假设的案例，尚不构成性能下降的因果证明。
- **评价与案例不能互相代替：** 父轮 F=57.1878、FV=56.3288，FV−F=−0.8590pp，4 视频改善、6 下降；native 与 stable tie 既有读数亦不同。单例好坏、文字更具体或来源更近都不能代替固定十例整体结果。

下一轮仍按主代理协议：共同选片提示加入相对价值判据，保留全部原 F/V、NA/unknown 装箱、引用规则、候选表、旧帧及输出接口。**本报告、逐例审查、标注侧指标不得进入模型提示。** 暂不同时修记忆装箱、事实局部门槛或分数导出，否则无法解释单变量效果。

## 产物与零新增调用收据

审计目录：tvsum_relative_offline_audit_2026-11-05（本地资料：`$MERIT_ROOT/comparisons/tvsum_relative_offline_audit_2026-11-05`）。包含 `audit.py`、冻结规则/源哈希清单、`cases.json`、`semantic_reviews.json`、四份 CSV、完整阅读包、20 张旧帧拼图及 `render_receipt.json`。`write_review_notes.py` 保存本次助手逐例审阅文字的生成过程，不调用模型。

实际 CPU 命令：

```bash
CUDA_VISIBLE_DEVICES='' $SHARED_DATA_ROOT/longvt-repro/env/inference/bin/python comparisons/tvsum_relative_offline_audit_2026-11-05/audit.py build
CUDA_VISIBLE_DEVICES='' $SHARED_DATA_ROOT/longvt-repro/env/inference/bin/python comparisons/tvsum_relative_offline_audit_2026-11-05/audit.py render
CUDA_VISIBLE_DEVICES='' python comparisons/tvsum_relative_offline_audit_2026-11-05/write_review_notes.py
CUDA_VISIBLE_DEVICES='' $SHARED_DATA_ROOT/longvt-repro/env/inference/bin/python comparisons/tvsum_relative_offline_audit_2026-11-05/audit.py finish
```

build 的来源、记录、完整条目、实际 prompt、token 数和导出向量一致性断言通过；导出检查只复原既有算法并逐值比对旧预测，没有输出新模型预测或计算新 AP。拼图只读冻结 `.npy`，无视频重新解码/采帧。

**本次新增实验模型/API 调用 0，重试 0，GPU 分配及 GPU 时间 0，新源视频帧 0。** Tokenizer 计量和助手查看旧图片不是新增实验模型请求，也不是独立人工盲评；未建立新的 GT 帧标签。父轮 110 次请求仍属于父轮账本，不重置、不混入本次；后续 20 次由主代理另行记账。

`audit_complete.json` 最后写入，仅含完成状态、10 视频覆盖、F/FV 两臂、零调用/零 GPU 与产物哈希，作为后续启动硬前置；无逐例指标。完成后本审计产物停止写入。
