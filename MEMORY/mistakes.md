# MEMORY/mistakes.md
> Anti-patterns specific to THIS project.
> Add entries whenever something goes wrong and is fixed.
> Prevents repeating the same mistakes.

---

## Format
Each entry:
```
### {date} — {brief title}
WRONG: {what was done wrong}
RIGHT: {the correct approach}
WHY:   {why the wrong approach fails}
```

---

## Universal Anti-Patterns (all projects)

### Silent assumption
WRONG: Assuming what the user wants without asking
RIGHT: Ask one clarifying question before proceeding
WHY:   Wrong assumptions build the wrong thing

### Over-engineering
WRONG: Building abstractions before they're needed
RIGHT: Simplest possible solution that works
WHY:   Code you don't need is code you have to maintain

### Skipping PDCA Check
WRONG: Marking a task done without testing success criteria
RIGHT: Test every criterion explicitly before closing
WHY:   Agent drift — implementation diverges from spec unnoticed

### Loading all context files
WRONG: Loading CLAUDE.md + CONTEXT.md + all MEMORY/ + all agents/ at session start
RIGHT: Load PROJECT.md + WORKING-CONTEXT.md only, load others on demand
WHY:   Wastes 60-70% of context budget on irrelevant content

---

## Project-Specific Mistakes

<!-- Add YOUR project's discovered mistakes here -->
{MISTAKES_WILL_ACCUMULATE_HERE}
