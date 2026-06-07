# Diagnose
> Source: mattpocock/skills (119K★)

## WHEN TO USE
Something is broken. You don't know why.

## STEPS
1. Reproduce the error reliably (if you can't reproduce it, you can't fix it)
2. State what you expect vs what actually happens
3. Find the boundary (works here, breaks here)
4. Check git log for recent changes to that boundary
5. Write a test that reproduces the bug
6. Fix the root cause (not the symptom)
7. Confirm test passes

## RULES
- Never fix something you don't understand
- Fix the root cause, not just the surface error
- Add the test to prevent regression
