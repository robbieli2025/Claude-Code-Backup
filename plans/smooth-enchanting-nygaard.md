# Blog 图片工作流统一 — Shopify Files 上传方案

## 问题

两个项目的 Blog 图片处理方式混乱，导致 blog HTML 中出现"隐藏图床"：

### Neobay 现状
- 封面图：base64 编码在 `article.image.attachment`（导致 API 请求体巨大）
- 正文图片：部分 base64 data URI 嵌入 HTML、部分硬编码 CDN URL、部分用 loremflickr 外链
- image-guide.md 文档两种方式并存，标注 base64 为"current state"

### Hauswirt 现状
- 封面图：base64 编码在 `article.image.attachment`
- 正文图片：`publish_blog.py` 硬编码了 3 个 Unsplash CDN URL，每篇文章都用一样的图
- 图片跟文章内容完全无关

### Robbie 要求
1. 从 Unsplash/Pexels 下载图片
2. 上传到 Shopify Files（通过 API）
3. 用 Shopify 返回的 CDN URL 插入 blog 正文和封面
4. 不用 base64 嵌入、不用外部 CDN 直链

## 技术方案

### Shopify Files 上传流程

使用 GraphQL `stagedUploadsCreate` mutation：

```
1. 调用 stagedUploadsCreate 获取临时上传 URL
2. HTTP PUT 图片到临时 URL
3. Shopify 自动将文件存入 Files，返回永久 CDN URL
4. 用 CDN URL 设置封面图(article.image.src) 和正文 <img> 标签
```

### 前提条件

**API token 需要 `write_files` scope。** 两个项目的 token 目前只有 `write_content`，需要 Robbie 在 Shopify Partner Dashboard 给两个 App 各添加 `write_files` scope。

## 修改清单

### 1. 新建：`Hauswirt.com/scripts/shopify_files_upload.py`
- 封装 `stagedUploadsCreate` GraphQL mutation
- 输入：本地图片路径
- 输出：Shopify CDN URL
- 两个项目通用（通过 .env 区分 store）

### 2. 修改：`Hauswirt.com/scripts/publish_blog.py`
- 删除硬编码的 3 个 Unsplash URL（第 153-155 行）
- 删除 `replace_image_comment()` 函数里面的 Unsplash URL 映射逻辑
- 改为：接受 `--body-images` 参数 → 调 `shopify_files_upload.py` 上传 → 用 Shopify CDN URL 替换 `<!-- IMAGE: ... -->` placeholder
- 封面图：改为传 Shopify CDN URL 给 `article.image.src`（而非 base64 attachment）

### 3. 修改：`Neobay` 项目
- `neobay-blog/references/image-guide.md`：删除 base64 方案，只保留 Shopify Files 方案
- `neobay-blog/SKILL.md` Phase 2：更新图片上传步骤为 Shopify Files 流程
- 后续新文章严格按新流程执行

### 4. 修改：两个项目的 `CLAUDE.md`
- 更新图片处理 Phase 的描述，指向新的上传流程
- 标注 token 需要 `write_files` scope

## 不改的
- 已发布的旧文章（base64 图片已经在 Shopify 服务器上，改的成本大于收益）
- Neobay 的 `publish_article.py`（该文件不存在，Neobay 文章通过命令行直接调 API 发布）

## 验证方式

1. 下载一张 Unsplash 测试图片
2. 运行 `python3 scripts/shopify_files_upload.py --file /tmp/test.jpg` → 得到 CDN URL
3. 浏览器打开 CDN URL → 确认图片可以访问
4. 用新流程发布一篇测试文章 → 确认正文图片和封面图来自 Shopify CDN
5. 检查 body_html 没有 `data:image` 或 `base64` 残留

## 前置依赖

- Robbie 在 Shopify Partner Dashboard 给两个 App 添加 `write_files` scope
- 两个项目的 `.env` 都有完整的 credentials（Neobay 的 .env 当前缺少凭证）
