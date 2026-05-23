---
name: neobay-blog
description: |
  Neobay Pet blog content creation, SEO optimization, and Shopify publishing workflow.
  Use this skill whenever the user asks to write, create, publish, or plan a blog article
  for the Neobay Pet store (neobaypet.com). Triggers include: "write a blog", "create an article",
  "publish a post", "下一篇blog", "继续写blog", "Neobay blog", "neobay content", "cat health article",
  "feline asthma blog", or any request involving Neobay content creation or publishing.
  Also use when the user says "publish" in the context of the Neobay project.
allowed-tools: [Bash, Read, Write, Edit, WebFetch, WebSearch]
---

# Neobay Blog — Creation & Publishing Skill

## Purpose

This skill encodes the complete Neobay blog workflow, from topic selection through published article.
It ensures consistent quality regardless of which model or session produces the content.

**Core principle:** Every article must meet three standards simultaneously:
- **SEO:** Captures search intent, ranks for target keywords
- **EEAT:** Demonstrates veterinary expertise, real-world experience, author authority, and trustworthiness
- **GEO:** Structured for AI-generated answers to extract and cite our content accurately

## Quick Reference

| Aspect | Rule |
|--------|------|
| Author | Always "Peter Jonathan" |
| Product handle | `neobay-cat-aerosol-chamber` |
| Product card placeholder | `%%bpc:spacer%%` |
| Store | neobaypet.myshopify.com |
| Blog API endpoint | `/admin/api/2024-01/blogs/{BLOG_ID}/articles.json` |
| API token | Auto-refreshed 24h token via `scripts/refresh_token.py` + `.env` credentials |
| Draft location | `blog-drafts/YYYY-MM-DD-slug.md` |
| Image source | LinkFox AI `@AI绘图` (Google Gemini), 1024×1024 → crop to 1200×675 |

## Workflow Overview

```
Phase 0: 竞品SERP调研(Google Autocomplete+Reddit+SERP Top5深度拆解) → 
Phase 1: 稿件撰写(EEAT+GEO标准) → 
Phase 2: 图片准备 → 
Phase 3: 发布前质检(SEO/EEAT/GEO Checklist) → 
Phase 4: 选择Blog分类 → API发布 → FAQ Schema → 
Phase 5: 发布后(内链审计+更新记忆)
```

Each phase is detailed below. Follow them in order — skipping a phase causes the bugs we've already fixed.

**Skills to invoke during this workflow:**

| Phase | Skill | Purpose |
|-------|-------|---------|
| Phase 0 | `agent-browser` | 绕过网络限制抓取 SERP/Reddit/竞品页面原始数据 |
| Phase 0 | `competitor-profiling` | Top 5 竞品文章结构化拆解，输出对比表 + Surpass Plan |
| Phase 0 | `seo-geo-content` | 关键词映射、搜索意图分析、H1-H3 大纲、FAQ 设计 |
| Phase 1 | `seo-content-writer` | 按 SEO + GEO 标准撰写稿件 |
| Phase 3 | `ai-seo` | AI 可引用性校验（LLM citation + GEO compliance） |
| Phase 3 | `seo-audit` | 技术性 on-page SEO 检查（标题、meta、结构化数据） |
| Phase 5 | `schema-markup` | FAQ Schema JSON-LD 生成与验证 |

---

## Phase 0: Pre-Writing Research (MANDATORY — do this before every article)

**Why this matters:** Keyword research alone misses the real search intent. By cross-referencing Google Autocomplete (what people actually type), Reddit (how owners talk about it), and **deep-diving the top 5 ranking articles**, we write content that doesn't just fill gaps — it **outranks** existing results on depth, structure, data, and user value.

**Goal of Phase 0:** Understand what the top 3-5 ranking articles do well, identify where they fall short, and design an article that is **objectively better** — longer, more structured, more data-backed, more EEAT-compliant, and more useful to readers. Google rewards the best answer. Our job is to build it.

**Invoke `seo-content-writer` skill during this phase** to validate SERP analysis findings and article structure design.

Three research streams, run in parallel where possible:

### 0.1 Google Autocomplete Research

Use Google's Suggest API to find real search queries around the topic:

