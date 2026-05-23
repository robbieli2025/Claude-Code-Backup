---
name: shopify-operations
description: Shopify 独立站日常运营操作执行手册。当用户需要设置折扣/优惠、配置运费、调整支付方式、管理库存、处理订单、配置域名、设置多语言多货币、排查运营故障，或任何 Shopify 后台操作相关的工作时使用此 skill。即使用户只是说"帮我设个折扣码"或"运费怎么配"，也应该触发此 skill。
---

# Shopify 独立站运营操作手册

本 skill 覆盖 Shopify 后台日常运营操作的完整指南，每个操作包含具体步骤、常见坑点和最佳实践。

## 折扣与优惠

### 折扣码（Discount Codes）

**路径**: Discounts → Create discount → Discount code

**设置步骤**:
1. 输入折扣码名称（如 `SUMMER20`）或点 Generate 生成随机码
2. 选择类型：
   - Percentage（百分比折扣）
   - Fixed amount（固定金额折扣）
   - Free shipping（免运费）
   - Buy X get Y（买X送Y/打折）
3. 设置值（如 20% off）
4. 设置适用范围：All products / Specific collections / Specific products
5. 设置最低购买条件（Minimum requirements）：无 / 最低金额 / 最低数量
6. 设置客户资格：Everyone / Specific customer segments / Customer login required
7. 设置使用限制：总使用次数 / 每人使用次数
8. 设置有效期：Start date / End date
9. 可设置 Combinable（是否可与其他折扣叠加）

**常见坑点**:
- 折扣码不能和自动折扣同类型叠加，除非设为 Combinable
- Free shipping 折扣码的免运费范围受运费方案限制（只免你设置的运费方案部分）
- Buy X get Y 中"Get Y"的折扣是针对 Y 产品的，不要搞反
- 设置最低金额时，金额不含税和运费（取决于设置）
- 折扣码大小写不敏感，但建议用大写便于识别
- 过期的折扣码不会自动删除，定期清理避免列表混乱

### 自动折扣（Automatic Discounts）

**路径**: Discounts → Create discount → Automatic discount

**与折扣码的区别**:
- 自动折扣不需要客户输入代码，购物车自动应用
- 一个时间段只能有一个自动折扣生效
- 优先级高于折扣码（如果允许叠加）

**常见组合策略**:
- 自动折扣做全站基础活动（如全场 9 折）
- 折扣码做特定渠道加码（如 KOL 专属额外 85 折）
- 设置 Combinable 让两者叠加

### 买赠（Buy X Get Y）

**关键设置**:
- Customer buys: 设置 X 的数量或金额
- Customer gets: 设置 Y 的产品和折扣力度
- Y 产品可以是特定产品或特定集合
- 最低购买量设置避免被薅

**坑点**:
- Buy X get Y 的"Y"需要客户自己添加到购物车，折扣才会自动应用（部分场景）。用自动折扣而非折扣码可改善体验
- 设置"Any items from"集合时，X 和 Y 可能是同一产品，注意限制

## 运费配置

**路径**: Settings → Shipping and delivery

### 运费方案结构

```
Shipping profile
├── General rates（通用运费规则）
│   ├── Domestic（国内）
│   │   ├── Standard: $5.00 (3-5 days)
│   │   └── Express: $15.00 (1-2 days)
│   └── International（国际）
│       ├── Standard: $15.00 (7-14 days)
│       └── Express: $35.00 (3-5 days)
└── Custom rates for specific products/collections
    ├── Heavy items collection
    │   └── Standard: $25.00
    └── Free shipping collection
        └── Free standard shipping
```

### 运费类型

1. **Flat rate**: 固定运费
2. **Calculated rate**: 基于 USPS/UPS/DHL 等承运商实时计算
3. **Free shipping**: 免运费（可设最低金额条件）
4. **Price-based rates**: 按订单金额区间定价（如 $0-50 运费 $10，$50+ 运费 $5）
5. **Weight-based rates**: 按重量区间定价

### 跨境电商运费配置建议

1. 设立通用国际运费方案，覆盖所有目标市场
2. 对高价值市场（如美国/欧洲）单独配置运费
3. 设置免运费门槛（如 $50+ 免运费），提升客单价
4. 产品重量必须准确填写，影响运费计算
5. 考虑使用 Shopify Shipping 获得承运商折扣费率

**常见坑点**:
- 未设置运费的国家/地区客户无法下单，除非开启"All remaining countries"
- 运费方案中"Free shipping"不会自动免运费，需要在运费规则中添加 Free shipping 选项
- 产品未分配到运费方案时，使用 General rates
- 多个运费方案时，同一产品只能属于一个方案
- Calculated rates 需要输入产品准确尺寸和重量，否则报价不准确
- 不要依赖"Free shipping"折扣码替代运费方案设置，客户看到"计算运费"时可能已放弃

