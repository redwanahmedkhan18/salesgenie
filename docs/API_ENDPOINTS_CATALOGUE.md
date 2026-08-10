# SalesGenie API Endpoints Catalogue

**Auto-generated from code**  
**Source:** Scanned all `router_*.py` and `main.py` files  
**Last Updated:** 2026-08-09

This catalogue lists all API endpoints found in the codebase, organized by service.
Use this to verify `api-routes.yaml` and `architecture.md` accuracy.

---

## 1. Authentication Service (Port 8001)

### `auth_service/src/router_auth.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| POST | `/api/v1/auth/signup` | User Registration with Email Verification | Public |
| POST | `/api/v1/auth/login` | User Authentication Login | Public |
| POST | `/api/v1/auth/refresh` | Refresh access token | Public |
| POST | `/api/v1/auth/logout` | Logout user and invalidate session | Authenticated |
| POST | `/api/v1/auth/forgot-password` | Request password reset | Public |
| POST | `/api/v1/auth/reset-password` | Reset password with token | Public |
| POST | `/api/v1/auth/verify-email` | Verify email address | Public |
| GET | `/api/v1/auth/sessions` | Get User Sessions | Authenticated |
| POST | `/api/v1/auth/mfa/setup` | Setup MFA | Authenticated |
| POST | `/api/v1/auth/mfa/verify` | Verify MFA Code | Authenticated |

### `auth_service/src/main.py`

| Method | Path | Tags |
|--------|------|------|
| GET | `/api/v1/health/live` | Health Checks |
| GET | `/api/v1/health/ready` | Health Checks |
| GET | `/api/v1/metrics` | Monitoring |

---

## 2. User Service (Port 8002)

### `user_service/src/router_user.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| GET | `/api/v1/users/me` | Get Current User Profile | Authenticated |
| PUT | `/api/v1/users/me` | Update Current User Profile | Authenticated |
| PATCH | `/api/v1/users/me/preferences` | Update User Preferences | Authenticated |
| POST | `/api/v1/users/me/export` | GDPR Article 20 Data Export | Authenticated |
| DELETE | `/api/v1/users/me` | GDPR Article 17 Right to Erasure | Authenticated |
| GET | `/api/v1/users/me/consent` | Get Consent Preferences | Authenticated |
| POST | `/api/v1/users/me/consent` | Update Consent Preferences | Authenticated |

---

## 3. Organization Service (Port 8003)

### `organization_service/src/router_organization.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| POST | `/api/v1/organizations` | Create Organization | Authenticated |
| GET | `/api/v1/organizations/{org_id}` | Get Organization | Authenticated |
| PATCH | `/api/v1/organizations/{org_id}` | Update Organization | `ORG_WRITE` |
| DELETE | `/api/v1/organizations/{org_id}` | Delete Organization | `ORG_DELETE` (super_admin) |
| GET | `/api/v1/organizations/{org_id}/metrics` | Get Org Metrics | Authenticated |
| PUT | `/api/v1/organizations/{org_id}/branding` | Update Branding | `ORG_WRITE` |
| GET | `/api/v1/organizations/{org_id}/members` | List Members | Authenticated |
| POST | `/api/v1/organizations/{org_id}/members` | Invite Member | `USER_INVITE` |
| PATCH | `/api/v1/organizations/{org_id}/members/{member_id}/role` | Update Role | `TENANT_MANAGE` |
| DELETE | `/api/v1/organizations/{org_id}/members/{member_id}` | Remove Member | `TENANT_MANAGE` |

---

## 4. Billing Service (Port 8004)

### `billing_service/src/router_billing.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| GET | `/api/v1/billing/plans` | List Plans | Public |
| POST | `/api/v1/billing/subscriptions` | Create Subscription | `BILLING_MANAGE` |
| GET | `/api/v1/billing/subscriptions/usage` | Get Token Usage | `BILLING_READ` |
| GET | `/api/v1/billing/subscriptions/check` | Check Subscription | `BILLING_READ` |
| GET | `/api/v1/billing/invoices` | List Invoices | `BILLING_READ` |
| POST | `/api/v1/billing/invoices/generate` | Generate Invoice PDF | `BILLING_MANAGE` |
| GET | `/api/v1/billing/invoices/{invoice_id}/pdf` | Download Invoice PDF | `BILLING_READ` |
| POST | `/api/v1/billing/payments/receipt` | Generate Payment Receipt | Authenticated |
| GET | `/api/v1/billing/usage/live` | Live Token Usage | `BILLING_READ` |
| GET | `/api/v1/billing/alerts` | Cost Alerts | `BILLING_READ` |
| GET | `/api/v1/billing/platform-usage` | Platform Usage | `BILLING_READ` (super admin) |

