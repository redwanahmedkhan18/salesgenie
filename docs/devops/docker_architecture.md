# SalesGenie — Docker Architecture Requirements

**File:** `docker_architecture.md`  
**Product:** SalesGenie / FlowMind AI  
**Document Type:** User Requirements, System Requirements & Functional Requirements  
**Architecture:** Containerized Enterprise Multi-Tenant SaaS + Microservices + Event-Driven + Multi-Agent AI  
**Primary Actors:** End Users, Sales Agents, Support Agents, Organization Admins, Developers, DevOps Engineers, SREs, Security Engineers, Platform Engineers, Super Admins, AI Agents

---

## 1. Purpose

The Docker Architecture subsystem defines how SalesGenie services, AI workloads, databases, messaging infrastructure, development environments, testing environments, and supporting infrastructure are containerized, deployed, isolated, monitored, secured, and operated.

The Docker architecture MUST support:

- Microservices
- Multi-tenant SaaS
- Multi-agent AI
- AI Gateway
- RAG
- Knowledge management
- Lead intelligence
- Sales automation
- Customer support
- Workflow automation
- Omnichannel communications
- Search
- Analytics
- Notifications
- Billing
- Developer APIs
- Webhooks
- Data ingestion
- ETL/ELT
- Data lake
- Data warehouse
- Background workers
- Scheduled jobs
- Local development
- CI/CD
- Production deployment
- Horizontal scaling
- Failure isolation
- Security
- Observability
- Disaster recovery
- Human-in-the-loop operations
- AI-assisted infrastructure operations

---

## 2. Docker Architecture Goals

The Docker platform MUST optimize for:

1. Reproducibility
2. Portability
3. Isolation
4. Scalability
5. Security
6. Reliability
7. Developer productivity
8. Fast deployment
9. Fast rollback
10. Resource efficiency
11. Observability
12. Fault isolation
13. Infrastructure automation
14. AI workload isolation
15. Multi-environment consistency

---

## 3. Docker Architecture Principles

## DAP-001 — Immutable Containers

Production containers MUST be treated as immutable runtime artifacts.

Containers MUST NOT rely on manual changes made after startup.

---

## DAP-002 — One Primary Responsibility

Each application container SHOULD have one primary responsibility.

Examples:

```text
auth-service
lead-intelligence-service
ai-gateway
workflow-service
notification-service
```

---

## DAP-003 — Stateless by Default

Application containers SHOULD remain stateless whenever possible.

Persistent state MUST be externalized to durable infrastructure.

---

## DAP-004 — Twelve-Factor Compatibility

Services SHOULD follow cloud-native application principles:

* Environment-based configuration
* Externalized state
* Structured logs
* Disposable processes
* Explicit dependencies
* Reproducible builds

---

## DAP-005 — Least Privilege

Containers MUST run with the minimum privileges required.

---

## DAP-006 — Reproducible Builds

The same source revision MUST produce a deterministic or substantially reproducible container artifact.

---

## DAP-007 — Environment Parity

Development, staging, and production SHOULD use the same container images wherever practical.

Configuration MUST vary independently from application artifacts.

---

## 4. High-Level Docker Architecture

```text
                              USERS
                                |
                                v
                         +--------------+
                         | CDN / WAF    |
                         +------+-------+
                                |
                                v
                         +--------------+
                         | Load Balancer|
                         +------+-------+
                                |
                                v
                         +--------------+
                         | API Gateway  |
                         +------+-------+
                                |
                +---------------+----------------+
                |               |                |
                v               v                v
          Frontend         API Services      Developer APIs
                |               |                |
                +---------------+----------------+
                                |
                         Container Platform
                                |
        +-----------------------+-----------------------+
        |                       |                       |
        v                       v                       v
   Core Services           AI Services             Workers
        |                       |                       |
        |                 +-----+-----+                |
        |                 |           |                |
        |                 v           v                |
        |             AI Gateway    Agent Runtime       |
        |                 |           |                |
        |                 +-----+-----+                |
        |                       |                       |
        +-----------------------+-----------------------+
                                |
                           Event Bus
                                |
             +------------------+------------------+
             |                  |                  |
             v                  v                  v
        PostgreSQL           Redis           Object Storage
             |                  |                  |
             +------------------+------------------+
                                |
                       Data / Analytics Layer
                                |
             +------------------+------------------+
             |                  |                  |
             v                  v                  v
          ETL/ELT           Warehouse          Search
                                |
                         Observability Stack
                                |
                  +-------------+-------------+
                  |             |             |
                 Logs        Metrics        Traces
                                |
                         AI Operations
                                |
                  +-------------+-------------+
                  |             |             |
               SRE Agent    Cost Agent   Security Agent
```

---

## 5. Containerized Service Architecture

SalesGenie SHOULD separate major workloads into independently deployable containers.

Recommended logical services:

```text
Frontend
API Gateway
Auth Service
User Service
Organization Service
RBAC Service
Lead Intelligence Service
Sales Service
Support Service
Conversation Service
Omnichannel Service
WhatsApp Service
Email Service
Notification Service
Workflow Service
AI Gateway
Agent Runtime
RAG Service
Knowledge Service
Embedding Service
Document Intelligence Service
Search Service
Analytics Service
Metrics Service
Billing Service
Payment Service
Webhook Service
Developer API Service
API Key Service
Service Account Service
Scheduler
Task Workers
Event Consumers
Data Ingestion Service
ETL Workers
ELT Workers
Data Quality Service
Data Governance Service
Data Catalog Service
Data Lineage Service
```

---

## 6. User Requirements

## UR-001 — Reliable Application Access

Users MUST be able to access SalesGenie even when individual containers restart or fail.

---

## UR-002 — Consistent Experience

Container restarts MUST NOT unexpectedly destroy persistent user state.

