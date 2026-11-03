# ReVALUE 区间 Verifier：REZE Direct 固定 QV100 协议 v1

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: plan，附用户所要求模块的CPU实现准备
- Origin Date: 2026-10-30
- Verification Status: UNVERIFIED（模型验证尚未运行，CPU检查不代表语义有效）
- Version Label: revalue_direct_verifier_v1_2026-10-30
- 执行身份：当前Codex主助手；独立只读方法/代码审查另存收据。不是跨模型视觉验证。

## 1. 已确定的主线与研究问题

按用户指令，将已完成的 **REZE论文Direct协议重建**作为后续base。该base一次读取整视频采样帧并输出区间，不是REZE局部Yes/No扫描，也不是完整ReVALUE Agent。沿用Qwen3-VL-8B-Instruct BF16、固定revision与原100条开发样本。历史自定义Direct仍保留为对照。

本轮设计问题：在不读取GT、不修改Direct输出的条件下，verifier能否利用query相关性与目的相关价值证据，指出错误事件、错误归属或边界问题？它首先是一个**反例筛查器**，本阶段不证明定位指标提升，也不检验价值维度的独立因果收益。

用户原话：“直接用reze direct方案当做我们的base方法吧，然后调用$ars，设计一个verifier模块，按照我们之前revalue方案中的设计，从价值维度以及query相关度，对direct方案输出的区间做一个验证，看一下能不能找出反例”。ARS `plan`用于形成方案；本轮准备时 `execution_authorized=false`，GPU运行命令待用户按code_runner要求确认。不能把准备文档或旧预算当成新推理授权。

## 2. 与原ReVALUE设计的对应

依据原v3第4–8节的事实/判断分层、请求资格、五类价值、来源与区间完整性原则。保留结果outcome、信息information、情感emotion、动作action、感官sensory，不把旧四cue换名冒充五类价值，不给五项固定加权总分。

本轮是单区间判断，无甲乙比较，因此不用tie。原始query直接传入，不运行旧TaskSpec对象抽取器；query判断须引用原query的原文子串，避免额外生成对象约束。字面引用正确不代表模型已经覆盖所有语义，仍需内容审查。

事实和判断在同次请求中生成，明确标记 `query_conditioned_observation`。这仅实现字段分层，**不满足原A模块“query盲事实提取”的独立性**，也不是全视频记忆或完整Agent闭环。

## 3. 固定总体与证据

- 使用base全部100条query、所有139个有效预测区间，保留生成顺序。不得只挑低IoU反例或表现好的子集。
- qid9160与2498的原始零长度输出没有有效区间，保留在100条总体中作为base结构问题；不编造候选，不计为verifier发现的反例。
- 每有效区间一次模型请求。原始区间、置信度导出、排名及base文件全部只读。
- 仅复用base已经保存的2FPS帧像素，不重新解码、不新增抽帧或空间裁剪。
- 区间按 `[start,end)` 分区：区间内最多16帧；`[max(0,start−4),start)` 最多4帧；`[end,min(D,end+4))` 最多4帧。
- 各区按时间有序列表的等分格中点索引 `floor((i+0.5)*N/cap)` 确定采样；不足取全部。按源帧ID去重，去除父视频编码时复制的末帧，绝不为补齐帧数复制观察。
- 保存实际PTS、源帧ID、父数组位置、区域和像素哈希。按时间以逐图像+PTS标签输入，避免把不连续证据当成均匀播放的视频；没有新音频。少帧不代表区间为空，稀疏观察也不能证明连续覆盖。

## 4. Verifier流程与契约

```text
冻结Direct区间 + 原query
  → 固定旧帧证据包（区间内/前/后）
  → 单次Qwen验证：来源事实 + query判断 + 五类价值 + 起止边界
  → CPU引用/区域/原query引用检查
  → flagged / supported / insufficient；格式或引用错误另记invalid
  → 预测冻结后才读GT，评价反例筛查与误报
```

输出最多6条有源帧引用的可见事实；每条事实只允许引用同一区域的帧，片内与片外事实分开。query_match返回supported/contradicted/unknown；supported或contradicted的直接证据必须全部来自区间内，不能用一个片内人物事实夹带片外动作当作支持。缺少关键动作采样不等于动作未发生，没看清保持unknown。

边界start/end分别输出supported/too_early/too_late/unknown，允许同一区间同时存在过宽与截断。起点过晚须同时引用inside锚点与before证据；终点过早须同时引用inside锚点与after证据，并将same_event标为supported；起点过早/终点过晚须引用inside的冗余内容。外部证据须属于同一次目标事件；另一轮重复事件不自动构成截断。必要阶段来自query，不能默认补齐“过程—结果—庆祝”。本版只指出问题，不生成新时间戳，也不声称验证亚秒边界。

五类价值分别保存supported/contradicted/unknown/not_applicable、依据事实及其与query的关系：

| 维度 | 与定位核查的关系示例 |
|---|---|
| outcome | query要求“进球”时核查完成结果，不能把射门尝试当作进球 |
| information | 检查可见过程/界面细节是否真能支持请求，不以描述长度评分 |
| emotion | 请求包含激动反应时核查表情/动作及其归属，不凭镜头近判定强烈 |
| action | 检查关键动作与阶段，而非只识别到同一人物或物体 |
| sensory | 检查请求相关可见外观和画面证据，不把普通画面或无音乐判为错误 |

