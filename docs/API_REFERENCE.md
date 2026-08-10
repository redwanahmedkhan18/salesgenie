# SalesGenie API Reference

**Version:** 1.0  
**Base URL:** `https://api.salesgenie.ai`  
**API Version:** `/api/v1`  
**Last Updated:** 2026-08-09

---

## Table of Contents

1. [Authentication](#1-authentication)
2. [Authorization (RBAC)](#2-authorization-rbac)
3. [Rate Limiting](#3-rate-limiting)
4. [Pagination](#4-pagination)
5. [Error Handling](#5-error-handling)
6. [Filtering & Sorting](#6-filtering--sorting)
7. [Idempotency](#7-idempotency)
8. [Webhook Security](#8-webhook-security)
9. [Event System](#9-event-system)
10. [API Standards](#10-api-standards)

---

## 1. Authentication

### JWT Bearer Token

All authenticated endpoints require an `Authorization: Bearer <JWT>` header.

**Token Format**
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

**Token Payload Structure**

| Field | Type | Description |
|-------|------|-------------|
| `sub` | string | User ID (UUID) |
| `tenant_id` | string | Organization tenant ID |
| `email` | string | User email address |
| `roles` | string[] | Platform roles assigned to user |
| `permissions` | string[] | Effective permissions derived from roles |
| `session_id` | string | Current session ID |
| `exp` | integer | Unix timestamp of expiration |

**Token Expiration**
- Access token: 60 minutes (`ACCESS_TOKEN_EXPIRE_MINUTES`)
- Refresh token: 14 days (`REFRESH_TOKEN_EXPIRE_DAYS`)

### Authentication Flow

```mermaid
sequenceDiagram
    participant C as Client
    participant A as Auth Service
    participant K as Keycloak

    C->>A: POST /auth/login (email, password)
    A->>K: Validate credentials
    K-->>A: Token set
    A-->>C: Access token + Refresh token
    Note over C,K: Subsequent requests use Bearer token

    C->>A: POST /auth/refresh (refresh_token)
    A-->>C: New access token
```

### Endpoints

| Method | Path | Description | Auth Required |
|--------|------|-------------|---------------|
| POST | `/api/v1/auth/signup` | Register new user account | No |
| POST | `/api/v1/auth/login` | Authenticate and receive tokens | No |
| POST | `/api/v1/auth/refresh` | Refresh access token | No |
| POST | `/api/v1/auth/logout` | Invalidate session | Yes |
| POST | `/api/v1/auth/forgot-password` | Send password reset email | No |
| POST | `/api/v1/auth/reset-password` | Reset password with token | No |
| POST | `/api/v1/auth/verify-email` | Verify email address | No |
| GET | `/api/v1/auth/sessions` | List active sessions | Yes |
| POST | `/api/v1/auth/mfa/setup` | Set up MFA | Yes |
| POST | `/api/v1/auth/mfa/verify` | Verify MFA code | Yes |

### MFA

Multi-Factor Authentication uses TOTP (Time-based One-Time Password).

**Setup:**
```
POST /api/v1/auth/mfa/setup
→ { qr_code_url, secret, backup_codes }
```

**Verify:**
```
POST /api/v1/auth/mfa/verify
{ code: "123456" }
→ { success: true, backup_codes: ["...", "..."] }
```

---

## 2. Authorization (RBAC)

### Roles

The platform uses 10 roles with a hierarchical permission model.

| Role | Value | Description |
|------|-------|-------------|
| SUPER_ADMIN | `super_admin` | Full platform access |
| WORKSPACE_ADMIN | `workspace_admin` | Manage entire workspace |
| ORG_ADMIN | `org_admin` | Manage organization |
| SALES_MANAGER | `sales_manager` | Sales team management |
| SALES_AGENT | `sales_agent` | Sales representative |
| SUPPORT_MANAGER | `support_manager` | Support team management |
| SUPPORT_AGENT | `support_agent` | Support representative |
| KNOWLEDGE_MANAGER | `knowledge_manager` | Knowledge base management |
| AUDITOR | `auditor` | Read-only audit access |
| END_USER | `end_user` | Basic platform user |

### Permission Matrix (Key Permissions)

| Permission | Super Admin | Workspace Admin | Org Admin | Sales Mgr | Sales Agent | Support Mgr | Support Agent | Knowledge Mgr | Auditor | End User |
|------------|-------------|-----------------|-----------|-----------|-------------|-------------|---------------|---------------|---------|----------|
| `system:manage` | ✓ | | | | | | | | | |
| `org:read` | ✓ | ✓ | ✓ | | | | | | ✓ | |
| `org:write` | ✓ | ✓ | ✓ | | | | | | | |
| `org:delete` | ✓ | ✓ | | | | | | | | |
| `user:read` | ✓ | ✓ | ✓ | | | | | | ✓ | |
| `user:write` | ✓ | ✓ | ✓ | | | | | | | |
| `user:delete` | ✓ | ✓ | ✓ | | | ✓ | | | | |
| `user:invite` | ✓ | ✓ | ✓ | | | | | | | |
| `agent:read` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | |
| `agent:write` | ✓ | ✓ | ✓ | | | | | | | |
| `prompt:manage` | ✓ | ✓ | ✓ | | | | | | | |
| `agent:execute` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | ✓ |
| `knowledge:read` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ | ✓ |
| `knowledge:write` | ✓ | ✓ | ✓ | | | ✓ | | ✓ | | | |
| `knowledge:delete` | ✓ | ✓ | | | | | | ✓ | | | |
| `vector:manage` | ✓ | ✓ | | | | | | | | |
| `leads:read` | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | |
| `leads:write` | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | |
| `deals:manage` | ✓ | ✓ | ✓ | ✓ | | | | | | |
| `ticket:read` | ✓ | ✓ | ✓ | | | ✓ | ✓ | | ✓ | |
| `ticket:write` | ✓ | ✓ | ✓ | | | ✓ | ✓ | | | |
| `ticket:assign` | ✓ | ✓ | ✓ | | | ✓ | | | | |
| `ticket:refund` | ✓ | ✓ | | | | ✓ | | | | |
| `live:handoff` | ✓ | ✓ | ✓ | | | ✓ | ✓ | | | |
| `analytics:read` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | ✓ | |
| `workflow:manage` | ✓ | ✓ | ✓ | | | | | | | |
| `billing:read` | ✓ | ✓ | ✓ | | | | | | ✓ | |
| `billing:manage` | ✓ | ✓ | | | | | | | | |

### Permission Enforcement

Permissions are enforced at the route level via FastAPI dependencies:

```python
from common.security_rbac import RequirePermissions, Permission

@router.get(
    "/admin/users",
    dependencies=[Depends(RequirePermissions(Permission.SYSTEM_MANAGE))]
)
```

**Super Admin Bypass:** Users with `super_admin` role bypass all permission checks.

---

## 3. Rate Limiting

Rate limits are applied per tenant/plan tier using a sliding window algorithm.

### Rate Limits by Tier

| Tier | Requests/Min | Requests/Hour | AI Token Quota/Hour | AI Token Quota/Min |
|------|-------------|---------------|---------------------|-------------------|
| Free | 60 | 500 | 100,000 | 5,000 |
| Starter | 120 | 2,000 | 500,000 | 25,000 |
| Growth | 300 | 10,000 | 2,000,000 | 100,000 |
| Enterprise | 1,000 | 50,000 | 10,000,000 | 500,000 |

### Headers

All responses include rate limit headers:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
Retry-After: 60  (only on 429 responses)
```

### Response on Limit Exceeded

```
HTTP/1.1 429 Too Many Requests
Content-Type: application/json
Retry-After: 60

{
  "detail": "Rate limit exceeded. Try again in 59 seconds.",
  "retry_after": 59
}
```

### Authentication Endpoints (Stricter)

| Endpoint | Limit | Window |
|----------|-------|--------|
| `/auth/login` | 5 requests | 15 minutes |
| `/auth/signup` | 3 requests | 1 hour |
| `/auth/forgot-password` | 3 requests | 1 hour |
| `/auth/mfa/verify` | 5 requests | 15 minutes |

### AI Request Limits

AI endpoints (chat, agent execution) have additional limits:
- AI calls per minute: `requests_per_minute // 10`
- Token quota: enforced per tier (see table above)

---

## 4. Pagination

### Standard Pagination

All list endpoints use `limit` and `offset` query parameters:

```
GET /api/v1/customers?limit=50&offset=100
```

**Parameters**

| Parameter | Type | Default | Max | Description |
|-----------|------|---------|-----|-------------|
| `limit` | integer | 20 | 100 | Number of items per page |
| `offset` | integer | 0 | 10000 | Number of items to skip |

**Response Format**

```json
{
  "data": [...],
  "pagination": {
    "limit": 20,
    "offset": 0,
    "total": 150,
    "has_more": true,
    "pages": 8
  }
}
```

### Cursor Pagination (AI Gateway)

The AI Gateway chat endpoint uses cursor-based pagination for message history:

```
GET /api/v1/ai/chat/{session_id}/messages?limit=50&before=msg_123abc
```

**Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `limit` | integer | Max items (default: 50, max: 200) |
| `before` | string | Cursor for pagination (message ID) |

---

## 5. Error Handling

### Error Response Format

All API errors follow the RFC 7807 Problem Details format:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Input validation failed",
  "details": {
    "field": "email",
    "issue": "must be a valid email address"
  },
  "request_id": "req_123abc456def",
  "timestamp": "2026-08-09T10:30:00Z",
  "path": "/api/v1/customers"
}
```

### Status Codes

| Status | Code | Description |
|--------|------|-------------|
| 200 | OK | Success |
| 201 | CREATED | Resource created |
| 204 | NO_CONTENT | Resource deleted |
| 400 | BAD_REQUEST | Malformed request |
| 401 | UNAUTHORIZED | Invalid/missing token |
| 403 | FORBIDDEN | Insufficient permissions |
| 404 | NOT_FOUND | Resource not found |
| 409 | CONFLICT | Resource conflict |
| 422 | UNPROCESSABLE_ENTITY | Validation error |
| 429 | TOO_MANY_REQUESTS | Rate limit exceeded |
| 500 | INTERNAL_ERROR | Server error |
| 502 | BAD_GATEWAY | Upstream service unavailable |
| 503 | SERVICE_UNAVAILABLE | Service degraded/maintenance |
| 504 | GATEWAY_TIMEOUT | Upstream timeout |

### Error Codes

| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Input data validation failed |
| `AUTHENTICATION_FAILED` | JWT token invalid or expired |
| `INSUFFICIENT_PERMISSIONS` | Missing required permission |
| `RESOURCE_NOT_FOUND` | Requested resource doesn't exist |
| `CONFLICT` | Duplicate resource or state conflict |
| `RATE_LIMITED` | Rate limit exceeded |
| `SUBSCRIPTION_REQUIRED` | Active subscription needed |
| `TENANT_QUOTA_EXCEEDED` | Tenant resource quota exceeded |
| `INTERNAL_ERROR` | Unexpected server error |
| `SERVICE_UNAVAILABLE` | Downstream service error |
| `BUDGET_EXCEEDED` | Tenant AI budget threshold reached |

---

## 6. Filtering & Sorting

### Filtering

Use `filter[field]` query parameters:

```
GET /api/v1/lead-intelligence/profiles?filter[status]=qualified&filter[company]="Acme Corp"
```

**Common Filter Fields:**

| Endpoint | Filterable Fields |
|----------|------------------|
| `/customers` | `status`, `segment`, `tags` |
| `/leads` | `status`, `source`, `score_min` |
| `/tickets` | `status`, `priority`, `assignee` |
| `/conversations` | `status`, `channel`, `agent_type` |

### Sorting

Use `sort` query parameter:

```
GET /api/v1/tickets?sort=-created_at,priority
```

- Prefix with `-` for descending order
- Comma-separated for multi-sort (applied left-to-right)

**Sortable Fields:**

| Endpoint | Default Sort | Sortable |
|----------|-------------|----------|
| `/customers` | `-created_at` | `name`, `created_at`, `updated_at` |
| `/leads` | `-score` | `score`, `created_at`, `updated_at` |
| `/tickets` | `-created_at` | `priority`, `created_at`, `updated_at` |

---

## 7. Idempotency

### Idempotency Keys

All write endpoints (POST, PUT, PATCH) support idempotency keys to prevent duplicate operations:

```
POST /api/v1/billing/subscriptions
Idempotency-Key: subscription_create_org_abc123_20260809
Content-Type: application/json

{ "plan": "growth_monthly" }
```

**Key Format:** `{resource_type}_{tenant_id}_{timestamp}`

**Rules:**
- Keys must be unique per tenant
- Keys expire after 24 hours
- Same key returns same response (including errors)
- 409 Conflict on key reuse with different request body

**Endpoints with Idempotency:**
- `POST /api/v1/billing/subscriptions` (subscription creation)
- `POST /api/v1/billing/invoices/generate` (invoice generation)
- `POST /api/v1/billing/payments/receipt` (receipt generation)
- `POST /api/v1/whatsapp/messages` (message sending)
- `POST /api/v1/slack/channels/{channel_id}/messages` (Slack messages)
- `POST /api/v1/email/send` (email sending)

### Response Headers

```
Idempotency-Key: subscription_create_org_abc123_20260809
Idempotency-Replay: true  (true on replayed requests)
```

---

## 8. Webhook Security

All webhook endpoints verify signatures using HMAC-SHA256.

### Signature Verification

```
POST /api/v1/billing/webhooks/stripe
Stripe-Signature: t=1691234567,v1=5257a869e7ecebeda32affa62cdca3fa51cad7e6766...',v0=...
```

Each provider has a distinct verification method:

| Provider | Header | Algorithm | Env Var |
|----------|--------|-----------|---------|
| Stripe | `Stripe-Signature` | HMAC-SHA256 | `STRIPE_WEBHOOK_SECRET` |
| Slack | `X-Slack-Signature` + `X-Slack-Request-Timestamp` | HMAC-SHA256 | `SLACK_SIGNING_SECRET` |
| Discord | `X-Signature-Ed25519` + `X-Signature-Timestamp` | Ed25519 | (N/A - public key hardcoded) |
| WhatsApp | `X-Hub-Signature-256` | HMAC-SHA256 | `WHATSAPP_WEBHOOK_SECRET` |
| Facebook Messenger | `X-Hub-Signature-256` | HMAC-SHA256 | `FACEBOOK_APP_SECRET` |
| Telegram | `X-Telegram-Bot-Api-Secret-Token` | Secret token | `TELEGRAM_WEBHOOK_SECRET_TOKEN` |

### Webhook Endpoints

| Service | Path | Verification |
|---------|------|-------------|
| Billing | `/api/v1/billing/webhooks/stripe` | Stripe signature |
| WhatsApp | `/api/v1/whatsapp/webhook` | Hub signature |
| Telegram | `/api/v1/telegram/webhook` | Secret token |
| Messenger | `/api/v1/messenger/webhook` | Hub signature |
| Slack | `/api/v1/slack/webhook` | Slack signature |
| Discord | `/api/v1/discord/webhook` | Ed25519 signature |
| Email | `/api/v1/email/webhook` | Hub signature |

### Idempotency

Webhook events are deduplicated using event IDs stored in Redis with a 7-day TTL. Events processed within the TTL window are skipped.

---

## 9. Event System

### Kafka Topics

| Topic | Description | Producers |
|-------|-------------|-----------|
| `user.registered` | New user registration | auth-service |
| `user.deleted` | User deleted (GDPR) | user-service |
| `user.profile.updated` | User profile changed | user-service |
| `org.created` | Organization created | organization-service |
| `org.updated` | Organization updated | organization-service |
| `org.deleted` | Organization deleted | organization-service |
| `org.member.invited` | Member invited | organization-service |
| `org.role.assigned` | Role assigned to member | organization-service |
| `subscription.created` | New subscription | billing-service |
| `subscription.canceled` | Subscription canceled | billing-service |
| `subscription.renewed` | Subscription renewed | billing-service |
| `conversation.started` | New conversation | conversation-service |
| `conversation.ended` | Conversation ended | conversation-service |
| `conversation.handoff` | Human handoff requested | conversation-service |
| `message.received` | New message received | conversation-service |
| `message.sent` | Message sent to user | conversation-service |
| `ticket.created` | New support ticket | ticket-service |
| `ticket.updated` | Ticket status changed | ticket-service |
| `ticket.assigned` | Ticket assigned | ticket-service |
| `billing.invoice.created` | Invoice generated | billing-service |
| `billing.payment.succeeded` | Payment succeeded | billing-service |
| `billing.payment.failed` | Payment failed | billing-service |

### Event Schema Format

All events follow CloudEvents 1.0 specification:

```json
{
  "specversion": "1.0",
  "id": "evt_123abc456def",
  "source": "salesgenie.auth-service",
  "type": "user.registered",
  "subject": "user:usr_789ghi",
  "time": "2026-08-09T10:30:00Z",
  "datacontenttype": "application/json",
  "data": {
    "user_id": "usr_789ghi",
    "tenant_id": "org_abc123",
    "email": "user@example.com",
    "source": "signup"
  }
}
```

---

## 10. API Standards

### Versioning

All endpoints are prefixed with `/api/v1/`. The version is included in the path, not in headers or content type.

### Request/Response Format

- **Content-Type:** `application/json` for all requests and responses
- **Encoding:** UTF-8
- **Date format:** ISO 8601 with UTC timezone (`2026-08-09T10:30:00Z`)
- **ID format:** UUIDv4 for all resource identifiers
- **Null handling:** Optional fields may be `null`

### HTTP Method Conventions

| Method | Semantics | Idempotent |
|--------|-----------|------------|
| GET | Read resource | Yes |
| POST | Create resource | No |
| PUT | Create or replace | Yes |
| PATCH | Partial update | Yes |
| DELETE | Delete resource | Yes |

### CORS

```
Access-Control-Allow-Origin: https://app.salesgenie.ai
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS
Access-Control-Allow-Headers: Authorization, Content-Type, Idempotency-Key
Access-Control-Max-Age: 3600
```

### Health Check Endpoints

Every service exposes:

| Endpoint | Description |
|----------|-------------|
| `/api/v1/health/live` | Liveness probe (process check) |
| `/api/v1/health/ready` | Readiness probe (DB/Redis/Kafka checks) |
| `/api/v1/metrics` | Prometheus metrics endpoint |

### OpenAPI Documentation

Each service exposes its OpenAPI spec at:
```
GET /openapi.json
GET /docs  (Swagger UI)
GET /redoc  (ReDoc)
```