```python
import requests

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def google_suggest(query):
    r = requests.get("https://suggestqueries.google.com/complete/search",
        params={"client": "firefox", "q": query, "hl": "en", "gl": "us"},
        headers=headers, timeout=10)
    return r.json()[1] if len(r.json()) > 1 else []

# Run these query prefixes for every topic:
# - "why is my cat [topic]"
# - "can cats [topic]"
# - "how to [topic] cat"
# - "cat [topic] when to worry"
# - "is cat [topic]"
# - "cat asthma [topic]"
# - "feline [topic]"
```

**Deliverable:** List of 10-20 real search queries, ranked by relevance. These become H2/H3 headers and FAQ questions.

### 0.2 Reddit User Discussion Research

Search Reddit for how real cat owners discuss this topic:

```python
import requests, time

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def search_reddit(query):
    r = requests.get("https://www.reddit.com/search.json",
        params={"q": query, "sort": "relevance", "t": "all", "limit": 25},
        headers=headers, timeout=15)
    posts = r.json().get("data", {}).get("children", [])
    results = []
    for post in posts:
        d = post["data"]
        results.append({
            "title": d["title"],
            "subreddit": d["subreddit"],
            "ups": d["ups"],
            "num_comments": d["num_comments"],
            "selftext": d["selftext"][:300],
            "permalink": d["permalink"]
        })
    return results

# Search at least 5 query variations:
# - "cat asthma [topic]"
# - "[topic] cat breathing"
# - "cat [topic] vet"
# - "feline [topic]"
# - The exact topic phrase as cat owners would type it
```

**What to extract from Reddit:**
- Top 5-10 user questions (these become FAQ questions)
- Common misconceptions (address these in the article body)
- Emotional pain points (use these in the intro hook)
- Trade-offs or controversies (address these for balance)
- Real owner language (mirror their vocabulary, not clinical terms)

### 0.3 Google Top 5 SERP Deep-Dive (Goal: Surpass, Not Just Analyze)

Search the target keyword on Google and perform a **deep competitive analysis** on the top 5 ranking articles. The objective is not to describe what they do — it's to identify exactly **how we will build a better article that outranks them**.

**Method:** Use WebSearch for the primary keyword, then WebFetch each of the top 5 results.

**For each top-ranking article, record with a "surpass" mindset:**

| Dimension | What to Analyze | Surpass Strategy |
|-----------|----------------|-----------------|
| **Title/H1** | What angle? What keyword? | Can we use a more compelling angle or broader keyword coverage? |
| **Structure** | How many H2s? Key Takeaways? FAQ? | Can we add sections they're missing? More granular H2/H3? |
| **Length** | Approximate word count | Can we go 1.5-2x deeper without fluff? |
| **Depth** | What sub-topics covered? What skipped? | Which missed sub-topics can we own? |
| **EEAT signals** | Vet citations? Author credentials? | Can we cite more authoritative sources? Add expert input? |
| **Data & Statistics** | What numbers? What's missing? | Can we include unique data they don't have? |
| **Visuals** | Images, tables, videos? | Can we use more structured tables? Better visuals? |
| **Product mentions** | Do they recommend? How? | Can we integrate product recommendations more naturally? |

**SERP comparison table (with surpass strategy):**

```
| Rank | URL | Title | Words | H2s | EEAT* | Strengths | Weaknesses We Can Beat |
|------|-----|-------|-------|-----|-------|-----------|------------------------|
| 1 | ... | ... | ~X | N | ⭐⭐⭐ | ... | ... |
| 2 | ... | ... | ~X | N | ⭐⭐⭐ | ... | ... |
...
*EEAT: subjective rating based on expert citations, author credentials, data quality
```