### `billing_service/src/webhooks.py`

| Method | Path | Summary | Auth |
|--------|------|---------|------|
| POST | `/api/v1/billing/webhooks/stripe` | Stripe webhook | Signature verified |

---

## 5. Customer Service (Port 8016)

### `customer_service/src/router_customers.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| POST | `/api/v1/customers` | Create Customer | `customer:create` |
| GET | `/api/v1/customers` | List Customers | `customer:read` |
| GET | `/api/v1/customers/{id}` | Get Customer | `customer:read` |
| PUT | `/api/v1/customers/{id}` | Update Customer | `customer:update` |
| DELETE | `/api/v1/customers/{id}` | Delete Customer | `customer:delete` |
| GET | `/api/v1/customers/{id}/history` | Customer History | `customer:read` |
| GET | `/api/v1/customers/{id}/orders` | Customer Orders | `customer:read` |
| GET | `/api/v1/customers/segments` | List Segments | `customer:read` |
| POST | `/api/v1/customers/segments` | Create Segment | `customer:write` |
| GET | `/api/v1/customers/tags` | List Tags | `customer:read` |
| POST | `/api/v1/customers/tags` | Create Tag | `customer:write` |

---

## 6. Conversation Service (Port 8018)

### `conversation_service/src/router_conversations.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| POST | `/api/v1/conversations` | Create Conversation | Authenticated |
| GET | `/api/v1/conversations` | Search Conversations | Authenticated |
| GET | `/api/v1/conversations/{conversation_id}` | Get Conversation | Authenticated |
| PUT | `/api/v1/conversations/{conversation_id}` | Update Conversation | Authenticated |
| PATCH | `/api/v1/conversations/{conversation_id}` | Partial Update | Authenticated |
| DELETE | `/api/v1/conversations/{conversation_id}` | Delete Conversation | Authenticated |
| GET | `/api/v1/conversations/overview` | Overview Stats | Authenticated |
| GET | `/api/v1/conversations/stats/by-status` | Status Stats | Authenticated |
| GET | `/api/v1/conversations/stats/by-channel` | Channel Stats | Authenticated |
| POST | `/api/v1/conversations/{conversation_id}/messages` | Send Message | Authenticated |
| GET | `/api/v1/conversations/{conversation_id}/messages` | Get Messages | Authenticated |
| POST | `/api/v1/conversations/{conversation_id}/handoff` | Handoff to Human | Authenticated |

---

## 7. AI Gateway Service (Port 8000)

### `ai_gateway_service/src/router_ai.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| POST | `/api/v1/ai/chat` | Multi-Agent Chat Completion | `AGENT_EXECUTE` + subscription |
| GET | `/api/v1/ai/agents` | List Platform AI Agents | Public |

### `ai_gateway_service/src/router_admin.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| GET | `/api/v1/admin/users` | List All Users | `SYSTEM_MANAGE` |
| GET | `/api/v1/admin/audit-events` | List Audit Events | `SYSTEM_AUDIT_READ` |
| GET | `/api/v1/admin/health` | System Health Status | `SYSTEM_MANAGE` |
| GET | `/api/v1/admin/ai-providers` | AI Provider Status | `SYSTEM_MANAGE` |
| GET | `/api/v1/admin/settings` | Platform Settings | `SYSTEM_MANAGE` |
| PATCH | `/api/v1/admin/settings` | Update Platform Settings | `SYSTEM_MANAGE` |
| GET | `/api/v1/admin/system-info` | System Information | `SYSTEM_MANAGE` |
| POST | `/api/v1/admin/users/{user_id}/suspend` | Suspend User | `SYSTEM_MANAGE` |
| POST | `/api/v1/admin/users/{user_id}/resume` | Resume User | `SYSTEM_MANAGE` |
| GET | `/api/v1/admin/metrics` | Platform Metrics | `SYSTEM_MANAGE` |
| GET | `/api/v1/admin/organizations` | List Organizations | `SYSTEM_MANAGE` |
| PATCH | `/api/v1/admin/organizations/{org_id}/suspend` | Suspend Org | `SYSTEM_MANAGE` |
| PATCH | `/api/v1/admin/organizations/{org_id}/resume` | Resume Org | `SYSTEM_MANAGE` |
| DELETE | `/api/v1/admin/organizations/{org_id}` | Delete Org | `SYSTEM_MANAGE` |

