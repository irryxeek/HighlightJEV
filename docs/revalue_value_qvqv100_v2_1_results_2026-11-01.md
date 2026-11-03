# ReVALUE verifier v2.1：字段联动修复后的固定 QV100 配对实验结果

CPU 自动汇总时间：2026-11-01T19:33:59.814348+00:00。实验状态：`complete`。固定 100 条 query、139 个候选 × Q/QV 两臂，共 278 个正式请求槽位；实际尝试 278 次，重试 0 次。

独立人工语义标签为 **0**，因此本实验尚不能证明价值提示改善语义核查。下述指标是固定候选的 IoU 错误代理筛查及输出机制诊断。原候选区间、分数、排序和 grounding 输出完全保留，没有新的定位性能提升结果。

## 字段联动修复前后对照

固定同一批 query、候选、图像、提示词与模型，仅生成 schema 增加 state/unknown_reason 联动。各臂完整分母均为139；无效、未尝试和证据不足均保留。旧结果来自已冻结的历史运行。

| 指标 | Q 修复前 | Q 修复后 | Q+V 修复前 | Q+V 修复后 |
|---|---:|---:|---:|---:|
| 合法输出 | 90 | 109 | 94 | 103 |
| 无效输出 | 49 | 30 | 45 | 36 |
| 无效率 | 35.25% | 21.58% | 32.37% | 25.90% |
| 未尝试 | 0 | 0 | 0 | 0 |
| 证据不足 | 53 | 56 | 49 | 52 |
| supported | 36 | 50 | 42 | 47 |
| 报警 | 1 | 3 | 3 | 4 |
| IoU代理 TP / 正确报警 | 1 | 2 | 3 | 3 |
| IoU代理 FP / 误报 | 0 | 1 | 0 | 1 |
| 代理筛查 precision | 100.00% | 66.67% | 100.00% | 75.00% |
| 代理筛查 recall | 1.18% | 2.35% | 3.53% | 3.53% |
| 代理正确区间误报率 | 0.00% | 1.85% | 0.00% | 1.85% |

比较状态：`complete_fixed_cohort_comparison`。
Q：旧 invalid→新合法 19 条；新判定分布 `{"supported": 14, "flagged": 2, "insufficient": 3}`。新增报警 2 条，其中旧 invalid 转入 2 条、旧合法转入 0 条。两次均合法的语义配对分母为 90。
QV：旧 invalid→新合法 9 条；新判定分布 `{"supported": 5, "flagged": 1, "insufficient": 3}`。新增报警 1 条，其中旧 invalid 转入 1 条、旧合法转入 0 条。两次均合法的语义配对分母为 94。

恢复合法输出不能直接解释为语义判断变准，更多 unknown 也不是反例检出收益。IoU仅为错误代理，独立人工语义标签为0；历史对照不能排除运行间非确定性。全部状态/判定转移、指标差值和失败类型见 schema_repair_comparison.json。


## 两臂与可解释边界

Q 为通用逐条件核查，QV 在相同 query 契约、候选、旧帧像素/PTS、模型、采样、输出 schema 和 CPU 检查上增加适用维度的证据提示。每候选每臂最多一次调用，零自动重试。差异检验这套提示包的增量，提示长度与注意力分配也随之改变，不能单独归因于抽象价值概念。

冻结契约中 2 条 query 无适用价值维度；固定输入完全相同的重复对照共 2 对，两臂均尝试 2 对、均合法 2 对。可比较原文 2 对，其中完全相同 2 对；合法配对的语义状态一致 2 对，技术状态不同 0 对。失败和未尝试保留在完整对照分母。该对照仅检查相同输入的重复性，差异不能归为价值效果；没有新增实验臂、调用或子集性能优势结论。

两臂仅核查语义条件，没有新的边界判断、回看、帧解码、重排或边界改写。semantic supported 不能证明整个区间边界正确；现有 IoU 标签无法独立识别纯边界错误。

## 全候选反例筛查

