#!/usr/bin/env python3
"""Render a native, editable SVG of the proposed VideoJev highlight agent."""

from pathlib import Path
from xml.etree import ElementTree as ET


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "videojev_agent_framework_v2.svg"
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)

COLOR = {
    "ink": "#203A4C",
    "muted": "#586F7C",
    "line": "#526D7B",
    "border": "#D6E1E5",
    "blue": "#3D7693",
    "blue_fill": "#EAF3F8",
    "blue_edge": "#B0CDDC",
    "teal": "#237D7F",
    "teal_fill": "#EAF5F3",
    "teal_edge": "#B0D4CD",
    "amber": "#B66A32",
    "amber_fill": "#FDF7EF",
    "amber_edge": "#DFC39E",
    "green": "#477D64",
    "green_fill": "#EEF5EE",
    "green_edge": "#BCD4BF",
    "white": "#FFFFFF",
}


def element(parent, tag, **attributes):
    return ET.SubElement(
        parent,
        f"{{{SVG}}}{tag}",
        {key.replace("_", "-"): str(value) for key, value in attributes.items()},
    )


def color(value):
    return COLOR.get(value, value)


def group(parent, name):
    return element(parent, "g", id=name)


def rect(parent, x, y, width, height, fill, stroke="none", radius=0, **attributes):
    return element(parent, "rect", x=x, y=y, width=width, height=height,
                   fill=color(fill), stroke=color(stroke), stroke_width=1.8,
                   rx=radius, **attributes)


def text(parent, x, y, value, size=28, fill="ink", weight=400, anchor="start", **attributes):
    node = element(parent, "text", x=x, y=y, font_family="Noto Sans CJK SC, sans-serif",
                   font_size=size, font_weight=weight, fill=color(fill),
                   text_anchor=anchor, **attributes)
    node.text = value
    return node


def line(parent, x1, y1, x2, y2, stroke="line", width=2, **attributes):
    return element(parent, "line", x1=x1, y1=y1, x2=x2, y2=y2,
                   stroke=color(stroke), stroke_width=width, **attributes)


def path(parent, d, stroke="line", width=3, dashed=False, arrow=False, **attributes):
    if dashed:
        attributes["stroke_dasharray"] = "9 7"
    if arrow:
        attributes["marker_end"] = f"url(#arrow-{stroke})"
    return element(parent, "path", d=d, fill="none", stroke=color(stroke),
                   stroke_width=width, stroke_linecap="round",
                   stroke_linejoin="round", **attributes)


def connector(parent, d, stroke="line", dashed=False):
    return path(parent, d, stroke=stroke, width=3.2, dashed=dashed, arrow=True)


def stage(parent, x, number, title, accent):
    text(parent, x, 207, number, size=28, fill=accent, weight=700)
    text(parent, x + 49, 207, title, size=31, weight=700)


root = ET.Element(f"{{{SVG}}}svg", {
    "width": "180mm", "height": "91.8mm", "viewBox": "0 0 2000 1020",
    "version": "1.1",
})
element(root, "title").text = "VideoJev-4B 高光检测 Agent：共享上下文、五维 QA 与按需回看"
element(root, "desc").text = (
    "待实现与验证的研究框架。全片采样帧和真实时间构成共享视觉上下文。"
    "每个目标时间窗分别进行结果、信息、情绪、动作、感官五维 QA，保留分数及未知概率。"
    "Agent 细化覆盖时间轴的候选；仅在缺少证据且仍有计算预算时定向读取源视频新帧，"
    "重新编码并局部再评分，将更新送回候选细化。停止后按独立的输出时长预算去重、"
    "合并并输出高光片段。矩阵与时间块仅表示数据结构，不是实验得分。"
)

defs = element(root, "defs")
for name in ("line", "blue", "teal", "amber", "green"):
    marker = element(defs, "marker", id=f"arrow-{name}", viewBox="0 0 10 10",
                     refX=9, refY=5, markerWidth=3.5, markerHeight=3.5,
                     orient="auto-start-reverse")
    element(marker, "path", d="M 0 0 L 10 5 L 0 10 Z", fill=color(name))

rect(root, 0, 0, 2000, 1020, "white")

header = group(root, "header")
text(header, 40, 73, "VideoJev-4B 高光检测 Agent", size=44, weight=700)
text(header, 40, 119, "共享全片上下文，逐窗判断价值，按需补证后选片", size=27, fill="muted")
text(header, 1960, 71, "方案设计 · 待验证", size=25, fill="muted", anchor="end")
line(header, 40, 148, 1960, 148, stroke="border", width=1.8)

stages = group(root, "stage-headings")
stage(stages, 40, "01", "全片上下文", "blue")
stage(stages, 450, "02", "五维 QA 初评分", "teal")
stage(stages, 995, "03", "Agent 候选细化", "amber")
stage(stages, 1660, "04", "预算选片", "green")

