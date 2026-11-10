<!-- ppt-master-schema: design-spec/v1 -->
# ReVALUE Weekly Highlight Research - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | revalue_weekly_highlight_20261110 |
| Canvas Format | ppt169, 1280×720 |
| Page Count | 10 |
| Primary Language | zh-CN |
| Target Audience | 导师与研究组，关注方法贡献、实验依据与下一步取舍 |
| Communication Intent | 汇报本周实验，解释均值提升与负结果，明确待验证机制及推进顺序 |
| Desired Audience Outcome | 区分记忆与评分两条路线、全50与后40两个范围，理解五维价值的收益仍不稳定 |
| Core Message / Ask / Action | 先核对事实与关键贡献，再检验按需补证；当前不能把五维价值写成稳定有效的贡献 |
| Delivery Context | 中文组会现场8–10分钟，随后通过讲稿复查 |
| Artifact Afterlife | 可编辑PPTX、逐页讲稿、来源归档与重复导出 |
| Reading Mode | balanced |
| Content Strategy | 基于已批准两段汇报重组；事实、样本范围和结论强度遵循冻结报告 |
| Design Style | evidence-first；海军蓝与青绿的克制学术数据汇报 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — delegated Stage-2 proactive policy |
| Custom Animations | disabled — delegated Stage-2 proactive policy |
| Narration Audio | disabled — delegated Stage-2 proactive policy |
| Created Date | 2026-11-10 |

Confirmation provenance: 用户已明确“按推荐目标，设计细节由你决定，直接完成（推荐）”；本轮要求依刚完成的组会汇报制作PPT。采用委托决策，不创建UI确认回执。设计深度brief。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280×720 |
| viewBox | `0 0 1280 720` |
| Margins | 左右64px，主要信息距上下边缘48px |
| Content Area | x=64..1216, y=164..650；来源与页码位于底部 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: pyramid
- **Mode Behavior**: 从当前结论进入两条工作路线，依次给出对照、反例与改进，再以有边界的验证计划结束；每页标题明确该页判断，配对差值与范围紧邻指标。
- **Visual style**: custom
- **Visual Style References**: swiss-minimal
- **Visual Style Behavior**: 使用清晰栅格、少量大面积分区、锐利边缘与留白；数据、细规则和方向连接承担结构，避免逐条重复包卡。相同语义用一致颜色，正文保持可投影字号。
- **Theme**: 从可观察事实到关键贡献的三段证据路径作为跨页主题；每页只突出一个主判断。
- **Tone**: 专业、审慎、直接。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 主页面 |
| Secondary background | #F1F5F7 | 次级证据区域 |
| Primary | #19344E | 标题、结构、深色封面 |
| Accent | #207F89 | 当前方法与主要结果 |
| Secondary accent | #C76B2C | 价值规则、待验证事项 |
| Body text | #263D50 | 正文 |
| Secondary text | #607586 | 注释与来源 |
| Divider | #D6E1E8 | 分隔规则 |
| Grid | #E7EDF1 | 图表网格 |
| Negative | #B34D4D | 失败或负向变化 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 清晰无衬线、字重形成层级 | Microsoft YaHei | Arial | sans-serif |
| Body | 与标题同族，便于研究数据阅读 | Microsoft YaHei | Arial | sans-serif |

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
| Kicker | 16 |
| Data | 24 |
| Display | 72 |
| Hero | 52 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 结论标题 → 主要证据 → 解释／范围 → 来源。
- **Composition tendency**: 对照图表、两条分支和单条判断链交替；案例页采用平行证据，结束页降低密度。
- **Cross-page continuity**: 事实→贡献→优先级的三个阶段逐步出现；页脚统一编号，图表内方法名称一致。
- **Spacing posture**: 封面与结尾留白较大，数据页有密度但保持清晰阅读路径。
- **Spacing anchors**: page margin64；block gap24；column gutter40；corner radius0；body leading34，单位px。

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | chart | horizontal_bar_chart | 记忆和核验两组各自同范围对照 |
| P05 | chart | horizontal_bar_chart | 相同50视频的窗口评分系统比较 |
| P07 | table | metric_table | 最新40视频的Top-5、mAP15和mAP50 |
| P08 | table | comparison_matrix | 跨数据集样本范围、指标与结果 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