主要代理：候选与任一标注区间的最大 IoU < 0.5。低 IoU 不自动等于真实语义错误。两臂各保留全部 139 个候选；invalid、运行失败、中断、未尝试及 insufficient 均不能算成功检出。precision 的分母为实际报警数，recall 为全部代理错误数，误报率为全部代理正确候选数。

| 指标 | Q | QV |
|---|---:|---:|
| 筛查 precision | 66.67% | 75.00% |
| 筛查 recall | 2.35% | 3.53% |
| 代理正确区间误报率 | 1.85% | 1.85% |
| 全部候选 | 139 | 139 |
| IoU 代理错误 | 85 | 85 |
| 通过公共契约 | 109 | 103 |
| 报警 | 3 | 4 |
| 代理真阳性 | 2 | 3 |
| 代理假阳性 | 1 | 1 |
| 漏检代理错误 | 83 | 82 |
| supported 中的代理错误 | 26 | 21 |
| supported | 50 | 47 |
| insufficient | 56 | 52 |
| 技术失败或未尝试 | 30 | 36 |

两臂技术状态（单独列示，绝不并入 unknown）：

```json
{
  "Q": {
    "complete": 109,
    "invalid": 30
  },
  "QV": {
    "complete": 103,
    "invalid": 36
  }
}
```

完整 per-query 表包含原 100 条 query；原 base 无有效区间的两个 query 单独标记 no_base_candidate，不能算本次核查检出的错误。所有查询、候选、条件和失败均保留在归档中。

## 配对变化与不确定性

全部 139 个候选进入状态/报警配对；其中 97 对两臂均通过契约，语义状态配对只使用这 97 对。条件状态配对分母为 284/421 个条件出现。invalid 或缺失输出没有被改成 unknown。

```json
{
  "point_differences_QV_minus_Q": {
    "precision": 0.08333333333333337,
    "recall": 0.011764705882352941,
    "false_alarm_rate": 0.0
  },
  "proxy_flag_changes": {
    "additional_error_flags": 1,
    "lost_error_flags": 0,
    "additional_correct_interval_flags": 1,
    "removed_correct_interval_flags": 1
  },
  "status_transitions": {
    "complete": {
      "complete": 97,
      "invalid": 12
    },
    "invalid": {
      "invalid": 24,
      "complete": 6
    }
  },
  "verdict_transitions": {
    "flagged": {
      "flagged": 2,
      "supported": 1
    },
    "insufficient": {
      "insufficient": 47,
      "invalid": 8,
      "supported": 1
    },
    "invalid": {
      "invalid": 24,
      "supported": 4,
      "insufficient": 1,
      "flagged": 1
    },
    "supported": {
      "flagged": 1,
      "supported": 41,
      "insufficient": 4,
      "invalid": 4
    }
  },
  "semantic_state_transitions_both_valid": {
    "contradicted": {
      "contradicted": 2,
      "supported": 1
    },
    "supported": {
      "contradicted": 1,
      "supported": 41,
      "unknown": 4
    },
    "unknown": {
      "unknown": 47,
      "supported": 1
    }
  },
  "condition_state_transitions_both_valid": {
    "contradicted": {
      "contradicted": 3,
      "supported": 2
    },
    "supported": {
      "supported": 140,
      "contradicted": 1,
      "unknown": 14
    },
    "unknown": {
      "unknown": 118,
      "supported": 6
    }
  }
}
```

source_video_id 聚类 bootstrap 使用同一组重采样同时计算 Q、QV 及 QV−Q 差值，保留无候选源视频。区间是探索性百分位区间，不覆盖系统性标注错误，也不是语义正确性或独立泛化证明。

