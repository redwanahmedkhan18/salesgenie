# SalesGenie Enterprise AI Platform

FAANG-level AI Sales & Customer Support Automation Platform.

## Quick Links

- **[Deployment Guide](README.md#table-of-contents)** - How to deploy locally and to production
- **[System Documentation](SYSTEM_DOCUMENTATION.md)** - Full architecture, services, and technology stack
- **[Security Standards](SECURITY.md)** - Enterprise security engineering guidelines
- **[Design Document](DESIGN.md)** - System design and data architecture

## Overview

SalesGenie is a multi-service microservices architecture that handles:
- AI-powered customer support and sales automation
- WhatsApp Business API integration
- Lead intelligence and qualification
- Real-time analytics and monitoring

## Architecture

```
Users → API Gateway → Microservices → PostgreSQL/Redis/Vector DB
```

**19 Microservices:**

| Service | Port | Description |
|---------|------|-------------|
| API Gateway | 8000 | API routing and gateway |
| Auth Service | 8001 | JWT authentication |
| User Service | 8002 | User management |
| Organization Service | 8003 | Organization Tenancy |
| Billing Service | 8004 | Stripe integration |
| Analytics Service | 8010 | Analytics and metrics |
| WhatsApp Service | 8005 | WhatsApp Business API |
| Telegram Service | 8019 | Telegram Bot integration |
| Messenger Service | 8020 | Facebook Messenger |
| Email Service | 8021 | Email sending (Mailpit dev mode) |
| Lead Intelligence | 8022 | AI lead qualification |
| AI Gateway | 8000 | AI gateway routing |
| And 7 more... | | Chat, Support, Ticket, Knowledge, Workflow, Search, Vector |

## Technology Stack

| Layer | Technology |
|-------|------------|
| **API** | FastAPI, Python 3.10+ |
| **Frontend** | Astro, React, TypeScript |
| **Database** | PostgreSQL 16, Redis 7 |
| **Vector DB** | pgvector |
| **LLM** | Groq, OpenAI, Gemini, Anthropic |
| **Containerization** | Docker, Kubernetes |
| **CI/CD** | GitHub Actions, Helm |

## Local Development

```bash
# Clone and setup
git clone https://github.com/salesgenie/salesgenie.git
cd salesgenie

# Start infrastructure (includes Mailpit for email testing)
docker-compose up -d postgres redis minio mailpit

# Run migrations
alembic upgrade head

# Start all services
./start-dev.sh
```

### Email Testing in Development

The Email Service uses **Mailpit** for zero-cost local email testing:

- **Web Interface**: http://localhost:8025
- **SMTP Server**: localhost:1025
- **No API keys required** - perfect for development

Configure in `.env`:
```env
SMTP_HOST=localhost
SMTP_PORT=1025
SMTP_USERNAME=
SMTP_PASSWORD=
SMTP_FROM_ADDRESS=noreply@salesgenie.local
```

### Running Individual Services

```bash
# Start specific services on their ports
poetry run uvicorn enterprise_ai_platform.email_service.main:app --port 8021
poetry run uvicorn enterprise_ai_platform.analytics_service.main:app --port 8010
poetry run uvicorn enterprise_ai_platform.whatsapp_service.main:app --port 8005
```

## Production Deployment

```bash
# Build images
docker build -t salesgenie/api-gateway -f enterprise-ai-platform/api-gateway/Dockerfile .

# Deploy to Kubernetes
helm install salesgenie ./helm/salesgenie \
  --namespace salesgenie \
  --create-namespace
```

## Security

- Zero Trust Architecture
- JWT Authentication
- RBAC + ABAC authorization
- AES-256 encryption
- TLS 1.3 everywhere

## Monitoring

- Prometheus metrics
- Grafana dashboards
- Structured JSON logging
- Sentry error tracking

## License

Copyright © 2024 SalesGenie. All rights reserved.