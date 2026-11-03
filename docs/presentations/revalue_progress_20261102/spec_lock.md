<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- primary_language: zh-CN
- audience: 导师与组会成员，了解grounding研究并审查现有证据
- objective: 汇报实验进度与卡点，使听众能区分合法性、语义检错和定位质量并理解下一步验证标准
- core_message: 输出可靠性已改善；检错召回仍低，价值引导收益未确立，32B暂未产生预测
- consumption_mode: balanced

## mode
- mode: custom
- mode_references: pyramid
- mode_behavior: 结论先行，以基线、对照、修复、案例和运行收据解释成果与缺口，最后给可审查的验证任务。

## visual_style
- visual_style: custom
- visual_style_references: swiss-minimal, data-journalism
- visual_style_behavior: 开放网格与左对齐重标题，平面图表和结构线承载比较，主数字与细来源线形成证据层级；青绿表示Q+V和工程完成，橙色表示不足与风险。

## colors
- background: #FFFFFF
- secondary_bg: #F2F5F8
- primary: #17324D
- accent: #237F89
- secondary_accent: #C96A32
- body_text: #243748
- secondary_text: #637485
- divider: #CFD9E2
- surface: #EAF3F3
- grid: #E5EBF0
- negative: #B44747

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
- display: 64
- cover: 60

## icons
- library: none
- inventory: none

## page_rhythm
- P01: anchor
- P02: dense
- P03: dense
- P04: dense
- P05: breathing
- P06: dense
- P07: dense
- P08: breathing
- P09: dense
- P10: dense
- P11: dense
- P12: anchor

## page_visualizations
- P03: table/comparison_matrix
- P05: chart/horizontal_bar_chart
- P06: chart/column_chart
- P07: chart/stacked_bar_chart
- P10: table/comparison_matrix

## pptx_structure
- mode: flat

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
