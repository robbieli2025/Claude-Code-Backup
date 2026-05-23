# 写作计划：Cat Litter and Feline Asthma: Is Your Litter Making It Worse?

## Context

5月追加5篇中，#16（Cat Gasping）已发布，**#19 是下一篇**。这篇是 Reddit 验证的零竞品内容空白——猫砂粉尘与哮喘的关系，用户高频搜索但现有文章几乎不覆盖。属于 Cluster A（Feline Asthma Core），知识教育层，Blog 分类 Feline Asthma。

---

## 写作质量原则（融合 SEO + GEO + EEAT + 去AI味）

### 去 AI 味规则
- **不写"过度组织"的段落**：AI 倾向于每段都"总-分-总"，真人写作有跳跃、有省略、有侧重点
- **不用 AI 套话**：禁止 "It's important to note"、"Interestingly"、"In conclusion"、"Moreover"、"Furthermore"、"Additionally"
- **句式长短交替**：不用全部长复合句。用短句制造节奏感。一短一长，像真人说话
- **观点要有立场**：不是"some say X, others say Y"的伪平衡，而是基于证据给明确建议
- **用具体细节替代抽象概括**：不说"many cats"而说"about 1 in 20 cats"；不说"various types"而说"clumping clay, crystal, and pine"
- **允许不完美**：真人写作会有轻微的口语化、偶尔的句首连词（But、So）、段落长短不一

### SEO 自然融入
- **关键词在标题和 H2 中自然出现**，不堆砌
- **Title Tag 50-60 字符**，含核心关键词，有吸引力
- **Meta Description 150-160 字符**，痛点钩子 + 核心关键词
- **3-5 个 tags**，覆盖主关键词 + 相关话题
- **内链 4-6 个**，在读者自然想深入时出现，不是为链接而链接

### GEO 结构化自然嵌入
- **Key Takeaways**：4-5 条独立可引用的事实，每条包含具体数字或明确结论——这是给 AI 提取用的，但用人类专家的语气写，不是 bullet point 机器
- **定义锚定**：关键术语首次出现时加粗 + 一句话定义，自然融入句子，不单独抽出
- **引用级统计数据**：数字 + 来源，写成"According to the Cornell Feline Health Center, about 1-5% of all cats..."而不是"Studies show that..."
- **FAQ 自包含**：每个答案 2-4 句，不看全文也能理解，口语化问法，无 markdown 链接
- **对比表格**：猫砂类型对比用 HTML 表格——AI 解析表格优于纯文本，但表格本身是给读者快速比较的，不是硬塞的
- **实体密度**：自然提及具体药名（Fluticasone、Prednisolone）、设备名（spacer chamber、MDI）、机构名（Cornell、AAFP），不堆砌

### EEAT 执行
- **Experience**：开头用猫主真实场景（"You've switched to three different litters, but your cat still coughs after using the box"）
- **Expertise**：引用兽医文献，用正确术语 + 通俗解释
- **Authoritativeness**：Peter Jonathan 统一署名，内链到相关深度文章
- **Trustworthiness**：不确定的事说"we don't have strong evidence"而非硬给结论；"consult your vet"在医疗建议处出现

---

## Phase 0: 写前调研（必须完成）

### 0.1 Google Autocomplete 调研
运行 Python 脚本查询以下前缀：
- `"cat litter asthma"`
- `"cat litter dust breathing"`
- `"best cat litter for asthma"`
- `"cat litter making cat cough"`
- `"dust free cat litter"`
- `"clay litter cats breathing"`
- `"is cat litter bad for cats"`
- `"cat litter respiratory"`

输出：10-20 个真实搜索词，用于 H2/H3 和 FAQ。

### 0.2 Reddit 用户讨论调研
搜索 5+ 组关键词：
- `"cat litter asthma"`
- `"litter dust cat coughing"`
- `"best litter asthma cat"`
- `"clay litter breathing problems"`
- `"cat litter sneezing wheezing"`

