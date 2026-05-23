---
name: Horizon Theme BPC Pitfall
description: Shopify Horizon 主题 blog product card 占位符不渲染的根因和解决方案
type: reference
originSessionId: 8e6e316d-6dab-4894-86f1-6bcab0f86270
---
## Shopify Horizon 主题：blog product card 占位符不渲染

### 核心结论
Horizon 主题中，`@theme` 类型 block 在 `section.blocks` 运行时**不携带 settings 数据**（`placeholder_id`、`product` 等字段均为空），且 `content_for 'block'` 创建隔离作用域。因此：
- 不能依赖 `section.blocks` 读取 block settings
- 不能通过 `content_for` 子 block 做占位符替换
- **必须在 section 层用硬编码映射做替换**

### 解决方案
在 `snippets/blog-product-card-article-process.liquid` 中用 `all_products['产品句柄']` + `for/case` 硬编码占位符 ID 与产品映射，在 `main-blog-post.liquid` section 层直接输出替换后的内容，不走 `content_for`。

### 完整排障记录
见 skill `blog-product-card-block` 的 SKILL.md 中"Horizon 踩坑总结"章节。
