# Brio — Components

Every component below is specified for both light and dark modes. Token references (`--token`) resolve to the values defined in `references/tokens.md`. When a component has a dark-mode override, it is listed explicitly; otherwise the light-mode value applies via CSS custom properties.

---

## 1. Button Primary

The main call-to-action. Used once per prominent section — "Shop Now", "Add to Cart", "Subscribe".

| Property | Light | Dark |
|----------|-------|------|
| Background | `--text1` (`#202223`) | `--surface2` (`#08131C`) |
| Text color | `#FFFFFF` | `--text1` (`#F5F6F6`) |
| Border | none | none |
| Radius | `--radius-control` (4px) | 4px |
| Height | 44px | 44px |
| Padding | `12px 24px` | `12px 24px` |
| Font | Inter 400, 15px | Inter 400, 15px |
| Hover bg | `#3B3D41` | `--surface3` (`#060D14`) |
| Active bg | `#141516` | `--border` (`#08131C`) |
| Focus | 2px solid `--accent`, offset 2px | 2px solid `--accent`, offset 2px |
| Disabled | opacity 0.4, cursor `not-allowed` | same |

**Rules:**
- One primary button per section. If two equal-weight actions exist, use one primary + one secondary.
- Text is sentence case: "Add to Cart", not "ADD TO CART".
- Icon + text: 20px icon left of label, 8px gap.
- Never use primary button style for navigation links.

---

## 2. Button Secondary

Secondary action — "Learn More", "Compare", "View Specs". Paired with primary to create visual hierarchy.

| Property | Light | Dark |
|----------|-------|------|
| Background | transparent | transparent |
| Text color | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Border | 2px solid `--text1` (`#202223`) | 2px solid `--text1` (`#F5F6F6`) |
| Radius | `--radius-control` (4px) | 4px |
| Height | 44px | 44px |
| Padding | `10px 24px` | `10px 24px` |
| Font | Inter 400, 15px | Inter 400, 15px |
| Hover bg | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Hover text | `#FFFFFF` | `--background` (`#0E2130`) |
| Hover border | 2px solid `--text1` | 2px solid `--text1` |
| Active bg | `#141516` | `#D5D8DA` |
| Active text | `#FFFFFF` | `--background` |
| Focus | 2px solid `--accent`, offset 2px | 2px solid `--accent`, offset 2px |
| Disabled | opacity 0.4, cursor `not-allowed` | same |

**Rules:**
- The 2px border replaces the filled background. The fill-inversion on hover creates a clear state change.
- Same height as primary (44px) so they stack evenly.

---

## 3. Button Ghost

Tertiary action — filter chips, inline links styled as buttons, card footer actions.

| Property | Light | Dark |
|----------|-------|------|
| Background | transparent | transparent |
| Text color | `--accent` (`#3C69B1`) | `--accent` (`#6FCFEB`) |
| Border | none | none |
| Radius | `--radius-control` (4px) | 4px |
| Height | 36px | 36px |
| Padding | `8px 16px` | `8px 16px` |
| Font | Inter 400, 15px | Inter 400, 15px |
| Hover bg | `--accent-subtle` (`#EBF2FA`) | `--accent-subtle` (`#08131C`) |
| Active bg | `#C5D9EE` | `--surface3` (`#060D14`) |
| Focus | 2px solid `--accent`, offset 2px | 2px solid `--accent`, offset 2px |
| Disabled | opacity 0.4, cursor `not-allowed` | same |

**Rules:**
- Ghost buttons never appear alone as the primary page action.
- If a ghost button sits inside a card, it goes in the card footer, never floating in body content.

---

## 4. Button Icon

Icon-only button — close modals, expand/collapse, tool actions.