---

## UR-003 — Secure Isolation

Users MUST only access services and data authorized for their tenant and role.

---

## UR-004 — Fast AI Responses

AI workloads MUST be independently scalable so that AI traffic does not unnecessarily degrade core application functionality.

---

## UR-005 — Reliable Background Processing

Long-running operations SHOULD execute asynchronously without blocking interactive requests.

---

## UR-006 — Reliable Notifications

Notification workers MUST be independently scalable and retry failed delivery attempts.

---

## UR-007 — Reliable Workflows

Workflow execution MUST survive individual worker/container failures.

---

## UR-008 — Search Availability

Search functionality SHOULD remain operational independently from transactional services.

---

## UR-009 — Analytics Isolation

Heavy analytics workloads MUST NOT unnecessarily consume resources required by interactive application services.

---

## 7. Developer Requirements

## UR-010

Developers MUST be able to start the required SalesGenie development environment using documented Docker commands.

---

## UR-011

Developers SHOULD be able to run:

```text
Frontend
Backend
Database
Redis
Event Bus
Workers
AI Services
```

locally without manually installing every infrastructure dependency.

---

## UR-012

Developers MUST be able to rebuild individual services independently.

---

## UR-013

Developers SHOULD be able to inspect container logs, health, networking, and resource consumption.

---

## 8. DevOps Requirements

## UR-014

DevOps engineers MUST be able to:

* Build images
* Tag images
* Scan images
* Push images
* Deploy containers
* Scale services
* Restart unhealthy workloads
* Roll back versions
* Inspect logs
* Inspect health checks
* Manage configuration

---

## 9. SRE Requirements

## UR-015

SREs MUST be able to identify:

```text
Failed Container
Failed Service
Resource Exhaustion
Crash Loop
Network Failure
Dependency Failure
Image Failure
Deployment Failure
```

---

## 10. AI Operations Requirements

## UR-016

AI agents SHOULD monitor container health and infrastructure telemetry.

---

## UR-017

AI agents MUST NOT receive unrestricted container-host privileges.

---

## UR-018

AI infrastructure operations MUST be governed by explicit policies.

---

## 11. System Requirements

## 11.1 Docker Engine

## SR-001

Development environments MUST support a current stable Docker Engine or Docker-compatible runtime.

---

## SR-002

Production deployments SHOULD use an orchestrator rather than unmanaged standalone Docker containers.

---

## 12. Docker Image Architecture

## SR-003

Every production service MUST have a versioned container image.

Example:

```text
salesgenie/auth-service:1.4.2
salesgenie/ai-gateway:2.1.0
salesgenie/lead-intelligence:3.0.1
```

---

## SR-004

Images MUST be uniquely identifiable by immutable digest.

Example:

```text
sha256:<image-digest>
```

---

## 13. Dockerfile Standards

Every production Dockerfile SHOULD implement:

```text
Minimal Base Image
Pinned Dependencies
Non-Root User
Multi-Stage Build
Health Check
Explicit Entry Point
Minimal Runtime Dependencies
```

---

## 14. Multi-Stage Builds

## SR-005

Build dependencies MUST NOT be unnecessarily included in production runtime images.

Example:

```text
Build Stage
    |
Compile
    |
Test
    |
Production Runtime Image
```

---

## 15. Base Image Standards

## SR-006

Production images MUST use maintained base images.

---

## SR-007

Base images MUST be periodically updated to address security vulnerabilities.

---

## 16. Image Size

## SR-008

Production images SHOULD minimize unnecessary dependencies and files.

Large AI images MAY use specialized images when justified by model/runtime requirements.

---

## 17. Dependency Pinning

## SR-009

Production dependencies MUST be pinned or constrained to controlled versions.

---

## 18. Container User

## SR-010

Application containers MUST run as non-root users unless root privileges are technically required.

Exceptions MUST be documented.

---

## 19. Filesystem Security

## SR-011

Production containers SHOULD use read-only root filesystems where practical.

---

## SR-012

Writable directories MUST be explicitly defined.

---

## 20. Container Capabilities

## SR-013

Linux capabilities MUST be minimized.

Containers SHOULD drop unnecessary capabilities.

---

## 21. Privileged Containers

## SR-014

Privileged containers MUST NOT be used in production unless explicitly approved and documented.

---

## 22. Docker Compose Architecture

Docker Compose SHOULD be used for local development and controlled test environments.

Example:

```text
docker-compose.yml

services:

  frontend
  api-gateway
  auth-service
  lead-intelligence
  ai-gateway
  workflow-service
  notification-service
  search-service
  analytics-service

  postgres
  redis
  event-bus
  object-storage

  worker
  scheduler
```

---

## 23. Local Development Architecture

```text
Developer Machine
        |
        v
Docker Compose
        |
+-------+------------------------------------+
|                                            |
v                                            v
Application Containers                 Infrastructure
|                                            |
+-- Frontend                                +-- PostgreSQL
+-- API Gateway                             +-- Redis
+-- Auth                                    +-- Event Bus
+-- AI Gateway                              +-- MinIO
+-- Lead Intelligence                       +-- Search
+-- Workflow                                |
+-- Workers                                 |
```

---

## 24. Docker Networks

## SR-015

Services MUST communicate through explicitly defined Docker networks.

---

## SR-016

Networks SHOULD be separated by trust boundary.

Example:

```text
public-network
application-network
data-network
management-network
```

---

## 25. Network Isolation

Database containers MUST NOT be directly exposed to the public host interface in production.

---

## 26. Container DNS

Services SHOULD communicate using service discovery rather than hard-coded container IP addresses.

Example:

```text
postgres:5432
redis:6379
event-bus:9092
```

---

## 27. Port Exposure

## SR-017

Only required ports MUST be exposed.

