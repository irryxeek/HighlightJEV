# TVSum 原子可观察性 v3：执行收据

## Material Passport

- Origin: academic-research-suite / experiment-agent / run。
- 按本轮明确授权执行固定8对，保留模型、像素／PTS、F、价值标准和阶段 token 上限。
- 本文件记录实际启动；完成状态以本轮 complete.json／退出收据为准。

## 启动与验证

- 北京时间：2026-11-08T04:32:51.136667+08:00；GPU [0, 1, 2, 3]，单个 TP4 worker。
- worker PID 65254；supervisor PID 65242。
- 65 项冻结源码 CPU 测试通过；18 个源文件冻结，独立源码审查通过。
- 原生上下文：5100–6179 prompt token＋1536 最大输出，保持16384上限。
- 原22命题逐项与v2一致，新增16个前提单独统计。
- 独立上限：8尝试／0重试／131072 token／1worker／900秒生命周期／3600 GPU秒；无旧额度转移。

## 冻结绑定

- `manifest.json`: `6d45bd8c1d7ad69d88dedb79c585f05056a906720d70aeec745e45bf1024ab52`。
- `authorization.json`: `8e2afe204a3a4f315cbc5f162f2bc0455c0594a403135337fbad29b8e7b88d99`。
- `requests.json`: `1e6585699a9b79494a5dc4ffae3a97b1ccffa6c0a45439391334bddaf8e2974d`。
- `cpu_tests.json`: `3bf0f543552b9101dd3f0906db6711bec22140a56a4b91618f9fed15cc0dc593`。
- `runner_review.json`: `099e5b17d33fc226739dc86440c6627926b26500cb698c77fe593a3e20cff5b0`。

运行目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_tvsum_atom_observability8_27b_v3_2026-11-08`。
