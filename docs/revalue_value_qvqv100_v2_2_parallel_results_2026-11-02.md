# ReVALUE verifier v2.2：事实与证据引用绑定修复的固定 QV100 配对实验结果（多卡续接）

CPU 自动汇总时间：2026-11-02T05:43:21.415186+00:00。实验状态：`complete`。固定 100 条 query、139 个候选 × Q/QV 两臂，共 278 个正式请求槽位；实际尝试 278 次，重试 0 次。

独立人工语义标签为 **0**，因此本实验尚不能证明价值提示改善语义核查。下述指标是固定候选的 IoU 错误代理筛查及输出机制诊断。原候选区间、分数、排序和 grounding 输出完全保留，没有新的定位性能提升结果。

## 事实与证据引用绑定修复前后对照

固定同一批 query、候选、图像与模型，以已完成 v2.1 为历史对照。v2.2 的 schema 绑定实际事实数量、连续 ID 与区间内外帧，提示词仅增加一句区间内事实优先、ID 连续的序列化说明；token 长度与生成次序随之变化。既有 state/unknown_reason 联动、输出字段、八条事实容量及 CPU 语义检查保留。各臂完整分母均为139；无效、未尝试和证据不足均保留。旧结果来自已冻结的历史运行。

| 指标 | Q 修复前 | Q 修复后 | Q+V 修复前 | Q+V 修复后 |
|---|---:|---:|---:|---:|
| 合法输出 | 109 | 112 | 103 | 108 |
| 无效输出 | 30 | 27 | 36 | 31 |
| 无效率 | 21.58% | 19.42% | 25.90% | 22.30% |
| 未尝试 | 0 | 0 | 0 | 0 |
| 证据不足 | 56 | 56 | 52 | 53 |
| supported | 50 | 53 | 47 | 50 |
| 报警 | 3 | 3 | 4 | 5 |
| IoU代理 TP / 正确报警 | 2 | 3 | 3 | 4 |
| IoU代理 FP / 误报 | 1 | 0 | 1 | 1 |
| 代理筛查 precision | 66.67% | 100.00% | 75.00% | 80.00% |
| 代理筛查 recall | 2.35% | 3.53% | 3.53% | 4.71% |
| 代理正确区间误报率 | 1.85% | 0.00% | 1.85% | 1.85% |

比较状态：`complete_fixed_cohort_comparison`。
Q：旧 invalid→新合法 12 条；新判定分布 `{"supported": 7, "insufficient": 4, "flagged": 1}`。新增报警 1 条，其中旧 invalid 转入 1 条、旧合法转入 0 条。两次均合法的语义配对分母为 100。
QV：旧 invalid→新合法 13 条；新判定分布 `{"supported": 6, "insufficient": 5, "flagged": 2}`。新增报警 2 条，其中旧 invalid 转入 2 条、旧合法转入 0 条。两次均合法的语义配对分母为 95。

恢复合法输出不能直接解释为语义判断变准，更多 unknown 也不是反例检出收益。IoU仅为错误代理，独立人工语义标签为0；历史对照不能排除运行间非确定性。全部状态/判定转移、指标差值和失败类型见 schema_repair_comparison.json。


## 用户授权的多卡调度续接

用户允许使用全部空闲GPU后，在完成批次边界将调度器切换为多卡并行。继承原运行 `$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_2_2026-11-02` 的 140 次已完成尝试、14 个已退出worker及其原始响应，未重复推理。后续批次使用不同空闲GPU，各候选内Q/QV次序、模型、输入、schema及采样保持不变。

278次尝试、28次worker及token/GPU累计上限包括继承部分，没有重置或扩充总预算。异常后未尝试位置继续保留在完整分母。并行缩短墙钟等待，不等于降低GPU总时间；硬件放置和并发执行可能带来运行间非确定性，不能将变化完全归因于修复。

```json
{
  "inherited_attempts": 140,
  "continuation_attempts": 138,
  "inherited_charged_tokens": 683770,
  "continuation_charged_tokens": 671275,
  "inherited_gpu_seconds_charged": 3096.689241344051,
  "continuation_gpu_seconds_charged": 3015.2167943311506,
  "budgets_reset": false,
  "inherited_predictions_rerun": false
}
```

并行续接阶段墙钟时间：846.979秒；上述campaign时间从原始调度开始累计。

## 两臂与可解释边界

Q 为通用逐条件核查，QV 在相同 query 契约、候选、旧帧像素/PTS、模型、采样、输出 schema 和 CPU 检查上增加适用维度的证据提示。每候选每臂最多一次调用，零自动重试。差异检验这套提示包的增量，提示长度与注意力分配也随之改变，不能单独归因于抽象价值概念。

