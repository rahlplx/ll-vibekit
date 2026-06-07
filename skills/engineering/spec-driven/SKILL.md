# Spec-Driven Development
> Source: addyosmani/agent-skills (48K★), coleam00/context-engineering-intro

## WHEN TO USE
Any new feature. Always write the spec before writing code.

## STEPS
1. Write INITIAL.md describing the feature
2. Run /generate-prp INITIAL.md
3. Review PRP — approve or request changes
4. Run /execute-prp PRPs/name.md
5. Verify all success criteria
6. Update DISCOVERIES.md

## THE KEY RULE
Never implement without an approved PRP.
"We'll figure it out as we go" = context drift = wrong product.
