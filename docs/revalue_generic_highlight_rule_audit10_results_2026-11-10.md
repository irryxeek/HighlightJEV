# 高光评分中间输出：10窗口规则审计结果

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run / validate
- Origin Date: 2026-11-10
- Verification Status: ANALYZED（运行与结构契约通过；规则语义仍有问题）
- Version Label: generic_highlight_rule_audit10_v1

## 已增加的输出

保留此前全部原始分数，新增独立结构化再判断。每个窗口保存：可见事实及局部帧引用、五维15项规则的supported／counterevidence／unknown／not_applicable状态、事实ID引用、简短说明、最终Yes/No、关键规则ID、背景使用方式。原问题、具体规则、8B模型、旧6帧和背景均保留；输出格式改为JSON并使用结构约束。

这是模型此次公开给出的可检查依据，**不能倒推出旧单token打分的真实内部过程，也不能据此认定某维度导致旧高分**。10个窗口为已知案例的事后诊断，不能计算或替代完整10视频mAP。

## 运行结果

10/10成功，150项规则全部输出，零失败、零重试。旧评分的10个目标全部输出Yes；新审计为5个Yes、5个No。规则状态为57 supported、26 counterevidence、32 unknown、35 not_applicable；这些数量不是价值分数。

| 视频／场景 | 3秒范围 | 原窗口P(Yes) | 新判断 |
|---|---|---:|---|
| 蜜蜂新闻，蜂群 | 51–54秒 | 0.996827 | No |
| 蜜蜂新闻，采访 | 57–60秒 | 0.999290 | Yes |
| 蜜蜂新闻，采访 | 60–63秒 | 0.999569 | Yes |
| 蜜蜂新闻，采访 | 63–66秒 | 0.999739 | No |
| 换胎视频，车内人物 | 6–9秒 | 0.999842 | No |
| 换胎视频，零食展示 | 123–126秒 | 0.999942 | Yes |
| 换胎视频，零食展示 | 129–132秒 | 0.999925 | No |
| 换胎视频，操作对照 | 354–357秒 | 0.904651 | Yes |
| 换胎视频，操作对照 | 366–369秒 | 0.991423 | No |
| 火车事故，现场对照 | 9–12秒 | 0.999665 | Yes |

这是3秒窗口原始概率，不是导出后的2秒片段分数。6个疑似高分误判中3个仍为Yes，3个为No；4个对照中2个也被判No。不能据此声称结构化输出已改善性能。旧分数只在审计输出冻结后由CPU拼接展示，没有告诉诊断模型原分数、旧Yes/No或GT。

## 现在能定位到的具体问题

### 1. 普通可见事实被升级为观看价值

蜜蜂新闻57–60秒，模型记录了受访者微笑、台标和署名，随后给出：

| 规则 | 新审计状态 | 模型实际简短说明 | 需要核查的问题 |
|---|---|---|---|
| I2，信息贡献 | supported | Identifies source and context for the footage. | 来源署名是否为当前新闻提供了值得优先保留的新信息？ |
| E2，情绪贡献 | supported | Smile and animated expression show intensity. | 微笑本身是否足以证明有意义的强度／变化？ |
| S1，视觉事件 | supported | Visible outdoor setting with trees and building. | 普通室外背景为何被当成视觉揭示／变化？ |
| S2，视觉贡献 | supported | Scene provides contextual visual information. | 可见环境与值得观看的视觉事件没有明确区分。 |

60–63秒又将“Smile shows specific emotional intensity beyond neutrality”作为E2支持，最终Yes。没有音频，不能验证讲话内容重要。它们与前轮“普通采访被抬高”的解释相符，但只能说明本次结构化再判断的显式依据。

### 2. 同样的升级出现在零食展示

换胎视频123–126秒：I2以“Identifies product, useful for understanding context”认定品牌有信息贡献；E2以笑容支持情绪强度；S1/S2把微笑和包装解释为视觉对比和独特观看体验。最终理由为“Visible product branding, smiling expression, and visual contrast make this moment worth retaining.”

