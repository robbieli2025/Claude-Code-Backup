# Blog 产品卡 - Liquid 占位符方案

## Context

需要在 blog 文章任意位置插入产品卡，产品卡包含 Add to Cart 和 Learn More 两个 CTA。当前主题（Impact by Maestrooo）的 `blog-product-card.liquid` 只能作为 section 添加在文章底部，无法插入内容中间。Shopify 的 `article.content` 是整段输出，无法原生拆分。

## 方案：Liquid 占位符替换

在 `article.content` 输出前，用 Liquid 的 `replace` 过滤器把占位符替换为产品卡 HTML。

### 使用方式

写文章时，在 HTML 视图中插入：
```
[product:kitchen-stand-mixer-m5]
```
Liquid 自动替换为该产品的卡片 HTML。产品数据（标题、价格、图片、库存）实时从 Shopify 获取，无需手动维护。

### 实现步骤

#### 1. 创建产品卡 snippet：`snippets/blog-product-card-inline.liquid`

- 接收参数：`product`（产品对象）、`highlights`（可选卖点文字）
- 渲染：产品图 + 标题 + 卖点 + 价格 + 两个按钮
- 使用主题原生的 `snippets/button.liquid` 渲染按钮，风格与全站一致
- Add to Cart 按钮使用主题已有的 `<product-form>` 自定义元素（`is="product-form"` extends "form"），提交到 `/cart/add.js`，触发 `variant:add` 和 `cart:change` 事件，购物车抽屉自动更新
- Learn More 按钮链接到产品详情页
- 样式使用与主题一致的 CSS 变量，内联 `<style>` 标签

#### 2. 修改 `sections/main-article.liquid`

在 `{{ article.content }}` 输出前，添加 Liquid 逻辑：
- 用 `split` 按占位符模式拆分文章内容
- 遍历每个片段，检测是否是 `[product:xxx]` 格式
- 如果是，用 `all_products[handle]` 获取产品，渲染 snippet
- 如果不是，直接输出原文

**具体实现方式**：创建一个 snippet `snippets/article-content-with-products.liquid` 来处理替换逻辑，保持 main-article.liquid 简洁。

#### 3. 更新 `sections/blog-product-card.liquid`

- 移除旧的自定义样式（#1a73e8 蓝色按钮等），改为复用 inline 版本
- 或者保留底部 section 用法不变，两种方式共存

### 需要修改/创建的文件

| 文件 | 操作 |
|------|------|
| `snippets/blog-product-card-inline.liquid` | 新建 - 产品卡渲染模板 |
| `snippets/article-content-with-products.liquid` | 新建 - 占位符替换逻辑 |
| `sections/main-article.liquid` | 修改 - 第101行 `{{ article.content }}` 改为 render snippet |

### 限制

- `all_products` 限制单页最多约20个产品，blog 中一般不会超过这个数
- 占位符格式固定为 `[product:handle]`，不支持变体选择（默认第一个可用变体）
- 不支持在占位符中传 highlights 参数（可通过 section settings 或 metafields 扩展）

### 验证方式

1. 推送主题到测试分支
2. 编辑一篇测试 blog 文章，在 HTML 视图中插入 `[product:kitchen-stand-mixer-m5]`
3. 查看文章页面，确认产品卡正确渲染
4. 点击 Add to Cart，确认购物车抽屉更新
5. 点击 Learn More，确认跳转到产品页
6. 测试 Sold Out 状态产品，按钮应禁用
7. 移动端测试响应式布局
