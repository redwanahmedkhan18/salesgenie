# SalesGenie Developer Guide

**Version:** 1.0  
**Last Updated:** 2026-08-09

---

## Table of Contents

1. [Local Development Setup](#1-local-development-setup)
2. [Environment Variables](#2-environment-variables)
3. [Service Dependencies & Startup Order](#3-service-dependencies--startup-order)
4. [Database Migrations & Seed](#4-database-migrations--seed)
5. [AI Model Configuration & Fallback](#5-ai-model-configuration--fallback)
6. [MCP Gateway](#6-mcp-gateway)
7. [Testing](#7-testing)
8. [Incident Response & Operations](#8-incident-response--operations)

---

## 1. Local Development Setup

### Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Python | 3.12+ | `pyenv install 3.12` |
| Node.js | 20.x | `nvm install 20` |
| Docker | 24+ | [docker.com](https://docker.com) |
| Docker Compose | 2.0+ | `pip install docker-compose` |
| PostgreSQL | 16+ with pgvector | Docker (see compose) |
| Redis | 7+ | Docker (see compose) |
| MinIO | RELEASE.2024 | Docker (see compose) |
| Git | 2.30+ | System package |

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/salesgenie/salesgenie.git
cd salesgenie

# 2. Copy environment file
cp enterprise-ai-platform/.env.example enterprise-ai-platform/.env

# 3. Start infrastructure (PostgreSQL, Redis, MinIO)
cd enterprise-ai-platform
docker-compose up -d postgres redis minio

# 4. Run database migrations
pip install -r requirements.txt
python database/migrations/migrate.py upgrade

# 5. Start all backend services
python scripts/start_all_services.py

# 6. Start frontend (from project root)
cd ..
npm install
npm run dev

# Or use the full stack:
docker-compose up -d
```

### Frontend Development

```bash
# From project root
npm install
npm run dev       # Astro dev server on http://localhost:4321

# Frontend proxies /api to backend services
# Configure services in src/lib/api-client.ts
```

### Backend Development

Each service can be run independently:

```bash
# Auth service (port 8001)
cd enterprise-ai-platform
python -m auth_service.main --port 8001

# AI Gateway (port 8000)
python -m ai_gateway_service.main --port 8000

# All services at once
python scripts/start_all_services.py
```

### Debugging

```bash
# Check service health
curl http://localhost:8001/health/ready

# View logs
docker-compose logs -f auth-service

# Run service with debug logging
LOG_LEVEL=DEBUG python -m auth_service.main
```

---

## 2. Environment Variables

### Core Platform Variables

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `ENVIRONMENT` | `development` | No | `development`, `staging`, `production` |
| `DEBUG` | `true` (dev) | No | Enable debug mode |
| `LOG_LEVEL` | `INFO` | No | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `API_V1_STR` | `/api/v1` | No | API version prefix |

### Database

| Variable | Default | Required in Prod | Description |
|----------|---------|-------------------|-------------|
| `POSTGRES_USER` | `salesgenie_admin` | No | PostgreSQL username |
| `POSTGRES_PASSWORD` | — | Yes | PostgreSQL password |
| `POSTGRES_HOST` | `localhost` | No | PostgreSQL host |
| `POSTGRES_PORT` | `5432` | No | PostgreSQL port |
| `POSTGRES_DB` | `salesgenie_db` | No | Database name |
| `USE_SQLITE` | `false` | No | Use SQLite (dev only) |
| `DB_POOL_SIZE` | `20` | No | Connection pool size |
| `DB_MAX_OVERFLOW` | `10` | No | Max pool overflow |
| `DB_POOL_TIMEOUT` | `30` | No | Pool timeout (seconds) |
| `DB_POOL_RECYCLE` | `3600` | No | Pool recycle interval |

### Redis

| Variable | Default | Required in Prod | Description |
|----------|---------|-------------------|-------------|
| `REDIS_HOST` | `localhost` | No | Redis host |
| `REDIS_PORT` | `6379` | No | Redis port |
| `REDIS_PASSWORD` | — | Yes (prod) | Redis password |
| `REDIS_DB` | `0` | No | Redis database index |
| `REDIS_SSL` | `true` | No | Enable TLS for Redis |

### Authentication & Security

| Variable | Default | Required in Prod | Description |
|----------|---------|-------------------|-------------|
| `KEYCLOAK_SERVER_URL` | `http://localhost:8080` | Yes (prod) | Keycloak URL |
| `KEYCLOAK_REALM` | `salesgenie-realm` | Yes (prod) | Keycloak realm |
| `KEYCLOAK_CLIENT_ID` | `salesgenie-auth-client` | Yes | Client ID |
| `KEYCLOAK_CLIENT_SECRET` | — | Yes (prod) | Client secret |
| `KEYCLOAK_ADMIN_USERNAME` | — | Yes (prod) | Admin username |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Yes (prod) | Admin password |
| `JWT_SECRET_KEY` | — | Yes | JWT signing key (32+ chars) |
| `JWT_ALGORITHM` | `HS256` | No | JWT algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `60` | No | Access token TTL |
| `REFRESH_TOKEN_EXPIRE_DAYS` | `14` | No | Refresh token TTL |
| `PII_ENCRYPTION_KEY` | — | Yes (prod) | PII field encryption key |

### LLM Providers

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Groq API key (primary provider) |
| `GOOGLE_API_KEY` | Google API key (Gemini/Mistral) |
| `OPENAI_API_KEY` | OpenAI API key (fallback) |
| `ANTHROPIC_API_KEY` | Anthropic API key (fallback) |
| `MISTRAL_API_KEY` | Mistral API key (fallback) |

### Billing & Payments

| Variable | Required in Prod | Description |
|----------|-------------------|-------------|
| `STRIPE_SECRET_KEY` | Yes | Stripe secret API key |
| `STRIPE_WEBHOOK_SECRET` | Yes | Stripe webhook signing secret |

### Communication Channels

| Variable | Description |
|----------|-------------|
| `SMTP_HOST` | SMTP server host |
| `SMTP_PORT` | SMTP port (1025 for Mailpit, 587 for SendGrid) |
| `SMTP_USERNAME` | SMTP username |
| `SMTP_PASSWORD` | SMTP password/API key |
| `SMTP_FROM_ADDRESS` | Sender email address |
| `SENDGRID_API_KEY` | SendGrid API key |
| `TWILIO_ACCOUNT_SID` | Twilio account SID |
| `TWILIO_AUTH_TOKEN` | Twilio auth token |
| `TWILIO_PHONE_NUMBER` | Twilio phone number |
| `SLACK_BOT_TOKEN` | Slack bot token |
| `SLACK_SIGNING_SECRET` | Slack signing secret |
| `DISCORD_BOT_TOKEN` | Discord bot token |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token |
| `FACEBOOK_PAGE_ACCESS_TOKEN` | Facebook Messenger access token |
| `WHATSAPP_ACCESS_TOKEN` | WhatsApp Business API token |
| `WHATSAPP_PHONE_NUMBER_ID` | WhatsApp phone number ID |

### Object Storage

| Variable | Default | Required | Description |
|----------|---------|----------|-------------|
| `MINIO_ENDPOINT` | `localhost:9000` | Yes | MinIO/S3 endpoint |
| `MINIO_ACCESS_KEY` | — | Yes | Access key |
| `MINIO_SECRET_KEY` | — | Yes | Secret key |
| `MINIO_BUCKET_NAME` | `salesgenie-files` | No | Bucket name |

### Monitoring

| Variable | Description |
|----------|-------------|
| `SENTRY_DSN` | Sentry error tracking DSN |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OpenTelemetry collector endpoint |
| `KAFKA_BOOTSTRAP_SERVERS` | Kafka broker addresses |

### Frontend

| Variable | Default | Description |
|----------|---------|-------------|
| `VITE_API_BASE_URL` | `/api` | Backend API base URL |
| `VITE_WS_URL` | (auto) | WebSocket URL |

---

## 3. Service Dependencies & Startup Order

### Service Startup Order

Services must be started in dependency order:

```mermaid
graph TD
    A[PostgreSQL + pgvector] --> B[Redis]
    A --> C[MinIO]
    B --> D[Auth Service]
    B --> E[Organization Service]
    A --> D
    A --> E
    D --> F[Billing Service]
    E --> F
    D --> G[User Service]
    A --> G
    F --> H[Subscription Check]
    G --> H
    D --> I[Customer Service]
    A --> I
    D --> J[Conversation Service]
    A --> J
    B --> J
    D --> K[Knowledge Service]
    A --> K
    K --> L[Vector Service]
    A --> L
    B --> L
    D --> M[Sales Service]
    A --> M
    D --> N[Ticket Service]
    A --> N
    D --> O[Workflow Service]
    A --> O
    D --> P[Analytics Service]
    A --> P
    D --> Q[Search Service]
    A --> Q
    A --> R[Audit Service]
    D --> S[File Service]
    C --> S
    D --> T[Notification Service]
    B --> T
    D --> U[AI Gateway Service]
    A --> U
    B --> U
    U --> V[Lead Intelligence]
    U --> W[Product Intelligence]
    D --> X[MCP Gateway]
    B --> X
    A --> X
```

### Port Assignments

| Service | Port | Depends On |
|---------|------|------------|
| postgres | 5432 | — |
| redis | 6379 | — |
| minio | 9000 | — |
| api-gateway | 80 | auth, user, org, billing, etc. |
| auth-service | 8001 | postgres, redis |
| user-service | 8002 | postgres |
| organization-service | 8003 | postgres |
| billing-service | 8004 | postgres |
| notification-service | 8014 | postgres, redis |
| knowledge-service | 8006 | postgres |
| sales-service | 8007 | postgres |
| ticket-service | 8008 | postgres |
| vector-service | 8009 | postgres, redis |
| workflow-service | 8011 | postgres |
| analytics-service | 8012 | postgres |
| search-service | 8013 | postgres |
| audit-service | 8023 | postgres |
| file-service | 8015 | postgres, minio |
| customer-service | 8016 | postgres |
| support-service | 8017 | postgres |
| conversation-service | 8018 | postgres, redis |
| telegram-service | 8019 | postgres |
| messenger-service | 8020 | postgres |
| email-service | 8021 | postgres |
| lead-intelligence-service | 8022 | postgres |
| slack-service | 8024 | postgres |
| discord-service | 8026 | postgres |
| ai-gateway-service | 8000 | postgres, redis |
| mcp-gateway-service | 8028 | postgres, redis |
| product-intelligence-service | 8027 | postgres |
| security-service | 8031 | postgres, redis |

### Docker Compose Startup

```bash
docker-compose up -d postgres redis minio  # Start infrastructure first
# Wait for health checks to pass
docker-compose up -d
```

### Readiness Checks

Each service exposes `/health/ready` which checks:
- Database connectivity
- Redis connectivity (if applicable)
- Downstream service availability

Services should be started with retry logic until readiness passes.

---

## 4. Database Migrations & Seed

### Migration Framework

SalesGenie uses Alembic with async SQLAlchemy.

**Location:** `enterprise-ai-platform/database/migrations/`

**Config:** `enterprise-ai-platform/database/migrations/alembic.ini`

### Running Migrations

```bash
# Set DATABASE_URL
export DATABASE_URL=postgresql+asyncpg://salesgenie_admin:password@localhost:5432/salesgenie_db

# Apply all migrations
cd enterprise-ai-platform/database/migrations/
alembic upgrade head

# Generate a new migration
alembic revision --autogenerate -m "add_customer_notes_table"

# Roll back one migration
alembic downgrade -1

# Check current revision
alembic current
```

### Seed Data

```bash
# Load seed data (plans, default agents, system prompts)
python scripts/seed_data.py

# Load test data
python scripts/seed_test_data.py
```

### Initial Setup (First Run)

```bash
# 1. Start PostgreSQL
docker-compose up -d postgres

# 2. Run initial schema
psql -h localhost -U salesgenie_admin -d salesgenie_db -f database/schema.sql

# 3. Run migrations
alembic upgrade head

# 4. Apply pgvector extension
psql -h localhost -U salesgenie_admin -d salesgenie_db -c "CREATE EXTENSION IF NOT EXISTS vector;"

# 5. Seed initial data
python scripts/seed_data.py
```

### Migration Best Practices

1. Always review autogenerated migrations before committing
2. Use `compare_type=True` in `env.py` for type comparisons
3. Never delete migration files — create new ones for reversals
4. Test migrations on a copy of production data before deploying

---

## 5. AI Model Configuration & Fallback

### Model Routing

The AI Gateway routes requests based on task complexity:

```python
from common.cost_management import TaskComplexity, MODEL_ROUTING

# Low complexity → Mistral (cheapest)
# Medium complexity → Groq LLaMA-70B
# High complexity → Groq + Gemini
# Critical → Claude (fallback)
```

| Task Complexity | Provider | Model | Cost (per 1M tokens) |
|----------------|----------|-------|---------------------|
| Low | Google | Mistral | $0.14 in / $0.42 out |
| Medium | Groq | LLaMA-70B | $0.59 in / $0.79 out |
| High | Groq + Gemini | Mixtral-8x7B-Instruct | $0.07 in / $0.42 out |
| Critical | Anthropic | Claude 3 | $15 in / $75 out |

### Provider Fallback Chain

```mermaid
graph LR
    A[AI Request] --> B{Primary: Groq}
    B -- Failure --> C{Fallback: Gemini}
    C -- Failure --> D{Fallback: OpenAI}
    D -- Failure --> E{Fallback: Mistral}
    E -- All Fail --> F[Error: AI_UNAVAILABLE]
```

### Circuit Breaker

Per-provider circuit breaker with:
- **Failure threshold:** 5 consecutive failures
- **Timeout:** 60 seconds (Open → Half-Open)
- **States:** Closed → Open → Half-Open → Closed (or Open on failure)

### Cost Controls

- **Budget warning:** 80% of monthly token quota → `warning` alert
- **Hard limit:** 95% of monthly budget → `RuntimeError` → HTTP 503
- **Cost-aware routing:** Routes to cheapest model for task complexity

### Prompt Management

System prompts are defined in `ai-gateway-service/src/prompts.py`:

| Agent | File | Description |
|-------|------|-------------|
| SalesAgent | `SYSTEM_PROMPTS["sales_agent"]` | Lead qualification, recommendations |
| SupportAgent | `SYSTEM_PROMPTS["support_agent"]` | Knowledge search, ticket escalation |
| MemoryAgent | `SYSTEM_PROMPTS["memory_agent"]` | User preference tracking |
| SearchAgent | `SYSTEM_PROMPTS["search_agent"]` | Vector document retrieval |
| AnalyticsAgent | `SYSTEM_PROMPTS["analytics_agent"]` | Evaluation and accuracy monitoring |

### Evaluation Framework

The AI Evaluation Framework (`/ai-evaluation-framework/`) provides:

| Component | Purpose |
|-----------|---------|
| Intent classification | Classify user query intent |
| Response accuracy | Compare AI response to reference |
| Hallucination detection | Flag fabricated information |
| RAG evaluation | Assess retrieval quality |
| Agent trajectory | Trace agent reasoning path |
| Guardrail violations | Detect policy violations |

**Run evaluation:**
```bash
python -m ai_evaluation_framework.main --dataset test_queries.json --model mistral-7b
```

### AI Training Consent

User messages sent to LLM providers require `ai_training` consent.
The `ai-consent` preference must be enabled in user settings.
If not consented, prompts are not logged or retained.

---

## 6. MCP Gateway

### Overview

The MCP (Model Context Protocol) Gateway (`mcp-gateway-service/`) provides:
- Tool registration and discovery
- Schema validation
- Authorization and approval policies
- Execution logging

### MCP Tools

Tools are registered with input/output schemas:

```python
from mcp_gateway_service.src.models import MCPToolDTO

tool = MCPToolDTO(
    name="crm_customer_lookup",
    description="Look up customer details by email",
    input_schema={
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "Customer email address",
            },
        },
        "required": ["email"],
    },
    output_schema={
        "type": "object",
        "properties": {
            "customer_id": {"type": "string"},
            "name": {"type": "string"},
            "status": {"type": "string"},
        },
    },
)
```

### Tool Registration

```
POST /api/v1/mcp/tools
{
  "name": "crm_customer_lookup",
  "description": "Look up customer by email",
  "input_schema": {...},
  "output_schema": {...},
  "required_permissions": ["customer:read"],
  "requires_approval": true
}
```

### Approval Policies

| Tool Risk Level | Requires Approval | Approver |
|-----------------|-------------------|----------|
| Read-only | No | — |
| Write (update) | Yes | Workspace Admin+ |
| Delete | Yes | Org Admin+ |
| Financial | Yes | Super Admin |
| PII access | Yes | Knowledge Manager+ |

### MCP Tool Execution

```
POST /api/v1/mcp/execute
{
  "tool_name": "crm_customer_lookup",
  "arguments": {"email": "customer@example.com"},
  "session_id": "sess_123abc"
}

→ { "result": {...}, "tool_call_id": "call_456def" }
```

### Tool Permissions

| Permission | MCP Tools Allowed |
|------------|-------------------|
| `customer:read` | customer_lookup, order_history |
| `customer:write` | customer_update, customer_create |
| `knowledge:read` | document_search, faq_lookup |
| `knowledge:write` | document_create, knowledge_update |
| `billing:manage` | invoice_create, refund_request |

---

## 7. Testing

### Test Structure

```
tests/
├── unit/                  # Unit tests
├── integration/           # Integration tests
├── fixtures/              # Test data fixtures
└── conftest.py           # Pytest configuration
```

### Running Tests

```bash
# Unit tests
pytest tests/unit/ -v

# Integration tests
pytest tests/integration/ -v

# Coverage report
pytest tests/ --cov=src --cov-report=html

# Specific test
pytest tests/unit/test_auth.py::test_login_success -v
```

### Test Data

```bash
# Seed test data
python scripts/seed_test_data.py

# Reset test database
python scripts/reset_test_db.py
```

---

## 8. Incident Response & Operations

### Incident Response Procedure

1. **Detect** — Monitoring alerts trigger (Prometheus/Grafana)
2. **Assess** — Check `/api/v1/admin/health` for system status
3. **Contain** — Route traffic away from affected service (Kong routing rules)
4. **Mitigate** — Apply circuit breaker, scale replicas, roll back deployment
5. **Resolve** — Fix root cause, verify health checks pass
6. **Post-mortem** — Document in incident report, update runbooks

### Rollback Procedure

```bash
# 1. Identify last good version
kubectl rollout history deployment/ai-gateway-service

# 2. Rollback to previous revision
kubectl rollout undo deployment/ai-gateway-service --to-revision=2

# 3. For database rollbacks (use with caution)
alembic downgrade -1

# 4. Verify health
kubectl rollout status deployment/ai-gateway-service
```

### Backup & Restore

**PostgreSQL backup (daily):**
```bash
# Create backup
pg_dump -h $DB_HOST -U $DB_USER $DB_NAME > backup_$(date +%Y%m%d).sql

# Restore from backup
psql -h $DB_HOST -U $DB_USER $DB_NAME < backup_20260809.sql
```

**Redis backup (daily):**
```bash
# RDB snapshot
redis-cli BGSAVE

# AOF persistence
redis-cli BGREWRITEAOF
```

**MinIO backup (daily):**
```bash
# Create bucket-level backup
mc mirror salesgenie/minio/ backups/minio_$(date +%Y%m%d)/
```

### Common Troubleshooting

| Issue | Check | Fix |
|-------|-------|-----|
| Service won't start | `docker-compose logs auth-service` | Check env vars, DB connectivity |
| 502 Bad Gateway | API Gateway logs | Check service readiness probe |
| JWT expired | Auth service logs | Refresh token, check clock sync |
| Rate limit hit | Response `429` | Upgrade plan tier, use batching |
| Migration failed | `alembic current` | Check for conflicting changes |
| LLM timeout | AI Gateway logs | Check provider status, reduce token count |
| Webhook not received | Provider dashboard | Verify webhook URL, check signature |
| Vector search slow | pgvector index | `CREATE INDEX ON embeddings USING ivfflat` |
| CORS error | Browser console | Check `BACKEND_CORS_ORIGINS` in config |
| Token quota exceeded | Billing service | Upgrade plan, wait for reset |

### Monitoring Dashboards

| Dashboard | Description |
|-----------|-------------|
| System Overview | All service health, CPU/memory, uptime |
| AI Usage | Token usage, cost, provider performance |
| Rate Limits | Real-time rate limit status per tenant |
| Database | Query performance, connection pool, slow queries |
| Frontend | Page load times, error rates, user flows |
| Security | Failed logins, suspicious activity, RBAC violations |
