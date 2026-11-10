<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- format: ppt169
- viewBox: 0 0 1280 720

## communication
- primary_language: zh-CN
- audience: 导师与研究组，关注方法贡献、实验依据和下一步取舍
- objective: 用同范围对照和失败案例说明本周进展，让观众区分已验证结果与尚未确认的价值收益并讨论验证顺序。
- core_message: 事实保真和关键贡献目标值得继续优化；五维价值的稳定额外收益尚未确认。
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: pyramid
- mode_behavior: 结论先行，区分两条工作路线，以对照与反例支持判断，再给出有边界的下一步；数据页紧邻指标标注范围与配对差值。

## visual_style
- visual_style: custom
- visual_style_references: swiss-minimal
- visual_style_behavior: 清晰栅格、少量大面积分区、锐利边缘与留白；数据、细规则和方向连接承担结构。相同语义使用一致颜色，避免逐条重复包卡。

## colors
- background: #FFFFFF
- secondary_bg: #F1F5F7
- primary: #19344E
- accent: #207F89
- secondary_accent: #C76B2C
- body_text: #263D50
- secondary_text: #607586
- divider: #D6E1E8
- grid: #E7EDF1
- negative: #B34D4D

## typography
- font_family: Microsoft YaHei, Arial
- title_family: Microsoft YaHei, Arial
- body_family: Microsoft YaHei, Arial
- body: 24
- title: 42
- subtitle: 30
- lead: 28
- annotation: 20
- footnote: 14
- kicker: 16
- data: 24
- display: 72
- hero: 52

## icons
- library: none
- inventory: none

## page_rhythm
- P01: anchor
- P02: dense
- P03: dense
- P04: dense
- P05: dense
- P06: breathing
- P07: dense
- P08: dense
- P09: dense
- P10: anchor

## page_visualizations
- P03: chart/horizontal_bar_chart
- P05: chart/horizontal_bar_chart
- P07: table/metric_table
- P08: table/comparison_matrix

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
