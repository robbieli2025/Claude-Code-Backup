# Neobay Blog Categories

## Shopify Blog Inventory

| Blog Name | Handle | Blog ID | Purpose |
|-----------|--------|---------|---------|
| Blog | blog | 89686802530 | Default/general articles |
| Feline Asthma | feline-asthma | 90090766434 | Asthma symptoms, diagnosis, treatment, medication |
| Cat Breathing | cat-breathing | 90090799202 | Cat breathing problems, respiratory rates, emergencies |
| Spacer Guides | spacer-guides | 90090831970 | Inhaler spacer usage guides, tutorials, tips |
| Success Stories | success-stories | 89726189666 | Customer testimonials, before/after stories |
| News | news | 88151523426 | Brand announcements, product launches, company news |
| User's Guide | users-guide | 89675071586 | Product manuals, setup instructions, maintenance |

## Decision Flow

For each new article, answer these questions in order:

```
1. Is it about feline asthma (symptoms / diagnosis / treatment / medication)?
   → YES → Feline Asthma (90090766434)

2. Is it about cat breathing rate / breathing problems / respiratory emergencies?
   → YES → Cat Breathing (90090799202)

3. Is it a spacer/inhaler usage guide or tutorial?
   → YES → Spacer Guides (90090831970)

4. Is it a customer success story or testimonial?
   → YES → Success Stories (89726189666)

5. Is it brand news, product launch, or company update?
   → YES → News (88151523426)

6. Is it a product user manual or setup guide?
   → YES → User's Guide (89675071586)

7. Everything else:
   → Blog (89686802530)
```

## Article Distribution (Current)

### Feline Asthma (4 articles)
- Why Does My Cat Cough After Running or Playing?
- Feline Asthma vs. Hairball: How to Tell the Difference
- How Vets Diagnose Feline Asthma: Tests, X-Rays, and What to Expect
- Common Triggers That Make Your Cat's Asthma Worse
- Can Cats Use Human Inhalers? What Every Pet Owner Must Know

### Cat Breathing (3 articles)
- Why Is My Cat Breathing Fast While Sleeping?
- Why Is My Cat Wheezing?
- The Ultimate Guide to Feline Rhinitis

### Spacer Guides (4 articles)
- What Is a Cat Inhaler Spacer and Why Does Your Vet Recommend One?
- How to Train Your Cat to Accept an Inhaler Mask (Step-by-Step)
- How to Administer Inhaled Medication Stress-Free
- AeroKat vs Neobay: Which Cat Inhaler Spacer Is Right for You?

### Success Stories (1 article)
- Real Cat Owner Story: How We Managed Our Cat's Asthma Without Daily Pills

### Blog (main) — overflow/general articles
- Currently houses some earlier articles and may receive overflow

## Edge Case Rules

- If an article bridges two categories (e.g., asthma + breathing rate), use the more specific category (Feline Asthma)
- If an article could go in Spacer Guides but has strong asthma treatment focus → Feline Asthma wins
- Success Stories that are primarily educational → put in the topic blog, not Success Stories
- News about a product update → News, not Spacer Guides or User's Guide
