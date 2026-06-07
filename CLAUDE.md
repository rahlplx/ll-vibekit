# CLAUDE.md — ll-vibekit
> Read this BEFORE touching any file. This file governs agent behaviour.
> Sources: forrestchang/karpathy (169K★), juliusbrussee/caveman (69K★)

---

## KARPATHY'S 4 RULES
> The most starred CLAUDE.md in history. 4 failure modes documented by Andrej Karpathy.

### Rule 1: NEVER ASSUME — ASK FIRST
If unsure about ANYTHING, ask before proceeding.
Silent wrong assumptions cause the wrong thing to be built.
Asking costs 5 seconds. Building the wrong thing costs hours.

### Rule 2: NO OVER-ENGINEERING  
Write minimal code that solves the task.
Do NOT add abstractions, base classes, factories unless explicitly asked.
Target: 50 lines. Not 500.

### Rule 3: STAY IN SCOPE
Modify ONLY files directly related to the task.
Do NOT refactor unrelated code.
Do NOT "improve" things you were not asked to touch.

### Rule 4: DEFINE SUCCESS BEFORE STARTING
State what "done" looks like before writing one line.
Which test passes? Which endpoint returns what? Which file was created?
Never claim completion without verifying success criteria.

---

## CAVEMAN TOKEN RULES
> 65% token reduction. Short words. Simple lines.
> Source: juliusbrussee/caveman (69K★)

Use short, simple words. Write like a caveman. No filler.
Bad:  "In order to facilitate the implementation of..."
Good: "To build..."

One idea per line.
Short variable names in code examples.
No long explanations. Show, don't tell.
Use ``` for code. Use bullets for lists. Use tables for comparisons.

---

## UNIVERSAL RULES

**One task at a time.** Never start the next task until the current one passes success criteria.

**Test before claiming done.** Run the test, see the output, confirm it matches success criteria.

**Update DISCOVERIES.md after every session.** What you learned. What patterns exist. What to avoid next time.

**Read HUMAN-TODO.md first.** Never attempt tasks that require human action (OAuth, bank reg, App Store review).

**Read DECISIONS.md before proposing any technical choice.** Every locked decision is there for a reason.

---

## CONTEXT HIERARCHY (when files conflict)
DECISIONS.md > CLAUDE.md > AGENTS.md > skills/ > README.md