**After completing the table, write the "Surpass Plan"** — 3-5 specific dimensions where our article will be objectively better than the #1 ranking article. Each dimension must name what #1 does and how we beat it.
```

### 0.4 Surpass Strategy Decision (based on all three research streams)

Answer these before writing. The goal is **to build the best article on this topic on the internet**, not just to be different:

1. **What are the top 3 unanswered questions** from Reddit that the top 5 SERP articles don't address? → These become our exclusive content moat
2. **On which 3-5 specific dimensions** will our article be objectively better than #1? (depth, structure, data, EEAT, visual presentation)
3. **What real owner language** should we mirror in headers and FAQ? (from Reddit)
4. **What specific data/statistics** can we include that the top 5 don't have?
5. **How do we connect this topic to Neobay's product?** (Natural connection, not forced)

**Output format:** Brief Surpass Plan (half page max) covering the 5 questions above. This becomes the article brief.

### 0.5 Amazon Reviews Research (When Applicable)

For product-comparison or treatment-guide articles, Amazon reviews for AeroKat (ASIN B001B0TIBG) and similar products provide valuable competitive intel — real user complaints, praise, and questions.

**Direct scraping is blocked by Amazon's anti-bot measures.** Three options:

| Method | Cost | Effort |
|--------|------|--------|
| **Rainforest API** | ~$29/mo, free tier available | API call → structured review data |
| **Keepa API** | Free tier available | Limited review data, good for pricing |
| **Manual export** | Free | Open Amazon review page, scroll to load all, copy-paste into file |

**What to extract from reviews:**
- Common complaints (these are content opportunities)
- Questions users ask in Q&A section
- What users wish they knew before buying
- Real user language about spacer chambers

---

## Phase 1: Content Writing (the Markdown Draft)

### 1.1 Article Structure (mandatory template)

Every article follows this exact structure. Do not deviate.

```
# [H1 Title — typically a question or "How to" statement]

**Title Tag**: [50-60 chars, includes primary keyword]
**Meta Description**: [150-160 chars, includes primary keyword, compelling hook]
**URL Slug**: `/blogs/blog/[slug]`

---

## Key Takeaways
- [Bullet 1 — most critical fact]
- [Bullet 2]
- [Bullet 3]
- [Bullet 4 — typically ties to product/solution]
- [Bullet 5 — optional, for complex topics]

---

[Intro paragraph — relatable cat-owner scenario hook]

[Transition paragraph — why this matters, what the article covers]

## [H2: Main body section 1]

[Content with bold key terms, data points, and practical guidance]

### [H3 subsection as needed]

## [H2: Main body section 2]

...

%%bpc:spacer%%

## [H2: More sections as needed]

## Frequently Asked Questions

### [Question 1?]
[Answer — remove markdown links from FAQ answers for clean schema output]

### [Question 2?]
[Answer]

... [5-6 questions total]

## What to Do Next

1. [Actionable step 1]
2. [Actionable step 2]
3. [Actionable step 3]

[Final CTA paragraph with product link to /products/neobay-cat-aerosol-chamber]

Have questions? Visit our [FAQ page](/pages/faqs) or [contact us](/pages/contact) directly.

---

