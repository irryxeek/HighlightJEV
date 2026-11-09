# TVSum 固定 8 例原子可观察性与前提依赖 v3：运行结果

## Material Passport

- Origin: academic-research-suite / experiment-agent / run.
- Verification: CPU 契约与运行收据已核验；视觉语义需另看逐例审查。
- 固定 8 对，涉及原 10 视频中的 7 条；不是全量性能实验。
- 相同 Qwen3.8-27B、旧帧/PTS、F、五维标准及阶段 token 上限。

## 运行与独立账本

- 8/8 次尝试，8/8 合法；零重试，1 个 TP4 worker。
- 实际已知 token 53339；计费／预留 token 53339/131072。
- worker 生命周期 578.177/900 秒；GPU 生命周期 2312.706/3600 秒。
- 历史 317 份文件及旧评价/报告绑定不变；旧 v1/v2 账本独立且不转移剩余。
- 运行状态 `complete`；界限检查 `True`。

## 完整 8 例对照

| 视频与片段 | 新输出 | v2→v3 原子判断 | v3 前提判断 | v2→v3 比较 |
|---|---|---|---|---|
| WxtbjNsCQ8A [200, 202] | complete | a1:unknown→unknown, a2:unknown→supported | p1:supported | insufficient → insufficient |
| i3wAGJaaktw [22, 24] | complete | a1:unknown→unknown | p1:unknown, p2:supported | insufficient → insufficient |
| AwmHb44_ouw [300, 302] | complete | a1:unknown→unknown, a2:unknown→supported, a3:unknown→unknown | 无前提／无合法判断 | insufficient → insufficient |
| iVt07TCkFM0 [18, 20] | complete | a1:unknown→unknown, a2:unknown→unknown, a3:unknown→supported | p1:unknown | insufficient → insufficient |
| z_6gVvQb2d0 [270, 272] | complete | a1:unknown→supported, a2:unknown→contradicted, a3:unknown→supported, a4:unknown→supported | p1:supported | insufficient → insufficient |
| gzDbaEs1Rlg [172, 174] | complete | a1:unknown→unknown, a2:unknown→unknown, a3:unknown→unknown | p1:unknown, p2:unknown, p3:unknown | insufficient → insufficient |
| GsAD1KT1xo8 [132, 134] | complete | a1:unknown→unknown, a2:supported→supported, a3:supported→unknown, a4:supported→unknown | p1:unknown, p2:unknown, p3:supported, p4:unknown | insufficient → insufficient |
| GsAD1KT1xo8 [98, 100] | complete | a1:unknown→unknown, a2:unknown→unknown | p1:supported, p2:supported, p3:supported, p4:unknown | insufficient → insufficient |

## 数字的边界

- 原子模型提案：`{"unknown": 13, "supported": 8, "contradicted": 1}`。
- 控制器原子判断：`{"unknown": 14, "supported": 7, "contradicted": 1}`。
- 控制器前提判断（单独分母）：`{"supported": 7, "unknown": 9}`。
- 依赖阻断规则计数：`{}`。
- 合法 JSON、局部引用和类型关系不能证明画面事实。语义精度保持未定义，不将 0 个反证写成 100% 精度。
- 固定旧失败案例用于开发回归，手工／助手审校的文本原子化不是自动解析能力。
- 没有重排、边界修改、新 mAP 或全 50 对收益；未授权自动补跑剩余 42 对。
- 逐项原模型提案、控制器规则及旧输出路径见同目录的 comparisons 案例数据。
