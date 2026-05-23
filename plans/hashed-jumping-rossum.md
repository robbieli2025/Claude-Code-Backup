# Plan: Neobay Footer 重新设计

## Context

当前 footer 只有邮箱订阅 + utilities bar（版权/政策弹出框/社交链接），非常单薄。缺少 logo、导航菜单、payment icons。对于 DTC 电商网站，footer 是 SEO 内链、信任建设和转化的重要位置。

## 当前问题

1. 无导航菜单 — 用户和搜索引擎缺少快捷路径
2. 无 Logo — 缺少品牌识别
3. 无 Payment Icons — 缺少信任信号
4. 社交链接是占位 URL — 前台实际不显示图标
5. 政策链接藏在弹出框里 — 不够直观

## 新 Footer 布局

### Desktop: 4 列

```
┌─────────────────┬──────────┬──────────┬──────────┐
│  Neobay Logo    │  Learn   │  Support │  We      │
│  Tagline        │          │          │  Accept  │
│  Email CTA      │          │          │          │
│  [Email Form]   │          │          │  💳💳💳  │
├─────────────────┴──────────┴──────────┴──────────┤
│  © 2026 Neobay Pet          📘 📸 ▶️             │
└──────────────────────────────────────────────────┘
```

### Mobile: 单列，菜单折叠为 Accordion

```
Neobay Logo
Tagline + Email
─────────────
▶ Learn (accordion)
▶ Support (accordion)
Payment Icons
─────────────
© 2026 Neobay Pet | Social
```

## 实现方案

### 修改文件：`sections/footer-group.json`

#### Main Footer Section — 4 个 top-level blocks：

**1. `brand-group`** (type: `group`)
内含 4 个子 block：

| 子 block | 类型 | 内容 |
|---------|------|------|
| `brand-logo` | `logo` | Neobay logo, pixel_height: 40 |
| `brand-tagline` | `text` | "Helping cats breathe easier, one chamber at a time." |
| `email-cta` | `text` | "Join our email list for exclusive deals and early access." |
| `email-form` | `email-signup` | 圆角边框 + 箭头按钮 |

**2. `learn-menu`** (type: `menu`, accordion on mobile)

| 链接文字 | URL |
|---------|-----|
| Feline Asthma | `/blogs/blog/tagged/feline-asthma` |
| Cat Breathing | `/blogs/blog/tagged/cat-breathing` |
| Cat Health | `/blogs/blog/tagged/cat-health` |
| Respiratory Care | `/blogs/blog/tagged/respiratory-care` |
| Buyer's Guide | `/blogs/blog/tagged/buyers-guide` |
| Why Is My Cat Coughing? | `/pages/why-is-my-cat-coughing` |
| Our Story | `/pages/brand-story` |

**3. `support-menu`** (type: `menu`, accordion on mobile)

| 链接文字 | URL |
|---------|-----|
| FAQs | `/pages/faqs` |
| Contact Us | `/pages/contact` |
| Return Policy | `/pages/return-policy` |
| Shipping Policy | `/policies/shipping-policy` |
| Privacy Policy | `/policies/privacy-policy` |

**4. `payment-block`** (type: `payment-icons`)

#### Footer Utilities Section — 2 个 blocks（移除 policy-list）：

| Block | 内容 |
|-------|------|
| `footer-copyright` | © 2026 Neobay Pet (保留) |
| `social_links` | Facebook + Instagram + YouTube (移除 policy-list，政策已移入 Support 菜单) |

### 社交链接 URL

| 平台 | URL |
|------|-----|
| Facebook | `https://www.facebook.com/neobaypet` |
| Instagram | `https://www.instagram.com/neobaypet/` |
| YouTube | `https://www.youtube.com/@Neobaypet` |
| TikTok / X | 留空 |

### 需要在 Shopify Admin 手动创建的菜单

推送主题后，在 **Settings → Navigation** 创建 2 个菜单：

**1. `footer-learn`（heading: "Learn"）**— 7 个链接，前 5 个用 Custom URL 指向 blog tag 页，后 2 个链接到现有 page

**2. `footer-support`（heading: "Support"）**— 5 个链接，FAQs/Contact/Return Policy 链接到 page，Shipping/Privacy Policy 链接到 `/policies/` 路径

## 不需要修改的文件

- `sections/footer.liquid` — 已支持所有 block 类型（group, menu, logo, text, email-signup, payment-icons）
- `blocks/menu.liquid` — 已支持 accordion + link_list
- `blocks/logo.liquid` — 已存在
- `blocks/payment-icons.liquid` — 已存在
- `sections/footer-utilities.liquid` — 结构不变，只减少 block 数量

## 关键变化总结

| 改动 | 之前 | 之后 |
|------|------|------|
| 品牌列 | 无 logo，只有邮箱 CTA 文字 | Logo + Tagline + Email |
| 导航 | 无 | Learn (7链接) + Support (5链接) |
| Payment Icons | 无 | 有，独立列 |
| 政策链接 | utilities bar 里的弹出框 | Support 菜单里的独立入口 |
| 社交链接 | 占位 URL（前台不显示） | 实际品牌主页 URL |
| About Peter Jonathan | — | 不放 |
| Collection | — | 不放（只有一款产品） |
| Success Stories | 独立页面入口 | 归入 blog 内容集群，不放独立入口 |

## 验证

1. `shopify theme push --store neobaypet.myshopify.com` 推送主题
2. 在 Shopify Admin 创建 `footer-learn` 和 `footer-support` 两个菜单
3. 访问网站任意页面底部，确认：
   - 4 列布局正确（品牌+邮箱 | Learn | Support | Payment）
   - 移动端菜单折叠为 accordion
   - 社交图标（Facebook/Instagram/YouTube）正确显示
   - 所有链接指向正确页面
   - Payment Icons 显示
