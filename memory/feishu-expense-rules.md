---
name: feishu-expense-rules
description: 飞书费用台账录入规则：费用类别、白名单、API配置、字段映射、常见坑
metadata: 
  node_type: memory
  type: project
  originSessionId: 44c298d5-c140-4a1c-a862-ddc2b9ccd594
---

# 飞书费用台账 — 录入规则

**飞书 Base：** 📇费用台账
**Skill 路径：** `~/.claude/skills/feishu-expense/`

## Robbie 的费用类别与白名单

**AI费用**

| 服务商 | 说明 |
|--------|------|
| DeepSeek | DeepSeek API 调用费用 |
| 火山引擎 | 火山引擎 Coding Plan（含 API） |
| Cursor | AI 编程工具订阅 |
| Google One | AI 相关云存储订阅 |

**店铺订阅套餐**

| 服务商 | 说明 |
|--------|------|
| Shopify | 店铺月费/年费及附加费用 |

**规则：** 不在以上白名单的扣款不录入，除非 Robbie 明确说要加。

## 表格字段映射

| 提取信息 | 飞书字段 | 类型 | 写入格式 |
|---------|---------|------|---------|
| 服务商+费用名 | 报销摘要 | 文本 | `{服务商} - {费用名称}` |
| 金额 | 费用金额 | 数字 | 纯数字 |
| 日期 | 报销日期 | 日期 | Unix 毫秒时间戳（UTC+8） |
| 费用类别 | 报销科目 | 单选 | AI费用 / 店铺订阅套餐 |
| — | 报销进度 | 单选 | 默认「未报销」 |
| 补充信息 | 备注 | 文本 | 服务商等 |
| — | 报销人 | 人员 | Charles Li（Robbie） |

## API 配置

- **App ID：** cli_aa82f4a1d7b89cd2（费用台账录入）
- **App Token：** D1GBwCykKii3mokCApFcxcHqnHg
- **Table ID：** tbl4nlYrsvtzjLCD
- 凭证存储在 `~/.claude/settings.json` 的 `env` 中
- **必须用 batch_create 接口**（单条创建接口会 403）
- 读取接口正常，写入/字段更新需用 batch API

## Robbie 飞书身份

- 显示名：Charles Li
- open_id：ou_aa43de4d46f59e045a90a3e4b3b55008
- 邮箱：charlesli@neobaypet.com

## 团队使用

同事使用同款 skill，需各自在 `references/user-whitelists.md` 配置自己的白名单，并在 settings.json 配置各自的飞书 API 凭证。
