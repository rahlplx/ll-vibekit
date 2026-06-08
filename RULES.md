# RULES.md — Explicit Non-Negotiable Rules
> Source: ECC pattern. Hard rules the agent MUST follow.

---

## RULE 1: Read CLAUDE.md First
Every session starts by reading CLAUDE.md. No exceptions.
If CLAUDE.md has not been read, stop and read it before anything else.

## RULE 2: DECISIONS.md is the Tiebreaker
When any two files contradict each other on a technical choice:
DECISIONS.md wins. Always. No exceptions.

## RULE 3: Never Assume — Ask
From Karpathy: "If you are not sure about something, ask before proceeding."
Silent assumptions are the #1 cause of failed agent sessions.

## RULE 4: Check HUMAN-TODO.md Before Starting
Some tasks require humans (OAuth, bank registration, App Store submission).
If the task is on HUMAN-TODO.md: tell the human, don't attempt it yourself.

## RULE 5: Verify Success Criteria Before Closing
Never mark a task complete without explicitly verifying the success criteria
from the PRP. State what you tested and what the result was.

## RULE 6: WORKING-CONTEXT.md Updates Each Session
At the end of every session, update WORKING-CONTEXT.md with:
- What was accomplished
- What was left incomplete
- What decisions were made
- What the next session should start with

## RULE 7: Token Budget Awareness
When context is large, apply caveman compression:
- Write terse, short responses unless detail is requested
- Summarize long code sections instead of repeating them
- Use /caveman skill when token budget is under pressure

## RULE 8: Stack-Specific Rules Per Product
For AgencyOS: read agencyos-api/DECISIONS.md before ANY AgencyOS task.
For mobile: read android/SETUP.md or ios/SETUP.md before mobile tasks.
For new products: read docs/PRODUCTS.md to understand scope.

## RULE 9: Soft Delete Only
When working in ANY database context: never DELETE FROM. Always is_deleted=true.

## RULE 10: Mobile is First Class
Mobile apps (Android + iOS) are not afterthoughts.
Every UI decision must consider: does this work on a 375px screen with touch?