## 支付设置

**路径**: Settings → Payments

### 支付方式对比

| 支付方式 | 优点 | 缺点 | 适合场景 |
|----------|------|------|----------|
| Shopify Payments | 无额外月费、手续费最低、支持加速结账 | 仅特定国家可用 | 首选支付方式 |
| PayPal Express | 客户信任度高、全球通用 | 手续费高、提现有延迟 | 必备补充 |
| Apple Pay / Google Pay | 结账快、转化率高 | 需要 Shopify Payments | 所有站点 |
| Shop Pay | 一键结账、转化率最高 | 仅 Shopify 生态 | 所有站点 |
| 手动支付(Bank Deposit) | 无手续费 | 需手动确认订单 | 特定市场 |
| 第三方网关(Stripe等) | 灵活 | 额外月费+高手续费 | Shopify Payments 不可用时 |

### 支付设置关键点

1. **优先启用 Shopify Payments**：手续费最低，支持 Shop Pay / Apple Pay / Google Pay
2. **PayPal 必须启用**：部分客户只用 PayPal
3. **Express checkout 顺序**：Shop Pay > Apple Pay > Google Pay > PayPal
4. **货币**：Shopify Payments 支持多币种收款（需 Shopify Plus 或 Advanced 方案）
5. **支付授权**：选择"Automatically"（自动捕获）或"Manually"（手动捕获）

**常见坑点**:
- Shopify Payments 和第三方支付网关不能同时启用部分功能
- PayPal 需要单独配置 Business 账户，Personal 账户无法用于收款
- 手动支付方式需在订单页面手动确认，否则库存不会释放
- 退款时 Shopify 不退还交易手续费
- 测试支付时使用 Shopify Bogus Gateway 测试模式

## 税费配置

**路径**: Settings → Taxes and duties

### 关键设置

1. **自动税费计算**: Shopify 根据发货地和收货地自动计算税率
2. **税费包含在价格中**: 决定显示价格是否含税（各国要求不同）
3. **运费税费**: 运费是否收税
4. **免税产品**: 部分产品类别免税（如服装、食品），需手动设置

### 跨境税费要点

- 欧洲销售需注册 VAT，设置 OSS (One Stop Shop) 简化申报
- 美国各州税率不同，Shopify 自动计算但不代收代缴（除 Marketplace Facilitator 州）
- 英国脱欧后需独立处理 VAT
- 加拿大有 GST/HST/PST 差异
- 澳大利亚 GST 门槛 $1,000
- 使用 Shopify Tax（如可用）自动处理税费计算和申报

**常见坑点**:
- 不要手动覆盖自动税率，容易出错
- 确保产品正确设置了 HS code（海关编码），影响税费和关税计算
- B2B 客户可能需要免税，设置客户免税标签
- 退款时不自动退回税费，需手动处理

## 库存管理

**路径**: Products → [选择产品] → Inventory

### 库存策略

1. **Shopify 追踪库存**: 启用"Track quantity"自动追踪
2. **多仓库管理**: 使用 Inventory locations 管理不同仓库
3. **低库存预警**: 设置"Continue selling when out of stock"或设为不卖
4. **库存转移**: Location 间调拨库存

### 缺货处理选项

| 策略 | 设置 | 适合场景 |
|------|------|----------|
| 停止销售 | 取消勾选"Continue selling..." | 热销品、不可补货 |
| 继续销售 | 勾选"Continue selling..." | 可快速补货、预售 |
| 预售模式 | 勾选 + 产品页标注发货时间 | 新品预热、爆品预售 |

**常见坑点**:
- 多渠道销售时库存共享，一个渠道卖完其他渠道也显示缺货
- 取消订单后库存自动恢复，退货需手动恢复
- variant 级别的库存独立管理，不要只管理产品级别
- 导入 CSV 更新库存时，用"Overwrite"会覆盖现有数据，用"Add"会累加

## 订单处理

### 订单状态流转

```
Pending → Authorized → Paid → Fulfilled → Delivered
                                    ↓
                               Partially Fulfilled
                                    ↓
                               Refunded / Returned
```

### 日常订单处理流程

1. 检查新订单（标记可疑订单 — 大额、多件、不同收发货地址）
2. 确认库存
3. 处理支付（如手动捕获）
4. 添加发货追踪号
5. 标记 Fulfilled
6. 处理客户邮件

### 异常订单处理

