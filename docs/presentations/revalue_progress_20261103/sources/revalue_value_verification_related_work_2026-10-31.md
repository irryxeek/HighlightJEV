# 多维价值判断与区间验证：相关工作调研

## Material Passport

- Origin Skill: academic-research-suite / deep-research
- Origin Mode: quick；定向文献与实现核查，不是系统综述
- Origin Date: 2026-10-31
- Verification Status: UNVERIFIED（所述设计核对原文/公开代码，未运行或复现外部方法）
- Version Label: value_verification_related_work_v1
- 问题：现有工作如何把抽象价值转换成可操作判断，哪些适合当前 REZE Direct 区间 verifier？
- 边界：只检索公开资料并阅读源码，不加载模型、调用实验 API、运行推理或修改原实验。

## 1. 主要判断

已有明确先例，包括高光评价规则、维度专属检测器、二值问题库、动态评价细则和组合式语义验证。它们分别服务于观看价值、生成质量或文本与视频的一致性，不能混为同一种“正确性”。本次检索未确认有能直接替代我们五类价值与 QV 区间契约的现成模块；这不是对全部文献的不存在证明。

当前最有用的组合是借鉴 **VisionReward 的具体问题化、UnifiedReward-Flex 的按任务生成细则、DSG 的依赖约束，以及 VTune 的定位验证设计**。迁移是否有效仍需实验；“使用多维价值”本身已有先例。

## 2. 关键工作与实现依据

### VisionReward：维度 → 判断题 → 学习权重

