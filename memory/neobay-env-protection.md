---
name: neobay-env-protection
description: Neobay .env 文件必须保护，不能清空或删除内容
metadata: 
  node_type: memory
  type: project
  originSessionId: 5d8c6c30-aa98-414b-a458-be681c451fad
---

.env 文件存放 Shopify API 凭证（SHOPIFY_CLIENT_ID + SECRET + STORE_DOMAIN），所有 API 操作依赖它。**任何情况下不得清空 .env 文件内容。** token 刷新通过 `refresh_token.py` 写入新的 SHOPIFY_ADMIN_TOKEN 行即可，原有凭证行不动。
