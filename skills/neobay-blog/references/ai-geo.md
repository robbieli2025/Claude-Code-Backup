# AI GEO (Generative Engine Optimization) — Neobay Blog

## What This Is

AI GEO ensures our content is preferentially cited, referenced, and surfaced by AI systems: Google AI Overviews, ChatGPT, Claude, Perplexity, Bing Copilot, and voice assistants (Siri, Alexa, Google Assistant).

**The principle:** AI models don't "rank" content like search engines do. They extract, synthesize, and cite. Our job is to make our content the easiest and most trustworthy thing for them to extract.

---

## Layer 1: Structural Optimization (AI Parsing)

### 1.1 Key Takeaways as AI Snippet Bait

The "Key Takeaways" section at the top of every article serves a dual purpose:
- **Human reader**: Quick scan to decide if the article answers their question
- **AI model**: Pre-extracted, self-contained factual statements ready for citation

**Rules for Key Takeaways:**
- Each bullet is a **complete, standalone statement** (makes sense without reading the article)
- Include the **primary keyword** in at least 2 bullets
- Include **at least 1 specific number or statistic**
- Include **at least 1 bullet that ties to the solution** (spacer/product angle)

**Example:**
```markdown
## Key Takeaways
- **Feline asthma affects approximately 1-5% of all cats**, making it one of the most common respiratory diseases in felines.
- **Cat flu and feline asthma share overlapping symptoms** — coughing, wheezing, and labored breathing can indicate either condition.
- **A veterinarian diagnosis is essential** because cat flu is temporary while asthma requires lifelong management.
- **Inhaled medication delivered through a spacer chamber** is the gold-standard treatment for feline asthma, with fewer side effects than oral steroids.
- **Never use a human inhaler on a cat without a veterinary-prescribed spacer chamber** — it can be ineffective or dangerous.
```

### 1.2 Definition Anchoring (Entity Recognition)

AI models build knowledge graphs by connecting entities (concepts, terms, objects) through relationships. When you define a term clearly the first time it appears, you help AI systems:
- Recognize the entity
- Extract its definition
- Connect it to related entities

**Format:**
```
**Bold the term** followed immediately by its definition in the same sentence.
```

**Example:**
> **Feline asthma is a chronic inflammatory disease of the lower airways** that causes recurrent episodes of coughing, wheezing, and difficulty breathing. Unlike human asthma, which is often allergic in origin, feline asthma...

**Key terms to define in every relevant article:**
- Feline asthma
- Bronchodilator
- Corticosteroid
- Aerosol chamber / Spacer chamber
- Metered-dose inhaler (MDI)
- Feline upper respiratory infection (URI)
- Cat flu (feline calicivirus / feline herpesvirus)

### 1.3 Semantic Heading Hierarchy

AI models use heading structure for passage ranking — determining which sections of a page answer specific questions.

**Rules:**
- Only one H1 per article (the title)
- H2 for major sections — each H2 should cover a distinct subtopic
- H3 for subsections — breaking down complex H2 content
- Never skip levels (H2 → H4 without H3)
- Include keywords in H2/H3 naturally

**Example of good structure:**
```
H1: Cat Flu or Feline Asthma? How to Tell the Difference
H2: What Is Cat Flu?
  H3: Common Causes of Feline Upper Respiratory Infections
  H3: Cat Flu Symptoms to Watch For
H2: What Is Feline Asthma?
  H3: How Asthma Differs from Temporary Respiratory Infections
H2: Key Differences Between Cat Flu and Feline Asthma
  H3: Duration: Temporary vs. Chronic
  H3: Triggers: Viruses vs. Allergens
  H3: Treatment Approaches
H2: When to See a Veterinarian
H2: Frequently Asked Questions
H2: What to Do Next
```

---

## Layer 2: Citation Optimization (Being the Source)

### 2.1 Citation-Ready Statistics

AI models preferentially cite content that contains **specific, verifiable, sourced numbers**. Vague statements like "many cats suffer from asthma" are not citable. "1-5% of cats suffer from feline asthma (Cornell Feline Health Center, 2024)" is citable.

**Format:**
```
[Specific number/statistic] + (Source, Year)
```

