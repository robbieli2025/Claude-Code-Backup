---
name: shopify-theme-dev
description: Use when modifying, reviewing, debugging, or planning Shopify theme code, including Liquid templates, sections, snippets, JSON templates, theme settings, CSS, JavaScript, product pages, collection pages, landing pages, checkout-adjacent UI, performance, accessibility, Shopify CLI workflows, and theme preview QA.
---

# Shopify Theme Dev

## Purpose

Use this skill for Shopify theme work where code changes must respect the existing theme architecture, merchant editing experience, storefront performance, SEO, accessibility, and responsive behavior.

## Workflow

1. Identify the theme structure before editing.
   - Inspect `layout/`, `templates/`, `sections/`, `snippets/`, `assets/`, `config/`, and `locales/`.
   - Determine whether the theme is Online Store 2.0, Dawn-derived, or custom.
   - Prefer existing section, block, setting, CSS, and JavaScript patterns over introducing new architecture.

2. Clarify the merchant-facing editing model.
   - Add or update section schema only when the merchant needs control.
   - Keep settings labels concise and non-technical.
   - Preserve existing block limits, presets, translations, and theme setting conventions.

3. Implement with Shopify constraints in mind.
   - Use Liquid filters and objects according to Shopify semantics.
   - Keep snippets focused and avoid duplicated markup when an existing snippet can be reused.
   - Avoid breaking dynamic sources, metafields, market/language behavior, and cart/product form behavior.
   - Do not hardcode product, collection, page, or market-specific content unless the user explicitly asks.

4. Protect storefront quality.
   - Check desktop and mobile layouts.
   - Avoid layout shift, oversized assets, render-blocking additions, and unnecessary JavaScript.
   - Maintain keyboard access, focus states, semantic headings, alt text, and color contrast.
   - Preserve SEO-critical elements such as canonical URLs, structured data, breadcrumbs, title hierarchy, and indexable content.

5. Verify the change.
   - Run the repo's available linting, formatting, theme-check, tests, or build commands.
   - If a local preview is available, use the browser to inspect the affected pages and capture visual issues.
   - Summarize the edited files, verification performed, and any remaining merchant setup steps.

## Common Tasks

- Create or modify Shopify sections and blocks.
- Adjust product, collection, blog, article, page, cart, header, footer, and landing page templates.
- Add metafield-driven content modules.
- Improve responsive styling and interaction behavior.
- Diagnose Liquid errors, broken schema, missing snippets, theme-check findings, or storefront regressions.
- Prepare clean commits or pull requests for Shopify theme changes.

## Output Expectations

When proposing or completing Shopify work, include:
- The affected storefront surfaces.
- The files changed.
- How merchants can edit the new behavior in the theme editor, if relevant.
- The verification performed and anything that still needs live-store credentials, preview URLs, or Shopify admin access.