**Sources**:
- [Author et al. "Title." *Journal Name*, Year.]
- [Cornell Feline Health Center citation]
```

### 1.2 Writing Voice & EEAT Standards

See `references/writing-voice.md` for detailed guidelines. Key principles:

- **American English**, natural and conversational but professionally informed
- **Benefits-first**: Lead with what the cat owner gains, not product features
- **EEAT signals** in every article:
  - Experience: Real cat-owner scenarios, practical steps you can do at home
  - Expertise: Cite real veterinary journals (J Feline Medicine, J Veterinary Internal Medicine, Cornell Feline Health Center)
  - Authoritativeness: All articles by "Peter Jonathan", consistent byline
  - Trustworthiness: Balanced information, "consult your vet" disclaimers where appropriate, transparent product mentions
- **GEO optimization**: See `references/ai-geo.md` for complete AI citation guidelines. Key principles:
  - Key Takeaways at top — each bullet is a standalone, citable statement
  - FAQ section with self-contained answers — AI models cite these for voice/snippets
  - Bold key statistics with source attribution — AI preferentially cites verifiable numbers
  - Definition anchoring — bold key terms on first mention with definition
  - Descriptive H2/H3 headers — AI uses these for passage ranking
  - Entity-rich writing — mention specific drug names, brands, conditions, organizations

### 1.3 Internal Linking

Link to relevant existing content following the Topic Cluster architecture. The complete linking matrix, rules, and anchor text conventions are in `references/internal-linking.md`.

**Quick rules:**
- Every article → link to its cluster hub + 2-3 related spokes + product page
- Every article → receive links from at least 2 other articles (retroactive linking)
- Product-card articles (with `%%bpc:spacer%%`) → double inbound links
- Varied anchor text per target (rotate 2-3 variants)

**Common link targets:**

| Content Type | Link Path |
|-------------|-----------|
| Product page | `/products/neobay-cat-aerosol-chamber` |
| FAQ page | `/pages/faqs` |
| Contact page | `/pages/contact` |
| Brand Story | `/pages/brand-story` |
| Success Stories | `/pages/success-stories` |
| Why Is My Cat Coughing | `/pages/why-is-my-cat-coughing` |
| Cat cough after running | `/blogs/blog/why-does-my-cat-cough-after-running` |
| Asthma vs hairball | `/blogs/blog/feline-asthma-vs-hairball` |
| How vets diagnose asthma | `/blogs/blog/how-vets-diagnose-feline-asthma-tests-x-rays-and-what-to-expect` |
| Asthma triggers | `/blogs/blog/common-triggers-that-make-your-cats-asthma-worse` |
| AeroKat vs Neobay | `/blogs/blog/aerokat-vs-neobay-which-cat-inhaler-spacer-is-right-for-you` |
| Cat breathing fast | `/blogs/blog/why-is-my-cat-breathing-fast-while-sleeping` |
| Train cat for inhaler | `/blogs/blog/how-to-train-your-cat-to-accept-an-inhaler-mask` |
| What is a spacer | `/blogs/blog/what-is-a-cat-inhaler-spacer` |
| Inhaler stress-free | `/blogs/blog/how-to-administer-inhaled-medication-stress-free` |
| Cat wheezing | `/blogs/blog/why-is-my-cat-wheezing` |
| Feline rhinitis | `/blogs/blog/the-ultimate-guide-to-feline-rhinitis` |
| Cat owner success story | `/blogs/blog/real-cat-owner-story-managed-feline-asthma-without-daily-pills` |
| Human inhalers for cats | `/blogs/blog/can-cats-use-human-inhalers` |

**Rule:** Every article should contain 3-5 internal links to related articles. Link naturally where the reader would want to go deeper.

### 1.4 Product Card Placement

Insert `%%bpc:spacer%%` as a standalone paragraph at the natural decision point — typically after explaining the problem and before the "how to implement" section. The best placement is right after a section that establishes *why a spacer chamber is necessary*.

**Good placement examples:**
- After "The Right Way: Spacer Chamber + Face Mask" explanation
- After establishing that inhaled medication is the preferred treatment
- After a comparison that shows spacer chambers are superior

**Bad placement:**
- In the intro (too early — reader hasn't understood the need yet)
- After FAQ (too late — reader may have left already)
- In the middle of a section (breaks reading flow)

### 1.5 Selling Point Integration

When discussing cat medication delivery, naturally mention the two core differentiators:

- **Visual Flow Indicator** — use when the topic is "how do I know the medication is working?" or "uncertainty about whether my cat inhaled the medicine"
- **Comfort Feeder Design** — use when the topic is "my cat won't accept the mask" or "how to make the treatment less stressful"

Both points should emerge organically from the content, not feel bolted on.

---

## Phase 2: AI Image Generation (LinkFox `@AI绘图`)

All blog images are now generated by LinkFox AI's `@AI绘图` tool (powered by Google Gemini). No more stock photo sourcing.

### 2.1 Image Requirements

| Image | Size | Count | Source | Format |
|-------|------|-------|--------|--------|
| Featured (hero) | 1200×675 (16:9) | 1 | LinkFox `@AI绘图` → crop from 1024×1024 | WebP |
| Body illustrations | 1200×675 (16:9) | 2-3 | LinkFox `@AI绘图` → crop from 1024×1024 | WebP |

> **Why 16:9:** Blog 模板 CSS 约束为 `max-width: 1064px; max-height: 598px`（≈16:9），主内容栏 700px。封面和配图统一 16:9 与模板完全匹配，视觉一致。

### 2.2 LinkFox API Configuration

**Required environment variable:**
```bash
export LINKFOXAGENT_API_KEY=<JWT token from LinkFox dashboard>
```

**API details:**
- Base URL: `https://agent-api.linkfox.com/`
- Submit endpoint: `POST /chat/saveMessageForApi`
- Poll endpoint: `POST /chat/getMessageForApi`
- Auth header: `Authorization: <TOKEN>` (raw JWT, no "Bearer" prefix)
- Auth header: `Content-Type: application/json`