---

## SR-018

Internal service ports SHOULD remain internal to container networks.

---

## 28. Persistent Volumes

## SR-019

Persistent application data MUST NOT depend on container filesystem persistence.

---

## SR-020

Stateful services MUST use persistent volumes or external managed storage.

---

## 29. PostgreSQL Container

For development/testing, PostgreSQL MAY run in Docker.

Example:

```text
postgres:16-alpine
```

Production PostgreSQL SHOULD preferably use managed database infrastructure unless there is a strong operational reason to self-host it.

---

## 30. Redis Container

Redis MAY run in Docker for development/testing.

Production Redis SHOULD use a highly available deployment.

---

## 31. Object Storage

Local development MAY use:

```text
MinIO
```

Production SHOULD use durable object storage.

---

## 32. Event Bus

Local development MAY use:

```text
Kafka
Redpanda
RabbitMQ
NATS
```

Production event infrastructure MUST provide durability and operational monitoring.

---

## 33. AI Container Architecture

AI workloads SHOULD be separated from general-purpose services.

Example:

```text
AI Gateway
     |
     +---- Model Router
     |
     +---- Agent Runtime
     |
     +---- RAG
     |
     +---- Embedding
     |
     +---- Reranking
     |
     +---- Document Intelligence
     |
     +---- Voice AI
```

---

## 34. GPU Containers

## SR-021

GPU-enabled containers MUST use controlled GPU access.

---

## SR-022

GPU workloads MUST NOT have unrestricted access to unrelated host resources.

---

## 35. AI Model Containers

Self-hosted model containers SHOULD define:

```text
Model Version
Runtime Version
GPU Requirements
Memory Requirements
Concurrency
Context Length
Health Endpoint
Readiness Endpoint
```

---

## 36. AI Model Isolation

One model failure MUST NOT automatically terminate unrelated AI services.

---

## 37. AI Resource Limits

AI containers MUST have explicit resource limits.

Example:

```text
CPU
Memory
GPU
GPU Memory
Concurrency
Queue Capacity
```

---

## 38. Container Health Checks

## SR-023

Every critical container MUST define a health check.

Example conceptual endpoints:

```text
/health
/ready
/live
```

---

## 39. Health States

Containers SHOULD expose:

```text
Starting
Healthy
Degraded
Unhealthy
Stopping
```

---

## 40. Startup Ordering

Container startup SHOULD account for dependency readiness.

Example:

```text
PostgreSQL
     |
     v
Migration
     |
     v
Application
     |
     v
Workers
```

---

## 41. Restart Policies

## SR-024

Production services MUST use controlled restart policies.

---

## SR-025

Restart loops MUST be detectable.

---

## 42. Crash Loop Detection

The orchestration layer MUST detect repeatedly crashing containers.

---

## 43. Graceful Shutdown

## SR-026

Containers MUST handle termination signals correctly.

Applications MUST:

* Stop accepting new work
* Finish safe in-flight work
* Close connections
* Flush telemetry
* Commit safe state
* Exit cleanly

---

## 44. Worker Containers

Workers MUST support graceful task completion.

---

## 45. Queue Consumers

Queue consumers MUST support:

```text
Acknowledgement
Retry
Backoff
Dead Letter
Idempotency
Graceful Shutdown
```

---

## 46. Scheduler Containers

Scheduled workloads SHOULD run separately from interactive API services.

---

## 47. Environment Configuration

## SR-027

Configuration MUST be externalized.

Configuration sources MAY include:

```text
Environment Variables
Secrets Manager
Config Service
Kubernetes Secrets
Configuration Files
```

---

## 48. Secret Management

## SR-028

Secrets MUST NOT be baked into Docker images.

---

## SR-029

Secrets MUST NOT be committed to Git.

---

## SR-030

Secrets MUST NOT be printed into container logs.

---

## 49. Environment Variables

Example categories:

```text
DATABASE_URL
REDIS_URL
EVENT_BUS_URL
AI_PROVIDER_CONFIG
JWT_CONFIG
STORAGE_CONFIG
EMAIL_CONFIG
PAYMENT_CONFIG
```

Actual secrets MUST be supplied securely at runtime.

---

## 50. Configuration Validation

## SR-031

Services MUST validate required configuration during startup.

---

## 51. Container Logging

## SR-032

Applications MUST log to stdout/stderr in production containers.

---

## SR-033

Logs SHOULD be structured JSON.

---

## 52. Logging Fields

Recommended fields:

```text
timestamp
level
service
version
environment
request_id
trace_id
tenant_id
event
message
error
```

Sensitive information MUST be excluded or redacted.

---

## 53. Container Metrics

## SR-034

The platform MUST collect:

```text
CPU
Memory
Network
Filesystem
Restart Count
Container Health
Request Rate
Latency
Errors
```

---

## 54. Container Tracing

## SR-035

Distributed tracing SHOULD propagate across containers.

---

## 55. Container Security Scanning

## SR-036

Production images MUST be scanned for vulnerabilities.

Scanning SHOULD detect:

```text
OS Vulnerabilities
Package Vulnerabilities
Language Dependencies
Malware
Secrets
Misconfigurations
```

---

## 56. Image Signing

## SR-037

Production images SHOULD be cryptographically signed.

---

## 57. Image Registry

The organization MUST use a controlled container registry.

Example logical structure:

```text
registry/
|
+-- salesgenie/
    |
    +-- frontend
    +-- auth-service
    +-- ai-gateway
    +-- lead-intelligence
    +-- workflow-service
    +-- notification-service
```

---

## 58. Registry Access

## SR-038

Container registry access MUST use IAM-controlled authentication.

---

## 59. Image Retention

## SR-039

Old container images SHOULD follow configurable retention policies.

Production versions required for rollback MUST be retained.

