# Git Workflow
> Source: addyosmani/agent-skills (48K★), mattpocock/skills (119K★)

## BRANCH NAMING
feature/{ticket}-description
fix/{ticket}-description
chore/{description}

## COMMIT FORMAT
type(scope): description

Types: feat | fix | chore | docs | test | refactor | perf
Examples:
  feat(content): add Bengali voice generation via MPT
  fix(hitl): correct expiry trigger when final_content is NULL
  chore(deps): update pydantic-ai to 0.0.46

## RULES
- One logical change per commit
- Never commit: .env files, node_modules, __pycache__
- Always run pre-commit-check.sh before committing
- Squash before merging to main
