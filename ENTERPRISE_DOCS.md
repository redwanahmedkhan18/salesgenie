# SalesGenie Enterprise Documentation

## Overview

SalesGenie is an enterprise-grade AI Customer Support & Sales Platform designed for organizations from startups to Fortune 500 companies.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Architecture](#architecture)
3. [API Reference](#api-reference)
4. [Deployment](#deployment)
5. [Security](#security)
6. [Monitoring](#monitoring)
7. [CI/CD](#ci-cd)
8. [Troubleshooting](#troubleshooting)

## Getting Started

### Prerequisites

- Python 3.12+
- PostgreSQL 15+
- Redis 7+
- Kubernetes 1.30+
- Docker 24+

### Quick Start

```bash
# Clone repository
git clone https://github.com/salesgenie/salesgenie.git
cd salesgenie

# Set environment variables
export DATABASE_URL="postgresql://user:pass@localhost/salesgenie"
export REDIS_URL="redis://localhost:6379"

# Run migrations
python3 database/migrate.py upgrade

# Start services
python3 enterprise-ai-platform/ai-gateway-service/main.py &
python3 enterprise-ai-platform/auth-service/main.py &
```

## Architecture

### System Components

```mermaid
graph TD
    A[Users] --> B[Cloudflare CDN/WAF]
    B --> C[Nginx Reverse Proxy]
    C --> D[Kong API Gateway]
    D --> E[Keycloak Auth]
    E --> F[SalesGenie Services]
    F --> G[PostgreSQL]
    F --> H[Redis]
    F --> I[Kafka]
```

### Microservices

| Service | Port | Purpose |
|---------|------|---------|
| AI Gateway | 8000 | AI orchestration |
| Auth Service | 8001 | Authentication |
| User Service | 8002 | User management |
| Organization Service | 8003 | Multi-tenancy |
| Billing Service | 8004 | Payments |
| AI Gateway Service | 8000 | LLM routing |
| Knowledge Service | 8006 | RAG |
| Sales Service | 8007 | Lead qualification |
| Ticket Service | 8008 | Support tickets |
| Vector Service | 8009 | Embeddings |
| ... | ... | ... |

## API Reference

### Authentication

```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

Response:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 3600
}
```

### Rate Limiting

Default limits:
- Global: 100,000 requests/minute
- Auth endpoints: 10 requests/minute
- AI endpoints: Configurable per model

Response headers:
```
X-RateLimit-Limit: 100000
X-RateLimit-Remaining: 99950
X-RateLimit-Reset: 2026-08-03T14:30:00Z
```

## Deployment

### Kubernetes

```bash
# Deploy to production
kubectl apply -f deployment/kubernetes/manifests/

# Check deployment
kubectl get pods -n salesgenie
kubectl get services -n salesgenie
```

### Environment Variables

```
ENVIRONMENT=production
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
JWT_SECRET=<32-char-secret>
STRIPE_SECRET_KEY=sk_live_...
```

## Security

### Security Features

- OAuth 2.0 / OIDC
- JWT authentication (15 min access, 30 day refresh)
- MFA (TOTP, SMS)
- ABAC + RBAC
- Role-Based Access Control
- Rate limiting
- WAF
- Audit logging

### Compliance

- GDPR
- SOC 2 Type II
- HIPAA
- ISO 27001
- PCI DSS

## Monitoring

### Metrics

- Prometheus metrics at `/metrics`
- Health checks at `/health`, `/ready`, `/live`
- Request tracing via Jaeger

### Grafana Dashboards

Access: `https://monitoring.salesgenie.ai`
- Security Dashboard
- System Metrics
- AI Performance
- Business Metrics

## CI/CD

### Pipeline Steps

1. **Test** - Unit, integration, security scans
2. **Security** - Vulnerability scans
3. **Build** - Docker image build
4. **Deploy** - Kubernetes deployment
5. **Performance** - Load tests

### Branch Strategy

- `main` - Production
- `develop` - Staging
- `feature/*` - Development

## Troubleshooting

### Common Issues

**Service not starting:**
```bash
kubectl logs -n salesgenie salesgenie-ai-gateway-X
kubectl describe pod -n salesgenie salesgenie-ai-gateway-X
```

**Database errors:**
```bash
kubectl exec -n salesgenie postgres-pod - -- psql -U postgres
```

**High latency:**
1. Check Grafana dashboard
2. Review Prometheus alerts
3. Check Kubernetes resource usage

### Support

- Slack: https://salesgenie.slack.com
- Email: support@salesgenie.ai
- Status: https://status.salesgenie.ai