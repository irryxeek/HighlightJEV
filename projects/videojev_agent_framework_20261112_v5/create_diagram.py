#!/usr/bin/env python3
"""Build the editable SVG for the proposed HighlightJEV hierarchy (no inference)."""

from pathlib import Path
from xml.etree import ElementTree as ET


HERE = Path(__file__).resolve().parent
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
W, H = 2600, 1760
COLORS = {
    "ink": "#203A4C", "muted": "#586F7C", "line": "#526D7B",
    "border": "#D6E1E5", "white": "#FFFFFF",
    "blue": "#3D7693", "blue_fill": "#EAF3F8", "blue_edge": "#B0CDDC",
    "teal": "#237D7F", "teal_fill": "#EAF5F3", "teal_edge": "#B0D4CD",
    "amber": "#B66A32", "amber_fill": "#FDF7EF", "amber_edge": "#DFC39E",
    "green": "#477D64", "green_fill": "#EEF5EE", "green_edge": "#BCD4BF",
    "purple": "#71678F", "purple_fill": "#F1EFF7", "purple_edge": "#CBC5DD",
}


def element(parent, tag, **attributes):
    return ET.SubElement(parent, f"{{{SVG}}}{tag}", {
        key.replace("_", "-"): str(value) for key, value in attributes.items()
    })


def color(value):
    return COLORS.get(value, value)


def group(parent, name):
    return element(parent, "g", id=name)


def rect(parent, x, y, w, h, fill="white", stroke="none", radius=12, **kw):
    return element(parent, "rect", x=x, y=y, width=w, height=h, rx=radius,
                   fill=color(fill), stroke=color(stroke), stroke_width=2, **kw)


def text(parent, x, y, value, size=30, fill="ink", weight=400, anchor="start", **kw):
    node = element(parent, "text", x=x, y=y,
                   font_family="Noto Sans CJK SC, sans-serif", font_size=size,
                   font_weight=weight, fill=color(fill), text_anchor=anchor, **kw)
    node.text = value
    return node


def line(parent, x1, y1, x2, y2, stroke="line", width=2, **kw):
    return element(parent, "line", x1=x1, y1=y1, x2=x2, y2=y2,
                   stroke=color(stroke), stroke_width=width, **kw)


def path(parent, d, stroke="line", width=3.2, dashed=False, arrow=False, **kw):
    if dashed:
        kw["stroke_dasharray"] = "10 8"
    if arrow:
        kw["marker_end"] = f"url(#arrow-{stroke})"
    return element(parent, "path", d=d, fill="none", stroke=color(stroke),
                   stroke_width=width, stroke_linecap="round", stroke_linejoin="round", **kw)


def arrow(parent, d, stroke="line", dashed=False):
    return path(parent, d, stroke=stroke, dashed=dashed, arrow=True)


def dot(parent, x, y, fill):
    element(parent, "circle", cx=x, cy=y, r=5, fill=color(fill))


def pill(parent, x, y, w, label, fill="white", stroke="border", ink="ink", size=27):
    rect(parent, x, y, w, 46, fill, stroke, 9)
    text(parent, x+w/2, y+33, label, size, ink, anchor="middle")


root = ET.Element(f"{{{SVG}}}svg", {
    "width": "280mm", "height": f"{280*H/W:.5f}mm", "viewBox": f"0 0 {W} {H}",
    "role": "img", "aria-labelledby": "figure-title figure-description",
})
element(root, "title", id="figure-title").text = "HighlightJEV：分层评分、证据回溯与高光边界"
element(root, "desc", id="figure-description").text = (
    "Proposed, unvalidated framework. Reuse official VideoJev-4B Cached visual context; "
    "L1 scores uniform windows on five 0–5-or-unknown value questions, L2 merges same-event "
    "windows and rescores events, evidence checks and boundary correction precede L3 "
    "same-type comparison. Missing evidence invokes existing records first and then, "
    "within budget, new frames or external audio, ASR and OCR tools. Evidence updates "
    "return to the triggering judgment. Final duration-bounded clips differ from evidence windows."
)
defs = element(root, "defs")
for key in ("line", "blue", "teal", "amber", "green", "purple"):
    marker = element(defs, "marker", id=f"arrow-{key}", viewBox="0 0 10 10", refX=9,
                     refY=5, markerWidth=8, markerHeight=8, orient="auto-start-reverse", markerUnits="userSpaceOnUse")
    element(marker, "path", d="M 0 0 L 10 5 L 0 10 Z", fill=color(key))
rect(root, 0, 0, W, H, "white", radius=0)

