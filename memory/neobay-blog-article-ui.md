---
name: neobay-blog-ui
description: Neobay Blog改造全貌 — 列表页布局+文章页两列+TOC+Related+Product CTA+首页聚合section
metadata: 
  node_type: memory
  type: project
  originSessionId: 0cbf3a71-0714-4c5c-8471-ebda3abf84ab
---

## Blog 改造全貌（截至 2026-05-24）

### 文章页（`sections/main-blog-post.liquid`）
- 两列布局（正文 + Related sidebar），正文内嵌 TOC 卡片
- TOC 由 JS 生成，只显示 H2
- Related 同分类优先，跨分类补齐至 5 篇
- Product CTA 在 sidebar 底部（绿色渐变卡片+产品主图）
- 进度条、dropcap、H2 绿色下划线

### 列表页（`sections/main-blog.liquid`）
- Featured 区域：Flex 外层 + Grid 内层，3 张 side 卡片图片 120×120 不变形
- 左右间距 40px（与首页/PDP 统一）
- Newsletter 样式更新（全宽绿底+左右间距+form 满宽）

### 首页聚合（`sections/ta-homepage-blog.liquid`）
- 跨 4 个 Blog 聚合（feline-asthma, cat-breathing, spacer-guides, success-stories）
- 替代原生 `featured-blog-posts`（只支持单 Blog）
- 3 列卡片 Grid，标题 "Resources" + 绿色竖线 accent
- "View All Articles →" 链接到 /blogs/blog
- 全站统一 Inter 字体，32px 标题

### 产品卡（`assets/blog-product-card.css`）
- 缩小尺寸：padding 34→24px, gap 34→20px, 图片 220→180px, 价格 28→24px

### 关键文件
- `sections/main-blog.liquid` — 列表页
- `sections/main-blog-post.liquid` — 文章页
- `sections/ta-homepage-blog.liquid` — 首页聚合
- `snippets/blog-toc.liquid` — TOC 卡片
- `snippets/blog-related.liquid` — Related + Product CTA
- `snippets/blog-newsletter.liquid` — Newsletter
- `assets/blog-article.js` — 进度条+平滑滚动+TOC JS 生成
- `assets/blog-product-card.css` — 正文内产品卡
