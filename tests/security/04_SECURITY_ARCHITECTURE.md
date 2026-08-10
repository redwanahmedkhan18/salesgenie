# SalesGenie Security Architecture

## Overview

SalesGenie is a multi-tenant AI platform built on a microservices architecture. This document describes the security controls implemented after the authorized security assessment.

---

## Architecture Diagram

```
                    ┌─────────────────────────────────────┐
                    │  Client (Browser / SPA)             │
                    │  Astro SSG + React Islands          │
                    │  HttpOnly cookies (prod)            │
                    │  In-memory token store (prod)       │
                    └──────────┬──────────────────────────┘
                               │
                               ▼
                    ┌─────────────────────────────────────┐
                    │  Astro API Gateway (SSR)            │
                    │  /api/v1/auth/*                     │
                    │  /api/auth/*                        │
                    │                                     │
                    │  ┌──────────────────────────────┐  │
                    │  │  Security Middleware          │  │
                    │  │  - requireAuth()              │  │
                    │  │  - requirePermission()        │  │
                    │  │  - requireRole()              │  │
                    │  │  - isRateLimited()            │  │
                    │  │  - logAuditEvent()            │  │
                    │  │  - validateId()               │  │
                    │  │  - validateFileUpload()       │  │
                    │  └──────────────────────────────┘  │
                    └──────────┬──────────────────────────┘
                               │
            ┌──────────────────┼──────────────────┐
            ▼                  ▼                  ▼
   ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
   │ Auth Service    │ │ User Service    │ │ Org Service     │
   │ (port 8001)     │ │ (port 8002)     │ │ (port 8003)     │
   │ - PBKDF2 hash   │ │ - User CRUD     │ │ - Tenant CRUD   │
   │ - JWT issue     │ │ - Profile mgmt  │ │ - Brand mgmt    │
   │ - MFA setup     │ │                 │ │ - Members       │
   └─────────────────┘ └─────────────────┘ └─────────────────┘
            │                  │                  │
            ▼                  ▼                  ▼
   ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
   │ AI Gateway      │ │ Knowledge Svc   │ │ Search Service  │
   │ (port 8005)     │ │ (port 8004)     │ │ (port 8007)     │
   │ - LLM routing   │ │ - Doc storage   │ │ - Vector search │
   │ - Agent mgmt    │ │ - RAG pipeline  │ │ - Index mgmt    │
   └─────────────────┘ └─────────────────┘ └─────────────────┘
            │                  │                  │
            ▼                  ▼                  ▼
   ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
   │ File Service    │ │ Tickets Service │ │ Lead Intelligence│
   │ (port 8006)     │ │ (port 8008)     │ │ (port 8012)     │
   └─────────────────┘ └─────────────────┘ └─────────────────┘

                    ┌─────────────────────────────────────┐
                    │  External Integrations              │
                    │  Google OAuth, Slack, WhatsApp,     │
                    │  CRM, Payment Providers, MCP        │
                    └─────────────────────────────────────┘
```

---

## Trust Boundaries

### Boundary 1: Client ↔ API Gateway
- **Control:** JWT bearer token (validated server-side via `requireAuth()`)
- **Transport:** HTTPS (enforced via HSTS header)
- **Token Storage:** HttpOnly cookies in production, in-memory in dev
- **Headers:** CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy

### Boundary 2: API Gateway ↔ Backend Services
- **Control:** Service-to-service authentication (JWT forwarded from client)
- **Tenant Context:** Derived from validated JWT, never from client input
- **Authorization:** `requirePermission()` checks before proxying to backend

### Boundary 3: Backend Service ↔ Database
- **Control:** Server-side tenant scoping in all queries
- **Never trust:** Client-supplied `tenant_id`, `workspace_id`, `organization_id`

### Boundary 4: Backend Service ↔ External Integrations
- **Control:** Server-side OAuth tokens (stored encrypted, never exposed to client)
- **Scope:** Minimum required scopes per integration
- **Validation:** Token validity checked before each external call

