<!-- ppt-master-schema: design-spec/v1 -->
# ReVALUE Weekly 20261109 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | revalue_weekly_20261109 |
| Canvas Format | PPT 16:9, 1280×720 |
| Page Count | 16 |
| Primary Language | zh-CN |
| Target Audience | 导师及熟悉项目的组会成员 |
| Communication Intent | 汇报本周对照结果，解释记忆与价值核验的具体卡点，讨论下一步修复顺序 |
| Desired Audience Outcome | 能区分局部工程改善与尚未确认的价值收益，并理解为何先修原50对而非直接扩大运行 |
| Core Message / Ask / Action | 事实记忆缩小了与Direct的差距；价值比较未稳定受益，先补齐证据与最终结论的联合约束 |
| Delivery Context | 主讲人现场组会，约15分钟；附讲稿供会后复核 |
| Artifact Afterlife | 作为项目周报及后续实验讨论依据，保留结果与案例来源 |
| Reading Mode | presentation |
| Content Strategy | 按结论、证据、机制、案例、计划重组周报；数值与样本范围保持来源含义 |
| Design Style | 结果驱动的研究证据图解，选用方向A |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | enabled — delegated design decision; notes for every page |
| Custom Animations | disabled — final Stage-2 proactive policy |
| Narration Audio | disabled — final Stage-2 proactive policy |
| Created Date | 2026-11-09 |

Delegation: 用户此前明确“设计细节由你决定，直接完成”，本次沿用；不生成虚构的用户确认回执。Stage 1为中文现场组会、自由设计、16:9、14–16页；Stage 2确定16页、可编辑图表与表格、原始缓存帧及逐页讲稿。

Three solution intents: A按结论→对照→失败机制→修复顺序推进；B从蜂箱案例切入并展开总体证据；C按模型、记忆、核验、迁移模块平行汇报。选择A，因听众需要先获得总体结果，再讨论具体修复；B过早聚焦个例，C弱化了下一步取舍。

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280×720 |
| viewBox | `0 0 1280 720` |
| Margins | 56 px |
| Content Area | 页面四边保留56px，主体使用中部有效区域 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Mode References**: pyramid
- **Mode Behavior**: 每页先给可核查判断，随后展示对应对照或证据；按进度、结果、失败机制、下一步顺序收束，始终区分已完成结果与建议。
- **Visual style**: custom
- **Visual Style References**: data-journalism
- **Visual Style Behavior**: 用带来源的研究图表构成页面重心，以简洁衬线标题、无衬线正文和精确数字建立层级；对照页用细规则、侧注和整洁数据区域，案例页由真实缓存画面及引用关系承载说明。
- **Theme**: 浅色研究证据页；以阶段标签和底部来源形成跨页连续性，图表、流程和案例交替呈现。
- **Tone**: 客观、清晰，负结果明确，避免将格式合法或开发均值改善写成已证明有效。

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FFFFFF | 正文页面 |
| Secondary background | #F2F5F7 | 证据分区 |
| Primary | #18344B | 主结论、Direct系统参照 |
| Accent | #C66A2D | 价值条件与待修复重点 |
| Secondary accent | #257C82 | 事实记忆及普通核验 |
| Body text | #233746 | 正文 |
| Secondary text | #536777 | 注释与来源 |
| Divider | #D5DEE4 | 分隔规则 |
| Negative | #B74D4D | 契约冲突、修复V15失败 |
| Positive | #26705B | 局部已完成修复 |
| Grid | #E5EBEF | 图表网格 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 简洁研究出版标题 | SimSun | Cambria | serif |
| Body | 投影清晰的中性正文 | Microsoft YaHei | Arial | sans-serif |
| Data | 清晰等高数字 | Microsoft YaHei | Arial | sans-serif |

