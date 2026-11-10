# 同10窗口：原规则与贡献门槛修订逐项对照

完整10个事后诊断窗口；不计算准确率或全视频mAP。模型自报事实与引用未作新的独立人工标注。

“有贡献支持却判No”是输出字段一致性检查，不代表所声称的贡献真实成立。原输出均保留。

## 1. Se3oxnaPsz0，窗口17，51–54秒

**决定：No → Yes**

原依据：Visible bee swarm provides diagnostic detail and discovery value, but lacks action, emotion, or outcome to justify retention as a highlight.

新依据：Diagnostic view of bee swarm inside structure adds unique visual information.

原贡献支持：I2, S2；新贡献支持：I2, S2。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | counterevidence：No visible completion, transition, or state change shown. | counterevidence：No visible completion, transition, or outcome established. | — |
| O2 | counterevidence：No attempt or material change resolved in visible frames. | counterevidence：No resolved attempt or material change shown. | — |
| O3 | not_applicable：No other phase or comparable result visible for comparison. | not_applicable：No other phase or comparable result visible for comparison. | — |
| I1 | supported：Visible bees in structure provide diagnostic detail of hive location. | supported：Visible diagnostic detail: bees in confined wooden space. | f1 |
| I2 | supported：Adds context to bee removal or inspection process. | supported：Reveals key step: bee swarm location within structure. | f1 |
| I3 | not_applicable：No other moment for comparison within this segment. | not_applicable：No other moment for comparison visible. | — |
| E1 | not_applicable：No discernible human expression or reaction visible. | not_applicable：No discernible human expression or reaction visible. | — |
| E2 | not_applicable：No intensity or change in emotion attributable to any participant. | not_applicable：No marked reaction or change attributable to any subject. | — |
| E3 | not_applicable：No baseline or other reaction for comparison. | not_applicable：No baseline or comparison for emotional reaction. | — |
| A1 | not_applicable：No participants or interaction visible for action identification. | not_applicable：No observable action, interaction, or diagnostic phase. | — |
| A2 | not_applicable：No execution detail, mistake, or diagnostic phase observed. | not_applicable：No execution detail, mistake, or meaningful step visible. | — |
| A3 | not_applicable：No action phase to support claimed difference or significance. | not_applicable：No observed action or phase for comparative significance. | — |
| S1 | supported：Visible reveal of dense bee swarm inside wooden structure. | supported：Visible transformation: bees revealed in confined space. | f1 |
| S2 | supported：Adds discovery value to understanding bee removal context. | supported：Diagnostic view adds discovery: swarm location and density. | f1 |
| S3 | not_applicable：No other scene or state for visual contrast or comparison. | not_applicable：No other scene or state for visual contrast. | — |

**原可见事实（模型报告）**

- f1，帧[1, 2]：Close-up of dense swarm of bees inside wooden structure.

原关键规则：I1, I2, S1, S2。

原背景使用：Background context suggests bee removal theme, but segment lacks sufficient event value beyond visual observation.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[1, 2]：Close-up of dense swarm of bees inside wooden structure.

新关键规则：I1, I2, S1, S2。

新背景使用：Background context irrelevant; segment stands alone as informative visual reveal.

新运行时结构警告：无。

## 2. Se3oxnaPsz0，窗口19，57–60秒

**决定：Yes → No**

原依据：Provides context, visible emotion, and setting with identifiable source credit.

新依据：Credit graphic and woman’s expression provide minimal context or emotional value for retention.