**Python requirement:** Must use Homebrew Python 3.13+ (`/opt/homebrew/bin/python3`). System Python 3.9 is too old for SSL compatibility and type hint syntax.

**Skill scripts available at:** `~/.openclaw/skills/linkfoxagent/scripts/linkfox.py`

### 2.3 Prompt Writing for Cover Images

Each cover image prompt must be tailored to the article's specific topic and core content. Write prompts in English (Gemini works best with English).

**Prompt structure:**
- Scene description matching the article's core theme
- Domestic cat (not wild/exotic), specific coat color if relevant
- Setting that fits the topic (home, vet clinic, etc.)
- Lighting and mood appropriate to the topic
- "photorealistic" for realistic photos
- "professional pet photography style" for quality look

**Example — Cat Litter article:**
```
A healthy domestic shorthair cat standing next to a clean modern litter box 
filled with natural paper-based litter, in a bright clean home bathroom, 
soft morning light from window, the cat looks calm and comfortable, 
no visible dust cloud, photorealistic, warm natural colors, 
professional pet product photography style, shallow depth of field
```

**Example — Emergency Breathing article:**
```
A caring woman gently placing her hand on a calm domestic cat's side to 
check its breathing rate, the cat is resting comfortably on a cozy sofa 
in a warm living room, soft afternoon light, the owner looks attentive 
but not panicked, photorealistic, intimate pet care moment, natural lighting
```

**What to avoid in prompts:**
- Medical devices/procedures (may trigger content filters)
- Sick or distressed cats
- Text/logos visible in the image

### 2.4 Image Generation Workflow

**Step 1: Submit generation task**
```python
import urllib.request, json

TOKEN = os.environ["LINKFOXAGENT_API_KEY"]
prompt = "@AI绘图 提示词：<your English prompt here>"

payload = json.dumps({"text": prompt}).encode()
req = urllib.request.Request(
    "https://agent-api.linkfox.com/chat/saveMessageForApi",
    data=payload, method="POST",
    headers={"Authorization": TOKEN, "Content-Type": "application/json"}
)
with urllib.request.urlopen(req, timeout=30) as resp:
    result = json.loads(resp.read())
message_id = result["messageId"]
```

**Step 2: Poll until complete (typically ~30s)**
```python
import time

for i in range(60):  # max 5 min
    time.sleep(5)
    req = urllib.request.Request(
        "https://agent-api.linkfox.com/chat/getMessageForApi",
        data=json.dumps({"id": message_id}).encode(), method="POST",
        headers={"Authorization": TOKEN, "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        result = json.loads(resp.read())
    if result.get("status") in ("finished", "error", "cancel"):
        break
```

**Step 3: Extract image URL from HTML result**
```python
import re

for r in result.get("results", []):
    if r.get("type") == "html" and r.get("content"):
        html_req = urllib.request.Request(r["content"])
        with urllib.request.urlopen(html_req, timeout=10) as resp:
            html = resp.read().decode()
        imgs = re.findall(
            r'src="(https://agent-files\.linkfox\.com/generate_image/[^"]+)"', 
            html
        )
        if imgs:
            image_url = imgs[0]  # 1024×1024 PNG
```

**Step 4: Crop to target size**
```python
from PIL import Image
from io import BytesIO

img = Image.open(BytesIO(downloaded_bytes))
if img.mode != "RGB":
    img = img.convert("RGB")

TARGET_W, TARGET_H = 1200, 675  # 16:9 cover
ratio = TARGET_W / TARGET_H

w, h = img.size
crop_h = int(w / ratio)
if crop_h > h:
    crop_w = int(h * ratio)
    crop_box = ((w - crop_w) // 2, 0, (w + crop_w) // 2, h)
else:
    crop_box = (0, (h - crop_h) // 2, w, (h + crop_h) // 2)

cropped = img.crop(crop_box).resize((TARGET_W, TARGET_H), Image.LANCZOS)
```

