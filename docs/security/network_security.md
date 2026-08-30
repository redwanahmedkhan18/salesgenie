# SalesGenie — Network Security Requirements

**Document:** `network_security.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Level:** FAANG-Level / Production-Grade  
**Scope:** Human Users + AI Agents + Microservices + APIs + Databases + AI Gateway + RAG + MCP + Integrations + Webhooks + Workers + Admin Systems + Observability + Infrastructure

---

## 1. Purpose

SalesGenie shall implement a defense-in-depth network security architecture protecting all network communication between:

```text
Human Users
AI Agents
Web Applications
API Gateway
Microservices
AI Gateway
RAG Services
Vector Databases
Workflow Engine
MCP Servers
Integration Services
Databases
Caches
Object Storage
Message Brokers
External APIs
AI Providers
Administrative Systems
Monitoring Systems
```

The network-security architecture shall protect against:

```text
Unauthorized Network Access
Network Intrusion
Man-in-the-Middle Attacks
DDoS
API Abuse
Port Scanning
Service Enumeration
Lateral Movement
Network-Level Data Exfiltration
DNS Abuse
SSRF
Internal Service Spoofing
Unauthorized East-West Traffic
Cross-Tenant Network Access
Credential Theft
Webhook Abuse
Malicious Automation
AI Agent Network Abuse
MCP Network Abuse
Integration Abuse
```

---

## 2. Network Security Objectives

SalesGenie shall:

1. Apply zero-trust networking.
2. Minimize network exposure.
3. Keep internal services private by default.
4. Encrypt all protected traffic.
5. Enforce service-to-service authentication.
6. Segment production workloads.
7. Restrict east-west traffic.
8. Protect public APIs.
9. Protect administrative interfaces.
10. Protect databases and caches from public exposure.
11. Implement API rate limiting.
12. Implement DDoS protection.
13. Detect network anomalies.
14. Prevent SSRF.
15. Prevent unauthorized outbound connections.
16. Protect webhook endpoints.
17. Protect AI and MCP network access.
18. Secure external integrations.
19. Provide network-level auditability.
20. Support incident containment and isolation.
21. Prevent lateral movement.
22. Enforce tenant-aware authorization at the application layer even when network access is permitted.

---

## 3. Network Security Principles

## NET-PRINCIPLE-001 — Zero Trust

No network location shall automatically imply trust.

Every protected request shall be evaluated using appropriate:

```text
Identity
Authentication
Authorization
Service Identity
Tenant Context
Resource
Action
Network Policy
Risk
```

---

## NET-PRINCIPLE-002 — Private by Default

Internal resources shall not be publicly accessible unless explicitly required.

---

## NET-PRINCIPLE-003 — Least Network Privilege

Services shall communicate only with explicitly authorized destinations and ports.

---

## NET-PRINCIPLE-004 — Defense in Depth

Network protection shall operate across:

```text
DNS
CDN
WAF
Load Balancer
API Gateway
Service Mesh
Firewall
Security Groups
Network Policies
Application Authorization
Database Authorization
Monitoring
```

---

## NET-PRINCIPLE-005 — Encrypt in Transit

Protected network traffic shall use strong encryption.

---

## NET-PRINCIPLE-006 — Explicit Egress

Outbound traffic shall be explicitly controlled for sensitive workloads.

---

## NET-PRINCIPLE-007 — Minimize Blast Radius

A compromised service shall have limited ability to reach other services or data stores.

---

## NET-PRINCIPLE-008 — Fail Closed

Network-policy failures shall default to denying unauthorized communication.

---

## 4. Network Actors

## Human Actors

```text
H-001 End User
H-002 Sales Agent
H-003 Support Agent
H-004 Organization Admin
H-005 Security Admin
H-006 Billing Admin
H-007 Developer
H-008 Auditor
H-009 Super Admin
```

## AI Actors

```text
AI-001 Sales Agent
AI-002 Support Agent
AI-003 Lead Generation Agent
AI-004 Research Agent
AI-005 Customer Success Agent
AI-006 Workflow Agent
AI-007 MCP Agent
AI-008 Multi-Agent Orchestrator
```

## Infrastructure Actors

```text
N-001 CDN
N-002 WAF
N-003 Load Balancer
N-004 API Gateway
N-005 Service Mesh
N-006 Microservices
N-007 Database
N-008 Redis
N-009 Object Storage
N-010 Message Broker
N-011 AI Gateway
N-012 RAG Service
N-013 Vector Database
N-014 Workflow Engine
N-015 MCP Server
N-016 Integration Gateway
N-017 Monitoring Platform
```

---

## 5. User Requirements

## UR-NETSEC-001 — Secure Application Access

Users shall access SalesGenie through secure network channels.

---

## UR-NETSEC-002 — HTTPS

Users shall not transmit application credentials or protected data over plaintext HTTP.

---

## UR-NETSEC-003 — Secure Session Communication

Authenticated sessions shall communicate exclusively through protected transport.

---

## UR-NETSEC-004 — Network Availability

Users shall receive reliable access even during common network attacks or traffic spikes.

---

## UR-NETSEC-005 — Protection From Malicious Traffic

Users shall be protected from malicious requests targeting SalesGenie infrastructure.

---

## UR-NETSEC-006 — Tenant Network Isolation

Users shall not be able to use network-facing application interfaces to access another tenant's resources.

---

## UR-NETSEC-007 — Secure File Access

Uploaded and downloaded files shall use secure network channels.

---

## UR-NETSEC-008 — Secure Integration Communication

External integrations shall communicate through authenticated and encrypted channels.

---

## UR-NETSEC-009 — Secure Webhooks

Webhook communication shall validate the source and authenticity of incoming requests.

---

## UR-NETSEC-010 — Secure Administrative Access

Administrative network interfaces shall have stronger access controls than ordinary application endpoints.

---

## 6. AI User Requirements

## AI-UR-NETSEC-001 — Authorized Network Access

AI agents shall only access network resources explicitly authorized for their task.

---

## AI-UR-NETSEC-002 — Restricted Egress

AI agents shall not have unrestricted Internet access by default.

---

## AI-UR-NETSEC-003 — SSRF Protection

AI agents shall not be able to use tools or network capabilities to access protected internal infrastructure.

---

## AI-UR-NETSEC-004 — Internal Network Protection

AI agents shall not directly access:

```text
Databases
Redis
Internal Admin APIs
Cloud Metadata Services
Private Control Planes
Internal Service Credentials
```

unless explicitly authorized through a controlled service.

---

## AI-UR-NETSEC-005 — AI Integration Security

AI agents shall only communicate with approved integration endpoints.

---

## AI-UR-NETSEC-006 — AI Network Isolation

Compromised or malicious AI behavior shall not provide unrestricted lateral network access.

---

## AI-UR-NETSEC-007 — MCP Network Security

MCP tools shall communicate through explicitly approved network routes.

---

## AI-UR-NETSEC-008 — Workflow Network Security

AI-generated workflows shall not automatically obtain unrestricted network access.

---

## AI-UR-NETSEC-009 — AI Data Exfiltration Protection

AI agents shall be prevented from sending unauthorized customer or tenant data to arbitrary external destinations.

---

## AI-UR-NETSEC-010 — Network Auditability

AI-initiated network actions shall be attributable to:

```text
Tenant
User
Agent
Workflow
Tool
Destination
Action
Timestamp
Request ID
```

---

## 7. System Requirements

## SR-NETSEC-001 — Network Segmentation

SalesGenie shall segment infrastructure into appropriate security zones.

Example:

```text
Internet
   |
   v
