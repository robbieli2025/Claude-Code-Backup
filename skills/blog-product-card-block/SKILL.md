---
name: blog-product-card-block
description: 在 Shopify 博客文章正文的任意位置插入可配置的产品卡 block（含产品图、标题、原价划线、折后价、Save XX% 折扣徽章、Learn More 链接、Add to Cart 按钮）。当用户提到"博客里加产品卡"、"在 blog 文章中间嵌入产品 CTA"、"参考 Waterdrop 博客的产品卡片"、"博客正文加 Add to Cart"、"shopify blog inline product card"、"博客模板加 product block"，或者发了 Hauswirt/Neobay/Waterdrop 类似博客内嵌产品卡截图问怎么实现时，触发此 skill。这是一个跨主题（Impact / Horizon / Dawn / OS 2.0）通用的实施手册。
---

# Shopify 博客产品卡 Block

让运营在 Shopify 博客文章中**任意位置**插入产品卡，效果和 Waterdrop 博客文章里穿插产品卡片一致。

## 整体方案

无论什么主题，方案都是同一套：

1. **新增"主题级 block"**：在主题里注册一个 `product_card` block（Impact 主题在 main-article section schema 里，Horizon 主题在 `blocks/blog-product-card.liquid` 文件）。运营在 Theme Editor 里可视化添加 block，每个 block 选产品 + 填一个**唯一占位符 ID**（如 `card-1`）+ 自定义卖点和按钮文案。

2. **正文写占位符**：运营在 Shopify 博客文章后台正文编辑器里，在想插入产品卡的段落之间写：
   ```
   [product-card:card-1]
   ```

3. **Liquid 字符串替换**：在主题渲染 `article.content` 之前，将占位符替换为产品卡 HTML。同时替换 `<p>[product-card:xxx]</p>`（富文本编辑器自动包裹 p 标签）和裸占位符两种形态。

4. **CSS 按需加载**：仅当文章实际使用了产品卡 block 时才加载样式表，避免给所有博客文章引入额外资源。

## 主题判断（必须先做）

不同主题的"渲染 article.content 的位置"不同，先判断当前主题类型再选实施路径。

```bash
# 判断 1：看 templates/article.json 引用哪个 section
cat templates/article.json | python3 -m json.tool | head -5

# 判断 2：看是否有 blocks 文件夹（含 _ 前缀的 block 文件）
ls blocks/ 2>/dev/null | head -5

# 判断 3：看主题是否有 _blog-post-content.liquid
ls blocks/_blog-post-content.liquid 2>/dev/null
```

| 主题类型 | 标志 | 实施路径 |
|---|---|---|
| **Horizon** (新一代主题) | 有 `blocks/_blog-post-content.liquid`，section 用 `content_for 'block'` | 路径 A |
| **Impact** (老 OS 2.0) | 有 `sections/main-article.liquid`，section 内 `{{ article.content }}` 直接渲染 | 路径 B |
| **Dawn / 其他 OS 2.0** | `sections/main-article.liquid` 风格 | 路径 B（参考 Impact 套路适配） |

如果不确定，直接读两个候选 section 文件，看哪个里出现了 `{{ article.content }}` 或 `article.content` —— 那就是要改的位置。

---

## 路径 A：Horizon 主题

需改动 4 个文件：

### A.1 复制主题无关 CSS
拷贝 `templates/blog-product-card.css` 到项目 `assets/blog-product-card.css`。

### A.2 复制主题无关 snippet
拷贝 `templates/snippets/blog-product-card-article-process.liquid` → 项目 `snippets/blog-product-card-article-process.liquid`。

### A.3 新建 Horizon block 文件
拷贝 `templates/horizon/blog-product-card.liquid` → 项目 `blocks/blog-product-card.liquid`。

**重要：文件名不能带下划线前缀**。Horizon 主题里 `_xxx.liquid` 是"私有 block"，只能被 `content_for` 显式调用，不会出现在 Theme Editor 的 "Add block" 菜单中。运营会搜不到这个 block。

注意：**此 block 不直接渲染产品卡**，只在 design_mode 显示提示标记，前台不输出任何 HTML（产品卡 HTML 由占位符替换注入）。

### A.4 修改 `sections/main-blog-post.liquid` — 占位符替换

**⚠️ 重大坑（Neobay 项目 2026-05 踩了 6 次才解决，必读）**：

Horizon 主题中有 **三层陷阱**，必须全部绕过才能成功：

#### 陷阱 1：`content_for` 变量作用域隔离

`main-blog-post.liquid` 通过 `content_for 'block'` 渲染子 block 时，会创建**隔离作用域**。section 层通过 `capture` 生成的变量（如 `article_content_rendered`）**无法传递到子 block**，子 block 中该变量为空，回退到 `article.content`（原始未处理内容），占位符原样输出。