- **Title stack**: SimSun, Cambria, serif
- **Body stack**: Microsoft YaHei, Arial, sans-serif
- **Data stack**: Microsoft YaHei, Arial, sans-serif
- **Role rationale**: 数值沿用正文的等高数字；display专门服务封面与关键读数，annotation、chart_label、footnote服务不同证据层级。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 28 |
| Title | 42 |
| Subtitle | 32 |
| Lead | 30 |
| Annotation | 20 |
| Chart label | 22 |
| Table text | 24 |
| Data | 24 |
| Display | 64 |
| Footnote | 14 |

## V. Layout Principles

### Deck-wide Direction

- **Hierarchy direction**: 判断句标题优先，再读图表或真实画面，最后读关键限制与来源。
- **Composition tendency**: 大图表与解释侧栏、完整流程与局部放大、并列证据画面，依页面任务变化。
- **Cross-page continuity**: 保留阶段标签、方法颜色和来源习惯；案例中的帧与引用保持同一命名。
- **Spacing posture**: 结果页信息较密，机制页和计划页留出解释空间。
- **Spacing anchors**: page margin=56; block gap=28; column gutter=32; corner radius=4; body leading=40 px。

## VI. Icon Usage Specification

- **Primary bundled library**: none

| Icon Path | Suitable Scenarios |
| --- | --- |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |
| P05 | chart | grouped_bar_chart | 比较旧val10与新增40的视频组中B0、F和FV |
| P06 | chart | horizontal_bar_chart | 对照固定40视频密集D与各版本记忆 |
| P07 | table | metric_table | 跨数据集保留各自指标比较D、F、F-read |
| P08 | chart | horizontal_bar_chart | 展示200对核验后的最终mAP |
| P09 | table | metric_table | 合法率、明确偏好与接受替换三个不同阶段 |
| P10 | table | record_table | 新版原50对22条无效的首个阻断原因 |
| P13 | table | record_table | 对照已改善部分与尚未解决的问题 |
| P15 | table | metric_table | 固定37候选的跨模型Q／Q+V辅助核验 |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Image pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hive_a_f0140.png | 640×352 | 20:11 | A局部证据，66.9669秒 | Evidence | 与A上下文及B片内帧并列呈现，保留完整画面 | no-crop | user | Existing | 原冻结npy中WxtbjNsCQ8A的f0140；来源和像素哈希由已有manifest核对 | none | local |
| hive_context_f0142.png | 640×352 | 20:11 | A上下文，68.9689秒 | Evidence | 与前后不同来源帧并列，显式标为自身上下文 | no-crop | user | Existing | 原冻结npy中WxtbjNsCQ8A的f0142；不重新解码视频 | none | local |
| hive_b_f0178.png | 640×352 | 20:11 | B局部证据，118.9855秒 | Evidence | 与A证据并列，突出它未被最终引用覆盖 | no-crop | user | Existing | 原冻结npy中WxtbjNsCQ8A的f0178 | none | local |
| pet_a_f0000.png | 640×352 | 20:11 | A门面画面，0秒 | Evidence | 与B美容台画面并列，事实描述附在图外 | no-crop | user | Existing | 原冻结npy中i3wAGJaaktw的f0000 | none | local |
| pet_b_f0025.png | 640×352 | 20:11 | B美容台画面，58.4919秒 | Evidence | 与A场景并列，说明可见场景与完成结果的区别 | no-crop | user | Existing | 原冻结npy中i3wAGJaaktw的f0025 | none | local |

## IX. Content Outline

### Part 1: Progress and Method

#### Slide 01 - 本周进度
- **Audience move**: 从上次组会目标进入本周结论。
- **Relationships**: 事实记忆和价值核验为并行研究模块，服务高光选择。
- **Title**: 事实记忆与价值核验
- **Core message**: 记忆缩小了差距，价值比较仍未稳定受益。
- **Content**: 周期2026.11.03–11.09；林逸飞；ReVALUE实验进度；本周重点为高光选择，保留grounding核验作辅助。
- **Cover impact**: Hook=记忆缩小了差距，价值比较仍未稳定受益；以两层证据概念展开，避免泛化宣传。

