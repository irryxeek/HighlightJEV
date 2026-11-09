<!-- ppt-master-schema: design-spec/v1 -->
# ReVALUE Weekly Meeting Revision - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | revalue_weekly_meeting_revision_20261110 |
| Canvas Format | ppt169 — 1280 × 720 |
| Page Count | 16 |
| Primary Language | zh-CN |
| Target Audience | 导师和研究组成员，了解 ReVALUE 主线，需要判断证据与下一步优先级 |
| Communication Intent | 对照11月3日纪要汇报完成情况，解释记忆和价值核验的效果及失败，再讨论后续实验取舍 |
| Desired Audience Outcome | 理解已修复问题和未验证贡献，区分比较错误与缺证，同意优先级或提出具体调整 |
| Core Message / Ask / Action | 事实记忆更可用但尚未超过Direct；详细价值未超过普通核验；先修复证据链，再小规模验证按需价值和补证 |
| Delivery Context | 约12分钟中文组会讲解，兼顾会后阅读；统计期为11月3日组会后至11月9日 |
| Artifact Afterlife | 可编辑PPTX、逐页讲稿、完整数据与来源供会后核查 |
| Reading Mode | balanced |
| Content Strategy | balanced，按研究问题重组修订稿，事实与结论边界完整保留 |
| Design Style | 证据优先：出版式标题、数据主导、病例联系表、局限旁注 |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — final Stage-2 proactive policy |
| Custom Animations | disabled — final Stage-2 proactive policy |
| Narration Audio | disabled — final Stage-2 proactive policy |
| Created Date | 2026-11-10 |

Delegation: 用户在本会话已明确“设计细节由你决定，直接完成”；本次沿用该授权。Stage 1为中文导师组会、16:9、14–18页、free_design。Stage 2选择16页，图表和表格可编辑，备注开启，动画和配音关闭，无确认UI收据。

Direction alternatives: A证据优先（selected）：先结论，再数据，再案例，再决定；白底深蓝、衬线标题与无衬线正文，真实帧作为证据。B机制拆解：按观察—事实—价值—结论逐步解释，暖白色、文字与细线机制图为主，衬线和无衬线对比，渲染候选为无纹理平面信息插图。C进度看板：按已完成／待验证／进行中分组，深色底、同一无衬线字体、状态数字和横向进度，渲染候选为平面界面示意。A的证据对照最符合本次决定需求；B、C为未选设计。三者mode/visual_style/rendering均为custom；A基于pyramid、data-journalism、corporate-photo；B和C为独立行为方案，无目录引用。A rendering候选为保留自然纹理、真实景深与原有光照的纪实画面；不生成替代案例图。本次image_usage仅provided。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 56 px左右；42 px上下 |
| Content Area | x56–1224，y42–660，页脚位于底部安全区 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: pyramid
- **Mode Behavior**: 先给当前判断，围绕记忆收益和价值额外收益分组展示对照，再以具体错误解释限制，最后落到待讨论决定。
- **Visual style**: custom
- **Visual Style References**: data-journalism
- **Visual Style Behavior**: 以图表为页面主轴，衬线判断标题配无衬线精确数据，细分隔线和侧注组织证据；真实联系表与短证据链相邻，稀疏使用色块强调结论和待验证状态。
- **Theme**: 研究证据与缺口的对照；深蓝标题、青色事实改进、橙色价值条件、红色风险，跨页使用来源线与章节标签维持身份。
- **Tone**: 专业、坦率，完整保留负结果和开发集限制。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 正文页背景 |
| Secondary background | #F2F5F7 | 旁注和事实区 |
| Primary | #17324D | 标题与主判断 |
| Accent | #C56B2C | 价值条件、重点待检验项 |
| Secondary accent | #237F89 | 事实记忆与工程改进 |
| Body text | #243746 | 正文 |
| Secondary text | #52677A | 辅助说明与来源 |
| Divider | #CCD7E0 | 分隔规则 |
| Surface | #F7F9FB | 表格隔行 |
| Grid | #E2E8EE | 图表网格 |
| Negative | #B94444 | 无效、负向点差 |
| Neutral data | #64798B | 对照组 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 出版式衬线，结论句 | SimSun | Arial | serif |
| Body | 中性无衬线，清晰可读 | Microsoft YaHei | Arial | sans-serif |
| Display | 对齐数字与主数据 | Arial | Arial | sans-serif |
| Cover | 与判断标题保持衬线身份 | SimSun | Arial | serif |