CDN / DDoS
   |
   v
WAF
   |
   v
Public Load Balancer
   |
   v
API Gateway
   |
   +--------------------+
   |                    |
   v                    v
Application Zone     AI Gateway
   |                    |
   v                    v
Service Zone         AI Services
   |
   +---------+----------+---------+
   |         |          |         |
   v         v          v         v
Database   Redis     RAG       Workflow
Zone       Zone      Zone      Zone
```

---

## 8. Public Network Exposure

Only required services shall be publicly exposed.

Publicly exposed resources should generally be limited to:

```text
CDN
WAF
Load Balancer
API Gateway
Webhook Gateway
Required OAuth Callback Endpoints
```

---

## 9. Private Network Resources

The following shall not be directly exposed to the public Internet:

```text
PostgreSQL
Redis
Vector Database
Internal Message Broker
Internal Workers
Internal Service APIs
Object Storage Control Plane
Service Mesh Control Plane
Internal Admin APIs
Secrets Management
Internal Monitoring
```

---

## 10. Network Access Control

Network access shall be controlled using:

```text
Firewall Rules
Security Groups
Network ACLs
Kubernetes Network Policies
Service Mesh Policies
Application Authorization
Identity-Aware Proxies
```

---

## 11. Service-to-Service Authentication

Every sensitive service-to-service request shall use authenticated service identity.

Possible mechanisms include:

```text
mTLS
Short-Lived Service Tokens
JWT
Workload Identity
Signed Requests
```

---

## 12. Service Identity

Every internal service shall have a unique machine identity.

Example:

```text
api-gateway.salesgenie
auth-service.salesgenie
ai-gateway.salesgenie
rag-service.salesgenie
workflow-service.salesgenie
integration-service.salesgenie
billing-service.salesgenie
```

---

## 13. Service Authorization

Authentication alone shall not authorize arbitrary service communication.

A service shall only communicate with approved services and resources.

---

## 14. East-West Traffic

Internal east-west traffic shall be explicitly controlled.

Example:

```text
API Gateway
   |
   +--> Auth Service
   +--> AI Gateway
   +--> Lead Intelligence
   +--> Billing Service

AI Gateway
   |
   +--> Approved Model Providers
   +--> RAG Service

RAG Service
   |
   +--> Vector Database
   +--> Object Storage

Billing Service
   |
   +--> Payment Provider
```

Unnecessary routes shall be denied.

---

## 15. North-South Traffic

Internet-facing traffic shall pass through appropriate perimeter controls:

```text
Internet
   ↓
DDoS Protection
   ↓
CDN
   ↓
WAF
   ↓
Load Balancer
   ↓
API Gateway
   ↓
Application
```

---

## 16. TLS

SalesGenie shall use TLS for protected network communication.

---

## 17. TLS Version

Production systems shall prefer modern TLS versions and disable obsolete protocols and weak cipher suites.

---

## 18. Certificate Management

Certificates shall support:

```text
Automatic Provisioning
Expiration Monitoring
Rotation
Revocation
Renewal
Audit
```

---

## 19. Internal TLS

Sensitive internal service communication should use mTLS where appropriate.

---

## 20. Certificate Trust

Internal services shall validate certificates rather than blindly accepting any certificate.

---

## 21. HSTS

Public web applications shall support HTTP Strict Transport Security where appropriate.

---

## 22. Secure DNS

Production infrastructure shall use trusted DNS services and protect DNS configuration from unauthorized modification.

---

## 23. DNS Security

The platform shall monitor for:

```text
DNS Hijacking
Unauthorized Records
Domain Takeover
DNS Spoofing
Malicious Resolution
```

---

## 24. DNS Rebinding Protection

Server-side components shall protect against DNS rebinding attacks, particularly for URL-fetching functionality.

---

## 25. SSRF Protection

All server-side URL fetching shall enforce:

```text
Protocol Allowlist
Domain Allowlist
IP Validation
DNS Revalidation
Redirect Validation
Port Restrictions
Response Size Limits
Timeouts
```

---

## 26. SSRF Private Address Blocking

Outbound HTTP clients shall block access to unauthorized private and special-use ranges.

Examples include:

```text
127.0.0.0/8
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
169.254.0.0/16
::1/128
fc00::/7
```

Exact implementation shall account for IPv4, IPv6, DNS resolution, redirects, and cloud-provider metadata endpoints.

---

## 27. Cloud Metadata Protection

Application workloads shall not be able to arbitrarily access cloud instance metadata services.

---

## 28. Outbound Network Controls

Production services shall use egress policies where appropriate.

Example:

```text
AI Gateway
   |
   +--> Approved AI Providers

