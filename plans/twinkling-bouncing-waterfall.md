# 创建 3 个电商/DTC 专用 Skills

## Context

Robbie 是跨境电商操盘手，使用 Shopify 搭建 DTC 独立站。现有 45 个 skills 缺少：
- Shopify Liquid 模板技术层知识库
- 独立站日常运营操作手册
- 电商数据深度分析与诊断

## Skill 1: shopify-liquid

- **路径**: `~/.claude/skills/shopify-liquid/SKILL.md`
- **定位**: Shopify Liquid 模板修改的完整技术参考，不限定特定主题
- **内容要点**:
  - Liquid 语言核心：对象 `{{ }}`、标签 `{% %}`、过滤器
  - Shopify 主题目录结构：sections / snippets / templates / layout / assets / config / locales
  - JSON template 体系（Online Store 2.0+）
  - Section schema 规范和常用字段
  - 常见修改场景的代码模板：PDP、集合页、购物车、导航、页脚、自定义 page
  - 常用过滤器清单（money, url, image, string, array）
  - 常用对象：cart, product, collection, customer, shop, page, linklists
  - 常见坑点：Liquid 缓存、对象作用域、render vs include、section 重复 ID、pagination 限制
  - 调试方法：`{{ variable | json }}`、Shopify 主题检查器
  - 与 Shopify Customizer 配合的最佳实践
  - 主题修改安全规范（备份、版本管理、不影响 Customizer 可编辑性）

## Skill 2: shopify-operations

- **路径**: `~/.claude/skills/shopify-operations/SKILL.md`
- **定位**: 独立站日常运营操作执行手册，给具体可操作步骤
- **内容要点**:
  - 折扣码/自动折扣设置与常见坑
  - 运费配置（按重量/价格/条件，多仓方案）
  - 支付设置（Shopify Payments、PayPal、手动支付）
  - 税费配置
  - 库存管理策略（多 SKU、预售、缺货策略）
  - 订单处理流程与异常处理
  - 域名与 DNS 配置
  - 多语言/多货币设置
  - 常见故障排查清单
  - 运营日常检查项

## Skill 3: ecommerce-analytics（重新定位）

- **路径**: `~/.claude/skills/ecommerce-analytics/SKILL.md`
- **定位**: 不是指标字典，而是数据诊断引擎 — 给我数据，我深入分析，找出问题根因，给出优化建议
- **核心工作流**:
  1. **数据接收与结构化**: 接收用户粘贴的任意格式数据（GA4 截图、广告后台数据、Shopify 订单导出、手动输入等），自动识别数据类型和结构
  2. **异常检测**: 识别数据中的异常信号 — 哪个环节掉了、哪个指标偏离基准、趋势变化点
  3. **根因分析**: 不是停在"转化率低了"这层，而是向下追溯 — 是流量质量变了？落地页跳出率变了？加购到支付环节断了？哪个步骤在漏？
  4. **诊断报告**: 给出结构化分析结果，包含具体数字和证据链
  5. **优化建议**: 每个问题对应可执行的优化动作，按优先级排列
- **诊断维度**:
  - 流量质量诊断：渠道对比、流量结构变化、垃圾流量识别
  - 漏斗诊断：从访问 → PDP → 加购 → 结算 → 支付，逐层分析流失点和原因
  - 广告效率诊断：ROAS/MER 分析、CPC/CTR/CVR 交叉验证、广告支出与收入关系
  - 产品表现诊断：畅销品 vs 滞销品、退货率异常、客单价变化原因
  - 用户行为诊断：新客 vs 回购、AOV 变化、复购率
- **输出格式**:
  - 问题清单（按影响程度排序）
  - 每个问题：数据证据 → 可能原因 → 验证方法 → 优化建议
  - 优先级行动清单
- **避免的坑**:
  - 不要只列指标不给诊断
  - 不要给模糊建议（如"优化落地页"），要具体到"落地页的 X 环节流失率 Y%，建议做 Z"
  - 数据不足时明确说明需要什么数据，而不是硬分析
  - 区分相关性和因果性，不做无依据的归因

## 执行步骤

1. 创建 3 个目录 `~/.claude/skills/{shopify-liquid,shopify-operations,ecommerce-analytics}/`
2. 编写 SKILL.md 文件
3. 在 `.agents/skills/` 创建符号链接
4. 验证文件存在且链接可用

## 验证

- 3 个 SKILL.md 文件存在
- 符号链接可用
- 新开会话后 skill 可被触发