无图片任务。数字对照与原报告中的案例记录承担证据，不要求观众辨认现实主体，故本次使用可编辑数据和事实文字。

## IX. Content Outline

### Part 1: 本周工作与验证边界

#### Slide 01 - 从有价值到值得优先保留

- **Audience move**: 了解主题 → 明确本周研究张力与结论强度。
- **Relationships**: 事实观察、观看贡献、优先选择依次递进；初步改善与稳定收益的判断不同。
- **Composition**: 大标题与简洁阶段路径，低密度封面。
- **Title**: 从“有价值”到“值得优先保留”
- **Core message**: 五维价值评分出现初步均值提升，稳定收益仍待验证。
- **Content**:
  - ReVALUE高光检测组会汇报；林逸飞；2026.11.03组会后至11.10。
  - 两条实验路线：事实／价值记忆与候选核验；借鉴REZE的通用窗口评分。
- **Cover impact**: binding hook为“从有价值到值得优先保留”；推荐以三段证据路径组织封面。
- **Fact IDs**: F001, F003, F004

#### Slide 02 - 本周验证了价值加入的两个位置

- **Audience move**: 把所有实验当作一个方法 → 能区分记忆选片路线与密集评分路线。
- **Relationships**: 路线A按全片观察、F/FV记忆、候选选择、核验排列；路线B按局部窗口、背景与价值标准、概率评分、全片曲线排列；两条路线为对照而非先后依赖。
- **Composition**: 两条横向工作路线，下方标出已测与待验收边界。
- **Title**: 本周验证了价值加入的两个位置
- **Core message**: 记忆辅助选片与通用窗口评分分别检验，不能混成同一消融。
- **Content**:
  - A：全片采样 → 事实F／附加价值FV → 候选选择 → 普通C／详细V15核验。
  - B：3秒局部窗口 → 全片背景＋五维标准 → Yes/No概率 → 2秒完整分数。
  - 已完成：静态建库、读取、核验、评分；待验证：缺证触发、定向补看、记忆更新和边界修正。
- **Fact IDs**: F001, F002, F011, F012

#### Slide 03 - 事实改进缩小差距，详细核验未超过普通核验

- **Audience move**: 看到模块已实现 → 判断模块是否有实际额外收益。
- **Relationships**: 同一固定40视频内比较D与F/F-local/FV-local；F-local之后比较C、旧V15与修复V15。两组对照独立解读。
- **Composition**: 并列两组证据与一行结论。
- **Title**: 事实改进后均值上升，价值增益仍未确认
- **Core message**: 事实保真和时间绑定值得保留；详细五维核验未超过简单核验。
- **Content**:
  - 记忆40：D58.48；旧F54.48；F-local57.58；FV-local56.34，均为Top-5 mAP百分数。
  - 核验40／200对：F-local57.58；C58.46；旧V15 58.41；修复V15 57.65。
  - 修复V15合法135/200，仅4次接受替换；普通C合法200/200、29次替换。
  - 配对区间均跨0；D与记忆组的视觉输入组织不同，不作等token纯记忆因果结论。
- **Visualization**: memory-bars=记忆系统横条；verifier-bars=核验系统横条。
- **Native-ready**: memory-bars=yes; verifier-bars=yes
- **Fact IDs**: F001, F002

### Part 2: 通用高光评分与失败诊断

#### Slide 04 - 用具体价值标准生成完整时间轴分数

