---
name: hauswirt-blog
description: |
  Hauswirt stand mixer blog content creation, SEO optimization, and Shopify publishing workflow.
  Use when the user asks to write, create, publish, or plan blog articles for Hauswirt.com.
  Triggers: "写blog", "写文章", "发布文章", "Hauswirt blog", "stand mixer article",
  "buying guide", "recipe post", "product comparison", "baking tips article".
  Also triggers on: "下一篇", "继续写", "发布", "publish" in Hauswirt context.
allowed-tools: [Bash, Read, Write, Edit, WebFetch, WebSearch]
---

# Hauswirt Blog — Creation & Publishing Skill

## Purpose

End-to-end blog workflow for Hauswirt.com stand mixer content. Ensures every article meets four standards simultaneously:

- **SEO:** Captures search intent, ranks for target keywords, uses proper heading hierarchy
- **EEAT:** Demonstrates baking expertise, cites authoritative sources, consistent author authority
- **GEO:** Structured for AI-generated answers (Google AI Overviews, ChatGPT, Perplexity) to extract and cite
- **Readability:** Natural, non-AI-sounding American English that passes human scrutiny

## Quick Reference

| Aspect | Value |
|--------|-------|
| Author | Always "Ethan Brooks" |
| Store | hauswirt-com.myshopify.com |
| Store URL | hauswirt.com |
| Product handles | `kitchen-stand-mixer-m5` (M5), `stand-mixer-m5max` (M5max), `m9` (M9) |
| Product card format | `[product-card:m5]` or `[product-card:m5max]` |
| Collection handle | `stand-mixer` |
| Draft location | `blog-drafts/` (HTML format) |
| Knowledge base | `_knowledge_base/` |
| Image source | User-provided; use `<!-- IMAGE_PLACEHOLDER:... -->` if unavailable |
| Featured image size | 1200×675 |
| Token refresh | `python3 scripts/refresh_token.py` before every publish |
| Publish script | `python3 scripts/publish_blog.py` |

## Blog Categories

| Blog | ID | Handle | Use For |
|------|-----|--------|---------|
| Buying Guide | 95904890973 | `buying-guide` | 选购指南、通用对比、how to choose |
| Product Comparison | 96381829213 | `product-comparison` | 品牌/型号横向对比 (X vs Y) |
| Recipes & Ideas | 96381861981 | `recipes-ideas` | 食谱、用途创意、成品展示 |
| Baking Tips | 96381894749 | `baking-tips` | 技巧、方法、故障排除 |
| Product Guides | 96381927517 | `product-guides` | 附件指南、维护、修理、清洁 |
| News | 94423318621 | `news` | 品牌动态、产品发布 |

---

## Phase 0: Pre-Writing Research (MANDATORY)

Do NOT skip research. Research prevents thin content and AI-sounding generalizations.

### 0.1 Google Autocomplete

For every topic, run at minimum these query prefixes:

```python
import requests, json

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

def google_suggest(query):
    r = requests.get("https://suggestqueries.google.com/complete/search",
        params={"client": "firefox", "q": query, "hl": "en", "gl": "us"},
        headers=headers, timeout=10)
    data = json.loads(r.text)
    return data[1] if len(data) > 1 else []

# Query prefixes for stand mixer topics:
# - "how to [topic] stand mixer"
# - "best stand mixer for [topic]"
# - "stand mixer [topic] vs"
# - "why does my stand mixer [topic]"
# - "can a stand mixer [topic]"
# - "what stand mixer [topic]"
```

**Deliverable:** 10-20 real search queries. These become H2/H3 headers and FAQ questions.

### 0.2 Reddit User Discussion Research

Target subreddits: r/Baking, r/Breaddit, r/Cooking, r/StandMixer, r/AskCulinary, r/KitchenAppliances

Extract:
- Top 5-10 user questions (→ FAQ questions)
- Common complaints about stand mixers (→ address in body as "here's how to avoid this")
- Trade language — words real bakers use, not marketing-speak
- Controversies or brand debates (→ balanced discussion)

### 0.3 SERP Top 10 Analysis

For the target keyword, analyze the top 10 Google results. Record for each:

| Dimension | What to Check |
|-----------|---------------|
| Title/H1 angle | How did they frame the topic? |
| Structure | H2 count? Key Takeaways? FAQ? |
| Depth | What sub-topics covered? What's missing? |
| Sources | Do they cite data? What sources? |
| Content gaps | What questions go unanswered? |

### 0.4 Competitive Advantage

Answer these 5 questions before writing:

