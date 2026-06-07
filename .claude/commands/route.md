# /route

Read the request at $ARGUMENTS or from the current prompt.

CLASSIFY intent:
- build-feature | fix-bug | add-ai-feature | db-change | deploy | review | mobile

IDENTIFY scope:
- full-stack | api-only | ui-only | ai-only | mobile-android | mobile-ios | infra

SELECT agents: (print which agents will be used)

SELECT skills: (print which skills apply from skills/)

SET phase: 1-discover → 2-plan → 3-implement → 4-verify → 5-document

DECISION CHECKS: list any DECISIONS.md items relevant to this request

OUTPUT:
```
INTENT: {intent}
SCOPE: {scope}  
AGENTS: {list}
SKILLS: {list}
PHASE: {phase}
CHECKS: {decisions}
NEXT: /generate-prp INITIAL.md
```