- **Audience move**: 只知道借鉴REZE → 理解评分器的输入、判断和输出。
- **Relationships**: 旧全片采样生成背景；背景与当前3秒窗口共同输入评分；结果、信息、情绪、动作、视觉五类为可选支持路径；窗口概率按原映射生成2秒全片曲线。
- **Composition**: 主流程与背景支路；五类规则在同一判断节点汇合。
- **Title**: 用背景与具体价值标准生成全片分数
- **Core message**: 延续REZE的逐窗口概率读数，改变任务目标和价值判据。
- **Content**:
  - 3秒窗口，2fps，完整窗口6帧；同一视频复用一份稀疏背景。
  - 五类：结果、信息、情绪、动作、视觉；一个充分的关键贡献路径即可成立。
  - 输出1个Yes/No token；以概率读数排序，按原规则映射至2秒网格。
  - 并非五路数值加权；单token不能回溯模型究竟采用哪条规则；本轮没有动态回看。
- **Fact IDs**: F003, F004, F011

#### Slide 05 - 全50条得到小幅均值提升

- **Audience move**: 看到旧10条提升 → 使用相同50视频的系统结果判断收益。
- **Relationships**: 相同50视频、背景版本和修订版本比较；8B与27B为系统比较，27B缺少同模型REZE对照。
- **Composition**: 主要横条数据与配对差值侧注。
- **Title**: 全50条有小幅均值提升，稳定性仍不足
- **Core message**: 上一修订版8B55.96、27B56.26，REZE8B54.89，不能宣布稳定超越。
- **Content**:
  - Top-5 mAP：REZE8B54.89；背景8B53.53；修订8B55.96；背景27B55.54；修订27B56.26。
  - 修订8B−REZE：+1.06pp，配对95%区间[−3.74,+5.74]。
  - 修订27B−修订8B：+0.31pp，区间[−4.79,+5.46]；没有27B REZE条件。
  - 这是已用开发样本全50；最新关键贡献版只完成后40，不合并成同版本全50。
- **Visualization**: full50-bars=五个完整系统条件的Top-5 mAP横条。
- **Native-ready**: full50-bars=yes
- **Fact IDs**: F003, F012

#### Slide 06 - 失败案例暴露观看理由与优先级的差距

- **Audience move**: 把AP下降当成抽象指标 → 能说出被高估和被遗漏的具体内容。
- **Relationships**: 两个旧修订版低AP案例各自比较高排名内容与高人工评分但低排名的内容；这为支持性诊断，非规则内部因果证据。
- **Composition**: 两份并列案例记录，排名与人工评分形成对照。
- **Title**: “有观看理由”还不能保证选中关键片段
- **Core message**: 主体出现或文字有信息，仍可能挤掉关键行为和操作。
- **Content**:
  - Obie：主体展示排第1，人工1.45/5；96–98秒行走人工3.80/5，却排第59。
  - 洗耳：文字页占前4；78–80秒操作人工3.90/5，排第11。
  - 原单token输出不含规则解释，不能认定某一价值项是实际原因；重复占位只是部分解释。
- **Fact IDs**: F006

#### Slide 07 - 最新目标收紧后40条有所改善

- **Audience move**: 理解旧目标偏宽 → 检查修订是否带来完整范围改善。
- **Relationships**: 相同后40视频的三个系统对照；Top-5与补充mAP15/50为不同指标；新条件同时改变关键贡献目标与品牌/场景门槛。
- **Composition**: 指标表与突出差值，配对区间紧邻提升。
- **Title**: 收紧关键贡献目标，后40条均值上升
- **Core message**: 最新8B55.80高于REZE53.29，但+2.51pp的配对区间仍跨0。
- **Content**:
  - 三组Top-5：REZE53.2858、上一修订53.5694、关键贡献55.8007；mAP15分别34.0896、34.4441、35.1199；mAP50为68.3999、69.2434、70.4936。
  - 相对REZE +2.51pp；95%区间[−2.74,+7.69]；相对上一修订+2.23pp，区间[−0.68,+5.36]。
  - 区间针对差值；包含0表示现有样本仍不能确认稳定提升，不表示mAP等于0。
  - 两项联合改动，不能归因单个维度；mAP15/50沿用TVSum2秒补充协议。
