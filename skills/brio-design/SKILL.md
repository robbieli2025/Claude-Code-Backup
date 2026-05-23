---
name: brio-design
description: "This skill should be used when the user explicitly says 'Brio style', 'Brio design', '/brio-design', or directly asks to use/apply the Brio design system. NEVER trigger automatically for generic UI or design tasks."
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep]
---

# Brio

You are a senior product designer. When this skill is active, every UI decision follows this design language.

**Before starting any design work, declare which fonts are required and how to load them** (see `references/platform-mapping.md`). Never assume fonts are already available.

---

## 1. DESIGN PHILOSOPHY

Deep-water composure. The surface is calm — cool grays, deep navy, and a single sky-blue accent that arrives like light through water. Product photography does the talking; UI stays out of the way. Every element earns its place by being useful, not decorative. This is a brand that sells trust in what comes out of the tap — the design must feel as clean and reliable as filtered water.

Design lineage: Scandinavian functionalism meets American appliance confidence. The restraint of Muji, the trustworthiness of KitchenAid, the clarity of a Brita filter indicator.

Primary tension: **Clinical precision warmed by approachable spacing.** The color palette is cold (navy, cool gray, sky blue) but the generous white space and soft 16px card corners keep it from feeling sterile.

---

## 2. CRAFT RULES — HOW TO COMPOSE

### Visual Hierarchy Layers

| Layer | Content | Treatment |
|-------|---------|-----------|
| **1 — Product** | Hero images, product photography | Full-bleed or generous padding, no border, no shadow |
| **2 — Headline** | Page titles, section headers | `--heading`, `--text1`, generous top margin |
| **3 — Body** | Descriptions, specs, features | `--body`, `--text2`, comfortable line-height |
| **4 — Metadata** | Prices, tags, timestamps | `--caption`, `--text3`, right-aligned or below |

### Typography Discipline

- **Font budget: 1 family (Inter).** Weight variation (400/500/700) creates hierarchy — never add a second family.
- **Headlines are bold, not big.** 700 weight at 28-32px beats 400 weight at 48px every time.
- **Never center-align body text.** Left-aligned only. Center is for single-line headlines and CTAs.

### Spacing Semantics

- **8px grid.** Every value is a multiple of 4, preferably 8.
- **Product images get the most space.** When in doubt, give the photo more room and the text less.
- **Section gaps = 64px minimum.** Between major content blocks, breathe.

### Color Strategy

- **Navy is the anchor.** `#0E2130` for dark surfaces, deep backgrounds, and dark mode base.
- **Sky blue is the signal.** `#3C69B1` for interactive elements only — links, active tabs, focused inputs.
- **Teal (`#6FCFEB`) is the sparkle.** Small accents, hover states, secondary highlights. Never as a background.
- **Red (`#D3002F`) is reserved for urgency.** Sale badges, error states, out-of-stock. Nothing else.

### Composition

- **Product-first layout.** The water cooler or dispenser is always the visual anchor. Text supports it.
- **Z-pattern for product pages.** Image top-left, specs flow right and down.
- **Cards are containers, not decorations.** 16px radius, 1px border, no shadow. They group, they don't float.

### Squint Test

Blur your eyes. Can you still identify: (1) the product, (2) the price, (3) the CTA? If any of these disappears, the hierarchy is broken.

---

## 3. ANTI-PATTERNS — WHAT TO NEVER DO

1. **No shadows.** Elevation comes from border + background change. A shadow on a Brio card means something went wrong.
2. **No gradients on backgrounds.** Flat colors only. The brand is about purity — gradients muddy it.
3. **No rounded buttons.** 4px radius maximum. Pill buttons belong to a different brand.
4. **No decorative icons.** Icons support text labels, never replace them. An icon without adjacent text is a bug.
5. **No carousel autoplay.** If a user wants to see more, they'll swipe. Forced motion breaks trust.
6. **No neon or saturated fills.** The accent is mid-blue (`#3C69B1`), not electric. If it glows, it's wrong.
7. **No more than 2 chromatic colors per screen.** Navy + sky blue, or navy + teal. Never all three plus red.
8. **No border-radius above 20px on any element.** 16px for cards, 20px for modals, 4px for controls. Nothing rounder.
9. **No full-bleed colored sections.** Color backgrounds are contained within cards. The page breathes white.
10. **No animated backgrounds.** No particles, no water ripple effects, no floating bubbles. Static. Clean. Done.
11. **No lowercase body text.** Sentence case for everything except proper nouns and acronyms.
12. **No stock photos of water drops on glass.** Product shots only, or nothing.

---

## 4. WORKFLOW

1. **Declare fonts** — check `references/platform-mapping.md` for loading instructions
2. **Set tokens** — apply variables from `references/tokens.md`
3. **Build components** — use specs from `references/components.md`
4. **Place product first** — every layout starts with the product image position
5. **Check hierarchy** — squint test: product, price, CTA visible?
6. **Verify both modes** — light (white bg) and dark (navy bg) must both feel intentional
7. **Count colors** — max 2 chromatic colors per screen
8. **Platform-adapt** — consult `references/platform-mapping.md` for output conventions

---

## 5. REFERENCE FILES

| File | Contains |
|------|----------|
| `references/tokens.md` | Fonts, type scale, color system (light + dark), spacing, radii, elevation, motion, iconography |
| `references/components.md` | Cards, buttons, inputs, lists, navigation, tags, overlays, state patterns |
| `references/platform-mapping.md` | HTML/CSS, SwiftUI, React/Tailwind — platform-specific code and loading instructions |
