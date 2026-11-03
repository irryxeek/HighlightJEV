<!-- ppt-master-schema: design-spec/v1 -->
# ReVALUE 实验进度与结果 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | revalue_progress_20261103 |
| Canvas Format | PPT 16:9, 1280 × 720 |
| Page Count | 15 |
| Primary Language | zh-CN |
| Target Audience | 导师与组会成员，了解 grounding 主线，需要判断当前证据与下一步实验 |
| Communication Intent | 汇报已完成的基线与对照，解释工程进展及科学卡点，并对齐下一步验证任务 |
| Desired Audience Outcome | 能准确区分输出合法性、语义检错和定位质量，理解价值引导尚无稳定收益、32B 前20条已完成但未改善 |
| Core Message / Ask / Action | 输出可靠性已改善；32B同样本检错未改善，先诊断事实质量与unknown传播，再验证价值提示及边界 |
| Delivery Context | 中文组会现场主讲约 10–12 分钟，会后结合讲稿复核 |
| Artifact Afterlife | 项目内可编辑 PPTX 与逐页讲稿，保留来源和时间快照供后续复用 |
| Reading Mode | balanced |
| Content Strategy | 根据报告重新组织，保留所有主结论、分母、证据边界和失败状态；不加入新的实验预测或事实 |
| Design Style | 证据驱动的研究进展：深蓝标题、青绿数据、橙色风险，平面图表与开放式网格 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy |
| Custom Animations | disabled — final Stage-2 proactive policy |
| Narration Audio | disabled — final Stage-2 proactive policy |
| Created Date | 2026-11-03 |

沿用会话中用户已明确委托的“设计细节由你决定，直接完成”。Stage 1 采用 free_design，固定中文、导师组会、16:9 与上述沟通目标；不生成 UI 确认收据。修订快照截至 2026-11-03；沿用已交付项目的设计与用户委托。本轮在新版本目录修订，保留旧报告和PPT。

Stage 2 三个完整方向：

1. **证据与缺口（选用）**：先给结论，再用基线、对照、修复、案例和失败收据支持，最终收束到验证任务。Mode 为 custom，以 pyramid 为唯一目录基础。Visual style 为 custom，以 swiss-minimal 的开放网格和粗细层级为主体，采用 data-journalism 的数字、来源线与证据旁注；字体为 Microsoft YaHei / Arial，正文 24px，标题加粗同族形成 concord。六色角色为白、浅灰、深蓝、青绿、橙、深灰。备用图像 rendering 为 custom：清晰实线、平面不透明色、少量细规则、无材质深度，情绪如实验室证据图；本次不启用图像资源。
2. **问题演进**：依次讲基线失误、契约修复和仍然存在的未知，最后给定位闭环问题，Mode custom 自定义问题推进。Visual style custom，浅暖白底、深墨色标题、蓝色数据、赭色旁注，以较大留白和左右错落注释组织；标题 SimSun / Cambria，正文 Microsoft YaHei / Arial，24px，形成 contrast。六色为 #FAFAF7、#F0F1EC、#203442、#287E91、#B86C43、#242B30。Rendering custom：细轮廓、轻纸感、浅层标注、审慎而叙事化，如研究手记；不启用图像。
3. **机制拆解**：从输入、条件、证据、结论的链条进入，依次展示各环节的验证状态，以任务图结束，Mode custom 自定义机制解释。Visual style custom，白底、深蓝灰、冷蓝和暗红，强轴线与分支关系，标题 SimHei / Arial、正文 Microsoft YaHei / Arial，24px，形成 contrast。六色为 #FFFFFF、#F2F5F8、#233B53、#346FA1、#A8504B、#202C39。Rendering custom：等重线条、平面示意、明确分层、精确克制，如系统设计审查图；不启用图像。

