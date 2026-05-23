# Neobay Blog #23: Do Air Purifiers Help Cats with Asthma? The Evidence

## Context

5月追加 Blog 的第3篇（进度 2/5）。#19 Cat Litter 文章已内链到本篇（`/blogs/blog/do-air-purifiers-help-cats-with-asthma`），目前是 404，需优先发布。

## Phase 0 调研结论

### Google Autocomplete 关键发现
- "do air purifiers help cats with asthma" 是高频 autocomplete 建议，确认真实搜索需求
- Reddit 后缀高频：用户寻找真实经验而非商业内容
- "hepa filter for cat asthma" 独立出现 → 需要解释 HEPA 技术原理
- "are air purifiers safe/bad/dangerous for cats" → 需覆盖臭氧安全疑虑
- "do air purifiers help cats breathe better" → 情感驱动，适合做 hook

### Reddit 关键发现
- **核心痛点**：用户不是问"有没有用"，而是"我做了所有事还是不行"（$200 air purifier + meds + STILL ATTACKS）
- **误区**：一台净化器覆盖全屋、二手净化器安全、"低尘"猫砂就够、激素针=治愈
- **情感语言**："coughing fits"、"hacking"、"wheezing like crazy"、"burrito her"
- **争议**：预算 vs 覆盖（买不起多台）、一台大机 vs 多台小机、HEPA 滤网可能重新释放过敏原
- **安全担忧**：HEPA filter triggering asthma（净化器让症状加重）

### SERP 竞品分析（基于调研 + 已知格局）

| Rank | Site | 内容类型 | 估计字数 | EEAT | 核心弱点 |
|------|------|---------|---------|------|---------|
| 1 | The Spruce Pets | 产品测评列表 | ~1500 | ⭐⭐ | 纯产品推荐，无医学证据，无兽医引用 |
| 2 | Catster | 产品测评+简短科普 | ~2000 | ⭐⭐⭐ | 科普浅，不区分过敏和哮喘 |
| 3 | Hepper | 产品测评 | ~1200 | ⭐⭐ | 无 FAQ，无具体数据 |
| 4 | PetMD | 猫哮喘概述 | ~2500 | ⭐⭐⭐⭐ | 不是空气净化器专题，只提一句环境管理 |
| 5 | PawTracks/Daily Paws | 轻科普 | ~1000 | ⭐⭐ | 无 HEPA 原理，无臭氧警告 |

### Surpass Plan — 5 个超越维度

1. **证据深度**：竞品全是产品列表，没有一篇引用兽医文献证明空气净化器对猫哮喘的效果。我们引用 Reinero 等人环境触发研究 + EPA 室内空气质量数据，用证据说话而非靠产品推荐数量
2. **HEPA 原理 + 臭氧警告**：竞品没有一个解释 HEPA 为什么有效（0.3微米过滤精度 vs 猫哮喘触发物粒径），也没有一篇警告臭氧发生器对猫的危险。我们两个都做
3. **"做了所有事还是不行"的实战指南**：竞品都说"买净化器"，没人回答"买了还是发作怎么办"。我们覆盖：净化器 + 药物 + 环境管理的组合策略，一台 vs 多台、放哪间房、CADR 怎么选
4. **FAQ 覆盖面**：竞品 FAQ 0-2 条。我们 6 条，覆盖 Reddit 最高频问题（安全、臭氧、二手净化器、一台够不够）
5. **产品卡自然嵌入**：竞品要么是纯 affiliate 链接，要么完全不提治疗。我们在"空气净化器不够，药物才是基础"这一段自然嵌入 `%%bpc:spacer%%`

---

## Phase 1: 文章大纲

