# process/ — Feature Lifecycle Management
> Source: withkynam/vibecode-pro-max-kit process/ pattern

## Folders
```
process/features/backlog/   — ideas not started
process/features/active/    — currently building
process/features/completed/ — shipped
process/general-plans/      — multi-sprint roadmap
```

## Workflow
```
Idea → backlog/  → (sprint starts) → active/  → (ships) → completed/
```

## Create a Feature
```bash
cp -r process/_seeds/feature-template/ process/features/backlog/my-feature/
nano process/features/backlog/my-feature/PLAN.md
```

## Files Per Feature
- PLAN.md — what and why
- PROGRESS.md — current status and blockers
- REFERENCES.md — related PRPs, decisions, code links
- REPORT.md — final summary after shipping