header = group(root, "title-and-design-status")
text(header, 50, 83, "HighlightJEV：分层价值判断与证据驱动的高光定位", 49, weight=700)
text(header, 50, 133, "等长窗口 → 完整事件 → 同类比较；证据不足时定向补充，按时长预算输出", 30, "muted")
text(header, 2550, 80, "v5 · 方案设计 / 待验证", 27, "muted", anchor="end")
line(header, 50, 160, 2550, 160, "border")

context = group(root, "shared-official-cached-context")
rect(context, 50, 190, 2500, 150, "blue_fill", "blue_edge", 18)
text(context, 80, 236, "全片采样帧＋真实时间", 30, weight=700)
for i in range(4):
    x = 83 + i*84
    rect(context, x, 260, 70, 48, "white", "blue_edge", 6)
    element(context, "polygon", points=f"{x+7},300 {x+24},277 {x+38},291 {x+48},282 {x+63},300",
            fill="#9BBCC6")
arrow(context, "M 454 269 H 524", "blue")
text(context, 554, 237, "VideoJev-4B · 官方 Cached", 34, "blue", 700)
text(context, 554, 284, "视觉编码 → 视频前缀预填充 → 独立问题分支", 29)
text(context, 554, 321, "复用注意力 KV 与卷积 / 循环状态", 25, "muted")
line(context, 1375, 211, 1375, 320, "blue_edge")
text(context, 1415, 237, "每题绑定目标时间段；共享全片视觉上下文", 30, weight=600)
text(context, 1415, 281, "输出时长预算与计算预算分别设置", 29)
text(context, 1415, 319, "已选 4B 的音频 / ASR / OCR 由外部工具按需补充", 25, "muted")
text(root, 50, 385, "主流程", 27, "muted", 600)
text(root, 2550, 385, "后续 QA 共用缓存；新增局部帧另建对应上下文", 26, "muted", anchor="end")

l1 = group(root, "level-1-uniform-window-value-scoring")
rect(l1, 50, 410, 500, 440, "teal_fill", "teal_edge", 18)
text(l1, 80, 461, "L1  等长片段初评分", 36, "teal", 700)
text(l1, 80, 505, "完整覆盖时间轴 · 每窗五道题", 28)
labels = ["结果", "信息", "情绪", "动作", "感官"]
fills = ["#B9DCD4", "#C7DDE9", "#EFD3BD", "#E8DCB0", "#D6CFE4"]
for i, label in enumerate(labels):
    text(l1, 176+i*75, 555, label, 26, anchor="middle")
for j, label in enumerate(("W₁", "W₂", "…", "Wₙ")):
    y = 576+j*40
    text(l1, 80, y+25, label, 25, "muted")
    for i, fill in enumerate(fills):
        if j == 2:
            text(l1, 176+i*75, y+24, "⋮", 26, "muted", anchor="middle")
        else:
            rect(l1, 145+i*75, y, 62, 28, fill, radius=4)
text(l1, 80, 771, "0–5 六档＋未知 U", 30, "teal", 700)
text(l1, 80, 815, "保留逐维分数与未知概率", 27, "muted")

l2 = group(root, "level-2-event-assembly-and-rescoring")
rect(l2, 610, 410, 500, 440, "teal_fill", "teal_edge", 18)
text(l2, 640, 461, "L2  合并与事件复评", 36, "teal", 700)
text(l2, 640, 505, "高分＋缺证＋覆盖候选", 28)
for i in range(6):
    fill = "#A7CEC6" if i < 3 else ("#D6E1E5" if i == 3 else "#C2B4D5")
    rect(l2, 643+i*72, 541, 59, 36, fill, radius=5)
arrow(l2, "M 770 592 V 622", "teal")
arrow(l2, "M 1010 592 V 622", "purple")
rect(l2, 643, 640, 205, 49, "#A7CEC6", radius=6)
rect(l2, 927, 640, 133, 49, "#C2B4D5", radius=6)
text(l2, 746, 675, "事件 A", 28, anchor="middle")
text(l2, 994, 675, "事件 B", 28, anchor="middle")
text(l2, 640, 731, "同一事件 / 过程才合并", 28, weight=600)
text(l2, 640, 774, "完整事件重新判断五维价值", 27)
text(l2, 640, 816, "保留父窗口 · 不累加子窗分数", 25, "muted")

check = group(root, "evidence-sufficiency-check")
rect(check, 1170, 410, 630, 150, "amber_fill", "amber_edge", 18)
text(check, 1200, 459, "证据充分性检查", 35, "amber", 700)
text(check, 1200, 505, "支持 / 反证 / 缺证 / 冲突", 29)
text(check, 1200, 543, "事件可见 → 属性成立 → 支持价值判断", 26, "muted")