Integration Service
   |
   +--> Approved Integration Providers

Notification Service
   |
   +--> Approved Messaging Providers

Application Service
   |
   +--> Approved Internal Services
```

---

## 29. Egress Allowlisting

High-risk workloads shall use destination allowlists where feasible.

---

## 30. Dynamic Destination Controls

User-supplied URLs shall not automatically become trusted egress destinations.

---

## 31. Egress Data Protection

Outbound traffic carrying sensitive data shall be subject to:

```text
Authorization
DLP
Destination Policy
Audit
Rate Limiting
```

---

## 32. Network Rate Limiting

Rate limits shall apply at multiple layers:

```text
IP
User
Tenant
API Key
Service
Agent
Workflow
Integration
Endpoint
```

---

## 33. Adaptive Rate Limiting

The platform should dynamically adjust rate limits based on:

```text
Traffic Volume
Authentication State
Tenant Plan
Risk
Historical Behavior
Endpoint Sensitivity
```

---

## 34. DDoS Protection

SalesGenie shall implement protection against:

```text
Volumetric DDoS
Protocol Attacks
Application-Layer DDoS
Connection Exhaustion
Request Flooding
```

---

## 35. WAF

A Web Application Firewall shall protect public application endpoints from common web attacks.

---

## 36. WAF Protections

WAF policies shall address relevant attacks including:

```text
SQL Injection
XSS
Path Traversal
Protocol Abuse
Malformed Requests
Known Exploit Patterns
Bot Abuse
Request Flooding
```

---

## 37. Bot Protection

Public endpoints shall support detection and mitigation of malicious automation.

---

## 38. API Gateway Security

The API gateway shall enforce:

```text
Authentication
Authorization
Rate Limiting
Request Validation
TLS
CORS
Security Headers
Request Size Limits
Timeouts
Audit Logging
```

---

## 39. Request Size Limits

Public endpoints shall enforce maximum request sizes.

---

## 40. Connection Limits

Network-facing services shall enforce reasonable:

```text
Connection Limits
Concurrent Request Limits
Idle Timeouts
Keepalive Limits
```

---

## 41. API Timeout Protection

Requests shall have explicit timeout policies to prevent resource exhaustion.

---

## 42. Slow Request Protection

The platform shall mitigate slow-client and slow-request attacks.

---

## 43. WebSocket Security

If SalesGenie uses WebSockets or streaming connections, they shall enforce:

```text
Authentication
Authorization
Origin Validation
Connection Limits
Message Size Limits
Idle Timeouts
Rate Limiting
Tenant Isolation
```

---

## 44. Server-Sent Events

Streaming endpoints shall enforce:

```text
Authentication
Authorization
Connection Limits
Timeouts
Tenant Isolation
```

---

## 45. CORS

CORS shall use explicit origin allowlists for production environments.

Wildcard origins shall not be used with sensitive authenticated APIs unless explicitly justified and safely configured.

---

## 46. CSRF

State-changing browser requests shall use appropriate CSRF protections where cookie-based authentication is used.

---

## 47. Security Headers

Public application responses shall use appropriate security headers.

Examples:

```text
Strict-Transport-Security
Content-Security-Policy
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
```

---

## 48. Internal API Security

Internal APIs shall not rely solely on private network location for security.

---

## 49. Network Policy

Network policy shall define:

```text
Source
Destination
Port
Protocol
Identity
Action
```

Example:

```text
api-gateway
    → auth-service:8001
    ALLOW

api-gateway
    → billing-service:8004
    ALLOW

api-gateway
    → postgres:5432
    DENY

public-internet
    → postgres:5432
    DENY
