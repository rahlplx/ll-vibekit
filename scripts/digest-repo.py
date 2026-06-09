#!/usr/bin/env python3
"""Digest a GitHub repo using gitingest.
Usage: python3 scripts/digest-repo.py https://github.com/owner/repo [name]
Requires: pip install gitingest
"""
import sys, os
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/digest-repo.py <url> [name]")
        sys.exit(1)
    url = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else url.split("/")[-1]
    out = Path("digests") / f"{name}.txt"
    out.parent.mkdir(exist_ok=True)

    try:
        from gitingest import ingest
    except ImportError:
        print("Install: pip install gitingest")
        sys.exit(1)

    print(f'Digesting {url}...')
    result = ingest(url, max_file_size=30_000,
        exclude_patterns=["*.lock","*.sum","node_modules/*","dist/*",
                          "*.min.js","*.min.css","*.png","*.jpg","*.gif"])

    text = '\n\n'.join(str(r) for r in result if r) if isinstance(result, tuple) else str(result)
    out.write_text(f"SOURCE: {url}\n\n{text}")
    print(f'Saved: {out} ({out.stat().st_size:,} bytes)')

if __name__ == '__main__':
    main()
