# Plan：撰写并发布 #23《Do Air Purifiers Help Cats with Asthma? The Evidence》

## 背景

#23 是5月追加5篇中的第4篇（前有 #16 急救、#19 猫砂、#20 哮喘发作急救、#21 费用明细）。#19（Cat Litter and Feline Asthma）已发布到 neobaypet.com，文中内链引用了 #23。

基本信息：
- **Cluster**：D — 通用猫呼吸健康
- **类型**：知识教育层
- **Blog 分类**：主 Blog（89686802530）
- **产品关联度**：弱（产品卡插入但非核心转化文章）

现有草稿中已有两处提到空气净化器：
- #5 Common Triggers：FAQ 中一段简短回答"Is a HEPA air purifier worth it?"
- #7 Breathing Fast While Sleeping：一句 bullet 提到 HEPA

本文将这些零散提及扩展为深度、循证的环境控制指南。

## 实施步骤

### 第一步：Phase 0 调研

对 "do air purifiers help cats with asthma" 执行 Google Autocomplete + Reddit + SERP Top 10 分析：
- 识别 Reddit 上猫主人最关心的 3 个未解答问题
- 分析 Top 10 排名文章的优势和内容缺口
- 提取真实的猫主人语言用于标题和 FAQ
- 找到竞品文章缺乏的具体数据/统计

### 第二步：撰写 Markdown 草稿

文件路径：`blog-drafts/2026-05-20-do-air-purifiers-help-cats-with-asthma.md`

**元数据：**
- Title：Do Air Purifiers Help Cats with Asthma? The Evidence
- Title Tag：Do Air Purifiers Help Cats with Asthma? What Science Says（50-60 字符）
- Meta Description：Can an air purifier really help your asthmatic cat breathe easier? We review the evidence, HEPA vs ionizer risks, and how to choose the right one.（150-160 字符）
- Slug：`/blogs/blog/do-air-purifiers-help-cats-with-asthma`
- Tags：air purifier for cats, HEPA filter cat asthma, feline asthma environmental control, cat breathing health

**文章结构：**
- **Key Takeaways**（4-5 条，含粗体数据和统计）
- **Intro**：猫主人场景 — 用了药还在咳嗽，是不是家里空气有问题？
- **H2: How Feline Asthma Works（简要）** — 建立"空气中的颗粒物会触发哮喘"的认知
- **H2: What Is a HEPA Air Purifier?** — 定义锚定，解释为什么 0.3 微米是关键
- **H2: What the Science Says — Air Purifiers and Respiratory Health** — 兽医文献 + 人类研究证据（人类研究更丰富，可类比推导）
- **H2: What Air Purifiers Can and Can't Do for Asthmatic Cats** — 平衡视角，不过度承诺
- **H2: How to Choose the Right Air Purifier for a Home with an Asthmatic Cat** — CADR、房间大小、滤网类型、避坑（离子发生器/臭氧）
- **H2: Placement and Usage Tips** — 放在哪个房间、运行多久、换滤网频率
- **H2: Other Environmental Changes That Work WITH an Air Purifier** — 猫砂、清洁用品、湿度控制 → 内链到 #5 和 #19
- `%%bpc:spacer%%`（在环境控制章节之后、FAQ 之前插入）
- **FAQ**：5-6 个问题
- **What to Do Next**：3-4 步行动指南
- **Sources**：引用真实兽医文献

**内链（3-5 条）：**
| 目标 | 锚文本方向 |
|------|----------|
| #5 Common Triggers | "other common asthma triggers in your home" |
| #19 Cat Litter | "how your cat's litter affects their breathing" — 呼应 #19 内链 |
| #7 Breathing Fast While Sleeping | "nighttime breathing issues in cats" |
| 产品页 `/products/neobay-cat-aerosol-chamber` | 最终 CTA |

### 第三步：配图

- **Featured image**：Unsplash 唯一照片，猫 + 家居环境/洁净空气主题，1200×675
- **Body images**：2-3 张不同场景（猫在家放松、空气净化器环境、猫在窗边）
- 验证与现有图片库存不重复

### 第四步：API 发布

- 刷新 token：`python3 scripts/refresh_token.py`
- Markdown → HTML 转换
- POST 到 Blog ID 89686802530（主 Blog）
- 如有 FAQ 区块，创建 FAQ schema metafield
- 验证发布内容完整性

### 第五步：发布后

- 更新 Blog 计划记忆文件，标记 #23 为已发布
- 更新图片库存清单
- 汇报文章 URL 和 ID

## 验证清单

- [ ] 文章在 `/blogs/blog/do-air-purifiers-help-cats-with-asthma` 可访问
- [ ] Title tag、meta description、featured image 齐全
- [ ] FAQ schema 正确渲染（如有 FAQ 区块）
- [ ] `%%bpc:spacer%%` 在前端渲染为产品卡
- [ ] 到 #5、#19、#7 的内链可正常跳转
- [ ] 图片 alt text 齐全且互不重复
