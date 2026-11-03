# REZE Direct：固定 QV100 执行记录

日期：2026-10-30。本文为启动快照；最终状态以运行目录的 `campaign_exit.json`、`evaluation_complete.json` 和结果报告为准。

**已完成（2026-10-30 18:13，北京时间）：100/100 请求、零重试，98条非空区间、2条零长度输出计零。完整100条 R1@0.5 / @0.7 为39% / 30%，MR mAP为26.48。** [完整结果报告](reze_direct_grounding_qv100_results_2026-10-30.md)包含与旧42% / 28%的同样本对比。以下启动记录按阶段保留。

用户要求将自定义 Direct 换成 REZE 的 Direct 基线并运行100条。保持此前冻结的完整100条 train 样本、模型与视频，改为 REZE 的整视频多区间提示、128 token 贪心生成和归一化解析；采用2 FPS、原生时间信息，本地空间尺寸沿用512×320外框。没有运行REZE密集Yes/No扫描或Agent模块。

- [初始协议 v1](reze_direct_grounding_qv100_protocol_v1_2026-10-30.md)
- [兼容性修订 v1.1](reze_direct_grounding_qv100_protocol_v1_1_2026-10-30.md)
- 代码：`experiments/reze_direct_grounding/`。
- v1.1 启动目录：`$ZEROSHOT_ARTIFACT_ROOT/reze_direct_grounding_qv100_v1_1_2026-10-30/`（启动失败，见下方修订）。
- 初始失败保留：`$ZEROSHOT_ARTIFACT_ROOT/reze_direct_grounding_qv100_v1_2026-10-30/`。

CPU已准备100/100，真实AutoProcessor与独立时间token展开逐条一致；全量最大请求预留2,316,827 token，最小context余量8,601 token；10项CPU测试通过。源码、输入、输出契约、评价源码和原样本清单均已冻结。

v1在发出第一个模型请求之前遇到vLLM 0.12对UUID格式设备列表的不兼容，保留0请求、0token、1次启动、24.407798650005134 GPU秒。v1.1改用经PCI/NVML顺序和运行时UUID核对的数字设备编号，直接复用全部准备帧和输入，不重采样。

独立边界为100次尝试、零重试、3,276,800 token、累计6000 GPU秒，同时最多两张空闲卡；累计启动上限11，包含原失败启动及10个正式冷worker。旧QV、TVSum和Direct账本不转移。新推理最初使用GPU4、5；每批重新核验资源，只清理所属进程组。

主指标为完整100分母的MR mAP、首个有效区间R1@0.5/0.7；best-of-K召回单列。旧Direct通过相同AP内核离线补算。原论文未完整公开Qwen3视觉尺寸/抽帧相位/Direct排名分数，本轮明确记为协议重建；同样本整套方案对照不能归因于某一个改动。本轮不推送。

## v1.2 续接记录

v1.1 在模型初始化检查时发现每卡 2 GiB KV 缓存不足以容纳 32768 上下文；按实际模型配置计算需要 2.25 GiB。此失败发生在第一个预测请求之前，消耗 96.54114510599175 GPU 秒。与 v1 合计 0 请求、0 token、2 次失败启动、120.94894375599688 GPU 秒，失败记录均保留。

[v1.2 协议](reze_direct_grounding_qv100_protocol_v1_2_2026-10-30.md)将每卡 KV 容量设为 3 GiB，新增容量契约测试，11 项 CPU 测试通过。全部100条帧、真实 PTS、提示、解码和评价仍使用冻结输入；没有重采样或请求重试。累计启动上限为12（两次启动失败及10个正式冷worker），100次请求、token及GPU总额上限不变，携带全部失败成本。

实际推理目录：`$ZEROSHOT_ARTIFACT_ROOT/reze_direct_grounding_qv100_v1_2_2026-10-30/`。本段记录成功进入推理；完整结果须以该目录终态收据与后续结果报告为准。

## 终态收据

v1.2完成100次请求，2,306,138 token；累计4,312.483284707967 GPU秒（包含两次启动失败），12次worker启动。十个正式worker均退出0、无所属残留进程。CPU评价完成后原账本哈希不变，210个受保护历史文件未改变。结果包保存至 `comparisons/qwen_direct/reze_direct_grounding_qv100_2026-10-30/`，未推送。
