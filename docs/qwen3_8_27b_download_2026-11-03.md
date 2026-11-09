# Qwen3.8-27B 权重下载记录

2026-11-03，用户要求下载 Qwen3.8 的 8B / 27B 权重。核对官方公开目录后，未找到 Qwen3.8-8B；用户随后明确选择“先下载 27B，8B 暂缓”。本轮只下载，不启动推理、加载权重或修改实验环境。

## 模型与来源

- 官方仓库：[Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)。
- 固定 revision：`1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`。
- 原始、非量化 BF16；18 个 safetensors 权重分片，包含配置、tokenizer、图像/视频 processor 和许可证共 32 个文件，总计 55,586,114,863 字节，约 55.6 GB。
- 官方配置中的架构名为 `Qwen3_5ForConditionalGeneration`、`model_type=qwen3_5`；这是 Qwen3.8-27B 自身公布的配置，不表示下载了另一个模型。
- 权重可经 Qwen 官方 ModelScope 仓库传输；最终接受标准为上述 Hugging Face 固定 revision 的文件尺寸及哈希。未使用第三方量化或蒸馏版本。

## 路径与执行

- 权重目录：`$SHARED_DATA_ROOT/MemDreamer/models/Qwen3.8-27B/`。
- 下载状态、日志、来源清单及完成凭证：`$SHARED_DATA_ROOT/MemDreamer/models/.downloads/Qwen3.8-27B/`。
- 维护脚本：download_qwen3_8_27b.py（本地资料：`$MERIT_ROOT/scripts/download_qwen3_8_27b.py`）；实际后台运行采用下载审计目录中的冻结副本。
- 启动时间：2026-11-03 18:38:02（北京时间）；启动 PID 9798 是当时快照，不能当作长期有效进程标识。
- 下载支持断点续传，使用独占锁避免重复任务。网络重试仅针对文件传输，不是实验模型重试。

## 完成标准

18 个权重分片和全部配套文件下载后，逐文件比对上游 LFS SHA-256 或 Git blob SHA-1，核对权重索引与模型配置。全部通过才生成 `complete.json` 和权重目录中的 `download_receipt.json`。文件存在或磁盘占用增长不代表完成校验。

本文是下载启动记录。实时状态查看 `status.json`，最终完成以 `complete.json` 为准；不要因本文仍为启动记录而重复下载。

本轮实验模型调用、实验 token、GPU 分配、推理 worker 均为 0。原 8B / 32B 权重、实验账本和预测保留；未启动任何实验，未推送远程。
