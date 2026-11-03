<!-- ppt-master-schema: design-spec/v1 -->
# ReVALUE 实验进度与结果 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | revalue_progress_20261102 |
| Canvas Format | PPT 16:9, 1280 × 720 |
| Page Count | 12 |
| Primary Language | zh-CN |
| Target Audience | 导师与组会成员，了解 grounding 主线，需要判断当前证据与下一步实验 |
| Communication Intent | 汇报已完成的基线与对照，解释工程进展及科学卡点，并对齐下一步验证任务 |
| Desired Audience Outcome | 能准确区分输出合法性、语义检错和定位质量，理解价值引导尚无稳定收益、32B 暂无预测结果 |
| Core Message / Ask / Action | 输出可靠性已改善；检错召回仍低，价值引导收益未确立，后续需分别验证语义证据与时间边界 |
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

沿用会话中用户已明确委托的“设计细节由你决定，直接完成”。Stage 1 采用 free_design，固定中文、导师组会、16:9 与上述沟通目标；不生成 UI 确认收据。内容快照截至 2026-11-02 23:56，制作日期为 2026-11-03。

Stage 2 三个完整方向：

1. **证据与缺口（选用）**：先给结论，再用基线、对照、修复、案例和失败收据支持，最终收束到验证任务。Mode 为 custom，以 pyramid 为唯一目录基础。Visual style 为 custom，以 swiss-minimal 的开放网格和粗细层级为主体，采用 data-journalism 的数字、来源线与证据旁注；字体为 Microsoft YaHei / Arial，正文 24px，标题加粗同族形成 concord。六色角色为白、浅灰、深蓝、青绿、橙、深灰。备用图像 rendering 为 custom：清晰实线、平面不透明色、少量细规则、无材质深度，情绪如实验室证据图；本次不启用图像资源。
2. **问题演进**：依次讲基线失误、契约修复和仍然存在的未知，最后给定位闭环问题，Mode custom 自定义问题推进。Visual style custom，浅暖白底、深墨色标题、蓝色数据、赭色旁注，以较大留白和左右错落注释组织；标题 SimSun / Cambria，正文 Microsoft YaHei / Arial，24px，形成 contrast。六色为 #FAFAF7、#F0F1EC、#203442、#287E91、#B86C43、#242B30。Rendering custom：细轮廓、轻纸感、浅层标注、审慎而叙事化，如研究手记；不启用图像。
3. **机制拆解**：从输入、条件、证据、结论的链条进入，依次展示各环节的验证状态，以任务图结束，Mode custom 自定义机制解释。Visual style custom，白底、深蓝灰、冷蓝和暗红，强轴线与分支关系，标题 SimHei / Arial、正文 Microsoft YaHei / Arial，24px，形成 contrast。六色为 #FFFFFF、#F2F5F8、#233B53、#346FA1、#A8504B、#202C39。Rendering custom：等重线条、平面示意、明确分层、精确克制，如系统设计审查图；不启用图像。

选用方向 1：当前需要把“工程修复有效”与“方法收益未证实”同时讲清楚，结论先行和可直接比较的数据最适合。页数解析为 12 页，notes 开启，动画与音频关闭，图表和表格按原生可编辑对象导出。

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
| P03 | table | comparison_matrix | 比较自定义 Direct 和 REZE Direct 的三项指标 |
| P05 | chart | horizontal_bar_chart | 共享零起点比较两组错误召回率 |
| P06 | chart | column_chart | 同验收口径旧版和新版的无效输出数 |
| P07 | chart | stacked_bar_chart | 完整 139 候选的四种结果分布 |
| P10 | table | comparison_matrix | 对比 Q、Q+V 与冻结时长规则的代理检错权衡 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Image usage: none。所给报告是统计与响应审查材料；数据、证据链与机制关系直接承载信息。本次不引入视频帧，避免将未经人工核验的响应解释为视觉事实。

## IX. Content Outline

### Part 1: 已完成的实验与当前结论

#### Slide 01 - 当前结论

- **Audience move**: 从零散进展进入“工程改善、检错不足”的共同判断。
- **Relationships**: 输出合法性提高与检错召回不足构成同一阶段的两面；32B 无结果是独立运行状态。
- **Composition**: 左侧主判断，右侧 98.20% 主数字，下方交代时间与任务范围。
- **Title**: 输出更可靠了，检错能力仍然不足
- **Core message**: 输出合法率达 98.20%，价值引导收益尚未确立。
- **Content**: ReVALUE 实验进度与结果；阶段 2026.10.30—11.02，快照截至 11.02 23:56；8B 278/278 完成、32B 0/278 正式请求；主线 grounding。
- **Cover impact**: 绑定钩子为“98.20% 合法输出，仍未通过检错门槛”；用大数字与主判断并置。

#### Slide 02 - 当前 pipeline