**Step 5: Upload to Shopify as article featured image**
```python
import base64

buf = BytesIO()
cropped.save(buf, "WEBP", quality=85)
b64 = base64.b64encode(buf.getvalue()).decode()

payload = json.dumps({
    "article": {
        "id": article_id,
        "image": {
            "attachment": b64,
            "filename": "cover.webp",
            "alt": "Descriptive alt text for SEO"
        }
    }
}).encode()

url = f"https://{domain}/admin/api/2024-01/articles/{article_id}.json"
req = urllib.request.Request(url, data=payload, method="PUT")
req.add_header("X-Shopify-Access-Token", shopify_token)
req.add_header("Content-Type", "application/json")
```

### 2.5 Image Uniqueness

Since AI generates unique images each time, duplicate images are unlikely. However:
1. Each cover prompt should describe a different scene from existing covers
2. Body images should show varied scenes (home, vet, owner interaction)
3. If a generation fails or looks wrong, re-submit with a modified prompt — each generation is unique

### 2.6 Image Alt Text

Every image must have descriptive alt text that:
- Describes what's in the image
- Includes the article's topic context
- Is 80-125 characters
- Is in English

---

## Phase 3: Pre-Publish Quality Check (MANDATORY — do not skip)

**Invoke `seo-content-writer` skill during this phase** for final EEAT/GEO validation.

Run through this checklist before every publish. Any unchecked item is a blocker.

### Structure
- [ ] Key Takeaways section present with 4-5 bullets
- [ ] Each Key Takeaway is a standalone, citable statement (GEO)
- [ ] Intro paragraph has relatable scenario hook
- [ ] All H2/H3 headers are descriptive and keyword-aware
- [ ] FAQ section has 5-6 questions with clear, self-contained answers
- [ ] What to Do Next has numbered action steps
- [ ] Sources section cites real, verifiable references
- [ ] Article ends with `---` before Sources

### SEO
- [ ] Title tag: 50-60 characters, unique, contains primary keyword
- [ ] Meta description: 150-160 characters, unique, compelling
- [ ] URL slug: kebab-case, contains primary keyword, under 80 chars
- [ ] Primary keyword in H1, first H2, and at least 2 other H2/H3 headers
- [ ] 3-5 relevant tags
- [ ] Summary HTML: one compelling sentence that makes people want to click

### EEAT
- [ ] Author set to "Peter Jonathan"
- [ ] At least 3 credible sources (veterinary journals, Cornell, academic papers)
- [ ] "Consult your vet" disclaimer where medical advice is given
- [ ] Balanced information — not purely promotional
- [ ] Key terms bolded with definitions on first mention (definition anchoring)

### GEO
- [ ] Key data points and statistics are **bolded**
- [ ] FAQ answers are self-contained (can be extracted by AI independently)
- [ ] Paragraphs are short (2-4 sentences)
- [ ] Tables used for comparison data where appropriate
- [ ] Specific entity names mentioned (drug names, brands, conditions, organizations)

### Product
- [ ] `%%bpc:spacer%%` placed at natural decision point
- [ ] Visual Flow Indicator mentioned where medication delivery certainty is discussed
- [ ] Comfort Feeder mentioned where cat acceptance/mask tolerance is discussed
- [ ] At least 3 internal links to related articles
- [ ] Product link in final CTA

### Images
- [ ] Featured image is unique (not used in any other article)
- [ ] 2-3 body images with varied scenes
- [ ] All images have descriptive alt text
- [ ] Images don't repeat each other
- [ ] Body images 1200×675 (16:9)，desktop 端受限于 max-width: 1064px / max-height: 598px，mobile 端撑满宽度

### Formatting
- [ ] H2 headings display at 32px, H3 at 24px (enforced by theme CSS)
- [ ] Body images 1200×675 (16:9)，desktop 受限于 CSS max-width: 1064px / max-height: 598px，mobile 撑满 100% 宽度

---

## Phase 4: Blog Category Selection

See `references/blog-categories.md` for the complete mapping.

**Decision flow:**
1. Does the article discuss feline asthma symptoms, diagnosis, or treatment? → **Feline Asthma** (90090766434)
2. Does it focus on cat breathing rates, breathing problems? → **Cat Breathing** (90090799202)
3. Is it a spacer/inhaler usage guide? → **Spacer Guides** (90090831970)
4. Is it a customer success story? → **Success Stories** (89726189666)
5. Is it brand or company news? → **News** (88151523426)
6. Is it a product user manual? → **User's Guide** (89675071586)
7. Everything else → **Blog** (89686802530, the main blog)