```json
{
  "method": "paired_source_video_cluster_percentile_bootstrap",
  "seed": 42,
  "resamples": 10000,
  "source_video_clusters": 100,
  "no_candidate_clusters_retained": 2,
  "draws_shared_between_arms": true,
  "intervals": {
    "precision": {
      "Q": {
        "valid_resamples": 9500,
        "ci95": [
          0.0,
          1.0
        ]
      },
      "QV": {
        "valid_resamples": 9828,
        "ci95": [
          0.0,
          1.0
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 9500,
        "ci95": [
          0.0,
          0.5
        ]
      }
    },
    "recall": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.06329113924050633
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.07620879120879095
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          0.0,
          0.03409090909090909
        ]
      }
    },
    "false_alarm_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.05128205128205128
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.05128205128205128
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          0.0,
          0.0
        ]
      }
    },
    "valid_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.7169769577558858,
          0.8424657534246576
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.664,
          0.8175686299507053
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          -0.11249999999999993,
          0.02857142857142858
        ]
      }
    },
    "insufficient_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.3012784090909091,
          0.5161290322580645
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.2867132867132867,
          0.4736927546138071
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          -0.09202453987730058,
          0.031746031746031744
        ]
      }
    },
    "flag_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.04697986577181208
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.006848150218991707,
          0.056338028169014086
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          0.0,
          0.022058823529411766
        ]
      }
    }
  },
  "systematic_label_error_covered": false,
  "semantic_correctness_test": false
}
```

## 条件与五维输出分布

以下分布仅统计合法输出。required 条件的 supported / contradicted / unknown 均来自逐条件 checks；未适用维度的 NA 由冻结契约映射确定，不是模型新识别出的价值，也不能把更多非 NA 或更多报警解释为收益。逐 query、逐 condition 的状态与配对明细见 paired_condition_audit.csv 及 evaluation.json。

```json
{
  "Q": {
    "valid_output_denominator": 109,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "invalid": 30
    },
    "semantic_states": {
      "supported": 50,
      "contradicted": 3,
      "unknown": 56
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 325,
    "required_condition_states": {
      "supported": 173,
      "contradicted": 5,
      "unknown": 147
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 3,
          "not_applicable": 106
        },
        "required_condition_occurrences": 3,
        "states": {
          "supported": 2,
          "contradicted": 0,
          "unknown": 1
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "information": {
        "role_counts": {
          "required": 22,
          "not_applicable": 87
        },
        "required_condition_occurrences": 33,
        "states": {
          "supported": 15,
          "contradicted": 0,
          "unknown": 18
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 6,
          "not_applicable": 103
        },
        "required_condition_occurrences": 6,
        "states": {
          "supported": 4,
          "contradicted": 0,
          "unknown": 2
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "action": {
        "role_counts": {
          "required": 93,
          "not_applicable": 16
        },
        "required_condition_occurrences": 124,
        "states": {
          "supported": 63,
          "contradicted": 2,
          "unknown": 59
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 63,
          "not_applicable": 46
        },
        "required_condition_occurrences": 94,
        "states": {
          "supported": 64,
          "contradicted": 2,
          "unknown": 28
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      }
    },
    "invalid_is_not_unknown": true,
    "counts_do_not_measure_semantic_correctness": true
  },
  "QV": {
    "valid_output_denominator": 103,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "invalid": 36
    },
    "semantic_states": {
      "supported": 47,
      "contradicted": 4,
      "unknown": 52
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 301,
    "required_condition_states": {
      "supported": 161,
      "contradicted": 5,
      "unknown": 135
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 2,
          "not_applicable": 101
        },
        "required_condition_occurrences": 2,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 2
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "information": {
        "role_counts": {
          "required": 23,
          "not_applicable": 80
        },
        "required_condition_occurrences": 34,
        "states": {
          "supported": 17,
          "contradicted": 0,
          "unknown": 17
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 5,
          "not_applicable": 98
        },
        "required_condition_occurrences": 5,
        "states": {
          "supported": 2,
          "contradicted": 0,
          "unknown": 3
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "action": {
        "role_counts": {
          "required": 86,
          "not_applicable": 17
        },
        "required_condition_occurrences": 111,
        "states": {
          "supported": 57,
          "contradicted": 1,
          "unknown": 53
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 59,
          "not_applicable": 44
        },
        "required_condition_occurrences": 87,
        "states": {
          "supported": 61,
          "contradicted": 3,
          "unknown": 23
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      }
    },
    "invalid_is_not_unknown": true,
    "counts_do_not_measure_semantic_correctness": true
  }
}
```

