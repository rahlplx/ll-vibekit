# /discover — Update Knowledge Base
> Run after shipping a feature to keep memory current.

## Steps

1. Read DISCOVERIES.md (create if missing)
2. Append what was learned this session:
   ```
   ## {date} — {feature-name}
   BUILT: {what shipped}
   LEARNED: {new patterns or pitfalls}
   ```
3. If a new code pattern was confirmed:
   → Update MEMORY/patterns.md (note: MEMORY/ uppercase)
4. If a new module or route was added:
   → Update MEMORY/modules.md
5. If a mistake was made and fixed:
   → Update MEMORY/mistakes.md
6. If a human task was completed:
   → Update HUMAN-TODO.md (check the box)
7. Update WORKING-CONTEXT.md "Active Sprint" section

## IMPORTANT: path is MEMORY/ (uppercase)
Not memory/ (lowercase). On Linux/Oracle ARM these are different directories.
Always use: MEMORY/patterns.md, MEMORY/modules.md, MEMORY/mistakes.md

## Keep entries short
One paragraph per entry maximum.
Date-stamp every entry: YYYY-MM-DD format.
