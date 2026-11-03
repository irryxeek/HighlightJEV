# ReVALUE 32B 固定 QV100：三卡恢复执行记录 v1.1

快照时间：2026-11-03T03:07:58.086075+08:00。**32B 已完成三卡装载并返回正式预测，实验正在后台运行。**

## 当前进度

- 固定100条query、139个REZE Direct区间，Q/Q+V共278次请求；当前已落盘2条、全部状态`{'complete': 2, 'reserved': 1}`。
- GPU 0、2、3联合运行一个TP1/PP3实例，分层21/22/21；未使用其他用户占用卡。
- CPU supervisor PID55221，CPU finalizer PID55222；后台独立会话运行，关闭当前聊天不停止该进程。
- 首对Q/QV均通过冻结输出契约。结构合法不等于语义判断正确，尚无完整评价结果。

| 已完成请求 | 状态 | 输出token | 推理秒数 |
|---|---|---:|---:|
| qv_2781_w01__Q | complete | 758 | 180.740 |
| qv_2781_w01__QV | complete | 190 | 48.284 |

首次两条速度约4输出token/秒，实际输出长度不同，当前不据此给完整完成时间保证。若后续速度不能满足冻结的worker生命周期或总预算，控制器会按原停止规则退出，保留完整失败/未尝试分母，不自动扩额。

## 修复和验证

1. v1无预测，启动时遇到显存准入和进程归属错误。所有59个旧运行文件已哈希保留，旧账本及历史失败不改。
2. 150项CPU测试和Ruff通过。CPU复现确认：vLLM使用的setproctitle会让/proc/environ失去原环境标记，旧检查误拒绝；新检查结合UID、session/PGID、父子链及创建时间，仍拒绝不明归属和冲突标记。旧日志未记录被拒绝PID，不能断言已逐进程复原唯一历史原因。
3. 将显存准入比例固定为0.90，并显式使用每rank 1GiB CPU权重offload为三卡留出余量。仍用BF16，未量化、减帧或缩短2048输出上限。实际host迁移按参数粒度可略超设置值，速度会受影响。
4. 新冻结源码24文件；278条请求、token IDs、像素/PTS、schema、query条件和rubric均与原实验一致，最长5532输入+2048输出，8192上下文余612。正式请求另行核验运行时token IDs。
5. 初次模型装载、KV及实际生成已成功。引擎日志中显式KV配置的“skipped memory profiling”指跳过自动可用KV预算测算，源码仍执行profile_run；没有添加skip_mm_profiling。

## 范围和预算

最新用户指令：“现在有3卡，跑一下32b模型”。授权绑定新manifest后仅fresh dispatch一次。
完整100条query/139区间不变；只做Q/QV verifier，不改Direct区间、分数或排序。CPU完成器在全部所属worker退出后冻结预测，再读取GT、评价一次并保存报告。
- v1.1：最多278次尝试、零请求重试、2,277,376 token；6个连续批次（48×5+38），每批3卡、3250墙钟秒，累计58,500 GPU秒。
- 旧v1：0次正式请求、1次失败worker启动、4,500 GPU秒保守费用；实际完整生命周期仍未知。
- 32B新旧合计最多7次worker启动和63,000计费GPU秒。旧QV、TVSum、Direct和8B等预算不转移。
- 运行失败、OOM、超时、资源或输入归属不明即停止派发，不自动改配置重试。尚在进行的GPU时间不是最终生命周期收据。

## 产物

- 冻结协议（本地资料：`$MERIT_ROOT/experiments/revalue_value_ablation_32b_v1_1/protocol.md`）
- CPU检查收据（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_1_preparation_2026-11-03/cpu_test_final_receipt.json`）
- CPU进程改名复现（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_1_preparation_2026-11-03/setproctitle_cpu_reproduction.json`）
- 运行器审查（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_1_preparation_2026-11-03/runtime_source_review.md`）
- 启动与初始预测收据（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_1_preparation_2026-11-03/inference_started_receipt.json`）
- 实时运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_32b_v1_1_2026-11-03`。
- 完成后预计报告：`docs/revalue_value_qvqv100_32b_v1_1_results_2026-11-03.md`；本快照尚未生成。
- manifest SHA256：`f315fea1ecc382d23de48de0a4cc02f27cf8862579ba4facff583cc715f9714a`。
- 旧v1 ledger SHA256：`f8b4245fd86bf804d1b13e6c4d21b2bdfb9b9e48ce3f469d46de79d9ba7eb7d3`。

本文件是执行快照，最终进度以实时账本、退出收据和完成评价为准。未推送远程。