1. What are the **top 3 unanswered questions** from Reddit that existing SERP articles skip?
2. What **unique angle** can Hauswirt take? (DC motor education, value vs premium, specific use cases)
3. What **real baker language** should appear in headers and FAQ?
4. What **specific data/statistics** can we include that competitors don't have?
5. How do we **connect to Hauswirt naturally**? (Not forced — only where the product solves a real problem)

---

## Phase 1: Content Writing

### 1.1 Article Structure Template

Every article follows this structure. Do not deviate without reason.

```html
<!-- IMAGE_PLACEHOLDER:featured --><!-- [Featured image: description, 1200x675] -->

<h2>Key Takeaways</h2>
<ul>
<li><strong>[Standalone fact 1 — specific, citable, makes sense without reading the article]</strong></li>
<li><strong>[Standalone fact 2 — include at least one number/statistic]</strong></li>
<li><strong>[Standalone fact 3]</strong></li>
<li><strong>[Standalone fact 4 — tie to solution/product where natural]</strong></li>
<li><strong>[Standalone fact 5 — optional, for complex topics]</strong></li>
</ul>

<hr>

<p>[Intro: relatable home baker scenario — not "In today's world..." or "When it comes to..."]</p>
<p>[Transition: what this article covers, why it matters]</p>

<h2>[H2: Body section 1]</h2>
<p>[Content...]</p>

<h3>[H3 subsection as needed]</h3>

<!-- IMAGE_PLACEHOLDER:body1 --><!-- [Body image: description, 1200x675] -->

<h2>[H2: Body section 2]</h2>
...

[product-card:m5]  <!-- or [product-card:m5max], at natural decision point -->

<h2>[H2: More sections]</h2>
...

<h2>Frequently Asked Questions</h2>

<h3>[Conversational question?]</h3>
<p>[Self-contained answer — 2-4 sentences, no "as mentioned above", no markdown links]</p>

<h3>[Conversational question?]</h3>
<p>[Self-contained answer]</p>

<!-- 5-6 questions total -->

<h2>The Bottom Line</h2>
<p>[Direct, memorable conclusion — not "in conclusion..."]</p>

<hr>

<h2>Sources</h2>
<ol>
<li>[Source description with publication, year. What the source is and why it's credible.]</li>
</ol>
```

### 1.2 Writing Voice — Anti-AI Detection Rules

**These rules are non-negotiable.** They ensure content reads as human-written by a knowledgeable baker, not generated by AI.

**Sentence variety (THE most important anti-AI signal):**
- Mix short sentences (5-8 words) with medium (12-18 words) and occasional long ones (20-25 words)
- Never use 3+ sentences of similar length in a row
- Start sentences differently — don't repeat "You can... You should... You will..."
- Use fragments sparingly for emphasis. Like this.

**Transition variety:**
- ❌ Banned transitions (AI tells): "Moreover", "Furthermore", "Nevertheless", "In conclusion", "It is worth noting that", "When it comes to", "In today's world"
- ✅ Human transitions: "Here's the thing:", "But here's what matters:", "The catch?", "This is why:", "One more thing:", "Bottom line:", direct statement with no transition

**Vocabulary rules:**
- ❌ Banned words: "elevate" (your baking), "game-changer", "revolutionize", "unleash", "culinary journey", "perfect for any kitchen", "seamless", "unparalleled"
- ✅ Replace with: specific, concrete descriptions of what happens
- Use colloquial American English: "a ton of", "way better", "pretty much", "go-to", "hands down"

**Opening paragraph rules:**
- ❌ Never: "In today's modern kitchen...", "When it comes to baking...", "For many home bakers..."
- ✅ Open with: a specific scenario, a surprising fact, a common frustration, a direct statement
- Examples of good openings:
  - "You've got flour on your counter, butter softening on the side, and a recipe that calls for 10 minutes of kneading. This is where your stand mixer either shines — or walks itself off the counter."
  - "Most stand mixer buying guides focus on bowl size and color. They skip the one spec that actually determines whether your mixer can handle bread dough."

**Paragraph rules:**
- 2-4 sentences max
- One idea per paragraph
- Vary paragraph length — don't let every paragraph be 3 sentences

**The "read-aloud" test:**
If a sentence sounds like something a human wouldn't say out loud, rewrite it. "The utilization of a DC motor facilitates superior torque delivery" → "DC motors give you more power where it counts."

### 1.3 EEAT for Kitchen Equipment Content