**价值低、无情绪、没有庆祝不能直接拒绝普通grounding正例。** CPU最终状态只由query明确反证或引用合法的边界缺陷产生flagged；query与两端边界均supported才supported；其余为insufficient。值字段不参与拒绝公式。事实引用存在只能证明来源契约合法，不能证明事实描述真实。

## 5. 输出和失败处理

每条保留原始响应、原始token用量、结束原因、解析对象、事实引用、派生状态、缺陷类型及未决问题。不生成可用于删除base区间的隐式分数。

格式错误、引用不存在、query引用不属于原请求、片外证据被写成片内支持等记invalid；保留原输出，不修写为正常unknown，不重试。正常insufficient是有效的不确定判断。invalid保留全分母并继续既定清单；运行错误/OOM/输入漂移/预算不足停止后续请求，未尝试项保留，不自动恢复或降输入配置。

## 6. 评价设计

区间级主要错误代理：当前Direct区间对任一独立GT的最大IoU<0.5。评价flag precision、错误召回、正确区间误报率、supported中漏过的错误、insufficient及技术失败率。unknown、invalid、未尝试均留在错误召回分母。零flag时precision为null，不伪装为100%。

该代理不是人工语义真值：合理但未标注的重复事件可能IoU低；轻微真实边界问题可能IoU仍高。补报0.3/0.7阈值、query宏平均与source-video聚类bootstrap（10,000次、seed42）；139区间不能当139个独立视频。

保留完整100查询计数；两个空预测单列，不借其提高verifier召回。比较无模型调用的“全部报警”基率及冻结的时长启发式（长度≤2秒或覆盖≥80%视频），均明确标为CPU基线。

输出全部候选审计CSV；后续语义审阅应覆盖flagged、insufficient及supported样本，不仅挑成功反例。没有独立人工审阅时人数/条数为0，不能把模型或助手检查称为人工真值。本版不改base预测，因此不报告虚构的grounding提升。

## 7. 探索性继续门槛

协议泄漏、输入漂移、原预测改写零容忍。技术输出至少138/139合法；探索筛查目标为precision≥80%且高于错误基率、recall≥30%、正确区间误报≤10%、insufficient≤40%，至少20个flag后才讨论精度稳定性。

这些是预先提议的开发筛选规则，不是显著性或语义正确性证明，不因结果不理想而修改门槛或循环提示。未通过时报告具体失败机制；通过也只支持进入独立人工审查或query-only对照。单臂联合提示不能证明五类价值的独立贡献。

## 8. 建议独立预算与运行边界

未来正式运行建议：最多139次总尝试、零重试、零额外故障请求；总token绝对上限1,138,688，输入+输出每请求≤8192，输出最多1536。每次只用一张空闲4090；14个顺序冷worker，每批10条（末批9条），每worker全生命周期≤300秒，累计≤4200 GPU秒（1.1667 GPUh），包含加载和失败。

权重、依赖、tokenizer均复用，不下载、不更新环境、不启用在线跟踪。不占用旧QV/TVSum/Direct任何剩余量。启动失败计worker和GPU成本，无自动启动重试；不足以完成全部时报告全部清单及未尝试项。

supervisor在GPU发现或模型导入前校验明确授权与源码审查，重复启动拒绝。入口必须来自实际加载的冻结源码目录。逐请求先预留最大token再生成，正常输出按实际记账，异常保留预留。每次启动预登记；收尾探测失败也保留启动和保守资源预留，实际生命周期不明时明确记unknown并阻止GT评价。评价须核对全部启动的终止收据与实时所属进程；已预留但中断的请求不能写成未尝试，未提交响应也冻结哈希并单列。健康监控只处理本轮所属进程。实验输出异常不自动调提示或补跑。

## 9. 运行入口与当前状态

代码目录：`$MERIT_ROOT/experiments/revalue_verifier/`。
运行准备目录：`$ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_2026-10-30/`。

CPU契约：

```bash
CUDA_VISIBLE_DEVICES='' PYTHONDONTWRITEBYTECODE=1 $LONGVT_ARTIFACT_ROOT/env/inference/bin/python -m unittest discover -s $MERIT_ROOT/experiments/revalue_verifier -p 'test_*.py'
```

拟确认的GPU命令（本轮准备不执行）：

```bash
$LONGVT_ARTIFACT_ROOT/env/inference/bin/python $ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_2026-10-30/source_snapshot/supervise.py --run $ZEROSHOT_ARTIFACT_ROOT/revalue_direct_verifier_v1_2026-10-30
```

用户确认命令与本协议范围后，才记录精确用户答复、绑定manifest哈希并将新授权收据设为true；不得改旧实验授权。正式退出后再调用冻结 `evaluate.py`，先冻结响应再读标签。

## 10. 交付与未验证项

准备交付完整100条/139区间清单、旧像素/PTS与输入token哈希、提示/schema、源码、CPU测试、来源审查和零新增模型调用收据。后续结果目录保存全部记录、账本、退出收据、错误检测CSV和评价。

当前尚未验证：Qwen能否可靠描述这些帧、判定真假反例、理解价值维度，以及本模型对自身错误的独立发现能力。使用同一模型与旧证据存在相关错误风险。原ReVALUE的query盲事实、全视频记忆、定向补看、多事件比较及边界修正不在本轮完成范围。