原贡献支持：I2, E2, S2；新贡献支持：I2。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | counterevidence：No visible completion, failure, or transition established. | counterevidence：No visible completion, failure, or transition established. | f1 |
| O2 | counterevidence：No material change or resolution of attempt observed. | counterevidence：No material change or resolved attempt observed. | f1 |
| O3 | unknown：No comparable phase or result for comparison available. | not_applicable：No other phase or comparable result visible for comparison. | — |
| I1 | supported：Credits and channel branding provide specific context. | supported：Visible credit identifies source and location of footage. | f2 |
| I2 | supported：Identifies source and context for the footage. | supported：Reveals videographer’s name and affiliation for context. | f2 |
| I3 | unknown：No other moment for comparison to establish novelty. | not_applicable：No other moment for comparison within this segment. | — |
| E1 | supported：Visible facial expression indicates engagement. | supported：Visible smile and speaking expression on woman’s face. | f1 |
| E2 | supported：Smile and animated expression show intensity. | counterevidence：Ordinary smile lacks event-linked intensity or change. | f1 |
| E3 | unknown：No baseline or comparison to establish relative intensity. | not_applicable：No baseline or comparison reaction visible. | — |
| A1 | supported：Woman speaking and smiling indicates interaction. | not_applicable：No observable action or interaction beyond speaking. | — |
| A2 | counterevidence：No distinctive execution detail or mistake observed. | not_applicable：No diagnostic step or meaningful mistake visible. | — |
| A3 | unknown：No other action for comparison to establish significance. | not_applicable：No action phase or comparative execution supported. | — |
| S1 | supported：Visible outdoor setting with trees and building. | not_applicable：No specific visual change or transformation observed. | — |
| S2 | supported：Scene provides contextual visual information. | not_applicable：No diagnostic or distinctive visual meaning added. | — |
| S3 | unknown：No other scene for comparison to establish visual contrast. | not_applicable：No other scene or state for visual contrast. | — |

**原可见事实（模型报告）**

- f1，帧[0, 1, 2]：Woman wearing pink cap and glasses smiles while speaking outdoors.
- f2，帧[0, 1, 2]：Lower third graphic credits 'Al Signori, freelance videographer, Bisbee'.
- f3，帧[0, 1, 2]：Background shows trees and a building with stacked wood.
- f4，帧[0, 1, 2]：Woman’s facial expression shows engaged, animated conversation.
- f5，帧[0, 1, 2]：News channel branding 'ONLY ON KOLD NEWS 13' visible.
- f6，帧[0, 1, 2]：Scene appears to be part of a news report or interview segment.

原关键规则：I1, I2, E1, E2, S1。

原背景使用：Background context confirms this is a news segment, but no event completion or action is visible.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[0, 1, 2]：Woman wearing pink cap and glasses smiles while speaking outdoors.
- f2，帧[0, 1, 2]：Lower third graphic credits 'Al Signori, freelance videographer, Bisbee'.
- f3，帧[0, 1, 2]：Background shows trees and a building with stacked wood.

新关键规则：I1, I2, E1。

新背景使用：Background context (trees, building) is irrelevant to highlight value; no action or outcome established.

新运行时结构警告：无。

## 3. Se3oxnaPsz0，窗口20，60–63秒

**决定：Yes → Yes**

原依据：Graphic provides identity and context; smile adds emotional engagement; visual reveal enhances informational value.

新依据：Graphic identifies subject and context, adding diagnostic value beyond scenery.

原贡献支持：I2, E2, S2；新贡献支持：I2, S2。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | counterevidence：No visible completion or state transition observed. | counterevidence：No visible completion, failure, or transition shown. | f1, f2 |
| O2 | counterevidence：No material change or resolved attempt demonstrated. | counterevidence：No material change or resolved attempt observed. | f1, f2 |
| O3 | unknown：No comparable phase or result for comparison available. | not_applicable：No other phase or comparable result visible for comparison. | — |
| I1 | supported：Graphic provides specific identity and news source context. | supported：Graphic clearly identifies subject and news outlet. | f2 |
| I2 | supported：Identifies speaker and situates segment in rural news context. | supported：Reveals specific person and media context beyond generic setting. | f2 |
| I3 | unknown：No other moment for comparison to establish novelty. | not_applicable：No other moment for comparison within this segment. | — |
| E1 | supported：Visible smile indicates discernible facial expression. | supported：Visible facial expression and posture of speaking woman. | f1 |
| E2 | supported：Smile shows specific emotional intensity beyond neutrality. | counterevidence：No marked, event-linked reaction beyond ordinary speaking. | f1 |
| E3 | unknown：No baseline or comparison to establish relative emotional priority. | not_applicable：No baseline or comparison reaction visible for evaluation. | — |
| A1 | supported：Woman is visibly speaking to camera, establishing interaction. | supported：Woman is visibly speaking to camera, establishing interaction. | f1 |
| A2 | counterevidence：No diagnostic step or distinctive execution detail observed. | counterevidence：No diagnostic step or meaningful mistake in action observed. | f1 |
| A3 | unknown：No other action for comparison to establish significance. | not_applicable：No other action or phase for comparative support. | — |
| S1 | supported：Graphic overlay reveals contextual information not previously visible. | supported：Graphic reveal adds diagnostic context to the scene. | f2 |
| S2 | supported：Graphic adds meaning by identifying speaker and news source. | supported：Lower third provides distinctive meaning beyond scenery. | f2 |
| S3 | unknown：No other scene for comparison to establish visual contrast. | not_applicable：No other scene or state for visual contrast or comparison. | — |

