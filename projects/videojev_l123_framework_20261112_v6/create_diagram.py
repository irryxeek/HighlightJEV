#!/usr/bin/env python3
"""Generate the editable HighlightJEV L1/L2/L3 design diagram; no inference."""

from pathlib import Path
from xml.etree import ElementTree as ET


HERE = Path(__file__).resolve().parent
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
W, H = 2600, 1400
C = {
    "ink": "#203A4C", "muted": "#586F7C", "line": "#526D7B",
    "border": "#D6E1E5", "white": "#FFFFFF",
    "blue": "#3D7693", "blue_fill": "#EAF3F8", "blue_edge": "#B0CDDC",
    "teal": "#237D7F", "teal_fill": "#EAF5F3", "teal_edge": "#B0D4CD",
    "purple": "#71678F", "purple_fill": "#F1EFF7", "purple_edge": "#CBC5DD",
    "green": "#477D64", "green_fill": "#EEF5EE", "green_edge": "#BCD4BF",
}


def el(parent, tag, **attrs):
    return ET.SubElement(parent, f"{{{SVG}}}{tag}", {
        k.replace("_", "-"): str(v) for k, v in attrs.items()
    })


def color(value):
    return C.get(value, value)


def group(parent, name):
    return el(parent, "g", id=name)


def rect(parent, x, y, w, h, fill="white", stroke="none", radius=12, **kw):
    return el(parent, "rect", x=x, y=y, width=w, height=h, rx=radius,
              fill=color(fill), stroke=color(stroke), stroke_width=2, **kw)


def txt(parent, x, y, value, size=30, fill="ink", weight=400, anchor="start", **kw):
    node = el(parent, "text", x=x, y=y, font_family="Noto Sans CJK SC, sans-serif",
              font_size=size, font_weight=weight, fill=color(fill), text_anchor=anchor, **kw)
    node.text = value
    return node


def path(parent, d, stroke="line", width=3.2, arrow=False, **kw):
    if arrow:
        kw["marker_end"] = f"url(#arrow-{stroke})"
    return el(parent, "path", d=d, stroke=color(stroke), fill="none",
              stroke_width=width, stroke_linecap="round", stroke_linejoin="round", **kw)


def pill(parent, x, y, w, h, value, accent, size=29):
    rect(parent, x, y, w, h, "white", accent + "_edge", radius=8)
    txt(parent, x + w / 2, y + h / 2 + size * 0.34, value,
        size=size, fill=accent, weight=500, anchor="middle")