```

---

## 50. Database Network Security

PostgreSQL shall:

```text
Not be Publicly Exposed
Require Authentication
Use TLS Where Applicable
Restrict Source Networks
Restrict Ports
Use Least-Privilege Accounts
Log Relevant Access
```

---

## 51. Redis Network Security

Redis shall:

```text
Remain Private
Require Authentication Where Supported
Use TLS Where Supported
Restrict Network Sources
Avoid Public Exposure
```

---

## 52. Vector Database Network Security

Vector databases shall:

```text
Remain Private
Require Authentication
Restrict Network Sources
Use Encryption in Transit
Enforce Tenant-Aware Application Authorization
```

---

## 53. Object Storage Network Security

Object storage shall use:

```text
Private Buckets
IAM Policies
Signed URLs
TLS
Expiration
Network Restrictions Where Available
```

---

## 54. Message Broker Security

Message brokers shall enforce:

```text
Authentication
Authorization
TLS
Topic/Queue Isolation
Consumer Authorization
Producer Authorization
```

---

## 55. Queue Security

Queue consumers shall only receive messages they are authorized to process.

---

## 56. Tenant-Aware Messaging

Asynchronous messages shall preserve:

```text
tenant_id
actor_id
service_identity
request_id
security_context
```

where appropriate.

---

## 57. Message Integrity

Sensitive asynchronous messages shall support integrity protection.

---

## 58. Replay Protection

Security-sensitive requests and messages shall support replay protection where applicable.

---

## 59. Webhook Security

Incoming webhooks shall use:

```text
Signature Validation
Timestamp Validation
Replay Detection
Schema Validation
Rate Limiting
Tenant Binding
IP Controls Where Reliable
Audit Logging
```

---

## 60. Webhook Network Isolation

Webhook ingestion shall be isolated from sensitive internal infrastructure.

---

## 61. OAuth Callback Security

OAuth callback endpoints shall enforce:

```text
State Validation
PKCE Where Applicable
Redirect URI Validation
TLS
Authorization
Rate Limiting
```

---

## 62. Integration Network Security

External integrations shall communicate using secure protocols and validated endpoints.

Integrations include:

```text
Google
Google Drive
Gmail
LinkedIn
Facebook
Instagram
WhatsApp
YouTube
TikTok
Slack
Zendesk
Salesforce
HubSpot
Jira
Notion
Microsoft Teams
```

---

## 63. Integration Egress

Integration services shall only communicate with configured and trusted providers.

---

## 64. Third-Party Endpoint Validation

External destinations shall be validated before transmitting protected data.

---

## 65. AI Gateway Network Security

The AI gateway shall act as a controlled network boundary between SalesGenie and AI providers.

```text
SalesGenie Services
        |
        v
   AI Gateway
        |
        +--> Provider A
        +--> Provider B
        +--> Provider C
```

---

## 66. AI Provider Allowlist

AI requests shall only be sent to configured providers.

---

## 67. AI Provider TLS

All AI-provider traffic shall use secure transport.

---

## 68. AI Provider Egress Logging

AI-provider network requests shall produce security telemetry without logging sensitive payloads unnecessarily.

---

## 69. AI Agent Network Sandbox

AI agents that can execute network-capable tools should operate within restricted network environments.

---

## 70. AI Agent Destination Policy

An AI agent's network permissions shall be based on:

```text
Tenant
User
Agent
Workflow
Tool
Purpose
Destination
Data Classification
```

---

## 71. AI Agent Internet Access

Internet access shall be disabled by default for AI execution environments unless required.

---

## 72. AI Web Browsing

If web browsing is supported, browsing shall use a controlled proxy or browser isolation layer where feasible.

---

## 73. AI Web Fetching

AI web-fetch operations shall enforce:

```text
URL Validation
DNS Validation
Private IP Blocking
Redirect Validation
Content Size Limits
Timeouts
Rate Limits
Domain Policy
```

---

## 74. AI Network Exfiltration

The platform shall detect or prevent suspicious AI network behavior such as:

```text
Large Outbound Requests
Repeated External Uploads
Unexpected Domains
High-Volume Requests
Encoded Data Transfers
Credential Transmission
Cross-Tenant Data Transmission
```

---

## 75. MCP Network Security

MCP servers shall be treated as privileged network resources.

---

## 76. MCP Server Access

MCP communication shall require:

```text
Authenticated Client
Authorized Tool
Authorized Resource
Tenant Context
Secure Transport
Audit
```

---

## 77. MCP Egress

MCP servers shall not have unrestricted outbound Internet access by default.

---

## 78. MCP Tool Isolation

High-risk MCP tools should execute in isolated environments.

---

## 79. MCP Network Audit

Every high-risk MCP network action shall be auditable.

---

## 80. Workflow Network Security

User-created workflows shall execute under a constrained network identity.

---

## 81. Workflow Egress

Workflow actions shall not automatically inherit unrestricted server network privileges.

---

## 82. Workflow Destination Allowlist

High-risk workflow actions may require destination allowlisting.

---

## 83. Workflow SSRF Protection

HTTP-request workflow nodes shall implement SSRF protections.

---

## 84. Workflow Rate Limiting

Workflow-generated network traffic shall be rate-limited per:

```text
Tenant
Workflow
Execution
Destination
```

---

## 85. Microservice Network Isolation

SalesGenie microservices shall be segmented according to trust boundaries.

Example:

```text
                    INTERNET
                       |
                       v
                [ Edge Network ]
                       |
                       v
                [ API Gateway ]
                       |
          +------------+-------------+
          |                          |
          v                          v
 [ Application Zone ]          [ AI Zone ]
          |                          |
          |                   +------+------+
          |                   |             |
          v                   v             v
 [ Service Zone ]         AI Gateway    MCP Zone
          |
    +-----+------+----------------+
    |            |                |
    v            v                v
 Database      Redis             RAG
    |                             |
    v                             v
 PostgreSQL                  Vector Store
```

---

## 86. Administrative Network

Administrative interfaces shall be separated from ordinary user traffic.

---

## 87. Super Admin Network Security

Super-admin capabilities shall require stronger controls including where appropriate:

```text
MFA
Device Verification
IP Restrictions
Privileged Access Management
Step-Up Authentication
Short-Lived Sessions
Audit Logging
```

---

## 88. Administrative API Isolation

Super-admin APIs shall not be exposed through the same unrestricted public routes as normal user APIs where architectural separation is feasible.

---

## 89. Developer Access

Developer access to production infrastructure shall be:

```text
Authenticated
Authorized
Time-Limited
Audited
Least-Privilege
```

---

## 90. Production Database Access

Direct production database access shall be highly restricted and should use controlled administrative paths.

---

## 91. Bastion / Access Gateway

If direct infrastructure administration is required, access should pass through a hardened administrative access gateway.

---

## 92. VPN / Zero-Trust Access

Private infrastructure access may use:

```text
VPN
Zero-Trust Network Access
Identity-Aware Proxy
Bastion Host
```

depending on deployment architecture.

---

## 93. Network Segmentation by Environment

Production, staging, development, and testing environments shall be logically separated.

```text
Development
      |
      X
      |
