# /review

Review the changes in $ARGUMENTS (file path or "staged").

Check against:
1. DECISIONS.md — any violations? List them.
2. Karpathy Rule 3 — any changes outside stated scope?
3. Karpathy Rule 2 — any over-engineering?
4. Project patterns (memory/patterns.md) — consistent?
5. Tests — success criteria verifiable?

Output:
- PASS: ready to commit
- FAIL: list specific issues, suggest fixes

Source: addyosmani/agent-skills code-review skill
