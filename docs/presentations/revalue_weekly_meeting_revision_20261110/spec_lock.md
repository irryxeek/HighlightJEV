<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: zh-CN
- audience: 导师与研究组成员
- objective: 对照纪要解释记忆与价值实验，帮助导师区分已解决问题、证据缺口和下一步实验取舍。
- core_message: 事实记忆更可用但尚未超过Direct；详细价值未超过普通核验；先修证据链，再验证按需价值与补证。
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: pyramid
- mode_behavior: 先给当前判断，围绕记忆收益和价值额外收益分组展示对照，再以具体错误解释限制，最后落到待讨论决定。

## visual_style
- visual_style: custom
- visual_style_references: data-journalism
- visual_style_behavior: 图表作为页面主轴，衬线判断标题配无衬线数据，细分隔线和侧注组织证据，真实联系表与短证据链相邻，色块强调结论与待验证状态。

## colors
- background: #FFFFFF
- secondary_bg: #F2F5F7
- primary: #17324D
- accent: #C56B2C
- secondary_accent: #237F89
- body_text: #243746
- secondary_text: #52677A
- divider: #CCD7E0
- surface: #F7F9FB
- grid: #E2E8EE
- negative: #B94444
- neutral_data: #64798B

## typography
- font_family: Microsoft YaHei, Arial
- title_family: SimSun, Arial
- body_family: Microsoft YaHei, Arial
- display_family: Arial
- cover_family: SimSun, Arial
- body: 24
- title: 46
- subtitle: 30
- lead: 28
- annotation: 18
- footnote: 14
- label: 20
- data: 22
- display: 72
- cover: 64

## icons
- library: none
- inventory: none

## images
- case-contradiction: images/z_6gVvQb2d0__pair01.jpg | source=user | crop=no-crop
- case-comparison: images/WxtbjNsCQ8A__pair02.jpg | source=user | crop=no-crop

## page_rhythm
- P01: anchor
- P02: breathing
- P03: dense
- P04: anchor
- P05: dense
- P06: dense
- P07: dense
- P08: breathing
- P09: dense
- P10: dense
- P11: dense
- P12: dense
- P13: dense
- P14: breathing
- P15: anchor
- P16: anchor

## page_visualizations
- P03: table/comparison_matrix
- P06: chart/grouped_bar_chart
- P07: chart/horizontal_bar_chart
- P09: chart/horizontal_bar_chart
- P10: chart/stacked_bar_chart
- P13: table/metric_table

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