boundary = group(root, "independent-start-and-end-correction")
rect(boundary, 1170, 625, 630, 225, "amber_fill", "amber_edge", 18)
text(boundary, 1200, 672, "边界修正：分别判断起点与终点", 32, "amber", 700)
line(boundary, 1220, 723, 1746, 723, "border", 5)
rect(boundary, 1350, 707, 275, 32, "#D9B480", radius=5)
line(boundary, 1350, 697, 1350, 748, "amber", 2.4)
line(boundary, 1625, 697, 1625, 748, "amber", 2.4)
path(boundary, "M 1267 723 H 1433", "amber", arrow=True, marker_start="url(#arrow-amber)")
path(boundary, "M 1543 723 H 1707", "amber", arrow=True, marker_start="url(#arrow-amber)")
text(boundary, 1350, 782, "起点 s", 26, anchor="middle")
text(boundary, 1625, 782, "终点 e", 26, anchor="middle")
text(boundary, 1485, 827, "保持 / ±2、4、6 秒 / 未知", 29, anchor="middle")

l3 = group(root, "level-3-same-type-event-comparison")
rect(l3, 1860, 410, 690, 440, "purple_fill", "purple_edge", 18)
text(l3, 1890, 461, "L3  同类事件比较", 36, "purple", 700)
text(l3, 1890, 505, "同类型 · 同标准 · 双方目标片内证据", 29)
rect(l3, 1895, 541, 268, 105, "white", "purple_edge", 12)
rect(l3, 2240, 541, 268, 105, "white", "purple_edge", 12)
text(l3, 2029, 584, "事件 A", 30, weight=600, anchor="middle")
text(l3, 2029, 623, "分级价值＋证据", 25, "muted", anchor="middle")
text(l3, 2374, 584, "事件 B", 30, weight=600, anchor="middle")
text(l3, 2374, 623, "分级价值＋证据", 25, "muted", anchor="middle")
text(l3, 2201, 606, "vs", 30, "purple", 600, "middle")
text(l3, 1890, 704, "A 更优 / B 更优 / 并列 / 缺证", 31, "purple", 600)
text(l3, 1890, 757, "并列须有证据；未知不等于 tie", 28)
text(l3, 1890, 811, "比较影响选片的候选 · 不强迫胜负", 27, "muted")

flow = group(root, "main-flow-connectors")
arrow(flow, "M 550 630 H 610", "teal")
arrow(flow, "M 1110 482 H 1170", "teal")
arrow(flow, "M 1485 560 V 625", "amber")
text(flow, 1510, 602, "充分或停止补证", 23, "muted")
arrow(flow, "M 1800 700 H 1860", "line")

requests = group(root, "shared-evidence-request-bus")
path(requests, "M 1170 520 H 1140 V 920", "amber", dashed=True)
path(requests, "M 1170 795 H 1140", "amber", dashed=True)
path(requests, "M 1970 850 V 920 H 1140", "amber", dashed=True)
dot(requests, 1140, 795, "amber")
dot(requests, 1140, 920, "amber")
arrow(requests, "M 1140 920 H 320 V 1000", "amber", dashed=True)
text(requests, 635, 906, "缺证且有预算 → 共用取证入口", 29, "amber", 600)
text(requests, 1170, 971, "补证后返回触发处，更新分数、边界或比较", 28, "teal")

retrieval = group(root, "evidence-backtracking-and-modality-tools")
rect(retrieval, 50, 1000, 1790, 620, "amber_fill", "amber_edge", 18)
text(retrieval, 80, 1052, "证据回溯与按需多模态", 35, "amber", 700)
text(retrieval, 80, 1095, "先查已有记录，再根据具体缺口访问源媒体", 28, "muted")

gap = group(retrieval, "explicit-evidence-gap")
rect(gap, 90, 1130, 300, 140, "white", "amber_edge")
text(gap, 240, 1177, "当前缺口", 31, weight=700, anchor="middle")
text(gap, 240, 1221, "内容 / 动作 / 归属", 26, anchor="middle")
text(gap, 240, 1255, "明确位置与核查问题", 24, "muted", anchor="middle")

ledger = group(retrieval, "source-linked-evidence-records")
rect(ledger, 460, 1130, 500, 140, "white", "amber_edge")
text(ledger, 490, 1177, "检索已有证据", 31, weight=700)
text(ledger, 490, 1221, "证据 ID · 原视频时间 · 模态", 26)
text(ledger, 490, 1255, "片内 / 上下文 / 对手 · 支持状态", 25, "muted")

