# SalesGenie Enterprise AI Platform - Full System Documentation

## Executive Summary

SalesGenie is a FAANG-grade enterprise AI platform that automates customer support, sales qualification, and knowledge management through AI agents. The platform handles millions of concurrent conversations with sub-200ms response times.

---

## Table of Contents

1. [System Architecture](#system-architecture)
2. [Backend Services](#backend-services)
3. [Frontend Features](#frontend-features)
4. [Technology Stack](#technology-stack)
5. [Data Architecture](#data-architecture)
6. [AI/ML Architecture](#aiml-architecture)
7. [Security Model](#security-model)
8. [Multi-Language Support](#multi-language-support)
9. [API Gateway & Routing](#api-gateway--routing)
10. [Infrastructure](#infrastructure)

---

## System Architecture

### High-Level Architecture

```
                    Users
                      |
              CDN / WAF
                      |
           Load Balancer
                      |
    ┌──────────────────────────────────┐
    │         API Gateway              │
    │   (Rate Limiting, Auth)          │
    └──────────────┬───────────────────┘
                   |
    ┌──────────────┴───────────────────┐
    │       Application Services       │
    ├──────────────────────────────────┤
    │  Auth  │  Users  │  Org  │  Billing│
    ├──────────────────────────────────┤
    │  Knowledge  │  Search  │  Vector │
    ├──────────────────────────────────┤
    │  AI Gateway  │  Agents  │  Tools │
    ├──────────────────────────────────┤
    │  WhatsApp │ Telegram │ Email  │
    ├──────────────────────────────────┤
    │  Lead Intelligence Service         │
    └──────────────┬───────────────────┘
                   |
    ┌──────────────┴───────────────────┐
    │         Data Layer             │
    ├──────────────────────────────────┤
    │ PostgreSQL │ Redis │ Vector DB  │
    └──────────────────────────────────┘
```

### Design Principles

- **Microservices**: Independent deployable units
- **Zero Trust Security**: Every request authenticated and authorized
- **Defense in Depth**: Multiple security layers
- **Event-Driven**: Kafka for async communication
- **Scalable**: Horizontal scaling with Kubernetes

---

## Backend Services

### Core Services (Port 8001-8022)

| Service | Port | Description |
|---------|------|-------------|
| **Auth Service** | 8001 | JWT/OAuth authentication, MFA, session management |
| **User Service** | 8002 | User profiles, preferences, language settings |
| **Organization Service** | 8003 | Multi-tenant org management, RBAC |
| **Billing Service** | 8004 | Stripe integration, subscriptions, invoices |
| **Notification Service** | 8005 | Email, SMS, push notifications |
| **Knowledge Service** | 8006 | Document management, OCR, search |
| **Sales Service** | 8007 | Leads, opportunities, bookings |
| **Ticket Service** | 8008 | Support tickets, escalations |
| **Vector Service** | 8009 | Embeddings, similarity search |
| **AI Gateway Service** | 8000 | LLM routing, prompt management |
| **Workflow Service** | 8011 | Workflow orchestration |
| **Analytics Service** | 8012 | KPIs, metrics, dashboards |
| **Search Service** | 8013 | Full-text search |
| **Audit Service** | 8014 | Audit logs, compliance |
| **File Service** | 8015 | File storage, uploads |
| **Customer Service** | 8016 | Customer 360, segments |
| **Support Service** | 8017 | Support knowledge base |
| **Conversation Service** | 8018 | Conversation history |
| **WhatsApp Service** | 8018 | Meta WhatsApp Business API |
| **Telegram Service** | 8019 | Telegram bot integration |
| **Messenger Service** | 8020 | Facebook Messenger |
| **Email Service** | 8021 | SMTP/SendGrid email |
| **Lead Intelligence Service** | 8022 | AI lead discovery, qualification |

### WhatsApp Service Features

- **Multi-number support**: Multiple WhatsApp numbers per organization
- **Template management**: Pre-approved message templates
- **Webhook handling**: Real-time message processing
- **Media support**: Images, videos, documents
- **Conversation sessions**: Track conversation state
- **Multi-language**: Messages in 150+ languages

### Lead Intelligence Service Features

- **Company Discovery**: Search companies by industry, location, size
- **Contact Enrichment**: Find decision makers and contacts
- **AI Qualification**: Lead scoring with reasoning
- **Research Briefs**: AI-generated company analysis
- **Outreach Drafts**: Personalized messages for email, LinkedIn, WhatsApp
- **Search Profiles**: Saved search criteria with scheduling

---

## Frontend Features

### Dashboard
- Real-time KPIs with charts
- Revenue tracking
- AI accuracy metrics
- Active conversations
- Token usage

### Agent Builder
- Visual workflow designer
- Tool integration
- Memory management
- Prompt templates
- Version control

### Lead Intelligence
- Company search with filters
- Lead scoring visualization
- Qualification reports
- Outreach draft generation
- Search profile management

### Channels
- WhatsApp Business integration
- Telegram bot setup
- Email configuration
- Messenger integration
- Channel health monitoring

### Knowledge Base
- Document upload with OCR
- Category management
- Search with filters
- Version history
- Access control

### CRM
- Customer 360 view
- Lead management
- Opportunity tracking
- Activity timeline
- Custom fields

---

## Technology Stack

### Backend

| Layer | Technology | Version |
|-------|------------|---------|
| **Framework** | FastAPI | 0.110+ |
| **Database** | PostgreSQL + pgvector | 16+ |
| **ORM** | SQLAlchemy 2.0 | 2.0+ |
| **Auth** | OAuth2/JWT | - |
| **Queue** | Redis + RQ | 7+ |
| **Cache** | Redis | 7+ |
| **Vector DB** | pgvector | 0.7+ |
| **Search** | PostgreSQL Full-Text | 16+ |
| **LLM** | Groq, OpenAI, Gemini, Anthropic | - |
| **Embeddings** | OpenAI, Cohere | - |
| **Containerization** | Docker | 24+ |
| **Orchestration** | Kubernetes | 1.28+ |
| **Service Mesh** | Istio | 1.20+ |
| **Monitoring** | Prometheus, Grafana | - |
| **Logging** | ELK Stack | - |
| **Tracing** | OpenTelemetry | - |
| **CI/CD** | GitHub Actions | - |

### Frontend

| Layer | Technology | Version |
|-------|------------|---------|
| **Framework** | Astro | 4+ |
| **UI** | React | 19+ |
| **Language** | TypeScript | 5+ |
| **Styling** | Tailwind CSS | 4+ |
| **State** | Zustand | 4+ |
| **HTTP** | Axios/Fetch | - |
| **Testing** | Jest, Playwright | - |
| **Build** | Vite | 5+ |

### AI/ML Stack

| Component | Technology |
|-----------|------------|
| **LLM Provider** | Groq (primary), OpenAI, Gemini, Anthropic |
| **Embedding** | OpenAI, Cohere, Voyage |
| **Vector DB** | pgvector |
| **RAG** | LangChain/LangGraph |
| **Agent Framework** | Custom with tool calling |
| **Prompt Management** | YAML-based templates |
| **Evaluation** | LangSmith, Arize AI |

---

## Data Architecture

### Database Schema

**Multi-Tenant Isolation**
```sql
-- Every table has tenant_id for isolation
SELECT * FROM customers WHERE tenant_id = 'org_123';
```

**Key Tables**

1. **Users**: Authentication, profiles, preferences
2. **Organizations**: Tenant management, RBAC
3. **Customers**: Customer 360, segments, tags
4. **Conversations**: Chat history, messages
5. **Documents**: Knowledge base, embeddings
6. **Leads**: Lead intelligence, scores
7. **Tickets**: Support tickets, SLA
8. **Agents**: AI agent definitions, memory
9. **Workflows**: Automation workflows
10. **Audit Logs**: Compliance, security

### Vector Embeddings

```
Document → Text Splitter → Embedding Model → pgvector → Similarity Search
```

- **Index Type**: HNSW (Hierarchical Navigable Small World)
- **Dimensions**: 1536 (OpenAI text-embedding-3-small)
- **Distance**: Cosine similarity
- **MCP Integration**: Real-time retrieval from multiple knowledge sources

---

## AI/ML Architecture

### RAG Pipeline

```
User Query → Query Processing → Embedding → Vector Search → 
Context Retrieval → Prompt Assembly → LLM Generation → Response
```

### Agent Architecture

```
User Message → Intent Classification → Tool Selection → 
Tool Execution → Context Building → LLM Response → 
Response Validation → Output
```

### Prompt Injection Protection

- Input sanitization
- Prompt isolation
- Output validation
- Tool restrictions

### Model Management

- **Version Control**: Git-based prompt versioning
- **A/B Testing**: Model comparison
- **Fallback**: Multiple LLM providers
- **Caching**: Response caching for repeated queries

---

## Security Model

### Zero Trust Architecture

```
Never Trust → Always Verify
     │              │
     ▼              ▼
  Authenticated  Authorized
     │              │
     ▼              ▼
  Validated      Monitored
     │              │
     ▼              ▼
   Executed
```

### Authentication

- **JWT**: 15-60 min access tokens
- **Refresh**: 7-30 days
- **MFA**: TOTP, SMS, Email
- **OAuth**: Google, Microsoft, Okta, Auth0

### Authorization

- **RBAC**: Role-Based Access Control
- **ABAC**: Attribute-Based Access Control
- **Permissions**: `resource.action` format
- **Tenant Isolation**: Database-level filtering

### Data Protection

- **Encryption**: AES-256 at rest, TLS 1.3 in transit
- **Secrets**: HashiCorp Vault, AWS Secrets Manager
- **PII Handling**: GDPR, CCPA compliant
- **Audit Logs**: All access logged

---

## Multi-Language Support

### Supported Languages (150+)

- **English**: en, en-US, en-GB
- **European**: es, fr, de, it, pt, nl, sv, da, fi, no, pl, cs, sk, hu, ro, bg, ru
- **Asian**: zh, ja, ko, th, vi, id, ms
- **Middle East**: ar, he, fa, ps, ur
- **Indian Subcontinent**: hi, bn, ta, te, mr, gu, kn, ml, pa, or
- **African**: sw, yo, ig, ha,zu,af,xh,st

### Language Features

- **UI Translation**: Full interface localization
- **LLM Responses**: Native language responses
- **RTL Support**: Arabic, Hebrew, Persian
- **Language Detection**: Automatic detection
- **User Preferences**: Per-user language settings

---

## API Gateway & Routing

### Service Registry

```yaml
auth: /api/v1/auth/* → auth-service:8001
users: /api/v1/users/* → user-service:8002
organizations: /api/v1/organizations/* → organization-service:8003
billing: /api/v1/billing/* → billing-service:8004
knowledge: /api/v1/knowledge/* → knowledge-service:8006
sales: /api/v1/sales/* → sales-service:8007
tickets: /api/v1/tickets/* → ticket-service:8008
search: /api/v1/search/* → search-service:8013
ai: /api/v1/agents/* → ai-gateway-service:8000
whatsapp: /api/v1/whatsapp/* → whatsapp-service:8018
lead-intelligence: /api/v1/lead-intelligence/* → lead-intelligence-service:8022
```

### Rate Limiting

| Tier | Requests/Min | AI Tokens/Hour |
|------|--------------|----------------|
| Free | 60 | 100,000 |
| Starter | 120 | 500,000 |
| Growth | 300 | 2,000,000 |
| Enterprise | 1000+ | 10,000,000+ |

### API Standards

- **RESTful**: Standard HTTP methods
- **JSON**: Request/response format
- **OpenAPI**: Auto-generated docs
- **Versioning**: `/api/v1/`
- **Pagination**: Cursor-based
- **Filtering**: Query parameters
- **Sorting**: Order by field

---

## Infrastructure

### Deployment Architecture

```
Internet → CDN/WAF → Load Balancer → API Gateway → Services → Databases
```

### High Availability

- **Multi-AZ**: Kubernetes across availability zones
- **Auto Scaling**: HPA based on CPU/memory
- **Replication**: PostgreSQL streaming replication
- **Backups**: Daily automated backups
- **Disaster Recovery**: RTO < 1hr, RPO < 5min

### Monitoring Stack

- **Metrics**: Prometheus + Grafana
- **Logs**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Tracing**: OpenTelemetry + Jaeger
- **Alerting**: PagerDuty, Slack
- **AI Monitoring**: LangSmith, Arize AI

### Cost Optimization

- **Spot Instances**: For batch processing
- **Auto Pause**: Development environments
- **Caching**: Redis for frequent queries
- **CDN**: CloudFront for static assets
- **Database**: Connection pooling, read replicas