Staging
      |
      X
      |
Production
```

Production credentials and private networks shall not be reused across environments.

---

## 94. Environment Isolation

Development workloads shall not access production data by default.

---

## 95. Production Data Restrictions

Production customer data shall not be copied into development environments without explicit authorization and appropriate sanitization.

---

## 96. Network Secrets

Network credentials shall be stored securely and rotated.

---

## 97. Firewall Rules

Firewall rules shall follow:

```text
Default Deny
Explicit Allow
Minimal Ports
Minimal Sources
Minimal Destinations
Periodic Review
```

---

## 98. Firewall Change Management

Firewall changes shall be:

```text
Reviewed
Authorized
Versioned
Audited
Tested
Reversible
```

---

## 99. Network Configuration Management

Infrastructure-as-Code shall manage production network policies where feasible.

---

## 100. Configuration Drift Detection

SalesGenie shall detect unauthorized changes to network configuration.

---

## 101. Network Asset Inventory

The platform shall maintain an inventory of:

```text
Load Balancers
Gateways
Servers
Containers
Pods
Databases
Caches
Queues
Storage
Service Endpoints
Public IPs
Private IPs
DNS Records
Firewall Rules
```

---

## 102. Port Management

Only required ports shall be exposed.

Example:

```text
443  → HTTPS
80   → Redirect only where required
5432 → PostgreSQL private network only
6379 → Redis private network only
```

Internal service ports shall never be publicly exposed unnecessarily.

---

## 103. Port Scanning Detection

The infrastructure shall detect suspicious port scanning and service enumeration.

---

## 104. Network Intrusion Detection

Production infrastructure should support IDS/IPS capabilities where appropriate.

---

## 105. Network Anomaly Detection

The platform shall detect:

```text
Unexpected Traffic
Unexpected Destinations
Traffic Spikes
Port Scanning
Connection Floods
Abnormal Egress
Abnormal East-West Traffic
```

---

## 106. Network Flow Logging

Network flow information should be collected for critical infrastructure.

---

## 107. Network Security Logging

Relevant events shall include:

```text
Connection Accepted
Connection Denied
Firewall Rule Trigger
WAF Block
Rate Limit
DDoS Event
SSRF Block
Unexpected Egress
Service Authentication Failure
Administrative Access
Network Configuration Change
```

---

## 108. Network Log Security

Network logs shall:

```text
Avoid Sensitive Payloads
Be Access-Controlled
Be Tamper-Resistant
Use Secure Transport
Have Defined Retention
```

---

## 109. Network Alerting

Alerts shall support:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

---

## 110. Critical Network Alerts

Critical alerts shall include:

```text
Database Public Exposure
Unexpected Production Port
Large Unauthorized Egress
DDoS Attack
Network Policy Bypass
Cross-Environment Connectivity
Repeated SSRF Attempts
Network Credential Abuse
Internal Network Scanning
```

---

## 111. Network Incident Response

The platform shall support:

```text
Traffic Blocking
Service Isolation
Network Policy Changes
Credential Revocation
Instance Isolation
Integration Shutdown
Agent Suspension
Workflow Suspension
```

---

## 112. Compromised Service Isolation

A compromised workload shall be isolatable without requiring complete platform shutdown.

---

## 113. AI Incident Isolation

A compromised AI agent shall be isolatable by:

```text
Agent ID
Tenant
Workflow
Tool
Network Identity
Destination
```

---

## 114. Integration Incident Isolation

A compromised integration shall support immediate:

```text
Token Revocation
Webhook Disablement
Egress Blocking
Credential Rotation
Tenant Isolation
```

---

## 115. DDoS Response

DDoS mitigation shall support:

```text
Traffic Filtering
Rate Limiting
IP Reputation
Bot Mitigation
Connection Limiting
Autoscaling
Circuit Breaking
```

---

## 116. Circuit Breakers

External dependencies shall support circuit breakers to prevent cascading failures.

---

## 117. Retry Controls

Retries shall use:

```text
Exponential Backoff
Jitter
Maximum Attempts
Timeouts
Circuit Breaking
```

to prevent retry storms.

---

## 118. Network Dependency Isolation

Failure of one external provider shall not automatically compromise unrelated services.

---

## 119. Network Resource Exhaustion

Services shall protect against:

```text
Connection Pool Exhaustion
File Descriptor Exhaustion
Thread Exhaustion
Socket Exhaustion
Bandwidth Exhaustion
CPU Exhaustion
```

caused by malicious traffic.

---

## 120. Request Queue Protection

Public request queues shall have bounded capacity.

---

## 121. Load Balancer Security

Load balancers shall support:

```text
TLS Termination
Health Checks
Connection Limits
Access Logging
WAF Integration
DDoS Controls
```

---

## 122. Health Check Security

Health endpoints shall reveal minimal information.

Detailed infrastructure diagnostics shall not be publicly exposed.

---

## 123. Internal Health Checks

Internal health checks shall authenticate where required.

---

## 124. Service Discovery Security

Service discovery shall prevent unauthorized service registration and spoofing.

---

## 125. Service Mesh Security

Where a service mesh is used, it should provide:

```text
mTLS
Service Identity
Authorization Policies
Traffic Encryption
Traffic Telemetry
Retries
Circuit Breaking
```

---

## 126. Container Network Security

Containers shall:

```text
Run With Least Network Privilege
Avoid Host Networking Unless Required
Restrict Capabilities
Use Network Policies
Avoid Unnecessary Ports
```

---

## 127. Kubernetes Network Security

If Kubernetes is used, SalesGenie shall implement:

```text
NetworkPolicies
Namespace Isolation
Pod Security
Service Accounts
mTLS Where Appropriate
Ingress Controls
Egress Policies
```

---

## 128. Container-to-Host Isolation

Application workloads shall not access host network resources unless explicitly required.

---

## 129. Cloud Security Groups

Cloud security groups shall follow default-deny principles.

---

## 130. Cloud Network Architecture

Production architecture should separate:

```text
Public Subnets
Private Application Subnets
Private Data Subnets
Administrative Networks
```

---

## 131. Private Database Subnet

Databases shall reside in private network segments where supported.

---

## 132. NAT / Egress Gateway

Private workloads requiring Internet access should route through controlled egress infrastructure.

---

## 133. Egress Gateway Logging

Outbound Internet traffic from sensitive workloads should be observable.

---

## 134. Network Encryption

Traffic between cloud zones and regions shall use secure encrypted channels where applicable.

---

## 135. Cross-Region Communication

Cross-region traffic shall use authenticated and encrypted connections.

---

## 136. Multi-Region Security

Each region shall independently enforce:

```text
Identity
Network Policy
Tenant Isolation
Encryption
Logging
Egress Controls
```

---

## 137. Data Residency Network Controls

Network routing shall respect configured data-residency policies.

---

## 138. CDN Security

CDN configuration shall:

```text
Use TLS
Protect Origin
Restrict Origin Access
Support DDoS Mitigation
Prevent Cache Poisoning
```

---

## 139. Origin Protection

Application origins shall not be directly exposed when CDN/WAF architecture is intended to protect them.

---

## 140. Cache Security

Sensitive authenticated responses shall not be publicly cached.

---

## 141. Cache Key Isolation

Cache keys shall preserve appropriate:

```text
Tenant
User
Authorization Context
Resource
```

boundaries.

---

## 142. API Cache Security

Authorization shall not be bypassed through cached API responses.

---

## 143. Network Data Exfiltration Protection

Sensitive outbound network traffic shall be monitored and controlled.

---

## 144. Destination Reputation

High-risk outbound destinations may be blocked based on security intelligence.

---

## 145. Domain Allowlisting

Critical services shall use destination allowlists where practical.

---

## 146. IP Allowlisting

Administrative interfaces may support IP allowlisting.

---

## 147. Dynamic IP Management

Network policies shall not depend on fragile hard-coded IP addresses when service identities or managed discovery mechanisms are available.

---

## 148. Geo-Based Controls

Where appropriate, the platform may apply geographic restrictions for administrative or high-risk access.

---

## 149. Network Time Synchronization

Production infrastructure shall use trusted time synchronization to support:

```text
TLS
Authentication
Token Validation
Audit
Replay Protection
Incident Investigation
```

---

## 150. Network Security Testing

SalesGenie shall implement:

```text
Port Scanning Tests
Firewall Tests
SSRF Tests
DDoS Tests
WAF Tests
TLS Tests
Network Policy Tests
Service Authentication Tests
Egress Tests
Tenant Isolation Tests
Container Network Tests
Kubernetes Network Tests
Webhook Tests
AI Network Tests
MCP Network Tests
Workflow Network Tests
```

---

## 151. Network Penetration Testing

Periodic penetration testing shall evaluate:

```text
Internet Perimeter
API Gateway
Public APIs
Webhook Endpoints
OAuth Callbacks
Internal APIs
Service Mesh
Administrative Interfaces
Cloud Networking
```

---

## 152. SSRF Test Matrix

The test suite shall attempt access to:

```text
localhost
127.0.0.1
Private IPv4 Ranges
Private IPv6 Ranges
Link-Local Addresses
Cloud Metadata Endpoints
Internal DNS Names
Internal Service Names
Redirected Internal URLs
DNS Rebinding Targets
```

---

## 153. Network Isolation Test Matrix

The platform shall verify:

```text
Public Internet → Database = DENY

