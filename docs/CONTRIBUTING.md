# Contributing to ll-vibekit

## Add a Skill
1. Copy SKILL.md.tmpl → skills/{category}/{name}/SKILL.md
2. Fill: When to Use, Steps, Output Format, Rules
3. Add entry to docs/SKILLS-REGISTRY.md
4. Test on a real task
5. PR: skill file + registry update + test result

## Add an Agent
1. Create agents/{name}.md
2. Include: Role, Responsibilities, Stack Knowledge, Rules, Output Format
3. Add to AGENTS.md agent table
4. Test: activate agent on real task

## Update MEMORY files
- stack.md: when tech decisions change
- patterns.md: when new code pattern confirmed
- mistakes.md: when pitfall encountered
- modules.md: when new module ships

## Source Attribution Rule
Every file from an external repo must start with:
`> Source: {repo-name} ({stars}★)`

## Evaluate New Repos First
```bash
gitingest https://github.com/owner/repo -o /tmp/digest.txt
# Read digest first, understand patterns, then add
# See docs/GITINGEST.md for full workflow
```
