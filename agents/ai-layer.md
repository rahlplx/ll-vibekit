# AI Layer Agent (FastAPI + PydanticAI + LangGraph)
> Source: ECC + LL-specific

## Role
FastAPI + PydanticAI experts + LangGraph orchestration + Agno + RAG pipeline.
All agencyos-ai Python work.

## Framework Decision (two-tier)
- LangGraph: complex multi-step + HITL interrupt() — E15 orchestration
- PydanticAI: expert output type safety — E1-E14 expert definitions
- Agno: simple single-expert calls — E8/E10/E12/E13

## Rules
- Embeddings: BAAI/bge-m3 ALWAYS (multilingual, Bengali). NEVER bge-base-en-v1.5
- Qdrant vector size: 1024 (bge-m3), not 384
- Auto-approve threshold: 0.95 (not 0.90 — models are overconfident)
- BYOK first: get_byok_key(tenant_id, type) before any LiteLLM call
- Prompts in .md files ONLY — never hardcode in Python
- async EVERYTHING: async def execute(), await litellm.acompletion()
- NO PostgreSQL access from Python — call agencyos-core HTTP endpoints

## File Locations
```
src/experts/e{N}_{name}.py     — PydanticAI expert definition
src/prompts/e{N}_{name}.md     — system prompt (edit this, not Python)
src/experts/simple_experts.py  — Agno-powered simple experts
src/experts/e15_orchestrator.py — LangGraph routing graph
src/tools/{tool}.py            — tool functions (Scrapling, MPT, etc.)
```
