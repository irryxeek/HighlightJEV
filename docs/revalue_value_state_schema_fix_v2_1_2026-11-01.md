# ReVALUE verifier v2.1：状态与未知原因联动修复

## 范围与结论

用户指令：“执行修复”。本次落实上一轮建议的第一阶段最小修复：将 `state` 与 `unknown_reason` 的已有一致性要求加入生成 schema，并完成 CPU 验证。修复代码已完成；尚未获得新模型推理结果，不能报告无效率下降或准确率提升。

本轮新增实验模型调用、实验 token、GPU 分配、GPU 秒、模型 worker 和重试均为 **0**。未修改旧预测、失败记录、评价、冻结源码或原协议；未推送。

## 已确认的问题

原 Q/Q+V 固定 QV100 共 278 次调用，184 条通过契约、94 条 invalid。按旧响应记录的第一个错误分类：

| 第一个错误 | 数量 |
|---|---:|
| 确定判断同时填写非空 `unknown_reason` | 32 |
| 单个事实混用区间内外帧 | 28 |
| 确定判断缺少证据或引用片外证据 | 19 |
| 确定判断依赖尚未确认的条件 | 7 |
| 引用未定义事实 | 4 |
| 时间先后判断缺少两个证据锚点 | 3 |
| 重复空白导致 JSON 截断 | 1 |

32 条第一类响应的 `scope_status` 实际为 `query_scope`，失败来自非空未知原因；旧报错将作用域与未知原因合并，不能据错误文案把它们解释为范围不足。检查全部原始 JSON 后，**40 条**含状态/未知原因矛盾（Q 28、QV 12），其中 8 条先被其他规则拦截。这些类别可同时出现，40 不是可恢复成功数。

旧 schema 将两个字段分别限制为枚举/nullable，却允许不相容的组合；生成结束后的 CPU 检查才拒绝它们。这一接口缺口可以复现。字段为什么被模型这样填写仍未作因果验证。

## 实际修改

修改 contract.py（本地资料：`$MERIT_ROOT/experiments/revalue_value_ablation/contract.py`） 的 `output_schema()`，将单个条件的输出定义为两个互斥状态范围的完整对象分支：

| 状态 | 允许的 `unknown_reason` |
|---|---|
| `supported` / `contradicted` | 仅 JSON `null` |
| `unknown` | 仅原先定义的 8 个具体原因之一 |

使用 `anyOf` 表达分支，经当前 XGrammar 0.1.27 和真实 Qwen tokenizer 的 CPU 检查。无需生成后改写字段、删除证据或重试。未知状态仍允许空证据，不强迫确定判断。

仅生成 schema 改变；原 `validate_output()`、三值汇总、事实引用、依赖、作用域与时间检查保持不变。Q/Q+V 使用相同的新 schema，原提示词、原 query 条件、帧/PTS、价值提示、模型、采样和评价逻辑均未修改。支持性判断的非空片内证据等要求继续由原校验器执行。本次未处理片外引用、依赖关系设计或空白循环，避免同时改变多个因素。

## CPU 验证

新增回归用例先在旧实现复现缺口，再检查修复后的行为；最终完整 CPU 测试 **66 项通过**，Ruff 检查和格式检查通过。运行相关测试全部使用模拟 GPU/worker，临时合成评价不涉及真实数据集 GT。

独立 CPU 审计完成以下检查：

- 278 条已有请求的提示文本逐字不变；139 对 Q/QV 的新 schema 完全相同。
- 139 个候选 schema 编译通过；834 次合成字符串检查覆盖合法状态及矛盾组合。
- 使用本地 Qwen tokenizer、模型配置中的词表大小及实际 XGrammar 编译选项，27 组 token 序列检查全部通过；未加载权重、未初始化 CUDA、未导入 vLLM。
- 184 条旧合法响应经新代码检查后，解析与最终判定完全一致。
- 93 条旧可解析失败仍被拒绝，1 条不可解析失败保持原样；没有失败被提升为合法预测。
- 源码 AST 比较确认唯一变化的原函数是 `output_schema()`；分支规范化检查确认只增加两个字段的联动。
- 1,164 个旧运行、归档和保护文件的 SHA256 保持一致，包括 AGENTS.md、旧结果报告与 v1.1 verifier 账本。

命令（已有环境，无依赖安装）：

```bash
CUDA_VISIBLE_DEVICES='' PYTHONDONTWRITEBYTECODE=1 $LONGVT_ARTIFACT_ROOT/env/inference/bin/python -m unittest discover -s experiments/revalue_value_ablation -p 'test_*.py' -v
CUDA_VISIBLE_DEVICES='' HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONDONTWRITEBYTECODE=1 $LONGVT_ARTIFACT_ROOT/env/inference/bin/python comparisons/qwen_direct/value_state_schema_fix_v2_1_2026-11-01/verify_cpu.py
```

审计脚本的收据为单次写入，已存在时拒绝覆盖。CPU 回放只检查旧响应的契约兼容性，没有运行旧 prepare、supervise、真实 worker、evaluate 或 finalizer，也没有生成新模型预测。

## 尚未解决与后续边界

约束能阻止指定的字段矛盾，但模型可能改答 unknown，也可能在其他证据/逻辑检查上失败。不能用“40 条旧响应被新语法排除”推算修复后合法率，更不能视作语义提升。

下一轮应保持固定输入，对 Q 和 Q+V 同时应用此 schema，再独立检查合法率、确定判断数量、证据不足比例、反例召回及误报。新实验需独立运行目录、完整源码/输入冻结和明确请求/token/GPU/worker 上限。本次 `execution_authorized=false`，未为后续推理分配额度。

旧 Q/Q+V 账本仍为 278/278 请求、28/28 worker、1,336,978 token、5,008.974413305987 GPU 秒、零重试。剩余 token/GPU 上限不转化为新请求；其他历史实验预算不转入本次修复。

## 产物与溯源

- 修复与回归用例（本地资料：`$MERIT_ROOT/experiments/revalue_value_ablation/test_contract.py`）
- 修复审计目录（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_state_schema_fix_v2_1_2026-11-01`）
- CPU 契约收据（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/value_state_schema_fix_v2_1_2026-11-01/cpu_contract_receipt.json`）
- [原 Q/Q+V 结果](revalue_value_qvqv100_results_2026-10-31.md)

原模型调用账本 SHA256：`739f9f9e98a2cd9d99e9f540aea62623f04215c3604e64376bd81b5fc628ce02`。

原评价 SHA256：`99ae7d1ac28bccb8d6e13e07b5bceaef1ff99c36479dbcb746c985e4a22ac6b4`。
