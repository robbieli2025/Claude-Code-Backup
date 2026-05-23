# SEO Checklist — Neobay Blog

## On-Page SEO Elements

### Title Tag (`global:title_tag` metafield)

- **Length:** 50-60 characters
- **Format:** `[Primary Keyword]: [Benefit/Context] | Neobay Pet`
- **Uniqueness:** Must be unique across all articles (Shopify enforces this)
- **Keywords:** Primary keyword near the front

**Examples:**
```
✅ "Cat Breathing Fast While Sleeping? When to Worry & What to Do"
✅ "Can Cats Use Human Inhalers? Safety, Risks & the Right Way"
✅ "Feline Asthma vs. Hairball: How to Tell the Difference"
❌ "Blog Post #10" — no keyword, too short
❌ "What Every Cat Owner Should Know About Feline Asthma, Cat Breathing Problems, and Respiratory Issues" — keyword stuffing, too long
```

### Meta Description (`global:description_tag` metafield)

- **Length:** 150-160 characters
- **Format:** Compelling hook + what reader learns + implicit CTA
- **Keywords:** Include primary and one secondary keyword naturally

**Examples:**
```
✅ "Notice your cat breathing fast while sleeping? Learn when it's normal, when it signals feline asthma, and what to do next. Vet-approved guidance for cat owners."
✅ "Wondering if your cat can use your inhaler? Learn why human inhalers are dangerous for cats without a spacer, and the safe way to deliver inhaled medication."
```

### URL Slug

- **Format:** kebab-case, under 80 characters
- **Keywords:** Primary keyword included
- **Avoid:** Stop words unless needed for readability (prefer `cat-asthma-signs` over `the-signs-of-asthma-in-your-cat`)

```
✅ can-cats-use-human-inhalers
✅ feline-asthma-vs-hairball
✅ why-is-my-cat-breathing-fast-while-sleeping
```

### Tags (`tags` field on article)

- **Count:** 3-5 tags
- **Format:** Comma-separated, lowercase
- **Strategy:** 1 primary keyword + 2-3 related topics + 1 broad category

```
feline asthma, cat inhaler, spacer chamber, inhaled medication, cat health
cat breathing, rapid breathing, feline asthma, respiratory health
```

### Author Consistency

- **Name:** "Peter Jonathan" (always, in both `author` field and `custom:author_name` metafield)
- This builds author entity authority for Google's EEAT signals

### Summary HTML (`summary_html` field)

- One compelling sentence (not a paragraph)
- Includes primary keyword
- Makes the reader want to click from the blog listing page

```
✅ "Wondering if your cat can use your inhaler? Learn why human inhalers are dangerous for cats without a spacer, and the safe way to deliver inhaled medication for feline asthma."
```

## Internal Linking Strategy

Every article must link to:
- **3-5 related articles** — natural "read more" links in context
- **Product page** — `/products/neobay-cat-aerosol-chamber` in final CTA
- **FAQ/Contact pages** — `/pages/faqs` and `/pages/contact` in the final paragraph

Full Topic Cluster architecture, linking matrix, anchor text conventions, and per-article link targets: see `references/internal-linking.md`.

## Structured Data

### Article JSON-LD
Automatically rendered by `main-blog-post.liquid`. No manual work needed — just ensure:
- Author = "Peter Jonathan"
- Featured image attached

### FAQ Schema (`seo.faq_schema` metafield)

Created as a separate API call after article publishing.

**Requirements:**
- JSON type metafield
- `@context`: `https://schema.org`
- `@type`: `FAQPage`
- `mainEntity`: Array of Question/Answer objects
- 5-6 questions minimum

**FAQ answer formatting rules:**
- Remove markdown links (use plain text)
- Self-contained answers (readable without the rest of the article)
- 2-4 sentences each

## GEO (Generative Engine Optimization)

Complete AI GEO guidelines: see `references/ai-geo.md`. Quick summary of what's covered:

1. **Structural optimization** — Key Takeaways as AI snippet bait, definition anchoring for entity recognition, semantic heading hierarchy
2. **Citation optimization** — Citation-ready statistics with source attribution, author entity strength
3. **FAQ & voice search** — Self-contained answers, conversational question phrasing
4. **Structured data** — FAQ Schema, Article Schema, comparison tables
5. **Content depth & uniqueness** — Minimum word counts by article type, entity density, unique insight per article
6. **Anti-patterns** — What makes AI deprioritize content

Per-article GEO checklist is at the bottom of `references/ai-geo.md`.