**Key rule:** Asthma-related medical articles go to Feline Asthma, not the main Blog. This was a specific correction from Robbie.

---

## Phase 5: Publishing (API Workflow)

### 4.1 Convert Markdown to HTML

Use the bundled `scripts/publish_article.py` script, which handles:

1. Parsing YAML-style metadata (title_tag, meta_description, slug) from the draft
2. **Correctly extracting body** between first `---` and last `---` separator (NOT `split('---')[-1]` — this was a critical bug)
3. Converting markdown to HTML with `markdown` library (extra extension for tables, code blocks)
4. Preserving `%%bpc:spacer%%` placeholder through conversion
5. Building the complete API payload with metafields

Manual command if script is unavailable:
```bash
python3 -c "
import markdown, re
with open('blog-drafts/FILENAME.md') as f:
    content = f.read()
parts = content.split('\n---\n')
body_md = '\n---\n'.join(parts[1:-1])  # CRITICAL: parts[1:-1], not parts[-1]
sources_md = parts[-1]
md = markdown.Markdown(extensions=['extra'])
body_html = md.convert(body_md) + md.convert(sources_md)
# Then build API payload manually
"
```

### 4.2 API Publishing Steps

Execute these steps sequentially:

**Step 0: Refresh API token (MANDATORY — do this first)**
```bash
python3 scripts/refresh_token.py
```
This exchanges the permanent Client ID + Secret in `.env` for a fresh 24h Admin API access token. Without this step, publishing will fail with 401.

**Step 1: Extract metadata from draft**
```bash
# Extract: title, title_tag, meta_description, slug, tags
python3 scripts/publish_article.py extract blog-drafts/YYYY-MM-DD-slug.md
```

**Step 2: Prepare images (LinkFox AI)**
- Write tailored prompts for featured image + 2-3 body images
- Submit to LinkFox `@AI绘图`, poll for completion
- Download 1024×1024 PNGs, crop to 1200×675 (16:9, 封面和配图统一尺寸)
- Upload to Shopify via REST API base64 attachment

**Step 3: Build and POST article**
```bash
# Token was already refreshed in Step 0 — read it from .env
SHOPIFY_ADMIN_TOKEN=$(grep SHOPIFY_ADMIN_TOKEN .env | cut -d= -f2)

python3 scripts/publish_article.py publish \
  --draft blog-drafts/YYYY-MM-DD-slug.md \
  --blog-id BLOG_ID \
  --featured-image /tmp/featured.jpg \
  --body-images /tmp/body1.jpg,/tmp/body2.jpg \
  --token $SHOPIFY_ADMIN_TOKEN
```

**Step 4: Create FAQ Schema metafield** (separate API call after article creation)
```bash
python3 scripts/publish_article.py faq-schema \
  --article-id NEW_ARTICLE_ID \
  --draft blog-drafts/YYYY-MM-DD-slug.md \
  --token $SHOPIFY_ADMIN_TOKEN
```

**Step 5: Verify the published article**
- Check all sections present in body_html
- Verify featured image is attached
- Confirm blog category is correct
- Verify FAQ schema has all items (not empty `[]`)

### 4.3 API Token & Credentials

**Token model:** Shopify Partner App uses 24h-expiring access tokens. The project uses `client_credentials` OAuth grant to auto-refresh tokens. Permanent credentials are stored in `.env`:
- `SHOPIFY_CLIENT_ID` — Partner app Client ID (permanent)
- `SHOPIFY_CLIENT_SECRET` — Partner app Client Secret (permanent)  
- `SHOPIFY_STORE_DOMAIN` — e.g. `neobaypet.myshopify.com`
- `SHOPIFY_ADMIN_TOKEN` — 24h access token (auto-refreshed by script)

**Before every publish**, run:
```bash
python3 scripts/refresh_token.py
```
This exchanges Client ID + Secret for a fresh 24h `SHOPIFY_ADMIN_TOKEN` and updates `.env` automatically. The publishing code should call `refresh_token.py` at the start of every publish flow.

