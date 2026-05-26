---
name: neobay-blog-optimization-plan
description: 现有Blog文章优化计划：按优先级排列，每天更新1篇，直到清零
metadata: 
  node_type: memory
  type: project
  originSessionId: ebe329b9-92b1-491e-8b70-714c33265b11
---

## 优化原则

- **结构性问题优先**（缺 Key Takeaways / FAQ / Sources / 产品卡）→ 需重写内容
- **配图问题其次**（零配图 / 仅1张 / 无 inline style）→ 需生图+插入
- **小修批量处理**（inline style 批量替换、Key Takeaways 标题删除）→ 一次脚本搞定
- 每天更新 1 篇老文章，直到待优化清零
- 更新时保持原 URL slug 不变，避免影响已建立的索引

## 已完成

| 日期 | 文章 | 操作 |
|------|------|------|
| 2026-05-24 | #1 How to Administer Inhaled Medication Stress-Free | 完全重写 + LinkFox 生图 3张 + 发布 + metafields |
| 2026-05-24 | #20 Cat Asthma Attack Emergency Response | 删除 Key Takeaways 标题 |
| 2026-05-24 | #21 How Much Does Cat Asthma Treatment Cost | 删除 Key Takeaways 标题 |
| 2026-05-25 | #2 Is Your Cat Sneezing? Feline Rhinitis | 完全重写(1500→2900词) + LinkFox 生图 3张 + KT/FAQ/Sources/PC + metafields |
| 2026-05-26 | #3 Why Is My Cat Wheezing? | 完全重写 + LinkFox 生图 3张 + KT/FAQ(6)/Sources/PC + metafields |
| 2026-05-26 | #4 Common Triggers | 补KT + LinkFox生图 2张 + 修image style + Sources格式 |

## 待优化清单（按严重程度排序）

### Tier 1：需要重写（缺多个核心模块）

| 优先级 | 文章 | Blog | 核心问题 | 需要做的 |
|--------|------|------|---------|---------|
| 1 | Is Your Cat Sneezing? Feline Rhinitis (564387774562) | Cat Breathing | 无KT/FAQ/Sources/PC/配图，仅1487词 | 完全重写 + LinkFox生图 + 产品卡 |
| 2 | Why Is My Cat Wheezing? (564392132706) | Cat Breathing | 无KT/Sources/PC/配图 | 完全重写 + LinkFox生图 + 产品卡 |
| 3 | Common Triggers (564541194338) | Feline Asthma | 无KT/Table，仅1张图无style | 补KT/Table + LinkFox生图 + inline style |
| 4 | AeroKat vs Neobay (564547125346) | Spacer Guides | 无KT，仅1张图无style | 补KT + LinkFox生图 + inline style |

### Tier 2：需要补内容（缺1-2个模块）

| 优先级 | 文章 | Blog | 核心问题 | 需要做的 |
|--------|------|------|---------|---------|
| 5 | Cat Litter and Feline Asthma (564580712546) | Feline Asthma | 无KT/配图 | 补KT + LinkFox生图 |
| 6 | How Vets Diagnose Feline Asthma (564541161570) | Feline Asthma | 无KT/配图 | 补KT + LinkFox生图 |
| 7 | Why Does My Cat Cough After Running? (564498366562) | Feline Asthma | 无PC/配图 | 补产品卡 + LinkFox生图 |
| 8 | Feline Asthma vs. Hairball (564498432098) | Feline Asthma | 无PC/inline style | 补产品卡 + inline style |
| 9 | Cat Asthma Attack Emergency Response (564593426530) | Feline Asthma | 仅1张配图 | 补1-2张LinkFox生图 |
| 10 | How Much Does Cat Asthma Treatment Cost? (564595490914) | Feline Asthma | 无KT | 补Key Takeaways内容 |

### Tier 3：小修（配图不足或缺 inline style）

| 优先级 | 文章 | Blog | 问题 |
|--------|------|------|------|
| 11 | What Is a Cat Inhaler Spacer? (564501348450) | Spacer Guides | 仅1张图，无inline style |
| 12 | Do Air Purifiers Help Cats? (564590248034) | Feline Asthma | 无配图 |
| 13 | Why Is My Cat Breathing Fast? (564551090274) | Cat Breathing | 无配图 |

### 批量修复（一次性脚本处理，不占每日配额）

| 问题 | 涉及文章数 | 操作 |
|------|-----------|------|
| Key Takeaways 标题删除 | ~10篇仍有`<h2>Key Takeaways</h2>` | Python脚本批量替换 |
| inline style 补充 | ~15篇有图但缺style | Python脚本批量添加 |
| Real Cat Owner Story 无table | 1篇 | 补table或接受无table（故事类文章） |

## 进度追踪

- Tier 1: 4/4 完成 ✅
- Tier 2: 0/6
- Tier 3: 0/3
- 批量修复: 3/3 完成 ✅
  - KT 位置修正：9 篇（5 篇 KT 移至 pos0 + 6 篇补充 `<hr>`）
  - 图片 inline style：5 篇 8 张图修复
  - Real Cat Owner Story：无 table，故事类文章不需要