Public Internet → Redis = DENY

Public Internet → Vector DB = DENY

Public Internet → Internal APIs = DENY

Tenant A → Tenant B Network Resources = DENY

AI Agent → Database = DENY unless explicitly mediated

AI Agent → Metadata Endpoint = DENY

Workflow → Arbitrary Internal Network = DENY

MCP Tool → Unauthorized Service = DENY
```

---

## 154. AI Network Security Testing

Tests shall verify that malicious prompts cannot cause agents to:

```text
Scan Internal Networks
Access Metadata Services
Access Databases
Reach Private Services
Exfiltrate Customer Data
Bypass Egress Policies
Reach Unauthorized Integrations
```

---

## 155. MCP Network Testing

MCP security tests shall verify:

```text
Unauthorized Tool Access
Unauthorized Destination
SSRF
Credential Abuse
Lateral Movement
Network Exfiltration
Cross-Tenant Access
```

---

## 156. Workflow Network Testing

Workflow security tests shall verify:

```text
SSRF
Open Proxy Abuse
Port Scanning
Internal Service Discovery
Unauthorized Egress
Network Flooding
Data Exfiltration
```

---

## 157. Network Security CI/CD Gates

Production deployment shall require:

```text
Infrastructure Security Tests
Firewall Validation
Network Policy Validation
TLS Validation
Secret Scanning
SSRF Tests
Container Network Tests
Dependency Scanning
SAST
DAST
Configuration Scanning
```

---

## 158. Network Configuration as Code

Network configurations should be version-controlled.

Examples:

```text
Firewall Rules
Security Groups
Network Policies
Ingress Rules
Egress Rules
DNS Configuration
Load Balancer Configuration
WAF Rules
```

---

## 159. Network Configuration Review

High-risk network changes shall require review and approval.

---

## 160. Network Configuration Rollback

Network configuration changes shall be reversible.

---

## 161. Network Security Drift Detection

The platform shall detect deviations between approved network architecture and deployed configuration.

---

## 162. Security Baseline

Production networking shall have a documented baseline covering:

```text
Public Ports
Private Ports
Allowed Services
Allowed Destinations
Allowed Egress
Firewall Rules
WAF Rules
DNS
TLS
Network Policies
Administrative Access
```

---

## 163. Human-to-Service Network Flow

```text
Human
  |
  v
