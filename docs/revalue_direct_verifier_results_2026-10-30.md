# ReVALUE 区间 Verifier v1.1：固定 QV100 验证结果

## 状态与主要结论

CPU 自动汇总时间：2026-10-30T12:40:59.717898+00:00。实验终止状态：`complete`。固定 100 条 query 的 139 个有效候选中，139 次尝试，81 个输出通过结构和引用契约。

预注册探索门槛：**未全部通过**。这是反例筛查开发诊断，不是定位性能提升结果；REZE Direct 原区间、排序和预测均未修改。

## 反例筛查指标

主要错误代理为候选对任一独立 GT 的最大 IoU < 0.5。低 IoU 不自动等同于真实语义错误，标注遗漏和事件切分可能影响该代理。全部 139 个候选均保留在适用分母中，技术无效、未尝试与不确定均不能算成功检出。

| 指标 | 结果 |
|---|---:|
| 反例筛查 precision | 53.70% |
| 反例筛查 recall | 34.12% |
| 正确区间误报率 | 46.30% |
| 全候选错误基率 | 61.15% |
| 通过契约的输出 | 81/139 |
| flagged / supported / insufficient | 54 / 10 / 17 |

技术状态：`{"invalid": 58}`。原 base 中两个无有效区间的 query（9160、2498）另计为结构问题，不能冒充 verifier 检出的反例。

### 完整计数与门槛

```json
{
  "primary": {
    "candidates": 139,
    "gt_proxy_errors": 85,
    "flags": 54,
    "true_positive": 29,
    "false_positive": 25,
    "precision": 0.5370370370370371,
    "recall": 0.3411764705882353,
    "false_alarm_rate": 0.46296296296296297,
    "supported": 10,
    "missed_error_among_supported": 6,
    "insufficient": 17,
    "technical_or_unattempted": 58
  },
  "exploratory_gates": {
    "structurally_valid_at_least_138": false,
    "precision_at_least_80_percent": false,
    "precision_above_error_prevalence": false,
    "recall_at_least_30_percent": true,
    "false_alarm_at_most_10_percent": false,
    "insufficient_at_most_40_percent": true,
    "at_least_20_flags": true
  }
}
```

### 查询、边界与价值判断分布

分布仅统计通过契约的输出；无效原始响应仍独立保留，不能据此把缺失判断当作 unknown。

```json
{
  "query": {
    "supported": 56,
    "unknown": 18,
    "contradicted": 7
  },
  "start": {
    "supported": 19,
    "unknown": 22,
    "too_early": 40
  },
  "end": {
    "supported": 10,
    "too_late": 53,
    "unknown": 18
  },
  "values": {
    "outcome": {
      "supported": 1,
      "not_applicable": 79,
      "contradicted": 1
    },
    "information": {
      "supported": 10,
      "not_applicable": 71
    },
    "emotion": {
      "not_applicable": 79,
      "supported": 2
    },
    "action": {
      "supported": 15,
      "not_applicable": 65,
      "contradicted": 1
    },
    "sensory": {
      "supported": 14,
      "not_applicable": 67
    }
  }
}
```

### 不确定性与 CPU 对照

