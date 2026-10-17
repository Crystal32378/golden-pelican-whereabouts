#!/usr/bin/env python3
"""Generate root-page WebP thumbnails without changing source artwork.

Requires Pillow. Run from any directory: python3 tools/gen_thumbnails.py
Full-resolution PNG/JPEG files remain the targets of the image links.
"""
from pathlib import Path
import re
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]

def generate():
    html = (ROOT / 'index.html').read_text()
    posters = sorted(set(re.findall(r'href="(posters/[^"<>]+\.jpg)"', html)))
    # Also accept the pre-optimization markup so this can bootstrap a clean copy.
    posters += sorted(set(re.findall(r'src="(posters/[^"<>]+\.jpg)"', html)) - set(posters))
    sources = sorted((ROOT / 'postcards').glob('*.png'))
    sources += [ROOT / name for name in posters]
    original_bytes = thumbnail_bytes = 0
    for source in sources:
        relative = source.relative_to(ROOT)
        target = ROOT / 'thumbs' / relative.with_suffix('.webp')
        target.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(source) as raw:
            image = ImageOps.exif_transpose(raw).convert('RGB')
            image.thumbnail((640, 640), Image.Resampling.LANCZOS)
            image.save(target, 'WEBP', quality=88 if relative.parts[0] == 'posters' else 80, method=6)
        original_bytes += source.stat().st_size
        thumbnail_bytes += target.stat().st_size
    print(f'{len(sources)} thumbnails: {original_bytes:,} → {thumbnail_bytes:,} bytes')

if __name__ == '__main__':
    generate()
