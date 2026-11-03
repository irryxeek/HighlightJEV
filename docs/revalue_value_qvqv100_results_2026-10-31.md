# ReVALUE 价值提示 Q/QV：固定 QV100 配对实验结果

CPU 自动汇总时间：2026-10-31T05:08:20.967790+00:00。实验状态：`complete`。固定 100 条 query、139 个候选 × Q/QV 两臂，共 278 个正式请求槽位；实际尝试 278 次，重试 0 次。

独立人工语义标签为 **0**，因此本实验尚不能证明价值提示改善语义核查。下述指标是固定候选的 IoU 错误代理筛查及输出机制诊断。原候选区间、分数、排序和 grounding 输出完全保留，没有新的定位性能提升结果。

## 两臂与可解释边界

Q 为通用逐条件核查，QV 在相同 query 契约、候选、旧帧像素/PTS、模型、采样、输出 schema 和 CPU 检查上增加适用维度的证据提示。每候选每臂最多一次调用，零自动重试。差异检验这套提示包的增量，提示长度与注意力分配也随之改变，不能单独归因于抽象价值概念。

冻结契约中 2 条 query 无适用价值维度；固定输入完全相同的重复对照共 2 对，两臂均尝试 2 对、均合法 2 对。可比较原文 2 对，其中完全相同 2 对；合法配对的语义状态一致 2 对，技术状态不同 0 对。失败和未尝试保留在完整对照分母。该对照仅检查相同输入的重复性，差异不能归为价值效果；没有新增实验臂、调用或子集性能优势结论。

两臂仅核查语义条件，没有新的边界判断、回看、帧解码、重排或边界改写。semantic supported 不能证明整个区间边界正确；现有 IoU 标签无法独立识别纯边界错误。

## 全候选反例筛查

主要代理：候选与任一标注区间的最大 IoU < 0.5。低 IoU 不自动等于真实语义错误。两臂各保留全部 139 个候选；invalid、运行失败、中断、未尝试及 insufficient 均不能算成功检出。precision 的分母为实际报警数，recall 为全部代理错误数，误报率为全部代理正确候选数。

| 指标 | Q | QV |
|---|---:|---:|
| 筛查 precision | 100.00% | 100.00% |
| 筛查 recall | 1.18% | 3.53% |
| 代理正确区间误报率 | 0.00% | 0.00% |
| 全部候选 | 139 | 139 |
| IoU 代理错误 | 85 | 85 |
| 通过公共契约 | 90 | 94 |
| 报警 | 1 | 3 |
| 代理真阳性 | 1 | 3 |
| 代理假阳性 | 0 | 0 |
| 漏检代理错误 | 84 | 82 |
| supported 中的代理错误 | 16 | 20 |
| supported | 36 | 42 |
| insufficient | 53 | 49 |
| 技术失败或未尝试 | 49 | 45 |

两臂技术状态（单独列示，绝不并入 unknown）：

```json
{
  "Q": {
    "complete": 90,
    "invalid": 49
  },
  "QV": {
    "complete": 94,
    "invalid": 45
  }
}
```

完整 per-query 表包含原 100 条 query；原 base 无有效区间的两个 query 单独标记 no_base_candidate，不能算本次核查检出的错误。所有查询、候选、条件和失败均保留在归档中。

## 配对变化与不确定性

全部 139 个候选进入状态/报警配对；其中 77 对两臂均通过契约，语义状态配对只使用这 77 对。条件状态配对分母为 223/421 个条件出现。invalid 或缺失输出没有被改成 unknown。