- Never hardcode any token in scripts or commands
- Never commit `.env` or any credential to git or memory files
- `SHOPIFY_CLIENT_ID` and `SHOPIFY_CLIENT_SECRET` must never leave `.env`
- Token requires `write_content` + `write_files` scopes (configured in Partner Dashboard app)

---

## Phase 6: Post-Publish

### 5.1 Update Memory

After successful publishing, update `~/.claude/projects/-Users-robbieli/memory/neobay-blog-plan-may2026.md`:
1. Mark the article status as ✅ 已发布 with Article ID
2. Add to the summary table with date, title, handle, and ID
3. Update the progress count (e.g., "10/12 完成")
4. Note the blog category if not the main Blog

### 5.2 Update Image Log

Add all images used (featured + body) to `references/image-guide.md` image inventory to prevent future duplicates.

### 5.3 Notify User

Report:
- Article URL (correct blog path — e.g., `/blogs/feline-asthma/...` if in Feline Asthma blog)
- Article ID
- Blog category used
- Image count (featured + body)
- Any warnings (e.g., "body image upload failed" or "token lacks write_files scope")

---

## Known Pitfalls (Read Before Publishing)

These are bugs we've already hit and fixed. Don't repeat them.

### 1. Body extraction: `split('---')[-1]` loses the entire article
**Root cause:** Draft files have multiple `---` separators (after metadata, before sources). Using `[-1]` only captures the Sources section.
**Fix:** Use `parts[1:-1]` to get everything between first and last separator, OR use the bundled script which handles this correctly.

### 2. Markdown not converted to HTML
**Root cause:** Publishing raw markdown as `body_html`. Shopify renders it as plain text.
**Fix:** Always convert through Python `markdown` library with `extra` extension before POST.

### 3. FAQ schema has empty `mainEntity: []`
**Root cause:** FAQ extraction regex failed because the body was already truncated or HTML-converted.
**Fix:** Extract FAQ from the original markdown draft, not the HTML output. The bundled script does this.

### 4. Wrong blog category
**Root cause:** Defaulting all articles to main Blog (89686802530) without checking the category rules.
**Fix:** Use Phase 3 decision flow. Asthma articles → Feline Asthma blog.

### 5. Missing featured image
**Root cause:** Publishing without including the `image` field in the API payload.
**Fix:** Generate image via LinkFox AI, then upload via REST API base64 attachment. Always set `article.image.alt` for SEO.

### 6. LinkFox image generation fails silently
**Root cause:** Prompt contains flagged content (medical devices, drug names) that triggers content filters. Task returns `taskSuccess: false` with empty results.
**Fix:** Simplify the prompt — avoid words like "medical device", "inhaler", "mask" in close proximity to the cat. Use neutral descriptions like "small plastic accessory" or describe the scene without the sensitive object.

### 7. Horizon theme block settings invisible at runtime
This is a theme-level issue, not per-article. The workaround (hardcoded mapping in `blog-product-card-article-process.liquid`) is already in place. Just ensure `%%bpc:spacer%%` is used in article body.

### 8. Article published but template blocks not updated
Changes to `templates/article.json` require manual `shopify theme push`. Blog publishing via API does NOT push template changes. When adding new product card placeholders, remind Robbie to push the theme.

---

## Reference Files

- `references/blog-categories.md` — Complete blog category mapping with IDs and selection rules
- `references/seo-checklist.md` — Detailed SEO specifications with examples
- `references/writing-voice.md` — Writing style guide, EEAT/GEO principles, tone examples
- `references/image-guide.md` — Image sizing standards, LinkFox AI prompt examples, alt text rules
- `references/internal-linking.md` — Full Topic Cluster architecture, linking matrix, anchor text conventions
- `references/ai-geo.md` — AI Generative Engine Optimization: structural, citation, FAQ, and entity optimization

## Bundled Scripts

- `scripts/publish_article.py` — Markdown parsing, HTML conversion, API payload building, publishing
- `scripts/refresh_token.py` — Shopify Partner App 24h token auto-refresh
- `scripts/shopify_files_upload.py` — Upload images to Shopify Files (GraphQL stagedUploadsCreate)
- `~/.openclaw/skills/linkfoxagent/scripts/linkfox.py` — LinkFox AI task submission and polling (use with Python 3.13+)