panels = group(root, "panel-backgrounds")
rect(panels, 40, 430, 340, 210, "blue_fill", "blue_edge", radius=15)
rect(panels, 450, 310, 490, 330, "teal_fill", "teal_edge", radius=15)
rect(panels, 980, 245, 615, 675, "amber_fill", "amber_edge", radius=20)
rect(panels, 1005, 310, 250, 330, "white", "amber_edge", radius=12)
rect(panels, 1660, 310, 300, 330, "green_fill", "green_edge", radius=15)
rect(panels, 40, 745, 900, 175, "#F4F8F8", "border", radius=15)
rect(panels, 1005, 745, 250, 140, "white", "amber_edge", radius=12)
rect(panels, 1315, 745, 250, 140, "white", "amber_edge", radius=12)
rect(panels, 1660, 745, 300, 175, "#F8FAF7", "green_edge", radius=15)

connections = group(root, "data-and-feedback-connections")
connector(connections, "M 210 377 V 430", "blue")
connector(connections, "M 380 485 H 450", "blue")
connector(connections, "M 940 485 H 1005", "teal")
connector(connections, "M 1255 485 H 1300")
connector(connections, "M 1570 485 H 1660", "green")
connector(connections, "M 695 745 V 640", "teal")
connector(connections, "M 1810 745 V 640", "green")
connector(connections, "M 1435 590 V 745", "amber", dashed=True)
connector(connections, "M 1315 815 H 1255", "amber", dashed=True)
connector(connections, "M 1130 745 V 640", "amber", dashed=True)

source = group(root, "sampled-full-video")
text(source, 210, 272, "全片采样帧 + 时间戳", size=28, anchor="middle")
for index, x in enumerate((61, 154, 247)):
    # Native vectors signify sampled frames; no illustrative photo is claimed as input data.
    frame = group(source, f"sample-frame-{index + 1}")
    rect(frame, x, 298, 82, 63, "#F0F6F6", "#AFC9D1", radius=6)
    element(frame, "circle", cx=x + 57, cy=314, r=6, fill="#D9B576")
    element(frame, "path", d=f"M {x + 8} 350 L {x + 28} 323 L {x + 42} 338 "
            f"L {x + 54} 329 L {x + 74} 350 Z", fill="#90B9BB")
line(source, 65, 376, 325, 376, "#8AA9B6", width=2)
for x in (102, 195, 288):
    line(source, x, 371, x, 381, "#8AA9B6", width=2)

cache = group(root, "shared-global-visual-context")
text(cache, 210, 475, "全片上下文缓存", size=31, weight=700, anchor="middle")
for row in range(2):
    for column in range(7):
        rect(cache, 76 + column * 39, 501 + row * 37, 29, 25,
             ("#9BC1D4", "#BDD8E2", "#C8DFE7")[(row + column) % 3], radius=3)
text(cache, 210, 608, "同一视频前缀跨问题复用", size=25, fill="blue", anchor="middle")

qa = group(root, "five-dimensional-qa")
text(qa, 695, 271, "目标时间窗 × 五维问题", size=28, anchor="middle", fill="teal")
text(qa, 695, 355, "VideoJev-4B  ·  QA / choice", size=30, weight=700, anchor="middle")
line(qa, 478, 378, 912, 378, "teal_edge", width=1.5)
dimension_fills = ("#C7E2DA", "#CDDFEC", "#EDDACD", "#EEE3BC", "#DED9EC")
for column, label in enumerate(("结果", "信息", "情绪", "动作", "感官")):
    x = 568 + column * 69
    text(qa, x + 27, 416, label, size=27, anchor="middle", weight=500)
    for row in (0, 1, 3):
        rect(qa, x, 432 + row * 34, 55, 23, dimension_fills[column], radius=4)
    text(qa, x + 27, 519, "⋮", size=23, anchor="middle", fill="muted")
for row, label in enumerate(("w₁", "w₂", "⋮", "wₙ")):
    text(qa, 526, 453 + row * 34, label, size=25, anchor="middle", fill="muted")
text(qa, 695, 593, "五维分数 + 未知概率", size=28, fill="teal", weight=600, anchor="middle")
text(qa, 695, 625, "固定融合规则 → 初始评分曲线", size=23, fill="muted", anchor="middle")

query = group(root, "target-window-and-value-query")
text(query, 64, 787, "目标时间窗", size=29, weight=700)
text(query, 64, 830, "n 由计算预算确定", size=26, fill="muted")
for index, label in enumerate(("w₁", "w₂", "…", "wₙ")):
    x = 64 + index * 78
    rect(query, x, 851, 66, 36, "#D8E9E7" if index != 1 else "#9FCAC4", radius=5)
    text(query, x + 33, 878, label, size=24, anchor="middle", fill="teal")