问题不只是有没有识别出物体或表情，而是从“看见了”到“对本片有保留价值”的依据不足。摘要提到换胎并未自动解决这一跳跃。不能把品牌可读性或微笑程度直接等同于主要事件的重要性。

### 3. 分项规则与最终决策的衔接不稳定

蜂群51–54秒：模型正确描述蜂群，I2支持信息贡献、S2支持发现价值，却最终No，理由称缺乏动作、情绪或结果。当前标准没有要求这三类必须出现，也没有要求五维全部满足。这是额外添加必要条件的迹象。

零食129–132秒也给E2、S2 supported，却以缺乏完成、动作细节或情境变化判No；与相邻123–126秒的Yes形成对照。场景并非完全相同，不能称为同一输入自相矛盾，但说明“哪些支持足够保留、哪些不够”的决策门槛没有得到一致解释。

### 4. 结构合规不代表事实或引用准确

本轮无悬空事实ID、supported无引用或“Yes但无贡献层支持”的机械警告；但事实→价值的语义跳跃并不会因此消失。部分“No visible completion”被记为counterevidence，说明“没看到”和“存在直接反证”的边界仍需核查。

所有生成的帧引用均集中在0–2，尽管每请求确有6张原帧。不能因此断言后三帧没被模型读取，但也不能把这些引用当作已验证的精准帧定位。需区分“ID在合法范围内”与“被引用帧确实支持该事实”；本次没有修改输入帧来修复索引理解。

## 成本、验证和结束状态

- 独立尝试10/10，零重试，30,437 input+output token；上限40,960。
- 单次worker、GPU0一张，生命周期257.804238秒，约4分18秒；上限900秒。
- 4项新增CPU契约测试、全部10目标的原生处理器／旧像素／PTS核对及XGrammar schema编译通过；最大输入2243token，输出上限1536，合计不超过4096。
- 原模型引擎和媒体处理逐字节复用；来源绑定审查建议已在冻结前补齐。
- worker与driver退出0，无所属残留进程，GPU0恢复15MiB、0%利用率；北京时间2026-11-10 **05:28:41**结束。
- 成本与前轮背景实验1,390次／2,556,639token／693.308218秒分开，不挪用历史余额。后处理新增模型调用0，未推送。

## 使用这些输出的边界

本轮已提供用户要求的可检查记录。它支持下一步检查“事实→观看贡献”的具体门槛，以及五维结果如何形成总体决定；还不能证明哪条规则造成旧分数，更不能把规则文本当作模型内部计算的忠实解释。若要确定某维度的因果贡献，需要另做控制干预；本轮没有启动消融或再跑全量。

统计风险检查覆盖11/11：原10视频结果仍全量报告；这里不从案例推断总体或逐维准确率；明确事后选例与开发集已见；不按新输出删例或条件化分析；不报告伪精确率；不将极端案例变化当总体改善；10目标全部保留；完整150规则可查；方案与输出合同先冻结；不把公开解释当内部因果；旧分数在新输出冻结后才拼接。未知事实引用和模型误识别仍为未解决的语义问题。

## 产物

- [10窗口完整逐项记录](artifacts/revalue_generic_highlight_rule_audit10_2026-11-10/case_details.md)：每条事实、15项状态、引用、理由与背景使用方式。
- [结构化对比JSON](artifacts/revalue_generic_highlight_rule_audit10_2026-11-10/audit_comparison.json)、[冻结协议](revalue_generic_highlight_rule_audit10_protocol_2026-11-10.md)、实现（本地资料：`$MERIT_ROOT/experiments/revalue_generic_highlight_rule_audit_v1/README.md`）。
- 原始提示、schema、响应、帧轨迹、预算与退出收据：`$ZEROSHOT_ARTIFACT_ROOT/revalue_generic_highlight_rule_audit10_v1_2026-11-10/`。
- [前轮全片背景结果](revalue_generic_highlight_tvsum_context10_results_2026-11-10.md)保持不变：59.3434，对照具体版59.6181、REZE61.3167。

审计输出SHA256：`7da0b07310c5418cbddadb31c8543c6b01c6a0ed6affec3d343bfe9d74763495`。
