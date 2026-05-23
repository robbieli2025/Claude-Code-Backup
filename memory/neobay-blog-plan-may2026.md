---
name: Neobay Blog Plan May 2026
description: Neobay 5月 Blog 月度内容规划（12篇）及完成进度
type: project
originSessionId: 8e6e316d-6dab-4894-86f1-6bcab0f86270
---
## 内容策略框架（4:4:4）

- 症状搜索层 4篇：捕获搜索流量，用户搜"猫为什么X"
- 知识教育层 4篇：深度指南，长尾关键词，建立专业权威
- 产品转化层 4篇：对比、教程、案例，直接带产品卡

## Shopify Store 信息

- Store: neobaypet.myshopify.com
- Admin API Token: 通过 Shopify Partner Dashboard → Cloud Code Assistant app 获取，scopes: write_content, write_products, write_product_feeds, write_files, read_orders（24h 过期，需 refresh_token.py 自动刷新）
- Blog ID: 89686802530（handle: blog）
- API 无 read_themes/write_themes 权限，模板推送需手动 `shopify theme push`

## 第1周（5/4-5/10）：症状驱动 + 基础认知

| # | 选题 | 层级 | 状态 | Article ID |
|---|------|------|------|-----------|
| 1 | Why Does My Cat Cough After Running or Playing? | 症状 | ✅ 已发布 | 564498366562 |
| 2 | Feline Asthma vs. Hairball: How to Tell the Difference | 症状 | ✅ 已发布 | 564498432098 |
| 3 | What Is a Cat Inhaler Spacer and Why Does Your Vet Recommend One? | 转化 | ✅ 已发布（模板未推送） | 564501348450 |

### 待办：第1周遗留
- 文章 #3 的 `blog_product_card_spacer` block 已添加到本地 `templates/article.json`，但未推送到 Shopify（API 无权限）。需手动执行 `cd /Users/robbieli/Github/Neobay && shopify theme push --store neobaypet.myshopify.com`，否则 `%%bpc:spacer%%` 占位符不会渲染为产品卡。

## 第2周（5/11-5/17）：深度教育 + 信任建设

| # | 选题 | 层级 | 状态 |
|---|------|------|------|
| 4 | How Vets Diagnose Feline Asthma: Tests, X-Rays, and What to Expect | 知识 | ✅ 已发布 | 564541161570 |
| 5 | Common Triggers That Make Your Cat's Asthma Worse | 知识 | ✅ 已发布 | 564541194338 |
| 6 | AeroKat vs Neobay: Which Cat Inhaler Spacer Is Right for You? | 转化 | ✅ 已发布 | 564547125346 |

## 第3周（5/18-5/24）：场景扩展 + 情感共鸣

| # | 选题 | 层级 | 状态 |
|---|------|------|------|
| 7 | Why Is My Cat Breathing Fast While Sleeping? | 症状 | ✅ 已发布 | 564551090274 |
| 8 | How to Train Your Cat to Accept an Inhaler Mask (Step-by-Step) | 知识 | ✅ 已发布 | 564553252962 |
| 9 | Real Cat Owner Story: How We Managed Our Cat's Asthma Without Daily Pills | 转化 | ✅ 已发布 | 564554596450 |

## 第4周（5/25-5/31）：长尾覆盖 + 购买决策

| # | 选题 | 层级 | 状态 |
|---|------|------|------|
| 10 | Can Cats Use Human Inhalers? What Every Pet Owner Must Know | 症状 | ✅ 已发布 | 564555219042 (Feline Asthma blog) |
| 11 | Cat Flu or Feline Asthma? How to Tell the Difference and Get the Right Treatment | 知识 | ✅ 已发布 | 564562198626 (Feline Asthma blog) |
| 12 | 5 Signs Your Cat's Inhaler Spacer Isn't Working (And How to Fix It) | 转化 | ✅ 已发布 | 564570194018 (Spacer Guides blog) |

> **2026-05-13 调整：** #11 从 Bronchitis 改为 Cat Flu vs Asthma，基于关键词缺口分析（Cat Flu 集群 25 个未布局关键词，流量更大）。Bronchitis 移至 Phase 3（7月）。详见 [[neobay-content-strategy]]。

## 当前进度：12/12 完成 ✅ Phase 1 完结

## 5月追加（5篇）— 急救+环境+费用

| # | 选题 | 层级 | 状态 | Article ID |
|---|------|------|------|-----------|
| 16 | Cat Gasping for Air? Emergency Signs vs. Manageable Symptoms | 症状 | ✅ 已发布 | 564572258402 (Cat Breathing blog) |
| 19 | Cat Litter and Feline Asthma: Is Your Litter Making It Worse? | 知识 | ✅ 已发布 | 564580712546 (Feline Asthma blog) |
| 20 | Cat Asthma Attack: Step-by-Step Emergency Response Guide | 症状 | ⏳ 待写 | — |
| 21 | How Much Does Cat Asthma Treatment Cost? A Realistic Breakdown | 转化 | ⏳ 待写 | — |
| 23 | Do Air Purifiers Help Cats with Asthma? The Evidence | 知识 | ✅ 已发布 | 564590248034 (Feline Asthma blog) |

