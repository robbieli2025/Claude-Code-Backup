---
name: neobay-linkfox-api
description: LinkFox AI 生图 API 正确用法：endpoint、参数、polling 流程、图片提取
metadata: 
  node_type: memory
  type: reference
  originSessionId: ebe329b9-92b1-491e-8b70-714c33265b11
---

## LinkFox AI 生图 API（@AI绘图，Google Gemini 驱动）

### 凭证
- API key 存 `.env` 的 `LINKFOX_API_KEY`（JWT，exp ~2126，长期有效）
- Authorization header 直接用 raw JWT，不加 "Bearer" 前缀

### API 端点
- **Submit**: `POST https://agent-api.linkfox.com/chat/saveMessageForApi`
- **Poll**: `POST https://agent-api.linkfox.com/chat/getMessageForApi`
- 错误域名：`www.linkfox.com`（405）、`api.linkfox.com`（404/500）

### 请求参数
- Submit: `{"text": "@AI绘图 提示词：<English prompt>"}` — 字段名必须是 `text`，不是 `content`
- Poll: `{"id": "<messageId>"}` — 也是 POST，不是 GET 查询参数
- Response 顶层含 `messageId` 和 `chatId`

### 结果提取
- 生图完成后 `results` 数组中 `type: "html"` 的 `content` 是 HTML 页面 URL
- HTML 页面在 `agent-files.linkfox.com/user/...` 下
- **WebFetch 无法访问**，必须用 `urllib.request` + User-Agent header 抓取
- 从 HTML 中用 `re.findall(r'src="(https://agent-files\.linkfox\.com/generate_image/[^"]+)"', html)` 提取图片 URL
- 部分HTML可能403，需加 Referer header 或重试

### 图片处理
- LinkFox 生成 1024×1024 PNG（实际变体可能不同）
- 裁剪为 16:9：`sips --resampleWidth 1200` → `sips --cropToHeightWidth 675 1200`
- 上传到 Shopify Files 用 `scripts/shopify_files_upload.py`（仅返回 staged URL）
- 获取永久 CDN URL：`fileCreate` mutation（`originalSource`=staged URL, `contentType: IMAGE`）→ 然后查询 `files(first: N, sortKey: CREATED_AT, reverse: true)` 提取 `edges[].node.image.url`
- **坑：`fileCreate` response 中 `MediaImage.image` 可能为 null**，即使 `fileStatus: READY`。不能依赖 mutation response，必须单独查询 files 连接获取 CDN URL
- 正文 `<img>` 必须加 `style="max-width:100%;height:auto;"`
- 封面图用 `resource: "IMAGE"` + body 更新时传 `image: {src: cdn_url}`

### 耗时
- 每张图约 30-60 秒生成
- Polling 间隔 5 秒