```json
{
  "source_cluster_bootstrap": {
    "method": "source_video_cluster_percentile_bootstrap",
    "seed": 42,
    "resamples": 10000,
    "source_video_clusters": 100,
    "intervals": {
      "precision": {
        "valid_resamples": 10000,
        "ci95": [
          0.3829787234042553,
          0.6863051470588231
        ]
      },
      "recall": {
        "valid_resamples": 10000,
        "ci95": [
          0.23529411764705882,
          0.4414443664443664
        ]
      },
      "false_alarm_rate": {
        "valid_resamples": 10000,
        "ci95": [
          0.3333333333333333,
          0.5833333333333334
        ]
      }
    },
    "systematic_label_error_covered": false
  },
  "query_macro": {
    "recall": 0.3113583138173302,
    "recall_denominator": 61,
    "precision": 0.5121951219512195,
    "precision_denominator": 41,
    "full_cohort_queries": 100
  },
  "threshold_sensitivity": {
    "0.3": {
      "candidates": 139,
      "gt_proxy_errors": 70,
      "flags": 54,
      "true_positive": 21,
      "false_positive": 33,
      "precision": 0.3888888888888889,
      "recall": 0.3,
      "false_alarm_rate": 0.4782608695652174,
      "supported": 10,
      "missed_error_among_supported": 6,
      "insufficient": 17,
      "technical_or_unattempted": 58
    },
    "0.5": {
      "candidates": 139,
      "gt_proxy_errors": 85,
      "flags": 54,
      "true_positive": 29,
      "false_positive": 25,
      "precision": 0.5370370370370371,
      "recall": 0.3411764705882353,
      "false_alarm_rate": 0.46296296296296297,
      "supported": 10,
      "missed_error_among_supported": 6,
      "insufficient": 17,
      "technical_or_unattempted": 58
    },
    "0.7": {
      "candidates": 139,
      "gt_proxy_errors": 101,
      "flags": 54,
      "true_positive": 38,
      "false_positive": 16,
      "precision": 0.7037037037037037,
      "recall": 0.37623762376237624,
      "false_alarm_rate": 0.42105263157894735,
      "supported": 10,
      "missed_error_among_supported": 6,
      "insufficient": 17,
      "technical_or_unattempted": 58
    }
  },
  "trivial_flag_all": {
    "candidates": 139,
    "gt_proxy_errors": 85,
    "flags": 139,
    "true_positive": 85,
    "false_positive": 54,
    "precision": 0.6115107913669064,
    "recall": 1.0,
    "false_alarm_rate": 1.0,
    "supported": 0,
    "missed_error_among_supported": 0,
    "insufficient": 0,
    "technical_or_unattempted": 0
  },
  "frozen_duration_heuristic": {
    "candidates": 139,
    "gt_proxy_errors": 85,
    "flags": 40,
    "true_positive": 31,
    "false_positive": 9,
    "precision": 0.775,
    "recall": 0.36470588235294116,
    "false_alarm_rate": 0.16666666666666666,
    "supported": 99,
    "missed_error_among_supported": 54,
    "insufficient": 0,
    "technical_or_unattempted": 0
  }
}
```

聚类 bootstrap 按源视频重采样，不能覆盖系统性标注错误。全报警和固定时长启发式均为 CPU 对照，不是额外模型预测。

## 独立成本与运行健康度

- 尝试：139/139；重试：0。
- token 记账：656,389/1,138,688（异常请求保留预留）。
- 模型 worker：14/14；并发上限一卡。
- GPU 生命周期：3283.347138562982 秒；记账 3283.347138562982 / 4,200 秒。
- 全部模型启动均有确认的退出收据：True。
- CPU 收尾新增模型调用、token、GPU 分配、推理重试均为 0。所有旧预算保持独立。

## 可支持的结论与限制

这是单区间 verifier：原 query + 固定旧帧 → 可见事实、查询相关性、五类价值与两端边界 → CPU 契约检查及 flagged / supported / insufficient。低价值不会直接拒绝正确的普通事件。不存在强制胜负、重排、边界改写、全视频记忆或新增回看。

人工独立语义审阅：**0 条**。该报告为冻结评价器的自动汇总，案例语义仍待审阅；结构与来源合法不代表视觉事实为真。同一 Qwen 模型对自己的预测做验证，可能共享错误。单臂联合提示不能证明五类价值的独立贡献。

## 产物与审计

- 原始运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_1_2026-10-30`。
- 完整归档（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/revalue_verifier_v1_1_2026-10-30/README.md`）。
- [冻结协议](revalue_direct_verifier_plan_v1_1_2026-10-30.md)。
- [执行记录](revalue_direct_verifier_execution_2026-10-30.md)。

响应冻结 SHA256：`732aab70d5353d9711b6b45b92eec76886bb88ff86e352310ad391dcf92b23ad`。
评价 SHA256：`ce370b4b65e65bcfc2acc9018358ace1fc7fb822b81a1006a228fdb5ef19bde6`。
最终实验账本 SHA256：`dd00c703ba9b2b06ce17686484bd2b7a9f42134744a7a24644a43bec8d372cb8`。

未推送远程。保留全部旧输入、预测、失败和准备快照，不覆盖历史记录。
