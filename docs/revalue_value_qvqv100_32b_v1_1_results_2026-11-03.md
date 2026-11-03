# ReVALUE verifier 32B v1.1：固定 QV100 的 Q/QV 模型对照结果

CPU 自动汇总时间：2026-11-02T19:53:46.581982+00:00。实验状态：`failed`。固定 100 条 query、139 个候选 × Q/QV 两臂，共 278 个正式请求槽位；实际尝试 20 次，重试 0 次。

独立人工语义标签为 **0**，因此本实验尚不能证明价值提示改善语义核查。下述指标是固定候选的 IoU 错误代理筛查及输出机制诊断。原候选区间、分数、排序和 grounding 输出完全保留，没有新的定位性能提升结果。

## 模型与独立执行边界

本轮使用Qwen3-VL-32B-Instruct BF16，revision 0cfaf48183f594c314753d30a4c4974bc75f3ccb。与8B v2.4对照保持所有请求内容、采样、旧帧、schema与验收规则相同。TP=1/PP=3，每个worker联合三张空闲卡；仅一个组三卡并发，不使用其他用户占用卡。8192上下文、256预填充块、768MiB/rank KV、每rank 1GiB CPU权重offload为必要运行差异，gpu_memory_utilization=0.90，BF16权重不量化；不能作为纯参数量因果实验。

本轮由用户重新明确启动，保留v1首次启动失败，不覆盖历史。OOM、启动错误或超时保留并停止，不自动重试或降采样。v1.1硬上限：278次尝试、零请求重试、2,277,376 token、6次worker启动、每worker3250墙钟秒、累计58,500 GPU秒、同时最多3卡。旧v1另记0次正式请求、1次失败启动、4,500 GPU秒保守费用（实际生命周期未知）；新旧合计最多7次启动、63,000计费GPU秒。GPU生命周期按每个三卡进程组存活墙钟×3相加，含启动、预热和清理；故障预留单独报告，不混同单卡时间。

## 同一输入与验收口径：8B v2.4 对照 32B v1

固定全部100条query、139候选、旧帧像素/PTS、提示、schema、token IDs与验收契约。8B v2.4的已完成评价直接作为历史对照，不重新解释或修写旧回答。本轮改用Qwen3-VL-32B-Instruct BF16；三卡PP、8192上下文、较小prefill与KV预算是必要运行差异，因此不能把差异仅归因于参数量。各臂完整分母均为139；失败、未尝试和证据不足保留。

| 指标 | Q 8B v2.4 | Q 32B v1 | Q+V 8B v2.4 | Q+V 32B v1 |
|---|---:|---:|---:|---:|
| 合法输出 | 136 | 10 | 137 | 9 |
| 无效输出 | 3 | 0 | 2 | 1 |
| 无效率 | 2.16% | 0.00% | 1.44% | 0.72% |
| 未尝试 | 0 | 129 | 0 | 129 |
| 证据不足 | 59 | 9 | 64 | 9 |
| supported | 70 | 0 | 63 | 0 |
| 报警 | 7 | 1 | 10 | 0 |
| IoU代理 TP / 正确报警 | 6 | 1 | 8 | 0 |
| IoU代理 FP / 误报 | 1 | 0 | 2 | 0 |
| 代理筛查 precision | 85.71% | 100.00% | 80.00% | 未定义 |
| 代理筛查 recall | 7.06% | 1.18% | 9.41% | 0.00% |
| 代理正确区间误报率 | 1.85% | 0.00% | 3.70% | 0.00% |

比较状态：`partial_campaign_full_denominator_comparison`。
当前含未完成运行；保留完整分母，不把缺失响应当合法或视为完成效果验证。
Q：旧 invalid→新合法 0 条；新判定分布 `{}`。新增报警 1 条，其中旧 invalid 转入 0 条、旧合法转入 1 条。两次均合法的语义配对分母为 10。
QV：旧 invalid→新合法 0 条；新判定分布 `{}`。新增报警 0 条，其中旧 invalid 转入 0 条、旧合法转入 0 条。两次均合法的语义配对分母为 9。

恢复合法输出不能直接解释为语义判断变准，更多 unknown 也不是反例检出收益。IoU仅为错误代理，独立人工语义标签为0；历史对照不能排除运行间非确定性。全部状态/判定转移、指标差值和失败类型见 model_comparison.json。


## 原始严格口径与去重口径

本轮为独立32B三卡PP验证，冻结278个正式请求槽位；实际尝试数以上表与账本为准。无旧预算转移。主表使用稳定去重后的验收；同时保存原文、原解析对象、规范化对象与逐项去重日志。仅facts.frames和checks.evidence的相同ID可稳定去重，ordered_evidence、状态和语义条件不改。

| 验收指标（各臂完整139分母） | Q | Q+V |
|---|---:|---:|
| 原始严格合法 | 2 | 1 |
| 原始严格无效 | 8 | 9 |
| 去重后合法 | 10 | 9 |
| 去重后无效 | 0 | 1 |
| 去重恢复合法 | 8 | 8 |
| 发生去重 | 8 | 8 |
| 去重后仍无效 | 0 | 0 |
| 技术失败或未尝试 | 129 | 129 |

