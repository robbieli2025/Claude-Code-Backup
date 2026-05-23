# Stand Mixer 关键词全面分析与 Blog 规划方案

## 背景

Hauswirt.com 现有的 SEO 内容极其薄弱：
- **0 篇 Blog 文章**
- M9 产品页使用占位模板，无自定义内容
- Stand mixer collection 页只有 banner + product grid，无 SEO 文字
- 品牌词 "hauswirt stand mixer" 仅 200 月搜索量
- 没有对比内容、附件指南、食谱内容、购买指南等高价值 SEO 内容
- "best stand mixer" (4900)、"stand mixer attachments" (1300)、"stand mixer pasta press" (5600) 等高流量关键词完全未部署

451 个匹配关键词，需要：
1. 去重（确认无重复）
2. 为每个关键词标注是否已部署、部署位置、URL
3. 对已部署的诊断是否科学
4. 对未部署的规划 2 个月 Blog 计划（M1: 10篇，M2: 15篇）
5. 输出统一表格

## 执行方式

用 Python 脚本处理 CSV，结合我手动分析的现有页面映射，输出最终 CSV 文件。

## 已有页面与关键词映射

### 已部署的关键词映射

| 页面类型 | URL | 已覆盖的关键词主题 |
|---------|-----|------------------|
| 首页 | `/` | stand mixer, home multi-functional stand mixer |
| Stand Mixer 合集页 | `/collections/stand-mixer` | stand mixer collection (弱) |
| M5 产品页 | `/products/kitchen-stand-mixer-m5` | kitchen stand mixer, touchscreen stand mixer, DC motor stand mixer, 5L stand mixer, stand mixer for family cooking, 11-speed stand mixer, stand mixer with attachments |
| M5max 产品页 | `/products/stand-mixer-m5max` | silent stand mixer, cast aluminum stand mixer, stand mixer for dough (1500g), 800W stand mixer, all-metal gearbox stand mixer, DC motor stand mixer, multi-functional stand mixer |
| M9 产品页 | `/products/m9` | home multi-functional stand mixer (弱 - 模板为空) |
| About 页面 | `/pages/about` | stand mixer brand (弱) |

## 输出文件

`/Users/robbieli/Downloads/hauswirt-stand-mixer-keyword-analysis.csv`

## 输出结构

CSV 列：
A. Keyword
B. Volume (US)
C. Difficulty
D. Category
E. Intent
F. 是否已布局 (已布局/未布局)
G. 页面类型 (产品页/合集页/首页/Blog文章/信息页)
H. 页面URL
I. 布局诊断 (已布局→是否科学+问题；未布局→"-")
J. 优化建议 (已布局且不科学→具体建议；未布局→"-")
K. Blog规划月份 (Month 1/Month 2/-)
L. 建议Blog标题
M. 优先级 (P0/P1/P2/P3)

## Blog 规划策略

### Month 1 (10篇) — 优先高流量 + 低难度关键词

优先级排序：Volume × (1/Difficulty) 的前10个非品牌关键词
覆盖方向：
1. Best stand mixer 类 (1篇) — "Best Stand Mixer 2026: Complete Buying Guide"
2. 附件指南 (2篇) — "Stand Mixer Attachments Guide: From Pasta to Meat Grinder", "Stand Mixer Paddle Attachment: What It Is and How to Use It"
3. 食谱/用途 (3篇) — "Easy Stand Mixer Bread Recipes", "How to Make Pizza Dough in a Stand Mixer", "Stand Mixer Recipes for Beginners"
4. 对比评测 (2篇) — "Hauswirt M5 vs KitchenAid: Which Stand Mixer Is Right for You?", "Tilt Head vs Bowl Lift Stand Mixer: Pros and Cons"
5. 选购指南 (2篇) — "How to Choose a Stand Mixer", "Best Affordable Stand Mixer Under $300"

### Month 2 (15篇) — 覆盖长尾 + 更高难度关键词

延伸方向：
1. 食谱类 (4篇) — sourdough, mashed potatoes, butter, pie crust
2. 附件详解 (3篇) — dough hook, meat grinder attachment, pasta attachment
3. 对比类 (2篇) — Hauswirt vs Cuisinart, Hauswirt vs Bosch
4. 使用技巧 (3篇) — how to knead dough, how to shred chicken, stand mixer storage
5. 维护保养 (2篇) — stand mixer repair guide, stand mixer cleaning and maintenance
6. 选购延伸 (1篇) — stand mixer sizes comparison

## 验证方式

1. 打开输出的 CSV 文件确认：
   - 451 行数据全部保留（无丢失）
   - 每行都有部署状态标注
   - 已部署的有 URL 和诊断
   - 未部署的有 Blog 规划
2. Blog 计划表完整性：
   - Month 1 有 10 篇
   - Month 2 有 15 篇
   - 每篇有关键词覆盖、优先级和难度参考
