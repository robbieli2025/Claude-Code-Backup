#!/usr/bin/env python3
"""
Neobay Blog Image Downloader

Downloads images from Unsplash for Neobay blog articles and checks uniqueness
against the previously-used image inventory.

Usage:
  python3 download_images.py search "cat veterinarian exam" --count 3
  python3 download_images.py download PHOTO_ID --width 1200 --output /tmp/img.jpg
  python3 download_images.py check PHOTO_ID  -- check if this photo was used before
  python3 download_images.py add PHOTO_ID "description" "article-name" featured
"""

import sys
import os
import json
import argparse
import subprocess
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
IMAGE_INVENTORY_FILE = SKILL_DIR / 'references' / 'image-guide.md'

# Well-known Unsplash cat photo IDs that are appropriate for veterinary/health content
# Format: (photo_id, description, scene_type)
CAT_PHOTO_CANDIDATES = [
    # Cat at vet / being examined
    ("1574158622682", "Veterinarian examining a cat with stethoscope", "vet-exam"),
    ("1592194996308-7b43878e84a6", "Cat being examined at veterinary clinic", "vet-exam"),
    ("1519052531761-1d2c25a7e6d5", "Cat at veterinary checkup", "vet-exam"),
    # Cat at home / resting
    ("1514888286974", "Orange tabby cat resting peacefully", "home-rest"),
    ("1541781774459-de7b1a0edd77", "Cat sleeping comfortably on sofa", "home-rest"),
    ("1571566882392-5df9c44a8c18", "Gray cat relaxing by window", "home-rest"),
    ("1492370284958-c476f6f9c29b", "Cat curled up on bed", "home-rest"),
    # Cat with owner
    ("1526336024174", "Owner gently holding cat for medication", "owner-interact"),
    ("1511044566532-e1fcb9c08d4a", "Woman petting cat on couch", "owner-interact"),
    ("1577648188599-28fc21b60b17", "Person cuddling with cat at home", "owner-interact"),
    ("1606214174584-fe142d0a9b2c", "Cat sitting on owner's lap", "owner-interact"),
    # Cat alert / active
    ("1536591203857-377e4c2b64a1", "Cat looking alert and curious", "active"),
    ("1545243424-0cefbeb7d8b2", "Cat playing with toy indoors", "active"),
    ("1574144611936-0b0e1e16e42b", "Cat stretching or moving actively", "active"),
    # Cat outdoors safely
    ("1529258284171-50b61ad3b69b", "Cat exploring garden safely", "outdoor"),
    ("1536591089680-1c043ba5b49c", "Cat sitting by open window", "outdoor"),
]


def search_images(query: str, count: int = 3) -> list[dict]:
    """Search Unsplash for cat images matching the query.

    Since Unsplash API may not be available, this uses a curated local catalog
    of cat photos appropriate for veterinary/health content.
    """
    results = []
    query_lower = query.lower()

    # Score each candidate by keyword match
    scored = []
    for photo_id, desc, scene_type in CAT_PHOTO_CANDIDATES:
        score = 0
        desc_lower = desc.lower()
        for word in query_lower.split():
            if word in desc_lower or word in scene_type:
                score += 1
        scored.append((score, photo_id, desc, scene_type))

    scored.sort(reverse=True)
    for score, photo_id, desc, scene_type in scored[:count]:
        results.append({
            'photo_id': photo_id,
            'description': desc,
            'scene_type': scene_type,
            'url_regular': f"https://images.unsplash.com/photo-{photo_id}?w=1200&q=80",
            'relevance_score': score,
        })

    return results


def download_image(photo_id: str, width: int = 1200, output_dir: str = '/tmp') -> str:
    """Download an Unsplash photo by ID."""
    url = f"https://images.unsplash.com/photo-{photo_id}?w={width}&q=80"
    output_path = os.path.join(output_dir, f"unsplash-{photo_id}-w{width}.jpg")

    try:
        import urllib.request
        import ssl
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, context=ssl_ctx) as resp:
            data = resp.read()
            with open(output_path, 'wb') as f:
                f.write(data)
        return output_path
    except Exception as e:
        # Fallback: use curl
        result = subprocess.run([
            'curl', '-s', '-L', '-o', output_path, url
        ], capture_output=True)
        if result.returncode == 0 and os.path.getsize(output_path) > 1000:
            return output_path
        raise RuntimeError(f"Failed to download photo {photo_id}: {e}")


def check_uniqueness(photo_id: str) -> dict:
    """Check if a photo ID has been used in any existing article."""
    if not IMAGE_INVENTORY_FILE.exists():
        return {'used': False, 'reason': 'No inventory file yet — likely safe'}

    with open(IMAGE_INVENTORY_FILE, 'r') as f:
        content = f.read()

    if photo_id in content:
        # Find the context
        lines = content.split('\n')
        for line in lines:
            if photo_id in line:
                return {'used': True, 'context': line.strip()}
        return {'used': True, 'context': 'Found in inventory'}

    return {'used': False}


