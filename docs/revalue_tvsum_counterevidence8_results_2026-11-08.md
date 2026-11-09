# TVSum 固定 8 例原子反证修复 v2：运行结果

## Material Passport

- Origin: academic-research-suite / experiment-agent / run.
- Verification: CPU 契约与运行收据已核验；视觉语义需另看逐例审查。
- 固定 8 对，涉及原 10 视频中的 7 条；不是全量性能实验。
- 相同 Qwen3.8-27B、旧帧/PTS、F、五维标准及阶段 token 上限。

## 运行与独立账本

- 8/8 次尝试，8/8 合法；零重试，1 个 TP4 worker。
- 实际已知 token 47981；计费／预留 token 47981/131072。
- worker 生命周期 466.653/900 秒；GPU 生命周期 1866.611/3600 秒。
- 历史 267 份文件哈希不变；旧 100 次账本独立且不转移剩余。
- 运行状态 `complete`；界限检查 `True`。

## 完整 8 例对照

| 视频与片段 | 新输出 | 原子判断（控制器） | 旧比较→新比较 |
|---|---|---|---|
| WxtbjNsCQ8A [200, 202] | complete | a1:unknown, a2:unknown | insufficient → insufficient |
| i3wAGJaaktw [22, 24] | complete | a1:unknown | invalid/unavailable → insufficient |
| AwmHb44_ouw [300, 302] | complete | a1:unknown, a2:unknown, a3:unknown | insufficient → insufficient |
| iVt07TCkFM0 [18, 20] | complete | a1:unknown, a2:unknown, a3:unknown | insufficient → insufficient |
| z_6gVvQb2d0 [270, 272] | complete | a1:unknown, a2:unknown, a3:unknown, a4:unknown | tie → insufficient |
| gzDbaEs1Rlg [172, 174] | complete | a1:unknown, a2:unknown, a3:unknown | insufficient → insufficient |
| GsAD1KT1xo8 [132, 134] | complete | a1:unknown, a2:supported, a3:supported, a4:supported | insufficient → insufficient |
| GsAD1KT1xo8 [98, 100] | complete | a1:unknown, a2:unknown | insufficient → insufficient |

## 数字的边界

- 原子模型提案：`{"contradicted": 2, "supported": 11, "unknown": 9}`。
- 控制器原子判断：`{"unknown": 19, "supported": 3}`。
- 合法 JSON、局部引用和类型关系不能证明画面事实。语义精度保持未定义，不将 0 个反证写成 100% 精度。
- 固定旧失败案例用于开发回归，手工／助手审校的文本原子化不是自动解析能力。
- 没有重排、边界修改、新 mAP 或全 50 对收益；未授权自动补跑剩余 42 对。
- 逐项原模型提案、控制器规则及旧输出路径见同目录的 comparisons 案例数据。
