# TVSum 固定 8 例反证修复 v2：执行收据

## Material Passport

- Origin: academic-research-suite / experiment-agent / run。
- 2026-11-08；用户授权“进行修复，启动新实验”。
- 本文件记录启动事实；后续完成和成本以运行根 complete.json、ledger.json、worker_0/exit.json 为准。

## 启动及验证

- 启动时间：2026-11-08T03:21:37.134262+08:00。
- GPU：[0, 1, 2, 3]，TP4；worker PID 31665；supervisor PID 31606。
- 独立 8 次尝试、零重试、131072 token、一次 worker、900 秒完整生命周期／3600 GPU 秒。
- 57 项 CPU 测试通过；原生上下文 4762–5704 prompt token，加最大输出 1536，低于16384。
- 17 份源文件冻结；原帧／PTS、F、五维 rubric、模型环境与旧条件一致。
- 不变的旧对照直接读取；没有重新生成旧模型预测。
- 对注册原子的判断不认证整句或像素真值。

## 冻结绑定

- `manifest.json`：`1ca04c33abf74df6f9bd780ff704cdab9545ba89ccef165f66d3e25c9b666dd3`。
- `authorization.json`：`54f4b1641e3ffeb4979df9e5342b0464b47de4b58a15f02a21afea0f3fd92412`。
- `requests.json`：`38210bb1c7b0912d50ac0c4512484b6c587e9695232f032b9e31b90ab0e4862a`。
- `runner_review.json`：`9e938e8785e1006fbb903366c5814b264dce287275d6cb643b609844be2b5ba7`。
- `cpu_tests.json`：`83c7dda2f590713626db823d4cdcff86869d18412a0aecd2c477a4a6ef5e22d5`。

运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_counterevidence8_27b_v2_2026-11-08`。

审查与来源：`$MERIT_ROOT/comparisons/tvsum_counterevidence8_v2_2026-11-08`。