选用方向 1：当前需要把“工程修复有效”与“方法收益未证实”同时讲清楚，结论先行和可直接比较的数据最适合。更新后共 15 页，notes 开启，动画与音频关闭，图表和表格按原生可编辑对象导出。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 56px horizontal; 42px top; footer below 672px |
| Content Area | x=56..1224, y=42..656 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: pyramid
- **Mode Behavior**: 结论先行，依次交代冻结基线、对照设计、数据与案例，最后给出有验收标准的下一步；区分工程成果、代理指标和待检验假设。
- **Visual style**: custom
- **Visual Style References**: swiss-minimal, data-journalism
- **Visual Style Behavior**: 采用开放网格、左对齐的重标题与平面几何，数据页围绕比较图表展开；细来源线、证据旁注与大数字形成层级，青绿承载新实验、橙色标注风险，结构页用流程和分支承载机制。
- **Theme**: “证据链”细线与条件节点作为可变连续线索，流程页连接模块，案例页指向断点；不在无关系页面强行重复。
- **Tone**: 简洁、审慎、可审计，成果与限制同页可见。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 主背景 |
| Secondary background | #F2F5F8 | 解释区、表格交替行 |
| Primary | #17324D | 标题、主要流程、Q 系列 |
| Accent | #237F89 | Q+V 系列、已完成工程状态 |
| Secondary accent | #C96A32 | 风险、待验证项、证据不足 |
| Body text | #243748 | 正文 |
| Secondary text | #637485 | 注释和来源 |
| Divider | #CFD9E2 | 分隔线 |
| Surface | #EAF3F3 | 轻量信息底 |
| Grid | #E5EBF0 | 图表网格 |
| Negative | #B44747 | 误报与无效输出 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 稳定、加粗、左对齐 | Microsoft YaHei | Arial | sans-serif |
| Body | 清晰、可投影 | Microsoft YaHei | Arial | sans-serif |

- **Title stack**: Microsoft YaHei, Arial
- **Body stack**: Microsoft YaHei, Arial

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 42 |
| Subtitle | 30 |
| Lead | 28 |
| Annotation | 20 |
| Footnote | 14 |
| Display | 64 |
| Cover | 60 |

Display 与 Cover 沿用同一字体栈，以字号和字重形成层级；所有细节进入讲稿，避免缩小主文。

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 判断句标题先行，主图或主机制居中，注释说明适用边界，底部保留来源。
- **Composition tendency**: 大数字封面、横向流程、比较表、数据轴、响应审查和后续路径交替，避免等权容器连续堆叠。
- **Cross-page continuity**: Q 深蓝、Q+V 青绿；unknown 橙色、invalid 暗红；案例页用相同“条件—事实—结论”语义链。
- **Spacing posture**: 数据页紧凑但保持可读，案例与结论页留白放大关键断点。
- **Spacing anchors**: page margin 56px; block gap 24px; column gutter 32px; corner radius 0px; body leading 36px.

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | table | comparison_matrix | 保留两种 Direct 的完整100条对照 |
| P06 | chart | horizontal_bar_chart | 8B Q/QV 完整139候选召回 |
| P07 | chart | column_chart | 同口径旧版与新版无效输出 |
| P08 | chart | stacked_bar_chart | 8B 四类输出完整分布 |
| P09 | table | comparison_matrix | 两模型同20条、37候选的对照 |
| P13 | table | comparison_matrix | 语义核查和时长规则的代理检错 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| video_comparison.png | 1600x1100 | 1.4545 | 证明GT与Direct原视频及证据能够同页审查 | Screenshot | 完整界面占主体，右侧原生文字解释两个播放器 | no-crop | user | Existing | projects/revalue_trace_viewer/validation/video_2026-11-03/preview-video-comparison.png | retain original interface text; key explanation stays editable | primary |

本地既有工程截图，原像素完整保留；仅展示页面能力，不作为独立语义核验。

## IX. Content Outline

#### Slide 01 - 最新结论
- **Audience move**: 理解工程进展与科学缺口。
- **Relationships**: 合法性改善和32B负结果为并列证据。
- **Title**: 输出更可靠了，检错仍未解决
- **Core message**: 8B合法率98.20%；32B前20条已完成但没有改善。
- **Content**: 阶段2026.10.30—11.03；8B278/278次、32B74/74次；价值引导收益未确立；grounding主线。

#### Slide 02 - 当前 pipeline
- **Audience move**: 区分当前实现与后续完整闭环。
- **Relationships**: order：Direct候选、帧与条件、事实与判断、CPU验收；query到冻结条件为输入分支。
- **Title**: 基线定位区间，verifier 检查内容条件
- **Core message**: 只验证内容，未修正边界。
- **Content**: 保留原页全部信息：固定100 query、98有候选、139区间；Q/QV共享条件与输入；事实和引用进入三值判断；尚无回看、边界修正或最终定位提升。

