---
name: neobay-blog-article-ui
description: Neobay Blog文章页UI改造：两列布局+TOC+Related+Product CTA+进度条+正文样式增强
metadata: 
  node_type: memory
  type: project
  originSessionId: 0cbf3a71-0714-4c5c-8471-ebda3abf84ab
---

## 改造完成（2026-05-23）

Blog 文章页（`sections/main-blog-post.liquid`）从单列重构为两列布局：

- **左侧正文**：max-width 700px，内嵌 TOC 卡片 + 文章内容
- **右侧 Sidebar**：280-340px，sticky，Related Articles（5篇同分类优先+跨分类补齐）+ Product CTA（产品主图+绿色渐变卡片）
- **移动端**：单列，Related 推到底部

### 文件清单
- `sections/main-blog-post.liquid` — 两列布局+全部CSS
- `snippets/blog-toc.liquid` — TOC 卡片（Liquid 渲染空壳，JS 填充）
- `snippets/blog-related.liquid` — Related + Product CTA
- `assets/blog-article.js` — 进度条、H2 id 注入、TOC JS 生成、smooth scroll、dropcap

### 关键决策
- TOC **只显示 H2**，不显示 H3（H3 数量过多导致 TOC 过长影响阅读）
- TOC 由 **JS 生成**（Liquid split HTML 不可靠，会误抓参考文献等内容）
- Product CTA 硬编码，不走 schema 配置
- 不实现 scrollspy（TOC 不在 sticky 区域，收益低）
- 不实现 Read Next（只保留 Related Articles）

### 已知坑点
- Horizon `{% stylesheet %}` 编译到 `compiled_assets/styles.css`，GitHub push 后不会自动重编译，需在 Theme Editor 保存一次
- GitHub push 后 Shopify 可能不自动同步（需要确认主题模板选择正确）
- 同事在 Theme Editor 编辑与 GitHub push 会冲突，导致推送失败或线上不更新