Internet
  |
  v
DDoS Protection
  |
  v
CDN
  |
  v
WAF
  |
  v
Load Balancer
  |
  v
API Gateway
  |
  v
Authentication
  |
  v
Authorization
  |
  v
Microservice
```

---

## 164. AI-to-Service Network Flow

```text
User
  |
  v
API Gateway
  |
  v
AI Orchestrator
  |
  v
Policy Engine
  |
  v
AI Agent
  |
  v
Tool Authorization
  |
  v
Controlled Network Proxy
  |
  +----> Approved Internal Service
  |
  +----> Approved External API
  |
  +----> Approved MCP Server
```

---

## 165. Secure AI Internet Architecture

```text
                 AI AGENT
                     |
                     v
             AI NETWORK SANDBOX
                     |
                     v
             EGRESS POLICY ENGINE
                     |
          +----------+----------+
          |                     |
        DENY                  ALLOW
          |                     |
          v                     v
       BLOCKED            SECURITY PROXY
                                |
                                v
                         DNS VALIDATION
                                |
                                v
                       DESTINATION POLICY
                                |
                                v
                          DLP / AUDIT
                                |
                                v
                           INTERNET
```

---

## 166. Secure Microservice Architecture

```text
                        INTERNET
                           |
                           v
                    [ DDoS / CDN ]
                           |
                           v
                         [ WAF ]
                           |
                           v
                    [ Load Balancer ]
                           |
                           v
                      [ API Gateway ]
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
     Auth Service      AI Gateway       Billing Service
          |                |                |
          |                v                |
          |           AI Providers          |
          |                                 |
          +----------------+----------------+
                           |
                           v
                    Internal Services
                           |
        +------------------+------------------+
        |                  |                  |
        v                  v                  v
    PostgreSQL           Redis             RAG
                                              |
                                              v
                                        Vector Store
```

---

## 167. Zero-Trust Network Decision

Every sensitive network request should conceptually pass through:

```text
REQUEST
   |
   v
IDENTITY
   |
   v
AUTHENTICATION
   |
   v
TENANT
   |
   v
AUTHORIZATION
   |
   v
NETWORK POLICY
   |
   v
DESTINATION POLICY
   |
   v
DATA POLICY
   |
   v
ALLOW / DENY
   |
   v
AUDIT
```

---

## 168. Network Security Invariants

The following conditions shall always remain true:

```text
1. Public Internet cannot directly access private databases.

2. Public Internet cannot directly access Redis.

3. Public Internet cannot directly access vector stores.

4. Internal network location does not automatically grant trust.

5. Service identity is required for sensitive service-to-service communication.

6. AI agents cannot automatically access arbitrary internal services.

7. AI agents cannot access cloud metadata services.

8. AI agents cannot use unrestricted outbound Internet access by default.

9. MCP tools cannot bypass network policy.

10. Workflows cannot bypass network policy.

11. User-supplied URLs cannot automatically become trusted destinations.

12. SSRF protections apply to every server-side URL-fetch capability.

13. Webhook payloads are authenticated before processing.

14. OAuth callbacks validate state and redirect destinations.

15. Sensitive traffic uses encrypted transport.

16. Production and development networks are isolated.

17. Administrative access uses stronger controls.

18. Database ports are never unnecessarily public.

19. Egress from high-risk workloads is controlled.

20. Network failures default to deny.

21. Network policies are version-controlled.

22. Network changes are auditable.

23. Security logs do not expose sensitive payloads.

24. Compromised services can be isolated.

25. Network traffic remains tenant-aware at the application layer.

26. AI-generated actions cannot expand network privileges.

27. Delegated agents cannot exceed delegated network permissions.

28. External integrations cannot arbitrarily reach internal services.

29. Network-level controls do not replace application authorization.

