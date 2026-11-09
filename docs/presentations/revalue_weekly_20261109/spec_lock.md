<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- format: PPT 16:9
- viewBox: 0 0 1280 720

## communication
- primary_language: zh-CN
- audience: 导师与熟悉项目的组会成员
- objective: 汇报本周实验结果与失败机制，使听众区分工程改善与尚未确认的价值收益，并理解下一步先修原50对的理由。
- core_message: 事实记忆缩小了与Direct的差距；价值比较未稳定受益，先补齐证据与最终结论的联合约束。
- consumption_mode: presentation

## mode
- mode: custom
- mode_references: pyramid
- mode_behavior: 每页先给可核查判断，再展示对照或来源，按进度、结果、失败机制、修复顺序推进，已测结果与建议明确区分。

## visual_style
- visual_style: custom
- visual_style_references: data-journalism
- visual_style_behavior: 以带来源的研究图表为重心，用衬线标题、无衬线正文、精确数字和细规则组织证据；流程、结果与真实帧案例交替呈现。

## colors
- background: #FFFFFF
- secondary_bg: #F2F5F7
- primary: #18344B
- accent: #C66A2D
- secondary_accent: #257C82
- body_text: #233746
- secondary_text: #536777
- divider: #D5DEE4
- negative: #B74D4D
- positive: #26705B
- grid: #E5EBEF

## typography
- font_family: Microsoft YaHei, Arial, sans-serif
- title_family: SimSun, Cambria, serif
- body_family: Microsoft YaHei, Arial, sans-serif
- data_family: Microsoft YaHei, Arial, sans-serif
- body: 28
- title: 42
- subtitle: 32
- lead: 30
- annotation: 20
- chart_label: 22
- table_text: 24
- data: 24
- display: 64
- footnote: 14

## icons
- library: none
- inventory: none

## images
- hive-a: images/hive_a_f0140.png | source=user | crop=no-crop
- hive-context: images/hive_context_f0142.png | source=user | crop=no-crop
- hive-b: images/hive_b_f0178.png | source=user | crop=no-crop
- pet-a: images/pet_a_f0000.png | source=user | crop=no-crop
- pet-b: images/pet_b_f0025.png | source=user | crop=no-crop

## page_visualizations
- P05: chart/grouped_bar_chart
- P06: chart/horizontal_bar_chart
- P07: table/metric_table
- P08: chart/horizontal_bar_chart
- P09: table/metric_table
- P10: table/record_table
- P13: table/record_table
- P15: table/metric_table

## page_rhythm
- P01: anchor
- P02: breathing
- P03: dense
- P04: dense
- P05: dense
- P06: dense
- P07: dense
- P08: dense
- P09: dense
- P10: dense
- P11: breathing
- P12: breathing
- P13: dense
- P14: anchor
- P15: dense
- P16: dense

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
