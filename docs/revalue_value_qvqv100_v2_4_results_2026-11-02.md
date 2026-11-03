# ReVALUE verifier v2.4：依赖约束与引用去重的固定 QV100 配对实验结果

CPU 自动汇总时间：2026-11-02T08:45:29.145930+00:00。实验状态：`complete`。固定 100 条 query、139 个候选 × Q/QV 两臂，共 278 个正式请求槽位；实际尝试 278 次，重试 0 次。

独立人工语义标签为 **0**，因此本实验尚不能证明价值提示改善语义核查。下述指标是固定候选的 IoU 错误代理筛查及输出机制诊断。原候选区间、分数、排序和 grounding 输出完全保留，没有新的定位性能提升结果。

## 同一去重验收口径下：旧 v2.2 与新 v2.4

固定同一批 query、候选、图像与模型，以已完成 v2.2 原始回答为历史对照。两边都使用相同v2.4普通引用去重与严格语义验收，避免把验收放宽算成模型收益。新生成侧保留事实绑定并加入依赖约束及前提优先输出说明；token长度与生成路径随之变化。各臂完整分母均为139；无效、未尝试和证据不足均保留。旧侧是对冻结原回答的CPU派生重验，不是重新调用模型，原始记录和官方旧评价不改。

| 指标 | Q 旧v2.2同口径 | Q 新v2.4 | Q+V 旧v2.2同口径 | Q+V 新v2.4 |
|---|---:|---:|---:|---:|
| 合法输出 | 129 | 136 | 126 | 137 |
| 无效输出 | 10 | 3 | 13 | 2 |
| 无效率 | 7.19% | 2.16% | 9.35% | 1.44% |
| 未尝试 | 0 | 0 | 0 | 0 |
| 证据不足 | 65 | 59 | 60 | 64 |
| supported | 58 | 70 | 59 | 63 |
| 报警 | 6 | 7 | 7 | 10 |
| IoU代理 TP / 正确报警 | 5 | 6 | 6 | 8 |
| IoU代理 FP / 误报 | 1 | 1 | 1 | 2 |
| 代理筛查 precision | 83.33% | 85.71% | 85.71% | 80.00% |
| 代理筛查 recall | 5.88% | 7.06% | 7.06% | 9.41% |
| 代理正确区间误报率 | 1.85% | 1.85% | 1.85% | 3.70% |

比较状态：`complete_fixed_cohort_comparison`。
Q：旧 invalid→新合法 9 条；新判定分布 `{"insufficient": 5, "flagged": 3, "supported": 1}`。新增报警 3 条，其中旧 invalid 转入 3 条、旧合法转入 0 条。两次均合法的语义配对分母为 127。
QV：旧 invalid→新合法 12 条；新判定分布 `{"insufficient": 8, "supported": 2, "flagged": 2}`。新增报警 4 条，其中旧 invalid 转入 2 条、旧合法转入 2 条。两次均合法的语义配对分母为 125。

恢复合法输出不能直接解释为语义判断变准，更多 unknown 也不是反例检出收益。IoU仅为错误代理，独立人工语义标签为0；历史对照不能排除运行间非确定性。全部状态/判定转移、指标差值和失败类型见 schema_repair_comparison.json。


## 原始严格口径与去重口径

本轮为独立四路并行完整重跑；全部278次均为本轮新尝试，不继承或重置旧轮次额度。主表使用稳定去重后的验收；同时保存原文、原解析对象、规范化对象与逐项去重日志。仅facts.frames和checks.evidence的相同ID可稳定去重，ordered_evidence、状态和语义条件不改。

| 验收指标（各臂完整139分母） | Q | Q+V |
|---|---:|---:|
| 原始严格合法 | 110 | 116 |
| 原始严格无效 | 29 | 23 |
| 去重后合法 | 136 | 137 |
| 去重后无效 | 3 | 2 |
| 去重恢复合法 | 26 | 21 |
| 发生去重 | 26 | 21 |
| 去重后仍无效 | 0 | 0 |
| 技术失败或未尝试 | 0 | 0 |

去重带来的合法率增加是验收规则效应，不是新模型学会了判断。与旧v2.2比较时，旧原始回答也按相同v2.4规则离线重验；旧文件保持不变。历史四路/阶段调度及本轮四路硬件放置仍可能带来运行间非确定性。

## 两臂与可解释边界

Q 为通用逐条件核查，QV 在相同 query 契约、候选、旧帧像素/PTS、模型、采样、输出 schema 和 CPU 检查上增加适用维度的证据提示。每候选每臂最多一次调用，零自动重试。差异检验这套提示包的增量，提示长度与注意力分配也随之改变，不能单独归因于抽象价值概念。

冻结契约中 2 条 query 无适用价值维度；固定输入完全相同的重复对照共 2 对，两臂均尝试 2 对、均合法 2 对。可比较原文 2 对，其中完全相同 2 对；合法配对的语义状态一致 2 对，技术状态不同 0 对。失败和未尝试保留在完整对照分母。该对照仅检查相同输入的重复性，差异不能归为价值效果；没有新增实验臂、调用或子集性能优势结论。

