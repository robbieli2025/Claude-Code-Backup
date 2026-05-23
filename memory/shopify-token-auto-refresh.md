---
name: shopify-token-auto-refresh
description: Shopify Partner App token 24h自动刷新标准 — 所有Shopify项目的Blog发布都用此方案
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 44c298d5-c140-4a1c-a862-ddc2b9ccd594
---

所有 Shopify 项目的 API 发布都必须使用 Client Credentials OAuth 自动刷新 token。

**Why:** Shopify 2025年后废弃了商店后台的 Custom App 永久 token，迁移到 Partner Dashboard。新版 access token 只有 24h 有效期（`expires_in: 86399`），不能手动复制后用多天。

**How to apply:** 
- 每个项目的 `.env` 存三个永久凭据：`SHOPIFY_CLIENT_ID`、`SHOPIFY_CLIENT_SECRET`、`SHOPIFY_STORE_DOMAIN`
- 项目 `scripts/refresh_token.py` 调 `POST /admin/oauth/access_token` + `grant_type=client_credentials` 换 24h token
- 发布流程 Step 0 必须跑 `python3 scripts/refresh_token.py`，后续步骤读刷新后的 `SHOPIFY_ADMIN_TOKEN`
- 适用于所有 Shopify 项目（Neobay、Hauswirt、Sumando 等），不是 Neobay 专属

**Neobay 当前凭据（2026-05-16）：**
- Client ID: `f23e4e7a8d622e4a61c9fea037294aed`
- Store domain: `neobaypet.myshopify.com`
- Token scope: `write_content, write_products, write_product_feeds, write_files, write_online_store_navigation, read_orders`