---

## 60. Container Supply Chain

The image supply chain SHOULD follow:

```text
Source Code
    |
    v
Dependency Resolution
    |
    v
Build
    |
    v
Test
    |
    v
Security Scan
    |
    v
Sign
    |
    v
Registry
    |
    v
Deploy
```

---

## 61. SBOM

## SR-040

Production images SHOULD have Software Bills of Materials.

SBOM SHOULD identify:

```text
OS Packages
Libraries
Versions
Licenses
Dependencies
```

---

## 62. CI/CD Requirements

## SR-041

Every production container image MUST pass automated CI validation.

Pipeline SHOULD include:

```text
Lint
Unit Tests
Integration Tests
Build
Vulnerability Scan
SBOM Generation
Image Signing
Push
Deployment
Smoke Test
```

---

## 63. Image Tagging

Images SHOULD use:

```text
semantic-version
git-sha
build-id
immutable-digest
```

Example:

```text
ai-gateway:2.4.1
ai-gateway:git-a91c2d7
```

---

## 64. Latest Tag

## SR-042

Production deployments MUST NOT depend exclusively on the mutable `latest` tag.

---

## 65. Deployment Strategy

Production containers SHOULD support:

```text
Rolling Deployment
Canary Deployment
Blue-Green Deployment
Rollback
```

---

## 66. Rolling Deployment

A deployment MUST maintain sufficient healthy capacity while replacing old containers.

---

## 67. Canary Deployment

The platform SHOULD support:

```text
Old Version: 95%
New Version: 5%
```

followed by controlled traffic progression.

---

## 68. Rollback

## SR-043

Every production deployment MUST have a documented rollback mechanism.

---

## 69. Resource Limits

## SR-044

Critical containers MUST define:

```text
CPU Request
CPU Limit
Memory Request
Memory Limit
```

GPU services MUST additionally define GPU requirements.

---

## 70. Resource Governance

The platform MUST prevent a single service from exhausting shared host resources.

---

## 71. Noisy Neighbor Protection

Container resource limits MUST protect:

```text
CPU
Memory
Disk
Network
GPU
```

---

## 72. Orchestration

Production containerized workloads SHOULD be managed using an orchestration platform.

Potential platforms:

```text
Kubernetes
Managed Kubernetes
ECS
Cloud Run
Azure Container Apps
Other Managed Container Platforms
```

---

## 73. Kubernetes Architecture

Where Kubernetes is used:

```text
Cluster
|
+-- Ingress
|
+-- API Gateway
|
+-- Application Namespace
|
+-- AI Namespace
|
+-- Worker Namespace
|
+-- Data/Infrastructure Namespace
|
+-- Observability Namespace
|
+-- Security Namespace
```

---

## 74. Kubernetes Namespaces

Services SHOULD be logically grouped by workload and trust boundary.

Example:

```text
salesgenie-prod
salesgenie-ai
salesgenie-workers
salesgenie-observability
salesgenie-security
```

---

## 75. Kubernetes RBAC

## SR-045

Kubernetes RBAC MUST follow least privilege.

---

## 76. Kubernetes Service Accounts

Each workload SHOULD use a dedicated service account where practical.

---

## 77. Network Policies

## SR-046

Production Kubernetes deployments MUST use network policies for sensitive workloads.

---

## 78. Pod Security

Production workloads MUST prevent unnecessary privilege escalation.

---

## 79. Pod Disruption Budgets

Critical services SHOULD define disruption budgets.

---

## 80. Horizontal Pod Autoscaling

## SR-047

Critical stateless services SHOULD support horizontal pod autoscaling.

Scaling signals MAY include:

```text
CPU
Memory
Request Rate
Latency
Queue Depth
Custom Metrics
```

---

## 81. AI Autoscaling

AI workloads SHOULD scale independently from regular API services.

Signals MAY include:

```text
Inference Queue
GPU Utilization
Token Rate
Request Rate
Latency
Concurrency
```

---

## 82. Worker Autoscaling

Workers SHOULD scale based on queue backlog.

---

## 83. Container Affinity

Critical workloads SHOULD support workload placement policies.

---

## 84. Availability Zones

Production workloads SHOULD be distributed across availability zones where supported.

---

## 85. Stateful Workloads

Stateful workloads SHOULD preferably use managed cloud services.

If containerized, they MUST implement:

```text
Persistent Storage
Backup
Recovery
Replication
Health Monitoring
```

---

## 86. Database Migration Containers

Database migrations SHOULD execute as controlled jobs rather than being implicitly executed by every application container.

---

## 87. Migration Safety

Production migrations MUST support:

```text
Forward Migration
Validation
Rollback Strategy
Compatibility Window
Backup
```

---

## 88. API Gateway Container

The API gateway SHOULD provide:

```text
Authentication
Authorization
Routing
Rate Limiting
Quotas
Request Validation
TLS
Tracing
Logging
```

---

## 89. Frontend Container

The frontend container SHOULD:

* Build static assets
* Serve optimized assets
* Avoid storing persistent application state locally
* Support environment-specific configuration
* Use secure headers

---

## 90. Backend Container Standards

Backend containers SHOULD expose:

```text
/health
/ready
/metrics
```

where appropriate.

---

## 91. Service-to-Service Authentication

Internal service communication MUST use authenticated identities for sensitive operations.

---

## 92. mTLS

For high-security deployments, service-to-service communication SHOULD support mutual TLS.

---

## 93. Container Network Encryption

Sensitive internal traffic SHOULD be encrypted in transit.

---

## 94. Docker Secrets

Docker/Kubernetes secrets SHOULD be used instead of plaintext configuration for sensitive values.

---

## 95. Tenant Context Propagation

Service requests SHOULD propagate tenant context securely.

Recommended context:

