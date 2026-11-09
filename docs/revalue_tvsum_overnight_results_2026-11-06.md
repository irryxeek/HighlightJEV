# TVSum 八小时自动任务结果

## Material Passport

- Origin Skill / Mode: academic-research-suite / experiment-agent, run + validate.
- Verification Status: ANALYZED for completed CPU evaluations; independent semantic review pending.
- User instruction: 我现在准备睡觉，请你安排接下来8h的任务并自动化执行。
- 截止时间：2026-11-06T09:27:06+08:00。
- 最终状态：`complete`。

## 旧输出导出诊断

| 导出 | 范围 | 条件 | Top-5 mAP (%) |
|---|---|---|---:|
| native | reused_val10 | B0 | 61.3167 |
| native | reused_val10 | F | 59.7625 |
| native | reused_val10 | FV | 62.9247 |
| native | new40_official_train | B0 | 53.2858 |
| native | new40_official_train | F | 52.6220 |
| native | new40_official_train | FV | 50.6473 |
| native | all50_zero_shot | B0 | 54.8919 |
| native | all50_zero_shot | F | 54.0501 |
| native | all50_zero_shot | FV | 53.1028 |
| rank_faithful | reused_val10 | B0 | 61.3167 |
| rank_faithful | reused_val10 | F | 60.3000 |
| rank_faithful | reused_val10 | FV | 63.2538 |
| rank_faithful | new40_official_train | B0 | 53.2858 |
| rank_faithful | new40_official_train | F | 52.6418 |
| rank_faithful | new40_official_train | FV | 50.1183 |
| rank_faithful | all50_zero_shot | B0 | 54.8919 |
| rank_faithful | all50_zero_shot | F | 54.1735 |
| rank_faithful | all50_zero_shot | FV | 52.7454 |

完整报告：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_overnight_27b_v1_2026-11-06/p0_rank_export/report.md`。

## 新增D-relative40

| 导出 | 范围 | 条件 | Top-5 mAP (%) |
|---|---|---|---:|
| native | new40_official_train | B0 | 53.2858 |
| native | new40_official_train | F | 52.6220 |
| native | new40_official_train | FV | 50.6473 |
| native | new40_official_train | D | 54.9161 |
| rank_faithful | new40_official_train | B0 | 53.2858 |
| rank_faithful | new40_official_train | F | 52.6418 |
| rank_faithful | new40_official_train | FV | 50.1183 |
| rank_faithful | new40_official_train | D | 54.9773 |

完整报告：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_overnight_27b_v1_2026-11-06/direct40/report.md`。

本阶段：40次尝试，942884记账token，6212.443 GPU秒；零自动重试。

## 条件性价值表示小试

本阶段没有完成评价；不将缺失结果写成有效预测。

## 自动分支与下一步

D有效输出：40/40；原生F−D=-2.2941pp，忠实秩导出F−D=-2.3354pp。
预定科学调度条件：`False`；它是探索性条件，不是显著性检验。

未自动启动价值模型分支。下一步先根据D/F/FV对照审查共同视觉覆盖、事实装箱和额外文本干扰；保留已准备的价值分支源码供后续审阅。

## 成本与边界

本次实际新增：40次尝试、942884记账token、6212.443 GPU秒。
历史来源哈希保持不变：True。未推送；未把旧额度、旧失败或缓存调用重记成本。
原native与rank-faithful并列，后者是后处理条件，不是新模型预测。旧10及已查看的新40均不能称未见测试集。
