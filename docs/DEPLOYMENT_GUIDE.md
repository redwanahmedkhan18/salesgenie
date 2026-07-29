# SalesGenie Deployment Guide

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Local Development Deployment](#local-development-deployment)
3. [Production Deployment](#production-deployment)
4. [Kubernetes Deployment](#kubernetes-deployment)
5. [Environment Configuration](#environment-configuration)
6. [Database Setup](#database-setup)
7. [Service Configuration](#service-configuration)
8. [Monitoring & Logging](#monitoring--logging)
9. [Security Configuration](#security-configuration)
10. [Troubleshooting](#troubleshooting)
11. [Rollback Procedures](#rollback-procedures)
12. [FAQ](#faq)

---

## Prerequisites

### Local Development

- **Docker**: 24.0+
- **Docker Compose**: 2.20+
- **Node.js**: 22.x
- **Python**: 3.12+
- **Poetry**: 1.8+

### Production

- **Kubernetes**: 1.28+
- **kubectl**: 1.28+
- **Helm**: 3.13+
- **AWS/GCP/Azure CLI**
- **Terraform**: 1.6+

---

## Local Development Deployment

### Quick Start

```bash
# 1. Clone repository
git clone https://github.com/salesgenie/salesgenie.git
cd salesgenie

# 2. Set environment variables
cp enterprise-ai-platform/.env.example .env
# Edit .env with your values

# 3. Start infrastructure
docker-compose up -d postgres redis minio

# 4. Run migrations
poetry run alembic upgrade head

# 5. Start backend services
poetry run uvicorn enterprise_ai_platform.api_gateway.main:app --port 8000
# Start other services similarly or use docker-compose

# 6. Start frontend
npm ci
npm run dev

# 7. Access
# Frontend: http://localhost:3000
# API: http://localhost:8000/api/v1
```

### Docker Compose Setup

```yaml
# docker-compose.yml
version: '3.8'
services:
  frontend:
    build: ./frontend
    ports: ["3000:3000"]
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
    depends_on: [api-gateway]

  api-gateway:
    build: ./enterprise-ai-platform/api-gateway
    ports: ["8000:8000"]
    environment:
      - AUTH_SERVICE_URL=http://localhost:8001
      - POSTGRES_URL=postgresql://...

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: salesgenie
      POSTGRES_USER: salesgenie
      POSTGRES_PASSWORD: password
    volumes: ["postgres_data:/var/lib/postgresql/data"]

  redis:
    image: redis:7-alpine
```

### Running Tests Locally

```bash
# Unit tests
poetry run pytest tests/unit/ -v

# Integration tests
poetry run pytest tests/integration/ -v

# E2E tests
npx playwright test

# Load tests
locust -f tests/load-tests/locustfile.py
```

---

## Production Deployment

### Prerequisites

1. Kubernetes cluster (EKS/GKE/AKS)
2. Docker registry (DockerHub, ECR, GCR)
3. TLS certificate (Let's Encrypt)
4. Domain name (salesgenie.ai)
5. External database (RDS/Cloud SQL)

### Deployment Steps

#### Step 1: Build Docker Images

```bash
# Build all services
docker build -t salesgenie/api-gateway:latest -f enterprise-ai-platform/api-gateway/Dockerfile .
docker build -t salesgenie/lead-intelligence-service:latest -f enterprise-ai-platform/lead-intelligence-service/Dockerfile .
docker build -t salesgenie/whatsapp-service:latest -f enterprise-ai-platform/whatsapp-service/Dockerfile .

# Push to registry
docker push salesgenie/api-gateway:latest
docker push salesgenie/lead-intelligence-service:latest
docker push salesgenie/whatsapp-service:latest
```

#### Step 2: Create Kubernetes Namespace

```bash
kubectl create namespace salesgenie
```

#### Step 3: Apply Kubernetes Manifests

```bash
kubectl apply -f kubernetes/salesgenie-production.yaml -n salesgenie
```

#### Step 4: Configure Ingress

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: salesgenie-ingress
  namespace: salesgenie
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/rate-limit: "100"
spec:
  tls:
  - hosts: [salesgenie.ai, www.salesgenie.ai]
    secretName: salesgenie-tls
  rules:
  - host: salesgenie.ai
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 3000
      - path: /api/v1
        pathType: Prefix
        backend:
          service:
            name: api-gateway
            port:
              number: 80
```

#### Step 5: Verify Deployment

```bash
# Check pods
kubectl get pods -n salesgenie

# Check services
kubectl get svc -n salesgenie

# Check ingress
kubectl get ingress -n salesgenie

# Port forward for testing
kubectl port-forward svc/api-gateway 8000:80 -n salesgenie
```

---

## Kubernetes Deployment

### Helm Chart Structure

```
helm/
├── Chart.yaml
├── values.yaml
├── templates/
│   ├── namespace.yaml
│   ├── secrets.yaml
│   ├── configmap.yaml
│   ├── postgres/
│   │   ├── statefullset.yaml
│   │   ├── service.yaml
│   │   └── pvc.yaml
│   ├── redis/
│   ├── api-gateway/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── hpa.yaml
│   ├── lead-intelligence-service/
│   ├── whatsapp-service/
│   └── ingress.yaml
└── README.md
```

### Installing with Helm

```bash
# Add repository
helm repo add salesgenie https://salesgenie.github.io/charts
helm repo update

# Install
helm install salesgenie salesgenie/salesgenie \
  --namespace salesgenie \
  --create-namespace \
  --set env=production \
  --set image.pullPolicy=Always
```

### Helm Values

```yaml
# values.yaml
replicaCount: 2

image:
  repository: salesgenie/api-gateway
  tag: latest
  pullPolicy: Always

env:
  ENVIRONMENT: production
  DEBUG: false

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 200m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70

postgres:
  enabled: true
  postgresql:
    postgresqlDatabase: salesgenie
    postgresqlUsername: salesgenie
    postgresqlPassword: ${POSTGRES_PASSWORD}

redis:
  enabled: true
  architecture: standalone
  auth:
    enabled: false
```

---

## Environment Configuration

### Required Environment Variables

```bash
# Database
POSTGRES_USER=salesgenie
POSTGRES_PASSWORD=secure_password
POSTGRES_HOST=postgres.salesgenie.svc.cluster.local
POSTGRES_PORT=5432
POSTGRES_DB=salesgenie_db

# Redis
REDIS_URL=redis://redis:6379/0

# JWT
JWT_SECRET_KEY=super_secret_key_change_in_production
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_DAYS=14

# LLM Providers
GROQ_API_KEY=gsk_your_key
OPENAI_API_KEY=sk_your_key
GOOGLE_API_KEY=AIza_your_key
ANTHROPIC_API_KEY=sk_your_key

# WhatsApp
WHATSAPP_ACCESS_TOKEN=your_token
WHATSAPP_PHONE_NUMBER_ID=your_phone_id
WHATSAPP_WEBHOOK_URL=https://salesgenie.ai/api/v1/whatsapp/webhook

# Stripe
STRIPE_SECRET_KEY=sk_live_your_key
STRIPE_WEBHOOK_SECRET=whsec_your_key

# Security
BACKEND_CORS_ORIGINS=https://salesgenie.ai,https://app.salesgenie.ai

# Language
DEFAULT_LANGUAGE=en
SUPPORTED_LANGUAGES=en,es,fr,de,it,pt,nl,zh,ja,ko,ar,hi
```

### .env File Template

```bash
# .env.production
ENVIRONMENT=production
DEBUG=false

# Services
AUTH_SERVICE_URL=https://api.salesgenie.ai
USER_SERVICE_URL=https://api.salesgenie.ai
POSTGRES_URL=postgresql://salesgenie:password@postgres:5432/salesgenie_db
REDIS_URL=redis://redis:6379/0

# LLM
GROQ_API_KEY=${GROQ_API_KEY}
OPENAI_API_KEY=${OPENAI_API_KEY}

# Webhooks
WHATSAPP_WEBHOOK_SECRET=${WHATSAPP_WEBHOOK_SECRET}
STRIPE_WEBHOOK_SECRET=${STRIPE_WEBHOOK_SECRET}
```

---

## Database Setup

### Initial Migration

```bash
# Create migration directory
mkdir -p migrations/versions

# Generate migration
alembic revision --autogenerate -m "initial migration"

# Apply migration
alembic upgrade head
```

### Migration File Example

```python
# migrations/versions/001_initial.py
def upgrade():
    # Create tables
    op.create_table('lead_intelligence_companies',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('tenant_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('language', sa.String(10), nullable=True, default='en'),
        sa.Column('created_at', sa.DateTime(timezone=True), default=datetime.utcnow),
    )
    
    # Create indexes
    op.create_index('idx_companies_tenant', 'lead_intelligence_companies', ['tenant_id'])
    op.create_index('idx_companies_language', 'lead_intelligence_companies', ['language'])

def downgrade():
    op.drop_table('lead_intelligence_companies')
```

### Database Connection Pool

```python
# Connection pool settings
DB_POOL_SIZE=20
DB_MAX_OVERFLOW=10
DB_POOL_TIMEOUT=30
DB_POOL_RECYCLE=3600
```

---

## Service Configuration

### API Gateway Configuration

```yaml
# api-gateway.yaml
service:
  name: api-gateway
  port: 8000
  replicas: 3
  
rate_limiting:
  enabled: true
  requests_per_minute: 100
  
cors:
  origins:
    - https://salesgenie.ai
    - https://app.salesgenie.ai
    
logging:
  level: INFO
  format: json
```

### Lead Intelligence Service Configuration

```yaml
# lead-intelligence-service.yaml
service:
  name: lead-intelligence-service
  port: 8022
  replicas: 2
  
ai:
  provider: groq
  model: gpt-4o-mini
  temperature: 0.7
  max_tokens: 4000
  
cache:
  ttl: 3600
  prefix: lead_intelligence:
```

### WhatsApp Service Configuration

```yaml
# whatsapp-service.yaml
service:
  name: whatsapp-service
  port: 8018
  replicas: 2
  
webhook:
  verify_token: ${WHATSAPP_VERIFY_TOKEN}
  url: https://api.salesgenie.ai/api/v1/whatsapp/webhook
  
rate_limit:
  messages_per_second: 10
  messages_per_day: 10000
```

---

## Monitoring & Logging

### Prometheus Metrics

```bash
# Service metrics
GET /metrics

# Key metrics
http_requests_total{service="api-gateway", status="200"}
http_request_duration_seconds{path="/api/v1/lead-intelligence/companies/search"}
database_connection_pool_used_connections
ai_tokens_used_total
```

### Grafana Dashboards

1. **System Overview**: CPU, memory, disk
2. **API Performance**: Latency, error rates
3. **Database**: Connections, queries
4. **AI Usage**: Tokens, costs, latency
5. **Business Metrics**: Revenue, conversions

### Logging Format

```json
{
  "timestamp": "2026-07-30T00:00:00Z",
  "level": "INFO",
  "service": "api-gateway",
  "request_id": "req_123456",
  "user_id": "user_789",
  "path": "/api/v1/auth/login",
  "method": "POST",
  "status": 200,
  "duration_ms": 45,
  "message": "Request processed successfully"
}
```

### Alerting Rules

```yaml
# Prometheus alerts
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
  for: 5m
  labels:
    severity: critical
  annotations:
    summary: "High error rate detected"

- alert: DatabaseDown
  expr: up{job="postgres"} == 0
  for: 1m
  labels:
    severity: critical
  annotations:
    summary: "Database is down"
```

---

## Security Configuration

### TLS Configuration

```yaml
# cert-manager cluster issuer
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: security@salesgenie.ai
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
```

### Network Policies

```yaml
# Network policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-gateway-policy
  namespace: salesgenie
spec:
  podSelector:
    matchLabels:
      app: api-gateway
  ingress:
  - from:
    - ipBlock:
        cidr: 0.0.0.0/0
    ports:
    - protocol: TCP
      port: 8000
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: auth-service
```

### Secret Management

```bash
# Using HashiCorp Vault
vault kv put secret/salesgenie/prod \
  POSTGRES_PASSWORD="secure_password" \
  JWT_SECRET_KEY="super_secret_key" \
  GROQ_API_KEY="gsk_your_key"

# Kubernetes secret from Vault
kubectl create secret generic salesgenie-secrets \
  --from-literal=POSTGRES_PASSWORD="secure_password" \
  --from-literal=JWT_SECRET_KEY="super_secret_key"
```

---

## Troubleshooting

### Common Issues

#### Service Won't Start

```bash
# Check logs
kubectl logs -n salesgenie deployment/api-gateway

# Check events
kubectl describe pod -n salesgenie

# Check configuration
kubectl exec -n salesgenie deployment/api-gateway -- env | grep POSTGRES
```

#### Database Connection Issues

```bash
# Check PostgreSQL
kubectl exec -n salesgenie postgres-0 -- psql -U salesgenie -d salesgenie_db -c "SELECT 1;"

# Check connection pool
SELECT * FROM pg_stat_activity WHERE datname = 'salesgenie_db';
```

#### High Latency

```bash
# Check resource usage
kubectl top pods -n salesgenie

# Check database queries
SELECT * FROM pg_stat_statements ORDER BY total_time DESC LIMIT 10;
```

### Debug Commands

```bash
# Port forward for debugging
kubectl port-forward svc/api-gateway 8000:80 -n salesgenie

# Exec into pod
kubectl exec -it -n salesgenie deployment/api-gateway -- /bin/sh

# Check service endpoints
kubectl get endpoints -n salesgenie

# Describe service
kubectl describe svc api-gateway -n salesgenie
```

---

## Rollback Procedures

### Kubernetes Rollback

```bash
# Rollback deployment
kubectl rollout undo deployment/api-gateway -n salesgenie

# Rollback to specific revision
kubectl rollout undo deployment/api-gateway --to-revision=3 -n salesgenie

# Check rollout status
kubectl rollout status deployment/api-gateway -n salesgenie
```

### Database Rollback

```bash
# Downgrade migration
alembic downgrade -1

# Downgrade to specific version
alembic downgrade base

# Check current version
alembic current
```

### Emergency Rollback Checklist

1. ✅ Verify backup exists
2. ✅ Document current state
3. ✅ Notify team
4. ✅ Execute rollback
5. ✅ Verify system health
6. ✅ Update documentation

---

## FAQ

### Q: How do I add a new service?

1. Create Dockerfile in service directory
2. Add service to docker-compose.yml
3. Add to Kubernetes manifests
4. Update API Gateway routes
5. Configure environment variables

### Q: How do I enable a new language?

1. Add language to SUPPORTED_LANGUAGES in .env
2. Add translation files to frontend
3. Update API Gateway routes if needed
4. Test with language selector

### Q: How do I scale the system?

```bash
# Horizontal pod autoscaling
kubectl scale deployment api-gateway --replicas=10 -n salesgenie

# Vertical pod autoscaling
kubectl apply -f vpa.yaml -n salesgenie
```

### Q: How do I monitor costs?

1. Enable AWS Cost Explorer
2. Set up billing alerts
3. Monitor LLM token usage
4. Review resource utilization

### Q: How do I rotate secrets?

```bash
# Update secret
kubectl create secret generic salesgenie-secrets \
  --from-literal=JWT_SECRET_KEY="new_secret_key" \
  --dry-run=client -o yaml | kubectl apply -f -

# Restart pods to pick up new secrets
kubectl rollout restart deployment/api-gateway -n salesgenie
```

---

## Contact & Support

- **Documentation**: https://docs.salesgenie.ai
- **Status Page**: https://status.salesgenie.ai
- **Support**: support@salesgenie.ai
- **Security**: security@salesgenie.ai

---

## License

Copyright © 2024 SalesGenie. All rights reserved.