提取：Top 问题、常见误解、情绪痛点、真实猫主语言。

### 0.3 SERP Top 10 竞品分析
搜索 `"cat litter feline asthma"` 和 `"best cat litter for cats with asthma"`，分析前 10 结果：
- 标题角度、文章结构、字数、深度、EEAT 信号、内容缺口

### 0.4 竞争优势决策
回答 5 个问题：
1. Reddit 上 Top 3 未被回答的问题
2. 我们 vs Top 10 的差异化角度
3. 应该镜像的猫主真实语言
4. 可包含的具体数据/统计
5. 如何自然连接到 Neobay 产品

---

## Phase 1: 写 Markdown 草稿

### 文章元数据
- **H1:** Cat Litter and Feline Asthma: Is Your Litter Making It Worse?
- **Title Tag:** ~55 chars，含 "cat litter" + "feline asthma"
- **Meta Description:** ~155 chars，含核心关键词 + 痛点钩子
- **URL Slug:** `/blogs/feline-asthma/cat-litter-feline-asthma`
- **Tags:** feline asthma, cat litter, dust-free litter, asthma triggers, cat respiratory health
- **Author:** Peter Jonathan
- **Blog Category:** Feline Asthma (ID: 90090766434)

### 文章结构（大纲，实际写作时灵活调整）

```
# Cat Litter and Feline Asthma: Is Your Litter Making It Worse?

## Key Takeaways（4-5 bullets）
- 每条是独立可引用的事实
- 至少 1 条含具体数字
- 至少 1 条连接到解决方案（spacer/吸入治疗）

[Intro — 真实猫主场景：换了三种猫砂，猫还是咳嗽。引出核心问题]

## Why Cat Litter Dust Is a Hidden Asthma Trigger
  - 粉尘如何进入猫的下呼吸道（机制解释）
  - 猫比人更敏感的原因：贴近地面、刨砂行为、呼吸模式
  - 粉尘颗粒大小与呼吸道沉积（引用具体数据）
  - 自然内链 → #5 Common Triggers

## Which Cat Litters Are Worst for Asthmatic Cats
  ### Clumping Clay Litter: The Biggest Dust Problem
  ### Silica Gel Crystals: Low Dust, Other Concerns
  ### Pine and Wood Pellets: Natural ≠ Allergy-Free
  ### Walnut, Corn, and Paper-Based Litters
  [HTML 表格：各类型粉尘等级、优缺点、推荐指数]

## The Best Cat Litter for Cats with Asthma
  - 低尘品牌推荐（基于实际测试和兽医建议）
  - 关键选购标准
  - 兽医怎么看

%%bpc:spacer%%
（逻辑：换猫砂是环境管理的一环；如果猫已确诊哮喘，还需要医学治疗 → 间隔器）

## How to Switch Your Cat's Litter Without the Stress
  - 7-10 天渐进式换砂步骤
  - 猫拒绝新猫砂怎么办

## Beyond Litter: Other Environmental Triggers in Your Home
  - 猫砂盆位置（远离通风口和空调出风口）
  - 清洁频率和方式
  - 空气净化 → 自然链接到 #23 Air Purifiers

## Frequently Asked Questions（5-6 questions，口语化）
  - Can cat litter cause asthma in cats?
  - What is the best dust-free cat litter for asthma?
  - How do I know if my cat's litter is triggering asthma?
  - Is clumping clay litter bad for cats with asthma?
  - Can switching litter stop my cat's asthma attacks?
  - How long after changing litter will I see improvement?

## What to Do Next
  1. Check your cat's current litter for dust
  2. Talk to your vet about whether litter is a trigger
  3. Consider an inhaler spacer if your cat has been diagnosed

[Final CTA — product link + FAQ/Contact]

---

**Sources**:
- Cornell Feline Health Center
- J Feline Medicine and Surgery
- 其他兽医文献
```