**Examples:**
> Studies indicate that approximately **1-5% of all cats** develop feline asthma during their lifetime (Cornell Feline Health Center, 2024).

> Inhaled corticosteroids delivered through a spacer chamber achieve approximately **10-20% lung deposition**, compared to less than **1% when using an inhaler directly** (Journal of Feline Medicine and Surgery, 2023).

> Cats with mild to moderate asthma treated with inhaled fluticasone showed **significant improvement within 2 weeks** in approximately **80% of cases** (Journal of Veterinary Internal Medicine, 2022).

**Inventory of hard statistics to maintain and rotate across articles** (use where relevant):
- 1-5% of cats have feline asthma (Cornell)
- 10-20% lung deposition with spacer vs. <1% without
- 80% improvement within 2 weeks with inhaled treatment
- Inhaled corticosteroids have 1/100th the systemic absorption of oral prednisolone
- Cats take 20-30 breaths per minute normally; >40 at rest = concerning
- Aerosol chambers reduce oropharyngeal deposition by 90%+ vs. direct inhaler use

### 2.2 Source Attribution Format

Every claim that could be cited by AI must have a traceable source. The format matters — AI models extract "Author, Title, Publication, Year" patterns.

**Good (AI can parse):**
```
A 2023 study by Reinero et al. in the *Journal of Feline Medicine and Surgery* found that...
According to the Cornell Feline Health Center (2024),...
Research published in the *Journal of Veterinary Internal Medicine* (Trzil et al., 2022) demonstrated...
```

**Bad (AI cannot verify):**
```
Studies show...
Veterinarians recommend...
Research indicates...
```

### 2.3 Author Entity Strength

AI models check author authority. "Peter Jonathan" must be a recognizable, consistent entity.

**Requirements (every article):**
- Author field: "Peter Jonathan"
- `custom:author_name` metafield: "Peter Jonathan"
- Link to `/pages/about-peter-jonathan` where natural (e.g., in intro or byline area)
- Author bio page must list credentials, expertise areas, and link back to key articles

---

## Layer 3: FAQ & Voice Search Optimization

### 3.1 Self-Contained FAQ Answers