**Experience (first-hand):**
- Describe real baking scenarios with sensory details: "the dough will start pulling away from the sides of the bowl"
- Include practical tips that only come from actually using mixers: "you'll hear the motor pitch change when the dough is fully developed"
- Acknowledge trade-offs honestly: "yes, this mixer is heavier than it looks — you probably won't want to move it between cabinets"

**Expertise (product/technical knowledge):**
- Cite established testing labs: America's Test Kitchen, Cook's Illustrated, Wirecutter, Consumer Reports
- Reference manufacturer specs accurately: wattage, bowl capacity in quarts AND grams, RPM ranges, gearbox materials
- Use correct baking terminology: "windowpane test", "autolyse", "hydration percentage", "gluten development"
- Explain technical concepts in plain language: "Torque — that's the twisting force that keeps the hook turning when dough gets thick"

**Authoritativeness:**
- All articles by "Ethan Brooks" — consistent byline across every post
- Internal linking demonstrates systematic coverage of stand mixer topics
- Cross-reference Hauswirt's own articles where relevant

**Trustworthiness:**
- Be transparent about Hauswirt affiliation — don't pretend to be an independent reviewer
- Acknowledge when other brands do something well
- Don't make claims without evidence — every performance claim needs a spec, test, or source
- Cite sources so readers can verify independently
- If something has a downside (weight, price, learning curve), say so

### 1.4 GEO Optimization — AI Citation Layer

Integrate these directly into writing, not as an afterthought.

**Key Takeaways (AI snippet bait):**
Each bullet must be a **complete, standalone, citable statement** — AI models extract these verbatim for answer snippets:
- ✅ "DC motor stand mixers produce 60-65 dB at top speed — about the same as normal conversation."
- ❌ "DC motors are quieter." (too vague to cite)

**Definition anchoring (entity recognition):**
On first mention of any key term, **bold the term** and define it in the same sentence:
- "A **tilt-head stand mixer** has a motor housing that pivots upward on a hinge, letting you access the bowl from above."
- "**DC motors** use permanent magnets instead of electrical brushes, producing higher torque with less vibration."

**Statistics with source attribution (40% citation boost):**
Format: `[Specific number] + (Source, Year)`
- ✅ "In stress tests, DC motor mixers handled 1,500g of stiff dough for 15 minutes with no measurable speed drop (America's Test Kitchen, 2025)."
- ❌ "DC motors perform better under load."

**FAQ answers — self-contained:**
- Every answer must make sense without reading the article
- 2-4 sentences only
- No "as mentioned above", "see previous section", or markdown links
- Phrase questions conversationally: "Can a stand mixer really replace kneading by hand?" not "Stand mixer hand kneading equivalence efficacy"

**Semantic heading hierarchy:**
- One H1 (the title, set by Shopify)
- H2 for major sections — each maps to a distinct search sub-query
- H3 for subsections — no skipped levels
- Headers should read as natural questions or topics: "How Much Dough Can a Tilt-Head Actually Handle?" not "Tilt-Head Dough Capacity Specifications"

**Entity density:**
Where contextually relevant, mention recognized entities to build AI knowledge graph connections:
- Brands: KitchenAid, Cuisinart, Bosch, Hamilton Beach, Ankarsrum, Smeg
- Organizations: America's Test Kitchen, Wirecutter, NYT Cooking, King Arthur Baking
- Technical terms: wattage, torque, RPM, planetary mixing, spiral vs C-hook, all-metal gearbox

### 1.5 Internal Linking

**6 Rules (from Topic Cluster architecture):**
1. Hub articles → link to their Cluster spokes
2. Spoke articles → link back to their Hub (anchor text contains keyword)
3. Spokes ↔ Spokes: cross-link related articles within and across Clusters
4. Every article → link to at least 1 product page (PDP)
5. Product card articles (with `[product-card:...]`) → double inbound links from related content
6. New article → retroactively link from 2+ existing articles where natural

**Link targets by Cluster:**

| Cluster | Article Examples | Link Targets |
|---------|-----------------|--------------|
| A: Buying Decision | Best stand mixer, Tilt vs Bowl, Size guide | `/collections/stand-mixer`, specific PDPs |
| B: Bread & Dough | Bread recipes, Pizza dough, Sourdough | PDPs (dough capacity focus), Baking Tips blog |
| C: Attachments | Pasta press, Meat grinder, Attachment guide | `/products/kitchen-stand-mixer-m5` (attachment hub compatible) |
| D: Tips & Maintenance | Cleaning guide, Repair, Storage, Kneading tips | Product Guides blog, PDPs |
| E: Brand & Product | Hauswirt vs KA, Hauswirt vs Cuisinart, M5 review | PDPs (double link), Buying Guide blog |