两臂仅核查语义条件，没有新的边界判断、回看、帧解码、重排或边界改写。semantic supported 不能证明整个区间边界正确；现有 IoU 标签无法独立识别纯边界错误。

## 全候选反例筛查

主要代理：候选与任一标注区间的最大 IoU < 0.5。低 IoU 不自动等于真实语义错误。两臂各保留全部 139 个候选；invalid、运行失败、中断、未尝试及 insufficient 均不能算成功检出。precision 的分母为实际报警数，recall 为全部代理错误数，误报率为全部代理正确候选数。

| 指标 | Q | QV |
|---|---:|---:|
| 筛查 precision | 85.71% | 80.00% |
| 筛查 recall | 7.06% | 9.41% |
| 代理正确区间误报率 | 1.85% | 3.70% |
| 全部候选 | 139 | 139 |
| IoU 代理错误 | 85 | 85 |
| 通过公共契约 | 136 | 137 |
| 报警 | 7 | 10 |
| 代理真阳性 | 6 | 8 |
| 代理假阳性 | 1 | 2 |
| 漏检代理错误 | 79 | 77 |
| supported 中的代理错误 | 41 | 32 |
| supported | 70 | 63 |
| insufficient | 59 | 64 |
| 技术失败或未尝试 | 3 | 2 |

两臂技术状态（单独列示，绝不并入 unknown）：

```json
{
  "Q": {
    "complete": 136,
    "invalid": 3
  },
  "QV": {
    "complete": 137,
    "invalid": 2
  }
}
```

完整 per-query 表包含原 100 条 query；原 base 无有效区间的两个 query 单独标记 no_base_candidate，不能算本次核查检出的错误。所有查询、候选、条件和失败均保留在归档中。

## 配对变化与不确定性

全部 139 个候选进入状态/报警配对；其中 135 对两臂均通过契约，语义状态配对只使用这 135 对。条件状态配对分母为 408/421 个条件出现。invalid 或缺失输出没有被改成 unknown。

