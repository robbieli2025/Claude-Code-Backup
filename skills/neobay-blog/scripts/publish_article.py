#!/usr/bin/env python3
"""
Neobay Blog Article Publisher

Handles the complete publishing workflow:
  extract  - Parse metadata from a draft markdown file
  convert  - Convert markdown draft to HTML
  publish  - Publish article to Shopify via Admin API
  faq-schema - Create/update FAQ schema metafield for an article

Usage:
  python3 publish_article.py extract blog-drafts/2026-05-13-slug.md
  python3 publish_article.py convert blog-drafts/2026-05-13-slug.md --output /tmp/body.html
  python3 publish_article.py publish --draft blog-drafts/2026-05-13-slug.md --blog-id 90090766434 --token $TOKEN
  python3 publish_article.py faq-schema --article-id 564555219042 --draft blog-drafts/2026-05-13-slug.md --token $TOKEN
"""

import sys
import json
import re
import os
import argparse
import subprocess
import mimetypes
import urllib.request
from pathlib import Path
from typing import Optional, Dict, List

try:
    import markdown
except ImportError:
    print("Installing markdown library...")
    subprocess.run([sys.executable, "-m", "pip", "install", "markdown"], check=True)
    import markdown


# ---------------------------------------------------------------------------
# Markdown draft parsing
# ---------------------------------------------------------------------------