```
# Do Air Purifiers Help Cats with Asthma? The Evidence

**Title Tag**: Do Air Purifiers Help Cats with Asthma? What the Evidence Says
**Meta Description**: Bought an air purifier but your cat still coughs? Learn what the research says about HEPA filters for feline asthma, which purifiers work, and why air quality alone isn't enough.
**URL Slug**: /blogs/blog/do-air-purifiers-help-cats-with-asthma

## Key Takeaways
- 空气净化器可以减少猫哮喘的环境触发物，但不能替代药物
- HEPA 过滤器对猫哮喘有效的原因：0.3微米精度覆盖了猫哮喘主要触发物
- 臭氧发生器对猫有害——永远不要在猫周围使用
- 一台净化器通常不够——需要根据房间数和 CADR 合理配置
- 空气净化器 + 吸入药物 + 环境管理的组合才是完整的治疗策略

## [Hook intro]
花了 $200 买空气净化器，无香薰产品，按时给猫用吸入器——但猫还是每天多次哮喘发作。Reddit 上这条帖子有上百条回复，因为太多猫主人有同样经历。

## How Airborne Triggers Cause Asthma Attacks in Cats
- 复习：猫哮喘的免疫机制（简短，内链到 triggers 文章）
- 空气中触发物的粒径分布图（表格）：
  - 猫皮屑 1-10μm
  - 尘螨粪便 10-40μm
  - 花粉 10-100μm
  - 香烟烟雾 0.01-1μm
  - 猫砂粉尘 PM2.5
- 为什么猫比人更脆弱（小气道 + 近距离 + 挖砂行为，内链到 cat litter 文章）

## What HEPA Filters Actually Do (And Why That Matters for Cats)
- HEPA 定义：捕获 99.97% 的 0.3μm 粒子
- 0.3μm 是 MPPS（Most Penetrating Particle Size）——更大的粒子反而更容易被捕获
- 所以 HEPA 能捕获猫皮屑、尘螨、花粉、大部分猫砂粉尘
- 但 HEPA 不能捕获气体（VOCs、香水、二手烟的气态成分）
- 活性炭层的补充作用

## What the Research Says About Air Purifiers and Feline Asthma
- Reinero et al. (2019)：环境触发物管理是治疗的重要组成
- EPA 室内空气质量数据：HEPA 可减少室内 PM2.5 50-80%
- 但没有针对"猫用空气净化器"的 RCT——诚实承认证据局限
- 机制推理有效 ≠ 临床试验已证明 → "合理但非充分"

## Ozone Generators: The Air Purifier Type That Can Harm Your Cat
- 臭氧发生器 ≠ HEPA 空气净化器
- 臭氧对猫呼吸道的刺激（EPA 警告：臭氧本身是呼吸道刺激物）
- 一些"离子"净化器也会产生微量臭氧
- 如何识别和避免：看是否有 CARB 认证、是否标注"ozone-free"

%%bpc:spacer%%

## How to Choose an Air Purifier for a Cat with Asthma
- 关键参数：CADR（Clean Air Delivery Rate）——按房间面积选
- 一台 vs 多台：为什么一台通常不够（空气不跨房间流通）
- 放置位置：猫待得最多的房间优先
- 噪音：猫对声音敏感，高噪音可能让猫避开净化器覆盖区域
- 滤网更换频率：积满过敏原的滤网可能重新释放（Reddit 用户反映的问题）

## Beyond the Purifier: A Complete Environmental Management Plan
- 净化器 + 低尘猫砂（内链到 cat litter 文章）
- 净化器 + 空调管道清洁
- 净化器 + 吸入药物（内链到 what is a spacer）
- 组合策略才是答案——单一措施不够

## FAQ (6 questions from Reddit/Autocomplete)
1. Can an air purifier stop my cat's asthma attacks?
2. Are air purifiers safe for cats?
3. Do I need more than one air purifier for my asthmatic cat?
4. Can a used air purifier make my cat's asthma worse?
5. Should I run the air purifier all the time?
6. What's the difference between HEPA and ozone generators?

## What to Do Next
1. 确认你现有的净化器是 HEPA 而非臭氧型
2. 根据猫待得最久的房间配置净化器
3. 和兽医讨论完整治疗计划（环境管理 + 吸入药物 + 间隔器）

## Sources
```

## Phase 2: 图片方案
- Hero: 1200×675，猫在室内舒适环境中（与空气净化器同框最佳，或窗边阳光）
- Body 1: 猫在兽医处检查呼吸道
- Body 2: 室内环境（低粉尘，清洁）

## Phase 3: 发布计划
- Blog 分类：Feline Asthma (90090766434)
- Tags: feline asthma, air purifier, HEPA filter, cat asthma triggers, indoor air quality
- 内链目标（至少3个）：
  - `/blogs/blog/common-triggers-that-make-your-cats-asthma-worse`（环境触发物）
  - `/blogs/feline-asthma/cat-litter-feline-asthma`（猫砂粉尘，#19 新文章）
  - `/blogs/blog/what-is-a-cat-inhaler-spacer`（间隔器，产品卡上下文）
  - `/products/neobay-cat-aerosol-chamber`（产品页）

## Phase 4-5: 执行步骤
1. 写完整 Markdown 草稿 → `blog-drafts/2026-05-22-do-air-purifiers-help-cats-with-asthma.md`
2. 下载 Unsplash hero image
3. 刷新 Shopify API token
4. 上传图片到 Shopify Files
5. API 发布文章到 Feline Asthma blog
6. 设置 metafields (title_tag, description_tag, author_name, faq_schema)
7. 更新 memory 进度