**结论：占位符替换必须在 `main-blog-post.liquid` section 层完成，不能依赖子 block。**

#### 陷阱 2：`content_for` 子 block 中 `section.blocks` 数据不完整

在 `_blog-post-content.liquid` 子 block 内遍历 `section.blocks` 时，只能看到**当前 block 自身**（`section.blocks.size = 1`），且其他 block 的 `settings` 为空。无法从子 block 中读取 blog-product-card block 的 `placeholder_id` 和 `product`。

**结论：无法在子 block 中通过 `section.blocks` 获取产品卡配置。**

#### 陷阱 3：`@theme` 类型 block 运行时不携带 settings

即使在 `main-blog-post.liquid` section 层遍历 `section.blocks`，Horizon 主题的 `@theme` 类型 block **运行时只提供 `type` 和 `id`，不提供 `settings` 数据**（`placeholder_id`、`product` 等字段均为空字符串）。所以 `b.type == 'blog-product-card'` 或 `b.settings.placeholder_id != blank` 等条件全部匹配失败。

诊断输出示例：
```
type=[@theme] id=[ASklyV0R6OEVVZWp4M__blog_product_card_spacer] pid=[] product=[]
```

**结论：无法通过 `section.blocks` 读取任何 block 的 settings，整个动态匹配方案在 Horizon 主题下不可行。**

#### ✅ 正确方案：硬编码占位符映射

因为 `section.blocks` 不可用，**必须在 snippet 中硬编码占位符 ID 与产品句柄的映射关系**：

1. `blog-product-card-article-process.liquid` 不再接收 `section` 参数，不再遍历 `section.blocks`
2. 直接用 `all_products['产品句柄']` 获取产品数据
3. 用 `for/case` 循环硬编码已知占位符 ID（如 `spacer`、`inhaler`）与对应 highlights
4. 新增占位符时，只需在 snippet 的 case 语句中添加一个 `when` 分支

在 `main-blog-post.liquid` 中：
```liquid
{%- liquid
  assign article_content_processed = article.content
  capture article_content_processed
    render 'blog-product-card-article-process', article_html: article.content
  endcapture
-%}
<div class="blog-post-content rte">
  {{ 'blog-product-card.css' | asset_url | stylesheet_tag }}
  <rte-formatter>
    {{- article_content_processed -}}
  </rte-formatter>
</div>
```

注意：替换了原来的 `{%- content_for 'block', id: 'blog-post-content', type: '_blog-post-content' %}`，文章内容直接在 section 层输出。

`_blog-post-content.liquid` 恢复为简单 block（仅作 article.json 中的占位注册），不再承担任何替换逻辑。

**运营友好**： instruct 运营在富文本里**新建一段**，只粘贴 **`%%bpc:占位符ID%%`**（无需「显示 HTML」），与 snippet 中硬编码的 ID 一致即可；仍支持标准 `[product-card:ID]`。

---

## 路径 B：Impact / Dawn 类老 OS 2.0 主题

需改动 3 个文件：

### B.1 复制 CSS / snippet
同 A.1、A.2。

### B.2 修改 main-article section
在 `sections/main-article.liquid`：

1. 在文件顶部 `{%- liquid -%}` 块加占位符替换逻辑（参考 `templates/impact/main-article-snippet.liquid`）
2. 把 `{{ article.content }}` 改成 `{{ article_content_rendered }}`
3. 在 schema 的 `"blocks"` 数组里加 `product_card` block 定义（见 `templates/impact/main-article-block-schema.json`）

**注意**：Impact 主题（路径 B）的 `section.blocks` **可以正常访问 settings**，动态匹配方案可用。只有 Horizon 主题（路径 A）存在 settings 不可用的问题。

如果该 section 用 `render 'price-list'` / `render 'product-badges'` 这类主题原生 snippet 已经能渲染 Save XX% 徽章（Impact 主题特性），可以选用主题原生写法替代主题无关 snippet 中的价格部分；否则保留主题无关版（更省心）。

---

## Horizon 踩坑总结（2026-05 Neobay 项目）

以下是在 Neobay 项目（Horizon 主题）中修复 blog product card 占位符不渲染问题的完整排障记录，供未来参考：