FAQ sections feed Google AI Overviews, voice search, and People Also Ask. Each answer must:
- Be **completely self-contained** — understandable without reading the article
- Be **2-4 sentences** — short enough for voice, detailed enough for text
- **Never reference other parts of the article** (no "as mentioned above")
- **Include the keyword** from the question naturally
- **Remove markdown links** — plain text only (schema doesn't render links)

**Good FAQ answer:**
> **Can cats get the flu from humans?**
> Most human influenza viruses cannot infect cats. However, cats can catch their own version of the flu — feline upper respiratory infections caused by feline calicivirus or feline herpesvirus. If you're sick, practice good hygiene around your cat, but the risk of transmission is very low.

**Bad FAQ answer:**
> **Can cats get the flu from humans?**
> As we discussed in the section above, the answer depends on several factors. Cats generally don't catch human flu, but there are exceptions. Click here to learn more about feline respiratory diseases.

### 3.2 Question Formatting for Voice Search

Voice assistants (Siri, Alexa, Google Assistant) pull answers from FAQ sections. The question phrasing should match how people actually speak:

- ✅ "Can my cat catch my cold?" (conversational)
- ✅ "How long does cat flu last?" (natural question)
- ❌ "Feline influenza duration prognosis" (clinical/search-engine speak)

**Voice-optimized question starters:**
- "Can cats..." / "Can my cat..."
- "How long does..." / "How often should..."
- "What does... look like?"
- "Is it normal for my cat to..."
- "When should I worry about..."

---

## Layer 4: Structured Data & Rich Results

### 4.1 FAQ Schema (Already Implemented)

`main-blog-post.liquid` renders FAQPage JSON-LD from `article.metafields.seo.faq_schema`. This directly feeds Google AI Overviews and rich results.

### 4.2 Article Schema

`main-blog-post.liquid` renders Article JSON-LD. Ensure:
- `headline` = article title
- `author.name` = "Peter Jonathan"
- `datePublished` / `dateModified` = correct
- `image` = featured image URL

### 4.3 BreadcrumbList Schema

Already provided by Shopify theme. Breadcrumbs help AI understand site hierarchy.

### 4.4 Comparison Tables (When Applicable)

When comparing two things (spacer vs no spacer, cat flu vs asthma, AeroKat vs Neobay, steroids vs inhaled), use HTML tables. AI models extract and cite structured comparison data better than prose.

**Example:**
```html
<table>
  <thead>
    <tr><th>Feature</th><th>Cat Flu</th><th>Feline Asthma</th></tr>
  </thead>
  <tbody>
    <tr><td>Duration</td><td>1-2 weeks</td><td>Lifelong (manageable)</td></tr>
    <tr><td>Cause</td><td>Viral infection</td><td>Immune-mediated inflammation</td></tr>
    <tr><td>Treatment</td><td>Supportive care</td><td>Inhaled corticosteroids via spacer</td></tr>
  </tbody>
</table>
```

---

## Layer 5: Content Depth & Uniqueness Signals

### 5.1 Minimum Depth Threshold

AI models associate content depth with authority. Thin content (under 1,000 words on a complex topic) is rarely cited.

| Article Type | Minimum Word Count |
|-------------|-------------------|
| Symptom-awareness | 1,500 |
| Knowledge-education | 2,000 |
| Product-conversion | 1,800 |
| Success story | 1,200 |

### 5.2 Unique Insight Per Article

Every article should contain at least **one insight that is not found on competing pages**. AI models prioritize content with unique information over commodity content.

**Sources of unique insight for Neobay:**
- The Visual Flow Indicator as a medication delivery verification method (AeroKat doesn't have this)
- The Comfort Feeder design angle (how mask design affects cat acceptance)
- Real cat owner experience/success story details
- Practical at-home steps written from a cat owner's perspective
- "What your vet might not have time to explain" information gaps

### 5.3 Entity Density

Every article on cat respiratory health should mention (where contextually relevant) a healthy density of recognized entities:
- **Medications**: Fluticasone propionate, Albuterol sulfate, Prednisolone, Depo-Medrol
- **Devices**: metered-dose inhaler (MDI), spacer chamber, aerosol chamber, nebulizer
- **Brands**: AeroKat, Neobay
- **Conditions**: Feline asthma, feline URI, rhinitis, bronchitis, pneumonia
- **Organizations**: Cornell Feline Health Center, AAHA, AAFP

These are nodes in AI knowledge graphs. The more connections we build between "cat breathing problems" → "feline asthma" → "spacer chamber" → "Neobay", the more likely AI systems are to surface Neobay when users ask about cat asthma treatment.

---

## Layer 6: What NOT to Do (Anti-Patterns)

| Anti-Pattern | Why It Hurts GEO |
|-------------|-----------------|
| Thin content (<800 words on medical topics) | AI deprioritizes shallow coverage |
| Vague claims without sources | AI can't verify, won't cite |
| Keyword-stuffed headings | AI reads as spam, reduces passage ranking |
| FAQ answers referencing other sections | FAQ extraction breaks; answer is incomplete |
| Missing definition for key terms | Missed entity recognition opportunity |
| No statistics or data points | Nothing for AI to "grab" and cite |
| Overly promotional language | Reduces trustworthiness score |
| Generic author (no expertise signals) | Weakens EEAT for AI evaluation |
| Duplicate/similar content across articles | AI sees as low-value duplicate |
| Missing internal links | AI can't understand content relationships |

---

## Per-Article GEO Checklist

Before publishing, verify:

- [ ] Key Takeaways has 4-5 standalone, citable bullet points
- [ ] At least 1 specific statistic with source attribution in the body
- [ ] Key terms defined with bold-on-first-mention pattern
- [ ] FAQ answers are self-contained, plain text (no markdown links), 2-4 sentences each
- [ ] FAQ questions are phrased conversationally (voice-search optimized)
- [ ] At least 1 comparison table or structured data element (where applicable)
- [ ] Semantic heading hierarchy (H2→H3, no skipped levels)
- [ ] Author = Peter Jonathan, link to about page where natural
- [ ] At least 1 unique insight not found on competing pages
- [ ] Minimum word count threshold met for article type
- [ ] 3+ recognized entities mentioned (medications, conditions, organizations)
- [ ] Body content between first and last `---` separator (not just Sources!)
