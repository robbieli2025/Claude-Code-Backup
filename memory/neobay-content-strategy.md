---
name: neobay-content-strategy
description: Neobay Blog 全盘内容战略：5大Topic Cluster架构、内链策略、AI GEO原则、竞品差异化
metadata: 
  node_type: memory
  type: project
  originSessionId: b98695c4-2567-4646-9ca7-bc4619fb5263
---

# Neobay Blog 全盘内容战略

制定日期：2026-05-13，基于 TrudellAnimalHealth 811 个去重关键词的缺口分析。

> **2026-05-16 更新：** 具体选题排期已移至 [[neobay-blog-plan-jun-nov-2026]]（6-11月50篇新规划，整合 Reddit+Google+YouTube+Amazon 全渠道调研）。本文件保留战略框架、Topic Cluster 架构、内链规则、AI GEO 原则。

## 战略目标

通过系统化内容矩阵覆盖"猫呼吸道健康"领域的全部搜索意图，建立 EEAT 权威性，将所有信息流量导向产品转化。

核心逻辑：**猫出现呼吸道症状 → 搜索 → Neobay 文章诊断/解释 → 如果是哮喘 → Neobay 间隔器解决。**

## 5 大 Topic Cluster

```
Cluster A: Feline Asthma Core（猫哮喘核心）
  Hub: How Vets Diagnose Feline Asthma (#4)
  Spokes: Triggers (#5), Asthma vs Hairball (#2), Cat Flu vs Asthma (#11), Steroids (#18)

Cluster B: Cat Breathing Symptoms（呼吸症状识别）
  Hub: Why Is My Cat Wheezing? (page)
  Spokes: Cough After Running (#1), Breathing Fast Sleeping (#7), Gasping (#16), Human Inhalers (#10)

Cluster C: Inhaler Spacer Treatment（间隔器治疗）
  Hub: What Is a Cat Inhaler Spacer (#3)
  Spokes: Train Cat for Mask (#8), AeroKat vs Neobay (#6), Spacer Not Working (#12), Administer Medication (早期)

Cluster D: General Cat Respiratory Health（猫呼吸健康综合）
  Hub: Cat Cold & URI Guide (#15)
  Spokes: Hairballs (#17), Rhinitis (早期), Pneumonia (#31), Cross-Species (#61)

Cluster E: Product Decision（购买决策 — 终点）
  Hub: 产品页 /products/neobay-cat-aerosol-chamber
  Spokes: AeroKat vs Neobay (#6), Success Story (#9), Spacer Not Working (#12), Cost Guide (#21)
```

注：括号内编号对应 [[neobay-blog-plan-jun-nov-2026]] 中的选题编号。

## 内链策略（6 条规则）

详见 skill reference `references/internal-linking.md`。核心规则：

1. **Hub → Spokes**：每个 Cluster Hub 链出到所有同 Cluster Spokes
2. **Spokes → Hub**：Spoke 链回 Hub，锚文本包含 Hub 核心关键词
3. **Spokes ↔ Spokes**：同 Cluster 内 Spoke 交叉互联
4. **跨 Cluster 桥接**：在内容自然转折点跨 Cluster 链接（如症状 → 治疗）
5. **每篇 → 产品页**：每篇文章至少 1 次链接到 `/products/neobay-cat-aerosol-chamber`
6. **产品卡文章获双倍内链**：含 `%%bpc:spacer%%` 的文章至少有 2 篇其他文章链向它

锚文本：多样化、描述性、自然包含关键词（不堆砌）。

## AI GEO 优化原则

详见 skill reference `references/ai-geo.md`。6 条核心摘要：

1. **Key Takeaways 作为 AI 片段诱饵** — 每条独立可被提取为 AI 答案
2. **定义锚定** — 首次出现的术语加粗 + 定义，利于 AI 实体识别
3. **可引用的统计数据** — 每条数据附来源，AI 优先引用可验证的数字
4. **自包含 FAQ 答案** — 每条答案可不看上下文独立理解
5. **结构化对比数据** — 对比场景用 HTML 表格，AI 解析优于纯文本
6. **实体密度** — 提及具体药名、品牌名、机构名，这些是 AI 知识图谱节点

## 竞品内容盲区（我们的差异化空间）

TrudellAnimalHealth 只覆盖 asthma、偏临床、不做产品问题/鉴别诊断/steroid alternative 内容。我们的差异化：
- 更广疾病覆盖（URI、cold、flu、hairballs、cross-species）
- 猫主人视角（非临床），贴近搜索意图
- 客观对比内容（spacer not working、when to replace）
- 鉴别诊断（flu vs asthma、hairball vs asthma、bronchitis vs asthma）
- Steroid alternative 叙事 — Neobay 最强产品论据
- 费用透明 + 情绪支持 — Reddit 验证的零竞品内容空白

## 与相关文档的关系

| 文档 | 层级 | 内容 |
|------|------|------|
| 本篇 | 战略层 | 做什么、为什么、架构是什么 |
| [[neobay-blog-plan-jun-nov-2026]] | 规划层 | 50篇选题、月度排期、发布日历 |
| [[neobay-blog-plan-may2026]] | 历史记录 | 5月12篇执行进度 |
| `references/internal-linking.md` | 执行层 | 每篇文章具体内链方案 |
| `references/ai-geo.md` | 执行层 | 每篇文章 GEO 写作规范 |
| `neobay-blog` SKILL.md | 流程层 | 怎么写、怎么发布 |