**原可见事实（模型报告）**

- f1，帧[0, 1]：Woman wearing purple cap and glasses speaks outdoors.
- f2，帧[2]：Lower third graphic identifies her as Jane Hewitt, Kold News 13.
- f3，帧[1, 2]：Woman smiles while speaking, showing engaged expression.
- f4，帧[0, 1, 2]：Background includes building and trees, suggesting rural setting.
- f5，帧[0, 1, 2]：Camera remains steady, focused on speaker’s face and upper body.
- f6，帧[2]：Graphic overlay indicates news segment context.

原关键规则：I1, I2, E1, E2, S1。

原背景使用：Background context supports rural news segment interpretation; no resolution or action value, but identification and emotion justify retention.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[0, 1]：Woman wearing purple cap and glasses speaks outdoors.
- f2，帧[2]：Lower third graphic identifies her as Jane Hewitt, Kold News 13.
- f3，帧[0, 1, 2]：Background shows rustic building and trees.

新关键规则：I1, I2, S2。

新背景使用：Background provides setting, but no action or outcome is visible. Identification and context are sufficient for retention.

新运行时结构警告：无。

## 4. Se3oxnaPsz0，窗口21，63–66秒

**决定：No → Yes**

原依据：Identifies speaker and context, but lacks emotional intensity, action detail, or visual novelty to justify retention.

新依据：Provides specific identity, profession, and context with visible speaking action and background.

原贡献支持：I2；新贡献支持：I2。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | counterevidence：No visible completion, failure, or transition shown. | counterevidence：No visible completion, failure, or state transition shown. | f1, f5 |
| O2 | counterevidence：No material change or resolved attempt observed. | counterevidence：No material change or resolved attempt observed. | f1, f5 |
| O3 | unknown：No comparable phase or result for comparison. | unknown：No other comparable phase or result visible for comparison. | — |
| I1 | supported：Visible identification of speaker and role. | supported：Visible identification of subject and role provides specific information. | f1, f3 |
| I2 | supported：Provides context for who is speaking and why. | supported：Reveals her identity and profession beyond generic context. | f1, f3 |
| I3 | unknown：No other moment for comparison to establish novelty. | unknown：No other moment for comparison to establish novelty. | — |
| E1 | supported：Visible facial expression and posture. | supported：Discernible facial expression and posture visible. | f2 |
| E2 | counterevidence：Smile is generic, no intensity or change shown. | counterevidence：Smile is ordinary, no marked event-linked reaction shown. | f2 |
| E3 | unknown：No baseline or comparison for emotional difference. | unknown：No baseline or comparison to establish grounded difference. | — |
| A1 | supported：Action of speaking to camera is visibly established. | supported：Action of speaking to camera is visibly established. | f1, f5 |
| A2 | counterevidence：No distinctive execution detail or mistake observed. | counterevidence：No diagnostic step or meaningful mistake observed. | f5 |
| A3 | unknown：No other action for comparison to establish significance. | unknown：No other action for comparison to establish significance. | — |
| S1 | supported：Visible background context including building and trees. | supported：Visible background context adds environmental detail. | f4 |
| S2 | counterevidence：No visual transformation or unusual scene observed. | counterevidence：No transformation or unusual scene; ordinary appearance. | f4 |
| S3 | unknown：No other scene for comparison to establish visual difference. | unknown：No other scene for comparison to establish visual difference. | — |

**原可见事实（模型报告）**

- f1，帧[0, 1, 2]：Woman identified as Jane Hewitt, farmer, speaking outdoors.
- f2，帧[0, 1, 2]：She wears pink cap, glasses, and scarf, smiling slightly.
- f3，帧[0, 1, 2]：News graphic shows 'ONLY ON KOLD NEWS 13' and her title.
- f4，帧[0, 1, 2]：Background includes building, trees, and stacked wood.
- f5，帧[0, 1, 2]：Her mouth moves, suggesting she is speaking to camera.
- f6，帧[0, 1, 2]：Lower third graphic remains static throughout segment.

原关键规则：I1, I2, A1, S1。