- **Title stack**: SimSun, Arial
- **Body stack**: Microsoft YaHei, Arial
- **Display stack**: Arial
- **Cover stack**: SimSun, Arial
- **Role rationale**: Display为多页主数字与数据对齐；Cover保持封面与标题的衬线身份；其他支持角色继承Body。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 46 |
| Subtitle | 30 |
| Lead | 28 |
| Annotation | 18 |
| Footnote | 14 |
| Label | 20 |
| Data | 22 |
| Display | 72 |
| Cover | 64 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 判断标题→图表或证据→结论边界→来源。
- **Composition tendency**: 数值页优先横向读数与侧注，机制页用关系承载结构，案例页完整联系表配独立证据说明。
- **Cross-page continuity**: 小节编号、颜色语义和来源线复用；主结论在封面与结尾呼应。
- **Spacing posture**: 数据页适度密集，结论和下一步页留白，案例页优先证据可辨识度。
- **Spacing anchors**: page margin=56；block gap=24；column gutter=32；corner radius=0；body leading=36。

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P03 | table | comparison_matrix | 对照会议安排、完成工作与当前状态 |
| P06 | chart | grouped_bar_chart | 旧10与新增40的B0/F/FV比较 |
| P07 | chart | horizontal_bar_chart | 同40视频各阶段系统mAP |
| P09 | chart | horizontal_bar_chart | 普通核验与V15的最终mAP |
| P10 | chart | stacked_bar_chart | 固定200对的完整判定分布 |
| P13 | table | metric_table | 三个迁移数据集的读数与边界 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| z_6gVvQb2d0__pair01.jpg | 1920 × 1608 | 1.194 | 警车与挥手候选的真实输入证据 | Evidence | 完整联系表与模型矛盾说明相邻 | no-crop | user | Existing | 已冻结缓存帧；保留所有时间标签及A/B上下文 | embedded | local |
| WxtbjNsCQ8A__pair02.jpg | 1920 × 1216 | 1.579 | 开蜂箱与展示巢框的上下文引用案例 | Evidence | 完整联系表配时间范围与比较依据说明 | no-crop | user | Existing | 已冻结缓存帧；前后过程不等于双方比较 | embedded | local |

## IX. Content Outline

### Part 1: 回应会议问题

#### Slide 01 - 本周进展
- **Audience move**: 从上周待办转到本周应检验的核心问题。
- **Relationships**: 记忆和价值判断共同服务高光选择；观察补证为待验证后续。
- **Title**: 记忆更可用，价值增益仍待验证
- **Core message**: ReVALUE本周围绕上次纪要完成对照和诊断，尚未确认稳定方法收益。
- **Content**: 汇报期11.03–11.09；林逸飞；11.10会议对照修订版；事实→判断→补证。
- **Cover impact**: hook=记忆更可用，价值增益仍待验证；以可编辑大标题和证据链建立当前判断。

#### Slide 02 - 本周判断
- **Audience move**: 理解工程改善与有效方法贡献之间的差距。
- **Relationships**: F-local与D为系统参照；C与V15检验详细价值的额外作用。
- **Title**: 已有局部改善，还没有稳定超越基线
- **Core message**: 记忆更接近D，详细价值未超过普通核验。
- **Content**: F-local57.58与D58.48；C58.46、旧V15 58.41、修复V15 57.65；均为固定40开发视频；建议优先事实核验，价值按需。

#### Slide 03 - 会议对照
- **Audience move**: 看清纪要中哪些已推进、哪些仍未解决。
- **Relationships**: 六项会议要求对应本周工作及各自未完成部分。
- **Title**: 纪要中的主要对照已开展，补证仍未落地
- **Core message**: 第一阶段推进有据，事件图和Agent闭环仍不完整。
- **Content**: 高光价值→五维15题；memory→F/FV对照；扩数据→50/40/7；比较→200对；模型→27B74/74合法；工具→ASR和定向回看待验证。
- **Visualization**: meeting-progress：三列六行会议对照表。
- **Native-ready**: meeting-progress=yes

