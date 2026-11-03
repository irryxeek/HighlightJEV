# REZE Direct + ReVALUE Verifier：实现与CPU准备收据

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: plan，附CPU模块准备
- Origin Date: 2026-10-30
- Verification Status: UNVERIFIED（视觉验证尚未执行）
- Version Label: revalue_direct_verifier_v1_1_2026-10-30

## 已完成的工作

按用户要求，将已完成的REZE Direct协议重建设为后续base；历史自定义Direct预测及报告不变。实现了逐区间verifier：

```text
REZE Direct区间 + 原query
→ 旧帧：片内最多16张，前后上下文各最多4张
→ 来源事实、query匹配、五类价值、起止边界判断
→ 引用与区域校验
→ 发现问题 / 支持当前区间 / 证据不足
```

五类价值为结果、信息、情感、动作、感官。价值低不直接构成grounding错误；需要明确query反证或具体边界缺陷才能标记问题。本轮不改Direct区间、不重排、不追加回看。单调用事实为query-conditioned，不冒称实现了原ReVALUE的query盲记忆。

## 实际CPU验证

| 项目 | 实际结果 |
|---|---|
| 固定总体 | 原100条query、139个有效区间；2个空预测单列 |
| 实际输入准备 | 139/139，全量真实图像processor处理 |
| 每请求图像数 | 6–24，来自原2FPS像素；无新增源帧 |
| 最大输入token / 输出上限 | 4,865 / 1,536 |
| 最小上下文余量 | 1,791 token（上下文8,192） |
| 全量最大请求预留 | 776,316 token |
| CPU契约测试 | 22项通过 |
| 原base受保护文件 | 116个哈希一致，原请求账本未变 |
| 新模型调用 / 实验token | 0 / 0 |
| GPU分配 / GPU秒 / 实验worker启动 | 0 / 0 / 0 |
| 授权门检查 | 实际拒绝未授权运行；未进入GPU发现或worker启动 |

测试覆盖低价值误拒绝、片外证据误归属、混合引用、截断缺少片内锚点、起止端同时有问题、非法引用与正常unknown区分、全失败分母、预算预留、重复调用、父输入漂移、未提交响应及异常收尾。

初始14项测试有一项夹具错误：伪造query引文先触发schema长度校验，夹具却期待子串校验的异常；改用较短伪引文后通过。随后根据独立审查增加回归测试，最终22项通过。历史记录保留，不计为模型失败或请求重试。

v1已完成CPU准备，最终审查补充Popen返回PID前被中断的情况。v1.1保留未知启动的资源预留并禁止读取GT，逐字节复用原139个输入，未重跑视觉模型。原v1源码和收据保留。

## 审查与未验证项

独立只读代理提出了终态收据、区域引用、未提交响应、实际源码绑定、父输入链和启动中断窗口问题；主助手完成修复与CPU测试，最终运行器收据由主助手签署。不宣称独立代理执行过测试或视觉审查。

引用合法不等于事实真实；同一模型验证自己的输出存在相关错误风险。当前没有verifier预测、错误检测成绩或新确认反例，不能把既有Direct反例改名为本模块的发现。

## 冻结与待确认运行

准备目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_1_2026-10-30/`。

```text
manifest SHA-256:
1e2972b27c68956e9636d3e7cd4dcb4f5ac0eaf8113b68e55bb8227dad2151f4
inputs SHA-256:
35f3c3297eed02b36ef32b98bdca1ac93b8e6ffdaa2113f6d379ee1f85b52f8a
原REZE Direct ledger SHA-256（保持不变）:
8fb3140ee26f8d0f785b65c244ac87dbc5213254b38d39aa5ad5ad7106615d8b
```

拟议独立上限：139次、零重试、1,138,688 token、同时一张GPU、累计4,200 GPU秒、14个冷worker。旧预算不转移；新授权收据仍为 `execution_authorized=false`。

拟确认命令：

```bash
$LONGVT_ARTIFACT_ROOT/env/inference/bin/python $ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_1_2026-10-30/source_snapshot/supervise.py --run $ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_1_2026-10-30
```

确认来源：用户调用的 academic-research-suite SKILL.md（本地资料：`$WORKSPACE_PARENT/.codex/skills/academic-research-suite/SKILL.md`） 路由至 code_runner_agent.md（本地资料：`$WORKSPACE_PARENT/.codex/skills/academic-research-suite/ars/experiment-agent/agents/code_runner_agent.md`），执行规则为“Confirm before execution — always show the command and ask for go-ahead”。设计、实现和CPU冻结已完成，待确认的是上面的新模型运行。

## 文件入口

- [完整协议v1.1](revalue_direct_verifier_plan_v1_1_2026-10-30.md)：schema、输入、检测指标、门槛及失败处理。
- 实现代码（本地资料：`$MERIT_ROOT/experiments/revalue_verifier/README.md`）、准备包（本地资料：`$MERIT_ROOT/comparisons/qwen_direct/revalue_verifier_preparation_2026-10-30/README.md`）。
- [原ReVALUE方案](revalue_execution_plan_v3_2026-10-23.md)、[grounding主线](temporal_grounding_mainline_2026-10-29.md)、[REZE Direct base结果](reze_direct_grounding_qv100_results_2026-10-30.md)。

本轮未推送远程，未启动新的GPU实验。
