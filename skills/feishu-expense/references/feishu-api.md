# 飞书 Base API 参考

## 前置准备

需要飞书自建应用，拥有 Bitable 权限。

### 1. 创建飞书应用

1. 访问 https://open.feishu.cn → 开发者后台
2. 创建企业自建应用
3. 添加权限：`bitable:app`（多维表格）
4. 发布应用（管理员审核通过）
5. 获取 **App ID** 和 **App Secret**（凭证与基础信息页）

### 2. 配置环境变量

在 `~/.claude/settings.json` 的 `env` 中添加：

```json
{
  "env": {
    "FEISHU_APP_ID": "cli_xxxxxxxxxxxx",
    "FEISHU_APP_SECRET": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
    "FEISHU_BITABLE_APP_TOKEN": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
    "FEISHU_TABLE_ID": "tblxxxxxxxxxxxxxxx"
  }
}
```

**获取 Bitable App Token 和 Table ID**：
- App Token：打开飞书 Base，URL 中 `/base/` 后面的那串
- Table ID：打开目标数据表，URL 中 `?table=` 后面的那串

## API 接口

### 获取 Tenant Access Token

```
POST https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal
Content-Type: application/json

{
  "app_id": "xxx",
  "app_secret": "xxx"
}
```

返回：
```json
{
  "code": 0,
  "tenant_access_token": "t-xxxxx"
}
```

### 新增 Bitable 记录

```
POST https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records
Authorization: Bearer {tenant_access_token}
Content-Type: application/json

{
  "fields": {
    "金额": 29.00,
    "日期": "2026-05-15",
    "服务商": "Shopify",
    "费用名称": "Shopify Basic Plan 月费"
  }
}
```

**注意**：
- `fields` 中的 key 必须与飞书 Base 表格的列名**完全一致**（包括大小写、标点、空格）
- 如果列名与默认字段名不一致，需要先在飞书表格中确认实际列名
- 金额字段类型如果是"数字"，传数字不要加引号和货币符号

## 常见问题

### Token 过期
- Tenant access token 有效期 2 小时
- 脚本会自动获取新 token，无需手动管理

### 字段名不匹配
- 飞书 API 对字段名大小写敏感
- 建议在飞书表格中使用简洁的英文/拼音列名，然后用 `field_name` alias
- 如果写入报错 "field not found"，去飞书表格确认列名
