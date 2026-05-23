# Internal Linking Structure — Neobay Blog

## Architecture: 5 Topic Clusters + 1 Conversion Endpoint

Every article belongs to one primary cluster. Links flow: Hub → Spokes, Spokes → Hub, Spokes ↔ Spokes, and cross-cluster bridges where content naturally connects.

---

## Cluster A: Feline Asthma Core

**Hub:** #4 How Vets Diagnose Feline Asthma (`/blogs/feline-asthma/how-vets-diagnose-feline-asthma-tests-x-rays-and-what-to-expect`)

| # | Article | Handle | Links To | Linked From |
|---|---------|--------|----------|-------------|
| A-Hub | How Vets Diagnose Feline Asthma | `how-vets-diagnose-feline-asthma-tests-x-rays-and-what-to-expect` | All A spokes, product page | All A spokes |
| A-1 | #5 Common Triggers of Feline Asthma | `common-triggers-that-make-your-cats-asthma-worse` | A-Hub, A-4 (#2 asthma vs hairball), product page | A-Hub, A-4, B-4 |
| A-2 | #2 Feline Asthma vs Hairball | `feline-asthma-vs-hairball` | A-Hub, A-1, C-1 (#3 what is spacer), product page, D-3 (June #3 hairballs) | A-Hub, A-1, D-3 |
| A-3 | #11 Cat Flu or Feline Asthma? | `cat-flu-or-feline-asthma` | A-Hub, A-1, A-2, C-1, product page, D-1 (June #1 cat cold) | A-Hub, D-1, D-2 |
| A-4 | June #4 Steroids for Cats | `steroids-for-cats-side-effects-alternatives` | A-Hub, A-1, C-1, B-5 (#10 human inhalers), product page | A-Hub, C-1 |
| A-5 | Phase 3 Feline Bronchitis | `feline-bronchitis-symptoms-treatment` | A-Hub, A-1, A-3 (#11 flu vs asthma), C-1, product page | A-Hub, A-3 |

---

## Cluster B: Cat Breathing Symptoms

**Hub:** Why Is My Cat Wheezing? (`/blogs/blog/why-is-my-cat-wheezing`) — existing early article

| # | Article | Handle | Links To | Linked From |
|---|---------|--------|----------|-------------|
| B-Hub | Why Is My Cat Wheezing? | `why-is-my-cat-wheezing` | All B spokes, A-Hub, product page | All B spokes |
| B-1 | #1 Cat Cough After Running | `why-does-my-cat-cough-after-running` | B-Hub, B-3 (#7 breathing fast), A-Hub, product page | B-Hub, B-3, D-2 |
| B-2 | #7 Cat Breathing Fast While Sleeping | `why-is-my-cat-breathing-fast-while-sleeping` | B-Hub, B-1, B-4 (June #2 gasping), A-Hub, product page | B-Hub, B-1, B-4 |
| B-3 | June #2 Cat Gasping for Air | `cat-gasping-for-air-emergency-signs` | B-Hub, B-2, B-1, A-Hub, A-2 (#2 asthma vs hairball), C-1, product page | B-Hub, B-2 |
| B-4 | #10 Can Cats Use Human Inhalers? | `can-cats-use-human-inhalers` | B-Hub, C-1, C-3 (#6 aerokat vs neobay), A-Hub, A-5 (June #4 steroids), product page | B-Hub, C-1, C-2, C-3, A-5 |

---

## Cluster C: Inhaler Spacer Treatment

**Hub:** #3 What Is a Cat Inhaler Spacer? (`/blogs/blog/what-is-a-cat-inhaler-spacer`)

| # | Article | Handle | Links To | Linked From |
|---|---------|--------|----------|-------------|
| C-Hub | What Is a Cat Inhaler Spacer? | `what-is-a-cat-inhaler-spacer` | All C spokes, product page | All C spokes, A-2, A-3, B-4, D-4 |
| C-1 | #8 Train Cat to Accept Inhaler Mask | `how-to-train-your-cat-to-accept-an-inhaler-mask` | C-Hub, C-2 (administer medication), C-4 (#12 spacer not working), #9 success story, product page | C-Hub, C-2, C-4 |
| C-2 | How to Administer Inhaled Medication (早期) | `how-to-administer-inhaled-medication-stress-free` | C-Hub, C-1, C-4, product page | C-Hub, C-1 |
| C-3 | #6 AeroKat vs Neobay | `aerokat-vs-neobay-which-cat-inhaler-spacer-is-right-for-you` | C-Hub, C-4 (#12 spacer not working), #9 success story, A-Hub, product page | C-Hub, B-4, C-4, E-1 |
| C-4 | #12 5 Signs Spacer Not Working | `signs-cat-inhaler-spacer-not-working` | C-Hub, C-1, C-3, product page (heavy) | C-Hub, C-1, C-3 |
| C-5 | Phase 3 Nebulizer vs Spacer | `cat-nebulizer-vs-aerosol-chamber` | C-Hub, C-3, A-Hub, product page | C-Hub, C-3 |

---

## Cluster D: General Cat Respiratory Health

**Hub:** June #1 Cat Cold & URI Guide (`/blogs/blog/cat-cold-upper-respiratory-infection-home-treatment`)

| # | Article | Handle | Links To | Linked From |
|---|---------|--------|----------|-------------|
| D-Hub | June #1 Cat Cold & URI Guide | `cat-cold-upper-respiratory-infection-home-treatment` | All D spokes, A-3 (#11 flu vs asthma), product page | All D spokes |
| D-1 | June #3 Hairballs Guide | `hairballs-in-cats-normal-vs-asthma` | D-Hub, A-2 (#2 asthma vs hairball), A-Hub, product page | D-Hub, A-2 |
| D-2 | Feline Rhinitis (早期) | `the-ultimate-guide-to-feline-rhinitis` | D-Hub, B-Hub, A-Hub, product page | D-Hub |
| D-3 | Phase 3 Cat Pneumonia | `cat-pneumonia-fluid-in-lungs` | D-Hub, B-Hub, B-3 (June #2 gasping), A-Hub, product page | D-Hub |
| D-4 | Phase 3 Sick Cat Signs | `how-to-tell-if-cat-is-sick` | D-Hub, B-Hub, B-2 (#7 breathing fast), product page | D-Hub |
| D-5 | Phase 3 Cross-Species Transmission | `can-cats-get-sick-from-humans` | D-Hub, A-3 (#11 flu vs asthma), product page | D-Hub |
| D-6 | Phase 3 Nasal Discharge Guide | `cat-nasal-discharge-mucus-color-guide` | D-Hub, D-2 (rhinitis), product page | D-Hub |

---

## Cluster E: Product Decision (Conversion Endpoint)

**Hub:** 产品页 `/products/neobay-cat-aerosol-chamber`

| # | Article | Handle | Links To | Linked From |
|---|---------|--------|----------|-------------|
| E-Hub | Product Page | `neobay-cat-aerosol-chamber` | (product page — receives links, links to collection/brand pages) | Every article (minimum 1 link each) |
| E-1 | #9 Cat Owner Success Story | `real-cat-owner-story-managed-feline-asthma-without-daily-pills` | E-Hub, C-1 (#8 training), C-3 (#6 aerokat vs neobay), product page | C-3, C-1 |
| E-2 | Landing Pages (FAQs, Brand Story, etc.) | various | product page, relevant blog articles | Mentioned in article CTAs |

---

## Six Linking Rules

### Rule 1: Hub → Spokes
Each hub article includes 1 contextual link to every spoke in its cluster. Example: In #4 (diagnosis hub), when discussing tests, link to #5 (triggers) ("Once diagnosed, identifying your cat's specific triggers is the next step"). When discussing treatment, link to #3 (spacer introduction).

### Rule 2: Spokes → Hub
Every spoke article links back to its cluster hub. Anchor text should include the hub's core keyword. Example: "As we explain in our detailed guide to **feline asthma diagnosis**..." → links to #4 hub.

### Rule 3: Spokes ↔ Spokes
Within the same cluster, spokes link to each other where the topic naturally connects. Avoid forced links. Example: "If your cat coughs after running, that could be a trigger-related asthma symptom" (B-1 → A-1).

### Rule 4: Cross-Cluster Bridges
At natural transition points, link across clusters. Typical bridges:
- **B → A** (symptom → disease): "These breathing symptoms may indicate feline asthma — here's how vets diagnose it"
- **B → C** (symptom → treatment): "If your cat is diagnosed, here's how a spacer chamber works"
- **A → C** (disease → treatment): "The standard treatment uses an inhaler with a spacer chamber"
- **D → A** (general → specific): "While cat colds are temporary, feline asthma is chronic — here's the difference"
- **D → C** (general → conversion): not typical unless respiratory issue requires inhaler

### Rule 5: Every Article → Product Page (Minimum 1×)
Every article must link to `/products/neobay-cat-aerosol-chamber` at least once. The natural place is in the "What to Do Next" final CTA section. Articles with stronger product relevance (#11, #12, AeroKat comparison, steroids, success story, spacer troubleshooting) should have 2-3 product links in natural contextual positions, not just the final CTA.

### Rule 6: Product-Card Articles Get Double Inbound Links
Articles containing `%%bpc:spacer%%` must receive at least 2 inbound links from other articles. These are typically from the same cluster's hub and a cross-cluster bridge. The product card's conversion function only works when traffic reaches the article.

---

## Anchor Text Conventions

- **Varied anchors**: Never use the exact same anchor text for all links to the same target. Rotate between 2-3 variants. Example for #4 (diagnosis hub):
  - "how vets diagnose feline asthma"
  - "feline asthma diagnostic process"
  - "what to expect during asthma testing"

- **Descriptive, not generic**: Avoid "click here" or "read more". The anchor text itself should tell the reader (and search engine) what the target page covers.

- **Natural keyword inclusion**: Include the target page's primary keyword in the anchor text, but only when it reads naturally.

- **Context-appropriate length**: 3-8 words. Short enough to be scannable, long enough to be descriptive.

---

## Linking By Article Type

### Symptom-Awareness Articles (症状搜索层)
- Primary outbound: → relevant disease hub (Cluster A or D), → treatment hub (Cluster C), → product
- Typical link count: 4-5 internal links (2-3 to other articles + 1 to product + 1 to FAQ/contact page)

### Knowledge-Education Articles (知识教育层)
- Primary outbound: → hub (if spoke), → related spokes, → treatment articles, → product
- Typical link count: 5-7 internal links (denser because these establish topic depth)

### Product-Conversion Articles (产品转化层)
- Primary outbound: → product page (heavy, 2-3×), → comparison articles, → success story, → training guide
- Typical link count: 4-6 internal links

---

## Linking Density by Article Length

| Article Length | Minimum Internal Links | Maximum |
|---------------|----------------------|---------|
| 1,500-2,000 words | 3 | 5 |
| 2,000-3,000 words | 4 | 7 |
| 3,000+ words | 5 | 8 |

Each internal link should appear where a reader naturally wants to go deeper on a related subtopic. Never force a link where it doesn't fit the reading flow.

---

## New Article Linking Checklist

When publishing a new article:

1. [ ] Identify which cluster it belongs to
2. [ ] Link to the cluster hub (unless this IS the hub)
3. [ ] Link to 2-3 related spokes (same cluster or cross-cluster bridges)
4. [ ] Link to product page at least once (final CTA + contextual if high relevance)
5. [ ] Link to FAQ page or Contact page in final paragraph
6. [ ] Go back to 2 related existing articles and add a link TO this new article (retroactive linking)
7. [ ] If this article has `%%bpc:spacer%%`, ensure at least 2 existing articles now link to it

Step 6 (retroactive linking) is critical for SEO — new pages need inbound links, and old pages benefit from fresh outbound links. Both directions matter.