update = group(retrieval, "evidence-update-and-return")
rect(update, 1430, 1130, 365, 140, "teal_fill", "teal_edge")
text(update, 1612, 1177, "更新并返回原判断", 29, "teal", 700, "middle")
text(update, 1612, 1221, "保留来源与前后变化", 26, anchor="middle")
text(update, 1612, 1255, "无新证据 / 达上限：保留未知", 22, "muted", anchor="middle")
arrow(retrieval, "M 390 1200 H 460", "amber")
arrow(retrieval, "M 960 1200 H 1430", "teal")
text(retrieval, 1190, 1183, "已有证据可用", 28, "teal", anchor="middle")
arrow(retrieval, "M 710 1270 V 1350", "amber", dashed=True)
text(retrieval, 745, 1335, "仍缺证＋有预算", 27, "amber", 600)

tools = group(retrieval, "on-demand-external-modalities")
rect(tools, 440, 1350, 920, 150, "white", "amber_edge", 15)
tool_data = [
    (460, "加密新帧", "瞬时动作 / 细节", "blue_fill", "blue_edge"),
    (685, "音频分析", "欢呼 / 强度 / 归属", "purple_fill", "purple_edge"),
    (910, "ASR", "发言 / 解说内容", "green_fill", "green_edge"),
    (1135, "OCR", "比分 / 文字变化", "blue_fill", "blue_edge"),
]
for i, (x, title, subtitle, fill, edge) in enumerate(tool_data):
    g = group(tools, f"evidence-tool-{i}")
    rect(g, x, 1370, 205, 120, fill, edge)
    text(g, x+102.5, 1415, title, 29, weight=700, anchor="middle")
    text(g, x+102.5, 1463, subtitle, 21, "muted", anchor="middle")
arrow(retrieval, "M 1360 1430 H 1612 V 1270", "teal")
text(retrieval, 1415, 1485, "写回证据与状态", 25, "teal")
text(retrieval, 90, 1386, "按需取证", 28, "amber", 600)
text(retrieval, 90, 1432, "不只检查视觉高分", 24)
text(retrieval, 90, 1470, "保留覆盖与声音线索", 24)
text(retrieval, 460, 1540, "外部工具结果带来源接入；新增帧不直接插入旧缓存", 26, "muted")
line(retrieval, 80, 1565, 1810, 1565, "amber_edge")
text(retrieval, 90, 1605, "来源链示意：传球 → 射门 → 进球 → 反应；时间相邻不自动证明因果", 27)

selection = group(root, "duration-constrained-highlight-output")
rect(selection, 1900, 1030, 650, 590, "green_fill", "green_edge", 18)
arrow(selection, "M 2220 850 V 1030", "green")
text(selection, 2250, 971, "候选与修正边界", 26, "green")
text(selection, 1935, 1084, "预算选片与输出", 36, "green", 700)
text(selection, 1935, 1130, "去重 · 事件覆盖 · 核心片段优先", 28)
for x, label in ((1940, "5 s"), (2115, "10 s"), (2290, "1 min")):
    pill(selection, x, 1164, 150, label, "white", "green_edge", "green", 29)
text(selection, 1935, 1260, "输出总时长 ≤ 用户预算", 32, "green", 700)
text(selection, 1935, 1310, "按时间顺序组织，保留证据引用", 28)
text(selection, 1935, 1393, "取证", 26, "muted")
line(selection, 2030, 1383, 2500, 1383, "blue_edge", 15)
text(selection, 1935, 1453, "输出", 26, "green")
line(selection, 2030, 1443, 2500, 1443, "border", 3)
rect(selection, 2080, 1425, 140, 36, "#89B498", radius=5)
rect(selection, 2330, 1425, 100, 36, "#89B498", radius=5)
text(selection, 1935, 1526, "查证范围可以大于最终保留范围", 28, weight=600)
text(selection, 1935, 1577, "输出区间＋价值向量＋来源轨迹", 27, "muted")

footer = group(root, "legend-and-method-boundary")
line(footer, 50, 1660, 2550, 1660, "border")
line(footer, 50, 1700, 107, 1700, "line", 3)
text(footer, 121, 1709, "主流程", 25, "muted")
line(footer, 255, 1700, 312, 1700, "amber", 3, stroke_dasharray="10 8")
text(footer, 326, 1709, "条件取证", 25, "muted")
line(footer, 505, 1700, 562, 1700, "teal", 3)
text(footer, 576, 1709, "证据复用 / 更新", 25, "muted")
text(footer, 2550, 1709, "复用开源模型；分级标准、工具调度与完整闭环尚待验证", 25, "muted", anchor="end")

out = HERE / "highlightjev_agent_framework_v5.svg"
ET.ElementTree(root).write(out, encoding="utf-8", xml_declaration=True)
print(out)