#### Slide 04 - 模块位置
- **Audience move**: 区分选片前价值记忆和选片后详细核验。
- **Relationships**: 采样观察先生成F；V引用F；F与FV分别作为选片输入；另一对照在F-local选片后使用C或V15；回看更新是后续而非已运行步骤。
- **Title**: 本周测试了两个加入价值的位置
- **Core message**: 价值记忆与价值核验是两套独立对照，不是完整Agent闭环。
- **Content**: 选片前：观察→F→可选V→结合帧选片；选片后：F-local Top-5→C或V15→受控替换；未验证：缺证→定向补看→更新。

#### Slide 05 - 五维设计
- **Audience move**: 理解五维如何转成证据问题，而非固定总分。
- **Relationships**: 结果、信息、情绪、动作、视觉事件属于价值视角；每维的问题按观察、贡献、相对优先递进。
- **Title**: 五维被拆成15题，但题目多不等于证据足
- **Core message**: 看见事件、值得观看、比另一段更好，是三个不同命题。
- **Content**: 五个视角；观察→贡献→相对优先；允许支持、反证、未知、不适用；价值引用事实与比较对象；当前未按yes数量加权。

### Part 2: 结果与失败机制

#### Slide 06 - 初版扩展
- **Audience move**: 从旧10条正结果转到完整扩展证据。
- **Relationships**: 旧val10与新增40是不同开发范围；每范围比较B0、F、FV。
- **Title**: 旧10条的价值收益，没有延续到新增40条
- **Core message**: 新增40 FV−F为−1.97pp，配对区间跨0。
- **Content**: 旧10 61.3167/59.7625/62.9247；新增40 53.2858/52.6220/50.6473；CI[−5.5885,+1.1280]；全50 FV53.1028；非独立官方test50。
- **Visualization**: cohort-comparison：B0/F/FV分组柱形比较，纵轴0–80。
- **Native-ready**: cohort-comparison=yes

#### Slide 07 - 记忆改进
- **Audience move**: 识别读取和事实改进的收益及与D的剩余差距。
- **Relationships**: 同40条的D、F、FV、FV-read、F-local、FV-local为系统条件对照。
- **Title**: 事实改进缩小差距，仍未超过密集视觉Direct
- **Core message**: F54.48→F-local57.58；D58.48；FV-local56.34。
- **Content**: 58.4767/54.4796/53.2167/55.3426/57.5828/56.3439；F-local−D−0.8939pp；FV-local−F-local−1.2389pp；区间跨0；非等token纯结构消融。
- **Visualization**: memory-comparison：横条mAP六条件，0–70共同基线。
- **Native-ready**: memory-comparison=yes

#### Slide 08 - 已修问题
- **Audience move**: 理解读取修复与语义可靠性是不同验收项。
- **Relationships**: 已生成400条中读入173条，155条读入记录属于结果或信息；全局不足与局部可见证据可同时成立。
- **Title**: 修好了部分读取和证据保留，真实性仍需检查
- **Core message**: 生成、读到、引用合法与真实正确逐级不同。
- **Content**: 400生成、173读入、155集中两维；调整装入顺序；全局不足保留蓝衣/栏杆等局部事实；8对最终全不足；完整事件图未实现。

#### Slide 09 - 后置核验效果
- **Audience move**: 判断详细价值是否比普通核验提供额外收益。
- **Relationships**: 固定F-local与三种后置核验在同40条完整分母比较；普通C也判断观看贡献。
- **Title**: 详细价值核验未超过普通核验
- **Core message**: C58.46、旧V1558.41、修复V1557.65，均未确认稳定增益。
- **Content**: F57.5828/C58.4573/旧V58.4085/修复V57.6496；C−F+.8745 CI[−.1929,+2.2367]；失败和弃判保留F；新增500复用100。
- **Visualization**: verifier-map：四臂横向mAP，0–70共同基线。
- **Native-ready**: verifier-map=yes

#### Slide 10 - 判定分布
- **Audience move**: 从全tie概括转为完整输出质量诊断。
- **Relationships**: 每臂200对由明确A/B、tie、不足、不可比、无效五种互斥状态组成。
- **Title**: 现在的瓶颈还包括无效输出与比较资格
- **Core message**: 普通C明确116/200，修复V仅26/200且65条无效。
- **Content**: C[116,31,23,30,0]；旧V[63,31,7,43,56]；修复V[26,49,1,59,65]；接受替换29/12/4；新接口不等于旧四态根因已解决。
- **Visualization**: verdict-distribution：三臂200总量的水平堆积条。
- **Native-ready**: verdict-distribution=yes

