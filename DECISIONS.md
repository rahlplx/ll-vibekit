# DECISIONS.md — Lab Launchpad
> Locked technical decisions. When any doc contradicts this: THIS WINS.
> Update only after deliberate team decision. Never auto-updated by agents.

---

## Quick decision tree

Q: Which embedding model for RAG?
A: BAAI/bge-m3 ALWAYS. 1024-dim. Never bge-base-en-v1.5 (English-only).

Q: How does frontend call backend?
A: REST HTTP with auth header. Never gRPC on CF Workers (no TCP).

Q: Real-time updates?
A: SSE + Valkey pub/sub. Never WebSockets. Never PG LISTEN/NOTIFY.

Q: Database delete?
A: is_deleted=true ONLY. Never DELETE FROM.

Q: Auth method?
A: Passkeys (WebAuthn) PRIMARY + email/password FALLBACK (mandatory).

Q: Auto-approve threshold?
A: 0.95 confidence. Never 0.90 (models are overconfident).

Q: Agent framework for complex HITL?
A: LangGraph (interrupt()). 

Q: Agent framework for simple single calls?
A: Agno (10,000x faster than LangGraph).

Q: LLM gateway?
A: LiteLLM. BYOK always. Never hardcode provider keys.

Q: Token reduction?
A: Use caveman-compress SKILL for markdown. Use rtk for CLI output compression.

---

## Full decision log
See: agencyos-api/DECISIONS.md for full AgencyOS-specific decisions.
