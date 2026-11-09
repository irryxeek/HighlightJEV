# TVSum 固定10条：D-1fps 对照执行记录

用户要求将无文字记忆D组改为1fps，并与既有F/FV比较。本轮固定原1fps实验的10条视频及顺序，只新增10次D-1fps选择；旧B0、D-sparse、F、FV冻结结果直接复用，不重跑建库与选择。

## 输入与运行

D-1fps一次读取1fps采样帧与原选片帧的去重合集，144–394张图片/视频，合计2430张；按真实PTS排序，原图片像素、源ID、候选choice表及局部证据容差全部保留。无事实/价值记忆块；提示仅修正图像输入描述，详细五维标准和输出契约沿用旧D。

CPU原生token实测最长输入88263、输出预留1536，共89799。继续使用原Qwen3.8-27B、BF16、TP4，max_model_len增加至90112，image上限394，GPU内存比例0.90；其余引擎参数和环境不变。8项针对新输入并集、时间顺序、无记忆引用、原始输出审计的CPU测试已通过，待冻结源码验收后启动。

独立最多10次正式/故障尝试、零重试、一次四卡worker；绝对token640622。worker墙钟最多3600秒另60秒清理，最多14640 GPU秒；不占用任何旧轮次余量。只使用真正空闲GPU，完整输出保留原文，失败/弃权/未尝试均保留10条分母并单列。

## 对照与解释

主比较FV−D-1fps，次比较F−D-1fps及D-1fps−D-sparse。新D覆盖了F/FV实际使用的全部源观察，但其一次呈现的图片数、上下文和计算量与压缩记忆不同，不能称为同token预算下的纯记忆结构比较。候选范围保持旧表，不能选择任意新观察时刻。

结束后确认所属进程退出、冻结预测再读取标签。自动报告原生Top5mAP、排序/同分敏感性、配对bootstrap区间、全部10条逐视频结果、引用合法率及新增与各条件单独运行的成本。旧B0/D/F/FV评价须精确复现。无论正负均不自动扩大样本或更改提示。

- 固定协议（本地资料：`$MERIT_ROOT/experiments/revalue_tvsum_dense_direct_v1/protocol.md`）
- 运行目录（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_dense_direct_10v_27b_v1_2026-11-07`）
- CPU容量检查（本地资料：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_dense_direct_10v_27b_v1_2026-11-07/capacity.json`）

结果报告预定路径：`$MERIT_ROOT/docs/revalue_tvsum_dense_direct_10v_results_2026-11-07.md`。本文件为准备快照；实际进度与成本以status.json/ledger.json和退出收据为准。未推送远程。

## 启动快照

2026-11-07 02:28（北京时间），冻结源码8项CPU测试及十条输入验收通过；监督进程PID 35629已在GPU 0,1,2,3启动单次worker。新增推理正在加载模型，非结果报告。后续以运行目录status.json和完成收据为准。