- **Audience move**: 理解已测环节及当前方法边界。
- **Relationships**: 视频与 query 输入 Direct，生成候选区间；query 形成条件；候选帧、条件进入 verifier；证据不足尚无补证回路，时间边界尚未验证。
- **Title**: 基线定位区间，verifier 检查内容条件
- **Core message**: 当前完成了局部内容验证，完整 grounding 闭环尚未完成。
- **Content**: REZE Direct 整视频一次输出区间列表；固定 100 query、98 条有效输出、139 区间；候选帧与冻结条件进入 Q/Q+V；事实→引用→条件判断→supported / flagged / insufficient；回看与边界修正为未验证后续。

#### Slide 03 - 固定基线

- **Audience move**: 知道基线选择与指标表现，避免把更换路径当确定提升。
- **Relationships**: 两个 Direct 实现处于对比关系；三个评价指标分别比较。
- **Title**: REZE Direct 已固定，指标尚无一致优势
- **Core message**: 后续冻结 REZE Direct 为参照；当前 verifier 未改写定位输出。
- **Content**: 固定 QVHighlights train 100 开发样本；R1@0.5 自定义 42.00、REZE 39.00；R1@0.7 28.00、30.00；MR mAP 24.72、26.48；帧数、提示、输出形式同时变化，不是单变量；不属于独立测试集。
- **Visualization**: baseline-table：指标 × 两个 Direct 方法的比较表，单位 %。
- **Native-ready**: baseline-table=yes

### Part 2: Q / Q+V 对照与工程修复

#### Slide 04 - 对照设计

- **Audience move**: 明白价值模块实际干预点和控制项。
- **Relationships**: Q 与 Q+V 共享输入和条件；Q+V 在条件核验中加入五类适用价值指导；适用性来源于冻结映射。
- **Title**: 价值引导是 Q 与 Q+V 的主要差异
- **Core message**: 对照评估的是判断指导，不是重新生成候选或修改时间边界。
- **Content**: Q 核查人物、物体、动作和关系；Q+V 加入结果、信息、情绪、动作、感官指导；固定候选、帧/PTS、模型、query 条件、schema 和验收；139×2=278，零重试；条件由助手 query-only 构建、无独立人工审校；not_applicable 不代表漏检。

#### Slide 05 - 主结果

- **Audience move**: 看到少量新增检出及伴随误报，理解结论仍弱。
- **Relationships**: Q 与 Q+V 在召回和报警结果上对比；低 IoU 是错误代理。
- **Title**: Q+V 多检出 2 个，同时净增 1 个误报
- **Core message**: 召回由 7.06% 到 9.41%，尚不足以建立稳定价值收益。
- **Content**: 两组每组 139 候选，85 个低 IoU 代理错误、54 个代理正确；Q TP6/FP1、precision85.71%；QV TP8/FP2、precision80.00%；低 IoU 不必然是内容错误，尚无独立人工语义标签；两组均未通过原探索性门槛。
- **Visualization**: recall-bars：共享 0–40% 轴的两条水平召回率，Q7.06、QV9.41；配报警计数和精确率文字。
- **Native-ready**: recall-bars=yes

#### Slide 06 - 工程修复

- **Audience move**: 区分验收恢复、生成改善与科学收益。
- **Relationships**: 旧版与新版同验收规则下比较；本轮原始严格输出经去重后部分恢复；剩余失败分为两个类别。
- **Title**: 无效输出降至 5 条，去重贡献需单列
- **Core message**: 合法性改善是工程成果，不能等同于语义判断提高。
- **Content**: 旧 v2.2 与新 v2.4 同验收口径 23→5；新一轮严格原始无效52，普通重复引用去重恢复47，剩5；2 条长度上限/JSON不完整、3 条有序事实不足；引用绑定、依赖检查、生成顺序和去重共同变化，非单因素归因。
- **Visualization**: invalid-bars：旧版23、新版5的计数柱图，共278响应；去重恢复47用独立流程文字解释。
- **Native-ready**: invalid-bars=yes

#### Slide 07 - 结果分布

- **Audience move**: 看见证据不足与保守接受仍是主要缺口。
- **Relationships**: 每组139候选由 supported、insufficient、flagged、invalid 四类组成；各类互斥且覆盖完整分母。
- **Title**: 超过四成候选仍停留在证据不足
- **Core message**: 当前没有补证闭环，unknown 不能直接转为错误。
- **Content**: Q supported70、insufficient59、flagged7、invalid3；QV63、64、10、2；insufficient比例42.45%和46.04%；supported中仍有低IoU41/70、32/63，但不能全部认定语义漏检；边界差异和标注争议需另核验。
- **Visualization**: verdict-stacks：2 条完整139候选堆叠柱图，保留各类别实际计数和统一类别顺序。
- **Native-ready**: verdict-stacks=yes