原背景使用：Background provides setting but no unique event or transformation. No added value beyond basic identification.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[0, 1, 2]：Woman identified as Jane Hewitt, farmer, speaking outdoors.
- f2，帧[0, 1, 2]：She wears pink cap, glasses, and scarf, smiling slightly.
- f3，帧[0, 1, 2]：News graphic shows 'ONLY ON KOLD NEWS 13' and her title.
- f4，帧[0, 1, 2]：Background includes building, trees, and stacked wood.
- f5，帧[0, 1, 2]：Her mouth moves, suggesting she is speaking to camera.
- f6，帧[0, 1, 2]：Lower third graphic remains static throughout segment.

新关键规则：I1, I2, A1, S1。

新背景使用：Background context is sparse but visible; no motion or emotion adds value beyond identification.

新运行时结构警告：无。

## 5. J0nA4VgnoCo，窗口2，6–9秒

**决定：No → No**

原依据：Smiling occupants and sunlight add mood, but no unique event, action, or information justifies retention.

新依据：No outcome, information, or event-linked emotion established to justify retention.

原贡献支持：E2, S2；新贡献支持：无。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | counterevidence：No visible completion, transition, or failure observed. | counterevidence：No visible completion, transition, or outcome established. | f1, f2 |
| O2 | counterevidence：No material change or resolved attempt demonstrated. | counterevidence：No material change or resolved attempt observed. | f1, f2 |
| O3 | unknown：No comparable phase or result visible for comparison. | not_applicable：No other comparable phase or result visible for comparison. | — |
| I1 | counterevidence：No diagnostic detail or crucial step visible. | counterevidence：No specific diagnostic detail or crucial step visible. | f1, f2 |
| I2 | counterevidence：No process or situation explanation beyond presence. | counterevidence：No substantive fact beyond identity or generic context. | f1, f2 |
| I3 | unknown：No other moment for comparison or novelty claim. | not_applicable：No other moment for comparison to establish novelty. | — |
| E1 | supported：Visible smiles and engaged expressions from both occupants. | supported：Visible expressions on both individuals. | f1, f2 |
| E2 | supported：Intensity of smiles suggests positive emotional state. | counterevidence：Smiles are ordinary, no event-linked reaction established. | f1, f2 |
| E3 | unknown：No baseline or comparison reaction visible for intensity. | not_applicable：No baseline or comparison to establish grounded difference. | — |
| A1 | supported：Action of driving and smiling by occupants visible. | supported：Man driving, woman passenger — correct participants visible. | f1, f2 |
| A2 | counterevidence：No distinctive execution detail or mistake observed. | counterevidence：No diagnostic step, mistake, or distinctive execution visible. | f1, f2 |
| A3 | unknown：No other action for comparative significance visible. | not_applicable：No other action or phase for comparative support. | — |
| S1 | supported：Sunlight and interior reveal context and mood. | supported：Sunlit car interior with visible background scenery. | f3 |
| S2 | supported：Visuals add mood and setting context for viewing. | counterevidence：No transformation, reveal, or diagnostic view established. | f3 |
| S3 | unknown：No other scene for visual contrast or comparison. | not_applicable：No other scene for comparison to establish visual priority. | — |

**原可见事实（模型报告）**

- f1，帧[0, 1, 2]：Man in sunglasses smiles while driving.
- f2，帧[0, 1, 2]：Woman in striped shirt smiles beside driver.
- f3，帧[0, 1, 2]：Both occupants appear happy and engaged.
- f4，帧[0, 1, 2]：Car interior visible with seatbelts and steering wheel.
- f5，帧[0, 1, 2]：Sunlight visible through car windows.
- f6，帧[0, 1, 2]：Camera angle suggests self-recorded video.

原关键规则：E1, E2, S1, S2。

原背景使用：Background context shows varied scenes, but this segment lacks unique event or information to justify retention.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[0, 1, 2]：Man in sunglasses smiles while driving.
- f2，帧[0, 1, 2]：Woman in striped shirt smiles beside driver.
- f3，帧[0, 1, 2]：Car interior visible with sunlit background.

新关键规则：O1, O2, I1, I2, E2。

新背景使用：Background context irrelevant; no unique event or diagnostic detail visible.

新运行时结构警告：无。

## 6. J0nA4VgnoCo，窗口41，123–126秒

**决定：Yes → Yes**

