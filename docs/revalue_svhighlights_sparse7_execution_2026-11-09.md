# SVHighlights 稀疏记忆测试执行记录

记录时间：2026-11-09T14:16:19.116730+00:00。状态：已启动，最终状态以运行根目录的 `complete.json` 和 `evaluation.json` 为准。

## 本轮配置

- 七场固定开发视频，约15.84小时，Qwen3-VL-8B-Instruct。
- 每场64个均匀全局时刻，八组生成事实记忆。D/F共用84张选片输入；C/V15共享固定局部帧与事实读取。
- 对照：缓存REZE B0、D、F、F+C、F+V15。最多140次调用，零重试。
- 三路独立单GPU推理，首批为american_football_36、baseball_13、ice_hockey_8，分别使用物理GPU 0、2、3；另四场等待同一调度器分配。
- 16项CPU回归通过，140个预期请求的上下文/schema检查通过；最保守上下文加输出为14634，低于16384。
- CPU审查发现原2GiB KV不足以承载16384上下文，已在启动前调整到2.5GiB；原CPU检查收据和独立引擎复核收据均保留。

## 源码与产物

- manifest SHA256：`c29e5f26253087de914d136fd394aa1a3aab5344780e28b162eec66df958ecb0`。
- 调度器PID：46153。每worker均有独立launch、进程身份、ledger和退出收据。
- 运行根：`$ZEROSHOT_ARTIFACT_ROOT/revalue_svhighlights_sparse7_8b_v1_2026-11-09`。
- 活动状态：`status.json`；每场明细：`workers/<vid>/status.json`、`ledger.json`、`worker.log`。
- 原始提示/输出：`workers/<vid>/requests/`、`records/`；事实库与固定配对单独保存。
- 结束后自动CPU汇总：`evaluation.json`、`results.md`、`complete.json`。
- 报告自动写入项目的 `docs/revalue_svhighlights_sparse7_results_2026-11-09.md`。

## 判断边界

稀疏全局时刻和20个候选的重合很少：五场为0，race为2，volleyball为1。因此本轮主要测试少量全局事实背景是否帮助固定候选选择，不能宣称已构建覆盖全部事件的记忆库。直接观察局部片段依靠各组预先固定的候选图片。

尚无本轮科学结果。旧REZE缓存成本与本轮新增调用分开；全七场进入分母。任何无效核验均保留F，不把证据不足视作反证。未运行视频/技术失败均留下记录，不重新派发。

## Material Passport

沿用已冻结协议与当前F-local/V15契约；CPU只完成输入、输出和资源检查，没有产生模型预测。所有原始视频、旧预测、旧失败和既有账本保留。此次未推送远程。
