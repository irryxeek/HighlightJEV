# VideoJev-4B 高光检测 Agent 框架图 · 优化版

根据 2026-11-12 的方案讨论与框架图反馈绘制。本图表达**待实现与验证的概念方案**，不代表完成了缓存适配、价值评分或 Agent 实验。上一版保留在研究工作区，本目录交付优化版。

## 文件与编辑

- `videojev_agent_framework_v2.svg`：主编辑源。模块、文本、矩阵与箭头均为原生矢量对象，按功能分组，可使用 Inkscape 等工具编辑。
- `videojev_agent_framework_v2.pdf`：180 × 91.8 mm 的矢量 PDF，用于论文或报告。
- `videojev_agent_framework_v2.png`：3000 × 1530 像素预览。
- `create_diagram.py`：仅依赖 Python 标准库的 SVG 生成程序。重新运行会覆盖对 SVG 的手动编辑。

## 相对上一版的调整

1. 主流程合并成四个阶段：全片上下文、五维 QA 初评分、Agent 候选细化、预算选片。
2. 用“时间窗 × 五维”的矩阵展示输出结构，明确每窗有五个判断问题，随后按固定规则融合。矩阵颜色仅标识维度，不表示实际得分或实验结果。
3. 将回看收进 Agent 区域：候选细化 → 补证判断 → 定向回看 → 局部再评分 → 候选更新，使用短连线表示可选闭环。
4. 分开显示计算预算和输出时长预算，统一字号、模块间距与颜色，压缩原版的大面积留白。

## 阅读与科学边界

- **上下文缓存**：指采样覆盖全时间轴的共享视觉上下文；不等于读取每一帧，也不等于生成一份自然语言背景摘要。语言前缀缓存的实际工程适配仍待实现，图中没有宣称现有入口已支持。
- **五维 QA**：结果、信息、情绪、动作、感官。问题显式绑定目标时间段，选项为 0、1、2、未知，保留概率。问题总量是 `5n`，不能把批处理或缓存复用等同于“一次前向完成所有判断”。融合规则、未知门槛和实际预算需在实验前冻结。
- **候选细化**：兼顾高分、缺证和时间覆盖；细分时间窗和边界，必要时才比较候选。图中的时间块只解释粗细粒度关系，没有对应真实视频结果。
- **回看**：仅在有明确证据缺口且仍有计算预算时触发。读取源视频新帧、重新编码，再核验受影响的判断；旧缓存不能提供从未读入的新画面。更新后重新检查停止条件，而非无条件无限循环。证据足够或预算用尽时进入选片；未解决的未知状态必须保留，不能伪装成已补足证据。
- **预算选片**：输出总时长不超过用户的 5 秒、10 秒或 1 分钟等要求，去重、合并、考虑事件覆盖，并按时间顺序输出。合并增加的间隔或上下文也要计入时长；具体选择策略仍需验证。

## 再生成

在本目录运行，使用已安装的 Python 3 与 Inkscape：

```bash
python create_diagram.py
inkscape videojev_agent_framework_v2.svg --export-type=png --export-width=3000 --export-filename=videojev_agent_framework_v2.png
inkscape videojev_agent_framework_v2.svg --export-type=pdf --export-filename=videojev_agent_framework_v2.pdf
```

## 导出检查

已打开最终 PNG 和按 180 mm 页宽渲染的 PDF 复查，核对主流程、回看方向、文字留距与图例；并与 SAM 2 参考图以相近显示宽度比较。修正了出口标注与 Agent 外框相碰的问题。PDF 为单页矢量图，中文及符号字体均已嵌入，无嵌入位图；SVG 保留 68 个文本对象和 17 个语义分组，PNG 非空且未裁边。

内容依据项目内 [HighlightJEV 设计讨论](../../docs/highlightjev_design_discussion_2026-11-11.md) 与后续对话。图稿制作阶段仅修改图稿，没有运行模型或占用 GPU；随后按用户要求同步图稿、说明与相关设计文档。

视觉设计延续上一版的低饱和蓝、青、橙、绿配色。时序输入与反馈回路参考 [SAM 2 Figure 3](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c1f6a8cbf2da59ebf2c802b4f742cd-Paper-Conference.pdf)，矩阵对齐参考 [VGGT Figure 2](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.pdf)。仅借鉴构图关系，所有图形均自行绘制。