| Property | Light | Dark |
|----------|-------|------|
| Background | transparent | transparent |
| Icon color | `--text2` (`#6D7175`) | `--text2` (`#9EA3AA`) |
| Border | none | none |
| Radius | `--radius-control` (4px) | 4px |
| Size | 36px x 36px | 36px x 36px |
| Icon size | 20px | 20px |
| Hover bg | `--surface2` (`#EBECEC`) | `--surface2` (`#08131C`) |
| Hover icon color | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Active bg | `--surface3` (`#D5D8DA`) | `--surface3` (`#060D14`) |
| Focus | 2px solid `--accent`, offset 2px | 2px solid `--accent`, offset 2px |
| Disabled | opacity 0.4, cursor `not-allowed` | same |

**Rules:**
- Always include an `aria-label` — icon-only buttons are meaningless to screen readers without it.
- 36px minimum touch target. The icon is 20px; the remaining 16px is padding.
- Never use two icon buttons adjacent without a 8px gap.

---

## 5. Card Standard

Default container for grouped content — feature blocks, spec groups, blog post previews.

| Property | Light | Dark |
|----------|-------|------|
| Background | `--surface1` (`#FFFFFF`) | `--surface1` (`#0B1A26`) |
| Border | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Radius | `--radius-component` (16px) | 16px |
| Padding | 24px | 24px |
| Shadow | none | none |
| Hover | border-color `--border-visible` (`#C5C8D1`) | border-color `--border-visible` (`#0B1A26`) |

**Rules:**
- Cards are separated from the page by background contrast (`#FFFFFF` on `#F5F6F6`) and a 1px border. No shadow. Ever.
- Content inside a card: title uses `--subheading`, body uses `--body`, metadata uses `--caption`.
- Card padding is 24px. If the card contains a full-bleed image, the image sits at the top with no padding; text content gets 24px below.

---

## 6. Card Product

Product listing card — used in collection grids, recommendation carousels, comparison tables.

| Property | Light | Dark |
|----------|-------|------|
| Background | `--surface1` (`#FFFFFF`) | `--surface1` (`#0B1A26`) |
| Border | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Radius | `--radius-component` (16px) | 16px |
| Shadow | none | none |
| Image area | top, full-bleed, 4:3 aspect ratio | same |
| Padding (text) | 16px | 16px |
| Title | Inter 500, 15px, `--text1` | Inter 500, 15px, `--text1` |
| Price | Inter 700, 22px, `--text1` | Inter 700, 22px, `--text1` |
| Compare price | Inter 400, 13px, `--text3`, strikethrough | Inter 400, 13px, `--text3`, strikethrough |
| Hover | border-color `--border-visible` | border-color `--border-visible` |

**Rules:**
- Product image is always full-bleed top. No rounded corners on the image itself — the card's 16px radius clips it.
- Price is the visual anchor after the image. Use `--subheading` scale (22px, 700 weight). A price is a headline.
- Sale badge: positioned top-right over image, 8px from edges. See Tag Status.
- Grid gap: 16px on mobile, 24px on desktop.

---

## 7. Card Feature

Feature highlight card — used for "Why Brio" sections, technology callouts, warranty highlights.

| Property | Light | Dark |
|----------|-------|------|
| Background | `--surface1` (`#FFFFFF`) | `--surface1` (`#0B1A26`) |
| Border | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Radius | `--radius-component` (16px) | 16px |
| Shadow | none | none |
| Padding | 24px | 24px |
| Icon | 24px, `--accent` (`#3C69B1`) | 24px, `--accent` (`#6FCFEB`) |
| Icon margin-bottom | 12px | 12px |
| Title | Inter 500, 15px, `--text1` | Inter 500, 15px, `--text1` |
| Title margin-bottom | 8px | 8px |
| Body | Inter 400, 13px, `--text2` | Inter 400, 13px, `--text2` |
| Hover | border-color `--border-visible` | border-color `--border-visible` |

**Rules:**
- The icon is decorative — it supports the title, it does not replace it. Title text is always present.
- Feature cards typically appear in a 3-column grid on desktop, 1-column on mobile.
- No CTA button inside feature cards. If the user needs to act, use a standard card with a ghost button footer.

---

## 8. Input Text

Single-line text input — forms, search, filters.

