# Security Checklist
> Source: addy-skills/references/security-checklist.md

Run before every feature ships.

## Authentication
- [ ] Passkeys implemented (primary)
- [ ] Email/password fallback (mandatory for BD Android)
- [ ] JWT tokens: httpOnly cookie, 15min expiry
- [ ] Refresh tokens: stored in DB with revocation
- [ ] MFA (TOTP) for admin roles

## Authorization
- [ ] RBAC via rbac.Can() — no hardcoded role names
- [ ] RLS on all tenant tables
- [ ] API key scope validation

## Data Protection
- [ ] Vault: AES-256-GCM for sensitive credentials
- [ ] Audit log: append-only, 7-year retention
- [ ] IP hashed after 90 days (GDPR)
- [ ] Soft delete only (GDPR erasure via anonymization)

## Input Validation
- [ ] All inputs validated (go-playground/validator)
- [ ] SQL: sqlc parameterized (never string concat)
- [ ] File uploads: type + size limits

## AI-Specific
- [ ] PII scrubber runs before LLM calls
- [ ] WidgetSpec data_source whitelisted
- [ ] BYOK keys in Vault, not DB plain text
- [ ] A2A calls require X-AgencyOS-Tenant header