```json
{
  "point_differences_QV_minus_Q": {
    "precision": 0.0,
    "recall": 0.023529411764705882,
    "false_alarm_rate": 0.0
  },
  "proxy_flag_changes": {
    "additional_error_flags": 2,
    "lost_error_flags": 0,
    "additional_correct_interval_flags": 0,
    "removed_correct_interval_flags": 0
  },
  "status_transitions": {
    "complete": {
      "complete": 77,
      "invalid": 13
    },
    "invalid": {
      "invalid": 32,
      "complete": 17
    }
  },
  "verdict_transitions": {
    "flagged": {
      "flagged": 1
    },
    "insufficient": {
      "insufficient": 44,
      "invalid": 8,
      "supported": 1
    },
    "invalid": {
      "invalid": 32,
      "flagged": 2,
      "supported": 12,
      "insufficient": 3
    },
    "supported": {
      "supported": 29,
      "insufficient": 2,
      "invalid": 5
    }
  },
  "semantic_state_transitions_both_valid": {
    "contradicted": {
      "contradicted": 1
    },
    "supported": {
      "supported": 29,
      "unknown": 2
    },
    "unknown": {
      "unknown": 44,
      "supported": 1
    }
  },
  "condition_state_transitions_both_valid": {
    "contradicted": {
      "contradicted": 2
    },
    "supported": {
      "supported": 92,
      "unknown": 10
    },
    "unknown": {
      "unknown": 115,
      "supported": 4
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
        "valid_resamples": 6304,
        "ci95": [
          1.0,
          1.0
        ]
      },
      "QV": {
        "valid_resamples": 9508,
        "ci95": [
          1.0,
          1.0
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 6304,
        "ci95": [
          0.0,
          0.0
        ]
      }
    },
    "recall": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.041666666666666664
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
          0.056818181818181816
        ]
      }
    },
    "false_alarm_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.0
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.0
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
          0.5663668011452369,
          0.7286821705426356
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.5925925925925926,
          0.7597467532467531
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          -0.05833333333333324,
          0.11475409836065575
        ]
      }
    },
    "insufficient_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.2777777777777778,
          0.5
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.2684563758389262,
          0.44882291499276866
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          -0.09032258064516124,
          0.03225806451612906
        ]
      }
    },
    "flag_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.024793388429752067
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.04838709677419355
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          0.0,
          0.036231884057971016
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
    "valid_output_denominator": 90,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "invalid": 49
    },
    "semantic_states": {
      "supported": 36,
      "contradicted": 1,
      "unknown": 53
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 266,
    "required_condition_states": {
      "supported": 122,
      "contradicted": 2,
      "unknown": 142
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 2,
          "not_applicable": 88
        },
        "required_condition_occurrences": 2,
        "states": {
          "supported": 1,
          "contradicted": 0,
          "unknown": 1
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "information": {
        "role_counts": {
          "required": 20,
          "not_applicable": 70
        },
        "required_condition_occurrences": 27,
        "states": {
          "supported": 9,
          "contradicted": 0,
          "unknown": 18
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 5,
          "not_applicable": 85
        },
        "required_condition_occurrences": 5,
        "states": {
          "supported": 3,
          "contradicted": 0,
          "unknown": 2
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "action": {
        "role_counts": {
          "required": 77,
          "not_applicable": 13
        },
        "required_condition_occurrences": 105,
        "states": {
          "supported": 46,
          "contradicted": 0,
          "unknown": 59
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 51,
          "not_applicable": 39
        },
        "required_condition_occurrences": 74,
        "states": {
          "supported": 47,
          "contradicted": 1,
          "unknown": 26
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      }
    },
    "invalid_is_not_unknown": true,
    "counts_do_not_measure_semantic_correctness": true
  },
  "QV": {
    "valid_output_denominator": 94,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "invalid": 45
    },
    "semantic_states": {
      "supported": 42,
      "contradicted": 3,
      "unknown": 49
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 272,
    "required_condition_states": {
      "supported": 138,
      "contradicted": 4,
      "unknown": 130
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 2,
          "not_applicable": 92
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
          "required": 21,
          "not_applicable": 73
        },
        "required_condition_occurrences": 30,
        "states": {
          "supported": 13,
          "contradicted": 0,
          "unknown": 17
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 5,
          "not_applicable": 89
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
          "required": 79,
          "not_applicable": 15
        },
        "required_condition_occurrences": 101,
        "states": {
          "supported": 48,
          "contradicted": 0,
          "unknown": 53
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 53,
          "not_applicable": 41
        },
        "required_condition_occurrences": 75,
        "states": {
          "supported": 51,
          "contradicted": 3,
          "unknown": 21
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
      "precision_at_least_80_percent": true,
      "precision_above_error_prevalence": true,
      "recall_at_least_30_percent": false,
      "false_alarm_at_most_10_percent": true,
      "insufficient_at_most_40_percent": true,
      "at_least_20_flags": false
    }
  },
  "QV": {
    "gates_passed": false,
    "exploratory_gates": {
      "structurally_valid_at_least_138": false,
      "precision_at_least_80_percent": true,
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
| 账本 charged token（含故障保留） | 652871 | 684107 |
| 已观测 prompt token | 585622 | 615660 |
| 已观测 output token | 67249 | 68447 |
| 无完整实际 token 记录的尝试 | 0 | 0 |
| 有记录的推理秒数合计 | 1,900.299 | 1,936.288 |

共享 worker：28 次；GPU 生命周期 5,008.974 秒，记账 5,008.974 秒；campaign 墙钟时间 5,024.440 秒。共享模型启动及清理成本不任意均摊为两臂 GPU 时间。

全部启动的终止已确认：True。CPU 收尾新增模型调用、token、GPU 分配、推理重试均为 0；旧 verifier 与其他实验账本独立。逐臂时间跨度、缺失成本记录及完整硬上限见 evaluation.json。

## 审计与结论限制

所有 worker 终止收据与进程组为空检查通过后，CPU 校验冻结账本和响应哈希，仅对原 complete 响应重验相同公共契约；invalid 原文及错误保持原样。先写 prediction_freeze.json，之后才打开 GT。未用 GT 修复、筛选、重新提示或重试响应。

结构/引用合法只说明满足公共契约，不能证明视觉事实为真。事实与判断来自同一模型，仍可能共享错误。当前缺少独立人工必要条件、证据支撑和语义错误标签，不报告这些不可测机制的正确率；未开展人工语义审阅。

## 产物

- 原始运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_2026-10-31`。
- 完整归档（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_2026-10-31/README.md`）。
- [设计 v2](revalue_value_judgement_design_v2_2026-10-31.md)。
- 归档含冻结协议/源码、278 请求、原始响应、全部失败、账本、退出收据、完整候选/条件/query CSV。

响应冻结 SHA256：`b11377d6542900fd7fd21ac5982f588daa5984dc42707b983c1527ff1d57a624`。
评价 SHA256：`99ae7d1ac28bccb8d6e13e07b5bceaef1ff99c36479dbcb746c985e4a22ac6b4`。
最终账本 SHA256：`739f9f9e98a2cd9d99e9f540aea62623f04215c3604e64376bd81b5fc628ce02`。

所有旧输入、输出、准备快照与失败保留，未覆盖历史记录，未推送远程。