| Property | Light | Dark |
|----------|-------|------|
| Background | `#FFFFFF` | `--surface1` (`#0B1A26`) |
| Border (default) | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Border (focus) | 2px solid `--accent` (`#3C69B1`) | 2px solid `--accent` (`#6FCFEB`) |
| Border (error) | 2px solid `--error` (`#D3002F`) | 2px solid `--error` (`#D3002F`) |
| Border (disabled) | 1px solid `--border`, opacity 0.4 | same |
| Radius | `--radius-control` (4px) | 4px |
| Height | 44px | 44px |
| Padding | `12px 16px` | `12px 16px` |
| Font | Inter 400, 15px | Inter 400, 15px |
| Text color | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Placeholder | `--text3` (`#9EA3AA`) | `--text3` (`#6D7175`) |
| Label | Inter 500, 11px, `--text2`, 4px below label | same, `--text2` (`#9EA3AA`) |
| Error message | Inter 400, 12px, `--error`, 4px below input | same |
| Transition | border-color 150ms ease-in-out | same |

**Rules:**
- Focus border increases from 1px to 2px. This shifts the input by 1px — compensate with 1px padding change or accept the shift (it is intentional and consistent).
- Label sits above the input, never inside it as a floating placeholder.
- Error state: red border + error message below. Never use red placeholder text.

---

## 9. Input Select

Dropdown select — model selection, quantity, region.

| Property | Light | Dark |
|----------|-------|------|
| Background | `#FFFFFF` | `--surface1` (`#0B1A26`) |
| Border (default) | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Border (focus) | 2px solid `--accent` (`#3C69B1`) | 2px solid `--accent` (`#6FCFEB`) |
| Border (error) | 2px solid `--error` (`#D3002F`) | 2px solid `--error` (`#D3002F`) |
| Radius | `--radius-control` (4px) | 4px |
| Height | 44px | 44px |
| Padding | `12px 40px 12px 16px` | same |
| Font | Inter 400, 15px | Inter 400, 15px |
| Text color | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Chevon | 20px, `--text2`, right 12px, pointer-events none | same, `--text2` (`#9EA3AA`) |
| Dropdown bg | `#FFFFFF` | `--surface1` (`#0B1A26`) |
| Dropdown border | 1px solid `--border` | 1px solid `--border` |
| Dropdown radius | `--radius-control` (4px) | 4px |
| Option hover | `--accent-subtle` (`#EBF2FA`) | `--surface2` (`#08131C`) |
| Label | Inter 500, 11px, `--text2`, 4px above | same |

**Rules:**
- Custom chevron (Phosphor `caret-down`) overrides native browser arrow.
- Dropdown panel has no shadow — separated by border and background contrast.
- Same height, border treatment, and focus behavior as Input Text.

---

## 10. Input Textarea

Multi-line text input — reviews, contact form messages, support tickets.

| Property | Light | Dark |
|----------|-------|------|
| Background | `#FFFFFF` | `--surface1` (`#0B1A26`) |
| Border (default) | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Border (focus) | 2px solid `--accent` (`#3C69B1`) | 2px solid `--accent` (`#6FCFEB`) |
| Border (error) | 2px solid `--error` (`#D3002F`) | 2px solid `--error` (`#D3002F`) |
| Radius | `--radius-control` (4px) | 4px |
| Min height | 120px | 120px |
| Padding | `12px 16px` | `12px 16px` |
| Font | Inter 400, 15px | Inter 400, 15px |
| Text color | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Placeholder | `--text3` (`#9EA3AA`) | `--text3` (`#6D7175`) |
| Resize | vertical | vertical |
| Label | Inter 500, 11px, `--text2`, 4px above | same |
| Character count | Inter 400, 12px, `--text3`, right-aligned below | same |

**Rules:**
- Shares the same border, focus, and error patterns as Input Text.
- Vertical resize only. Horizontal resize breaks layout.
- Character count appears only when a maxlength is defined.

---

## 11. Checkbox

Boolean selection — filter options, terms acceptance, preference toggles.

