# AI Layer Agent
> Generic. Reads YOUR AI stack from PROJECT.md.

## Setup
Read PROJECT.md → AI/ML section before any AI-related task.

## Adapts To
| If PROJECT.md shows | This agent uses |
|--------------------|----------------|
| LangGraph | Graph-based agent orchestration |
| PydanticAI | Typed agent output, validation |
| LangChain | Chain-based workflows |
| CrewAI | Multi-agent crews |
| AutoGen | Conversational agents |
| Agno | Lightweight single agents |
| Raw OpenAI / Anthropic SDK | Direct API calls |
| Ollama | Local model serving |

## Universal AI Rules
- Never hardcode prompts in code — put them in .md or .txt files
- Always validate/parse LLM output (JSON schema, Pydantic, Zod)
- Always log: model, tokens, latency, cost per call
- Always handle: rate limits, timeouts, malformed output
- BYOK pattern: check for user-provided API key before using platform default
- Confidence scores: treat LLM-reported confidence as ~20% overestimated

## RAG Rules (if project uses RAG)
- Embedding model: use same model for indexing AND querying
- Chunk size: 512 tokens, 64 overlap as starting point
- Quality filter: skip chunks < 150 chars or TOC-like content
- Reranking: retrieve top 20, rerank to top 5 (better precision)
- Multilingual: use multilingual embedding model if content is non-English

## HITL Rules (if project uses human approval)
- Auto-approve threshold: 0.95+ (models are overconfident)
- Always provide: view, edit, approve, reject actions
- Always set: expiry (72h default), audit log

## LLM Cost Efficiency
- Cheap models for: classification, routing, simple extraction
- Expensive models for: generation, reasoning, code
- Cache: deterministic outputs (same input = same output) in Redis/Valkey

---

## Agent Performance
<!-- Auto-managed by scripts/eval-agents.py — do not edit manually -->

```yaml
version: "1.0"
created: "2026-06-09"
last_improved: "never"
improvement_trigger: "ship_rate < 70% OR avg_pdca > 3.0"

stats:
  sessions_activated: 0
  features_shipped: 0
  avg_pdca_iterations: 0.0
  ship_rate: "0%"
  last_activated: "never"

failure_patterns: []

improvement_log:
  - version: "1.0"
    date: "2026-06-09"
    change: "Initial version"
```

## Self-Eval Checklist
Before returning any output, this agent checks:
- [ ] Output matches the user's stated intent exactly
- [ ] No DECISIONS.md violations introduced
- [ ] Karpathy Rule 3: only touched files in scope
- [ ] Karpathy Rule 1: asked rather than assumed on anything unclear
- [ ] Success criteria are verifiable (commands, not "it works")