冻结契约中 2 条 query 无适用价值维度；固定输入完全相同的重复对照共 2 对，两臂均尝试 2 对、均合法 2 对。可比较原文 2 对，其中完全相同 2 对；合法配对的语义状态一致 2 对，技术状态不同 0 对。失败和未尝试保留在完整对照分母。该对照仅检查相同输入的重复性，差异不能归为价值效果；没有新增实验臂、调用或子集性能优势结论。

两臂仅核查语义条件，没有新的边界判断、回看、帧解码、重排或边界改写。semantic supported 不能证明整个区间边界正确；现有 IoU 标签无法独立识别纯边界错误。

## 全候选反例筛查

主要代理：候选与任一标注区间的最大 IoU < 0.5。低 IoU 不自动等于真实语义错误。两臂各保留全部 139 个候选；invalid、运行失败、中断、未尝试及 insufficient 均不能算成功检出。precision 的分母为实际报警数，recall 为全部代理错误数，误报率为全部代理正确候选数。

| 指标 | Q | QV |
|---|---:|---:|
| 筛查 precision | 100.00% | 80.00% |
| 筛查 recall | 3.53% | 4.71% |
| 代理正确区间误报率 | 0.00% | 1.85% |
| 全部候选 | 139 | 139 |
| IoU 代理错误 | 85 | 85 |
| 通过公共契约 | 112 | 108 |
| 报警 | 3 | 5 |
| 代理真阳性 | 3 | 4 |
| 代理假阳性 | 0 | 1 |
| 漏检代理错误 | 82 | 81 |
| supported 中的代理错误 | 30 | 27 |
| supported | 53 | 50 |
| insufficient | 56 | 53 |
| 技术失败或未尝试 | 27 | 31 |

两臂技术状态（单独列示，绝不并入 unknown）：

```json
{
  "Q": {
    "complete": 112,
    "invalid": 27
  },
  "QV": {
    "complete": 108,
    "invalid": 31
  }
}
```

完整 per-query 表包含原 100 条 query；原 base 无有效区间的两个 query 单独标记 no_base_candidate，不能算本次核查检出的错误。所有查询、候选、条件和失败均保留在归档中。

## 配对变化与不确定性

全部 139 个候选进入状态/报警配对；其中 99 对两臂均通过契约，语义状态配对只使用这 99 对。条件状态配对分母为 296/421 个条件出现。invalid 或缺失输出没有被改成 unknown。