原依据：Visible product branding, smiling expression, and visual contrast make this moment worth retaining.

新依据：Brand reveal and product display offer clear diagnostic value beyond routine visuals.

原贡献支持：I2, E2, S2；新贡献支持：I2, S2。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | counterevidence：No completion, failure, or state transition observed. | counterevidence：No completion, failure, or state transition visible. | f1, f2 |
| O2 | counterevidence：No resolved attempt or material change in situation. | counterevidence：No material change or resolved attempt observed. | f1, f2 |
| O3 | unknown：No comparable phase or result for comparison. | not_applicable：No other comparable phase or result visible. | — |
| I1 | supported：Visible product branding adds specific information. | supported：Brand name 'Cadbury Mini Eggs' clearly visible. | f1 |
| I2 | supported：Identifies product, useful for understanding context. | supported：Specific product identity adds substantive information. | f1 |
| I3 | unknown：No other moment for comparison to establish novelty. | not_applicable：No other moment for comparison visible. | — |
| E1 | supported：Visible smile on woman’s face. | supported：Discernible smile on woman’s face. | f2 |
| E2 | supported：Intensity of smile suggests positive emotion. | counterevidence：Ordinary smile lacks event-linked intensity or change. | f2 |
| E3 | unknown：No baseline or comparison to establish emotional difference. | not_applicable：No baseline or comparison reaction visible. | — |
| A1 | supported：Action of holding package clearly established. | supported：Woman visibly holding product in car setting. | f1 |
| A2 | counterevidence：No distinctive execution detail or mistake observed. | counterevidence：No diagnostic step or meaningful mistake observed. | f1 |
| A3 | unknown：No other action for comparison to establish significance. | not_applicable：No other action or phase for comparison visible. | — |
| S1 | supported：Visible smile and candy package create visual contrast. | supported：Product packaging clearly revealed to viewer. | f1 |
| S2 | supported：Emotional expression adds distinctive viewing experience. | supported：Concrete reveal of branded item adds discovery value. | f1 |
| S3 | unknown：No other scene for comparison to establish visual difference. | not_applicable：No other scene or state for contrast visible. | — |

**原可见事实（模型报告）**

- f1，帧[0, 1, 2]：Woman in car holds Cadbury Mini Eggs package.
- f2，帧[1, 2]：Woman smiles broadly while holding candy package.
- f3，帧[0, 1, 2]：Car interior visible with window showing residential street.
- f4，帧[0, 1, 2]：Woman’s striped shirt and dark hair visible.
- f5，帧[0, 1, 2]：Package label clearly shows 'Mini Eggs' branding.
- f6，帧[0, 1, 2]：Camera angle suggests self-shot or handheld recording.

原关键规则：I1, I2, E1, E2, S1。

原背景使用：Background context (car, residential street) supports interpretation but does not override local evidence.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[0, 1, 2]：Woman in car holds Cadbury Mini Eggs package.
- f2，帧[0, 1, 2]：Woman smiles broadly while holding candy package.
- f3，帧[0, 1, 2]：Car interior visible with window showing residential street.

新关键规则：I1, I2, S1, S2。

新背景使用：Background context irrelevant; segment stands on visible product and expression alone.

新运行时结构警告：无。

## 7. J0nA4VgnoCo，窗口43，129–132秒

**决定：No → Yes**

原依据：Smiling face and candy reveal are visible, but no completion, action detail, or contextual change justifies retention.

新依据：Brand reveal and product display offer diagnostic value and visual novelty.