def parse_draft(filepath: str) -> Dict:
    """Parse a Neobay blog draft file and return structured metadata + body."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('\n---\n')
    header_section = parts[0]

    # --- Extract metadata from header ---
    # H1 title (first # line)
    title_match = re.search(r'^# (.+)$', header_section, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else None

    # SEO metadata
    title_tag = _extract_field(header_section, 'Title Tag')
    meta_description = _extract_field(header_section, 'Meta Description')
    url_slug = _extract_field(header_section, 'URL Slug')
    if url_slug:
        url_slug = url_slug.strip('`').rstrip('/').split('/')[-1]

    # --- Extract body (CRITICAL: parts[1:-1], NOT parts[-1]) ---
    if len(parts) >= 3:
        body_md = '\n---\n'.join(parts[1:-1])
        sources_md = parts[-1]
    elif len(parts) == 2:
        body_md = parts[1]
        sources_md = ''
    else:
        body_md = ''
        sources_md = ''

    return {
        'title': title,
        'title_tag': title_tag,
        'meta_description': meta_description,
        'slug': url_slug,
        'body_markdown': body_md,
        'sources_markdown': sources_md,
    }


def _extract_field(text: str, field_name: str) -> Optional[str]:
    """Extract a **Field Name**: value from the metadata section."""
    pattern = rf'\*\*{re.escape(field_name)}\*\*:\s*(.+)'
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None


# ---------------------------------------------------------------------------
# Markdown → HTML conversion
# ---------------------------------------------------------------------------

def convert_to_html(body_md: str, sources_md: str = '') -> str:
    """Convert markdown body and sources to HTML."""
    md = markdown.Markdown(extensions=['extra'])
    html_parts = []
    if body_md:
        html_parts.append(md.convert(body_md))
    if sources_md:
        html_parts.append(md.convert(sources_md))
    return '\n'.join(html_parts)


# ---------------------------------------------------------------------------
# FAQ schema extraction
# ---------------------------------------------------------------------------

def extract_faq_schema(body_md: str) -> List[Dict]:
    """Extract FAQ items from markdown body, return list of Question/Answer dicts."""
    faq_match = re.search(
        r'## Frequently Asked Questions\n\n(.*?)(?=\n## What to Do Next)',
        body_md, re.DOTALL
    )
    if not faq_match:
        faq_match = re.search(
            r'## Frequently Asked Questions(.+?)## What to Do Next',
            body_md, re.DOTALL
        )

    if not faq_match:
        return []

    faq_text = faq_match.group(1)
    qa_blocks = re.split(r'\n### ', faq_text)
    items = []

    for block in qa_blocks:
        block = block.strip()
        if not block:
            continue
        # Split on first newline after question line (may be \n\n or \n)
        parts = block.split('\n\n', 1)
        if len(parts) < 2:
            # Fallback: split on first \n after the question line
            newline_pos = block.find('\n')
            if newline_pos > 0:
                parts = [block[:newline_pos], block[newline_pos+1:]]
        if len(parts) >= 2:
            question = re.sub(r'^###\s*', '', parts[0].strip())
            answer = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', parts[1].strip())
            items.append({
                '@type': 'Question',
                'name': question,
                'acceptedAnswer': {
                    '@type': 'Answer',
                    'text': answer
                }
            })

    return items


def build_faq_schema_json(body_md: str) -> str:
    """Build complete FAQPage JSON-LD schema string."""
    items = extract_faq_schema(body_md)
    schema = {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        'mainEntity': items
    }
    return json.dumps(schema, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Shopify API helpers
# ---------------------------------------------------------------------------

def shopify_api(store: str, token: str, method: str, path: str, data: Optional[Dict] = None) -> Dict:
    """Make a Shopify Admin API call."""
    url = f"https://{store}/admin/api/2024-01/{path}"
    cmd = ['curl', '-s', '-X', method, url,
           '-H', f'X-Shopify-Access-Token: {token}']

    if data:
        cmd.extend(['-H', 'Content-Type: application/json', '-d', json.dumps(data)])

    result = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {'_raw': result.stdout, '_error': result.stderr}


def publish_article(draft_path: str, blog_id: str, store: str, token: str,
                    featured_image_path: Optional[str] = None,
                    body_image_paths: Optional[List[str]] = None) -> Dict:
    """Full publish workflow: parse draft, convert, upload images to Shopify Files, POST to Shopify."""
    # 1. Parse draft
    meta = parse_draft(draft_path)
    if not meta['title']:
        return {'error': 'Could not extract title from draft'}

    # 2. Convert to HTML
    body_html = convert_to_html(meta['body_markdown'], meta['sources_markdown'])

    # 3. Upload images to Shopify Files (not base64)
    featured_url = None
    if featured_image_path and os.path.exists(featured_image_path):
        print(f"Uploading featured image to Shopify Files...")
        featured_url = _upload_to_shopify_files(featured_image_path, store, token)

    if body_image_paths:
        print(f"Uploading {len(body_image_paths)} body image(s) to Shopify Files...")
        body_html = _insert_body_images(body_html, body_image_paths, store, token)

    # 4. Build article payload
    article_data = {
        'title': meta['title'],
        'body_html': body_html,
        'author': 'Peter Jonathan',
        'summary_html': meta.get('meta_description', ''),
        'tags': _determine_tags(meta),
        'metafields': [
            {'namespace': 'global', 'key': 'title_tag', 'value': meta.get('title_tag', meta['title']), 'type': 'single_line_text_field'},
            {'namespace': 'global', 'key': 'description_tag', 'value': meta.get('meta_description', ''), 'type': 'single_line_text_field'},
            {'namespace': 'custom', 'key': 'author_name', 'value': 'Peter Jonathan', 'type': 'single_line_text_field'},
        ]
    }

    if meta['slug']:
        article_data['handle'] = meta['slug']

    if featured_url:
        article_data['image'] = {'src': featured_url}

    payload = {'article': article_data}

    # 5. POST to Shopify
    resp = shopify_api(store, token, 'POST',
                       f"blogs/{blog_id}/articles.json", payload)

    return resp


def create_faq_metafield(article_id: str, draft_path: str, store: str, token: str) -> Dict:
    """Extract FAQ from draft and create the seo.faq_schema metafield."""
    meta = parse_draft(draft_path)
    schema_json = build_faq_schema_json(meta['body_markdown'])
    items = extract_faq_schema(meta['body_markdown'])

    if not items:
        return {'error': 'No FAQ items found in draft'}

    payload = {
        'metafield': {
            'namespace': 'seo',
            'key': 'faq_schema',
            'value': schema_json,
            'type': 'json'
        }
    }

    resp = shopify_api(store, token, 'POST',
                       f"articles/{article_id}/metafields.json", payload)
    return resp


# ---------------------------------------------------------------------------
# Shopify Files upload (replaces base64 embedding)
# ---------------------------------------------------------------------------

STAGED_UPLOADS_MUTATION = """
mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $input) {
    stagedTargets { url resourceUrl parameters { name value } }
    userErrors { field message }
  }
}
"""


def _guess_mime(filepath: str) -> str:
    mime, _ = mimetypes.guess_type(filepath)
    if mime and mime.startswith("image/"):
        return mime
    ext = os.path.splitext(filepath)[1].lower()
    return {
        ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".png": "image/png", ".gif": "image/gif",
        ".webp": "image/webp",
    }.get(ext, "image/jpeg")


def _upload_to_shopify_files(filepath: str, store: str, token: str) -> Optional[str]:
    """Upload an image to Shopify Files via stagedUploadsCreate. Returns CDN URL."""
    if not os.path.exists(filepath):
        print(f"  Warning: image not found: {filepath}", file=sys.stderr)
        return None

    filename = os.path.basename(filepath)
    mime_type = _guess_mime(filepath)
    file_size = os.path.getsize(filepath)

    gql_url = f"https://{store}/admin/api/2024-01/graphql.json"
    gql_body = json.dumps({
        "query": STAGED_UPLOADS_MUTATION,
        "variables": {"input": [{
            "resource": "FILE",
            "filename": filename,
            "mimeType": mime_type,
            "httpMethod": "POST",
            "fileSize": file_size,
        }]}
    }).encode("utf-8")

    req = urllib.request.Request(gql_url, data=gql_body, method="POST")
    req.add_header("X-Shopify-Access-Token", token)
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
    except Exception as e:
        print(f"  Upload error (stagedUploadsCreate): {e}", file=sys.stderr)
        return None

    staged = result.get("data", {}).get("stagedUploadsCreate", {})
    if staged.get("userErrors"):
        for err in staged["userErrors"]:
            print(f"  Staged upload error: {err}", file=sys.stderr)
        return None

    targets = staged.get("stagedTargets", [])
    if not targets:
        return None

    target = targets[0]
    upload_url = target["url"]
    resource_url = target["resourceUrl"]
    params = target.get("parameters", [])

    # Multipart POST to staged URL
    boundary = "----ShopifyFormBoundary" + os.urandom(16).hex()
    parts = []
    for p in params:
        parts.append(f"--{boundary}".encode())
        parts.append(f'Content-Disposition: form-data; name="{p["name"]}"'.encode())
        parts.append(b"")
        parts.append(p["value"].encode())

    with open(filepath, "rb") as f:
        file_data = f.read()

    parts.append(f"--{boundary}".encode())
    parts.append(f'Content-Disposition: form-data; name="file"; filename="{filename}"'.encode())
    parts.append(f"Content-Type: {mime_type}".encode())
    parts.append(b"")
    parts.append(file_data)
    parts.append(f"--{boundary}--".encode())

    body = b"\r\n".join(parts)
    req2 = urllib.request.Request(upload_url, data=body, method="POST")
    req2.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")

    try:
        with urllib.request.urlopen(req2, timeout=60) as resp:
            if resp.status in (200, 201, 204):
                return resource_url
    except Exception as e:
        print(f"  Upload failed (PUT to staged URL): {e}", file=sys.stderr)

    return None


def _insert_body_images(body_html: str, image_paths: List[str],
                        store: str, token: str) -> str:
    """Upload body images to Shopify Files and insert CDN URLs in body HTML."""
    # Upload all images first
    cdn_urls = []
    for path in image_paths:
        if not os.path.exists(path):
            print(f"  Warning: skipping missing file: {path}", file=sys.stderr)
            continue
        url = _upload_to_shopify_files(path, store, token)
        if url:
            cdn_urls.append(url)
        else:
            print(f"  Warning: failed to upload {path}", file=sys.stderr)

    if not cdn_urls:
        return body_html

    # Build img tags with CDN URLs
    img_tags = []
    for i, url in enumerate(cdn_urls):
        fname = os.path.basename(image_paths[i]) if i < len(image_paths) else "image"
        alt = fname.replace("-", " ").replace(".jpg", "").replace("_", " ")
        img_tags.append(
            f'<p style="text-align:center">'
            f'<img src="{url}" alt="{alt}" '
            f'style="max-width:100%;height:auto;border-radius:8px" loading="lazy">'
            f'</p>'
        )

    # Insert at natural break points
    h2_closing_tags = list(re.finditer(r'</h2>', body_html))
    what_to_do = body_html.find('What to Do Next')

    insertions = []
    if len(img_tags) >= 1 and len(h2_closing_tags) >= 2:
        idx = h2_closing_tags[1].end()
        next_p = body_html.find('</p>', idx)
        if next_p > 0:
            insertions.append((next_p + 4, img_tags[0]))

    if len(img_tags) >= 2 and what_to_do > 0:
        insertions.append((what_to_do, img_tags[1]))

    if len(img_tags) >= 3:
        mid = len(body_html) // 2
        mid_p = body_html.find('</p>', mid)
        if mid_p > 0:
            insertions.append((mid_p + 4, img_tags[2]))

    for pos, tag in sorted(insertions, reverse=True):
        body_html = body_html[:pos] + '\n' + tag + '\n' + body_html[pos:]

    return body_html


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _determine_tags(meta: Dict) -> str:
    """Determine appropriate tags based on article content. Default to cat health."""
    title = (meta.get('title') or '').lower()
    tags = ['cat health']

    if 'asthma' in title:
        tags.append('feline asthma')
    if any(w in title for w in ['inhaler', 'spacer', 'chamber', 'medication', 'inhaled']):
        tags.extend(['cat inhaler', 'spacer chamber', 'inhaled medication'])
    if 'breathe' in title or 'breathing' in title:
        tags.append('cat breathing')

    seen = set()
    unique = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            unique.append(t)

    return ', '.join(unique[:5])


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Neobay Blog Article Publisher')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # extract
    p_extract = subparsers.add_parser('extract', help='Parse metadata from draft')
    p_extract.add_argument('draft', help='Path to draft markdown file')

    # convert
    p_convert = subparsers.add_parser('convert', help='Convert draft to HTML')
    p_convert.add_argument('draft', help='Path to draft markdown file')
    p_convert.add_argument('--output', '-o', help='Output file path (prints to stdout if omitted)')

    # publish
    p_publish = subparsers.add_parser('publish', help='Publish article to Shopify')
    p_publish.add_argument('--draft', required=True, help='Path to draft markdown file')
    p_publish.add_argument('--blog-id', required=True, help='Shopify blog ID')
    p_publish.add_argument('--token', required=True, help='Shopify Admin API token')
    p_publish.add_argument('--store', default='neobaypet.myshopify.com', help='Shopify store domain')
    p_publish.add_argument('--featured-image', help='Path to featured image (JPEG)')
    p_publish.add_argument('--body-images', help='Comma-separated paths to body images')

    # faq-schema
    p_faq = subparsers.add_parser('faq-schema', help='Create FAQ schema metafield')
    p_faq.add_argument('--article-id', required=True, help='Shopify article ID')
    p_faq.add_argument('--draft', required=True, help='Path to draft markdown file')
    p_faq.add_argument('--token', required=True, help='Shopify Admin API token')
    p_faq.add_argument('--store', default='neobaypet.myshopify.com', help='Shopify store domain')

    args = parser.parse_args()

    if args.command == 'extract':
        meta = parse_draft(args.draft)
        print(json.dumps({
            'title': meta['title'],
            'title_tag': meta['title_tag'],
            'meta_description': meta['meta_description'],
            'slug': meta['slug'],
            'body_length': len(meta['body_markdown']),
            'has_sources': bool(meta['sources_markdown'].strip()),
        }, ensure_ascii=False, indent=2))

    elif args.command == 'convert':
        meta = parse_draft(args.draft)
        html = convert_to_html(meta['body_markdown'], meta['sources_markdown'])
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"HTML written to {args.output} ({len(html)} chars)")
        else:
            print(html)

    elif args.command == 'publish':
        body_images = args.body_images.split(',') if args.body_images else []
        resp = publish_article(
            draft_path=args.draft,
            blog_id=args.blog_id,
            store=args.store,
            token=args.token,
            featured_image_path=args.featured_image,
            body_image_paths=body_images,
        )

        if 'article' in resp:
            a = resp['article']
            print(json.dumps({
                'status': 'published',
                'id': a['id'],
                'title': a['title'],
                'handle': a['handle'],
                'blog_id': a['blog_id'],
                'has_image': bool(a.get('image')),
                'body_html_length': len(a.get('body_html', '')),
            }, ensure_ascii=False, indent=2))
        elif 'errors' in resp:
            print(json.dumps({'status': 'error', 'errors': resp['errors']}, ensure_ascii=False, indent=2))
        else:
            print(json.dumps({'status': 'unknown', 'response': resp}, ensure_ascii=False, indent=2))

    elif args.command == 'faq-schema':
        resp = create_faq_metafield(
            article_id=args.article_id,
            draft_path=args.draft,
            store=args.store,
            token=args.token,
        )
        if 'metafield' in resp:
            schema = json.loads(resp['metafield']['value'])
            print(json.dumps({
                'status': 'created',
                'metafield_id': resp['metafield']['id'],
                'faq_count': len(schema.get('mainEntity', [])),
            }, ensure_ascii=False, indent=2))
        else:
            print(json.dumps({'status': 'error', 'response': resp}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