### Part 3: 为什么还没有解决 grounding

#### Slide 08 - 语义绑定案例

- **Audience move**: 理解合法引用仍可能不支持 query 语义。
- **Relationships**: query 要求文章；响应描述可读文字和带字幕视频；这些事实被用于支持文章条件，支持关系存疑。
- **Title**: 引用合法，仍可能跨越语义证据
- **Core message**: 事实到结论的支持关系需要独立检查。
- **Content**: qid9572，候选28–37秒；query“男子横持手机阅读文章”；模型描述可读文字、带字幕视频→支持文章；证据语义跳跃嫌疑，文章可能包含视频，因此仅凭响应不能判真实定位错误；属于助手响应审查，非独立人工核验。
- **Composition**: 条件、模型事实、结论沿证据链展开，旁注标出支持关系存疑。

#### Slide 09 - 依赖条件案例

- **Audience move**: 理解 unknown 可来自响应内部依赖错误。
- **Relationships**: 独白条件因无音频未知；盆栽条件在冻结合同中无依赖，却被响应绑定到独白；这种额外依赖传播 unknown。
- **Title**: 错误的条件依赖会扩散 unknown
- **Core message**: 局部事实应独立核验，依赖按冻结合同传播。
- **Content**: qid10，候选0–150秒，query“女子在盆栽旁独白”；r1独白无音频 unknown；r3是否在盆里 depends_on=[]；模型仍称依赖独白而unknown，自己的事实多次提到盆栽；可复现响应内不一致，非人工视觉确认；程序传播依赖为待验证修复建议。
- **Composition**: 并列展示合同依赖和响应推断，突出多出的依赖。

#### Slide 10 - 内容与时间边界

- **Audience move**: 理解低IoU代理与语义验证目标不完全一致。
- **Relationships**: 区间包含目标内容与区间准确覆盖是两个判断；Q/QV与时长规则对同一代理错误集提供不同权衡。
- **Title**: 内容匹配与时间边界需要分别验证
- **Core message**: 一个过长区间可以包含事件，但仍然定位不准。
- **Content**: 概念区间示意只解释覆盖关系、无数值坐标；Q recall7.06 precision85.71 FP1；QV9.41 80.00 FP2；冻结时长规则36.47 77.50 FP9；均为139候选IoU代理口径；规则善于发现过长区间但误报高，不能替代语义检验；当前未改写区间，未证明R1或mAP提高。
- **Visualization**: proxy-tradeoffs：三个方法 × recall、precision、FP 的比较表；无新规则阈值。
- **Native-ready**: proxy-tradeoffs=yes

### Part 4: 运行状态与下一步

#### Slide 11 - 32B 首次启动

- **Audience move**: 修正“仍在排队”的旧印象，知道实际阻断与结果空缺。
- **Relationships**: 权重与CPU准备完成，首次启动随后出现进程归属和显存准入两类错误；失败阻断正式请求和评价。
- **Title**: 32B 首次启动失败，尚无预测结果
- **Core message**: 不能比较8B与32B能力，先排查运行阻断。
- **Content**: 14/14权重校验，145CPU检查，278输入一致；11.02 22:59 GPU0/2/3 首次启动；归属检查拒绝清理，触发机制未定位；vLLM要求空闲22.34GiB、实际22.31GiB；1worker、正式请求0/278、token0；4500GPU秒为保守预留，完整生命周期未知；23:56已知PID/组未发现残留，历史未确认收据保留、无重试。

#### Slide 12 - 下一步验证任务

- **Audience move**: 对齐下一步的顺序和可审查完成标准。
- **Relationships**: 运行修复提供32B比较前提；语义审校提供诊断依据；等预算补证对照与独立边界验证分别回应证据和时间问题。
- **Title**: 下一步要证明：能发现什么错，怎样补证
- **Core message**: 优先检验语义支持、证据补足和时间边界，避免把格式改善当定位收益。
- **Content**: 先定位32B两类启动失败并版本化审查；审校query条件与依赖、独立覆盖四类输出；补证比较旧帧/等量均匀新帧/等量定向新帧；单独验证边界，若改写区间再报告R1和mAP；上述为建议，新增实验需冻结范围预算；所有已有失败与预测保留。
- **Closing impact**: 绑定结论为“把合法性、语义检错、定位质量分别验证”；以三个明确检验对象与各自验收标准收束。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under `notes/`
- **Content**: 仅依据给定报告与最终可见页面，补足分母、方法差异、代理评价的局限、工程验收与真实语义质量的区别。不得给无证据案例新增视觉事实；原文件路径和成本细节可放入 notes。
- **Total duration**: 10–12 分钟
- **Notes style**: 中文组会口语，先解释判断，再交代依据与限制，短段落。
- **Presentation purpose**: 汇报已完成工作、解释卡点、对齐后续可审查实验。
