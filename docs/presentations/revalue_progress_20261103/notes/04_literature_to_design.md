当前价值判断设计主要借鉴四个工作。VisionReward 把多维偏好拆成具体视觉判断题，我们借鉴的是问题化思路，为五类视角写出支持证据、反证限制、缺证标准和不能做的推断。UnifiedReward-Flex 会按输入细化评价条件，我们借鉴任务适用性，只启用 query 真正需要的视角。与原论文的动态评价不同，我们在看到候选结果前冻结要求，避免为了某个片段临时加标准。

DSG 用原子问题和依赖关系减少矛盾回答，我们据此显式记录对象、属性和动作关系，并增加帧引用、时间作用域和 unknown。VTune 研究定位后的事件及组成条件验证，提醒我们：能够输出区间，不代表模型能可靠确认区间内容。因此我们在 Direct 后加 verifier，同时单独衡量 verifier 自己是否可信。

组合后就是：先拆 query 条件，再生成适用核查题，模型输出事实与帧引用，最后给三值判断。五类名称沿用我们此前的 ReVALUE 方案，不是复制某一篇论文的维度。当前也没有使用这些工作的训练权重、奖励分数或 VTune 训练；Q 与 Q 加 V 对照测的是这一套价值提示的额外贡献，收益仍待验证。举例说，横屏手机能提供外观证据，但不能自动证明屏幕是文章；看不清应当保留未知。

原始文献链接：[VisionReward](https://arxiv.org/html/2412.21059v2#S2)、[UnifiedReward-Flex](https://arxiv.org/html/2602.02380v1#S3.SS2)、[DSG 官方项目](https://google.github.io/dsg/)、[On the Consistency of Video Large Language Models in Temporal Comprehension / VTune](https://arxiv.org/html/2411.12951v1)。本项目迁移依据见二〇二六年十月三十一日的相关工作调研与价值判断设计 v2，本次重新核对原始来源，未复现论文性能。