#### Slide 03 - 固定基线
- **Audience move**: 了解后续对照采用的冻结基线。
- **Relationships**: contrast：自定义Direct与REZE Direct。
- **Title**: REZE Direct 已固定，指标尚无一致优势
- **Core message**: 两种Direct并非单变量；verifier不改定位。
- **Content**: 保留原页完整100条train指标：42/39、28/30、24.72/26.48，单位%；帧数、提示和输出形式不同。
- **Visualization**: baseline-table：三个指标×两种方法。
- **Native-ready**: baseline-table=yes

#### Slide 04 - 文献到设计
- **Audience move**: 看懂价值核查设计的来源和实际迁移。
- **Relationships**: link：四项论文原则分别对应四项本项目实现；order：query条件、证据核查、结果。
- **Title**: 从相关工作到“可核查的价值证据”
- **Core message**: 借鉴具体问题、任务适用性、依赖检查与定位后验证；不是移植奖励权重。
- **Content**: VisionReward：维度拆成问题→支持/反证/缺证题库；UnifiedReward-Flex：按输入细化标准→仅启用query相关视角；DSG：原子问题与依赖图→对象/属性/动作依赖；VTune：定位后验证→Direct之后逐条件核查。下方串起query条件→适用题库→事实+帧引用→支持/反证/未知。五类沿用项目旧方案，未接入论文权重；Q/QV检验提示增量，收益待验证。页面与notes注明四论文来源。

#### Slide 05 - 对照设计
- **Audience move**: 明白Q+V具体增加什么。
- **Relationships**: contrast：两臂差别；membership：五类视角属于同一条件核验。
- **Title**: 价值引导是 Q 与 Q+V 的主要差异
- **Core message**: 加入可操作证据说明，不增加query必要条件。
- **Content**: 保留原Q/QV设计；结果、信息、情绪、动作、感官；补充支持/反证/缺证/禁止推断；五维视图是程序映射，无加权总分；139×2次，零重试；条件尚无独立人工审校。

#### Slide 06 - 8B 完整结果
- **Audience move**: 判断价值引导的现有证据强度。
- **Relationships**: contrast：Q与Q+V召回及误报。
- **Title**: Q+V 多检出 2 个，同时净增 1 个误报
- **Core message**: 计数略有变化，尚无稳定收益。
- **Content**: 两臂各139候选，85代理错误、54正确；TP6/8、FP1/2；precision85.71/80；recall7.06/9.41；IoU为代理，独立语义标签0。净增不代表报警集合包含。
- **Visualization**: recall-bars：保留原0–40%轴及几何。
- **Native-ready**: recall-bars=yes

#### Slide 07 - 工程修复
- **Audience move**: 区分归一化贡献与模型质量。
- **Relationships**: contrast：同口径旧版与新版；order：原始无效→去重恢复→剩余。
- **Title**: 无效输出降至 5 条，去重贡献需单列
- **Core message**: 工程合法性不等于语义正确。
- **Content**: 同验收23→5；本轮52原始无效、47恢复、剩5；2截断JSON、3时间顺序证据不足；组合修复非单因素归因。
- **Visualization**: invalid-bars：保留原计数柱图。
- **Native-ready**: invalid-bars=yes

#### Slide 08 - 8B 输出分布
- **Audience move**: 认识补证与语义审查缺口。
- **Relationships**: membership：四种互斥结果覆盖各139候选。
- **Title**: 超过四成候选仍停留在证据不足
- **Core message**: unknown不能当错误，supported也待语义核验。
- **Content**: Q70/59/7/3，QV63/64/10/2；supported中低IoU41/70、32/63；独立审查未完成。
- **Visualization**: verdict-stacks：保留原统一分母堆叠图。
- **Native-ready**: verdict-stacks=yes

#### Slide 09 - 32B 同样本比较
- **Audience move**: 知道32B已完成且当前配置退化。
- **Relationships**: contrast：同20条37候选，两模型两臂。
- **Title**: 32B 已完成，同样本上更趋于“不判断”
- **Core message**: 32B QV无报警、无支持；零误报不等于更好。
- **Content**: 74/74完成、66合法；表格四行：8BQ支持23/不足11/无效1/TP2FP0/recall8%；8BQV17/16/0/4与0/16%；32BQ0/32/4/1与0/4%；32BQV0/33/4/0与0/0%。每臂37，25代理错12正确；QV精确率未定义。固定前缀非全100；输入一致，运行配置不同。358034token、三卡累计9.83GPUh进入notes。
- **Visualization**: matched-table：四条件×支持、不足、无效、TP/FP、召回。
- **Native-ready**: matched-table=yes