- **Visualization**: core40-metrics=三方法三指标的指标表。
- **Native-ready**: core40-metrics=yes
- **Fact IDs**: F004, F005

### Part 3: 迁移、主要问题与下一步

#### Slide 08 - 跨数据集尚无一致收益

- **Audience move**: 只看TVSum均值 → 认识迁移证据与范围限制。
- **Relationships**: QFVS40query、Mr.HiSum40记忆、Mr.HiSum10评分、SVHighlights14场是四项独立对照，指标不可横向比较。
- **Composition**: 按范围、指标、同组结果、限制组织一张比较表。
- **Title**: 跨数据集测试尚未得到一致收益
- **Core message**: 记忆与最新评分在外部开发子集上的效果仍不稳定。
- **Content**:
  - QFVS4视频40query：Oracle F1 D43.77、F-read43.52；Uniform47.72但覆盖条件不同。
  - Mr.HiSum40记忆：mAP50 D59.60、F-read59.10。
  - Mr.HiSum10最新评分：mAP50 REZE63.87、新版62.14；摘要F1提升不能代替mAP改善。
  - SVHighlights14场27B：HL-mAP B0 15.32、F+C15.45，每场仅64全局时刻。
  - 均非相应数据集官方全量或独立未见测试。
- **Visualization**: cross-dataset=范围、指标、结果与限制的比较表。
- **Native-ready**: cross-dataset=yes
- **Fact IDs**: F007, F008, F009, F010

#### Slide 09 - 判断链的三个环节需要分别验证

- **Audience move**: 认为增加规则即可解决 → 把事实、贡献和优先级作为不同故障位置。
- **Relationships**: 可观察事实先支持观看贡献，再支持全片优先级；当前单token把后两者压缩成一次输出，记忆读取与输出契约也会影响证据传递。
- **Composition**: 一条主要证据链，上下附已解决与未解决事项。
- **Title**: 事实、观看贡献和优先级需要分别核验
- **Core message**: 规则更具体仍需要可靠事实和相对贡献证据。
- **Content**:
  - 已推进：事实读取、时间绑定、局部证据保留与部分输出一致性。
  - 仍有问题：单词概率充当重要性分数；稀疏背景不能充分判断全片关键与重复；详细V15合法率与相对判断不足。
  - 未来检查记录须区分事实误读、目标偏宽和真正缺证；补充解释不是原评分的内部理由。
- **Fact IDs**: F001, F002, F006, F011

#### Slide 10 - 先统一验证，再按证据缺口补看

- **Audience move**: 看到多个方向 → 接受近期有顺序的推进计划与边界。
- **Relationships**: 同版本验证先于案例分类，分类先于定向补证；五维作为具体检查问题服务这些环节。
- **Composition**: 三个优先事项与单一结束判断。
- **Title**: 先把判断做对，再验证回看是否有用
- **Core message**: 收尾统一版本，定位失败机制，再决定是否增加新观察。
- **Content**:
  - 01 统一版本：补齐最新方案缺少10条；旧10＋新40仅可作为混合版本诊断，尚未完成该汇总。
  - 02 核对判断：固定案例清单，区分可见事实、主线贡献与相对优先级；保留提升和退步。
  - 03 按需补证：只有明确缺少动作、反应或语音信息时，再设计回看／ASR的单变量对照。
  - 状态：最新补齐因GPU资源竞争启动失败；本PPT整理不启动任何新实验。完整Agent闭环待验证。
- **Closing impact**: binding takeaway为“先把判断做对，再验证回看是否有用”；推荐降低信息密度，使推进顺序明确。
- **Fact IDs**: F006, F012

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under notes/
- **Content**: 逐页说明图表、范围、版本与结论强度；包含本地来源文件。基于最终SVG编写，不声称新增实验或回溯内部推理。
- **Total duration**: 8–10分钟
- **Notes style**: 中文组会口语，结论先行，解释必要术语。
- **Presentation purpose**: 汇报已完成工作、明确主要卡点并讨论下一步验证顺序。