| Property | Light | Dark |
|----------|-------|------|
| Box size | 18px x 18px | 18px x 18px |
| Box border (default) | 1px solid `--border-visible` (`#C5C8D1`) | 1px solid `--border-visible` (`#0B1A26`) |
| Box border (checked) | none (filled) | none (filled) |
| Box bg (checked) | `--accent` (`#3C69B1`) | `--accent` (`#6FCFEB`) |
| Box radius | `--radius-element` (2px) | 2px |
| Checkmark | 12px, `#FFFFFF` | `--background` (`#0E2130`) |
| Label | Inter 400, 15px, `--text1`, 8px left of box | same, `--text1` (`#F5F6F6`) |
| Focus | 2px solid `--accent` outline on box, offset 2px | same |
| Disabled | opacity 0.4 | same |
| Transition | background-color 150ms ease-in-out | same |

**Rules:**
- The label is clickable — the entire row is a touch target.
- Checkmark uses Phosphor `check` thin, 12px.
- Grouped checkboxes stack vertically with 8px gap between items.

---

## 12. Radio

Single-selection control — model variant picker, shipping option.

| Property | Light | Dark |
|----------|-------|------|
| Circle size | 18px x 18px | 18px x 18px |
| Circle border (default) | 1px solid `--border-visible` (`#C5C8D1`) | 1px solid `--border-visible` (`#0B1A26`) |
| Circle border (selected) | 2px solid `--accent` (`#3C69B1`) | 2px solid `--accent` (`#6FCFEB`) |
| Inner dot size | 10px | 10px |
| Inner dot bg | `--accent` (`#3C69B1`) | `--accent` (`#6FCFEB`) |
| Label | Inter 400, 15px, `--text1`, 8px left of circle | same, `--text1` (`#F5F6F6`) |
| Focus | 2px solid `--accent` outline, offset 2px | same |
| Disabled | opacity 0.4 | same |
| Transition | border-color 150ms ease-in-out | same |

**Rules:**
- Use radio for mutually exclusive options (pick one). Use checkbox for independent options (pick any).
- Grouped radios stack vertically with 8px gap.
- On product pages, radio is used for variant selection (e.g. color: Stainless Steel / Matte Black).

---

## 13. Toggle / Switch

On/off control — notification preferences, feature flags, settings.

| Property | Light | Dark |
|----------|-------|------|
| Track width | 44px | 44px |
| Track height | 24px | 24px |
| Track bg (off) | `--surface3` (`#D5D8DA`) | `--surface3` (`#060D14`) |
| Track bg (on) | `--accent` (`#3C69B1`) | `--accent` (`#6FCFEB`) |
| Track radius | `--radius-pill` (999px) | 999px |
| Thumb size | 18px | 18px |
| Thumb bg | `#FFFFFF` | `#FFFFFF` |
| Thumb offset (off) | 3px from left | 3px from left |
| Thumb offset (on) | 3px from right | 3px from right |
| Focus | 2px solid `--accent` outline, offset 2px | same |
| Disabled | opacity 0.4 | same |
| Transition | all 150ms ease-in-out | same |

**Rules:**
- Toggle is for binary settings that take effect immediately (no "Save" button required).
- If the action requires confirmation, use a checkbox instead.
- Label sits to the right of the toggle, 8px gap.

---

## 14. Tag / Badge

Non-interactive label — product category, filter indicator, content type.

| Property | Light | Dark |
|----------|-------|------|
| Background | `--surface2` (`#EBECEC`) | `--surface2` (`#08131C`) |
| Text color | `--text2` (`#6D7175`) | `--text2` (`#9EA3AA`) |
| Border | none | none |
| Radius (default) | `--radius-control` (4px) | 4px |
| Radius (pill variant) | `--radius-pill` (999px) | 999px |
| Height | 24px | 24px |
| Padding | `4px 8px` | `4px 8px` |
| Font | Inter 500, 11px | Inter 500, 11px |
| Letter spacing | 0.04em | 0.04em |