### 写作执行要点
- **目标字数**：2,000-2,500（知识教育层最低 2,000）
- **每段 2-4 句**，偶尔 1 句成段制造节奏
- **数据出现时**：数字 + 来源，写进自然句式，不单独列
- **产品提及**：不超过 2 次自然提及 Neobay 特点（Flow Indicator + Comfort Feeder），各在相关段落有机融入
- **内链出现位置**：读者想深入了解时，不是段落末尾的"see also"

### 内链规划（4-6 个内链）
| 目标 | 锚文本方向 | 位置 |
|------|-----------|------|
| `/blogs/blog/common-triggers-that-make-your-cats-asthma-worse` (#5) | "common asthma triggers" / "environmental triggers" | 粉尘触发器段落 |
| `/blogs/feline-asthma/how-vets-diagnose-feline-asthma-tests-x-rays-and-what-to-expect` (A-Hub) | "how vets diagnose feline asthma" | 何时就医段落 |
| `/blogs/blog/why-is-my-cat-wheezing` (B-Hub) | "why your cat is wheezing" | 症状识别段落 |
| `/products/neobay-cat-aerosol-chamber` (产品页) | 产品链接 | CTA + 间隔器治疗段落 |
| `/pages/faqs` | FAQ 页面 | 结尾段 |

### 产品卡
- `%%bpc:spacer%%` 放在 "The Best Cat Litter for Cats with Asthma" 之后
- 逻辑：环境管理（换猫砂）是第一步，但确诊的猫还需要医学治疗 → 间隔器

### 卖点整合（自然嵌入，不超过各 1 次）
- **Visual Flow Indicator**：在讨论"如何确认猫吸入了药物"时自然提及
- **Comfort Feeder Design**：在讨论"猫对治疗抗拒"时自然提及

---

## Phase 2: 图片准备

| 图片 | 尺寸 | 场景 | 来源 |
|------|------|------|------|
| Featured (hero) | 1200×675 | 猫在使用猫砂盆 / 猫砂场景 | Unsplash |
| Body 1 | 1200×800 | 猫在家中休息（健康状态） | Unsplash |
| Body 2 | 1200×800 | 猫在窗边/不同场景 | Unsplash |

**去重检查**：对照 `references/image-guide.md` 中的 Image Inventory，避免重复使用已有图片。

---

## Phase 3: Blog 分类

**Feline Asthma** (ID: 90090766434) — 讨论猫砂与哮喘触发机制，属于哮喘医学内容。

---

## Phase 4: 发布流程

1. `python3 scripts/refresh_token.py` — 刷新 API token
2. `python3 scripts/publish_article.py extract blog-drafts/2026-05-19-cat-litter-feline-asthma.md`
3. 下载图片 + 验证去重
4. `python3 scripts/publish_article.py publish` — 发布到 Feline Asthma blog
5. `python3 scripts/publish_article.py faq-schema` — 创建 FAQ Schema metafield
6. 验证发布结果

---

## Phase 5: 发布后

1. 更新记忆文件 `neobay-blog-plan-may2026.md`：标记 #19 为 ✅ 已发布
2. 更新 `references/image-guide.md` Image Inventory
3. 回溯内链：在 #5 Common Triggers 文章中添加指向本文的链接
4. 通知用户

---

## 验证方式

- 在 Shopify Admin 预览文章，确认所有段落、图片、产品卡渲染正常
- 确认 FAQ Schema 包含所有 5-6 个问题
- 确认内链可点击且指向正确
- 确认 Blog 分类为 Feline Asthma

---

## 关键文件

- 草稿目标路径：`blog-drafts/2026-05-19-cat-litter-feline-asthma.md`
- 发布脚本：`scripts/publish_article.py`
- Token 刷新：`scripts/refresh_token.py`
- 图片指南：`/Users/robbieli/.claude/skills/neobay-blog/references/image-guide.md`
- 内链架构：`/Users/robbieli/.claude/skills/neobay-blog/references/internal-linking.md`
- 写作风格：`/Users/robbieli/.claude/skills/neobay-blog/references/writing-voice.md`