```text
tenant_id
organization_id
user_id
role
request_id
trace_id
```

---

## 96. Tenant Isolation

Containers MUST NOT infer tenant authorization solely from client-provided headers.

Tenant identity MUST be validated against authenticated identity and authorization context.

---

## 97. AI Tenant Isolation

AI containers MUST enforce tenant isolation for:

```text
Prompts
Context
Embeddings
Documents
Conversation History
Memory
Tools
Agent State
```

---

## 98. RAG Containers

RAG services SHOULD be independently deployable.

Components MAY include:

```text
Document Processor
Chunker
Embedding Worker
Vector Store
Retriever
Reranker
Context Builder
```

---

## 99. Document Processing Containers

Document-processing workloads SHOULD be isolated because they may consume significant CPU and memory.

---

## 100. Untrusted File Processing

Uploaded files MUST be treated as untrusted input.

Processing containers SHOULD use:

```text
Restricted Permissions
Resource Limits
Timeouts
Sandboxing
Temporary Storage
Network Restrictions
Malware Scanning
```

---

## 101. Workflow Containers

Workflow execution MUST be isolated from core APIs.

---

## 102. Workflow Resource Controls

A workflow MUST have configurable:

```text
Timeout
Memory Limit
CPU Limit
Execution Limit
Concurrency Limit
Retry Limit
```

---

## 103. Notification Containers

Notification workers MUST support:

```text
Email
SMS
Push
In-App
Webhook
```

with independent scaling where necessary.

---

## 104. Search Containers

Search infrastructure MUST be isolated from transactional services.

---

## 105. Analytics Containers

Analytics jobs SHOULD run asynchronously.

---

## 106. Data Pipeline Containers

Data ingestion and ETL/ELT workers MUST be independently scalable.

---

## 107. Scheduled Jobs

Scheduled jobs SHOULD run as dedicated containers/jobs.

Examples:

```text
Data Cleanup
Report Generation
Billing Cycle
Usage Aggregation
Embedding Refresh
Search Reindexing
Analytics Aggregation
Backup Verification
```

---

## 108. Functional Requirements

## 108.1 Image Build

## FR-001

The system MUST build a container image for every deployable service.

---

## FR-002

Builds MUST produce versioned artifacts.

---

## FR-003

Build failures MUST stop downstream deployment stages.

---

## 109. Image Validation

## FR-004

The CI pipeline MUST validate image security before production deployment.

---

## 110. Container Startup

## FR-005

Containers MUST validate configuration during startup.

---

## FR-006

Containers MUST expose appropriate health status.

---

## 111. Automatic Recovery

## FR-007

The orchestration system MUST restart failed stateless containers when configured to do so.

---

## 112. Dependency Failure

## FR-008

Application containers MUST gracefully handle dependency failures.

Examples:

```text
Database unavailable
Redis unavailable
Event bus unavailable
AI provider unavailable
Search unavailable
External API unavailable
```

---

## 113. Circuit Breakers

## FR-009

Services SHOULD implement circuit breakers for unreliable external dependencies.

---

## 114. Retry Policies

## FR-010

Retries MUST use bounded exponential backoff.

---

## 115. Idempotency

## FR-011

Retryable operations MUST be designed to avoid unintended duplicate side effects.

---

## 116. Dead Letter Processing

## FR-012

Failed asynchronous jobs MUST be eligible for dead-letter handling.

---

## 117. Container Log Collection

## FR-013

Container logs MUST be centrally collectable.

---

## 118. Log Correlation

## FR-014

Logs MUST support correlation across services.

---

## 119. Metrics Collection

## FR-015

The system MUST collect service and container metrics.

---

## 120. Alerting

## FR-016

The platform MUST generate alerts for critical container failures.

Examples:

```text
Container Crash Loop
Memory Exhaustion
CPU Saturation
Disk Exhaustion
Repeated Restarts
Health Check Failure
Deployment Failure
Queue Backlog
GPU Exhaustion
```

---

## 121. AI Container Monitoring

## FR-017

AI SHOULD analyze container telemetry to identify abnormal behavior.

---

## 122. AI Anomaly Detection

AI SHOULD detect:

```text
Unusual CPU Usage
Memory Leaks
Restart Spikes
Latency Increase
Queue Growth
GPU Saturation
Unexpected Network Traffic
Container Drift
```

---

## 123. AI Root Cause Analysis

## FR-018

AI SHOULD correlate:

```text
Container Metrics
Application Logs
Distributed Traces
Deployment Events
Infrastructure Events
Dependency Health
```

to generate root-cause hypotheses.

---

## 124. AI Confidence

## FR-019

AI-generated infrastructure diagnoses MUST provide confidence and evidence.

---

## 125. AI Remediation

## FR-020

AI MAY perform low-risk container remediation when explicitly authorized.

Examples:

```text
Restart unhealthy worker
Scale stateless service
Retry failed job
Pause non-critical consumer
```

---

## 126. Human Approval

## FR-021

High-risk container operations MUST require human approval.

Examples:

```text
Delete production workload
Change network policy
Modify privileged permissions
Destroy persistent storage
Change tenant isolation
Deploy unverified image
```

---

## 127. AI + Human Container Operations

```text
Container Failure
       |
       v
AI Detection
       |
       v
AI Diagnosis
       |
       v
Risk Classification
       |
   +---+---+
   |       |
Low Risk High Risk
   |       |
Policy    Human
Check     Approval
   |       |
   +---+---+
       |
       v
Execution
       |
       v
Health Verification
       |
       v
Audit
```

---

## 128. Deployment Functional Requirements

## FR-022

Deployments MUST record:

```text
Service
Image
Digest
Version
Environment
Cluster
Namespace
Commit
Deployment Actor
Timestamp
```

---

## 129. Canary Validation