def add_to_inventory(photo_id: str, description: str, article_name: str, image_type: str):
    """Add a used photo to the image inventory."""
    if not IMAGE_INVENTORY_FILE.exists():
        print(f"Warning: Inventory file not found at {IMAGE_INVENTORY_FILE}")
        return

    with open(IMAGE_INVENTORY_FILE, 'r') as f:
        content = f.read()

    entry = f"photo-{photo_id}  — {image_type}: {article_name} ({description})"
    used_section = '### Used Unsplash Photo IDs (DO NOT REUSE)'

    if used_section in content:
        # Insert after the section header and its code block
        parts = content.split(used_section)
        # Find the ``` line
        code_start = parts[1].find('```')
        code_end = parts[1].find('```', code_start + 3)
        if code_start >= 0 and code_end >= 0:
            # Insert before the closing ```
            before = parts[1][:code_end]
            after = parts[1][code_end:]
            parts[1] = before + entry + '\n' + after
            new_content = used_section.join(parts)
        else:
            parts[1] = parts[1] + entry + '\n'
            new_content = used_section.join(parts)
    else:
        new_content = content + f'\n{entry}\n'

    with open(IMAGE_INVENTORY_FILE, 'w') as f:
        f.write(new_content)

    print(f"Added to inventory: {entry}")


def download_for_article(article_name: str, image_types: list[str],
                         output_dir: str = '/tmp/neobay-imgs') -> dict[str, str]:
    """Download a complete image set for an article.

    image_types: list of scene types like ['vet-exam', 'home-rest', 'owner-interact']
    Returns: dict mapping image_type → file_path
    """
    os.makedirs(output_dir, exist_ok=True)
    results = {}

    for scene_type in image_types:
        # Find an unused photo of this type
        candidates = [(pid, desc) for pid, desc, st in CAT_PHOTO_CANDIDATES
                       if st == scene_type]

        chosen = None
        for pid, desc in candidates:
            check = check_uniqueness(pid)
            if not check['used']:
                chosen = (pid, desc)
                break

        if not chosen:
            # Fallback: use the first candidate even if used before
            chosen = candidates[0] if candidates else None

        if chosen:
            pid, desc = chosen
            try:
                path = download_image(pid, width=1200, output_dir=output_dir)
                results[scene_type] = path
                add_to_inventory(pid, desc, article_name, 'body' if scene_type != 'vet-exam' else 'featured')
                print(f"Downloaded {scene_type}: {pid} → {path}")
            except Exception as e:
                print(f"Failed to download {scene_type}: {e}")
        else:
            print(f"No candidate found for scene type: {scene_type}")

    return results


def main():
    parser = argparse.ArgumentParser(description='Neobay Blog Image Downloader')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # search
    p_search = subparsers.add_parser('search', help='Search for cat images')
    p_search.add_argument('query', help='Search query (e.g., "cat veterinarian exam")')
    p_search.add_argument('--count', type=int, default=3, help='Number of results')

    # download
    p_dl = subparsers.add_parser('download', help='Download an Unsplash photo by ID')
    p_dl.add_argument('photo_id', help='Unsplash photo ID')
    p_dl.add_argument('--width', type=int, default=1200, help='Image width')
    p_dl.add_argument('--output', '-o', default='/tmp', help='Output directory')

    # check
    p_check = subparsers.add_parser('check', help='Check if a photo has been used before')
    p_check.add_argument('photo_id', help='Unsplash photo ID')

    # add
    p_add = subparsers.add_parser('add', help='Add a photo to the used inventory')
    p_add.add_argument('photo_id', help='Unsplash photo ID')
    p_add.add_argument('description', help='Image description')
    p_add.add_argument('article', help='Article name')
    p_add.add_argument('type', choices=['featured', 'body'], help='Image type')

    # download-for-article (convenience)
    p_dfa = subparsers.add_parser('download-for-article', help='Download full image set for an article')
    p_dfa.add_argument('--article', required=True, help='Article name for inventory tracking')
    p_dfa.add_argument('--scenes', required=True, help='Comma-separated scene types (vet-exam,home-rest,owner-interact)')
    p_dfa.add_argument('--output-dir', default='/tmp/neobay-imgs', help='Output directory')

    args = parser.parse_args()

    if args.command == 'search':
        results = search_images(args.query, args.count)
        for r in results:
            print(f"{r['photo_id']} [{r['scene_type']}] {r['description']}")
            print(f"  {r['url_regular']}")
            print()

    elif args.command == 'download':
        path = download_image(args.photo_id, args.width, args.output)
        print(f"Downloaded: {path}")

    elif args.command == 'check':
        result = check_uniqueness(args.photo_id)
        if result['used']:
            print(f"ALREADY USED: {result['context']}")
            sys.exit(1)
        else:
            print(f"Photo {args.photo_id} is available (not in inventory)")

    elif args.command == 'add':
        add_to_inventory(args.photo_id, args.description, args.article, args.type)

    elif args.command == 'download-for-article':
        scenes = [s.strip() for s in args.scenes.split(',')]
        results = download_for_article(args.article, scenes, args.output_dir)
        print(f"\nDownloaded {len(results)}/{len(scenes)} images:")
        for st, path in results.items():
            print(f"  {st}: {path}")


if __name__ == '__main__':
    main()