**Always-available link targets:**

| Target | URL |
|--------|-----|
| Stand Mixer Collection | `/collections/stand-mixer` |
| M5 Product | `/products/kitchen-stand-mixer-m5` |
| M5max Product | `/products/stand-mixer-m5max` |
| About Page | `/pages/about` |

**Anchor text rules:**
- Rotate 2-3 variants per target (don't use the same anchor text every time)
- Use descriptive anchors: "check out our stand mixer comparison" not "click here"
- Include target keyword in anchor text where natural

### 1.6 Product Card Placement

Insert `[product-card:m5]` or `[product-card:m5max]` at the **natural decision point** — after the reader understands their need but before the final sections (FAQ, Conclusion).

**Good placement:**
- After explaining DC motor advantages → "Here's what that looks like in practice: [product-card:m5]"
- After comparing tilt-head vs bowl-lift trade-offs → product card showing the best-of-both-worlds option
- After a recipe that requires dough kneading → product card for the M5max (1,500g dough capacity)

**Bad placement:**
- In the intro (reader doesn't understand the value yet)
- After FAQ (reader already scrolled past)
- At the very end of the article only (misses opportunities)

### 1.7 Hauswirt Differentiator Integration

Weave these 3 key differentiators naturally into relevant content:

1. **DC Motor** — Mention where topic involves power, noise, stability, or dough handling. This is the #1 technical differentiator. Connect to real benefits: "won't walk off the counter", "quieter than conversation", "handles stiff dough without slowing down."

2. **Value proposition** — When discussing pricing or comparisons: "premium motor tech at a mid-range price point." Compare specs not prices: "same DC motor type found in $700+ machines, at $250-300."

3. **Modern design & usability** — Touchscreen interface, intuitive speed control, clean aesthetic. Mention where topic involves ease of use, learning curve, or kitchen integration.

**Do NOT:**
- Mention Hauswirt in every paragraph
- Use promotional language ("amazing", "incredible", "revolutionary")
- Make unverified claims about competitors

---

## Phase 2: Blog Category Selection

Decision flow:

1. Is it a brand-vs-brand comparison? → **Product Comparison** (product-comparison)
2. Is it a recipe or food idea? → **Recipes & Ideas** (recipes-ideas)
3. Is it a technique, method, or troubleshooting tip? → **Baking Tips** (baking-tips)
4. Is it about attachments, maintenance, repair, or cleaning? → **Product Guides** (product-guides)
5. Is it a purchasing guide, how to choose, or general comparison? → **Buying Guide** (buying-guide)
6. Is it brand news or product launch? → **News** (news)

---

## Phase 3: Image Preparation

### 3.1 Image Requirements

| Image | Size | Count |
|-------|------|-------|
| Featured (hero) | 1200×675 | 1 |
| Body images | 1200×675 | 2-3 |

### 3.2 Image Rules

- **No competitor brand logos or visible trademarks** — this is a legal requirement
- Each image must be visually distinct from others in the same article
- Featured image must be unique across ALL articles
- Prefer images showing: mixing mechanisms (tilt/pivot action), dough in bowl, baking scenes, kitchen counter setups
- If no suitable non-branded image is available, use `<!-- IMAGE_PLACEHOLDER:... -->` comments and let the user fill them in manually

---

## Phase 4: Publishing

### 4.1 Workflow

```bash
# Step 1: Refresh token (MANDATORY — do this first or get 401)
python3 scripts/refresh_token.py

# Step 2: Verify HTML is ready
# HTML file must be in blog-drafts/, with all IMAGE_PLACEHOLDER comments and product cards in place

# Step 3: Publish
python3 scripts/publish_blog.py blog-drafts/<filename>.html \
  --title "Article Title" \
  --handle "url-slug" \
  --tags "tag1, tag2, tag3" \
  --author "Ethan Brooks" \
  --summary "Compelling summary for blog listing..." \
  --seo-title "SEO Title (50-60 chars)" \
  --seo-description "Meta description (150-160 chars)" \
  --featured-image /path/to/featured.jpg   # optional if using placeholders

# Step 4: Verify
# Check: all sections present, author = Ethan Brooks, correct blog category, 
# SEO metafields set, images loaded
```

### 4.2 SEO Metadata Specs

| Field | Length | Rules |
|-------|--------|-------|
| Title tag | 50-60 chars | Front-load primary keyword, unique per article |
| Meta description | 150-160 chars | Include keyword naturally, compelling hook, unique |
| Handle (URL slug) | Under 80 chars | kebab-case, contains primary keyword |
| Tags | 3-5 tags | Mix of broad (Stand Mixer) and specific (DC Motor, Bread Dough) |

---

## Phase 5: Post-Publish

1. **Update memory** — Mark article status in the blog plan, record article ID and URL
2. **Report to user** — Article URL, ID, blog category, image status, any warnings
3. **Retroactive linking** — Identify 2+ existing articles where a link to the new article would be natural; suggest adding

---

## Content Quality Checklist

Run through this before every publish:

### Structure
- [ ] Key Takeaways: 4-5 standalone, citable bullets
- [ ] Intro: scenario/fact/frustration hook (not "In today's world...")
- [ ] H2/H3 hierarchy: no skipped levels, headers match search queries
- [ ] FAQ: 5-6 conversational questions, self-contained answers, no markdown links
- [ ] Sources section: minimum 3 credible sources with descriptions
- [ ] The Bottom Line: direct, memorable closing

### Anti-AI Detection
- [ ] Sentence variety: mix of short, medium, and occasional long sentences
- [ ] No banned transitions ("Moreover", "Furthermore", "In conclusion")
- [ ] No banned words ("elevate", "game-changer", "culinary journey")
- [ ] Passes read-aloud test: sounds like a human baker explaining to a friend
- [ ] Each paragraph 2-4 sentences, one idea each

### SEO
- [ ] Title tag: 50-60 chars, keyword front-loaded, unique
- [ ] Meta description: 150-160 chars, compelling, unique
- [ ] URL slug: kebab-case, contains primary keyword
- [ ] 3-5 relevant tags

### GEO
- [ ] Key statistics **bolded** with source attribution
- [ ] Key terms **bolded** and defined on first mention
- [ ] FAQ answers self-contained (AI can extract independently)
- [ ] At least 1 structured comparison element (table, list, pros/cons)
- [ ] Entity-rich: mentions brands, organizations, technical terms where natural

### EEAT
- [ ] Author = Ethan Brooks
- [ ] Minimum 3 credible sources (equipment testing labs, culinary publications, manufacturer specs)
- [ ] Balanced perspective — acknowledges trade-offs and alternatives
- [ ] Hauswirt mentioned naturally, not promotionally

### Internal Linking
- [ ] At least 1 link to a product page (PDP)
- [ ] At least 1 link to the stand mixer collection
- [ ] 2-3 links to related blog articles (cross-Cluster where possible)
- [ ] Descriptive anchor text (not "click here")

### Product
- [ ] Product card at natural decision point (not in intro, not after FAQ)
- [ ] Product mentioned in context of solving a real problem
- [ ] DC motor differentiator woven in where relevant (not forced)

### Images
- [ ] Featured image placeholder present at top of body
- [ ] 2-3 body image placeholders at natural break points
- [ ] No competitor brand logos (legal requirement)
- [ ] Each image description is unique

---

## Known Pitfalls

1. **Token expiration** — Token lasts 24h. If API returns 401, run `python3 scripts/refresh_token.py` first.
2. **Image copyright** — Never use images showing competitor brand logos. When in doubt, use placeholders.
3. **Blog category mismatch** — Don't default everything to Buying Guide. Use the Phase 2 decision flow.
4. **Product card at the very end** — The `[product-card:m5]` should be at the natural decision point, not after the Sources section or at the absolute bottom.
5. **Generic intros** — "In today's world..." and "When it comes to baking..." are dead giveaways of AI-generated content. Always open with a specific scenario, fact, or question.
6. **Forgetting SEO metafields** — The publish script handles this, but verify `title_tag` and `description_tag` are set after publishing.
7. **Internal link count** — If you mention a topic that has an existing article, link to it. Don't make the reader search.

---

## Reference Files

- `_knowledge_base/research-stand-mixer-topics-20260517.md` — Full 3-channel content research (Reddit/YouTube/Google SERP)
- `_knowledge_base/blog-tilt-head-vs-bowl-lift-stand-mixer.md` — Example article following this skill's standards
- `scripts/refresh_token.py` — Shopify token auto-refresh (client_credentials grant, 24h expiry)
- `scripts/publish_blog.py` — Article publishing script (HTML→Shopify API, SEO metafields, image upload)
- Memory: `hauswirt-content-research` — 5 Topic Clusters, content differentiation strategy
- Memory: `hauswirt-keyword-analysis` — 451-keyword analysis, 2-month blog plan
