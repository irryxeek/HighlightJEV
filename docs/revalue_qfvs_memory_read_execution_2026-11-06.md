# QFVS 40查询记忆读取对照：启动记录

## Material Passport

- Origin Skill / Mode：academic-research-suite / experiment-agent，run + validate。
- Version：qfvs_memory_read_40q_v1；2026-11-06。
- Verification Status：CPU准备与源码审查通过，模型推理进行中；尚无本轮完整效果结论。

## 实验范围

用户确定每视频10个query，P01–P04共40条。比较D（无文本记忆）、F（旧读取）、F-read（新读取）。每视频建一次共享事实库，32次建库后完成120次选片；并非QFVS全180查询测试。

保留原生5秒shot、2%摘要长度和语义匹配F1。三组相同84候选及旧帧，主比较F-read−F固定同库、模型、帧、预算和任务提示，仅改变读取内容及活动引用ID。固定完整40分母，失败/弃权用冻结B0回退并单列。详细边界见同目录`revalue_qfvs_memory_read_protocol_2026-11-06.md`。

## 已完成检查

- 40条B0均由旧缓存原始概率重导一致；未重跑REZE。
- 4视频输入像素与真实PTS对旧完整窗口记录核验一致。
- 30项合成CPU测试通过，包括输出契约、原生5秒读取、全分母评价、四视频cluster统计、进程归属及异常退出记录。
- native schema 8组合通过，普通ASCII120字符可生成、121被拒，允许合法弃权。原生长度限制不再与正则混用；早期CPU探针失败保留在preflight_schema_v0。未用CPU检查伪造模型输出。
- 最大预留上下文21,314 / 32,768；905字节容量检查仅针对规范JSON写法，不保证任意等价转义都不截断；实际超限仍按invalid完整分母处理。
- 输入契约生产脚本、全部源码、模型环境、预算和旧文件哈希已冻结；另一个原生审查agent确认无阻断启动问题，未读真实GT或实验成绩。

## 执行状态

北京时间2026-11-06 14:19启动后台监督器，14:20模型就绪并派发首个建库请求；使用空闲GPU 0–3，Qwen3.8-27B / BF16 TP4。监督器PID为31493，worker PID为31588；PID只是当时快照，后续以进程身份/状态收据为准。

本轮最多152次、零重试，一个worker；token预留2,588,659，worker主生命周期10,800秒、退出余量60秒（四卡累计生命周期上限43,440 GPU秒）。独立记账，不挪用旧额度。异常停止新派发；仅清理确认属于本次的进程。结束后自动CPU评价并保存结果。

运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_qfvs_memory_read_40q_27b_v1_2026-11-06`。查看`status.json`、`ledger.json`、`heartbeat.json`、`worker_0/worker.log`。最终预计生成`evaluation.json`、`complete.json`以及项目`docs/revalue_qfvs_memory_read_results_2026-11-06.md`；此启动记录不表示结果已经生成。

本轮没有推送、安装依赖、改写旧预测或启动其它数据集实验。