**Rules:**
- No border. Tags are background-only — they group by color, not outline.
- Use 4px radius for tags inside forms/filters. Use pill (999px) for tags in editorial content.
- Text is uppercase for tags: "BOTTOM-LOAD", "STAINLESS STEEL". (This is the only uppercase exception in the system — tags are labels, not prose.)

---

## 15. Tag Status

Semantic-status label — "In Stock", "Sale", "Out of Stock", "Pre-order".

| Property | Light | Dark |
|----------|-------|------|
| Border | none | none |
| Radius | `--radius-control` (4px) | 4px |
| Height | 24px | 24px |
| Padding | `4px 8px` | `4px 8px` |
| Font | Inter 500, 11px | Inter 500, 11px |
| Letter spacing | 0.04em | 0.04em |

**Status variants:**

| Status | Background (Light) | Text (Light) | Background (Dark) | Text (Dark) |
|--------|-------------------|--------------|-------------------|-------------|
| Success (In Stock) | `#E8F8E8` | `#1B9500` | `#08131C` | `#1B9500` |
| Warning (Low Stock) | `#FFF8E8` | `#C48A00` | `#08131C` | `#C48A00` |
| Error (Out of Stock) | `#FDE8E8` | `#D3002F` | `#08131C` | `#D3002F` |
| Info (Pre-order) | `#EBF2FA` | `#3C69B1` | `#08131C` | `#6FCFEB` |
| Sale | `#FDE8E8` | `#D3002F` | `#08131C` | `#D3002F` |

**Rules:**
- Sale tag uses error (red) — urgency is the point. Never use green or blue for a sale indicator.
- Status tags on product cards sit top-right, overlapping the product image, 8px from top and right edges.
- Text is uppercase: "IN STOCK", "SALE", "OUT OF STOCK".

---

## 16. Avatar

User or reviewer identity — review cards, account header, support chat.

| Property | Light | Dark |
|----------|-------|------|
| Size (default) | 40px | 40px |
| Size (small) | 32px | 32px |
| Size (large) | 56px | 56px |
| Background | `--surface2` (`#EBECEC`) | `--surface2` (`#08131C`) |
| Text | Inter 500, 14px, `--text2` (`#6D7175`) | Inter 500, 14px, `--text2` (`#9EA3AA`) |
| Border | none | none |
| Radius | `--radius-pill` (999px) | 999px |
| Image | cover, center | cover, center |

**Rules:**
- If no photo, show initials (first + last, uppercase).
- Avatars are circular. No square avatars.
- In review cards, avatar sits left of the reviewer name and date, 12px gap.

---

## 17. Navigation Bar

Site header — logo, primary links, cart icon, search.

| Property | Light | Dark |
|----------|-------|------|
| Background | `--surface1` (`#FFFFFF`) | `--background` (`#0E2130`) |
| Border (bottom) | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Height | 64px | 64px |
| Padding (horizontal) | 24px | 24px |
| Logo height | 32px | 32px |
| Link font | Inter 400, 15px | Inter 400, 15px |
| Link color | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Link hover | `--accent` (`#3C69B1`) | `--accent` (`#6FCFEB`) |
| Active link | `--accent`, underline 2px, offset 4px | same |
| Icon color | `--text2` (`#6D7175`) | `--text2` (`#9EA3AA`) |
| Icon hover | `--text1` | `--text1` |
| Shadow | none | none |
| Sticky | yes, top | yes, top |
| Transition | background-color 300ms ease-in-out | same |

**Rules:**
- Navigation is border-separated from content, not shadow-separated.
- Mobile: hamburger icon (Phosphor `list` thin) replaces link row. Slide-out drawer uses same surface + border treatment.
- Cart icon shows count badge: 16px circle, `--accent` bg, `#FFFFFF` text, top-right of icon.
- Search: icon expands to Input Text on click (300ms width transition).

---

## 18. Breadcrumb

Wayfinding trail — collection pages, product pages, blog posts.

