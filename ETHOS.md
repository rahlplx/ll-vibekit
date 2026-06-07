# ETHOS.md — ll-vibekit
> Why this harness exists and how to use it.
> Adapted from: garrytan/gstack (107K★)

## The philosophy

This harness encodes decisions so you don't have to make them every time.
The agent reads this once. The decisions are made. Build the product.

Great software comes from clear constraints. This harness IS the constraints.

## What "agentic engineering" means

Old way: write code → hope it's right → debug → repeat
New way: write spec → agent implements → hooks validate → ship

The bottleneck is not the model. The bottleneck is the harness.
Poor context = poor output. Rich context = production-grade output.

## The 3 laws of this harness

1. **Spec before code.** Never implement without an approved PRP or INITIAL.md.
2. **Verify before done.** Never claim completion without running success criteria.
3. **Document what you learn.** DISCOVERIES.md compounds over time.

## Non-negotiables

- DECISIONS.md is law. If it says bge-m3, you use bge-m3.
- HUMAN-TODO.md is a wall. Never attempt tasks on that list.
- One thing at a time. Parallel tasks create context drift.
