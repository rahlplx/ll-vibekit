# /improve-skill — Improve an Underperforming Skill

## When to Run
After /report shows a skill with low ship rate (<70%) or high PDCA (>2.5).

## Usage
```
/improve-skill skills/saas/migration/SKILL.md
```

This runs: python3 scripts/improve-skill.py skills/saas/migration/SKILL.md

## What It Does
1. Reads the skill's failure_patterns from its metadata
2. Reads recent sessions where this skill was used but feature did not ship
3. Identifies what step caused the failure
4. Suggests specific improvements to the skill's Steps or Rules sections
5. Human reviews suggestion and applies manually (or approves auto-apply)

## Auto-improve all underperforming
```
python3 scripts/improve-skill.py --all-underperforming
```
