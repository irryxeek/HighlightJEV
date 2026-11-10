# REZE 启发的通用高光密集评分 v1：实现与 CPU 验证

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run（本轮仅实现及 CPU 检查；未执行模型推理）
- Origin Date: 2026-11-10
- Verification Status: UNVERIFIED（模型效果未验证；工程验证见准备收据）
- Version Label: generic_highlight_scoring_v1
- 用户请求：能否借鉴 REZE 方法，先实现一版我们在通用高光数据集上的打分方法。

## 目标与当前交付

实现一个不依赖 REZE 旧分数、旧 Top-5 或记忆库的通用高光评分器，直接输出完整时间轴分数。首个评价接口为 TVSum。现有 TVSum 的 27B Direct 是全片选片且依赖 B0 导出；本版本恢复逐窗口判断，避免把“是否选入最多五个建议”当作完整的密集评分。

代码位于 experiments/revalue_generic_highlight_scoring_v1（本地资料：`$MERIT_ROOT/projects/revalue_weekly_highlight_20261110/experiments/revalue_generic_highlight_scoring_v1/README.md`）。本轮授权按“先实现”处理；CPU 准备文件中的 `execution_authorized=false`。没有新增实验模型/API 调用、实验 token、模型权重加载、GPU 分配或实验 worker，没有推送。

## 评分流程

1. 输入完整视频和无标签元数据，使用连续 3 秒窗口、2 fps；完整窗口为 6 帧。沿用已有 REZE 真实 PTS、重复帧处理和缩放代码。
2. 每个窗口独立调用同一个视觉模型，问：这个片段是否包含有明确观看理由、值得保留进简短高光摘要的可见时刻？输出单个 Yes/No token。
3. 结果变化、有用信息、情绪反应、动作细节、视觉揭示仅作为可选判据示例。当前是一个整体问题，没有五路独立打分、固定加权、强制正例或强迫分差。
4. 两个标签均出现在 top-20 时，取 `P(Yes)/(P(Yes)+P(No))`。只有 Yes 时使用原词表概率；缺 Yes 时按原 REZE 回退为 0，并单独记录模式。该数值不是经校准的人类重要性概率。
5. 原样保留 REZE 的整数秒边界平均、缺口最近邻填充和相邻两秒平均，得到完整 1 秒及 2 秒分数。这里的时间映射并不表示模型独立观察过每个 2 秒片段。
6. 保存全部原始响应、token 概率、来源帧/PTS、失败和成本；冻结预测后再加载 TVSum 标注，计算 UMT Top-5 mAP。

## 与已有方法的对应关系

| 项目 | 旧 TVSum REZE B0 | 新 generic_highlight v1 | 旧 D-1fps |
|---|---|---|---|
| 模型 | Qwen3-VL-8B-Instruct | 默认同一现有 8B 权重 | 27B |
| 观察方式 | 3 秒局部窗口、2 fps | 相同 | 全片 1fps 帧并集 |
| 任务 | 将通用请求放入动作是否发生的模板 | 判断局部可见观看价值 | 全片直接选片 |
| 输出 | 单 token 概率 | 相同读数机制 | 最多五条建议和优先级 |
| 全片分数 | 独立窗口概率聚合 | 独立窗口概率聚合 | 建议与旧 B0 分数合并 |
| 旧 Top-5 / 旧分数输入 | 不需要 | 不需要 | 仍依赖 |

实现中保留 `reze_control` 条件，采用同一新运行器重建原提示。新条件的科学干预是任务提示整体（包括判据示例）；不能据此单独证明五维分类、某句话或某个维度的因果收益。提示长度必然改变，实际输入 token 和耗时会变化。新运行器保留默认多模态检查，没有复制旧运行器的跳过 profiling 参数；启动开销不宣称完全一致。旧 B0 只有在模型、完整输入和读数来源匹配后才能用作缓存对照。

## 失败、停止与解释边界

