# SalesGenie Threat Model

## STRIDE Threat Model

| Threat | Description | Mitigation | Priority |
|---|---|---|---|
| **Spoofing** | Attacker forges JWT with elevated roles | PBKDF2 password hashing, JWT HMAC signature verification, algorithm allowlist | P0 |
| **Tampering** | Attacker modifies tenant_id, role claims | Role allowlist validation, server-side tenant derivation from JWT | P0 |
| **Repudiation** | User denies actions, no audit trail | Audit logging for all security events (login, switch org, admin actions) | P1 |
| **Information Disclosure** | Stack traces, tokens in errors/logs | Generic error messages, secure token storage, sensitive data redaction | P1 |
| **Denial of Service** | Brute-force login, mass uploads, API abuse | Rate limiting per IP, account lockout, file size limits | P1 |
| **Elevation of Privilege** | End user escalates to admin | JWT signature validation, role allowlist, server-side permission checks | P0 |

---

## PASTA Risk Analysis

### Phase 1: Business Objectives
- AI-powered multi-tenant customer support & sales platform
- Must isolate organization data
- Must prevent unauthorized AI actions
- Must protect customer data

### Phase 2: Application Layer
```
[Internet] → [CDN/Proxy] → [Astro API GW] → [Microservices]
                                          → [External APIs]
                                          → [Database/Redis/Vector DB]
```

### Phase 3: Threat Analysis

| Asset | Threat Agent | Vulnerability | Impact |
|---|---|---|---|
| User passwords | Attacker w/ DB access | Weak hash | Full account takeover |
| JWT tokens | Attacker w/ forged token | No signature check | Privilege escalation |
| Tenant data | Authenticated Tenant B user | Client-controlled tenant_id | Cross-tenant data breach |
| API endpoints | Any internet user | No auth | Data exfiltration |
| File uploads | Authenticated user | No validation | RCE, XSS |
| OAuth flow | Attacker | No CSRF state | Account takeover |
| MFA secrets | Anyone viewing screen | alert() display | MFA bypass |

### Phase 4: Vulnerability Analysis

**High-risk combinations:**
1. No JWT signature verification + client-controlled roles = trivial privilege escalation
2. No server-side rate limiting + weak password hashing = brute-force account takeover
3. Client-controlled tenant_id + no server-side tenant validation = cross-tenant data breach
4. No file upload validation + RAG pipeline = malicious document ingestion → prompt injection → data exfiltration

### Phase 5: Attack Modeling

**Attack Path 1: Authentication Bypass**
```
Attacker → POST /api/v1/auth/login (no rate limit) → Brute-force weak hashes → Access account
```
**Mitigation:** Rate limiting (5/15min), PBKDF2 hashing, account lockout

**Attack Path 2: JWT Forgery**
```
Attacker → Forge JWT with roles=["super_admin"] → Decode with atob() → Access admin panel
```
**Mitigation:** HMAC signature verification, algorithm allowlist, audience validation

**Attack Path 3: Cross-Tenant Access**
```
Attacker (Tenant A) → localStorage.tenant_id = "tenant_b" → API returns Tenant B data
```
**Mitigation:** Server-side tenant_id from JWT, org switch membership validation

**Attack Path 4: RAG Poisoning**
```
Attacker → Upload malicious document → Ingested by RAG → Document becomes AI instruction → Data exfiltration
```
**Mitigation:** File upload validation, treat documents as untrusted data

### Phase 6: Risk Impact

| Risk | Probability | Impact | Score (1-5) | Treatment |
|---|---|---|---|---|
| JWT signature bypass | Medium | Critical | 5 (P0) | Fixed: signature verification |
| Cross-tenant access | High | Critical | 5 (P0) | Fixed: server-side tenant derivation |
| Password cracking | Medium | Critical | 5 (P0) | Fixed: PBKDF2, rate limiting |
| OAuth CSRF | Medium | High | 4 (P0) | Fixed: state validation, nonce |
| File upload RCE | Low | Critical | 4 (P1) | Fixed: type/size validation |
| XSS token theft | Medium | High | 4 (P1) | Fixed: secure storage, CSP |
| API brute-force | High | Medium | 3 (P1) | Fixed: rate limiting |

---

## DFD (Data Flow Diagram) Attack Surfaces

### Dataflow 1: User Authentication
```
User → Login Form → /api/v1/auth/login → Auth Service → Verify Password → Issue JWT
```
**Trust boundary:** Client → API Gateway  
**Controls:** Rate limiting, PBKDF2, JWT signing, input validation

### Dataflow 2: API Access
```
Client → API Request (Bearer JWT) → API Gateway → requireAuth() → requirePermission() → Backend Service
```
**Trust boundary:** API Gateway → Backend Services  
**Controls:** JWT validation, role-based permissions, tenant scoping

### Dataflow 3: RAG Query
```
User Query → AuthZ → Vector Search (tenant-scoped) → Permission Filter → LLM → Response
```
**Trust boundary:** AI processing  
**Controls:** Tenant-scoped retrieval, document permission filter, output validation

### Dataflow 4: File Upload
```
User Upload → /api/v1/files/upload → Validate Type/Size → Store → Index for RAG
```
**Trust boundary:** Untrusted file → Trusted system  
**Controls:** Type allowlist, size limit, path traversal detection, malware scan (recommended)

### Dataflow 5: OAuth Callback
```
Google OAuth → /auth/callback → Validate State → Exchange Code → Issue JWT
```
**Trust boundary:** External OAuth provider → Internal system  
**Controls:** State validation, nonce, provider allowlist, same-origin check

---

## Attack Surface Reduction Plan

### Removed Attack Surfaces
1. **Client-controlled roles** — Roles now derived from JWT, validated against allowlist
2. **Client-controlled tenant_id** — Always derived from server-side JWT
3. **Plaintext MFA secrets** — Only QR code file download, no secret display
4. **Unvalidated OAuth state** — CSRF state token with nonce enforced
5. **Weak password hashing** — Replaced with PBKDF2-SHA256

### Reduced Attack Surfaces
1. **localStorage token storage** — Memory-only in production
2. **Missing security headers** — Full header set added
3. **No rate limiting** — All auth endpoints rate-limited
4. **Debug logging** — Removed sensitive data logging
5. **File upload risks** — Type, size, path traversal validation added

---

## Assumptions & Limitations

### Assumptions
- JWT secret is securely managed in production environment variables
- Backend services (Auth Service, etc.) enforce their own server-side authorization
- Infrastructure (Docker, Kubernetes, network) is properly isolated
- TLS is terminated at the ingress/load balancer layer

### Limitations
This threat model covers the Astro frontend and API gateway layer. Backend microservices and infrastructure are out of scope for this assessment. Professional infrastructure and network security assessment is recommended before production deployment.
