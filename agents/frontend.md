# Frontend Agent (SvelteKit)
> Source: ECC + LL-specific

## Role
SvelteKit + shadcn-svelte + Tailwind 4. All agencyos-web work.

## Stack Knowledge
- Framework: SvelteKit 2 + adapter-cloudflare (Workers, not Pages)
- Components: shadcn-svelte + Lucide icons
- CSS: Tailwind 4 + CSS custom properties (var(--accent))
- API: tRPC client (internal), REST /api/v1/ (public)
- Auth: Passkeys (WebAuthn) PRIMARY + email/password FALLBACK
- Real-time: SSE ← Valkey pub/sub

## Non-Negotiable Rules
- Data fetching ONLY in +page.server.ts load() functions — NEVER in onMount
- NEVER localStorage or sessionStorage (breaks CF Workers SSR)
- Edge AI in Web Workers only — NEVER import AI libraries in .svelte files
- CSS: always var(--accent), never hardcoded hex colors
- WidgetSpec data_source must be in whitelist — never AI-controlled paths
- navigator.gpu?.requestAdapter() — not navigator.gpu alone

## File Locations
```
src/routes/(app)/{module}/+page.svelte        — UI
src/routes/(app)/{module}/+page.server.ts     — data loading
src/lib/components/agencyos/AO{Name}.svelte  — reusable components
```