### Boundary 5: RAG Pipeline
```
User Query → AuthZ Check → Tenant Context
     ↓
Vector Search (tenant-scoped)
     ↓
Permission Filter (server-side)
     ↓
Retrieved Documents (untrusted data)
     ↓
LLM (documents treated as data, NOT instructions)
     ↓
Output Validation
```

---

## Authentication Flow

```
1. User submits credentials (email, password, optional MFA)
   → POST /api/v1/auth/login
   → Rate limited (5 attempts/15min per IP)
   → Account lockout after 5 failures

2. Backend validates credentials
   → PBKDF2-SHA256 password verification
   → JWT issued with:
     - sub: user_id
     - roles: PlatformRole[]
     - tenant_id: string
     - exp: now + 24h
     - aud: origin
     - alg: HS256

3. Client receives JWT
   → Stored in memory (production) or secure storage (dev)
   → NOT in localStorage in production
   → NOT logged

4. Subsequent requests
   → Authorization: Bearer <jwt>
   → requireAuth() validates signature + expiration + audience
   → requirePermission() checks role → permission matrix
```

---

## Authorization Model

```
USER
  ↓ (authenticated)
  has ROLES
    ↓
    ROLE → PERMISSIONS (server-side matrix)
      - super_admin: [*] (all permissions)
      - workspace_admin: org:*, user:*, agent:*, knowledge:*, leads:*, ticket:*, analytics:*
      - org_admin: org:read, user:read/write, agent:*, knowledge:*, leads:*, ticket:*, analytics:*
      - sales_manager: leads:*
      - sales_agent: leads:read
      - support_manager: ticket:*
      - support_agent: ticket:read/write
      - knowledge_manager: knowledge:*
      - auditor: system:audit:read
      - end_user: agent:execute, knowledge:read, ticket:read

  Every protected resource checks:
  1. Authenticated user? (requireAuth)
  2. Has required role? (requireRole)
  3. Has required permission? (requirePermission)
  4. Tenant membership? (tenant_id from JWT, NOT from client)
```

---

## Multi-Tenant Isolation

Tenant context flows through the system:

```
JWT (validated server-side)
  ↓
tenant_id = JWT.tenant_id  (TRUSTED)
  ↓
All queries filtered by: WHERE tenant_id = <JWT.tenant_id>
  ↓
File paths: /{tenant_id}/{resource}
  ↓
Cache keys: {tenant_id}:{resource_id}
  ↓
Vector DB: collection = {tenant_id}
  ↓
Search: tenant-scoped index
```

**Never accepts `tenant_id` from:**
- Client request body
- Query parameters
- localStorage (client-side only for display, never for queries)

---

## Audit Logging Architecture

```
Security Event
  → logAuditEvent({
      action,           # e.g. "login_failed"
      resource_type,    # e.g. "auth"
      user_id,          # from JWT
      tenant_id,        # from JWT
      ip_address,       # server-side
      severity,         # low/medium/high/critical
      details           # non-sensitive context
    })
  → In-memory ring buffer (10k entries)
  → High/critical events also console.warn() to server logs
```

**Events logged:**
- login_success, login_failed, signup_success, signup_failed
- password_reset_requested, password_reset_success, password_reset_failed
- rate_limit_exceeded
- org_switch_success, org_switch_denied
- token_refresh_success
- audit events for admin actions

**Never logged:**
- Passwords
- Access tokens
- Refresh tokens
- API keys
- Full request bodies with credentials

---

## Deployment Security

### Docker Hardenings
- Non-root user in containers
- Minimal base images
- Security headers enforced at proxy layer
- TLS enforced via ingress

### CI/CD
- `npm audit` / `pip-audit` for dependency scanning
- TypeScript type checking (`astro check`)
- Security regression test suite
- Build fails on P0/P1 test failures

### Infrastructure
- Services bound to localhost (internal only)
- No direct public access to backend services
- Ingress gateway terminates TLS
- Redis/Databases isolated in private network
