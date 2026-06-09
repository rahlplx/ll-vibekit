# SaaS Auth Flow
> Standard auth implementation for Lab Launchpad SaaS products

## WHEN TO USE
Building auth for any LL SaaS product.

## PATTERN
1. Passkeys (WebAuthn) — PRIMARY
2. Email + password — MANDATORY FALLBACK (50-60% BD Android lacks passkey support)
3. TOTP — mandatory for owner + admin roles on email/password path

## IMPLEMENTATION
```
Registration: passkey preferred → email+password as backup
Login: try passkey → "Use email instead" link always visible
MFA: TOTP on email+password path for privileged roles
JWT: 15min access + 7d refresh, httpOnly cookie
Session: stored in DB, deleted on logout/expiry
```

## NEVER
- Passkey-only (locks out BD Android users)
- Store plain passwords (bcrypt minimum)
- JWT in localStorage (XSS risk)

---

## Skill Metadata
<!-- Auto-managed by scripts/eval-skills.py — do not edit manually -->

```yaml
version: "1.0"
source: "ll-vibekit (LL-specific)"
created: "2026-06-09"
last_improved: "never"
improvement_trigger: "avg_pdca_when_used > 2.5 OR ship_rate < 70%"

# Populated by eval-session.py after each use
stats:
  times_used: 0
  features_shipped_after_use: 0
  avg_pdca_iterations_when_used: 0.0
  ship_rate_when_used: "0%"
  last_used: "never"

# Auto-populated by scripts/eval-skills.py
failure_patterns: []

# Manual + auto improvement history
improvement_log:
  - version: "1.0"
    date: "2026-06-09"
    change: "Initial version"
    source: "ll-vibekit (LL-specific)"
```

## Eval Criteria
<!-- What does success look like when this skill is used? -->
- Feature ships on first PDCA Check attempt
- No DECISIONS.md violations in generated code
- Implementation matches PRP scope exactly
- No errors in build/test commands after use