#### Slide 11 - 引用矛盾案例
- **Audience move**: 看懂已复现的实现矛盾与尚未确认的偏好。
- **Relationships**: A警车经过与B人员挥手为比较对象；B胜出引用B.I3，而该题是未知。
- **Title**: 案例一：选了B，却引用“证据不足”的答案
- **Core message**: 逐题状态与最终胜负的联合约束遗漏。
- **Content**: A80–82s、B226–228s；最终B；support=B.I3；该题u且B五个比较问均u；不据此判断哪段真实更好；助手审阅非人工真值。
- **Images**: z_6gVvQb2d0__pair01.jpg完整展示来源、时间和候选上下文。

#### Slide 12 - 比较依据案例
- **Audience move**: 区分自身时间上下文与双方价值比较证据。
- **Relationships**: A66–68s开蜂箱，B118–120s展示巢框；A之后68.97s上下文不属于B。
- **Title**: 案例二：自身前后过程不能单独证明A胜B
- **Core message**: 时间关联、动作完成和相对观看价值须分开核验。
- **Content**: 新版选A；引用68.97s的A后文；没有绑定B片内画面；原50对局部前提违规8/4→0；22条最终无效仍过JSON；不是输出截断。
- **Images**: WxtbjNsCQ8A__pair02.jpg完整联系表作为上下文位置证据。

### Part 3: 迁移与下一步

#### Slide 13 - 跨数据集
- **Audience move**: 识别迁移完成范围、读数及不能混同的评价目标。
- **Relationships**: 三数据集按任务和评价分别报告，不能合并平均或认定同一原因。
- **Title**: 跨数据集尚无一致收益，任务瓶颈不同
- **Core message**: QFVS看覆盖，Mr.HiSum看选片传递，SV看稀疏观察与失败。
- **Content**: QFVS4视频40query F1 D43.77/Fread43.52/Uniform47.72；MrHiSum40视频mAP15 D24.40/Fread22.91，60/190建议不入摘要；SV7 mAP B016.27/F16.33/C16.38；均非全量。
- **Visualization**: transfer-results：数据集、范围、读数、边界四列表。
- **Native-ready**: transfer-results=yes

#### Slide 14 - 长视频状态
- **Audience move**: 区分七场完成结果与十四场待完成扩测。
- **Relationships**: 七场8B已完成；十四场27B为独立扩展，复用旧七场基线，新增七场初始化先行。
- **Title**: 七场长视频已测，27B十四场尚待收尾
- **Core message**: 截至报告的11月9日23:37状态，27B未开始，无最终结果。
- **Content**: 已完成15.84h视频内容、每场64观察、相隔91–177s；mAP16.27→16.38，C/V接受1/0；十四场扩测基线进行中；非11月10日实时进度。

#### Slide 15 - 下一步顺序
- **Audience move**: 接受可检验、范围清楚的推进顺序。
- **Relationships**: 先修契约和核验语义，再检验按需价值，随后单变量补证；已启动SV按既有协议收尾。
- **Title**: 先修证据链，再检验按需价值与补证
- **Core message**: 新建议不构成启动许可，已有任务独立收尾。
- **Content**: CPU回归原50对；独立区分观察/完成/贡献；小规模按需问题库；等帧均匀vs定向补看，语音另设ASR；模型复验目标≥48/50合法但不靠全弃判；均为待审阅建议。

#### Slide 16 - 讨论决定
- **Audience move**: 明确需要组会决定的研究定位与验收条件。
- **Relationships**: 保留事实核验作主对照；五维承担按需问题与缺证提示；有效性需新增受控证据。
- **Title**: 建议保留五维，但将其定位为按需问题库
- **Core message**: 先证明它带来了有用新证据，再主张它提高高光选择。
- **Content**: 当前：更可追溯的事实、更明确的失败；待证：价值额外收益、定向补证、事件图；讨论：以普通核验为主对照是否合理；多需求剪辑与成片仍在后续阶段。
- **Closing impact**: hook=让价值问题指向缺证；以可验证问题和证据循环承接下一步，而非宣布收益。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under notes/
- **Content**: 根据最终SVG逐页写中文讲稿，保留精确数据、开发集限制、指标定义与来源；不逐字照读图表，区分完成与待验证。
- **Total duration**: 约12分钟
- **Notes style**: 自然、简明，先判断后证据，说明变化的意义和局限。
- **Presentation purpose**: 回应上次会议安排，解释结果和失败机制，讨论下一步取舍。
