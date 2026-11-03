# ReVALUE 推理过程查看页面

2026-10-30，按用户“设计一个前端页面查看中间过程”的要求完成本地只读实现。没有新增实验推理、修改模型提示或修复旧预测，没有推送远程。

## 实际交付

页面采用三部分：左侧是固定候选列表和筛选；中间是原输入帧、区域标签和时间轴；右侧是可见事实、query/边界、五类价值与原始记录。点击事实 ID 或帧 ID 可以联动定位和高亮画面。

接入现有 139 个候选：54 flagged、10 supported、17 insufficient、58 invalid。完整 100 query 中的 2 条 Base 空预测保留在概况中，不伪造候选。所有候选都可检索，12 条已有助手审阅的候选额外标记；标记不表示独立人工核验。

功能包括：

- QID/query/视频 ID 搜索、结果筛选、候选切换、可分享的单条 URL。
- 原输入帧放大、逐帧切换、按片前/片内/片后筛选、采样帧轮播；轮播明确不是连续视频。
- 事实与来源引用联动，保留缺失/重复引用，单独区分理由中提及但未绑定的帧。
- 展示原始价值状态，包括 NA/unknown，不根据页面规则补值。
- 保留 invalid 原始响应、错误和空事实，不把原始判断显示为已通过验证。
- GT 默认隐藏；打开后显示既有 GT、IoU 代理与固定时长规则结果，不重新评价。
- 实际序列化提示、Direct 原输出、token/本条生成耗时、来源路径与哈希、单条 JSON 下载。
- 桌面双栏详情与移动端单栏/抽屉，键盘焦点和大图对话框。

页面展示的是保存的输入、模型输出及 CPU 判定，不是模型内部思维链。事实和各判断仍来自同一次模型调用；没有新增回看、全视频记忆或 Agent 多轮执行。

## 启动

在服务器终端运行：

```bash
bash $MERIT_ROOT/projects/revalue_trace_viewer/start.sh
```

在 VS Code SSH 的 **端口（Ports）** 面板转发 `8765` 后打开。若本地映射同端口，访问 `http://localhost:8765`；指定案例可用 `?case=qv_9572_w01`。仅监听服务器 loopback，不注册或发布云端站点。

完整使用说明（本地资料：`$MERIT_ROOT/projects/revalue_trace_viewer/README.md`）包含其他端口、环境和测试命令。交付前关闭仅用于验证的 HTTP 服务和独立 Firefox；日常使用由用户启动上面的查看器。

## 验证结果

| 验证 | 结果 |
|---|---|
| Python 回归测试 | 6 项通过：invalid 不提升、原像素保真、非输入帧拒绝、输入/记录漂移拒绝、读取路由与写入拒绝 |
| JavaScript 数据函数测试 | 5 项通过：筛选顺序、缺失引用、时间格式、时间轴范围、错误说明 |
| 实际浏览器交互 | 11 组通过，使用已有 Firefox 158 与 Node 24；未安装浏览器或前端依赖 |
| 实际数据载入 | 全部 139 条 payload 校验通过，状态和候选窗口沿用原产物 |
| 响应式显示 | 1600×1200 桌面与 390×844 手机检查通过，无横向溢出；未发现 JavaScript 错误 |
| 旧文件保护 | 原离线审计中 433 个受保护文件哈希不变 |

浏览器实测覆盖筛选、搜索空状态与恢复、事实点击联动、停止轮播、价值 NA、原始提示与 Direct 输出、GT 开关、全片时间轴、手机抽屉和大图。

数据核验收据（本地资料：`$MERIT_ROOT/projects/revalue_trace_viewer/validation/data_checks.json`）、浏览器验证收据（本地资料：`$MERIT_ROOT/projects/revalue_trace_viewer/validation/browser_qa.json`）与桌面截图（本地资料：`$MERIT_ROOT/projects/revalue_trace_viewer/validation/preview-desktop.png`）已保存。另有价值页、invalid 页与手机截图。

## 实现边界与保存规则

前端为原生 HTML/CSS/ES modules，后端为 Python 标准库 HTTP + 已安装的 NumPy/Pillow，无 npm 构建、外部 CDN 或模型 API。后端只读旧 JSON/NumPy 缓存；图片按请求在内存生成 PNG，并校验旧像素哈希，不新增源帧或视频解码。启动时核验冻结输入与已提交响应哈希。

本轮新增实验请求/token/GPU 分配/模型 worker 为 0。查看器 HTTP 进程和测试浏览器是普通 CPU 工具，不是实验推理 worker。旧 QV、TVSum、Direct、verifier 账本不改动、不转移预算。

- 原 verifier ledger SHA256：`dd00c703ba9b2b06ce17686484bd2b7a9f42134744a7a24644a43bec8d372cb8`。
- 原 evaluation SHA256：`ce370b4b65e65bcfc2acc9018358ace1fc7fb822b81a1006a228fdb5ef19bde6`。

当前查看器依赖服务器上的冻结数据与旧帧缓存。若移到其他机器，只复制前端源码不足以显示图像，需要保留相应输入文件和缓存位置。尚未实现任意实验格式导入或原视频播放器。