---

## 8. Sales Service (Port 8007)

### `sales_service/src/router_sales.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| GET | `/api/v1/sales/leads` | List Leads | `LEADS_READ` |
| POST | `/api/v1/sales/leads` | Create Lead | `LEADS_WRITE` |
| GET | `/api/v1/sales/leads/{id}` | Get Lead | `LEADS_READ` |
| PUT | `/api/v1/sales/leads/{id}` | Update Lead | `LEADS_WRITE` |
| PATCH | `/api/v1/sales/leads/{id}` | Partial Update Lead | `LEADS_WRITE` |
| DELETE | `/api/v1/sales/leads/{id}` | Delete Lead | `LEADS_WRITE` |
| GET | `/api/v1/sales/leads/{id}/history` | Lead Activity History | `LEADS_READ` |
| GET | `/api/v1/sales/recommendations` | Sales Recommendations | `LEADS_READ` |
| POST | `/api/v1/sales/leads/{id}/qualify` | Qualify Lead | `LEADS_WRITE` |
| GET | `/api/v1/sales/deals` | List Deals | `DEALS_MANAGE` |
| POST | `/api/v1/sales/deals` | Create Deal | `DEALS_MANAGE` |
| PATCH | `/api/v1/sales/deals/{id}/stage` | Update Deal Stage | `DEALS_MANAGE` |
| GET | `/api/v1/sales/metrics` | Sales Metrics | `ANALYTICS_READ` |

---

## 9. Ticket Service (Port 8008)

### `ticket_service/src/router_ticket.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| GET | `/api/v1/tickets` | List Tickets | `TICKET_READ` |
| POST | `/api/v1/tickets` | Create Ticket | `TICKET_WRITE` |
| GET | `/api/v1/tickets/{id}` | Get Ticket | `TICKET_READ` |
| PUT | `/api/v1/tickets/{id}` | Update Ticket | `TICKET_WRITE` |
| PATCH | `/api/v1/tickets/{id}` | Partial Update | `TICKET_WRITE` |
| DELETE | `/api/v1/tickets/{id}` | Delete Ticket | `TICKET_WRITE` |
| GET | `/api/v1/tickets/analytics/overview` | Ticket Analytics | `ANALYTICS_READ` |

---

## 10. Knowledge Service (Port 8006)

### `knowledge_service/src/router_knowledge.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| GET | `/api/v1/knowledge/categories` | List Categories | `KNOWLEDGE_READ` |
| GET | `/api/v1/knowledge/documents` | List Documents | `KNOWLEDGE_READ` |
| POST | `/api/v1/knowledge/documents` | Create Document | `KNOWLEDGE_WRITE` |
| GET | `/api/v1/knowledge/documents/{id}` | Get Document | `KNOWLEDGE_READ` |
| PUT | `/api/v1/knowledge/documents/{id}` | Update Document | `KNOWLEDGE_WRITE` |
| DELETE | `/api/v1/knowledge/documents/{id}` | Delete Document | `KNOWLEDGE_DELETE` |
| POST | `/api/v1/knowledge/upload` | Upload Document | `KNOWLEDGE_WRITE` |
| POST | `/api/v1/knowledge/ocr` | OCR Processing | `KNOWLEDGE_WRITE` |
| POST | `/api/v1/knowledge/search` | Search Knowledge | `KNOWLEDGE_READ` |

---

## 11. Vector Service (Port 8009)

### `vector_service/src/router_vector.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| POST | `/api/v1/vector/embeddings` | Generate Embeddings | Authenticated |
| POST | `/api/v1/vector/search` | Vector Search | Authenticated |
| GET | `/api/v1/vector/collections` | List Collections | Authenticated |
| POST | `/api/v1/vector/collections` | Create Collection | Authenticated |
| POST | `/api/v1/vector/index` | Index Documents | Authenticated |
| GET | `/api/v1/vector/stats` | Get Vector Stats | Authenticated |

---

## 12. Workflow Service (Port 8011)

