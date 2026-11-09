# ReVALUE 组会汇报：2026年11月3日至11月9日

[下载可编辑 PPTX](../ReVALUE_组会汇报_2026-11-03至11-09.pptx) · [本周总结报告](../../revalue_weekly_progress_2026-11-03_to_2026-11-09.md) · [逐页讲稿](notes/total.md)

共16页：14页主体和2页附录，约15分钟。包含事实与价值记忆设计、TVSum多轮结果、QFVS／Mr.HiSum迁移、V15合法率诊断、两页真实帧案例，以及尚待验证的下一步建议。

PPT内保留3张原生可编辑图表、5张原生表格、16页备注及5张精选证据帧。图表原始数值、备注和外部依赖已完成文件结构检查；结果来自已完成实验，本次整理与发布没有新增模型推理。

## 制作与核验材料

- [页面源文件](svg_output/)与[自包含SVG预览](svg_final/)；后者便于直接查看。
- [版式与内容设计](design_spec.md)、[设计锁定](spec_lock.md)、[归档来源报告](sources/)。
- [证据帧](images/)、[帧来源与像素哈希](analysis/evidence_assets.json)、[图片使用清单](analysis/image_analysis.csv)。
- [交付收据](validation/delivery_receipt.json)、[页面质量检查](validation/svg_quality_report.json)、[图表数值检查](validation/chart_verification.md)。

## 结果与证据边界

固定40视频中，F-local、普通核验、旧V15、修复V15的Top-5 mAP分别为57.5828、58.4573、58.4085、57.6496；尚未确认稳定增益。案例是助手对既有缓存帧的审阅，不能当成独立人工语义真值。下一步48/50合法率属于待验证建议，不是已有结果或启动授权。

发布副本将机器路径替换为项目别名，并将可发布报告改为仓库内链接。原始报告、冻结预测、模型、完整视频和帧缓存保留本地；本目录不是完整实验代码发布，也不包含临时预览服务、备份或重复PPT导出。