原贡献支持：E2, S2；新贡献支持：I2, S2。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | counterevidence：No visible completion, failure, or state transition shown. | counterevidence：No completion, failure, or state transition visible. | — |
| O2 | counterevidence：No resolved attempt or material change observed. | counterevidence：No resolved attempt or material change observed. | — |
| O3 | not_applicable：No other phase or comparable result visible for comparison. | not_applicable：No other comparable result or phase observed. | — |
| I1 | not_applicable：No diagnostic detail or crucial step visible beyond object display. | supported：Brand name clearly visible and identifiable. | f6 |
| I2 | not_applicable：No process or situation requiring additional information shown. | supported：Reveals specific product identity beyond generic context. | f6 |
| I3 | not_applicable：No other moment for comparison to establish novelty. | not_applicable：No other moment for comparison available. | — |
| E1 | supported：Visible smile on woman’s face indicates discernible expression. | supported：Discernible smile on woman’s face visible. | f2 |
| E2 | supported：Intensity of smile suggests specific emotional reaction. | counterevidence：Smile lacks event-linked reaction or marked change. | — |
| E3 | not_applicable：No baseline or other reaction visible for comparison. | not_applicable：No baseline or comparison reaction observed. | — |
| A1 | supported：Action of holding and shaking candy package is visibly established. | supported：Action of holding candy package visibly established. | f1 |
| A2 | not_applicable：No diagnostic detail or meaningful mistake observed. | counterevidence：No diagnostic step, mistake, or distinctive execution. | — |
| A3 | not_applicable：No other action or phase for comparative significance. | not_applicable：No other action or phase for comparison. | — |
| S1 | supported：Visible candy package and smiling face constitute a visual reveal. | supported：Brand reveal adds concrete visual discovery. | f6 |
| S2 | supported：Smiling face and candy package add emotional and visual meaning. | supported：Transformation from hidden to revealed product identity. | f6 |
| S3 | not_applicable：No other scene or state for visual contrast or comparison. | not_applicable：No other scene or state for comparison. | — |

**原可见事实（模型报告）**

- f1，帧[0]：Woman holds colorful candy package inside car.
- f2，帧[1]：Woman smiles broadly while holding candy package.
- f3，帧[2]：Woman shakes candy package slightly while smiling.

原关键规则：E1, E2, S1, S2, A1。

原背景使用：Background context shows car interior and outdoor setting, but no event progression or unique action supports highlight retention.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[0, 1, 2]：Woman holds colorful 'Sour Patch Kids' candy package.
- f2，帧[0, 1, 2]：Woman smiles broadly while holding candy package.
- f3，帧[0, 1, 2]：Car interior visible with seatbelt and window.
- f4，帧[0, 1, 2]：Background shows parked car and residential street.
- f5，帧[0, 1, 2]：Woman’s blue-and-white striped shirt and necklace visible.
- f6，帧[0, 1, 2]：Candy package brand name clearly readable.

新关键规则：I1, I2, S1, S2, A1。

新背景使用：Background context irrelevant; no contextual linkage to other events or phases.

新运行时结构警告：无。

## 8. J0nA4VgnoCo，窗口118，354–357秒

**决定：Yes → No**

原依据：Tool use, posture, and tire lift provide diagnostic, emotional, and action value.

新依据：No completion, diagnostic detail, emotion, or distinctive action established to justify retention.

原贡献支持：I2, E2, A2, S2；新贡献支持：无。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | unknown：No visible completion or state transition established. | counterevidence：No visible completion or state transition shown. | f1, f2, f3 |
| O2 | unknown：No resolved attempt or material change visible. | counterevidence：No resolved attempt or material change evident. | f1, f2, f3 |
| O3 | unknown：No comparable result or phase for comparison. | not_applicable：No other comparable phase observed for comparison. | — |
| I1 | supported：Tool use visible, indicating specific action step. | not_applicable：No specific diagnostic detail or step clearly identifiable. | — |
| I2 | supported：Tool use adds diagnostic detail to tire repair process. | not_applicable：No substantive fact revealed beyond generic activity. | — |
| I3 | unknown：No other moment for comparison to establish novelty. | not_applicable：No comparison to another moment for novelty claim. | — |
| E1 | supported：Man’s bent posture indicates focused effort. | not_applicable：No discernible expression or posture attributable to person. | — |
| E2 | supported：Posture suggests concentrated physical engagement. | not_applicable：No marked reaction or change beyond ordinary motion. | — |
| E3 | unknown：No baseline or comparison to establish emotional intensity. | not_applicable：No baseline or comparison for emotional difference. | — |
| A1 | supported：Man and tool visibly interacting with tire. | supported：Man visibly interacts with car tire and tool. | f1, f2, f3 |
| A2 | supported：Tool application visible, indicating key step. | counterevidence：No distinctive execution detail or mistake observed. | f1, f2, f3 |
| A3 | unknown：No other action for comparison to establish significance. | not_applicable：No comparative action or phase to establish significance. | — |
| S1 | supported：Tire visibly lifted, indicating physical change. | not_applicable：No specific visual change or transformation observed. | — |
| S2 | supported：Lifted tire adds visual meaning to repair process. | not_applicable：No diagnostic view or distinctive meaning added. | — |
| S3 | unknown：No other scene for comparison to establish visual priority. | not_applicable：No other scene or state for visual contrast. | — |