def main():
    root = ET.Element(f"{{{SVG}}}svg", {
        "width": "280mm", "height": f"{280 * H / W:.6f}mm",
        "viewBox": f"0 0 {W} {H}", "version": "1.1",
    })
    el(root, "title").text = "HighlightJEV：L1–L2–L3 分层高光流水线"
    el(root, "desc").text = (
        "Proposed visual-only pipeline: official VideoJev-4B Cached prefix feeds "
        "independent window scoring, bounded event merging/rescoring, and limited "
        "comparable-pair reranking. A deterministic program selects intervals under "
        "a playback budget. All shapes are schematic, not experiment results."
    )
    defs = el(root, "defs")
    for name in ("line", "blue", "teal", "purple", "green"):
        marker = el(defs, "marker", id="arrow-" + name, markerWidth=10,
                    markerHeight=8, refX=8.5, refY=4, orient="auto",
                    markerUnits="userSpaceOnUse")
        el(marker, "path", d="M 0 0 L 9 4 L 0 8 Z", fill=color(name))
    rect(root, 0, 0, W, H, radius=0)

    header = group(root, "title-and-scope")
    txt(header, 50, 83, "HighlightJEV：L1–L2–L3 分层高光流水线", 49, weight=700)
    txt(header, 50, 138, "窗口五维评分 → 事件合并复评 → 同类候选比较 → 预算选片", 31, "muted")
    txt(header, 2550, 85, "v6 · 精简首版 / 设计待验证", 27, "muted", anchor="end")
    path(header, "M 50 165 H 2550", "border", 2)

    context = group(root, "shared-video-context")
    rect(context, 50, 195, 2500, 165, "blue_fill", "blue_edge", radius=18)
    txt(context, 80, 242, "全片采样帧＋真实时间 PTS", 31, weight=700)
    frames = group(context, "schematic-frame-sequence")
    for i in range(4):
        x = 82 + i * 98
        rect(frames, x, 264, 82, 61, "white", "blue_edge", radius=6)
        el(frames, "path", d=f"M {x+9} 314 L {x+29} 284 L {x+46} 303 L {x+59} 292 L {x+74} 314 Z",
           fill="#9BBBC9")
    path(context, "M 515 290 H 607", "blue", arrow=True)
    txt(context, 644, 245, "VideoJev-4B · 官方 Cached", 37, "blue", 700)
    txt(context, 644, 291, "视觉编码 → 视频前缀预填充", 30)
    txt(context, 644, 334, "复用注意力 KV 与卷积 / 循环状态", 27, "muted")
    path(context, "M 1448 218 V 337", "blue_edge", 2)
    txt(context, 1490, 245, "同一全片视觉输入 · 每题绑定目标时间段", 32, weight=700)
    txt(context, 1490, 292, "各题独立使用前缀，不继承前题答案", 30)
    txt(context, 1490, 334, "缓存复用后，每个新问题仍需计算", 27, "muted")

    shared = group(root, "shared-prefix-to-three-layers")
    path(shared, "M 1300 360 V 414", "blue", 2.8)
    path(shared, "M 440 414 H 2160", "blue", 2.8)
    for x in (440, 1300, 2160):
        path(shared, f"M {x} 414 V 463", "blue", 2.8, arrow=True)
        el(shared, "circle", cx=x, cy=414, r=4.3, fill=color("blue"))
    txt(shared, 60, 409, "共享视觉上下文", 26, "blue")

    l1 = group(root, "l1-uniform-window-scoring")
    rect(l1, 50, 465, 780, 560, "teal_fill", "teal_edge", radius=18)
    txt(l1, 82, 522, "L1 等长窗口评分", 40, "teal", 700)
    txt(l1, 82, 570, "覆盖全时间轴 · 每窗五道选择题", 30)
    matrix = group(l1, "five-value-probability-matrix")
    labels = ["结果", "信息", "情绪", "动作", "感官"]
    fills = ["#B6DBD2", "#BFD9E6", "#EED2BC", "#E8DBAC", "#D4CCE5"]
    for j, (label, fill) in enumerate(zip(labels, fills)):
        x = 180 + j * 122
        txt(matrix, x + 50, 632, label, 30, anchor="middle")
        for y in (654, 710, 798):
            rect(matrix, x, y, 100, 35, fill, radius=5)
        txt(matrix, x + 50, 781, "⋮", 31, "muted", anchor="middle")
    for y, label in ((682, "W₁"), (738, "W₂"), (781, "⋮"), (826, "Wₙ")):
        txt(matrix, 98, y, label, 30, "muted")
    txt(l1, 82, 886, "0–5 六档＋未知 U", 36, "teal", 700)
    txt(l1, 82, 933, "每维 Top-K 并集＋固定时间覆盖", 29)
    txt(l1, 82, 982, "保留概率；未知候选按固定规则保留", 27, "muted")

    l2 = group(root, "l2-event-merging-and-rescoring")
    rect(l2, 910, 465, 780, 560, "teal_fill", "teal_edge", radius=18)
    txt(l2, 942, 522, "L2 事件合并与复评", 40, "teal", 700)
    txt(l2, 942, 570, "邻接候选 → 合并判断 → 重新评分", 30)
    merge = group(l2, "bounded-merge-example")
    for i in range(6):
        fill = "#A6CEC5" if i < 3 else ("#D6E1E5" if i == 3 else "#C2B4D5")
        rect(merge, 960 + 108 * i, 620, 90, 40, fill, radius=5)
    path(merge, "M 960 674 V 686 H 1266 V 674", "teal", 2.5)
    path(merge, "M 1113 686 V 727", "teal", arrow=True)
    path(merge, "M 1329 674 V 727", "line", arrow=True)
    path(merge, "M 1392 674 V 686 H 1590 V 674", "purple", 2.5)
    path(merge, "M 1491 686 V 727", "purple", arrow=True)
    rect(merge, 960, 734, 306, 61, "#A6CEC5", radius=7)
    rect(merge, 1284, 734, 90, 61, "#D6E1E5", radius=7)
    rect(merge, 1392, 734, 198, 61, "#C2B4D5", radius=7)
    txt(merge, 1113, 775, "事件候选 A", 30, anchor="middle")
    txt(merge, 1329, 774, "原窗", 25, "muted", anchor="middle")
    txt(merge, 1491, 775, "候选 B", 30, anchor="middle")
    txt(l2, 942, 850, "同一连续事件才合并；未知不合并", 30, weight=500)
    txt(l2, 942, 894, "合并区间再做五维 0–5＋U", 32, "teal", 700)
    txt(l2, 942, 938, "保留子窗，不累加旧分数", 29)
    txt(l2, 942, 982, "复评提示隐藏 L1 分数与排名", 27, "muted")

    l3 = group(root, "l3-limited-comparable-pair-reranking")
    rect(l3, 1770, 465, 780, 560, "purple_fill", "purple_edge", radius=18)
    txt(l3, 1802, 522, "L3 同类候选比较", 40, "purple", 700)
    txt(l3, 1802, 570, "共同标准 · 固定候选对 · 双向复核", 30)
    rect(l3, 1810, 612, 270, 101, "white", "purple_edge", radius=10)
    rect(l3, 2240, 612, 270, 101, "white", "purple_edge", radius=10)
    txt(l3, 1945, 654, "候选 A", 32, weight=700, anchor="middle")
    txt(l3, 1945, 693, "目标区间", 26, "muted", anchor="middle")
    txt(l3, 2375, 654, "候选 B", 32, weight=700, anchor="middle")
    txt(l3, 2375, 693, "目标区间", 26, "muted", anchor="middle")
    txt(l3, 2160, 650, "A/B", 27, "purple", anchor="middle")
    path(l3, "M 2110 665 H 2210", "purple", 2.5, arrow=True)
    path(l3, "M 2210 687 H 2110", "purple", 2.5, arrow=True)
    txt(l3, 2160, 727, "B/A", 27, "purple", anchor="middle")
    pill(l3, 1810, 754, 335, 51, "A 更值得保留", "purple")
    pill(l3, 2175, 754, 335, 51, "B 更值得保留", "purple")
    for x, label in ((1810, "相当"), (2050, "不可比"), (2290, "未知")):
        pill(l3, x, 825, 220, 51, label, "purple")
    txt(l3, 1802, 936, "两向确认同一赢家才改序", 34, "purple", 700)
    txt(l3, 1802, 982, "相当、弃判或冲突：保留 L2 顺序", 28, "muted")

    flow = group(root, "forward-candidate-flow")
    path(flow, "M 830 710 H 908", "line", 3.8, arrow=True)
    path(flow, "M 1690 710 H 1768", "line", 3.8, arrow=True)
    path(flow, "M 2160 1025 V 1118", "green", 3.8, arrow=True)
    txt(flow, 2200, 1080, "区间与顺序", 28, "green")
    txt(flow, 50, 1082, "三层使用同一帧池；后续判断不读取此前分数或理由", 29, "muted")

    output = group(root, "deterministic-budget-selection")
    rect(output, 50, 1120, 2500, 175, "green_fill", "green_edge", radius=18)
    txt(output, 82, 1175, "预算选片与输出", 40, "green", 700)
    txt(output, 82, 1223, "固定程序：去重 → 选片 → 时间顺序", 29)
    txt(output, 82, 1267, "保留原区间与子窗；不做细边界搜索", 27, "muted")
    timeline = group(output, "schematic-output-timeline")
    txt(timeline, 910, 1172, "选中片段按原视频时间输出", 28, "green")
    path(timeline, "M 910 1222 H 1710", "green_edge", 8)
    for x, width in ((952, 161), (1260, 125), (1517, 144)):
        rect(timeline, x, 1202, width, 40, "#8CB59B", radius=5)
    txt(timeline, 910, 1270, "时间区间＋价值向量＋未知状态", 26, "muted")
    path(output, "M 1844 1146 V 1268", "green_edge", 2)
    txt(output, 1910, 1185, "总播放时长 ≤ B", 41, "green", 700)
    txt(output, 1910, 1234, "B：5 秒 / 10 秒 / 1 分钟等", 29)
    txt(output, 1910, 1270, "不要求凑满预算", 26, "muted")

    footer = group(root, "scope-and-legend")
    path(footer, "M 50 1330 H 2550", "border", 2)
    path(footer, "M 50 1364 H 104", "blue", 2.8, arrow=True)
    txt(footer, 122, 1374, "共享缓存", 25, "muted")
    path(footer, "M 292 1364 H 346", "line", 3.8, arrow=True)
    txt(footer, 364, 1374, "候选流转", 25, "muted")
    txt(footer, 630, 1374, "选择题概率输出；无需生成中间证据或理由", 25, "muted")
    txt(footer, 2550, 1374, "色块为结构示意 · 精简设计 / 尚未实测", 25, "muted", anchor="end")

    target = HERE / "highlightjev_l123_framework_v6.svg"
    for i, node in enumerate(root.iter(f"{{{SVG}}}text"), 1):
        node.set("id", f"label-{i:03d}")
    ET.indent(root)
    ET.ElementTree(root).write(target, encoding="utf-8", xml_declaration=True)
    print(target)


if __name__ == "__main__":
    main()