- 原始帧、模型元数据/权重文件状态或冻结源码改变时停止。每次请求前检查原生处理器展开后的完整上下文不超过 4096，单次输出最多 1 token。
- 单条或批次异常保留全部已经返回的原始内容，停止后续派发，不自动重试。一个窗口缺失则该视频的完整分数为 `null`；所有视频仍在分母中，评价单列零失败信用，不能用旧 B0 填补。
- `No` 同时包含可见支持不足，尚不能区分“确实不值得看”和“没看清”；此版不作为证据不足触发器。不能把 token 概率直接当作可信置信度。
- 局部窗口无法充分判断全片主题、重复程度、完整因果过程或全片最佳时刻。当前不加入全局记忆、比较器、ASR、回看或边界生成；这些都需后续独立变量实验。
- 常数分数、并列、缺标签 token 的回退均保留。即使 CPU 契约通过，也不代表能识别高光或优于旧基线。

## CPU 准备与后续实验范围

准备使用旧 REZE 两个无标签分片的完整 50 视频清单，顺序保持为分片 0 后分片 1；全部视频此前已用于开发。此清单只用于完整输入审计，不是已获批的全量推理。

按标注对应的视频时长，共 **4,213 个正式窗口**。如未来对全部 50 视频运行一个新条件，将需要最多 4,213 次正式尝试、零额外故障调用、零重试；按每次 4,096 token 保守预留，绝对 token 要求为 **17,256,448**。GPU 生命周期需要在实际执行范围确定后单独批准，当前为 `null`，并且 `execution_authorized=false`。运行器仅支持单 GPU、一次 worker，清理时间计入 GPU 生命周期上限。

这不是沿用旧 TVSum transfer 的 670 次、旧 QV、Direct 或 verifier 额度。若先做小规模，应在读标签前生成新的完整固定清单和准备收据，再确定其正式请求/token/GPU 边界，不能在此 50 条清单中按指标挑选片段。

工程验证覆盖概率读数、失败缺口、时间映射、禁止输入旧分数/标签、原始批次保留、原子收据、一次 worker 守卫与 TVSum 官方评价一致性。真实媒体 CPU 预检使用清单首视频的首/中/末窗口，比较两种提示的原生模板和输入帧，并核对旧 REZE 像素哈希；这不是全 4,213 窗口 GPU 预检。

实际检查数、源码/输入哈希与产物路径见 implementation_receipt.json（本地资料：`$MERIT_ROOT/projects/revalue_weekly_highlight_20261110/sources/artifacts/revalue_generic_highlight_scoring_v1_2026-11-10/implementation_receipt.json`）。完成后的完整源码快照、50条元数据、CPU 预检和默认禁止执行的预算模板保存在同目录 `preparation/`。

本轮已完成的工程检查：**26 项 CPU 测试通过，新增源码 Ruff 检查通过**。首视频 `WxtbjNsCQ8A` 的第 0、44、88 号窗口均通过原生处理器检查，像素哈希、真实 PTS 和采样帧索引与旧 REZE 完全一致。前两个窗口的输入由 777 增至 901 token，尾窗口由 549 增至 673 token，均低于固定上下文上限；这是提示长度差异，不是新增视觉输入。只核查了这 3 个真实窗口，不能写成全量原生预检通过。

独立只读代码审查提出的 5 项运行边界问题已修复并复核：总 GPU 时间内预留清理、禁止脱离 supervisor 直接启动 worker、收据原子发布、全批原始响应先保存、预检绑定实际冻结源码。GPU 引擎启动、真实生成与 GPU 子进程退出尚未实测。准备收据与本地 ARS 运行账本均记录新增实验模型/API 调用、实验 token、GPU 秒和实验 worker 为 **0**。

## 下一步如何检验

先在新冻结的完整开发子集上对照同模型 REZE 与新评分条件，主看全分母 Top-5 mAP 及按视频配对差异，同时检查常数分数、概率饱和、top-20 回退比例和真实失败率。不要只挑已知反例或只报告成功窗口。若局部判据有效，再单独测试“事实上下文是否改善评分”；当前不直接叠加完整 Agent。

## 来源

- 原 REZE TVSum 实现（本地资料：`$MERIT_ROOT/projects/QVHighlights-ZeroShot/experiments/reze_tvsum/README.md`）：冻结的 3 秒、2 fps、8B、单 token 和概率读数。
- Direct 密集视觉对照（本地资料：`$MERIT_ROOT/projects/revalue_weekly_highlight_20261110/sources/revalue_tvsum_dense_direct_10v_results_2026-11-07.md`）：全片选片与 B0 导出的实际限制。
- [本周会议对照汇报](revalue_weekly_progress_2026-11-03_to_2026-11-09_meeting_revision.md)：事实、价值和 verifier 当前结果与未解决问题。