**原可见事实（模型报告）**

- f1，帧[0]：Man in white shirt bends over car tire.
- f2，帧[1]：Man uses tool on wheel lug nuts.
- f3，帧[2]：Man lifts tire slightly off ground.
- f4，帧[0]：Jack stand visible under car near tire.
- f5，帧[0]：Man wears flip-flops while working.
- f6，帧[0]：White parking line visible on asphalt.

原关键规则：I1, I2, E1, E2, A1。

原背景使用：Background context confirms tire repair setting but does not override local evidence.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[0]：Man in white shirt bends over car tire.
- f2，帧[1]：Man uses tool on wheel lug nuts.
- f3，帧[2]：Man adjusts position while working on tire.

新关键规则：O1, O2, I1, I2, E1。

新背景使用：Background context irrelevant; no additional evidence supports highlight value.

新运行时结构警告：无。

## 9. J0nA4VgnoCo，窗口122，366–369秒

**决定：No → Yes**

原依据：No completion, diagnostic detail, emotion, or distinctive action visible to justify retention.

新依据：Visible tire repair with coordination and diagnostic context justifies retention.

原贡献支持：无；新贡献支持：I2, E2, A2, S2。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | counterevidence：No visible completion or state transition established. | counterevidence：No visible completion or state transition shown. | f1, f6 |
| O2 | counterevidence：No material change or resolved attempt visible. | counterevidence：No material change or resolution of attempt visible. | f1, f6 |
| O3 | not_applicable：No other phase or comparable result visible for comparison. | not_applicable：No other comparable result or phase observed. | — |
| I1 | not_applicable：No diagnostic detail or crucial step identifiable beyond general action. | supported：Visible actions reveal specific repair steps and collaboration. | f2, f3, f5 |
| I2 | not_applicable：No information beyond visible action or object identification. | supported：Diagnostic detail: hands-on tire repair with assistance. | f2, f3, f5 |
| I3 | not_applicable：No comparison to another moment for novelty or added content. | not_applicable：No other moment for comparison available. | — |
| E1 | not_applicable：No discernible facial expression or posture attributable to participants. | supported：Focused posture indicates intent, not ordinary expression. | f5 |
| E2 | not_applicable：No specific intensity or change in emotion observed. | supported：Event-linked concentration adds viewing value beyond routine. | f5 |
| E3 | not_applicable：No baseline or comparison to establish emotional difference. | not_applicable：No baseline or comparison reaction observed. | — |
| A1 | supported：Action of two people working on flat tire is visibly established. | supported：Correct participants performing tire repair task. | f2, f3, f5 |
| A2 | counterevidence：No distinctive execution detail or mistake observed. | supported：Observable coordination and key step: hands-on repair. | f2, f3 |
| A3 | not_applicable：No other action or phase for comparative significance. | not_applicable：No other action phase for comparison. | — |
| S1 | not_applicable：No specific visual change, reveal, or transformation observed. | supported：Visible change: tire being worked on, car stationary. | f1, f4 |
| S2 | not_applicable：No visual event adding meaning or distinctive experience. | supported：Diagnostic view: flat tire repair context clearly established. | f1, f4 |
| S3 | not_applicable：No other scene or state for visual contrast or support. | not_applicable：No other scene for visual contrast. | — |

**原可见事实（模型报告）**

- f1，帧[0, 1, 2]：Two people are crouched beside a car with a flat tire.
- f2，帧[0, 1, 2]：Woman in white shirt and orange shorts is working on the tire.
- f3，帧[0, 1, 2]：Man in white shirt and jeans is assisting with the tire.
- f4，帧[0, 1, 2]：Car is stationary on asphalt with visible jack and tools nearby.
- f5，帧[0, 1, 2]：Both individuals are focused on the wheel well area.
- f6，帧[0, 1, 2]：No visible completion, mistake, or state transition is shown.

原关键规则：O1, O2, I1, E1, A2。

原背景使用：Background context shows varied scenes, but no local evidence supports highlight value in this segment.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[0, 1, 2]：Two people are crouched beside a car's flat tire.
- f2，帧[0, 1, 2]：Woman is actively working on the tire with her hands.
- f3，帧[0, 1, 2]：Man is assisting by holding or stabilizing the tire area.
- f4，帧[0, 1, 2]：Car is stationary on pavement with visible jack stand.
- f5，帧[0, 1, 2]：Both individuals are focused on the tire repair task.
- f6，帧[0, 1, 2]：Scene suggests a collaborative effort to fix a flat tire.