| 尝试 | 方案 | 失败原因 |
|------|------|---------|
| 第1次 | 在 `_blog-post-content.liquid` 中遍历 `section.blocks`，`b.type == 'blog-product-card'` | `content_for` 子 block 作用域中 `section.blocks` 只有自身 1 个 block，且 settings 为空 |
| 第2次 | 在 `main-blog-post.liquid` section 层 `capture article_content_rendered`，子 block 用 `{{ article_content_rendered \| default: article.content }}` | `content_for` 变量作用域隔离，`article_content_rendered` 在子 block 中不可访问，回退到 `article.content` |
| 第3次 | 同第2次，改匹配条件为 `b.type == '@theme' and b.settings.placeholder_id != blank` | `@theme` 类型 block 运行时 `settings` 数据全部为空，`placeholder_id` 为空字符串 |
| 第4次 | 把替换逻辑移回 `_blog-post-content.liquid` | 同第1次，子 block 中 `section.blocks` 不完整 |
| 第5次 | 在 `main-blog-post.liquid` section 层直接输出，不走 `content_for`，但仍有 `section.blocks` 遍历 | section 层 `section.blocks` 虽有 block，但 `settings` 仍然为空 |
| **第6次** | **弃用 `section.blocks`，在 snippet 中硬编码占位符 ID 与产品映射** | **✅ 成功** |

**核心教训**：
1. Horizon 主题 `@theme` 类型 block 运行时不携带 settings → 不能依赖 `section.blocks` 做动态匹配
2. `content_for 'block'` 创建隔离作用域 → 变量不能跨作用域传递
3. 子 block 的 `section.blocks` 只有自身 → 无法遍历其他 block
4. 对于 Horizon 主题，**硬编码映射是唯一可靠方案**

---

## 主题原生 vs 主题无关

主题无关 snippet（`blog-product-card-inline.liquid`）自己计算 savings 百分比、自己输出 badge HTML、不依赖任何主题原生 snippet。**优先用这个**，跨主题最稳。

只有当用户**强烈要求"和 PDP 视觉完全一致"**时，再考虑改用主题原生 price snippet：
- Impact 主题：`render 'price-list', variant: ..., size: 'lg'` + `render 'product-badges', types: 'discount', context: 'product'`
- Horizon 主题：`render 'price', product_resource: ...`（**注意：Horizon 的 price.liquid 不输出 Save 徽章，需要自己加**）

---

## 主题适配检查清单（实施完必查）

### 1. Article 正文容器的 a 标签下划线
某些主题（Impact 的 `.prose a:not(.button)`）对正文里所有 `<a>` 用 `linear-gradient` 模拟下划线。我们的 Learn More 是 `<a>`，会被命中。

修复（CSS 已含此覆盖，但**需确认选择器特异性够**）：
```css
.bpc-wrapper a.bpc-btn,
.bpc-wrapper a.bpc-btn:hover {
  background-image: none;
  text-decoration: none;
}
```

如果主题用了更高特异性选择器（例如 `.prose .blog-post-content a`），需要把 `.bpc-wrapper a.bpc-btn` 升级为 `.prose .bpc-wrapper a.bpc-btn` 之类。

### 2. 价格 + Save 徽章对齐
**已用 baseline 对齐方案**，跨字号、跨字体最稳。如运营反馈 badge 偏上/偏下：
- 偏下 → 微调 `.bpc-savings-badge` 加 `align-self: center` 配合负 margin
- 偏上 → 反向

绝对不要"猜数字"，先看 DevTools 测量像素差再调整。

### 3. 占位符替换的边界
- 富文本编辑器会把 `[product-card:xxx]` 包成 `<p>[product-card:xxx]</p>`，必须先替换 `<p>...</p>` 整段
- 也要兜底替换裸占位符
- 占位符 ID 必须 `| strip` 处理空格
- 占位符 ID 为空时跳过

### 4. CSS 加载策略
- **Horizon 主题**：因硬编码方案无法判断文章是否含产品卡，CSS 改为无条件加载（体积小，影响可忽略）
- **Impact 主题**：仍可按需加载（`section.blocks` 可用）

### 5. design_mode 占位
Horizon 路径里 block 不直接渲染产品卡，需在 `request.design_mode` 下渲染**可见的提示标记**，否则运营在 Theme Editor 里点不到这个 block，无法配置。

### 6. shopify_attributes
渲染产品卡 HTML 时一定要在外层 wrapper 加 `{{ block.shopify_attributes }}`，否则 Theme Editor 高亮和点选失效。

### 7. Horizon block 文件命名（重要坑）
Horizon 主题里 `blocks/_xxx.liquid`（下划线前缀）= 私有 block，只能被 `content_for` 显式调用，**不会出现在 Theme Editor 的 "Add block" 菜单中**。运营会搜不到。

让运营可以自由添加的 block 文件名**必须不带下划线前缀**，例如 `blocks/blog-product-card.liquid`（正确）vs `blocks/_blog-product-card.liquid`（错误，搜不到）。

对应地，引用代码里 `block.type` 字符串也是文件名（不带 `.liquid`、不带下划线）：
```liquid
{# 正确：#}
{% if sibling.type == 'blog-product-card' %}

{# 错误：#}
{% if sibling.type == '_blog-product-card' %}
```

