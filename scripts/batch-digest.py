#!/usr/bin/env python3
"""Batch digest all ll-vibekit source repos.
Usage: python3 scripts/batch-digest.py
Requires: pip install gitingest
"""
import subprocess, sys

REPOS = [
    ("multica-ai/andrej-karpathy-skills", "karpathy"),
    ("affaan-m/ECC",                      "ecc"),
    ("garrytan/gstack",                   "gstack"),
    ("mattpocock/skills",                 "mattpocock"),
    ("addyosmani/agent-skills",           "addy"),
    ("JuliusBrussee/caveman",             "caveman"),
    ("coleam00/context-engineering-intro","ctx-eng"),
    ("popup-studio-ai/bkit-claude-code",  "bkit"),
    ("profullstack/vibe-stack",           "vibe-stack"),
    ("shanraisshan/claude-code-best-practice","shanraisshan"),
    ("withkynam/vibecode-pro-max-kit",    "vibecode-pro"),
    ("sickn33/antigravity-awesome-skills","antigravity"),
]

for repo, name in REPOS:
    url = f"https://github.com/{repo}"
    print(f"  {name}...", end=" ", flush=True)
    r = subprocess.run(["python3","scripts/digest-repo.py", url, name],
                       capture_output=True)
    print("ok" if r.returncode == 0 else f"FAIL: {r.stderr.decode()[:60]}")