### `workflow_service/src/router_workflows.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| GET | `/api/v1/workflows` | List Workflows | Authenticated |
| POST | `/api/v1/workflows` | Create Workflow | `WORKFLOW_MANAGE` |
| GET | `/api/v1/workflows/{id}` | Get Workflow | Authenticated |
| PUT | `/api/v1/workflows/{id}` | Update Workflow | `WORKFLOW_MANAGE` |
| DELETE | `/api/v1/workflows/{id}` | Delete Workflow | `WORKFLOW_MANAGE` |
| POST | `/api/v1/workflows/{id}/execute` | Execute Workflow | `WORKFLOW_MANAGE` |
| GET | `/api/v1/workflows/{id}/history` | Execution History | Authenticated |

---

## 13. Analytics Service (Port 8012)

### `analytics_service/src/router_analytics.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| GET | `/api/v1/analytics/kpis` | Get Platform KPIs | `ANALYTICS_READ` |
| GET | `/api/v1/analytics/conversations` | Conversation Analytics | `ANALYTICS_READ` |
| GET | `/api/v1/analytics/revenue` | Revenue Analytics | `ANALYTICS_READ` |
| GET | `/api/v1/analytics/channels` | Channel Analytics | `ANALYTICS_READ` |
| GET | `/api/v1/analytics/time-series` | Time Series Analytics | `ANALYTICS_READ` |
| POST | `/api/v1/ai/evaluate` | AI Evaluation | `AGENT_EXECUTE` |

---

## 14. Search Service (Port 8013)

### `search_service/src/router_search.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| POST | `/api/v1/search/search` | Full-Text Search | `KNOWLEDGE_READ` |
| GET | `/api/v1/search/search` | Search (GET) | `KNOWLEDGE_READ` |
| POST | `/api/v1/search/index` | Index Document | `KNOWLEDGE_WRITE` |
| POST | `/api/v1/search/index/bulk` | Bulk Index | `KNOWLEDGE_WRITE` |
| DELETE | `/api/v1/search/index/{document_id}` | Remove from Index | `KNOWLEDGE_DELETE` |
| GET | `/api/v1/search/index/stats` | Index Statistics | `KNOWLEDGE_READ` |
| GET | `/api/v1/search/index/settings` | Index Settings | `KNOWLEDGE_READ` |
| POST | `/api/v1/search/index/rebuild` | Rebuild Index | `KNOWLEDGE_WRITE` |
| GET | `/api/v1/search/suggest` | Search Suggestions | `KNOWLEDGE_READ` |

---

## 15. File Service (Port 8015)

### `file_service/src/router_files.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| GET | `/api/v1/files` | List Files | Authenticated |
| POST | `/api/v1/files` | Create File Record | Authenticated |
| GET | `/api/v1/files/{id}` | Get File | Authenticated |
| PUT | `/api/v1/files/{id}` | Update File | Authenticated |
| DELETE | `/api/v1/files/{id}` | Delete File | Authenticated |
| POST | `/api/v1/files/upload` | Upload File | Authenticated |
| GET | `/api/v1/files/{id}/download` | Download File | Authenticated |
| GET | `/api/v1/files/{id}/presigned-url` | Get Presigned URL | Authenticated |

---

## 16. Lead Intelligence Service (Port 8022)

### `lead_intelligence_service/src/router_lead_intelligence.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| POST | `/api/v1/lead-intelligence/companies/search` | Search Companies | Authenticated |
| GET | `/api/v1/lead-intelligence/companies/{company_id}` | Get Company | Authenticated |
| POST | `/api/v1/lead-intelligence/companies/{company_id}/qualify` | Qualify Lead | Authenticated |
| POST | `/api/v1/lead-intelligence/companies/{company_id}/research` | Research Company | Authenticated |
| POST | `/api/v1/lead-intelligence/companies/{company_id}/outreach` | Outreach Lead | Authenticated |
| GET | `/api/v1/lead-intelligence/profiles` | List Profiles | Authenticated |
| POST | `/api/v1/lead-intelligence/profiles` | Create Profile | Authenticated |

---

## 17. MCP Gateway Service (Port 8028)

### `mcp_gateway_service/src/router_mcp.py`

| Method | Path | Summary | Permissions |
|--------|------|---------|-------------|
| POST | `/api/v1/mcp/tools` | Register MCP Tool | `AGENT_EXECUTE` |
| GET | `/api/v1/mcp/tools` | List MCP Tools | Authenticated |
| GET | `/api/v1/mcp/tools/{tool_id}` | Get MCP Tool | Authenticated |
| PATCH | `/api/v1/mcp/tools/{tool_id}` | Update MCP Tool | Authenticated |
| DELETE | `/api/v1/mcp/tools/{tool_id}` | Delete MCP Tool | Authenticated |
| POST | `/api/v1/mcp/tools/{tool_id}/execute` | Execute MCP Tool | Authenticated |
| POST | `/api/v1/mcp/execute` | Execute Tool by Name | Authenticated |
| GET | `/api/v1/mcp/logs` | Get Execution Logs | Authenticated |
| GET | `/api/v1/mcp/stats` | Get Tool Statistics | Authenticated |