#### Slide 02 - 本周做了什么
- **Audience move**: 知道已完成范围与当前结论。
- **Relationships**: TVSum全50初版、固定40改进、200对核验是先后递进的不同实验，40 query与40视频是不同迁移范围。
- **Title**: 完成了多组对照，尚未确认稳定价值收益
- **Core message**: 关键成果是受控对照和可定位失败机制。
- **Content**: TVSum初版50视频；密集记忆40视频；后置核验200对；QFVS40 query与Mr.HiSum40视频；最新500次新增调用全部结束。

#### Slide 03 - 当前Pipeline
- **Audience move**: 区分记忆写入、选片、局部核验与未实现工具。
- **Relationships**: 冻结视频帧先生成事实记忆，事实与旧帧支持初选，初选候选对进入C或V15，核验决定受控替换；前置V为历史对照，当前后置verifier不读V库。
- **Title**: 先用事实记忆选片，再对固定候选做核验
- **Core message**: 当前是静态记忆与局部核验路径。
- **Content**: 1fps分组观察→F事实库→预算读取→Top-5初选→固定候选对→C或V15→受控替换；失败／弃判保留原选择；回看、边界细化、候选外搜索尚待验证。

#### Slide 04 - 价值判断标准
- **Audience move**: 理解15题的三层问题及来源边界。
- **Relationships**: 结果、信息、情绪、动作、视觉事件同属五种价值视角；每维依次判断事实、贡献、相对优先。
- **Title**: 五维价值拆成十五个问题，逐项绑定证据
- **Core message**: 有事实、有观看贡献、有比较优势是三个判断。
- **Content**: 关键结果、核心信息、情绪反应、精彩动作、视觉事件；每维观察→贡献→相对优先；每候选15题、每对30题；允许支持／反证／不足／不适用；借鉴VisionReward的问题分解，没有使用其权重或官方高光标准。

### Part 2: Results

#### Slide 05 - 从10到50
- **Audience move**: 识别小样本开发收益没有延续。
- **Relationships**: 旧val10与新增40互不混作同一视频组，B0、F、FV在各自组内对比。
- **Title**: 旧10条的价值收益，未延续到新增40条
- **Core message**: FV−F从旧val10的+3.1622pp变为新增40的−1.9747pp。
- **Content**: 旧val10 B0/F/FV=61.3167/59.7625/62.9247；新增40=53.2858/52.6220/50.6473；全50汇总54.8919/54.0501/53.1028；新增40差值CI[−5.5885,+1.1280]；全50非独立官方test50。
- **Visualization**: early-results：B0/F/FV按两个视频组并列，保留完整零基线。
- **Native-ready**: early-results=yes

#### Slide 06 - 密集观察与事实保真
- **Audience move**: 看清读取和时间绑定改善，但仍未稳定超过D。
- **Relationships**: 同一固定40范围内，F、FV读取和F-local、FV-local是后续版本；D为不同成本系统参照。
- **Title**: 事实保真改进缩小差距，价值增量仍待确认
- **Core message**: F-local从54.4796升至57.5828；D-1fps为58.4767。
- **Content**: D-1fps58.4767，F54.4796，旧FV53.2167，FV-read55.3426，F-local57.5828，FV-local56.3439；F-local−F +3.1032pp，CI[−1.1440,+7.7236]；D与记忆组视觉呈现与token成本不同。
- **Visualization**: dense-results：六种系统条件的水平条形比较。
- **Native-ready**: dense-results=yes

#### Slide 07 - 迁移验证
- **Audience move**: 理解跨数据集结果没有一致收益，且指标不同。
- **Relationships**: QFVS与Mr.HiSum分别使用自身指标，F-read对F是主比较，系统参照覆盖不同。
- **Title**: 事实读取改进没有带来一致的跨数据集收益
- **Core message**: 两轮都是小规模事实读取对照，不是完整新方案的跨集验证。
- **Content**: QFVS40 query，F1 D43.7665/F43.3331/F-read43.5179，Uniform47.7199；Mr.HiSum40视频，mAP50 D59.5961/F59.4063/F-read59.0989，mAP15 24.4014/22.9383/22.9127，F1 46.0845/47.1429/45.8208；QFVS仅4源视频且84候选；Mr.HiSum不含V、非1fps。
- **Visualization**: transfer-results：数据集／指标与三组读数的可编辑表格。
- **Native-ready**: transfer-results=yes

