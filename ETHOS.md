# ETHOS.md — Principles and Philosophy
> Source: gstack pattern (garrytan/gstack). The "why" behind the harness.

---

## The Harness is the Bottleneck

In 2026, the model is not the bottleneck. The harness is.
A weak harness turns a powerful model into an unreliable assistant.
A strong harness turns even a mid-tier model into a reliable engineer.

This harness is designed to remove every point of ambiguity that causes
agents to fail: wrong stack choice, wrong pattern, wrong constraint,
wrong assumption.

## Specificity Beats Generality

Generic harnesses fail because agents have to guess too much.
"You are a helpful coding assistant" leaves 10,000 decisions unmade.

ll-vibekit pre-makes those decisions:
- Which language is used for which layer
- Which port connects to which service
- Which framework handles which concern
- Which threshold triggers which action

The agent arrives at a task with most decisions already made.
Its job is implementation, not architecture.

## Non-Technical is the Target User

Rahul (Lab Launchpad founder) codes by directing AI agents.
He describes features in plain English. The harness converts intent to code.

This means:
- INITIAL.md uses plain English (no technical jargon required)
- HUMAN-TODO.md clearly separates what needs a human
- Success criteria are in English, not test syntax
- Error messages explain what to do, not what went wrong

## Memory Must Compound

The #1 failure mode in vibe coding is re-explaining the same context
every session. The agent forgets. The founder re-types. Nothing compounds.

This harness fixes that with:
- WORKING-CONTEXT.md: updated every session with current state
- DISCOVERIES.md: growing list of things learned
- MEMORY/: structured knowledge that survives context compaction

## Token Efficiency is Respect

Long contexts = slow responses = expensive sessions.
We respect the model's context window like we respect RAM.
Only load what the current task needs.
