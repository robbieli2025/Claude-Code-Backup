---
name: feedback-blog-publishing-standards
description: Blog 发布必须遵守的硬标准：HTML 格式、图片尺寸约束、产品卡 dropcap 排除，一次性发布到位
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ebe329b9-92b1-491e-8b70-714c33265b11
---

每篇 Blog 发布必须一次性达到以下标准，不允许发布后再手动修复：

## 硬标准

1. **body_html 必须是 HTML，不是 raw markdown** — `##`、`**bold**`、`- list` 在 Shopify 页面显示为纯文本。发布前用 Python `re` 转换（H1/H2/H3 → `<h1>`/`<h2>`/`<h3>`，`**text**` → `<strong>`，`- ` → `<ul><li>`，表格 → `<table>`，段落 → `<p>`）

2. **`%%bpc:spacer%%` 必须在 HTML 转换后完整保留** — 转换后搜索确认占位符存在。如果丢失，产品卡不会渲染

3. **正文配图 `<img>` 必须有 `style="max-width:100%;height:auto;"`** — 主内容栏仅 700px，CSS `max-width: 100%` 提供第一层保护，inline style 是第二层保险

4. **配图 URL 从 LinkFox HTML 结果页提取时用 Python urllib** — WebFetch 无法访问 `agent-files.linkfox.com`。用 `re.findall(r'src="(https://agent-files\.linkfox\.com/generate_image/[^"]+)"', html)` 提取

5. **产品卡标题不受 dropcap 影响** — `blog-article.js` `initDropcap()` 已排除 `.bpc-wrapper` 和 `.bpc-title`。前提是正文有正常的 `<p>` 标签（即 body_html 必须是 HTML）

6. **`shopify_files_upload.py` 的 `fileSize` 已修复为 string** — 但使用前确保 `.env` 中 `SHOPIFY_ADMIN_TOKEN` 有效（先跑 `refresh_token.py`）

7. **LinkFox AI 配图以真实性为主** — 不要强行把产品画进图中。如果 AI 生成的产品外观与实际差异大，用纯场景图代替。生图不等于广告图，真实性 > 产品露出

8. **Key Takeaways 标题保留** — `## Key Takeaways` 必须保留，不要删除。不要在它上方重复 H1 标题

9. **body_html 不得包含 `<h1>`** — Shopify 模板 `main-blog-post.liquid` 的 `blog-post-title` block 已渲染 `article.title` 为 H1。body_html 开头再加 `<h1>` 会导致页面出现两个重复标题。markdown 草稿中的 `# Title` 行应在 markdown→HTML 转换时删除

10. **Key Takeaways 必须是 body_html 的第一个元素，且后面必须有 `<hr>` 分隔线** — `<h2>Key Takeaways</h2>` + `<ul>` + `</ul>` + `<hr>` 必须位于 body_html position 0（紧随模板渲染的 H1 之后）。TOC 由 `blog-article.js` 动态注入在文章顶部，KT 紧贴 TOC 下方，分隔线将 KT 与正文内容清晰分开。intro 段落放在 `<hr>` 之后。结构顺序：TOC → KT → `<hr>` → intro → 正文

**Why:** 2026-05-24 重写 #1 时，LinkFox 生成的产品图与实际产品差异大（Comfort Feeder 位置不对、spacer 形状失真），用户要求真实性优先。同日误删 Key Takeaways 标题，用户纠正必须保留。5/25 发现 `<h1>` 重复渲染（模板已渲染标题 + body_html 又有 `<h1>`），修正为 body_html 从 `<h2>Key Takeaways</h2>` 开头。同日优化 #2 时发现 intro 段落被放在 KT 之前，导致 KT 出现在页面内容下方而非 TOC 正下方，用户指出 KT 必须在 TOC 下立即展示。

**How to apply:** 生图 prompt 不强加产品外观描述，以真实猫护理场景为主。markdown 模板中 `## Key Takeaways` 始终保留。