#### Slide 10 - 事实生成退化
- **Audience move**: 区分已复现的传播与待定根因。
- **Relationships**: contrast：两模型同输入；link：无片内事实导致unknown分支。
- **Title**: 32B 的空泛事实会传到后续判断
- **Core message**: 不是前端丢字；提示/schema/运行路径根因未定。
- **Content**: qid2781 Q，[37,41)秒，同16帧；32B原文The required evidence is not available.，片后f0089=44.745s，三条件unknown；8B两条投掷/烟雾描述，引用片内37.237s、39.740s。32B本条stop378token未截断；全74中25非空facts仅固定套话，8B0。CPU复现零片内事实→仅unknown；不能证明为何如此生成。8B描述非独立真值，候选IoU=0；GT56–60、72–98写入notes。

#### Slide 11 - 语义绑定案例
- **Audience move**: 识别来源合法与语义支持的区别。
- **Relationships**: link：文章要求、模型文字/视频事实、支持结论存在疑点。
- **Title**: 引用合法，仍可能跨越语义证据
- **Core message**: 需独立审核事实到结论。
- **Content**: 原qid9572案例完整保留；28–37秒；文章可能含视频，仅响应审阅不能定真错。

#### Slide 12 - 依赖案例
- **Audience move**: 看到不必要unknown的另一来源。
- **Relationships**: contrast：冻结无依赖与模型额外依赖。
- **Title**: 错误的条件依赖会扩散 unknown
- **Core message**: 冻结依赖应与局部事实分开核验。
- **Content**: 原qid10完整保留，独白无音频不能让盆栽条件自动未知；这是响应内部不一致。

#### Slide 13 - 内容与边界
- **Audience move**: 理解为什么检错代理不能替代grounding评价。
- **Relationships**: overlap：包含事件与准确覆盖不同；contrast：语义与时长规则。
- **Title**: 内容匹配与时间边界需要分别验证
- **Core message**: 尚未证明R1或mAP提升。
- **Content**: 保留概念覆盖示意和固定139候选时长规则：recall36.47、precision77.50、FP9；Q7.06/85.71/1，QV9.41/80/2。区间示意无数据轴，仅概念。
- **Visualization**: proxy-tradeoffs：三个方法×召回、精确、误报。
- **Native-ready**: proxy-tradeoffs=yes

#### Slide 14 - 视频审查页面
- **Audience move**: 知道如何直接核查样本。
- **Relationships**: contrast：GT与原Direct播放器；link：片段与响应/引用。
- **Title**: 现在可以直接对照 GT 与 Direct 视频
- **Core message**: 已有审查工具，但尚无独立语义标签。
- **Content**: 完整页面截图；左GT右Direct，每区间可播/切换，保留Q/QV事实/引用和原响应。8B100端口8766、32B20端口8765；两页base同为8BDirect；GT是数据集参照；功能不算模型收益。

#### Slide 15 - 下一步
- **Audience move**: 对齐诊断优先级而非直接扩大运行。
- **Relationships**: order：审查→单变量机制诊断→价值对照→补证/边界；后两步有前提。
- **Title**: 先查事实与证据，再扩展验证闭环
- **Core message**: 分开验证合法性、语义判断和定位质量。
- **Content**: ①用视频审查固定覆盖四类输出并审校条件；②分别检验占位示例与schema，运行配置另列；③事实可用后再比Q/QV；④有缺证证据再做均匀/定向补帧与独立边界验证。不强迫确定判断；新实验先冻结范围与验收，本次未运行。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match SVG names; notes/total.md split after final gate
- **Content**: 中文组会口语，解释分母、代理评价局限、源码/结果来源；P04明确四论文借鉴边界，P09与P10区分事实和假设。
- **Total duration**: 12–15分钟
- **Notes style**: 结论先行，说明证据与限制；不把模型原文当事实真值。
- **Presentation purpose**: 更新既有汇报，提供可审查结果与下一步讨论依据。