#### Slide 08 - 后置Verifier结果
- **Audience move**: 区分普通核验收益与V15详细标准的额外贡献。
- **Relationships**: F-local为共同基线，C／旧V15／修复V15分别后置核验。
- **Title**: 详细价值核验仍未超过普通核验
- **Core message**: 最新40视频的普通核验58.4573，旧V15 58.4085，修复V15 57.6496。
- **Content**: F-local57.5828；普通C增0.8745pp且CI跨0；旧V15增0.8257pp；修复V15增0.0668pp；D-1fps为58.4767但成本不同；C也判断一般观看贡献，V15额外引入逐题标准与绑定。
- **Visualization**: verifier-map：共同F-local与三个后置核验结果的水平条形比较。
- **Native-ready**: verifier-map=yes

#### Slide 09 - 合法率与覆盖
- **Audience move**: 理解修复版同时损失输出合法性和明确比较覆盖。
- **Relationships**: 合法响应、明确A/B偏好和通过保守替换是不同处理阶段。
- **Title**: 合法率与比较覆盖一起下降，修复尚未成功
- **Core message**: 200对中修复V15仅135合法、26明确偏好、4次接受替换。
- **Content**: C=200合法/116偏好/29替换；旧V15=144/63/12；修复V15=135/26/4；原50对旧33合法，11变无效、6恢复，最终28；局部已修≠整个输出一致。
- **Visualization**: verifier-coverage：三种核验臂的三个阶段计数表。
- **Native-ready**: verifier-coverage=yes

### Part 3: Diagnosis and Next Step

#### Slide 10 - 失败机制
- **Audience move**: 把合法率下降定位到生成与校验接口。
- **Relationships**: 单题前提约束与整条结论约束是不同层级；生成schema与最终校验承接同一响应。
- **Title**: 逐题依赖已修，最终胜负仍缺联合约束
- **Core message**: 新版原50对的22条无效全部通过生成JSON schema。
- **Content**: 首个阻断原因：赢家依据不足8、自身上下文当双方比较8、事件不足却胜负或tie6；第2问前提违规8→0，第3问4→0；两组均stop，无截断；这些是契约诊断，不是语义错误率。
- **Visualization**: invalid-causes：22条无效首因分解表；生成→最终检查的关系用几何说明。
- **Native-ready**: invalid-causes=yes

#### Slide 11 - 蜂箱案例
- **Audience move**: 通过真实帧理解上下文证据为何不等于双方比较。
- **Relationships**: A区间66–68秒先于A上下文68.9689秒；B区间118–120秒是另一候选；A.O3引用A上下文却用于A胜B。
- **Title**: 蜂箱案例：自身过程不能替代双方比较证据
- **Core message**: f0142能补A的过程，却不能单独证明A比B更值得选。
- **Content**: 视频WxtbjNsCQ8A、pair02；A.O3=s，comparator=f0142，最终verdict=A；A局部f0140=66.9669秒，A上下文f0142=68.9689秒，B局部f0178=118.9855秒；助手缓存帧审阅，非独立人工标签。
- **Images**: hive_a_f0140.png、hive_context_f0142.png、hive_b_f0178.png完整并列，图外标时间与证据角色。

#### Slide 12 - 美容台案例
- **Audience move**: 区分可见事实、结果确认和价值结论。
- **Relationships**: A门面与B美容台是两候选；B场景可见不推出已完成美容，事件状态与最终A胜又有契约冲突。
- **Title**: 狗在美容台上可见，完成美容仍需额外证据
- **Core message**: 没看到完成，不能覆盖已经看清的事实。
- **Content**: 视频i3wAGJaaktw、pair00；A0–2秒，B58–60秒；新B.observation描述狗在台上、state却为insufficient，missing为没有完成或明显动作；comparison仍选A；部分报错误指空missing，实际为事件资格失败。
- **Images**: pet_a_f0000.png与pet_b_f0025.png完整并列，分别标明A/B和PTS，下面对应三个命题层次。