去重带来的合法率增加是验收规则效应，不是新模型学会了判断。8B v2.4已使用完全相同的验收策略，因此直接复用已完成评价，不重验或改写旧失败。8B单卡与32B三卡PP的运行差异及运行间非确定性仍需保留。

## 两臂与可解释边界

Q 为通用逐条件核查，QV 在相同 query 契约、候选、旧帧像素/PTS、模型、采样、输出 schema 和 CPU 检查上增加适用维度的证据提示。每候选每臂最多一次调用，零自动重试。差异检验这套提示包的增量，提示长度与注意力分配也随之改变，不能单独归因于抽象价值概念。

冻结契约中 2 条 query 无适用价值维度；固定输入完全相同的重复对照共 2 对，两臂均尝试 0 对、均合法 0 对。可比较原文 0 对，其中完全相同 0 对；合法配对的语义状态一致 0 对，技术状态不同 0 对。失败和未尝试保留在完整对照分母。该对照仅检查相同输入的重复性，差异不能归为价值效果；没有新增实验臂、调用或子集性能优势结论。

两臂仅核查语义条件，没有新的边界判断、回看、帧解码、重排或边界改写。semantic supported 不能证明整个区间边界正确；现有 IoU 标签无法独立识别纯边界错误。

## 全候选反例筛查

主要代理：候选与任一标注区间的最大 IoU < 0.5。低 IoU 不自动等于真实语义错误。两臂各保留全部 139 个候选；invalid、运行失败、中断、未尝试及 insufficient 均不能算成功检出。precision 的分母为实际报警数，recall 为全部代理错误数，误报率为全部代理正确候选数。

| 指标 | Q | QV |
|---|---:|---:|
| 筛查 precision | 100.00% | 未定义 |
| 筛查 recall | 1.18% | 0.00% |
| 代理正确区间误报率 | 0.00% | 0.00% |
| 全部候选 | 139 | 139 |
| IoU 代理错误 | 85 | 85 |
| 通过公共契约 | 10 | 9 |
| 报警 | 1 | 0 |
| 代理真阳性 | 1 | 0 |
| 代理假阳性 | 0 | 0 |
| 漏检代理错误 | 84 | 85 |
| supported 中的代理错误 | 0 | 0 |
| supported | 0 | 0 |
| insufficient | 9 | 9 |
| 技术失败或未尝试 | 129 | 130 |

两臂技术状态（单独列示，绝不并入 unknown）：

```json
{
  "Q": {
    "complete": 10,
    "not_attempted": 129
  },
  "QV": {
    "complete": 9,
    "invalid": 1,
    "not_attempted": 129
  }
}
```

完整 per-query 表包含原 100 条 query；原 base 无有效区间的两个 query 单独标记 no_base_candidate，不能算本次核查检出的错误。所有查询、候选、条件和失败均保留在归档中。

## 配对变化与不确定性

全部 139 个候选进入状态/报警配对；其中 9 对两臂均通过契约，语义状态配对只使用这 9 对。条件状态配对分母为 27/421 个条件出现。invalid 或缺失输出没有被改成 unknown。