---

## 18. Channel Integration Services

### Telegram Service (Port 8019)

| Method | Path | Summary |
|--------|------|---------|
| GET | `/api/v1/telegram/bot-info` | Get bot info |
| GET | `/api/v1/telegram/updates` | Get updates |
| GET | `/api/v1/telegram/webhook` | Webhook verification |
| POST | `/api/v1/telegram/webhook` | Webhook handler |
| POST | `/api/v1/telegram/messages` | Send message |

### Slack Service (Port 8024)

| Method | Path | Summary |
|--------|------|---------|
| POST | `/api/v1/slack/webhook` | Webhook handler |
| POST | `/api/v1/slack/workspace/{workspace_id}/channels` | Create channel |
| POST | `/api/v1/slack/channels/{channel_id}/messages` | Send message |
| POST | `/api/v1/slack/integrations` | Create integration |
| GET | `/api/v1/slack/integrations` | List integrations |
| GET | `/api/v1/slack/channels/{channel_id}` | Get channel info |
| DELETE | `/api/v1/slack/integrations/{channel_id}` | Delete integration |

### Discord Service (Port 8026)

| Method | Path | Summary |
|--------|------|---------|
| POST | `/api/v1/discord/webhook` | Webhook handler |
| POST | `/api/v1/discord/workspaces/{guild_id}/channels` | Create channel |
| POST | `/api/v1/discord/channels/{channel_id}/messages` | Send message |
| POST | `/api/v1/discord/bots/{guild_id}/invite` | Get bot invite link |
| POST | `/api/v1/discord/integrations` | Create integration |
| GET | `/api/v1/discord/integrations` | List integrations |
| GET | `/api/v1/discord/channels/{channel_id}` | Get channel info |
| DELETE | `/api/v1/discord/integrations/{channel_id}` | Delete integration |

---

## Discrepancies Found

### Missing from `api-routes.yaml`

1. **Auth Service:** `/auth/signup`, `/auth/refresh`, `/auth/logout`, `/auth/forgot-password`, `/auth/reset-password`, `/auth/verify-email` — only `/login`, `/sessions`, `/mfa/setup`, `/mfa/verify` listed
2. **Billing Service:** `/usage/live`, `/alerts`, `/platform-usage`, `/invoices/generate`, `/invoices/{id}/pdf`, `/payments/receipt`, `/subscriptions/check`, `/webhooks/stripe` — only `/plans`, `/subscriptions`, `/usage`, `/invoices` listed
3. **User Service:** GDPR endpoints (`/me/export`, `/me/consent`, DELETE `/me`) undocumented
4. **Conversation Service:** `/conversations/{id}/messages` (POST/GET), `/conversations/{id}/handoff`, `/overview`, `/stats/by-status`, `/stats/by-channel` missing
5. **MCP Gateway Service:** Entirely missing from `api-routes.yaml`
6. **Product Intelligence Service:** Entirely missing from `api-routes.yaml`
7. **Support Service:** Only partial listing (no analytics endpoint documented)
8. **WhatsApp Service:** Uses `whatsapp-service` but port differs between config files (8005 vs 8017 vs 8025)

### Incorrect Port Numbers in `api-routes.yaml`

| Service | Doc Port | Config Port | Issue |
|---------|----------|-------------|-------|
| Notification Service | 8005 | 8014 | Mismatch |
| WhatsApp Service | 8018 | 8005 (config) / 8025 (docker-compose) | Triple mismatch |
| Chat Service | 8009 | 8010 | Mismatch |
| Vector Service | 8009 | 8009 | Correct, but chat-service also claims 8009 |

### Duplicate Ports

- `chat-service` and `vector-service` both claim port 8009 in `api-routes.yaml`
- `conversation-service` and `whatsapp-service` both claim port 8018

### Missing Health/Monitoring Endpoints

The `api-routes.yaml` does not document health check or metrics endpoints for any service, though all services expose:
- `/api/v1/health/live`
- `/api/v1/health/ready`
- `/api/v1/metrics`