30. Application authorization does not replace network segmentation.
```

---

## 169. Network Security Metrics

SalesGenie shall monitor:

```text
Blocked Requests
Allowed Requests
WAF Blocks
DDoS Events
Rate-Limit Events
SSRF Attempts
Blocked Egress
Unexpected Egress
Firewall Denials
Port Scan Events
Authentication Failures
Service-to-Service Authentication Failures
Network Policy Violations
Webhook Failures
OAuth Callback Failures
AI Network Violations
MCP Network Violations
Workflow Network Violations
Connection Exhaustion
Circuit Breaker Events
TLS Failures
Certificate Expiration
```

---

## 170. Network Security SLOs

Production shall define measurable SLOs for:

```text
Network Availability
API Availability
DDoS Mitigation
TLS Availability
DNS Availability
Internal Service Connectivity
Security Event Detection
Incident Containment
Network Policy Deployment
Certificate Renewal
```

---

## 171. Network Security Acceptance Criteria

## AC-NETSEC-001

All public application traffic uses HTTPS.

## AC-NETSEC-002

Sensitive internal communication uses authenticated and encrypted transport.

## AC-NETSEC-003

Internal services are not publicly accessible unless explicitly required.

## AC-NETSEC-004

PostgreSQL is not directly exposed to the Internet.

## AC-NETSEC-005

Redis is not directly exposed to the Internet.

## AC-NETSEC-006

Vector databases are not directly exposed to the Internet.

## AC-NETSEC-007

Public traffic passes through appropriate perimeter controls.

## AC-NETSEC-008

Production firewall rules use default-deny principles.

## AC-NETSEC-009

Service-to-service communication requires appropriate authentication.

## AC-NETSEC-010

Service authorization restricts communication to approved destinations.

## AC-NETSEC-011

Production workloads use network segmentation.

## AC-NETSEC-012

Development and production networks are isolated.

## AC-NETSEC-013

SSRF protections block unauthorized private-network access.

## AC-NETSEC-014

Cloud metadata endpoints cannot be arbitrarily accessed.

## AC-NETSEC-015

AI agents cannot access arbitrary internal network resources.

## AC-NETSEC-016

AI agents do not have unrestricted Internet access by default.

## AC-NETSEC-017

MCP servers use authenticated and authorized network communication.

## AC-NETSEC-018

Workflow HTTP actions enforce SSRF and egress protections.

## AC-NETSEC-019

Webhook endpoints validate signatures and prevent replay where applicable.

## AC-NETSEC-020

OAuth callbacks validate state and redirect parameters.

## AC-NETSEC-021

Public APIs implement rate limiting.

## AC-NETSEC-022

DDoS mitigation protects public infrastructure.

## AC-NETSEC-023

WAF protections cover relevant common web attacks.

## AC-NETSEC-024

Administrative interfaces have stronger network access controls.

## AC-NETSEC-025

Network configuration changes are audited.

## AC-NETSEC-026

Network security logs are protected from unauthorized access.

## AC-NETSEC-027

Network anomalies generate alerts.

## AC-NETSEC-028

Compromised workloads can be isolated.

## AC-NETSEC-029

Network policies are tested automatically.

## AC-NETSEC-030

Critical network-security vulnerabilities block production deployment unless formally risk-accepted.

---

## 172. FAANG-Level Network Security Quality Gates

```text
[ ] Zero-trust network architecture
[ ] Network segmentation
[ ] Public/private network separation
[ ] Default-deny firewall
[ ] Security groups
[ ] Network ACLs
[ ] Kubernetes NetworkPolicies
[ ] Service identity
[ ] mTLS where appropriate
[ ] TLS
[ ] Certificate lifecycle management
[ ] HSTS
[ ] Secure DNS
[ ] DNS monitoring
[ ] DNS rebinding protection
[ ] SSRF protection
[ ] Cloud metadata protection
[ ] Egress filtering
[ ] Egress allowlisting
[ ] DLP for high-risk egress
[ ] DDoS protection
[ ] WAF
[ ] Bot protection
[ ] API gateway protection
[ ] Rate limiting
[ ] Adaptive rate limiting
[ ] Connection limits
[ ] Request size limits
[ ] Timeout controls
[ ] Circuit breakers
[ ] Retry controls
[ ] WebSocket security
[ ] SSE security
[ ] CORS
[ ] CSRF protection where applicable
[ ] Security headers
[ ] Database network isolation
[ ] Redis network isolation
[ ] Vector database isolation
[ ] Object storage security
[ ] Message broker security
[ ] Queue isolation
[ ] Webhook security
[ ] OAuth callback security
[ ] Integration egress controls
[ ] AI gateway network isolation
[ ] AI provider allowlisting
[ ] AI agent sandboxing
[ ] AI egress control
[ ] AI exfiltration prevention
[ ] MCP network isolation
[ ] Workflow network isolation
[ ] Admin network isolation
[ ] Production/staging/dev isolation
[ ] Infrastructure-as-Code
[ ] Configuration drift detection
[ ] Network asset inventory
[ ] Port management
[ ] Network flow logging
[ ] IDS/IPS
[ ] Network anomaly detection
[ ] Network security alerting
[ ] Incident response
[ ] Compromised workload isolation
[ ] DDoS response
[ ] Penetration testing
[ ] SSRF testing
[ ] AI network security testing
[ ] MCP security testing
[ ] Workflow security testing
[ ] CI/CD network-security gates
[ ] Network configuration rollback
[ ] Disaster recovery
```

---

## 173. Definition of Done

`network_security.md` shall be considered fully implemented when SalesGenie provides end-to-end network protection across:

```text
Human Users
AI Agents
API Gateway
Authentication Service
Authorization Service
AI Gateway
Multi-Agent Orchestrator
RAG Service
Vector Database
Workflow Engine
MCP Servers
Integration Services
Lead Intelligence
Billing Service
Notification Services
Background Workers
PostgreSQL
Redis
Object Storage
Message Brokers
Webhooks
OAuth Callbacks
External APIs
AI Providers
Administrative APIs
Monitoring Systems
```

The final network-security architecture shall guarantee:

```text
                         INTERNET
                            |
                            v
                     [ DDoS Defense ]
                            |
                            v
                         [ CDN ]
                            |
                            v
                          [ WAF ]
                            |
                            v
                    [ Load Balancer ]
                            |
                            v
                      [ API Gateway ]
                            |
                +-----------+-----------+
                |                       |
                v                       v
        [ Authentication ]       [ AI Gateway ]
                |                       |
                v                       v
        [ Authorization ]        [ AI Policy ]
                |                       |
                +-----------+-----------+
                            |
                            v
                    [ Network Policy ]
                            |
            +---------------+----------------+
            |               |                |
            v               v                v
      [ App Services ] [ AI Services ] [ Integration ]
            |               |                |
            |               v                v
            |          [ RAG / MCP ]   [ External APIs ]
            |               |
            +-------+-------+
                    |
                    v
             [ Private Data ]
                    |
          +---------+---------+
          |         |         |
          v         v         v
      PostgreSQL  Redis   Vector DB
```

SalesGenie shall ensure that **every network path is explicitly authorized, encrypted where required, minimized, monitored, auditable, and isolated according to trust boundaries—with particular protection against lateral movement, SSRF, unauthorized egress, AI-agent abuse, MCP abuse, workflow abuse, integration compromise, and cross-tenant access.**