论文定义视频的 9 个维度、64 个二值问题，利用人工问答监督微调 CogVLM2-Video，再以偏好对学习线性权重。公开推理入口选用 29 题，逐题调用模型，将答案映射为 ±1 后加权。它提供可查的问题库，而不是只给抽象维度名称。[论文 §2](https://arxiv.org/html/2412.21059v2#S2)、[实际入口](https://github.com/zai-org/VisionReward/blob/main/inference-video.py)、[29题清单](https://github.com/zai-org/VisionReward/blob/main/VisionReward_Video/VisionReward_video_qa_select.txt)。

可借鉴问题化与正负例校准。其视频生成偏好权重、二值输出和观看质量要求不应直接作为 grounding 拒绝规则；当前入口也没有我们的帧引用契约。

### UnifiedReward-Flex：按输入生成细分评价条件

该 2026 预印本在共同大类下生成与文本、视频相关的子维度，再给出分维度及总体比较。训练采用教师评估轨迹蒸馏 SFT 与 DPO；底座为 UnifiedReward-Think-qwen3vl-8B。[论文 §3.2、§4.1](https://arxiv.org/html/2602.02380v1)。

公开视频 demo 每段抽 8 帧；每个大类要求 3–5 个子维度，输出 JSON 理由、分数及赢家。其分项两视频分数之和固定为 10，总赢家限定二选一。[视频入口](https://github.com/CodeGoat24/UnifiedReward/blob/main/UnifiedReward-Flex/flex_pair_rank_video_generation.py)。

可借鉴任务适用性和具体检查项生成；不能原封不动采用强制赢家、零和打分或动态添加偏好要求。我们的单区间 verifier 仍需 unknown、不适用和来源约束。

### HIVE：专家规则驱动的高光价值判断

HIVE（EMNLP 2025 Industry）先形成结合人物、对白、关系和场景的叙事描述，再让 LLM 对照编辑规则逐场景评分。附录给出明确规则，例如剧情转折、情绪共鸣和悬念，命中则累计对应分数，输出场景 ID、理由和得分。[论文 §3、附录 A.3，表5–7](https://aclanthology.org/2025.emnlp-industry.185.pdf)。

这是“提示中给出可操作价值定义”的直接先例。但规则针对短剧广告及目标受众，依赖上游叙事质量，不能直接证明真实视频中某个 query 区间错误。本次核查论文提示模板，未验证完整运行代码。

### TRINITY：价值分支有专门信号和监督

TRINITY（2026）区分 Event、Emotion、Nature。事件沿用 Mr.HiSum 回看信号；情绪先用表情识别筛持续非中性片段，再由 Qwen2-VL-7B 核对类别；风景先筛场景，再用审美模型评分。检测网络以共享与任务专属时序表示输出三类分数。[论文 §3–4](https://arxiv.org/html/2608.29577v1)。

公开代码可见 emotion/event/nature 三个打分头。[模型文件](https://github.com/vanilladucky/TRINITY/blob/main/networks/sl_module/sl_module_split_heads.py)。可借鉴各维度有不同观察依据与监督的设计；它是经训练的高光检测器，不能当作现成 query 区间验证器。

### DSG：原子问题与依赖图

DSG（ICLR 2024）将文本转成语义元组、依赖关系和问题，由视觉问答模型逐题回答；父节点为 No 时，依赖问题的得分归零，防止“对象不存在但其属性成立”的矛盾。[论文与项目](https://google.github.io/dsg/)、[公开流程伪代码](https://github.com/j-min/DSG/blob/main/README.md)。

适合借鉴到“手机存在 → 屏幕可见 → 内容是否为文章”。这是本文的迁移建议，原方法面向图像生成评价，不能直接解决时序、边界或稀疏帧不可见问题。我们需要另行定义 unknown 的传播，不能将缺证一律计 No。

### VTune：直接研究定位后的验证

CVPR 2025 的 *On the Consistency of Video Large Language Models in Temporal Comprehension* 包含整句与主体/动作/关系的组合验证。VTune 利用内容被改错、时间区间被改错的训练例，让模型识别并纠正不一致，而不只学习输出时间戳。[论文 §3、§5.3](https://arxiv.org/html/2411.12951v1)。

其定位任务比生成偏好更接近我们。官方仓库注明旧 Charades-CON 训练数据有重叠并提供 v2 修订；若复现须注意该版本差异。[仓库与修订说明](https://github.com/minjoong507/Consistency-of-Video-LLM)。该工作不能证明原生 Qwen 加提示即可可靠自检。

### 补充：VideoScore2

VideoScore2 用视觉质量、文本一致性、物理/常识一致性的细则和人工分数训练 Qwen2.5-VL-7B，经过 SFT、GRPO 后输出分数及解释。它说明多维评估还可以通过专门监督学习。[论文 §3–4](https://arxiv.org/html/2509.22799v1)。它评估生成视频质量，未在本次核查中获得可直接用于 QV 区间拒绝的证据。

## 3. 对当前方案的具体启发（研究建议，非已验证结论）

建议结构：

```text
原 query
  → 保留原语义的必要条件及依赖
  → 选择相关价值视角，生成具体核查问题
  → 在固定旧帧中寻找可引用证据
  → supported / contradicted / unknown；无关维度标不适用
  → query 与边界控制规则输出区间核查结论
```

五类价值可保留为问题生成的分类，但应说明各自核查哪个原始要求。例如 outcome 问“是否达到 query 所要求结果”，information 问“界面内容能否确认”，action 问“是否发生必要动作”，emotion 仅在反应相关时启用，sensory 检查相关外观。不能自动增加“必须精彩、成功、有情绪”等约束。

优先顺序：先借鉴具体问题与依赖校验，修复相关但未证实的条件仍被判 supported；再用 query-only 对照检验价值提示的额外贡献。若缺证是像素/采样问题，再单独研究定向观察。不要同时更换模型、加入审美打分和回看，导致收益无法解释。

## 4. 检索范围、核查程度与限制

本次定向搜索覆盖视频高光、多维视频评价、视觉偏好和 temporal-grounding verification。检索词包括 `video highlight value emotion LLM`、`video temporal grounding verifier`、`multi dimensional video assessment` 及发现后的方法名。纳入有方法原文、与模块相关的工作；摘要站只用于发现，不作为实现依据。没有使用 S2 API，也没有进行系统综述式全量筛选。

重点读取上述方法章节、HIVE 提示附录；抽查 VisionReward 推理/问题/权重、Flex 视频提示、TRINITY 打分头、DSG 官方流程和 VTune 运行说明。没有把源码阅读说成运行验证，没有独立复现作者性能。公开设计能支持“如何实现”，不能独立证明其迁移到我们的数据有效。

只做公开资料检索、CPU 文档整理；本轮新增实验模型调用、实验 token、GPU、worker、重试均为 0，未修改或重跑旧实验，未推送。