| 异常类型 | 判断信号 | 处理方式 |
|----------|----------|----------|
| 欺诈风险 | Shopify 风险分析标记、不同收发货地址、大额订单 | 取消或手动审核 |
| 支付失败 | Pending 超过授权期 | 联系客户或取消 |
| 地址无效 | 物流退回 | 联系客户更正后重发 |
| 退款请求 | 客户发起 | 按退款政策处理 |
| 部分退款 | 只退部分商品 | 退款指定商品金额 |
| 换货 | 客户要求 | 退款后重新下单或手动创建新订单 |

### 退款处理注意事项

- 退款方式：原路退回（默认）或 Store Credit
- 部分退款：只退商品金额，不含运费（除非全退）
- 退回库存：退款时选择"Restock items"
- 退款手续费不退：Shopify 和支付网关的手续费不退还
- 取消订单 vs 退款：未发货的可以取消（Cancel），已发货的用退款（Refund）

## 域名与 DNS

**路径**: Settings → Domains

### 域名配置步骤

1. **连接已有域名**: Settings → Domains → Connect existing domain
2. **修改 DNS 记录**:
   - A Record → `23.227.38.65`
   - CNAME → `www` → `shops.myshopify.com`
3. **等待 DNS 传播**（最多 48 小时，通常几分钟）
4. **验证连接**: Shopify 显示"Connected"

### 子域名和多店

- 一个 Shopify 店可以绑定多个域名
- 主域名设置在 Settings → Domains → Set as primary
- 不同域名可以对应不同市场（需 Shopify Plus 用域名做市场路由）

**常见坑点**:
- DNS 修改后需要等传播时间，不要反复修改
- 切换域名时确保旧域名做了 301 重定向
- 邮箱 MX 记录不要指向 Shopify，保持原 DNS 的 MX 记录
- SSL 证书自动生成，DNS 正确后等待即可，不要手动配置

## 多语言与多货币

### 多语言设置

**路径**: Settings → Languages

1. 启用 Shopify Markets
2. 添加目标市场语言
3. 翻译内容：使用 Shopify Translate & Adapt 或第三方翻译 App
4. 语言切换器会自动出现在页头

### 多货币设置

**路径**: Settings → Markets

1. 添加目标市场
2. 启用当地货币
3. 设置汇率转换方式：自动（Shopify 汇率）或手动
4. 设置四舍五入规则（减少零头金额）

**常见坑点**:
- 多货币结算时，Shopify 以店铺基础货币结算
- 汇率转换可能造成金额偏差，设置 rounding 规则
- 翻译不完整时，缺失部分会回退到默认语言
- 不是所有主题都完整支持多语言，检查主题的语言兼容性
- 产品 URL 会带语言前缀（如 `/en/products/...`、`/zh/products/...`），影响 SEO

## 常见故障排查清单

| 问题 | 可能原因 | 排查步骤 |
|------|----------|----------|
| 客户无法下单 | 运费未覆盖该地区 | 检查 Shipping 设置中是否有该国家/地区 |
| 折扣码无效 | 已过期/使用次数用尽/条件不满足 | 检查折扣码状态和条件设置 |
| 支付方式不显示 | 支付网关未启用/国家限制 | 检查 Payments 设置和国家可用性 |
| 产品页显示缺货 | 库存为 0/未勾选继续销售 | 检查库存数量和缺货设置 |
| 运费显示异常 | 产品重量/尺寸未填/运费规则冲突 | 检查产品重量和运费方案 |
| 域名无法访问 | DNS 未正确指向/SSL 未就绪 | 检查 DNS 记录和 SSL 状态 |
| 订单未捕获支付 | 设为手动捕获/授权过期 | 检查支付授权状态 |
| 邮件通知未发送 | 邮件模板被禁用/发件邮箱问题 | 检查 Notifications 设置 |
| 购物车异常 | JS 错误/App 冲突/缓存问题 | 检查浏览器控制台和 App 冲突 |
| 网站速度慢 | 图片过大/App 过多/主题代码冗余 | 检查 PageSpeed、禁用不必要 App |

## 运营日常检查项

### 每日
- [ ] 检查新订单，处理异常订单
- [ ] 检查库存预警
- [ ] 回复客户咨询
- [ ] 监控支付失败率

### 每周
- [ ] 审查折扣码使用情况，清理过期折扣
- [ ] 检查退款率和退款原因
- [ ] 审查运费方案是否需要调整
- [ ] 检查 App 运行状态和费用

### 每月
- [ ] 审查税费设置和申报
- [ ] 检查域名和 SSL 状态
- [ ] 审查库存周转率，清理滞销品
- [ ] 检查支付方式费率是否需要优化
- [ ] 备份主题和关键数据

## Related Skills

- **shopify-liquid** — Shopify Liquid 模板修改技术
- **ecommerce-analytics** — 电商数据分析诊断
- **page-cro** — 页面转化率优化
- **pricing-strategy** — 定价策略