connector(query, "M 399 835 H 446", "teal")
text(query, 476, 787, "仅评价 [tₛ, tₑ] 的该维度贡献", size=27, weight=600)
text(query, 476, 833, "每窗 5 题；共享同一全片上下文", size=26, fill="muted")
text(query, 476, 879, "选项：0 / 1 / 2 / 未知", size=28, fill="teal")

candidate = group(root, "candidate-selection-and-refinement")
text(candidate, 1130, 355, "候选细化", size=32, weight=700, anchor="middle")
text(candidate, 1130, 399, "高分 · 缺证 · 覆盖", size=25, fill="muted", anchor="middle")
rect(candidate, 1030, 426, 200, 25, "#E9E6DF", radius=4)
rect(candidate, 1087, 426, 80, 25, "#DAB279", radius=4)
connector(candidate, "M 1127 461 V 491", "amber")
for index in range(5):
    rect(candidate, 1030 + index * 41, 504, 35, 25,
         ("#E9E6DF", "#E9E6DF", "#DAB279", "#9FBCAD", "#E9E6DF")[index], radius=3)
text(candidate, 1130, 577, "窗口与边界细化", size=26, anchor="middle")
text(candidate, 1130, 614, "必要时比较", size=26, fill="muted", anchor="middle")

controller = group(root, "agent-budget-aware-controller")
text(controller, 1435, 340, "Agent 调度", size=30, weight=700, anchor="middle")
element(controller, "path", d="M 1435 380 L 1570 485 L 1435 590 L 1300 485 Z",
        fill="#FAEBD7", stroke=color("amber_edge"), stroke_width=2)
text(controller, 1435, 476, "是否补证？", size=29, weight=700, anchor="middle")
text(controller, 1435, 517, "证据 · 预算", size=24, fill="amber", anchor="middle")
text(controller, 1618, 456, "否", size=26, fill="green", anchor="middle")

feedback = group(root, "optional-evidence-revisit-loop")
rect(feedback, 1313, 663, 245, 40, "amber_fill")
text(feedback, 1435, 692, "缺证且有预算", size=27, fill="amber", weight=600, anchor="middle")
rect(feedback, 1000, 663, 260, 40, "amber_fill")
text(feedback, 1130, 692, "更新分数与边界", size=26, fill="amber", weight=600, anchor="middle")
text(feedback, 1440, 786, "定向回看", size=29, weight=700, anchor="middle")
text(feedback, 1440, 826, "源视频新帧", size=26, anchor="middle")
text(feedback, 1440, 862, "位置 · 问题 · 密度", size=24, fill="muted", anchor="middle")
text(feedback, 1130, 786, "局部再评分", size=29, weight=700, anchor="middle")
text(feedback, 1130, 826, "新帧编码 + QA", size=26, anchor="middle")
text(feedback, 1130, 862, "只更新相关判断", size=24, fill="muted", anchor="middle")

selection = group(root, "budgeted-highlight-output")
text(selection, 1810, 355, "高光片段", size=32, weight=700, anchor="middle")
text(selection, 1810, 402, "去重 · 合并 · 覆盖", size=25, fill="muted", anchor="middle")
line(selection, 1687, 471, 1933, 471, "#A5BCA6", width=3)
for x, width, fill in ((1694, 49, "#85B095"), (1783, 46, "#C6AB77"), (1876, 51, "#85B095")):
    rect(selection, x, 454, width, 35, fill, radius=4)
connector(selection, "M 1810 503 V 532", "green")
for x, width, fill in ((1731, 49, "#85B095"), (1783, 46, "#C6AB77"), (1832, 51, "#85B095")):
    rect(selection, x, 545, width, 35, fill, radius=4)
text(selection, 1810, 615, "按时间顺序输出", size=26, fill="green", anchor="middle")

budget = group(root, "user-output-duration-budget")
text(budget, 1810, 788, "用户时长预算", size=29, weight=700, anchor="middle")
for x, label in ((1681, "5 s"), (1770, "10 s"), (1859, "1 min")):
    rect(budget, x, 813, 78, 40, "white", "green_edge", radius=7)
    text(budget, x + 39, 842, label, size=25, fill="green", anchor="middle")
text(budget, 1810, 892, "输出总时长 ≤ 预算", size=26, fill="green", weight=600, anchor="middle")

footer = group(root, "legend-and-caveat")
line(footer, 40, 951, 1960, 951, "border", width=1.8)
line(footer, 40, 984, 90, 984, "line", width=3)
text(footer, 103, 993, "主流程", size=24, fill="muted")
line(footer, 218, 984, 268, 984, "amber", width=3, stroke_dasharray="9 7")
text(footer, 281, 993, "按需回看", size=24, fill="muted")
text(footer, 1960, 993, "缓存适配、价值评分与回看策略均待验证", size=24, fill="muted", anchor="end")

ET.ElementTree(root).write(OUTPUT, encoding="utf-8", xml_declaration=True)
print(OUTPUT)
