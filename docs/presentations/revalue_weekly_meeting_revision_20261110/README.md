# ReVALUE 会议对照修订版：2026年11月3日至11月9日

[下载16页可编辑PPT](../ReVALUE_实验进度汇报_2026-11-03至11-09_会议对照修订版.pptx) · [会议对照修订报告](../../revalue_weekly_progress_2026-11-03_to_2026-11-09_meeting_revision.md) · [逐页讲稿](notes/total.md) · [封面预览](exports/preview_cover.png)

按“上次会议问题—本周验证—结论与卡点—下一步决定”组织，包含4个原生图表、2个原生表格、16页讲稿备注和2页真实输入帧案例。图表与表格均可在PowerPoint中编辑，图表包含4个内嵌数据工作簿。

## 结果与时间范围

固定40视频上，F-local、普通C、旧V15、修复V15的Top-5 mAP为57.5828、58.4573、58.4085、57.6496；密集视觉Direct为58.4767。事实改进缩小差距，但记忆与详细价值均未确认稳定优势。案例的视觉解释来自助手审阅，尚非独立人工语义真值。

SVHighlights七视频8B结果已完成。十四视频27B扩测按11月9日23:37的周报快照列为进行中，不能当作11月10日实时进度。按需五维、定向回看和ASR是待验证建议；本次制作和推送未启动或干预实验。

## 源文件与验证

- [页面源文件](svg_output/)与[自包含SVG预览](svg_final/)。
- [设计方案](design_spec.md)、[设计约定](spec_lock.md)、[归档来源](sources/)、[实际输入帧联系表](images/)。
- [页面质量检查](validation/svg_quality_report.json)：16页全部通过，0错误、0警告。
- [图表坐标核验](validation/chart_geometry_verification.json)：4个图表共30个数据标记，最大坐标误差小于0.001像素。
- [原始交付收据](validation/delivery_receipt.json)及[导出检查](validation/revalue_weekly_meeting_revision_20261110_003155_native_charts_tables.report.json)。收据中的项目别名表示本地来源位置。

发布副本把机器路径替换为项目别名，并把可发布报告、讲稿和帧资料转为仓库内链接。原始预测、失败与账本、完整视频、模型和其他缓存继续保留本地。临时服务、运行锁、重复PPT和备份不属于交付内容；同周期初稿保留其原始版本。