| Property | Light | Dark |
|----------|-------|------|
| Font | Inter 400, 13px | Inter 400, 13px |
| Text color | `--text3` (`#9EA3AA`) | `--text3` (`#6D7175`) |
| Current page color | `--text2` (`#6D7175`) | `--text2` (`#9EA3AA`) |
| Separator | `/` (slash), `--text4` (`#C5C8D1`), 4px margin each side | same, `--text4` (`#C5C8D1`) |
| Link hover | `--accent` (`#3C69B1`) | `--accent` (`#6FCFEB`) |
| Padding (vertical) | 8px 0 | 8px 0 |

**Rules:**
- Breadcrumb sits above the page title, below the navigation bar.
- Current page is plain text (not a link), styled in `--text2`.
- On mobile, show only the parent level + current: "Collection > Product Name".

---

## 19. Tab Bar

Content switcher — product detail sections (Overview / Specs / Reviews), account pages.

| Property | Light | Dark |
|----------|-------|------|
| Background | transparent | transparent |
| Tab font | Inter 400, 15px | Inter 400, 15px |
| Tab color (default) | `--text2` (`#6D7175`) | `--text2` (`#9EA3AA`) |
| Tab color (active) | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Tab color (hover) | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Active indicator | 2px solid `--accent` (`#3C69B1`), bottom | 2px solid `--accent` (`#6FCFEB`), bottom |
| Tab padding | `12px 16px` | `12px 16px` |
| Tab gap | 0 (adjacent) | 0 |
| Border (bottom container) | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Panel padding | 24px 0 | 24px 0 |
| Transition | color 150ms ease-in-out, indicator 300ms ease-in-out | same |

**Rules:**
- Active tab indicator slides (300ms) — it does not pop.
- Tab content panel has no border or background — it sits flush in the page flow.
- On mobile, if tabs exceed screen width, they scroll horizontally with no scrollbar (overflow-x: auto, -webkit-overflow-scrolling: touch).

---

## 20. Pagination

Page navigation — collection pages, blog listing, search results.

| Property | Light | Dark |
|----------|-------|------|
| Page number font | Inter 400, 15px | Inter 400, 15px |
| Page number color | `--text2` (`#6D7175`) | `--text2` (`#9EA3AA`) |
| Active page color | `--text1` (`#202223`) | `--text1` (`#F5F6F6`) |
| Active page indicator | 2px solid `--accent` (`#3C69B1`), bottom | 2px solid `--accent` (`#6FCFEB`), bottom |
| Page button size | 44px x 44px | 44px x 44px |
| Page button radius | `--radius-control` (4px) | 4px |
| Page button hover bg | `--surface2` (`#EBECEC`) | `--surface2` (`#08131C`) |
| Arrow icon | 20px, Phosphor `caret-left` / `caret-right` thin | same |
| Arrow color | `--text2` | `--text2` |
| Arrow hover | `--accent` | `--accent` |
| Disabled arrow | opacity 0.3 | opacity 0.3 |
| Gap | 4px | 4px |

**Rules:**
- 44px touch targets for every page button and arrow.
- Show at most 5 page numbers. Use ellipsis for gaps: `1 2 ... 8 9`.
- On mobile, show "Page X of Y" text instead of number buttons.

---

## 21. Modal

Overlay dialog — product quick view, confirm actions, image zoom.

| Property | Light | Dark |
|----------|-------|------|
| Background | `--surface1` (`#FFFFFF`) | `--surface1` (`#0B1A26`) |
| Border | none | none |
| Top radius | `--radius-container` (20px) | 20px |
| Bottom radius | 0 | 0 |
| Shadow | none | none |
| Max width | 560px | 560px |
| Max height | 85vh | 85vh |
| Padding | 24px | 24px |
| Backdrop | `rgba(0, 0, 0, 0.5)` | `rgba(0, 0, 0, 0.7)` |
| Close button | top-right, 12px from edges, icon button style | same |
| Title | Inter 700, 22px, `--text1` | Inter 700, 22px, `--text1` |
| Transition | fade-in 300ms ease-in-out, slide-up 300ms ease-in-out | same |