新关键规则：I1, I2, E2, A2, S2。

新背景使用：Background confirms flat-tire context; no missing frames or inferred actions.

新运行时结构警告：无。

## 10. sTEELN-vY30，窗口3，9–12秒

**决定：Yes → Yes**

原依据：Train collision visibly completed, car crushed, providing diagnostic detail and visual transformation.

新依据：Crushed car and visible emergency response establish a concrete collision outcome with diagnostic value.

原贡献支持：O2, I2, A2, S2；新贡献支持：O2, I2, A2, S2。

| 规则 | 原状态与依据 | 新状态与依据 | 新事实引用 |
|---|---|---|---|
| O1 | supported：Train collision visibly completed, car crushed under locomotive. | supported：Crushed car indicates completion of collision event. | f1 |
| O2 | supported：Collision result materially changes scene, establishes wreckage state. | supported：Collision result materially changes visible situation. | f1 |
| O3 | not_applicable：No other comparable result or phase visible for comparison. | not_applicable：No other phase or comparable result is visible for comparison. | — |
| I1 | supported：Visible wreckage and location text provide specific context. | supported：Visible wreckage and location text provide specific facts. | f1, f5 |
| I2 | supported：Wreckage and location text add diagnostic detail to understand event. | supported：Crushed car and location text reveal key accident details. | f1, f5 |
| I3 | not_applicable：No other observed moment for comparison to establish novelty. | not_applicable：No other moment for comparison is visible in this segment. | — |
| E1 | not_applicable：No discernible facial expressions or reactions from individuals visible. | not_applicable：No discernible facial expressions or reactions from individuals. | — |
| E2 | not_applicable：No specific intensity or change in emotion attributable to participants. | not_applicable：No marked emotional reaction is visibly established. | — |
| E3 | not_applicable：No baseline or comparison reaction to establish emotional priority. | not_applicable：No baseline or comparative reaction is visible for evaluation. | — |
| A1 | supported：Train and car interaction clearly established as collision event. | supported：Train and car are visibly interacting in collision phase. | f1 |
| A2 | supported：Crushed car and locomotive position show key diagnostic phase. | supported：Crushed car indicates key diagnostic step in collision. | f1 |
| A3 | not_applicable：No other action or phase visible for comparative significance. | not_applicable：No other action or phase is visible for comparative support. | — |
| S1 | supported：Visible transformation: car crushed under train locomotive. | supported：Visible transformation of car from intact to crushed state. | f1 |
| S2 | supported：Visual event adds meaning: collision outcome clearly revealed. | supported：Crushed car reveals diagnostic meaning of collision outcome. | f1 |
| S3 | not_applicable：No other scene or state visible for contrast or comparison. | not_applicable：No other scene or state is visible for comparison. | — |

**原可见事实（模型报告）**

- f1，帧[0, 1]：Red car is visibly crushed under train locomotive.
- f2，帧[0, 1]：Police car and minivan are visible on adjacent road.
- f3，帧[0, 1]：Emergency personnel in yellow vests are near wreckage.
- f4，帧[0, 1]：Train tracks run parallel to paved roadway.
- f5，帧[0, 1]：CBS Atlanta logo and location text are displayed on screen.
- f6，帧[0, 1]：Temperature and time display visible in lower right corner.

原关键规则：O1, O2, I1, I2, S1。

原背景使用：Background context confirms urban setting and CBS Atlanta branding, but no additional interpretation needed for local judgment.

原运行时结构警告：无。


**新可见事实（模型报告）**

- f1，帧[0, 1]：Red car is visibly crushed under train locomotive.
- f2，帧[0, 1]：Police car and minivan are visible on adjacent road.
- f3，帧[0, 1]：Emergency personnel in yellow vests are near wreckage.
- f4，帧[0, 1]：Train tracks run parallel to paved roadway.
- f5，帧[0, 1]：CBS Atlanta logo and location text are visible on screen.
- f6，帧[0, 1]：Temperature display shows 48 degrees Fahrenheit.

新关键规则：O1, O2, I1, I2, A1。

新背景使用：Background context confirms urban accident setting but does not override visible collision evidence.

新运行时结构警告：无。
