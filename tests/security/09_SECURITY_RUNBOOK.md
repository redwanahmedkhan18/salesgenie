# SalesGenie Security Runbook

## Incident Response Procedure

### 1. Security Event Detection
Security events are detected via:
- Audit logs (`logAuditEvent` in `src/lib/auth-middleware.ts`)
- Rate limit violations (429 responses)
- Authentication failures (401 responses)
- Authorization failures (403 responses)
- Suspicious input patterns (rate limiter, validation failures)

### 2. Triage and Escalation
| Severity | Response Time | Actions |
|---|---|---|
| Critical (P0) | 5 minutes | Page security team, isolate affected services |
| High (P1) | 30 minutes | Create incident ticket, investigate |
| Medium (P2) | 4 hours | Log, investigate during business hours |
| Low (P3) | 24 hours | Log, review in weekly security sync |

### 3. Containment
- **Auth compromise:** Revoke all sessions, force token refresh, rotate JWT secret
- **Cross-tenant access:** Disable affected API routes, audit all tenant_id usage
- **File upload exploit:** Quarantine uploaded files, scan all recent uploads
- **Rate limit bypass:** Tighten rate limits, add CAPTCHA on auth endpoints
- **OAuth compromise:** Revoke OAuth client secrets, rotate integration tokens

### 4. Eradication
- Patch vulnerable code
- Rotate any exposed credentials
- Add regression test to prevent recurrence
- Re-run security test suite

### 5. Recovery
- Deploy fix to staging
- Run full regression test suite
- Gradual rollout to production
- Monitor audit logs for 24 hours

### 6. Post-Incident Review
- Root cause analysis
- Update threat model
- Add preventive controls
- Update runbook

---

## Detection Rules

### Rule 1: Brute-Force Login Detection
```
IF login_failed count > 5 from same IP within 15 minutes
THEN log severity=high, alert security team
```
**Implementation:** `isAuthRateLimited()` in `auth-middleware.ts`

### Rule 2: Cross-Tenant Access Detection
```
IF requirePermission returns 403 due to tenant mismatch
THEN log severity=critical, alert immediately
```

### Rule 3: Rate Limit Bypass Detection
```
IF 429 responses > 100 from same IP within 1 minute
THEN log severity=medium, flag for review
```

### Rule 4: Suspicious OAuth Pattern
```
IF OAuth callback received with state mismatch
THEN log severity=high, block provider
```

---

## Forensic Procedures

### Collecting Evidence
1. **Audit logs:** `logAuditEvent()` calls capture all security-relevant events
2. **Error logs:** Application errors (sanitized — no PII/tokens)
3. **Access logs:** API gateway access logs
4. **Rate limit logs:** Rate limit violation records

### Log Redaction Policy
**NEVER log:**
- `password` — passwords are never logged
- `auth_token` — tokens redacted by `useErrorReporting.ts`
- `refresh_token` — tokens redacted by `useErrorReporting.ts`
- `secret_key` — secrets are never logged
- API keys
- Private keys
- Full credit card numbers

**Safe to log:**
- User IDs (non-PII)
- Email addresses (for audit trail)
- Timestamps
- IP addresses
- Action types
- Resource IDs
- Error types (not messages)

### Correlation IDs
All requests through the Astro API gateway should include a correlation ID header (`x-correlation-id`). This allows stitching together the full attack chain across microservices.

---

## Emergency Procedures

### Emergency: Active Cross-Tenant Data Breach
1. Run: `python3 -m pytest tests/security/ -v` — verify isolation controls
2. Check audit logs for `cross-tenant` events
3. Disable affected API routes in `src/pages/api/v1/`
4. Force all users to re-authenticate (invalidate all JWTs)
5. Contact security team

### Emergency: Authentication Bypass Discovered
1. Verify JWT secret is rotated: `requireNewJWTSecret()`
2. Check all API routes use `requireAuth()`
3. Verify no `atob()` JWT decoding remains
4. Deploy fix within 1 hour

### Emergency: Credential Exposure
1. Revoke exposed credential immediately
2. Rotate replacement credential
3. Search Git history: `git log -p --all -S "secret_value"`
4. Update `tests/security/test_security_regression.py::TestNoSecretsInCode`
5. Scan all services for exposed credentials

---

## Recovery Checklist

After any security incident:

- [ ] All vulnerabilities patched
- [ ] Security regression tests pass (59/59)
- [ ] Audit logs reviewed for related events
- [ ] Rate limits adjusted if bypass found
- [ ] JWT secret rotated if forged tokens detected
- [ ] OAuth clients rotated if compromise suspected
- [ ] File uploads scanned if upload exploit found
- [ ] All users notified if PII exposed
- [ ] Incident report filed
- [ ] Threat model updated
- [ ] Runbook updated
- [ ] Post-mortem completed

---

## Contact Information

| Role | Contact |
|---|---|
| Security Team | security@salesgenie.ai |
| On-Call Engineer | See PagerDuty |
| Incident Commander | security-incident@salesgenie.ai |

---

## Security Test Commands

```bash
# Run all security regression tests
python3 -m pytest tests/security/test_security_regression.py -v

# Run specific vulnerability test
python3 -m pytest tests/security/test_security_regression.py::TestJWTValidation -v

# Run TypeScript type checking
npx astro check

# Check for secrets in code
# (Recommended: integrate trufflehog or gitleaks into CI)
grep -rn "password\s*=\|secret\s*=\|api_key\s*=" src/ --include="*.ts" --include="*.tsx" | grep -v node_modules
```
