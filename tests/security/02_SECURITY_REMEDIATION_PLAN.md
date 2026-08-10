# SalesGenie Security Remediation Plan

## PRIORITY LEVELS

| Level | Count | Status |
|-------|-------|--------|
| P0 (Critical) | 5 | ✅ Fixed |
| P1 (High) | 5 | ✅ Fixed |
| P2 (Medium) | 4 | ✅ Fixed |
| **Total** | **14** | **✅ All Fixed** |

---

## P0 — CRITICAL FIXES (Release Blockers)

### P0-001: Server-Side Authorization Middleware
**Status:** ✅ Complete

Created `/src/lib/auth-middleware.ts` with:
- `requireAuth()` — validates JWT signature, expiration, audience
- `requirePermission()` — role-based permission matrix
- `requireRole()` — role-based access control
- `isRateLimited()` — per-IP rate limiting
- `logAuditEvent()` — security event audit logging
- `validateId()` — ID format validation
- `sanitizeString()` — XSS/injection sanitization
- `hashPassword()` / `verifyPassword()` — PBKDF2-SHA256
- `validateFileUpload()` — file upload validation

All API routes now import and use these functions.

**Affected files:**
- `src/lib/auth-middleware.ts` (new)
- `src/pages/api/v1/auth/login.ts`
- `src/pages/api/v1/auth/signup.ts`
- `src/pages/api/v1/auth/refresh.ts`
- `src/pages/api/v1/auth/forgot-password.ts`
- `src/pages/api/v1/auth/reset-password.ts`
- `src/pages/api/auth/verify-email.ts`
- `src/pages/api/auth/reset-token/[token].ts`
- `src/pages/api/v1/auth/switch-organization.ts` (new)

---

### P0-002: Secure Password Hashing
**Status:** ✅ Complete

Replaced static-salt string hash with PBKDF2-SHA256:
```typescript
// BEFORE: Trivial string hash
const hash = (salt + password + salt).split('').reduce(...)

// AFTER: PBKDF2-SHA256 with 100k iterations
const hash = pbkdf2Sync(password, randomSalt, 100000, 64, 'sha256')
```

Added password strength requirements:
- Minimum 12 characters
- At least 1 uppercase, 1 lowercase, 1 number, 1 special character
- Maximum 128 characters

**Affected files:**
- `src/lib/auth-middleware.ts` (new)
- `src/pages/api/v1/auth/signup.ts`
- `src/pages/api/v1/auth/reset-password.ts`

---

### P0-003: JWT Signature Verification
**Status:** ✅ Complete

Replaced insecure `atob()` decoding with full validation:
- Algorithm allowlist: `HS256`, `HS384`, `HS512`, `RS256`, `RS384`, `RS512`
- Reject `alg: "none"` and `alg: "None"`
- HMAC signature verification via `crypto.timingSafeEqual`
- Audience validation (must match `window.location.origin`)
- Expiration check with `iat`/`exp` age validation (max 24h)

**Affected files:**
- `src/lib/auth-middleware.ts` (new)
- `src/auth/AuthProvider.tsx`
- `src/auth/OAuthCallback.tsx`

---

### P0-004: MFA Secret Protection
**Status:** ✅ Complete

Removed plaintext MFA secret display:
```typescript
// BEFORE: alert(`MFA Secret: ${mfa.secret_key}`)
// AFTER: Download QR code as SVG file; partial backup code display
```

**Affected files:**
- `src/auth/UserProfile.tsx`

---

### P0-005: Cross-Tenant Isolation
**Status:** ✅ Complete

Created server-side organization switch endpoint that:
1. Validates JWT from request
2. Checks user membership in target tenant
3. Issues new scoped token for new tenant
4. Only returns tenant_id matching the JWT

`AgentBuilder.tsx` now derives `tenant_id` from authenticated user session, not `localStorage`.

**Affected files:**
- `src/pages/api/v1/auth/switch-organization.ts` (new)
- `src/components/islands/AgentBuilder.tsx`
- `src/auth/AuthProvider.tsx`

---

## P1 — HIGH FIXES

### P1-006: Security Headers
**Status:** ✅ Complete

Added to `Layout.astro`:
- `Content-Security-Policy` (default-src, script-src, style-src, img-src, etc.)
- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy` (camera, microphone, geolocation, payment)
- `Strict-Transport-Security`
- `format-detection` meta tag
- `crossorigin="anonymous"` on font CSS

All API routes now return security headers on every response.

### P1-007: Secure Token Storage
**Status:** ✅ Complete

- `secureTokenStorage` is now memory-only in production
- `localStorage` fallback only in development
- All 11 `localStorage.getItem('auth_token')` calls replaced with `getToken()`
- `localStorage.setItem('user_data')` replaced with `secureTokenStorage`

### P1-008: Rate Limiting
**Status:** ✅ Complete

- Auth endpoints: 5 requests/15 minutes per IP (returns 429)
- Password reset: 5 requests/minute per IP
- API endpoints: 100 requests/minute per IP
- Account lockout after 5 failed login attempts (15-min lockout)

### P1-009: OAuth State Validation
**Status:** ✅ Complete

- CSRF state token with `crypto.randomUUID()` nonce
- State stored in secure storage, validated on callback
- State mismatch → rejection
- Provider allowlist: `['google', 'github', 'microsoft', 'slack', 'auth0']`

### P1-010: File Upload Security
**Status:** ✅ Complete

- File type allowlist: `.txt`, `.csv`, `.json`, `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- MIME type validation
- 10MB max file size
- Path traversal detection (rejects `..`, `/`, `\` in filename)

---

## P2 — MEDIUM FIXES

### P2-011: CSRF Protection
**Status:** ✅ Complete
- OAuth state tokens with nonce
- `SameSite=Strict` cookie guidance documented
- Same-origin checks on OAuth callback

### P2-012: Debug Log Removal
**Status:** ✅ Complete
- Removed `console.log('Sessions:', sessions)`
- Removed `console.log('AI Assist results:', data)`
- Removed `console.log('Version:', v)`
- Removed MFA secret from `console.debug`

### P2-013: Generic Error Messages
**Status:** ✅ Complete
- All API routes return generic error messages (`"An error occurred..."`)
- Stack traces never sent to client
- Internal errors logged via audit system only

### P2-014: Audit Logging
**Status:** ✅ Complete
- `logAuditEvent()` function created in `auth-middleware.ts`
- Login success/failure logged
- Signup events logged
- Rate limit events logged
- Org switch events logged
- Token refresh events logged
- MFA setup events logged
- Sensitive data redacted from logs

---

## Regression Tests

```
tests/security/test_security_regression.py
```

59 tests covering every vulnerability category.

```
======================== 59 passed, 1 warning in 0.24s ========================
```

---

## Remaining Hardening (Recommended)

These are recommended for production hardening but not classified as vulnerabilities:

1. **HTTP-only cookies** — Move JWT tokens to `Set-Cookie` with `HttpOnly`, `Secure`, `SameSite=Strict`
2. **Token encryption** — Encrypt refresh tokens in DB at rest
3. **WAF** — Deploy Web Application Firewall
4. **Vulnerability scanning** — Integrate `bandit`, `safety`, `trivy` into CI/CD
5. **Dependency scanning** — Automated CVE scanning for npm packages
6. **CSP nonces** — Use nonce-based script hashes instead of `'unsafe-inline'`
7. **Rate limit storage** — Move in-memory rate limits to Redis for distributed deployments
8. **Professional pentest** — Independent third-party security assessment
