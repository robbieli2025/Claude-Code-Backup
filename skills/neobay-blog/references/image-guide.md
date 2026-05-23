# Image Guide — Neobay Blog

## Image Specifications

| Type | Dimensions | Format | Source | Count per Article |
|------|-----------|--------|--------|-------------------|
| Featured (Hero) | 1200 × 675 | JPEG | Unsplash / Pexels | 1 |
| Body illustration | ≤1064 × 598 | JPEG | Unsplash / Pexels | 2-3 |

**Important:** Body images are constrained by theme CSS to `max-width: 1064px; max-height: 598px`. Download images at 1200px width and let the CSS constrain the display size. On mobile (<768px), images are full-width.

## Image Sourcing Protocol

### Featured Image Selection

1. Search Unsplash for the article's primary visual concept
2. Download at 1200px width (`?w=1200` parameter)
3. **Verify uniqueness** against the Image Inventory below — SAME photo ID = reject
4. Alt text: Descriptive, includes article topic keywords, 5-10 words

### Body Image Selection

1. Choose 2-3 images that illustrate different aspects of the article
2. **Scene diversity requirement:** Each image must show a distinctly different scene
3. **Good scene types for cat health articles:**
   - Cat at home (on couch, by window, on cat tree, in bed)
   - Cat at veterinarian clinic (being examined, owner + vet + cat)
   - Cat interacting with owner (being held, being petted, playing)
   - Cat relaxing/sleeping (content, healthy, peaceful)
   - Cat outdoors safely (in garden, on leash, looking out window)
4. **Never use:** Same cat twice, same scene type twice, obviously stock-photo poses

### Alt Text Rules

- Descriptive of what's IN the image, not the article topic
- Include "cat" as the subject
- 5-10 words
- Natural English, not keyword stuffing

```
✅ "Orange tabby cat resting peacefully on a sunny windowsill"
✅ "Veterinarian examining a gray cat with a stethoscope in a clinic"
❌ "feline asthma inhaler spacer chamber cat health blog image"
❌ "cat"
```

## Uniqueness Verification (Critical)

**Rule:** The featured image for every new article MUST be a photo that has never been used as a featured image or body image in any existing Neobay article.

**Verification process:**
1. After choosing an Unsplash photo, note its photo ID (from the URL: `photo-XXXXXXXXX`)
2. Check the Image Inventory below — is this photo ID listed? If yes, choose a different photo
3. Also visually check: does this look very similar to an existing featured image? If yes, choose a different photo
4. After confirming uniqueness, add to the inventory

## Image Upload — Shopify Files (Required)

**All images must go through Shopify Files.** Never embed base64 data URIs or use external CDN URLs (Unsplash, Flickr, etc.) directly in blog articles.

### Workflow

```
1. Download image from Unsplash/Pexels → local file
2. Upload to Shopify Files via scripts/shopify_files_upload.py
3. Use the returned Shopify CDN URL in blog body <img> tags or article.image.src
```

### Upload command

```bash
# Single image
python3 scripts/shopify_files_upload.py /tmp/hero.jpg

# Multiple images
python3 scripts/shopify_files_upload.py /tmp/hero.jpg /tmp/body1.jpg /tmp/body2.jpg
```

Output: Shopify CDN URL like `https://cdn.shopify.com/s/files/1/0656/7546/0706/files/hero_abc123.jpg?v=...`

### Featured image

Set `article.image.src` to the Shopify CDN URL (not `article.image.attachment` with base64):

```python
article["image"] = {"src": "https://cdn.shopify.com/s/files/..."}
```

### Body images

Use the Shopify CDN URL directly in HTML:

```html
<img src="https://cdn.shopify.com/s/files/..." alt="Descriptive alt text" loading="lazy">
```

### Token requirement

API token must have **`write_files`** scope for `stagedUploadsCreate` mutation. Without it, file uploads will fail.

## Image Inventory

### Current Featured Images

| Article | Unsplash Photo ID | Description |
|---------|-------------------|-------------|
| Why Does My Cat Cough After Running? | (check published article) | Cat mid-run / playing |
| Feline Asthma vs. Hairball | (check published article) | Cat coughing / health |
| What Is a Cat Inhaler Spacer? | (check published article) | Cat with medical equipment |
| How Vets Diagnose Feline Asthma | (check published article) | Cat at veterinarian |
| Common Triggers | (check published article) | Home environment / cat |
| AeroKat vs Neobay | (check published article) | Cat with spacer device |
| Cat Breathing Fast While Sleeping | (check published article) | Cat sleeping |
| Train Cat to Accept Inhaler Mask | (check published article) | Cat being handled / trained |
| Real Cat Owner Story | (check published article) | Happy cat with owner |
| Can Cats Use Human Inhalers? | photo-1574158622682 | Cat at veterinarian exam |
| How to Administer Inhaled Medication | (check published article) | Cat receiving treatment |
| Cat Flu or Feline Asthma? | photo-1592194996308 | Cat at veterinarian exam |
| 5 Signs Spacer Isn't Working | loremflickr (Flickr CDN, not Unsplash) | Cat resting at home |

### Current Body Images

| Article | Scene Types Used |
|---------|-----------------|
| Can Cats Use Human Inhalers? | Cat receiving medication indoors, healthy cat resting at home |
| Cat Flu or Feline Asthma? | Shopify CDN (3 images: varied cat/home/vet scenes) |
| Cat Gasping for Air? | Shopify CDN (Pexels: cat at vet, cat resting, owner with cat) |
| 5 Signs Spacer Isn't Working | Cat at veterinary clinic, cat resting at home by window |

### Used Unsplash Photo IDs (DO NOT REUSE)

```
photo-1574158622682  — featured: Can Cats Use Human Inhalers? (cat at vet)
photo-1526336024174  — body: Can Cats Use Human Inhalers? (cat with medication)
photo-1514888286974  — body: Can Cats Use Human Inhalers? (cat resting)
photo-1592194996308  — featured: Cat Flu or Feline Asthma? (cat at veterinary exam)
```

### Used Pexels Photo IDs (DO NOT REUSE)

```
pexels-7469240  — featured: Cat Gasping for Air? (cat at veterinarian for breathing exam)
pexels-6231932  — body: Cat Gasping for Air? (cat resting peacefully at home)
pexels-6816852  — body: Cat Gasping for Air? (owner petting cat on couch)
```

**Note:** This inventory is incomplete for earlier articles. Before downloading any image, do a fresh check against all published article featured images via the Shopify API. When you use a new photo, add it to this list immediately.