## FR-023

Canary deployments SHOULD automatically evaluate:

```text
Error Rate
Latency
Crash Rate
Resource Usage
Health Checks
Business Metrics
```

---

## 130. Automatic Rollback

## FR-024

Configured deployment thresholds MUST be able to trigger automated rollback.

---

## 131. Configuration Rollback

## FR-025

Configuration changes SHOULD be version controlled and reversible.

---

## 132. Secret Rotation

## FR-026

Secret rotation MUST NOT require rebuilding application images.

---

## 133. Certificate Rotation

## FR-027

TLS certificates SHOULD be rotated without unnecessary application downtime.

---

## 134. Resource Monitoring

## FR-028

The platform MUST track container resource consumption.

---

## 135. Resource Anomaly Detection

## FR-029

AI SHOULD detect inefficient resource usage.

Examples:

```text
CPU Overprovisioning
Memory Overprovisioning
Underutilized Containers
GPU Underutilization
Excessive Replica Count
Idle Workers
```

---

## 136. AI Cost Optimization

## FR-030

AI SHOULD recommend container resource optimization.

Recommendations MAY include:

```text
CPU Adjustment
Memory Adjustment
Replica Adjustment
Worker Scheduling
GPU Optimization
Image Optimization
```

---

## 137. Container Security Posture

## FR-031

The platform SHOULD maintain a security score for container workloads.

Factors:

```text
Image Vulnerabilities
Root Execution
Privileged Mode
Excess Capabilities
Secrets Exposure
Network Exposure
Outdated Packages
Missing Health Checks
Missing Resource Limits
```

---

## 138. Runtime Security

## FR-032

Runtime monitoring SHOULD detect suspicious container behavior.

Examples:

```text
Unexpected Process
Unexpected Network Connection
Privilege Escalation
Filesystem Modification
Credential Access
Unexpected Binary Execution
```

---

## 139. AI Runtime Security Agent

## FR-033

AI SHOULD analyze runtime security events and prioritize threats.

---

## 140. Container Incident Management

## FR-034

Every critical container incident MUST have an incident identifier.

---

## 141. Incident Data

Incidents MUST capture:

```text
Incident ID
Service
Container
Image
Version
Host/Node
Namespace
Region
Start Time
End Time
Error
Impact
Root Cause
Mitigation
Resolution
```

---

## 142. Container Dependency Graph

The platform SHOULD maintain:

```text
Frontend
   |
API Gateway
   |
Auth
   |
Business Service
   |
PostgreSQL
Redis
Event Bus
AI Gateway
```

---

## 143. Blast Radius Analysis

## FR-035

The platform SHOULD determine which services depend on a failed container.

---

## 144. Container Capacity Planning

## FR-036

The platform SHOULD forecast future:

```text
CPU
Memory
Storage
Network
GPU
Replica
Queue
```

requirements.

---

## 145. Container Lifecycle

Containers MUST support:

```text
Create
Start
Ready
Healthy
Degraded
Stopping
Stopped
Restarting
Failed
Removed
```

---

## 146. Graceful Deployment

## FR-037

Deployments MUST avoid terminating all healthy replicas simultaneously for critical services.

---

## 147. Maintenance

Maintenance operations SHOULD support:

```text
Drain
Stop
Upgrade
Restart
Validate
Resume
```

---

## 148. Development Workflow

Developers SHOULD be able to perform:

```text
docker compose up
docker compose down
docker compose build
docker compose logs
docker compose ps
docker compose exec
```

without modifying production configuration.

---

## 149. Local Debugging

## FR-038

Developers MUST be able to inspect:

```text
Container Logs
Environment Configuration
Network Connectivity
Health Status
Mounted Volumes
Resource Usage
```

---

## 150. Test Environment

The platform SHOULD provide disposable containerized test environments.

---

## 151. Integration Testing

Integration tests SHOULD run against isolated containers for:

```text
PostgreSQL
Redis
Event Bus
Object Storage
Search
AI Gateway
```

---

## 152. End-to-End Testing

The CI pipeline SHOULD support complete containerized E2E environments.

---

## 153. Load Testing

The platform SHOULD support load testing against containerized environments.

Test dimensions:

```text
API Throughput
Concurrent Users
Concurrent Conversations
AI Requests
Event Throughput
Workflow Executions
Search Requests
```

---

## 154. Chaos Testing

The platform SHOULD test:

```text
Container Kill
Node Failure
Network Partition
Database Failure
Redis Failure
Queue Failure
AI Provider Failure
Storage Failure
```

---

## 155. Disaster Recovery

Container deployments MUST be reproducible from version-controlled configuration.

---

## 156. Backup and Restore

Persistent infrastructure MUST have independent backup and recovery mechanisms.

Containers themselves MUST NOT be treated as backups.

---

## 157. Production Docker Architecture

```text
                    INTERNET
                       |
                  CDN / WAF
                       |
                  Load Balancer
                       |
                  API Gateway
                       |
              Container Orchestrator
                       |
     +-----------------+-----------------+
     |                 |                 |
     v                 v                 v
 Application         AI Tier          Worker Tier
 Containers          Containers       Containers
     |                 |                 |
     +-----------------+-----------------+
                       |
                   Event Bus
                       |
       +---------------+---------------+
       |               |               |
       v               v               v
   PostgreSQL        Redis        Object Storage
       |               |               |
       +---------------+---------------+
                       |
                  Data Platform
                       |
                Observability
                       |
          +------------+------------+
          |            |            |
        Logs        Metrics       Traces
          |            |            |
          +------------+------------+
                       |
                  AI Operations
                       |
             Human Governance
```

---

## 158. Docker Compose Development Architecture