## 原探索门槛与 CPU 对照

保留原 139 候选的全部探索门槛，不降低标准。它们在本语义对照中仅供参考；通过不能证明价值提示有效，未通过也不能单独判断语义价值无效。

```json
{
  "Q": {
    "gates_passed": false,
    "exploratory_gates": {
      "structurally_valid_at_least_138": false,
      "precision_at_least_80_percent": false,
      "precision_above_error_prevalence": true,
      "recall_at_least_30_percent": false,
      "false_alarm_at_most_10_percent": true,
      "insufficient_at_most_40_percent": false,
      "at_least_20_flags": false
    }
  },
  "QV": {
    "gates_passed": false,
    "exploratory_gates": {
      "structurally_valid_at_least_138": false,
      "precision_at_least_80_percent": false,
      "precision_above_error_prevalence": true,
      "recall_at_least_30_percent": false,
      "false_alarm_at_most_10_percent": true,
      "insufficient_at_most_40_percent": true,
      "at_least_20_flags": false
    }
  }
}
```

IoU 阈值 0.3/0.5/0.7 敏感性、query macro、全报警和旧版固定时长启发式均见 evaluation.json。固定时长规则仍为区间长度 ≤ 2 秒或长度 / 视频时长 ≥ 0.8，不读取本次结果调参，也不是新增模型预测。

## 独立成本与运行健康度

| 记账 | Q | QV |
|---|---:|---:|
| 实际尝试 | 139 | 139 |
| 账本 charged token（含故障保留） | 652325 | 683943 |
| 已观测 prompt token | 585622 | 615660 |
| 已观测 output token | 66703 | 68283 |
| 无完整实际 token 记录的尝试 | 0 | 0 |
| 有记录的推理秒数合计 | 1,886.991 | 1,935.912 |

共享 worker：28 次；GPU 生命周期 5,015.231 秒，记账 5,015.231 秒；campaign 墙钟时间 5,033.174 秒。共享模型启动及清理成本不任意均摊为两臂 GPU 时间。

全部启动的终止已确认：True。CPU 收尾新增模型调用、token、GPU 分配、推理重试均为 0；旧 verifier 与其他实验账本独立。逐臂时间跨度、缺失成本记录及完整硬上限见 evaluation.json。

## 审计与结论限制

所有 worker 终止收据与进程组为空检查通过后，CPU 校验冻结账本和响应哈希，仅对原 complete 响应重验相同公共契约；invalid 原文及错误保持原样。先写 prediction_freeze.json，之后才打开 GT。未用 GT 修复、筛选、重新提示或重试响应。

结构/引用合法只说明满足公共契约，不能证明视觉事实为真。事实与判断来自同一模型，仍可能共享错误。当前缺少独立人工必要条件、证据支撑和语义错误标签，不报告这些不可测机制的正确率；未开展人工语义审阅。

## 产物

- 原始运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_1_2026-11-01`。
- 完整归档（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_1_2026-11-01/README.md`）。
- [设计 v2](revalue_value_judgement_design_v2_2026-10-31.md)。
- 归档含冻结协议/源码、278 请求、原始响应、全部失败、账本、退出收据、完整候选/条件/query CSV。

响应冻结 SHA256：`b9136d4d2b74f1341b910f5c42822bbebee3785236e7ad9a275b9e4420625f54`。
评价 SHA256：`df14f32b06e69375714c5983fb9df3de76320348f9a469b1b1ef632194275b6b`。
最终账本 SHA256：`ece1fa6dbe01648c3839e3d990205df9083cdba7b2bd38fffc96f35deef32932`。

所有旧输入、输出、准备快照与失败保留，未覆盖历史记录，未推送远程。
