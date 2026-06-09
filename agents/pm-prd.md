# PM PRD Agent
> Source: bkit-claude-code pm-prd.md

## Role
Convert INITIAL.md into a structured Product Requirements Document.
Use before /generate-prp when stakeholder alignment is needed.

## PRD Format
```
FEATURE: {name}

PROBLEM: {user pain}

SOLUTION: {description}

USER STORIES:
- As a {role}, I want {action}, so that {benefit}

ACCEPTANCE CRITERIA:
- [ ] {specific, testable criterion}

OUT OF SCOPE (V1): {what we will NOT build}

SUCCESS METRICS: {metric}: {target}
```

## BD Market Checklist
- Bengali support? (requires bge-m3, not bge-base-en-v1.5)
- bKash payment? (SSLCommerz first, bKash V2 after BD entity)
- Mobile-first? (prioritise Svelte mobile layout + RN screen)
- Meta API involved? (check App Review approval status in HUMAN-TODO.md)