**Rules:**
- Modal is separated from the page by backdrop opacity, not shadow.
- Bottom radius is 0 — the modal meets the viewport edge on mobile (full-height sheet).
- Close via: X button, clicking backdrop, pressing Escape.
- Focus trap: Tab cycles within modal. Focus returns to trigger on close.

---

## 22. Toast / Notification

Non-blocking feedback — "Added to cart", "Saved", "Error saving".

| Property | Light | Dark |
|----------|-------|------|
| Background | `--text1` (`#202223`) | `--surface2` (`#08131C`) |
| Text color | `#FFFFFF` | `--text1` (`#F5F6F6`) |
| Border | none | 1px solid `--border` (`#08131C`) |
| Radius | `--radius-component` (16px) | 16px |
| Padding | `12px 16px` | `12px 16px` |
| Font | Inter 400, 15px | Inter 400, 15px |
| Icon (success) | 20px, `#1B9500` | 20px, `#1B9500` |
| Icon (error) | 20px, `#D3002F` | 20px, `#D3002F` |
| Icon (info) | 20px, `#3C69B1` | 20px, `#6FCFEB` |
| Position | bottom-center, 24px from bottom | same |
| Max width | 400px | 400px |
| Auto-dismiss | 4000ms | 4000ms |
| Transition | slide-up 300ms ease-in-out, fade-out 150ms ease-in-out | same |

**Rules:**
- Toasts stack with 8px gap if multiple appear simultaneously.
- No action buttons inside toasts. If the user needs to act, use a modal.
- Success toast: check icon left of message. Error toast: warning icon.

---

## 23. Tooltip

Contextual help — icon hints, truncated text reveal, form field descriptions.

| Property | Light | Dark |
|----------|-------|------|
| Background | `--text1` (`#202223`) | `--surface2` (`#08131C`) |
| Text color | `#FFFFFF` | `--text1` (`#F5F6F6`) |
| Border | none | 1px solid `--border` (`#08131C`) |
| Radius | `--radius-element` (2px) | 2px |
| Padding | `6px 8px` | `6px 8px` |
| Font | Inter 400, 12px | Inter 400, 12px |
| Max width | 240px | 240px |
| Arrow | 6px, `--text1` bg | 6px, `--surface2` bg |
| Shadow | none | none |
| Show delay | 300ms | 300ms |
| Hide delay | 0ms (immediate) | 0ms |
| Transition | opacity 150ms ease-in-out | same |

**Rules:**
- Tooltips appear above the trigger element by default. If viewport edge conflicts, flip below.
- Never put interactive content (links, buttons) inside a tooltip.
- Tooltip text is a short phrase, not a paragraph. Max 2 lines.

---

## 24. Accordion / Collapsible

Expandable content — FAQ sections, product specs, shipping details.

| Property | Light | Dark |
|----------|-------|------|
| Background | `--surface1` (`#FFFFFF`) | `--surface1` (`#0B1A26`) |
| Border (between items) | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Border (outer) | 1px solid `--border` | 1px solid `--border` |
| Radius (outer) | `--radius-component` (16px) | 16px |
| Header padding | `16px 24px` | `16px 24px` |
| Header font | Inter 500, 15px, `--text1` | Inter 500, 15px, `--text1` |
| Header icon | 20px, Phosphor `caret-down` thin, `--text2` | same, `--text2` (`#9EA3AA`) |
| Header icon rotation (open) | 180deg | 180deg |
| Header hover | background `--surface2` (`#EBECEC`) | background `--surface2` (`#08131C`) |
| Body padding | `0 24px 16px 24px` | `0 24px 16px 24px` |
| Body font | Inter 400, 15px, `--text2` | Inter 400, 15px, `--text2` |
| Body max-height transition | 300ms ease-in-out | 300ms ease-in-out |
| Icon rotation transition | 300ms ease-in-out | 300ms ease-in-out |
| Shadow | none | none |

**Rules:**
- Only one item open at a time (single-expand mode) for product pages. FAQ pages may allow multi-expand.
- The outer container has a border and 16px radius. Inner dividers are 1px border, no radius.
- No shadow on the expanded body. Content is visually grouped by padding and border.

