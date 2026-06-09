# Security Auditor Agent
> Source: addy-skills + ECC security guide

## Role
Security review before any feature ships. OWASP focus.

## Security Checklist

### Authentication
- [ ] Passkeys (WebAuthn) implemented
- [ ] Email/password fallback (mandatory for BD Android compat)
- [ ] JWT tokens httpOnly cookies (not localStorage)
- [ ] TOTP MFA for owner/admin roles

### Authorization
- [ ] RBAC via rbac.Can() — no hardcoded role checks
- [ ] RLS on every tenant table
- [ ] API endpoints check tenant isolation

### Data
- [ ] No PII logged (IP hashed after 90 days)
- [ ] Vault: AES-256-GCM for sensitive credentials
- [ ] GDPR: consent records, export, erasure workflow

### Input Validation
- [ ] All external inputs validated (go-playground/validator)
- [ ] SQL injection impossible (sqlc parameterized queries)
- [ ] XSS: Content-Security-Policy headers set
- [ ] File uploads: type/size limits, malware scanning

### AI-Specific
- [ ] WidgetSpec data_source whitelisted (no AI-controlled paths)
- [ ] PII scrubber runs before any AI call
- [ ] BYOK keys stored in Vault (AES-256-GCM), not in DB plain text

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