```json
{
  "point_differences_QV_minus_Q": {
    "precision": -0.19999999999999996,
    "recall": 0.011764705882352941,
    "false_alarm_rate": 0.018518518518518517
  },
  "proxy_flag_changes": {
    "additional_error_flags": 1,
    "lost_error_flags": 0,
    "additional_correct_interval_flags": 1,
    "removed_correct_interval_flags": 0
  },
  "status_transitions": {
    "complete": {
      "complete": 99,
      "invalid": 13
    },
    "invalid": {
      "invalid": 18,
      "complete": 9
    }
  },
  "verdict_transitions": {
    "flagged": {
      "flagged": 3
    },
    "insufficient": {
      "insufficient": 46,
      "invalid": 7,
      "supported": 3
    },
    "invalid": {
      "invalid": 18,
      "flagged": 2,
      "supported": 4,
      "insufficient": 3
    },
    "supported": {
      "invalid": 6,
      "supported": 43,
      "insufficient": 4
    }
  },
  "semantic_state_transitions_both_valid": {
    "contradicted": {
      "contradicted": 3
    },
    "supported": {
      "supported": 43,
      "unknown": 4
    },
    "unknown": {
      "unknown": 46,
      "supported": 3
    }
  },
  "condition_state_transitions_both_valid": {
    "contradicted": {
      "contradicted": 3
    },
    "supported": {
      "supported": 151,
      "unknown": 22,
      "contradicted": 1
    },
    "unknown": {
      "unknown": 108,
      "supported": 11
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
        "valid_resamples": 9491,
        "ci95": [
          1.0,
          1.0
        ]
      },
      "QV": {
        "valid_resamples": 9928,
        "ci95": [
          0.3333333333333333,
          1.0
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 9491,
        "ci95": [
          -0.6,
          0.0
        ]
      }
    },
    "recall": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.08433734939759036
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.010752688172043012,
          0.09523809523809523
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
          0.0
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.056338028169014086
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          0.0,
          0.056338028169014086
        ]
      }
    },
    "valid_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.7404580152671756,
          0.8712121212121212
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.7032232862903226,
          0.851063829787234
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          -0.11188941655359576,
          0.054263565891472854
        ]
      }
    },
    "insufficient_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.310126582278481,
          0.5076953124999999
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.2982456140350877,
          0.481204182330827
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          -0.08270676691729323,
          0.04512132604237855
        ]
      }
    },
    "flag_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.050853643449214316
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.008,
          0.06626589229847567
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          0.0,
          0.032471061547148454
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
    "valid_output_denominator": 112,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "invalid": 27
    },
    "semantic_states": {
      "supported": 53,
      "contradicted": 3,
      "unknown": 56
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 334,
    "required_condition_states": {
      "supported": 192,
      "contradicted": 3,
      "unknown": 139
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 4,
          "not_applicable": 108
        },
        "required_condition_occurrences": 4,
        "states": {
          "supported": 3,
          "contradicted": 0,
          "unknown": 1
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "information": {
        "role_counts": {
          "required": 23,
          "not_applicable": 89
        },
        "required_condition_occurrences": 32,
        "states": {
          "supported": 17,
          "contradicted": 0,
          "unknown": 15
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 6,
          "not_applicable": 106
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
          "required": 95,
          "not_applicable": 17
        },
        "required_condition_occurrences": 130,
        "states": {
          "supported": 75,
          "contradicted": 1,
          "unknown": 54
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 64,
          "not_applicable": 48
        },
        "required_condition_occurrences": 92,
        "states": {
          "supported": 63,
          "contradicted": 2,
          "unknown": 27
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      }
    },
    "invalid_is_not_unknown": true,
    "counts_do_not_measure_semantic_correctness": true
  },
  "QV": {
    "valid_output_denominator": 108,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "invalid": 31
    },
    "semantic_states": {
      "supported": 50,
      "contradicted": 5,
      "unknown": 53
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 325,
    "required_condition_states": {
      "supported": 183,
      "contradicted": 6,
      "unknown": 136
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 4,
          "not_applicable": 104
        },
        "required_condition_occurrences": 4,
        "states": {
          "supported": 1,
          "contradicted": 0,
          "unknown": 3
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "information": {
        "role_counts": {
          "required": 23,
          "not_applicable": 85
        },
        "required_condition_occurrences": 31,
        "states": {
          "supported": 15,
          "contradicted": 0,
          "unknown": 16
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 3,
          "not_applicable": 105
        },
        "required_condition_occurrences": 3,
        "states": {
          "supported": 2,
          "contradicted": 0,
          "unknown": 1
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "action": {
        "role_counts": {
          "required": 93,
          "not_applicable": 15
        },
        "required_condition_occurrences": 123,
        "states": {
          "supported": 64,
          "contradicted": 2,
          "unknown": 57
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 67,
          "not_applicable": 41
        },
        "required_condition_occurrences": 98,
        "states": {
          "supported": 70,
          "contradicted": 3,
          "unknown": 25
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
      "insufficient_at_most_40_percent": false,
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
| 账本 charged token（含故障保留） | 662529 | 692516 |
| 已观测 prompt token | 588541 | 618579 |
| 已观测 output token | 73988 | 73937 |
| 无完整实际 token 记录的尝试 | 0 | 0 |
| 有记录的推理秒数合计 | 2,276.263 | 2,282.969 |

共享 worker：28 次；GPU 生命周期 6,111.906 秒，记账 6,111.906 秒；campaign 墙钟时间 4,083.241 秒。共享模型启动及清理成本不任意均摊为两臂 GPU 时间。

全部启动的终止已确认：True。CPU 收尾新增模型调用、token、GPU 分配、推理重试均为 0；旧 verifier 与其他实验账本独立。逐臂时间跨度、缺失成本记录及完整硬上限见 evaluation.json。

## 审计与结论限制

所有 worker 终止收据与进程组为空检查通过后，CPU 校验冻结账本和响应哈希，仅对原 complete 响应重验相同公共契约；invalid 原文及错误保持原样。先写 prediction_freeze.json，之后才打开 GT。未用 GT 修复、筛选、重新提示或重试响应。

结构/引用合法只说明满足公共契约，不能证明视觉事实为真。事实与判断来自同一模型，仍可能共享错误。当前缺少独立人工必要条件、证据支撑和语义错误标签，不报告这些不可测机制的正确率；未开展人工语义审阅。

## 产物

- 原始运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_2_parallel_2026-11-02`。
- 完整归档（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_2_parallel_2026-11-02/README.md`）。
- [设计 v2](revalue_value_judgement_design_v2_2026-10-31.md)。
- 归档含冻结协议/源码、278 请求、原始响应、全部失败、账本、退出收据、完整候选/条件/query CSV。

响应冻结 SHA256：`bd5bfb514f45f90a8633d0332f20faeb4bc0c799c6a03d441c8f3910b3d98533`。
评价 SHA256：`fcc3661d58ac8e26ad89eab9bcc825b4fe5d534ebc113b23eeb6458917c5e43a`。
最终账本 SHA256：`c9a9afeb942ee7030a447b6fa931e3734b6e84ee91df5457ce5b1c5a287dd220`。

所有旧输入、输出、准备快照与失败保留，未覆盖历史记录，未推送远程。
