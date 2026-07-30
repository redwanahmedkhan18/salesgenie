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
- API Gateway (Port 8000)
- Auth Service (Port 8001)
- User Service (Port 8002)
- Organization Service (Port 8003)
- Billing Service (Port 8004)
- Analytics Service (Port 8012)
- Lead Intelligence Service (Port 8022)
- WhatsApp Service (Port 8018)
- AI Gateway Service (Port 8000)
- And 11 more...

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

# Start infrastructure
docker-compose up -d postgres redis minio

# Run migrations
alembic upgrade head

# Start services
poetry run uvicorn enterprise_ai_platform.api_gateway.main:app --port 8000
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