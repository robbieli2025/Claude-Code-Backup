---
name: feedback-featured-image-unique
description: Blog 文章封面图必须唯一，不能与任何已有文章的封面图或内嵌图片重复
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a1b01dce-60cf-4ef7-901a-56021d369576
---

每篇 Blog 文章的封面图（featured image）必须是全新图片，不能与以下任何图片重复：
1. 其他文章的封面图
2. 同一文章的 body 内嵌图片
3. 其他文章的 body 内嵌图片

**Why:** 之前出现过3处重复——Cat Cough After Running 和 AeroKat vs Neobay 共用同一张封面图；Asthma vs Hairball 和 Train Cat Inhaler Mask 的封面图与自身 body 内嵌图相同。Robbie 要求所有封面图必须独特，不能"用过"。

**How to apply:** 发布新文章前，必须用新下载的图片作为封面图（不能复用 Unsplash 同一 photo ID）。上传封面图后，用 MD5 hash 对比全站所有图片（featured + body），确认无重复后再发布。同时检查 body 内嵌图片是否与封面图重复。
