# /generate-prp

Read INITIAL.md or the file at $ARGUMENTS.

1. Read DECISIONS.md fully first. Any conflict = flag [DECISION CONFLICT].
2. Read existing code in the relevant module/route/expert.
3. Write PRPs/{feature-name}.md with:
   - Goal (one sentence)
   - Success criteria (testable, specific)
   - What NOT to change
   - Files to create/modify (exact paths)
   - Implementation order
   - Edge cases (minimum 3)
4. Stop. Do not implement. Say: "PRP written. Review it. Run /execute-prp PRPs/name.md"

Source: coleam00/context-engineering-intro