---

## 25. List Item

Row in a list — order line items, cart items, search results.

| Property | Light | Dark |
|----------|-------|------|
| Background | `--surface1` (`#FFFFFF`) | `--surface1` (`#0B1A26`) |
| Border (bottom) | 1px solid `--border` (`#D5D8DA`) | 1px solid `--border` (`#08131C`) |
| Padding | `16px 24px` | `16px 24px` |
| Hover | background `--surface2` (`#EBECEC`) | background `--surface2` (`#08131C`) |
| Title | Inter 500, 15px, `--text1` | Inter 500, 15px, `--text1` |
| Subtitle | Inter 400, 13px, `--text2` | Inter 400, 13px, `--text2` |
| Metadata (right) | Inter 400, 15px, `--text2` | Inter 400, 15px, `--text2` |
| Thumbnail | 48px x 48px, `--radius-control` (4px), object-fit cover | same |
| Thumbnail gap | 12px | 12px |
| Shadow | none | none |

**Rules:**
- List items are horizontal rows: thumbnail left, text center, metadata right.
- No border on the last item in a group.
- Clickable list items use hover state. Non-clickable items do not.

---

## 26. Divider

Visual separator — section breaks, content grouping, form field separation.

| Property | Light | Dark |
|----------|-------|------|
| Type | horizontal line | horizontal line |
| Color | `--border` (`#D5D8DA`) | `--border` (`#08131C`) |
| Thickness | 1px | 1px |
| Margin (vertical) | 24px above, 24px below | 24px, 24px |
| Width | 100% (default), 32px (short variant) | same |
| Short variant alignment | center | center |
| Short variant color | `--border-visible` (`#C5C8D1`) | `--border-visible` (`#0B1A26`) |
| Radius | 0 (straight line) | 0 |

**Rules:**
- Use the full-width divider between major sections. Use the short variant (32px centered) between minor content blocks.
- Never use a divider immediately after a heading — use spacing instead.
- Dividers are never decorative. They exist to separate distinct content groups that are not already separated by cards or background changes.

---

## Cross-Component Rules

### Interaction State Consistency

| State | Treatment | Applies to |
|-------|-----------|------------|
| Default | As specified per component | All |
| Hover | Background shifts one step, or accent-subtle fill | Buttons, cards, list items, nav links, tabs |
| Active / Pressed | Background darkens one more step, no scale | Same as hover |
| Focus | 2px solid `--accent` outline, 2px offset | All interactive elements |
| Disabled | opacity 0.4, cursor `not-allowed` | Buttons, inputs, checkboxes, radios, toggles |
| Error | `--error` border or text | Inputs, tags, status indicators |

### Elevation Rule

All components are flat. Depth is created exclusively by:
1. Background color change (`--surface1` on `--background`)
2. 1px border (`--border`)
3. Backdrop overlay (modals)

Shadows are banned at every elevation level. If a component appears to "float," it should be re-examined — it likely needs a border or background adjustment instead.

### Transition Timing

| Context | Duration | Easing |
|---------|----------|--------|
| Color change (hover, focus) | 150ms | ease-in-out |
| Border/outline appearance | 150ms | ease-in-out |
| Content expand (accordion, dropdown) | 300ms | ease-in-out |
| Modal/sheet present | 300ms | ease-in-out |
| Page navigation | 300ms | ease-in-out |
| Emphasis motion (hero transitions) | 500ms | ease-in-out |

### Dark Mode Adjustments

When switching to dark mode, apply these overrides in order:
1. Swap `--background` and all surface tokens (navy palette replaces neutral palette).
2. Swap `--accent` from `#3C69B1` to `#6FCFEB` (teal for visibility on navy).
3. Swap `--text1`/`--text2` (light neutrals replace dark neutrals).
4. Increase backdrop opacity from 0.5 to 0.7 (modals need stronger separation on dark surfaces).
5. Add 1px border on dark-mode toasts and tooltips (they need definition without shadow).
6. Status colors (success, warning, error) remain the same — they are designed for both backgrounds.
