# /eval-prp — Score a PRP Before Executing

## When to Run
BEFORE running /execute-prp. Catches weak PRPs early.
A PRP scoring below 70 will likely drift or fail.

## Usage
```
/eval-prp PRPs/feature-name.md
```

This runs: python3 scripts/eval-prp.py PRPs/feature-name.md

## Scoring
- 90-100: Excellent — execute immediately
- 80-89:  Good — minor gaps, acceptable
- 70-79:  Acceptable — review failed checks
- 60-69:  Weak — improve before executing
- <60:    Poor — DO NOT execute, rewrite PRP

## What Gets Checked
- Has clear goal sentence
- Has verifiable success criteria (checkboxes with test commands)
- Criteria are specific (not vague like 'it works')
- Has scope boundaries (files NOT in scope)
- Has numbered implementation order
- Has edge cases (minimum 3)
- Has DECISIONS.md compliance checklist
- References .vibekit.json test_commands