> 发布节奏：5/19(Mon) - 5/31(Sat)，约每2天1篇。当前进度：3/5 完成。

> **5月后续：** Phase 2/3 已被 [[neobay-blog-plan-jun-nov-2026]] 替代。原规划 6-11月 50篇（6月10篇），2026-05-16 调整为 5月追加5篇+6-11月50篇（6月缩至8篇）。2026-05-17 基于 Amazon 评论分析替换 #51/#58/#61 为3篇高转化新选题。全部基于 Reddit+Google+YouTube+Amazon 全渠道调研验证。

## 已发布文章汇总（13篇，含更早期的）

| 发布日期 | 标题 | Handle | ID |
|---------|------|--------|-----|
| 2026-04-09 | How to Administer Inhaled Medication Stress-Free | how-to-administer-inhaled-medication-stress-free | 564382793826 |
| 2026-04-09 | Is Your Cat Sneezing? The Ultimate Guide to Feline Rhinitis | the-ultimate-guide-to-feline-rhinitis | 564387774562 |
| 2026-04-10 | Why Is My Cat Wheezing? | why-is-my-cat-wheezing | 564392132706 |
| 2026-05-02 | Why Does My Cat Cough After Running or Playing? | why-does-my-cat-cough-after-running | 564498366562 |
| 2026-05-02 | Feline Asthma vs. Hairball: How to Tell the Difference | feline-asthma-vs-hairball | 564498432098 |
| 2026-05-02 | What Is a Cat Inhaler Spacer? | what-is-a-cat-inhaler-spacer | 564501348450 |
| 2026-05-09 | How Vets Diagnose Feline Asthma: Tests, X-Rays, and What to Expect | how-vets-diagnose-feline-asthma-tests-x-rays-and-what-to-expect | 564541161570 |
| 2026-05-09 | Common Triggers That Make Your Cat's Asthma Worse | common-triggers-that-make-your-cats-asthma-worse | 564541194338 |
| 2026-05-10 | AeroKat vs Neobay: Which Cat Inhaler Spacer Is Right for You? | aerokat-vs-neobay-which-cat-inhaler-spacer-is-right-for-you | 564547125346 |
| 2026-05-11 | Why Is My Cat Breathing Fast While Sleeping? | why-is-my-cat-breathing-fast-while-sleeping | 564551090274 |
| 2026-05-12 | How to Train Your Cat to Accept an Inhaler Mask (Step-by-Step) | how-to-train-your-cat-to-accept-an-inhaler-mask | 564553252962 |
| 2026-05-12 | Real Cat Owner Story: How We Managed Our Cat's Asthma Without Daily Pills | real-cat-owner-story-managed-feline-asthma-without-daily-pills | 564554596450 |
| 2026-05-13 | Can Cats Use Human Inhalers? What Every Pet Owner Must Know | can-cats-use-human-inhalers | 564555219042 |
| 2026-05-15 | Cat Flu or Feline Asthma? How to Tell the Difference and Get the Right Treatment | cat-flu-or-feline-asthma | 564562198626 |
| 2026-05-16 | 5 Signs Your Cat's Inhaler Spacer Isn't Working (And How to Fix It) | signs-cat-inhaler-spacer-not-working | 564570194018 |
| 2026-05-17 | Cat Gasping for Air? Emergency Signs vs. Manageable Symptoms | cat-gasping-for-air-emergency-vs-manageable-symptoms | 564572258402 |
| 2026-05-19 | Cat Litter and Feline Asthma: Is Your Litter Making It Worse? | cat-litter-feline-asthma | 564580712546 |
| 2026-05-22 | Do Air Purifiers Help Cats with Asthma? The Evidence | do-air-purifiers-help-cats-with-asthma | 564590248034 |

## 写作规范

- Hero image: 1200x675，从 Unsplash 下载，通过 Shopify Files (stagedUploadsCreate) 上传，用 CDN URL 设置 article.image.src
- Alt text: 描述性英文，与文章主题相关
- Product card 占位符: `%%bpc:ID%%`（ID 需与 article.json 中 blog-product-card block 的 placeholder_id 一致）
- 内链: 按 `references/internal-linking.md` 的 Cluster 矩阵和 6 条规则执行，每篇至少 3 个内链 + 产品页
- SEO: 通过 metafields 设置 title_tag 和 description_tag
- AI GEO: 按 `references/ai-geo.md` 执行，Key Takeaways 每条可独立引用，FAQ 自包含，数据附来源
- 文章结构: Key Takeaways → 正文 → FAQ → What to Do Next → Sources
- 英文 DTC 文案风格，利益点前置
