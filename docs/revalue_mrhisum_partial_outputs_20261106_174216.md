# Mr.HiSum固定40视频：运行中输出预览

快照时间：2026-11-06 17:42:16（北京时间）。

已完成三组的固定清单前缀：4/40视频；已完成请求53/440，已发起54。本次只做CPU查看，原后台实验继续，没有新增诊断模型调用。

## 阅读范围

以下展示模型选出的5秒重排建议及模型给出的简短理由。它们尚未与GT评价，也没有独立人工语义核验。合法表示格式和来源映射通过；不表示选片正确。这些至多5个建议并非最终15%摘要。官方指标按原协议在完整40预测冻结后计算。

| 视频 | D：无记忆（秒） | F：旧读取（秒） | F-read：新读取（秒） | 新旧读取导致的5秒得分变化数 |
|---|---|---|---|---:|
| video_23234 | 145–150；150–155；55–60；10–15；120–125 | 120–125；145–150；10–15；55–60；5–10 | 120–125；145–150；55–60；10–15；5–10 | 2 |
| video_26502 | 弃权，回退B0_5s_flat | 弃权，回退B0_5s_flat | 弃权，回退B0_5s_flat | 0 |
| video_9757 | 85–90；10–15；80–85；15–20；140–144 | 85–90；10–15；5–10；70–75；45–50 | 85–90；10–15；15–20；70–75；35–40 | 8 |
| video_6458 | 20–25；140–145；160–165；25–30；155–160 | 20–25；140–145；160–165；25–30；10–15 | 20–25；140–145；160–165；25–30；0–5 | 32 |

表格按模型原始输出顺序列出，tier并列信息保留在下方。CPU导出对同层建议沿用B0稳定顺序；原始pick次序不应误读为严格先后优劣。

## video_23234（160秒）

事实读取token：998→1000；视图变化：True。

### D：complete

- 145–150秒；tier=0；事实引用=[]。模型理由：Visible peak of emotional distress with a contorted, anguished facial expression.
- 150–155秒；tier=1；事实引用=[]。模型理由：Close-up reveals a tearful, shocked reaction to the preceding outburst.
- 55–60秒；tier=2；事实引用=[]。模型理由：Distinctive physical gesture of pointing during a heated confrontation.
- 10–15秒；tier=3；事实引用=[]。模型理由：Initial tense exchange establishing the conflict between the two characters.
- 120–125秒；tier=4；事实引用=[]。模型理由：Sustained emotional intensity as the confrontation reaches its climax.

### F：complete

- 120–125秒；tier=0；事实引用=['g06.f00']。模型理由：Young woman's face shows visible distress and tears during the confrontation.
- 145–150秒；tier=1；事实引用=['g07.f00']。模型理由：Older woman's expression shifts to intense, pained emotion.
- 10–15秒；tier=2；事实引用=['g00.f01']。模型理由：Camera angle shifts and the woman moves away in a blur.
- 55–60秒；tier=3；事实引用=['g02.f00']。模型理由：Woman gestures emphatically while speaking in a wide shot.
- 5–10秒；tier=4；事实引用=['g00.f00']。模型理由：Sustained conversational posture establishes the initial scene context.

### F_read：complete

- 120–125秒；tier=0；事实引用=['g06.f00']。模型理由：Young woman appears distressed and tearful during the confrontation.
- 145–150秒；tier=1；事实引用=['g07.f00']。模型理由：Woman shows a visibly distressed and pained facial expression.
- 55–60秒；tier=2；事实引用=['g02.f00']。模型理由：Woman gestures emphatically while speaking in a heated exchange.
- 10–15秒；tier=3；事实引用=['g00.f01']。模型理由：Camera angle shifts as the woman looks down and moves away.
- 5–10秒；tier=4；事实引用=['g00.f00']。模型理由：Sustained conversational posture between the two women.

## video_26502（159秒）

事实读取token：999→996；视图变化：True。

### D：complete

模型未给出建议，按冻结规则回退B0_5s_flat。理由：The video consists of a static title card with no visible action, change, or event to highlight.

### F：complete

模型未给出建议，按冻结规则回退B0_5s_flat。理由：The video consists of a static logo card with no visible action, change, or event to highlight.

### F_read：complete

模型未给出建议，按冻结规则回退B0_5s_flat。理由：The video consists entirely of a static logo card with no visible action, change, or event.

## video_9757（144秒）

事实读取token：983→1024；视图变化：True。

### D：complete