```text
docker compose
|
+-- frontend
|
+-- api-gateway
|
+-- auth-service
|
+-- lead-intelligence
|
+-- ai-gateway
|
+-- workflow-service
|
+-- notification-service
|
+-- search-service
|
+-- analytics-service
|
+-- worker
|
+-- scheduler
|
+-- postgres
|
+-- redis
|
+-- event-bus
|
+-- minio
|
+-- mailpit
```

---

## 159. Docker Environment Separation

```text
                 SALES GENIE
                     |
       +-------------+-------------+
       |             |             |
       v             v             v
 Development       Staging      Production
       |             |             |
 Docker Compose   Containers    Orchestrator
       |             |             |
 Local Data       Test Data     Production Data
```

---

## 160. Production vs Development

Development MAY use:

```text
Docker Compose
Local PostgreSQL
Local Redis
MinIO
Mailpit
Local Event Bus
```

Production SHOULD use:

```text
Managed PostgreSQL
Managed Redis
Cloud Object Storage
Managed Event Infrastructure
Container Orchestrator
Centralized Observability
Managed Secrets
```

---

## 161. Container Naming

Container/service names MUST follow predictable conventions.

Example:

```text
salesgenie-auth
salesgenie-ai-gateway
salesgenie-lead-intelligence
salesgenie-workflow
salesgenie-notification-worker
```

---

## 162. Docker Labels

Containers SHOULD expose standardized metadata:

```text
service
version
environment
owner
team
tenant_scope
managed_by
```

---

## 163. Container Metadata

The platform SHOULD maintain:

```text
Container ID
Image Digest
Image Version
Service
Environment
Host
Node
Region
Start Time
Health
Restart Count
```

---

## 164. Container Registry Governance

Registry policies SHOULD enforce:

```text
Approved Base Images
Vulnerability Scanning
Image Signing
Retention
Access Control
Immutable Production Artifacts
```

---

## 165. Vulnerability Management

Critical container vulnerabilities MUST be prioritized for remediation.

---

## 166. Vulnerability Exceptions

Security exceptions MUST include:

```text
Vulnerability
Affected Image
Risk
Reason
Owner
Expiration
Mitigation
Approval
```

---

## 167. AI Vulnerability Analysis

AI MAY assist security engineers by:

* Prioritizing vulnerabilities
* Explaining impact
* Identifying affected services
* Suggesting upgrades
* Identifying compensating controls

AI MUST NOT silently suppress security findings.

---

## 168. Image Provenance

Production deployments SHOULD verify that images originated from trusted CI/CD pipelines.

---

## 169. Deployment Authorization

Only authorized identities MUST be able to deploy production images.

---

## 170. Production Access

Production container shells SHOULD be restricted and audited.

---

## 171. Container Exec

Interactive access SHOULD require:

```text
Strong Authentication
Authorization
Audit Logging
Time-Bounded Access
Reason
```

---

## 172. AI Container Access

AI agents MUST NOT receive unrestricted interactive shell access.

---

## 173. AI Operational Tools

AI infrastructure agents SHOULD interact through controlled APIs/tools rather than arbitrary shell execution.

---

## 174. AI Action Policy

Every AI container-management action SHOULD be evaluated against:

```text
Actor
Resource
Action
Environment
Risk
Policy
Approval
```

---

## 175. AI Action Audit

Every AI-initiated container operation MUST be auditable.

---

## 176. Human Override

Human operators MUST be able to:

```text
Pause AI Automation
Reject Action
Approve Action
Revert Action
Disable Agent
```

---

## 177. AI Continuous Improvement

Post-incident AI analysis SHOULD identify:

```text
Detection Failure
Diagnosis Failure
Remediation Failure
Policy Failure
Capacity Failure
Deployment Failure
```

and recommend improvements.

---

## 178. SLO Requirements

Critical containerized services MUST define:

```text
Availability SLO
Latency SLO
Error SLO
Recovery Objective
Scaling Objective
```

---

## 179. Reliability Metrics

The platform SHOULD measure:

```text
Container Availability
Container Restart Rate
Crash Loop Rate
Deployment Failure Rate
Rollback Rate
Mean Time to Recovery
Mean Time Between Failures
Resource Utilization
```

---

## 180. AI Infrastructure Metrics

The platform SHOULD measure:

```text
AI Detection Accuracy
AI Root Cause Accuracy
AI Remediation Success Rate
Human Override Rate
False Positive Rate
Automated Action Rate
Infrastructure Cost Savings
```

---

## 181. Docker Architecture Acceptance Criteria

The Docker architecture is production-ready when:

* [ ] Every deployable service has a versioned image.
* [ ] Production images are immutable.
* [ ] Images use maintained base images.
* [ ] Dependencies are controlled.
* [ ] Multi-stage builds are used where appropriate.
* [ ] Containers run as non-root where possible.
* [ ] Privileged containers are prohibited by default.
* [ ] Unnecessary Linux capabilities are removed.
* [ ] Secrets are never baked into images.
* [ ] Production images are vulnerability scanned.
* [ ] Production images have provenance.
* [ ] Production images are signed where supported.
* [ ] SBOM generation is available.
* [ ] Container registry access is IAM controlled.
* [ ] Production image retention policies exist.
* [ ] Development Docker Compose environment is documented.
* [ ] Production uses a container orchestrator or equivalent managed platform.
* [ ] Critical services have health checks.
* [ ] Readiness and liveness behavior is defined.
* [ ] Containers support graceful shutdown.
* [ ] Restart policies are configured.
* [ ] Crash loops are detected.
* [ ] CPU limits are defined.
* [ ] Memory limits are defined.
* [ ] GPU limits are defined for AI workloads where applicable.
* [ ] Noisy-neighbor protection is implemented.
* [ ] Container networks are segmented.
* [ ] Database ports are not publicly exposed.
* [ ] Persistent data is stored outside ephemeral containers.
* [ ] Stateful workloads have backup and recovery procedures.
* [ ] Service discovery does not depend on static container IPs.
* [ ] Logs are centrally collectable.
* [ ] Metrics are centrally collectable.
* [ ] Distributed tracing is supported.
* [ ] Critical failures generate alerts.
* [ ] CI/CD automatically validates images.
* [ ] Production deployments are auditable.
* [ ] Rollback procedures are tested.
* [ ] Canary or equivalent safe deployment is available.
* [ ] AI workloads are independently scalable.
* [ ] Worker workloads are independently scalable.
* [ ] Data processing workloads are isolated.
* [ ] Untrusted document processing is sandboxed.
* [ ] AI agents use controlled operational permissions.
* [ ] High-risk AI actions require human approval.
* [ ] AI infrastructure actions are audited.
* [ ] Container dependency graphs are available.
* [ ] Blast-radius analysis is available.
* [ ] Disaster recovery deployments are reproducible.
* [ ] Containerized integration tests exist.
* [ ] E2E tests exist.
* [ ] Load testing exists.
* [ ] Failure/chaos testing exists.
* [ ] Security posture monitoring exists.
* [ ] Vulnerability remediation procedures exist.
* [ ] Production access is strongly controlled.
* [ ] Container shell access is audited.
* [ ] AI cannot obtain unrestricted host/container privileges.

---

## 182. Non-Functional Requirements

## NFR-001 — Portability

The application architecture SHOULD remain portable across compatible container runtimes and cloud platforms.

---

## NFR-002 — Reproducibility

A production deployment MUST be reproducible from:

```text
Source Code
Container Definitions
Image Digest
Configuration
Infrastructure Code
```

---

## NFR-003 — Security

Containers MUST implement defense-in-depth security.

---

## NFR-004 — Availability

Critical services MUST support multiple replicas or an equivalent highly available deployment model.

---

## NFR-005 — Scalability

Containerized services MUST support horizontal scaling where applicable.

---

## NFR-006 — Observability

Every critical workload MUST expose sufficient telemetry for production diagnosis.

---

## NFR-007 — Performance

Container overhead MUST remain within acceptable service-specific performance budgets.

---

## NFR-008 — Maintainability

Container definitions MUST be version controlled, reviewed, tested, and documented.

---

## NFR-009 — Cost Efficiency

Container resources MUST be continuously evaluated for overprovisioning and underutilization.

---

## NFR-010 — Fault Isolation

Failure of one container SHOULD NOT cascade into unrelated services.

---

## 183. Recommended SalesGenie Container Topology

```text
salesgenie/
|
+-- frontend
|
+-- api-gateway
|
+-- auth-service
|
+-- user-service
|
+-- organization-service
|
+-- rbac-service
|
+-- conversation-service
|
+-- sales-service
|
+-- support-service
|
+-- lead-intelligence-service
|
+-- omnichannel-service
|
+-- whatsapp-service
|
+-- workflow-service
|
+-- notification-service
|
+-- search-service
|
+-- analytics-service
|
+-- metrics-service
|
+-- billing-service
|
+-- payment-service
|
+-- webhook-service
|
+-- developer-api-service
|
+-- ai-gateway
|
+-- model-router
|
+-- agent-runtime
|
+-- rag-service
|
+-- embedding-service
|
+-- document-intelligence-service
|
+-- voice-ai-service
|
+-- knowledge-service
|
+-- data-ingestion-service
|
+-- etl-worker
|
+-- elt-worker
|
+-- scheduler
|
+-- task-worker
|
+-- event-consumer
|
+-- postgres
|
+-- redis
|
+-- event-bus
|
+-- object-storage
|
+-- search-engine
|
+-- observability
|
+-- security-monitor
|
+-- ai-operations
```

---

## 184. Final Docker Operating Model

SalesGenie MUST treat containers as the fundamental packaging and deployment boundary for application workloads.

The operating model SHOULD be:

```text
                    SOURCE CODE
                         |
                         v
                  CI/CD PIPELINE
                         |
                  Build Container
                         |
                         v
                  Security Scan
                         |
                         v
                    SBOM / Sign
                         |
                         v
                 Container Registry
                         |
                         v
                  Deployment System
                         |
                         v
               Container Orchestrator
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
       Services        AI Workloads    Workers
          |              |              |
          +--------------+--------------+
                         |
                    Observability
                         |
          +--------------+--------------+
          |              |              |
        Logs           Metrics        Traces
          |              |              |
          +--------------+--------------+
                         |
                  AI Operations
                         |
          +--------------+--------------+
          |              |              |
      Detection       Diagnosis      Optimization
          |              |              |
          +--------------+--------------+
                         |
                  Risk Classification
                         |
                +--------+--------+
                |                 |
             Low Risk          High Risk
                |                 |
          Policy Approval     Human Approval
                |                 |
                +--------+--------+
                         |
                     Execution
                         |
                     Verification
                         |
                       Audit
                         |
                 Continuous Improvement
```

The Docker architecture MUST ensure that:

* Containers are reproducible.
* Production artifacts are immutable.
* Services are independently deployable.
* Stateful data is externalized.
* Critical workloads are isolated.
* AI workloads have independent resource controls.
* Background workers scale independently.
* Containers are observable.
* Images are security scanned.
* Secrets remain outside images.
* Production access is controlled.
* Deployments are automated.
* Rollbacks are reliable.
* Failures are isolated.
* Tenant boundaries are preserved.
* AI operations are permission-bounded.
* High-risk AI actions require human authorization.
* Low-risk automation can operate under explicit policy.
* Container infrastructure can scale from local development to enterprise production.
* The architecture supports SalesGenie's long-term evolution toward highly available, multi-region, multi-tenant enterprise infrastructure.
