# Mr.HiSum 40视频记忆读取实验启动记录

## Material Passport

- Origin Skill / Mode：academic-research-suite / experiment-agent，run + validate。
- 状态：已启动后台推理，结果尚未生成；本文件是启动快照。
- 用户授权：在TVSum和Mr.HiSum测试，Mr.HiSum选择40视频（约440次建库与选片）。

## 本次范围

固定历史清单前40视频，每视频8次共享建库、D/F/F-read各一次选片，最多440次、零重试。三组均用Qwen3.8-27B，F和F-read共用同一事实库，唯一差别是读取策略及对应事实ID集合。候选、模型、原像素/PTS、任务提示和token上限相同。输入为64全局旧帧与候选旧帧，去重后77–83帧；没有缩图、换样本或新增回看。

Mr.HiSum使用原生5秒建议网格、完整1秒分数导出，再评价mAP50、mAP15与KTS/15%摘要F1。保留原8B REZE B0、B0_5s_flat和Constant CPU对照。五个建议不等于最终摘要长度；失败/弃权回退B0_5s_flat，保留全部40分母。

## 启动前验证

- 历史B0从缓存概率重建一致；所用旧窗口resize后RGB、raw/effective PTS与冻结轨迹一致。
- 440个请求定义；261个grammar通过；最大预留context 41036/49152。
- 20个合成CPU测试通过；独立源码审查通过。
- 发现并修复评价环境缺少默认h5py导入：仅给CPU子进程设置已有安装路径。真实内存HDF5读写、版本与来源哈希检查通过；没有安装依赖或读取真实GT。
- 预测将先完整冻结，再由独立CPU进程读取GT评价。

## 后台执行与记账

- 启动时间UTC：2026-11-06T09:12:26.953626+00:00（北京时间17:12，2026-11-06）。
- GPU：[0, 1, 2, 3]，TP=4；监督器PID 60555。
- 本次独立请求上限440；token预留上限4,497,048；worker上限1、墙钟上限21600秒、GPU生命周期含清理上限86640秒。
- 任一runtime/OOM错误停止，不自动重试；只有本轮身份核验通过的子进程可被清理。
- 初步预计4–5小时，实际耗时以账本和worker生命周期收据为准。
- 终端断开不影响监督器；自动CPU评价和Markdown报告已接入。
- 没有挪用任何旧实验额度，也没有推送远程。

## TVSum复用结果

已核验315项历史输入/结果哈希，原40视频读取对照未重复运行或重算评价。Top-5 mAP：B0 53.2858、D 54.9161、F 52.6220、F-read 54.4187、FV 50.6473；F-read−F为+1.7967pp，95%配对区间[-0.7540,4.3780]，尚不能据此确认稳定增益。旧TVSum本轮零新增调用。

## 产物和查询进度

- [正式协议](revalue_mrhisum_memory_read_protocol_2026-11-06.md)。
- [当前价值提示说明](highlight_value_prompt_current_2026-11-06.md)。
- 运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_mrhisum_memory_read_40v_27b_v1_2026-11-06`。
- 进度：`status.json`、`ledger.json`、`heartbeat.json`；日志：`worker_0/worker.log`。
- 自动收尾产物：`evaluation.json`、`complete.json`、`report.md`，以及项目`docs/revalue_mrhisum_memory_read_results_2026-11-06.md`。这些结果尚未完成，不把预计路径当已有结果。
- 源码manifest SHA256：`4779b7258da366e6886a62122f3a1d25ad99996a8448b5437897c36c939ab00d`。
