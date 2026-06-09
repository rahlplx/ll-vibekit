#!/usr/bin/env python3
"""Validate all SKILL.md files have required sections."""
from pathlib import Path

REQUIRED = ['## When to Use', '## WHEN TO USE', '## PATTERN', '## Steps', '## STEPS']
errors = 0

for skill in sorted(Path('skills').rglob('SKILL.md')):
    content = skill.read_text()
    has_when = any(r in content for r in REQUIRED[:3])
    has_steps = any(r in content for r in REQUIRED[3:])
    size = len(content)
    issues = []
    if not has_when: issues.append('missing When to Use')
    if not has_steps: issues.append('missing Steps')
    if size < 200: issues.append(f'stub ({size} chars)')
    if issues:
        print(f'  FAIL {skill}: {", ".join(issues)}')
        errors += 1
    else:
        print(f'  ok   {skill}')

print(f'\nDone. {errors} issues found.')
raise SystemExit(errors)
