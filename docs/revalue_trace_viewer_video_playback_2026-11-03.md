# GT 标注与 Qwen Direct 预测的视频回放

用户澄清需要直接观看对应视频的标注片段和Direct预测片段，故在已有统计与证据帧功能之外增加真实视频播放器。

## 使用

访问原8B页面8766或32B页面8765，点击标题下「▶ 播放 GT / Direct 片段」。左右选择器分别列出当前query的全部GT区间与Direct有效预测区间，点击「播放本段」播放连续原视频，到终点自动暂停。切换Direct候选时同步切换该候选的verifier记录。默认静音，用户可开启原音轨。

[8B直接播放示例](http://localhost:8766/?view=video&case=qv_2781_w02__Q&v=video1)：QID2781，左侧GT为56–60秒、72–98秒；右侧当前Direct候选为37–41秒，共9个有效预测区间。播放器使用冻结记录中的合法区间，不修补原输出截断的尾部。

## 内容边界

- GT是当前grounding任务的标注相关区间，不是额外高光saliency分数，也不是verifier的“支持”标签。
- 两个页面的原Direct预测都来自Qwen3-VL-8B-Instruct；32B页面只对应更换了verifier基模的实验。
- 视频回放用于用户离线审阅，不代表模型当时看过连续视频或听过音频。原证据区继续显示实际输入的稀疏帧。
- 播放入口覆盖现有候选列表。Base无有效候选的两条query继续计入总体范围，但当前没有对应的候选详情入口。

## 来源与实现

原视频从REZE Direct冻结inputs.json中的video_path及media_sha256绑定，并核对query视频ID和时长。首次读取校验视频哈希，后续文件元信息变化重新校验。只允许当前查看清单的请求ID访问，支持HEAD和单段HTTP Range，流式传输现有MP4，不生成新裁剪文件或转码。

时间使用数据集裁剪视频自身的0秒起点，不能再次叠加文件名中的源视频起点。示例文件时长150.024秒、H.264/AAC，文件SHA与原Direct输入一致。

## 验证

20项Python检查通过，涵盖旧功能、原文件/清单漂移、范围请求、越界请求、作用域及GT完成门槛。6项真实浏览器检查通过：原视频解码，分别定位GT56秒与Direct37秒，实际播放推进，Direct在41秒暂停、GT第二段在98秒暂停，切换候选同步证据，移动端布局及32B页面正确显示原8B Direct来源。

没有新增模型调用、GPU分配、实验预测、评价或视频编码。只重启了两个只读查看服务。

浏览器验证收据（本地资料：`$MERIT_ROOT/projects/revalue_trace_viewer/validation/video_2026-11-03/browser_qa.json`） · 使用说明（本地资料：`$MERIT_ROOT/projects/revalue_trace_viewer/README.md`）