#### Slide 13 - 已改善与待解决
- **Audience move**: 区分可确认修复与未通过验收的科学问题。
- **Relationships**: 读取、事实、原子判断、整体比较和选片评价各层存在不同剩余问题。
- **Title**: 已改善局部证据接口，尚未验证价值增益
- **Core message**: 代码契约、视觉语义、相对高光价值需分别验收。
- **Content**: 读取偏差已定位并对照，但压缩与比较证据仍缺；F-local改善开发均值但事实可能看错；原子可观察性8/8合法但最终8/8不足；V15局部依赖修好但全局结论冲突；未实现自动回看／边界细化／候选外搜索。
- **Visualization**: issue-status：已确认进展与尚未解决项的对照记录表。
- **Native-ready**: issue-status=yes

#### Slide 14 - 下一步
- **Audience move**: 形成先修接口、再小试、再决定扩展的顺序。
- **Relationships**: CPU联合契约通过后才能做原50对前瞻测试，随后判断比较与选片收益，再决定是否扩展。
- **Title**: 先保证证据与结论一致，再验证价值增益
- **Core message**: 原50对验证通过后，再讨论扩到200对或增加工具。
- **Content**: 联合约束与报错定位→原50对CPU回归→原50对修复V15前瞻→合法率、明确比较、替换与mAP共同验收；建议至少48/50合法，允许不足与负结果，不强迫胜负；本次仅制作PPT，后续测试未启动。
- **Data class**: scenario — 至少48/50是拟议验收目标，不是已测结果。
- **Closing impact**: Hook=先修证据到结论的接口；保留事实、比较、结果三层验收。

### Part 4: Appendix

#### Slide 15 - 辅助模型对照
- **Audience move**: 复核本周27B结果，避免把低IoU检错写成HD提升。
- **Relationships**: 8B、32B、27B均在固定37候选比较Q与Q+V，但原生处理器不同。
- **Title**: 27B输出更稳定，Q+V尚未优于Q
- **Core message**: 27B两臂37/37合法，Q报警9、Q+V报警6。
- **Content**: 六行按模型／臂列合法、报警、证据不足、低IoU代理召回：8B Q36/37,2,11,8%；8B Q+V37/37,4,16,16%；32B Q33/37,1,32,4%；32B Q+V33/37,0,33,0%；27B Q37/37,9,17,36%；27B Q+V37/37,6,21,24%；只flagged计报警，未改边界、无人类语义真值，不是高光mAP。
- **Visualization**: model-controls：固定37候选的可编辑核验表。
- **Native-ready**: model-controls=yes

#### Slide 16 - 证据边界与归档
- **Audience move**: 知道结果可追溯、未完成项及泛化限制。
- **Relationships**: 已完成500次与旧100次复用分账；未完成brief/detail与全量实验不混用。
- **Title**: 保留完整分母与失败，当前结论限于开发证据
- **Core message**: 可以复核工程问题，尚不能宣布稳定泛化或SOTA。
- **Content**: 最新新增500次、2922469token、95897.409187GPU秒、10worker零重试；旧100次单列；brief/detail中止各仅6视频完成，其余34回退不当完整实验；QFVS40query与Mr.HiSum40视频非全量；D与记忆成本不同；案例为助手查看旧帧、非独立人工核验；主要来源在同目录sources及项目周报。

## X. Speaker Notes Requirements

- **Generation**: enabled
- **Filename**: match each SVG filename under notes/
- **Content**: 根据最终可见页面写中文讲稿；每页开头给结论，解释设置与边界，补充原始数值与文件来源；不添加新结果。附录明确为备用。
- **Total duration**: 主体14页约15分钟，附录2页按需使用。
- **Notes style**: 组会口述，清晰、客观，可直接使用。
- **Presentation purpose**: 汇报本周实验、解释失败机制并讨论下一步修复顺序。
