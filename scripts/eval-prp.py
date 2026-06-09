#!/usr/bin/env python3
"""eval-prp.py -- Score a PRP before execution (0-100).
Usage: python3 scripts/eval-prp.py PRPs/feature.md
"""
import sys, re
from pathlib import Path

CHECKS = [
    ("has_goal",       [r"## Goal", r"## What"],           15, "Add ## Goal section"),
    ("has_criteria",   [r"- \[ \]", r"Success Criteria"], 20, "Add ## Success Criteria with checkboxes"),
    ("criteria_spec",  [r"exit 0|returns \d{3}|pnpm|pytest|go test"], 15, "Make criteria specific with commands"),
    ("has_scope",      [r"NOT in scope|NOT to change|Files NOT"], 15, "Add Files NOT in scope section"),
    ("has_order",      [r"## Implementation Order|## Steps"],   10, "Add numbered Implementation Order"),
    ("has_edge_cases", [r"## Edge|edge case"],               10, "Add ## Edge Cases (min 3)"),
    ("has_decisions",  [r"DECISIONS|decisions\.md"],        10, "Add DECISIONS.md compliance checklist"),
    ("has_commands",   [r"vibekit|test_commands|goose|go build|pnpm build|pytest"], 5, "Reference test commands"),
]

def grade(s): return ("A -- Excellent",90) if s>=90 else ("B -- Good",80) if s>=80 else ("C -- OK",70) if s>=70 else ("D -- Weak",60) if s>=60 else ("F -- Rewrite",0)

def main():
    if len(sys.argv) < 2: print("Usage: python3 scripts/eval-prp.py PRPs/feature.md"); sys.exit(1)
    path = sys.argv[1]
    if not Path(path).exists(): print(f"Not found: {path}"); sys.exit(1)
    content = Path(path).read_text()
    score, passed, failed = 0, [], []
    for name, patterns, weight, fix in CHECKS:
        if any(re.search(p, content, re.I | re.M) for p in patterns):
            score += weight; passed.append(name)
        else: failed.append((name, fix))
    label, _ = grade(score)
    print(f"\nPRP: {path}\nScore: {score}/100 -- {label}\n")
    if passed: print(f"PASSED ({len(passed)}):"); [print(f"  + {p}") for p in passed]
    if failed:
        print(f"\nFIX THESE ({len(failed)}):")
        for name, fix in failed: print(f"  - {name}: {fix}")
    print()
    if score >= 80: print(f"Ready: /execute-prp {path}")
    else: print("Improve the PRP first, then re-run this eval.")
    sys.exit(0 if score >= 70 else 1)

if __name__ == "__main__": main()