- 85–90秒；tier=0；事实引用=[]。模型理由：Displays the final profit summary of 8,047 gold earned over six days.
- 10–15秒；tier=1；事实引用=[]。模型理由：Shows the opening skit with the 'can i haz gold' beggar interaction.
- 80–85秒；tier=2；事实引用=[]。模型理由：Shows the auction house interface with a list of successful sales.
- 15–20秒；tier=3；事实引用=[]。模型理由：Demonstrates the auction house interface used for the gold-making strategy.
- 140–144秒；tier=4；事实引用=[]。模型理由：Displays the closing screen with a final message to the viewer.

### F：complete

- 85–90秒；tier=0；事实引用=['g05.f00']。模型理由：Displays the final 8,047G profit calculation, the video's key outcome.
- 10–15秒；tier=1；事实引用=['g00.f01']。模型理由：Character engulfed in flames, a distinctive and dramatic visual event.
- 5–10秒；tier=2；事实引用=['g00.f00']。模型理由：Comedic dialogue exchange with 'can i haz gold?' speech bubbles.
- 70–75秒；tier=3；事实引用=['g04.f00']。模型理由：Shows the player creating an auction listing, a crucial step.
- 45–50秒；tier=4；事实引用=['g02.f01']。模型理由：Player searches the Auction House for specific enchant items.

### F_read：complete

- 85–90秒；tier=0；事实引用=['g04.f01']。模型理由：Displays the final profit summary, the key outcome of the video.
- 10–15秒；tier=1；事实引用=['g00.f01']。模型理由：Shows a character engulfed in flames, a distinctive visual event.
- 15–20秒；tier=2；事实引用=['g01.f00']。模型理由：Shows the market interface with item lists and prices.
- 70–75秒；tier=3；事实引用=['g04.f00']。模型理由：Shows the player creating an auction house listing.
- 35–40秒；tier=4；事实引用=['g02.f00']。模型理由：Shows the player browsing the vendor item list.

## video_6458（273秒）

事实读取token：973→972；视图变化：True。

### D：complete

- 20–25秒；tier=0；事实引用=[]。模型理由：Demonstrates a pull-up rep on the outdoor bar.
- 140–145秒；tier=0；事实引用=[]。模型理由：Shows a dynamic pull-up movement on the bar.
- 160–165秒；tier=0；事实引用=[]。模型理由：Captures a pull-up rep with clear body extension.
- 25–30秒；tier=1；事实引用=[]。模型理由：Shows a pull-up rep in the early exercise set.
- 155–160秒；tier=1；事实引用=[]。模型理由：Shows a pull-up rep in the later exercise set.

### F：complete

- 20–25秒；tier=0；事实引用=['g00.f01']。模型理由：Demonstrates the core pull-up exercise with visible body movement.
- 140–145秒；tier=0；事实引用=['g04.f00']。模型理由：Shows a distinct pull-up execution sequence on the wooden bar.
- 160–165秒；tier=0；事实引用=['g04.f00']。模型理由：Captures the peak of a pull-up rep with clear form.
- 25–30秒；tier=1；事实引用=['g00.f01']。模型理由：Shows the transition from hanging to standing after exercise.
- 10–15秒；tier=2；事实引用=[]。模型理由：Displays the studio branding and title card for context.

### F_read：complete

- 20–25秒；tier=0；事实引用=['g00.f01']。模型理由：Demonstrates the core pull-up exercise with visible body movement.
- 140–145秒；tier=0；事实引用=['g04.f00']。模型理由：Shows a distinct pull-up execution phase on the wooden bar.
- 160–165秒；tier=0；事实引用=['g04.f00']。模型理由：Captures the peak of a pull-up rep, showing full extension.
- 25–30秒；tier=1；事实引用=['g00.f01']。模型理由：Shows the transition from hanging to standing after the set.
- 0–5秒；tier=2；事实引用=['g00.f00']。模型理由：Establishes the outdoor gym context and the instructor's presence.

## 当前可支持的结论

- 4/4份事实读取视图发生变化；3/4个视频的F与F-read导出分数不同。读取干预已实际进入预测。
- 尚不能判断F-read精度优于F或D；此预览不计算部分mAP/F1，也不按结果筛选后续样本。
- 模型选入片头/字幕/结束界面、或称视频静态的情况，仅是待核查行为；这里没有把模型解释当成真实视频结论。

完整可审计快照：`$ZEROSHOT_ARTIFACT_ROOT/revalue_mrhisum_memory_read_40v_27b_v1_2026-11-06/progress_previews/20261106_174216/partial_outputs.json`；同目录保留账本快照。
