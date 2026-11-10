# TVSum全50两版及27B：执行快照

快照时间：2026-11-10T07:05:54+08:00。本文件不是实时进度，查询命令见下方；后续以运行收据为准。

## 8B已完成

| 条件 | 旧开发10 | 新增40 | 全50 Top-5 mAP(%) |
|---|---:|---:|---:|
| REZE 8B | 61.3167 | 53.2858 | 54.8919 |
| 原详细五维＋背景 | 59.3434 | 52.0726 | 53.5267 |
| 最新v5＋同一背景 | 65.5021 | 53.5694 | 55.9560 |

背景520次、两版新增评分5,906次全部完成、零推理重试；旧10的2,520评分直接复用。新模型调用合计6,426次、12,757,817 token、3,240.895301卡秒（约0.900249 GPUh）。四个8B worker均退出0并释放0–3卡。

最新相对REZE全50为+1.0640pp，95%配对区间[-3.7397,+5.7352]；新增40为+0.2837pp，区间[-4.9419,+5.2979]。最新相对背景全50+2.4292pp，区间[-1.0446,+6.3432]。尚不能宣称稳定泛化收益。

[完整8B结果](revalue_generic_highlight_tvsum_full50_8b_results_2026-11-10.md)。

## 27B运行中

首次启动因vLLM要求数字GPU索引而失败，0模型评分请求，33.066865卡秒已计费保留。数字掩码修复后在 `scoring27_v2` 继续，两版共8,426次请求；截至本快照已完成200次，未发现新的失败收据。不是完整27B指标，不对部分视频做评价。

50视频／4,213窗口的无损缓存与原像素、帧索引和PTS逐一匹配；全部8,426份原生CPU提示契约已验证，最大输入2,270 token。新运行只修改GPU启动映射并扣除原失败耗时，原生输入契约经字节等价审核复用。原背景和修订版均使用同一份8B背景。

当前四卡worker由单次监督器控制，恢复后墙钟上限14,391秒，故障时只清理所属进程；不自动第三次启动。后台 `analysis_snapshot_v2/finish27_v2.py` 会在退出后生成完整CPU比较、成本和Markdown，不依赖本轮交互持续打开。

## 文件与查询

- [50份背景](artifacts/revalue_generic_highlight_tvsum_full50_8b27b_2026-11-10/backgrounds50.json)
- [背景版规则](artifacts/revalue_generic_highlight_tvsum_full50_8b27b_2026-11-10/background/value_rubric.json)
- [最新修订规则](artifacts/revalue_generic_highlight_tvsum_full50_8b27b_2026-11-10/revised/value_rubric.json)
- [运行修订与失败计费](revalue_generic_highlight_tvsum_full50_runtime_amendment_v2_2026-11-10.md)
- [输入等价与启动核验](artifacts/revalue_generic_highlight_tvsum_full50_8b27b_2026-11-10/recovery27_v2/input_equivalence_review.json)

```bash
python3 $MERIT_ROOT/experiments/revalue_generic_highlight_full50_v1/status.py \
  --campaign $ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_tvsum_full50_8b27b_v1_2026-11-10
```

27B最终比较目录为运行根下 `all_models_report_v2/`，最终项目报告预定为 `docs/revalue_generic_highlight_tvsum_full50_8b27b_results_v2_2026-11-10.md`，完成标记为 `campaign_complete_v2.json`。旧 `campaign_complete.json` 是v1故障结束记录，不能据此判断恢复任务结束；旧27B失败0分不是模型性能。