```json
{
  "point_differences_QV_minus_Q": {
    "precision": -0.05714285714285705,
    "recall": 0.023529411764705882,
    "false_alarm_rate": 0.018518518518518517
  },
  "proxy_flag_changes": {
    "additional_error_flags": 2,
    "lost_error_flags": 0,
    "additional_correct_interval_flags": 2,
    "removed_correct_interval_flags": 1
  },
  "status_transitions": {
    "complete": {
      "complete": 135,
      "invalid": 1
    },
    "invalid": {
      "complete": 2,
      "invalid": 1
    }
  },
  "verdict_transitions": {
    "flagged": {
      "flagged": 6,
      "supported": 1
    },
    "insufficient": {
      "insufficient": 51,
      "supported": 6,
      "invalid": 1,
      "flagged": 1
    },
    "invalid": {
      "insufficient": 1,
      "supported": 1,
      "invalid": 1
    },
    "supported": {
      "insufficient": 12,
      "supported": 55,
      "flagged": 3
    }
  },
  "semantic_state_transitions_both_valid": {
    "contradicted": {
      "contradicted": 6,
      "supported": 1
    },
    "supported": {
      "unknown": 12,
      "supported": 55,
      "contradicted": 3
    },
    "unknown": {
      "unknown": 51,
      "supported": 6,
      "contradicted": 1
    }
  },
  "condition_state_transitions_both_valid": {
    "contradicted": {
      "contradicted": 8,
      "supported": 2
    },
    "supported": {
      "unknown": 37,
      "supported": 210,
      "contradicted": 3
    },
    "unknown": {
      "unknown": 129,
      "supported": 18,
      "contradicted": 1
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
        "valid_resamples": 9989,
        "ci95": [
          0.5,
          1.0
        ]
      },
      "QV": {
        "valid_resamples": 9989,
        "ci95": [
          0.5,
          1.0
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 9989,
        "ci95": [
          -0.2857142857142857,
          0.11428571428571432
        ]
      }
    },
    "recall": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.02352257181942545,
          0.1250262605042013
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.025974025974025976,
          0.16666666666666666
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          0.0,
          0.06818181818181818
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
          0.07692307692307693
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          0.0,
          0.05633802816901408
        ]
      }
    },
    "valid_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.9490445859872612,
          1.0
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.9609375,
          1.0
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          -0.016000000000000014,
          0.03418803418803418
        ]
      }
    },
    "insufficient_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.32557678110003696,
          0.528
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.3486792264752791,
          0.5813953488372093
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          -0.027524517557734895,
          0.09999999999999998
        ]
      }
    },
    "flag_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.019351736972704717,
          0.08441558441558442
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.024193548387096774,
          0.12318840579710146
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          0.0,
          0.05185185185185184
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
    "valid_output_denominator": 136,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "invalid": 3
    },
    "semantic_states": {
      "supported": 70,
      "contradicted": 7,
      "unknown": 59
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 410,
    "required_condition_states": {
      "supported": 250,
      "contradicted": 10,
      "unknown": 150
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 5,
          "not_applicable": 131
        },
        "required_condition_occurrences": 5,
        "states": {
          "supported": 2,
          "contradicted": 1,
          "unknown": 2
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "information": {
        "role_counts": {
          "required": 30,
          "not_applicable": 106
        },
        "required_condition_occurrences": 43,
        "states": {
          "supported": 22,
          "contradicted": 0,
          "unknown": 21
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 6,
          "not_applicable": 130
        },
        "required_condition_occurrences": 6,
        "states": {
          "supported": 5,
          "contradicted": 0,
          "unknown": 1
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "action": {
        "role_counts": {
          "required": 118,
          "not_applicable": 18
        },
        "required_condition_occurrences": 154,
        "states": {
          "supported": 97,
          "contradicted": 5,
          "unknown": 52
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 78,
          "not_applicable": 58
        },
        "required_condition_occurrences": 117,
        "states": {
          "supported": 80,
          "contradicted": 4,
          "unknown": 33
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      }
    },
    "invalid_is_not_unknown": true,
    "counts_do_not_measure_semantic_correctness": true
  },
  "QV": {
    "valid_output_denominator": 137,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "invalid": 2
    },
    "semantic_states": {
      "supported": 63,
      "contradicted": 10,
      "unknown": 64
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 414,
    "required_condition_states": {
      "supported": 235,
      "contradicted": 12,
      "unknown": 167
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 5,
          "not_applicable": 132
        },
        "required_condition_occurrences": 5,
        "states": {
          "supported": 2,
          "contradicted": 1,
          "unknown": 2
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "information": {
        "role_counts": {
          "required": 30,
          "not_applicable": 107
        },
        "required_condition_occurrences": 43,
        "states": {
          "supported": 18,
          "contradicted": 0,
          "unknown": 25
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 5,
          "not_applicable": 132
        },
        "required_condition_occurrences": 5,
        "states": {
          "supported": 4,
          "contradicted": 0,
          "unknown": 1
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "action": {
        "role_counts": {
          "required": 119,
          "not_applicable": 18
        },
        "required_condition_occurrences": 157,
        "states": {
          "supported": 88,
          "contradicted": 6,
          "unknown": 63
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 79,
          "not_applicable": 58
        },
        "required_condition_occurrences": 118,
        "states": {
          "supported": 79,
          "contradicted": 6,
          "unknown": 33
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
      "insufficient_at_most_40_percent": false,
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
| 账本 charged token（含故障保留） | 673285 | 701452 |
| 已观测 prompt token | 595368 | 625406 |
| 已观测 output token | 77917 | 76046 |
| 无完整实际 token 记录的尝试 | 0 | 0 |
| 有记录的推理秒数合计 | 2,261.497 | 2,220.412 |

共享 worker：28 次；GPU 生命周期 5,892.557 秒，记账 5,892.557 秒；campaign 墙钟时间 1,946.571 秒。共享模型启动及清理成本不任意均摊为两臂 GPU 时间。

全部启动的终止已确认：True。CPU 收尾新增模型调用、token、GPU 分配、推理重试均为 0；旧 verifier 与其他实验账本独立。逐臂时间跨度、缺失成本记录及完整硬上限见 evaluation.json。

## 审计与结论限制

所有 worker 终止收据与进程组为空检查通过后，CPU 校验冻结账本和响应哈希，对 complete/invalid 响应核对同一去重策略及严格契约，包含失败时的规范化明细；原文和冻结判断不改。先写 prediction_freeze.json，之后才打开 GT。未用 GT 修复、筛选、重新提示或重试响应。

结构/引用合法只说明满足公共契约，不能证明视觉事实为真。事实与判断来自同一模型，仍可能共享错误。当前缺少独立人工必要条件、证据支撑和语义错误标签，不报告这些不可测机制的正确率；未开展人工语义审阅。

## 产物

- 原始运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_v2_4_2026-11-02`。
- 完整归档（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_v2_4_2026-11-02/README.md`）。
- [设计 v2](revalue_value_judgement_design_v2_2026-10-31.md)。
- 归档含冻结协议/源码、278 请求、原始响应、全部失败、账本、退出收据、完整候选/条件/query CSV。

响应冻结 SHA256：`a76a55c7b3ae4cd0ed416a96d2b53f0bb32fb1e58ec63521874629de13abc265`。
评价 SHA256：`a2f6567fe9dc346360df8d3daff63c0f8bfcc7456484d1c39888e19f86ea8295`。
最终账本 SHA256：`8dc135ff037258e6971bcbb235623cb6ff15ecefec3099a1d45287e49ae9e9c1`。

所有旧输入、输出、准备快照与失败保留，未覆盖历史记录，未推送远程。