```json
{
  "point_differences_QV_minus_Q": {
    "precision": null,
    "recall": -0.011764705882352941,
    "false_alarm_rate": 0.0
  },
  "proxy_flag_changes": {
    "additional_error_flags": 0,
    "lost_error_flags": 1,
    "additional_correct_interval_flags": 0,
    "removed_correct_interval_flags": 0
  },
  "status_transitions": {
    "complete": {
      "complete": 9,
      "invalid": 1
    },
    "not_attempted": {
      "not_attempted": 129
    }
  },
  "verdict_transitions": {
    "flagged": {
      "insufficient": 1
    },
    "insufficient": {
      "invalid": 1,
      "insufficient": 8
    },
    "not_attempted": {
      "not_attempted": 129
    }
  },
  "semantic_state_transitions_both_valid": {
    "contradicted": {
      "unknown": 1
    },
    "unknown": {
      "unknown": 8
    }
  },
  "condition_state_transitions_both_valid": {
    "contradicted": {
      "unknown": 1
    },
    "unknown": {
      "unknown": 26
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
        "valid_resamples": 6336,
        "ci95": [
          1.0,
          1.0
        ]
      },
      "QV": {
        "valid_resamples": 0,
        "ci95": null
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 0,
        "ci95": null
      }
    },
    "recall": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.03488372093023256
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
          -0.03488372093023256,
          0.0
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
          0.0,
          0.20279973649538863
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.1812233068944476
        ]
      },
      "difference_QV_minus_Q": {
        "valid_paired_resamples": 10000,
        "ci95": [
          -0.021739130434782594,
          0.0
        ]
      }
    },
    "insufficient_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.1812233068944476
        ]
      },
      "QV": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.1812233068944476
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
    "flag_rate": {
      "Q": {
        "valid_resamples": 10000,
        "ci95": [
          0.0,
          0.021739130434782608
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
          -0.021739130434782608,
          0.0
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
    "valid_output_denominator": 10,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "not_attempted": 129
    },
    "semantic_states": {
      "supported": 0,
      "contradicted": 1,
      "unknown": 9
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 30,
    "required_condition_states": {
      "supported": 0,
      "contradicted": 1,
      "unknown": 29
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 0,
          "not_applicable": 10
        },
        "required_condition_occurrences": 0,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 0
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "information": {
        "role_counts": {
          "required": 0,
          "not_applicable": 10
        },
        "required_condition_occurrences": 0,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 0
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 0,
          "not_applicable": 10
        },
        "required_condition_occurrences": 0,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 0
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "action": {
        "role_counts": {
          "required": 10,
          "not_applicable": 0
        },
        "required_condition_occurrences": 20,
        "states": {
          "supported": 0,
          "contradicted": 1,
          "unknown": 19
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 1,
          "not_applicable": 9
        },
        "required_condition_occurrences": 1,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 1
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      }
    },
    "invalid_is_not_unknown": true,
    "counts_do_not_measure_semantic_correctness": true
  },
  "QV": {
    "valid_output_denominator": 9,
    "full_candidate_denominator": 139,
    "excluded_technical_statuses": {
      "invalid": 1,
      "not_attempted": 129
    },
    "semantic_states": {
      "supported": 0,
      "contradicted": 0,
      "unknown": 9
    },
    "required_condition_occurrences_in_full_population": 421,
    "required_condition_occurrences_in_valid_outputs": 27,
    "required_condition_states": {
      "supported": 0,
      "contradicted": 0,
      "unknown": 27
    },
    "dimensions": {
      "outcome": {
        "role_counts": {
          "required": 0,
          "not_applicable": 9
        },
        "required_condition_occurrences": 0,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 0
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "information": {
        "role_counts": {
          "required": 0,
          "not_applicable": 9
        },
        "required_condition_occurrences": 0,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 0
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "emotion": {
        "role_counts": {
          "required": 0,
          "not_applicable": 9
        },
        "required_condition_occurrences": 0,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 0
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "action": {
        "role_counts": {
          "required": 9,
          "not_applicable": 0
        },
        "required_condition_occurrences": 18,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 18
        },
        "applicability_source": "deterministic_frozen_contract_mapping_not_model_detection"
      },
      "sensory": {
        "role_counts": {
          "required": 1,
          "not_applicable": 8
        },
        "required_condition_occurrences": 1,
        "states": {
          "supported": 0,
          "contradicted": 0,
          "unknown": 1
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
      "precision_at_least_80_percent": false,
      "precision_above_error_prevalence": false,
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
| 实际尝试 | 10 | 10 |
| 账本 charged token（含故障保留） | 40085 | 42651 |
| 已观测 prompt token | 34190 | 35641 |
| 已观测 output token | 5895 | 7010 |
| 无完整实际 token 记录的尝试 | 0 | 0 |
| 有记录的推理秒数合计 | 1,395.939 | 1,653.831 |

共享三卡PP worker：1 次；GPU 生命周期合计 9,393.104 GPU秒，记账 9,393.104 GPU秒；campaign 墙钟时间 3,132.352 秒。共享模型启动及清理成本不任意均摊为两臂 GPU 时间。

全部启动的终止已确认：True。CPU 收尾新增模型调用、token、GPU 分配、推理重试均为 0；旧 verifier 与其他实验账本独立。逐臂时间跨度、缺失成本记录及完整硬上限见 evaluation.json。

## 审计与结论限制

所有 worker 终止收据与进程组为空检查通过后，CPU 校验冻结账本和响应哈希，对 complete/invalid 响应核对同一去重策略及严格契约，包含失败时的规范化明细；原文和冻结判断不改。先写 prediction_freeze.json，之后才打开 GT。未用 GT 修复、筛选、重新提示或重试响应。

结构/引用合法只说明满足公共契约，不能证明视觉事实为真。事实与判断来自同一模型，仍可能共享错误。当前缺少独立人工必要条件、证据支撑和语义错误标签，不报告这些不可测机制的正确率；未开展人工语义审阅。

## 产物

- 原始运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_value_qvqv100_32b_v1_1_2026-11-03`。
- 完整归档（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_qvqv100_32b_v1_1_2026-11-03/README.md`）。
- [设计 v2](revalue_value_judgement_design_v2_2026-10-31.md)。
- 归档含冻结协议/源码、278 请求、原始响应、全部失败、账本、退出收据、完整候选/条件/query CSV。

响应冻结 SHA256：`098166b65698405937bff90fa931d5427d0fc2941e093436c660ae4abe22c20a`。
评价 SHA256：`eadf0fc93ca439d33660b207f0e761767212eef93756666b1cf2b8fb71058c89`。
最终账本 SHA256：`083b5475ca91fce236735d48fd5056fd61da6fdea3991f9a76f014f6746759f4`。

所有旧输入、输出、准备快照与失败保留，未覆盖历史记录，未推送远程。
