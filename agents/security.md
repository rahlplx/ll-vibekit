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