### 8. Horizon 占位符前台不替换（仍显示 `%%bpc:xxx%%` 原文）
**不再建议在 `_blog-post-content.liquid` 或通过 `section.blocks` 做替换**。正确做法见 A.4 节"正确方案：硬编码占位符映射"。

### 9. 富文本把 `<meta charset="utf-8">` 插进占位符
后台 HTML 可能变成 `<span>[product-card:<meta charset="utf-8">inhaler]</span>`，与标准 `[product-card:inhaler]` 不匹配。处理：在 replace 循环**之前**对 `article.content` 全局 `replace` 剔除常见 `<meta charset=...>` 片段；并增加 `<span>token</span><br>` 等包裹形态的 replace（见 article-process snippet）。**仍建议**运营在文章里改回纯文本占位符 `[product-card:inhaler]`，避免 RTE 再污染。

### 10. 新增占位符 ID 的操作步骤（Horizon 主题）
当需要在新的文章中使用不同的占位符 ID 时：
1. 在 `snippets/blog-product-card-article-process.liquid` 的 `for/case` 循环中添加新的 `when` 分支
2. 在 `blocks/blog-product-card.liquid` 的 Theme Editor 中添加对应 block（仅用于 design_mode 提示）
3. 在文章正文插入 `%%bpc:新ID%%`
4. 推送代码，刷新验证

---

## 运营操作流程（实施完告诉用户）

1. Shopify 后台 → "在线商店" → 主题 → 自定义 → 选 Blog post 模板 → 选要编辑的文章
2. 给该 section 添加 **Blog Product Card** block
3. 配置：
   - 占位符 ID（英文/数字唯一标识，如 `inhaler`、`card-1`）
   - 选产品
   - 可选填卖点和按钮文案
4. 在后台 "Blog posts" 编辑文章正文，在想要插入产品卡的位置 **新建一个段落**，只输入下面**任选一种**（与 ID 一致）：
   - **推荐（富文本友好）**：`%%bpc:inhaler%%`
   - 标准：`[product-card:inhaler]`
5. 保存，前台刷新即可看到产品卡

同一篇文章多张卡：多个 Block + 多个不同 ID + 多段占位符。

**不要**从网页整页复制占位符；**要**在编辑器里手打或从 Theme Editor 提示里复制**纯文本**一行。

---

## 验证清单（实施后必跑）

- [ ] 占位符在段落之间正确替换为产品卡，不留空 `<p>`
- [ ] 不存在的占位符（如运营手误）以原文文本出现，不会误替换
- [ ] Learn More 按钮**没有下划线**（重点查这个，是常见坑）
- [ ] 价格、划线价、Save XX% 徽章**视觉对齐**
- [ ] Add to Cart 真实可加购（点后 cart 数量 +1）
- [ ] 卖完商品显示 Sold Out 且禁用按钮
- [ ] 移动端：卡片单列堆叠、按钮组撑满宽度
- [ ] DevTools 看 HTML 中**搜不到** `[product-card:` 或 `%%bpc:` 残留
- [ ] CSS 文件加载正常
- [ ] 多语言站点：占位符是 ASCII，不被翻译流程影响

---

## 模板文件清单

所有可直接拷贝的代码模板都在本 skill 的 `templates/` 子目录：

```
templates/
├── blog-product-card.css                       ← 复制到 assets/（主题无关，跨主题通用）
├── blog-product-card-inline.liquid             ← 复制到 snippets/（主题无关，跨主题通用）
├── snippets/
│   └── blog-product-card-article-process.liquid ← 复制到 snippets/（Horizon 硬编码版）
├── horizon/
│   ├── blog-product-card.liquid                ← 复制到 blocks/（文件名不能带下划线前缀！）
│   └── main-blog-post-insert.liquid            ← 替换 main-blog-post.liquid 中 content_for 正文部分
└── impact/
    ├── main-article-snippet.liquid             ← 在 main-article.liquid 顶部插入这段 liquid
    └── main-article-block-schema.json          ← 在 main-article.liquid 的 schema "blocks" 数组中追加这条
```

实施时直接读这些模板文件再写入项目对应位置。

---

## 已实施过的项目

| 项目 | 主题 | 路径 | 实施日期 | 备注 |
|---|---|---|---|---|
| Hauswirt.com | Impact | 路径 B（用主题原生 price-list/product-badges） | 2026-05-01 | section.blocks 可用，动态匹配正常 |
| Neobay | Horizon | 路径 A（硬编码版） | 2026-05-04 | section.blocks 不可用，必须硬编码 |

后续新项目实施完，**追加到此表**，方便后面对照参考。
