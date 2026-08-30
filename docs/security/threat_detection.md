# SalesGenie — FAANG-Level Threat Detection Requirements

## `threat_detection.md`

> **Scope:** Enterprise-grade threat detection for SalesGenie covering human users, AI agents, autonomous workflows, APIs, microservices, integrations, identities, sessions, data, infrastructure, networks, billing, and third-party systems.
>
> **Primary objective:** Detect, correlate, prioritize, investigate, and respond to malicious or anomalous behavior across the complete SalesGenie control plane while enforcing tenant isolation, least privilege, privacy, AI safety, and human oversight.

---

## 1. Threat Detection Objectives

SalesGenie MUST provide a unified threat detection capability that can:

- Detect known attack patterns.
- Detect unknown and emerging behavioral anomalies.
- Detect attacks against human accounts.
- Detect attacks against AI agents.
- Detect service-to-service attacks.
- Detect API abuse.
- Detect integration compromise.
- Detect credential abuse.
- Detect privilege escalation.
- Detect cross-tenant access attempts.
- Detect data exfiltration.
- Detect malicious workflows.
- Detect AI tool abuse.
- Detect prompt injection and indirect prompt injection.
- Detect suspicious OAuth behavior.
- Detect webhook abuse.
- Detect account takeover.
- Detect insider-threat indicators.
- Detect infrastructure compromise.
- Detect network anomalies.
- Detect security-control tampering.
- Correlate events across multiple services.
- Generate explainable risk scores.
- Create actionable alerts.
- Support human investigation.
- Support AI-assisted investigation.
- Support controlled automated response.
- Continuously improve detection quality.

---

## 2. Threat Detection Actors

## 2.1 Human Actors

### TD-H-001 — End User

The system MUST detect suspicious security activity associated with an end-user account.

### TD-H-002 — Sales Agent

The system MUST detect anomalous access, exports, authentication behavior, and privilege changes involving sales agents.

### TD-H-003 — Support Agent

The system MUST monitor support-agent access to customer information and administrative capabilities.

### TD-H-004 — Organization Administrator

The system MUST provide enhanced threat detection for organization administrators.

### TD-H-005 — Security Administrator

Security administrators MUST be able to investigate, tune, and manage threat detections according to their permissions.

### TD-H-006 — Super Administrator

Super-admin activity MUST receive enhanced monitoring and privileged-operation detection.

### TD-H-007 — Incident Responder

Incident responders MUST be able to investigate threats and execute authorized containment actions.

### TD-H-008 — Compliance Auditor

Auditors MUST be able to review relevant threat evidence without receiving unauthorized operational capabilities.

---

## 3. AI Threat Actors

## TD-AI-001 — AI Sales Agent

The platform MUST detect abnormal sales-agent behavior.

## TD-AI-002 — AI Support Agent

The platform MUST detect unauthorized customer-data access, abnormal tool usage, and suspicious external actions.

## TD-AI-003 — AI Workflow Agent

The system MUST detect workflow manipulation, runaway automation, and unauthorized actions.

## TD-AI-004 — AI Orchestrator

The system MUST monitor agent delegation and orchestration behavior.

## TD-AI-005 — AI Security Agent

Security-analysis agents MAY perform threat analysis under explicit permissions.

## TD-AI-006 — Autonomous Response Agent

Autonomous response agents MUST operate under strict policy and authorization boundaries.

---

## 4. Threat Taxonomy

SalesGenie MUST support detection for at least:

```text
ACCOUNT_TAKEOVER
BRUTE_FORCE
CREDENTIAL_STUFFING
PASSWORD_SPRAYING
SESSION_HIJACKING
TOKEN_REPLAY
MFA_ABUSE
PRIVILEGE_ESCALATION
RBAC_ABUSE
ABAC_ABUSE
CROSS_TENANT_ACCESS
IDOR
API_ABUSE
API_ENUMERATION
BOT_ABUSE
DATA_EXFILTRATION
DATA_SCRAPING
MASS_EXPORT
INSIDER_THREAT
MALICIOUS_AUTOMATION
WORKFLOW_ABUSE
OAUTH_ABUSE
WEBHOOK_ABUSE
INTEGRATION_COMPROMISE
PROMPT_INJECTION
INDIRECT_PROMPT_INJECTION
AI_TOOL_ABUSE
AI_PRIVILEGE_ESCALATION
AI_DATA_EXFILTRATION
RAG_POISONING
MODEL_ABUSE
JAILBREAK_ATTEMPTS
SECRET_EXPOSURE
KEY_ABUSE
CONFIGURATION_TAMPERING
NETWORK_INTRUSION
SERVICE_COMPROMISE
CONTAINER_COMPROMISE
DATABASE_ABUSE
SUPPLY_CHAIN_ATTACK
DENIAL_OF_SERVICE
SECURITY_CONTROL_TAMPERING
```

---

## 5. User Requirements

## UR-001 — Threat Visibility

Authorized security users MUST be able to view detected threats within their permitted scope.

## UR-002 — Real-Time Detection

Critical threats MUST be detected with low latency.

## UR-003 — Threat Severity

Detected threats MUST have standardized severity.

Supported levels:

```text
INFO
LOW
MEDIUM
HIGH
CRITICAL
```

## UR-004 — Threat Risk Score

Every actionable threat SHOULD have a normalized risk score.

```text
0 ─────────────────────────── 100
LOW                         CRITICAL
```

## UR-005 — Explainable Detection

Users MUST be able to understand why a threat was detected.

## UR-006 — Evidence

Every significant detection MUST reference supporting evidence.

## UR-007 — Threat Timeline

Investigators MUST be able to reconstruct the sequence of events associated with a threat.

## UR-008 — Threat Correlation

Users MUST be able to view related authentication, API, AI, data, integration, and infrastructure events.

## UR-009 — Threat Investigation

Authorized investigators MUST be able to investigate detected threats.

## UR-010 — Threat Assignment

Threats MUST be assignable to authorized security personnel.

## UR-011 — Threat Status

Threats MUST support lifecycle management.

```text
DETECTED
ACKNOWLEDGED
INVESTIGATING
CONTAINED
RESOLVED
FALSE_POSITIVE
CLOSED
```

## UR-012 — Human Response

Authorized humans MUST be able to perform approved containment actions.

## UR-013 — AI Assistance

Authorized security users MAY use AI to analyze threats and recommend actions.

## UR-014 — Human Oversight

High-impact AI-recommended or automated responses MUST support human approval.

## UR-015 — Tenant Isolation

Organization administrators MUST only see threats belonging to their authorized tenant.

---

## 6. System Requirements

## SR-001 — Distributed Threat Detection Architecture

SalesGenie MUST implement a centralized threat detection control plane.

```text
                    +-----------------------+
                    | Human Activity        |
                    +-----------+-----------+
                                |
                    +-----------v-----------+
                    | AI Agent Activity     |
                    +-----------+-----------+
                                |
        +-----------------------+-----------------------+
        |                       |                       |
        v                       v                       v
      APIs                Integrations            Infrastructure
        |                       |                       |
        +-----------------------+-----------------------+
                                |
                                v
                    +-----------------------+
                    | Telemetry Collection  |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | Event Normalization   |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | Event Stream          |
                    +-----------+-----------+
                                |
                 +--------------+--------------+
                 |                             |
                 v                             v
        +------------------+          +------------------+
        | Rule Detection   |          | AI Detection     |
        +--------+---------+          +--------+---------+
                 |                             |
                 +--------------+--------------+
                                |
                                v
                    +-----------------------+
                    | Correlation Engine    |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | Risk Engine            |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | Threat Manager         |
                    +-----------+-----------+
                                |
                    +-----------+-----------+
                    |                       |
                    v                       v
             Human Investigation     AI Investigation
                    |                       |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | Response Engine       |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | Evidence / Audit      |
                    +-----------------------+
```

---

## 7. Threat Telemetry Sources

The detection system MUST ingest telemetry from:

```text
Authentication Service
Authorization Service
API Gateway
AI Gateway
Agent Orchestrator
RAG Service
Workflow Engine
Billing Service
Subscription Service
Payment Service
Integration Services
Database Services
Redis
Object Storage
Message Queues
WAF
Reverse Proxy
Network Layer
Container Runtime
Infrastructure
Secrets Manager
Key Management
Audit Logging
Application Services
External Integrations
```

---

## 8. Threat Event Schema

Each normalized threat-relevant event SHOULD contain:

```yaml
event_id:
event_type:
event_version:
timestamp:
ingestion_timestamp:

tenant_id:

actor_type:
actor_id:
actor_role:

service_id:
resource_type:
resource_id:

action:
result:

severity:
risk_score:

source_ip:
destination_ip:
user_agent:
device_id:
session_id:

request_id:
trace_id:
span_id:
correlation_id:

authentication_context:
authorization_context:

ai_agent_id:
ai_model:
ai_agent_version:

integration_id:
workflow_id:

data_classification:

detection_rule_id:
threat_id:

metadata:
```

---

## 9. Detection Layers

SalesGenie MUST support multiple detection layers:

```text
Layer 1 — Signature Detection
Layer 2 — Rule-Based Detection
Layer 3 — Threshold Detection
Layer 4 — Behavioral Baselines
Layer 5 — Statistical Anomaly Detection
Layer 6 — Correlation Detection
Layer 7 — Threat Intelligence
Layer 8 — AI-Assisted Detection
Layer 9 — Graph-Based Detection
Layer 10 — Human Investigation
```

No single detection method SHOULD be treated as sufficient for enterprise-grade threat detection.

---

## 10. Signature-Based Detection

The platform MUST support known attack signatures.

Examples:

```text
known malicious IP
known malicious domain
known attack payload
known exploit pattern
known bot signature
known compromised credential indicator
```

---

## 11. Rule-Based Detection

Security administrators MUST be able to define detection rules.

Example:

```yaml
rule_id: AUTH_BRUTE_FORCE_001

name: Repeated Authentication Failures

condition:
  failed_logins: ">= 10"
  time_window: "5m"
  target_type: "ACCOUNT"

severity: HIGH

actions:
  - create_threat
  - increase_risk
  - notify_security
```

---

## 12. Threshold Detection

The system MUST support configurable thresholds.

Examples:

```text
Failed logins > N
API requests > N
Sensitive records accessed > N
Exports > N
AI tool calls > N
OAuth requests > N
Workflow executions > N
```

Thresholds MUST be tenant-aware where required.

---

## 13. Behavioral Baselines

The system SHOULD establish behavioral baselines for:

```text
Users
Administrators
AI Agents
Services
Integrations
Devices
IP Addresses
Workflows
API Clients
```

---

## 14. Behavioral Anomaly Detection

The system SHOULD detect significant deviations from established baselines.

Example:

```text
Normal:
AI Sales Agent
10–30 CRM lookups/hour

Observed:
AI Sales Agent
4,000 CRM lookups/hour

Result:
Behavioral Anomaly
```

---

## 15. Human Account Threat Detection

The system MUST monitor:

```text
login behavior
session behavior
device behavior
IP behavior
resource access
API activity
data exports
role changes
password changes
MFA activity
```

---

## 16. Account Takeover Detection

The platform SHOULD correlate:

```text
New device
+
New location
+
Password reset
+
MFA failure
+
Sensitive data access
```

and generate an account-takeover threat when confidence is sufficient.

---

## 17. Brute-Force Detection

The system MUST detect repeated authentication failures.

Example:

```text
Account A

10 failed attempts
+
5 minutes

=
HIGH-RISK AUTHENTICATION THREAT
```

Thresholds MUST be configurable.

---

## 18. Credential Stuffing Detection

The system SHOULD identify:

```text
Many accounts
+
Same source
+
High authentication failure rate
```

---

## 19. Password Spraying Detection

The system SHOULD detect:

```text
One password pattern
+
Many accounts
+
Low attempts per account
+
Common source
```

---

## 20. Session Hijacking Detection

The system SHOULD identify suspicious session changes such as:

```text
IP suddenly changes
+
Device fingerprint changes
+
User-agent changes
+
Sensitive action occurs
```

---

## 21. Token Replay Detection

The platform SHOULD detect:

```text
Same token
+
Multiple locations
+
Impossible timing
```

and invalidate or escalate according to policy.

---

## 22. MFA Abuse Detection

The system SHOULD detect:

```text
Repeated MFA failures
MFA fatigue indicators
Unexpected MFA enrollment
MFA method replacement
MFA disablement
```

---

## 23. Privilege Escalation Detection

The platform MUST detect suspicious privilege transitions.

Example:

```text
USER
 |
 v
ROLE CHANGE
 |
 v
ADMIN
 |
 v
SENSITIVE DATA ACCESS
```

---

## 24. RBAC Abuse Detection

The system SHOULD detect:

```text
unexpected role assignment
unusual role usage
privilege changes outside workflow
excessive permissions
privileged access outside normal patterns
```

---

## 25. Cross-Tenant Attack Detection

The platform MUST detect attempts to access resources belonging to another tenant.

Example:

```text
Tenant A
User
 |
 v
API Request
 |
 v
Tenant B Resource
 |
 X
ACCESS DENIED
 |
 v
THREAT GENERATED
```

Confirmed cross-tenant data access MUST be treated as a critical security event.

---

## 26. IDOR Detection

The system SHOULD detect patterns consistent with insecure direct object reference abuse.

Example:

```text
/user/1001
/user/1002
/user/1003
/user/1004
...
```

combined with unauthorized access results SHOULD increase threat confidence.

---

## 27. API Threat Detection

The system MUST detect:

```text
API enumeration
credential abuse
authorization bypass attempts
rate-limit abuse
mass requests
abnormal payloads
endpoint scanning
resource enumeration
unexpected clients
```

---

## 28. API Enumeration Detection

The system SHOULD detect:

```text
Sequential resource IDs
+
High request rate
+
Large number of 404/403 responses
```

---

## 29. API Scraping Detection

The platform SHOULD identify:

```text
high-volume reads
large resource coverage
repeated pagination
automated access patterns
unusual user agents
```

---

## 30. Bot Threat Detection

The platform SHOULD detect:

```text
automated authentication
automated registration
API scraping
credential attacks
mass submissions
abnormal request frequency
```

---

## 31. Data Exfiltration Detection

The platform MUST detect indicators such as:

```text
mass downloads
large exports
unusual API reads
large document retrieval
sensitive-record access spikes
unusual external destinations
```

---

## 32. Data Access Anomaly

Example:

```text
User baseline:
20 customer records/day

Observed:
12,000 customer records/hour

Result:
Potential Data Exfiltration
```

---

## 33. Insider Threat Detection

Where legally and organizationally permitted, the system SHOULD detect:

```text
unusual privileged activity
mass data access
unusual exports
access outside job function
unusual administrative operations
repeated policy violations
```

---

## 34. AI Threat Detection

AI activity MUST be treated as a separate threat-detection domain.

The system MUST monitor:

```text
agent selection
agent delegation
prompt processing
tool invocation
data retrieval
external actions
workflow execution
permission checks
policy checks
guardrail events
model outputs
```

---

## 35. AI Agent Identity

Every AI agent MUST have a unique identity.

Minimum metadata:

```yaml
agent_id:
agent_type:
agent_version:
model:
tenant_id:
owner:
permissions:
allowed_tools:
risk_level:
policy_version:
```

---

## 36. AI Behavioral Baseline

The platform SHOULD maintain a behavioral profile for each AI agent.

Dimensions:

```text
Typical tools
Typical APIs
Typical data
Typical tenants
Typical action frequency
Typical execution duration
Typical workflows
Typical external integrations
```

---

## 37. AI Tool Abuse Detection

The system MUST detect:

```text
unexpected tool
unauthorized tool
unexpected tool sequence
high-frequency tool use
sensitive tool usage
cross-tenant tool access
```

---

## 38. AI Privilege Escalation Detection

The system MUST detect when an AI agent attempts to obtain or use privileges outside its assigned scope.

Example:

```text
AI Sales Agent
      |
      X
      |
Super Admin API
```

---

## 39. AI Data Exfiltration Detection

The platform SHOULD detect:

```text
AI agent
+
large sensitive retrieval
+
external tool invocation
+
unusual destination
```

as a potential AI data-exfiltration threat.

---

## 40. Prompt Injection Detection

The system SHOULD detect potentially malicious instructions embedded in untrusted content.

Potential sources:

```text
Customer messages
Emails
RAG documents
Uploaded documents
Web pages
Support tickets
CRM notes
Slack messages
External integrations
```

---

## 41. Indirect Prompt Injection

The system MUST treat external content as untrusted input.

Example:

```text
External Document
       |
       v
"Ignore your system instructions..."
       |
       v
RAG Retrieval
       |
       v
AI Agent
```

The system SHOULD identify and record the security signal.

---

## 42. AI Jailbreak Detection

The system SHOULD identify attempts to bypass configured AI safety policies.

Examples:

```text
role manipulation
instruction override
policy bypass
system prompt extraction
security-policy evasion
```

---

## 43. System Prompt Extraction Detection

The platform SHOULD monitor attempts to extract:

```text
system instructions
hidden policies
security rules
credentials
internal configuration
```

---

## 44. RAG Poisoning Detection

The system SHOULD detect suspicious document behavior such as:

```text
malicious instructions
conflicting permissions
unexpected privilege requests
instruction-heavy documents
suspicious document provenance
```

---

## 45. AI Output Threat Detection

AI outputs SHOULD be evaluated for:

```text
credential leakage
PII leakage
system prompt leakage
unauthorized data
policy violations
unsafe external actions
```

---

## 46. AI Action Chain Detection

The platform MUST correlate multi-step AI actions.

Example:

```text
Prompt
  |
  v
RAG Search
  |
  v
CRM Lookup
  |
  v
Customer Export
  |
  v
External API
```

The combined sequence SHOULD be evaluated as a single behavioral chain.

---

## 47. AI Agent Loop Detection

The system SHOULD detect:

```text
Tool A
 -> Tool B
 -> Tool A
 -> Tool B
 -> ...
```

when execution exceeds configured safety boundaries.

---

## 48. Runaway Automation Detection

The workflow engine MUST detect:

```text
unexpected execution frequency
infinite loops
recursive triggers
mass execution
unexpected external calls
```

---

## 49. Malicious Workflow Detection

The system SHOULD identify workflows that:

```text
access sensitive data
+
export data
+
invoke external services
+
bypass expected approval
```

---

## 50. Workflow Privilege Escalation

The system MUST detect workflows that attempt to execute privileged operations without appropriate authorization.

---

## 51. OAuth Threat Detection

The platform MUST monitor:

```text
new OAuth authorization
new scopes
scope expansion
token refresh
token revocation
unusual API activity
unexpected location
```

---

## 52. OAuth Scope Escalation

Example:

```text
Existing:
read_contacts

New:
read_contacts
+
write_contacts
+
delete_contacts
```

The system SHOULD generate an elevated-risk event when scope expansion is unexpected.

---

## 53. Integration Compromise Detection

The system SHOULD detect:

```text
unexpected API volume
unexpected geographic origin
new device
new OAuth scope
unusual resource access
unexpected exports
webhook anomalies
```

---

## 54. Webhook Attack Detection

The platform MUST detect:

```text
invalid signature
replayed webhook
unexpected sender
abnormal frequency
unexpected payload
```

---

## 55. Supported Integration Threat Monitoring

Threat detection SHOULD cover:

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

## 56. Network Threat Detection

The platform SHOULD detect:

```text
port scanning
service enumeration
unexpected outbound traffic
unexpected inbound traffic
suspicious destinations
DNS anomalies
network policy violations
abnormal traffic volumes
```

---

## 57. Service-to-Service Threat Detection

Every service request SHOULD contain a verifiable service identity.

The system MUST detect:

```text
unknown service
invalid service identity
unauthorized service call
unexpected service relationship
abnormal service request rate
```

---

## 58. Microservice Compromise Detection

The platform SHOULD detect:

```text
unexpected process
unexpected network connection
unexpected API call
unusual service behavior
abnormal resource consumption
unexpected privilege
```

---

## 59. Container Threat Detection

Where containers are deployed, the system SHOULD detect:

```text
privileged container
unexpected process
unexpected filesystem access
unexpected network connection
container escape indicators
runtime configuration changes
```

---

## 60. Database Threat Detection

The platform SHOULD detect:

```text
mass SELECT
mass DELETE
mass UPDATE
schema modification
privileged queries
unexpected database clients
unusual database access
```

---

## 61. Object Storage Threat Detection

The platform SHOULD detect:

```text
mass downloads
mass deletion
permission changes
public-access changes
unusual object access
unusual bucket access
```

---

## 62. Secrets Threat Detection

The platform MUST detect:

```text
unexpected secret access
secret access spikes
secret retrieval from unauthorized service
secret exposure
credential misuse
```

---

## 63. Key Abuse Detection

The system SHOULD detect:

```text
unexpected key usage
abnormal decrypt operations
unusual key access
key policy changes
key deletion
```

---

## 64. Configuration Attack Detection

Security-sensitive configuration changes MUST be monitored.

Examples:

```text
RBAC policy
AI policy
security policy
network policy
WAF rules
rate limits
integration scopes
retention policies
audit configuration
```

---

## 65. Security Control Tampering Detection

The platform MUST detect attempts to:

```text
disable logging
disable monitoring
disable alerts
modify detection rules
delete evidence
bypass authorization
disable guardrails
```

---

## 66. Threat Correlation

The detection engine MUST correlate events using:

```text
tenant_id
actor_id
session_id
device_id
source_ip
service_id
resource_id
request_id
trace_id
correlation_id
AI agent ID
integration ID
workflow ID
```

---

## 67. Attack Chain Detection

The platform SHOULD detect multi-stage attack chains.

Example:

```text
Credential Attack
       |
       v
Account Compromise
       |
       v
Privilege Escalation
       |
       v
Sensitive Data Access
       |
       v
Large Export
       |
       v
External Transfer
```

This MUST produce a higher-confidence threat than isolated events.

---

## 68. Threat Graph

SalesGenie SHOULD represent relationships as:

```text
Actor
 |
 +--> Session
 |
 +--> Device
 |
 +--> IP
 |
 +--> API
 |
 +--> Resource
 |
 +--> AI Agent
 |
 +--> Integration
 |
 +--> Workflow
 |
 +--> Data
```

This graph MAY be used for advanced threat detection.

---

## 69. Risk Scoring

Risk SHOULD consider:

```text
Threat Severity
Actor Privilege
Resource Sensitivity
Tenant Context
Historical Behavior
Frequency
Velocity
Confidence
Threat Intelligence
AI Agent Risk
Integration Risk
Data Classification
Attack Chain
Detection Confidence
```

---

## 70. Risk Score Example

```text
Base Risk
   +
Privilege Risk
   +
Data Sensitivity
   +
Behavioral Anomaly
   +
Threat Intelligence
   +
Attack-Chain Evidence
   =
Final Risk Score
```

---

## 71. Detection Confidence

Every detection SHOULD include:

```text
confidence_score
confidence_level
supporting_signals
contradicting_signals
```

Example:

```yaml
confidence_score: 0.94
confidence_level: HIGH
```

---

## 72. False Positive Management

Security administrators MUST be able to mark threats as:

```text
TRUE_POSITIVE
FALSE_POSITIVE
BENIGN
DUPLICATE
INCONCLUSIVE
```

Detection models SHOULD learn from approved feedback where appropriate.

---

## 73. Alert Generation

The threat detection engine MUST generate alerts when risk exceeds configured thresholds.

Example:

```text
Risk >= 90
      |
      v
CRITICAL ALERT
```

---

## 74. Alert Deduplication

Repeated signals belonging to the same attack MUST be grouped where appropriate.

Example:

```text
10,000 failed requests
        |
        v
1 correlated threat
```

instead of 10,000 independent alerts.

---

## 75. Threat Suppression

Authorized users MAY suppress known benign patterns.

Suppression MUST include:

```yaml
suppression_id:
reason:
created_by:
created_at:
expires_at:
scope:
conditions:
```

Critical detections SHOULD not be suppressible without elevated authorization.

---

## 76. Threat Escalation

Threat severity SHOULD increase when:

```text
attack persists
affected resources increase
additional attack stages appear
privileged account is involved
sensitive data is affected
multiple tenants are affected
AI agent is involved
critical infrastructure is affected
```

---

## 77. Threat Investigation

Investigators MUST be able to:

```text
view threat
view evidence
view event timeline
view actor
view sessions
view devices
view IPs
view API calls
view AI actions
view integration actions
view workflows
view affected resources
view related threats
```

---

## 78. Threat Timeline

The platform MUST construct an investigation timeline.

Example:

```text
10:01  Failed login
10:02  Successful login
10:03  New device
10:04  Role changed
10:05  Sensitive API access
10:06  AI agent session
10:07  Mass export
10:08  Threat detected
10:09  Session revoked
```

---

## 79. AI-Assisted Threat Investigation

AI MAY:

```text
summarize attack
correlate events
identify attack chain
identify affected resources
estimate confidence
suggest root cause
recommend containment
recommend additional investigation
```

---

## 80. AI Investigation Grounding

AI analysis MUST reference original evidence.

Example:

```yaml
finding:
  "Potential account takeover"

evidence:
  - event_id: EVT-001
  - event_id: EVT-002
  - event_id: EVT-003
```

AI MUST NOT modify source events.

---

## 81. AI Hallucination Controls

AI threat-analysis output MUST distinguish:

```text
OBSERVED
INFERRED
SUSPECTED
RECOMMENDED
CONFIRMED
```

---

## 82. Human Approval

The following SHOULD require human approval unless explicitly covered by an approved automated policy:

```text
account suspension
organization suspension
mass session revocation
integration disablement
credential rotation
large-scale IP blocking
workflow termination
AI permission reduction
```

---

## 83. Automated Threat Response

The platform MAY automatically perform:

```text
session revocation
temporary account lock
OAuth token revocation
workflow pause
integration isolation
temporary rate limiting
IP blocking
AI tool restriction
```

only when authorized by policy.

---

## 84. Automated Response Safety

Before automated response:

```text
Threat
+
Confidence
+
Risk
+
Policy
+
Target
+
Action
+
Impact
```

MUST be evaluated.

---

## 85. Response Rollback

Where technically possible:

```text
Threat
  |
  v
Automated Containment
  |
  v
Human Review
  |
  +--> Confirmed Threat
  |       |
  |       v
  |    Permanent Remediation
  |
  +--> False Positive
          |
          v
      Rollback
```

---

## 86. Threat Playbooks

The system SHOULD support predefined playbooks.

Example:

```yaml
playbook: ACCOUNT_TAKEOVER

trigger:
  threat_type: ACCOUNT_TAKEOVER
  confidence: HIGH

actions:
  - revoke_sessions
  - require_mfa
  - notify_security
  - create_incident
  - request_human_review
```

---

## 87. AI Playbook Recommendation

AI MAY recommend a playbook based on:

```text
threat_type
risk_score
confidence
attack_stage
affected_resources
historical incidents
```

AI MUST NOT bypass playbook authorization.

---

## 88. Threat Intelligence

The platform MAY integrate trusted threat intelligence for:

```text
malicious IPs
malicious domains
known attack indicators
compromised credentials
known bot infrastructure
```

Threat intelligence MUST be validated before automated blocking.

---

## 89. Detection Rule Governance

Every rule MUST support:

```text
rule_id
version
owner
status
severity
conditions
actions
created_at
updated_at
approved_by
```

---

## 90. Rule Lifecycle

Rules MUST support:

```text
DRAFT
TESTING
APPROVED
ACTIVE
DISABLED
DEPRECATED
ROLLED_BACK
```

---

## 91. Detection Rule Testing

The platform SHOULD support:

```text
unit testing
historical replay
simulation
staging validation
false-positive analysis
performance testing
attack replay
```

---

## 92. Threat Detection Metrics

The system MUST measure:

```text
true positives
false positives
false negatives where measurable
detection latency
alert latency
investigation time
containment time
resolution time
rule effectiveness
detection coverage
```

---

## 93. Core Security Metrics

The platform SHOULD expose:

```text
MTTD
MTTA
MTTC
MTTR
False Positive Rate
Threat Detection Rate
Critical Threat Count
High Threat Count
Threat Recurrence
Detection Coverage
Telemetry Coverage
```

---

## 94. Threat Detection Health

The system MUST monitor itself.

Required metrics:

```text
events_received
events_processed
events_dropped
events_delayed
events_failed
queue_depth
rule_engine_latency
AI_detection_latency
correlation_latency
alert_latency
```

---

## 95. Detection Blind-Spot Detection

The system MUST detect when expected telemetry stops.

Example:

```text
Auth Service
    |
    v
Expected events every minute
    |
    X
No events for 15 minutes
    |
    v
TELEMETRY BLIND-SPOT THREAT
```

---

## 96. Threat Detection Availability

Recommended target:

```text
Threat Detection Control Plane >= 99.99%
```

Critical telemetry SHOULD use durable processing.

---

## 97. Event Durability

Critical security events MUST NOT be silently dropped.

The system SHOULD support:

```text
durable queues
retries
dead-letter queues
idempotent processing
event replay
```

---

## 98. Event Ordering

Where attack-chain analysis depends on ordering, the platform SHOULD preserve event ordering using:

```text
timestamp
sequence number
trace ID
correlation ID
```

---

## 99. Duplicate Event Handling

The system MUST safely handle duplicate telemetry.

Duplicate events MUST NOT create uncontrolled alert storms.

---

## 100. Late Event Handling

The system MUST support delayed events without corrupting existing threat timelines.

---

## 101. Tenant Isolation

Threat detection queries MUST enforce tenant boundaries.

Example:

```text
Tenant A investigator
       |
       X
Tenant B threat evidence
```

---

## 102. Super Admin Monitoring

Super administrators MAY access cross-tenant security data only under appropriate privileged-access controls.

All such access MUST be monitored.

---

## 103. Threat Data Privacy

Threat telemetry MUST NOT unnecessarily contain:

```text
passwords
access tokens
refresh tokens
private keys
payment credentials
full sensitive payloads
```

---

## 104. Secret Redaction

The system MUST redact detected secrets from threat events.

Examples:

```text
API keys
JWTs
OAuth tokens
database credentials
webhook secrets
private keys
```

---

## 105. PII Minimization

Where PII is required for detection:

* collect only necessary fields
* mask unnecessary identifiers
* restrict access
* encrypt storage
* enforce retention

---

## 106. Threat Evidence Integrity

Threat evidence SHOULD support:

```text
immutable event storage
event hashing
tamper detection
sequence validation
signed evidence where required
```

---

## 107. Evidence Preservation

Evidence associated with active incidents MUST be protected from normal retention deletion.

---

## 108. Threat Export

Authorized investigators MAY export threat evidence.

Exports MUST:

```text
be authorized
be audited
be encrypted
be traceable
respect tenant isolation
respect data-retention policy
```

---

## 109. Threat Notification

Threat notifications MAY use:

```text
In-App
Email
Slack
Microsoft Teams
Webhook
SMS
Incident Management Platform
```

---

## 110. Critical Threat Notification

Critical threats SHOULD use redundant notification paths.

```text
CRITICAL THREAT
      |
      +--> In-App
      +--> Email
      +--> Security Channel
      +--> Incident System
```

---

## 111. Threat Dashboard

The SalesGenie Security Command Center SHOULD provide:

```text
Threat Posture
Critical Threats
High Threats
Open Incidents
Attack Chains
Authentication Threats
API Threats
AI Threats
Integration Threats
Data Threats
Network Threats
Insider Threat Indicators
Threat Detection Health
Telemetry Health
```

---

## 112. Threat Investigation Dashboard

Investigators SHOULD see:

```text
Threat Summary
Risk Score
Confidence
Attack Type
Attack Timeline
Affected Users
Affected AI Agents
Affected Services
Affected Integrations
Affected Resources
Evidence
Related Threats
Recommended Actions
Response History
```

---

## 113. AI Threat Dashboard

The platform SHOULD provide:

```text
AI Threats
Agent Risk
Tool Abuse
Prompt Injection
RAG Poisoning
AI Data Access
AI Privilege Violations
AI Policy Violations
Autonomous Actions
Human Approvals
```

---

## 114. Threat Analytics

The platform SHOULD provide:

```text
Threat Trends
Threat Categories
Threat Sources
Attack Chains
Top Threat Actors
Top Targeted Resources
AI Threat Trends
Integration Threat Trends
Detection Accuracy
False Positive Trends
```

---

## 115. Threat Hunting

Authorized security personnel SHOULD be able to perform proactive threat hunting.

Search dimensions:

```text
actor
tenant
IP
device
session
service
AI agent
integration
workflow
resource
event
threat
timestamp
risk
```

---

## 116. Threat Hunting Query

Example:

```text
tenant_id = "tenant_123"
AND risk_score >= 70
AND timestamp >= last_24_hours
AND (
    actor_type = "AI_AGENT"
    OR actor_role = "ADMIN"
)
AND event_type IN (
    "data.export",
    "ai.tool.invoked",
    "permission.changed"
)
```

---

## 117. Threat Hunting AI

AI MAY help security analysts:

```text
construct queries
identify suspicious patterns
correlate entities
summarize findings
suggest additional searches
```

AI-generated queries MUST be reviewed according to access-control policy before execution when necessary.

---

## 118. Threat Detection Feedback Loop

The platform SHOULD support:

```text
Threat
 |
 v
Investigation
 |
 v
Classification
 |
 v
Analyst Feedback
 |
 v
Rule / Model Improvement
 |
 v
Validation
 |
 v
Production Detection
```

---

## 119. Model Governance

AI/ML threat-detection models MUST support:

```text
model version
training version
feature version
evaluation metrics
approval status
deployment status
rollback version
```

---

## 120. Model Drift Detection

The system SHOULD monitor:

```text
feature drift
behavior drift
false-positive drift
detection-rate drift
data-quality drift
```

---

## 121. AI Detection Explainability

AI-generated threat detections SHOULD expose:

```text
primary signals
supporting signals
behavior deviation
risk factors
confidence
```

---

## 122. AI Detection Safety

AI MUST NOT:

* fabricate evidence
* modify telemetry
* delete threats
* suppress threats without authorization
* bypass RBAC
* access unrelated tenants
* disable detection
* alter audit records
* execute unauthorized containment

---

## 123. Security Monitoring of AI Security Agents

Security agents themselves MUST be monitored for:

```text
unexpected tool use
unexpected data access
excessive queries
privilege escalation
policy bypass
cross-tenant access
configuration modification
```

---

## 124. Recursive AI Security

The platform MUST treat AI security agents as potentially compromised actors.

```text
AI Security Agent
       |
       v
Security APIs
       |
       v
Behavior Monitoring
       |
       v
Independent Detection Layer
```

AI MUST NOT be the sole authority for validating its own security behavior.

---

## 125. Independent Detection Layer

Critical AI security controls SHOULD have non-AI enforcement.

Example:

```text
AI Agent
   |
   v
Policy Enforcement Point
   |
   v
Authorization
   |
   v
Action
```

---

## 126. Security Invariants

## SI-001

Every threat MUST have an identifiable source or detection basis.

## SI-002

Every critical threat MUST have supporting evidence.

## SI-003

Threat evidence MUST remain tenant-isolated.

## SI-004

AI-generated findings MUST remain distinguishable from source telemetry.

## SI-005

AI agents MUST NOT modify source evidence.

## SI-006

Critical security controls MUST not depend exclusively on AI detection.

## SI-007

High-impact automated responses MUST require explicit policy authorization.

## SI-008

Secrets MUST never appear unredacted in threat telemetry.

## SI-009

Cross-tenant access attempts MUST be detectable.

## SI-010

Threat detection failures MUST themselves be detectable.

## SI-011

Detection rules MUST be versioned.

## SI-012

Detection models MUST be versioned.

## SI-013

Privileged threat investigations MUST be audited.

## SI-014

Threat suppression MUST be auditable.

## SI-015

Security evidence associated with active incidents MUST be preserved.

---

## 127. Threat Detection Testing

## Unit Tests

MUST cover:

```text
event normalization
rule evaluation
threshold detection
risk scoring
confidence scoring
correlation
tenant filtering
secret redaction
alert generation
deduplication
```

## Integration Tests

MUST cover:

```text
authentication
authorization
API gateway
AI gateway
agent orchestrator
RAG
workflow engine
billing
integrations
database
object storage
event bus
notification systems
```

## Security Tests

MUST simulate:

```text
brute force
credential stuffing
password spraying
account takeover
session hijacking
token replay
privilege escalation
cross-tenant access
IDOR
API enumeration
data exfiltration
OAuth abuse
webhook replay
prompt injection
AI tool abuse
RAG poisoning
workflow abuse
secret exposure
network intrusion
```

---

## 128. Adversarial AI Testing

The platform MUST test AI systems against:

```text
prompt injection
indirect prompt injection
jailbreak attempts
system prompt extraction
tool manipulation
tool chaining
privilege escalation
data exfiltration
malicious RAG documents
malicious customer messages
malicious emails
malicious CRM content
```

---

## 129. Red-Team Requirements

Red-team exercises SHOULD attempt to:

```text
bypass detection
evade behavioral baselines
hide attack chains
poison telemetry
forge events
disable monitoring
suppress alerts
bypass tenant isolation
abuse AI agents
abuse integrations
bypass rate limits
steal sessions
replay tokens
escalate privileges
exfiltrate data
disable security controls
```

---

## 130. Detection Coverage Matrix

SalesGenie SHOULD maintain:

| Threat               | Telemetry    | Detection              | Alert    | Response       | Evidence |
| -------------------- | ------------ | ---------------------- | -------- | -------------- | -------- |
| Account takeover     | Auth/Session | Rule + Behavioral      | Yes      | Session revoke | Yes      |
| Brute force          | Auth         | Threshold              | Yes      | Rate limit     | Yes      |
| Credential stuffing  | Auth/IP      | Correlation            | Yes      | Block/limit    | Yes      |
| Privilege escalation | RBAC         | Rule                   | Yes      | Revoke         | Yes      |
| Cross-tenant access  | API/AuthZ    | Policy                 | Critical | Block          | Yes      |
| Data exfiltration    | API/Data     | Behavioral             | Critical | Contain        | Yes      |
| AI tool abuse        | AI telemetry | Behavioral             | High     | Restrict tool  | Yes      |
| Prompt injection     | AI/RAG       | AI + Rules             | High     | Block action   | Yes      |
| OAuth abuse          | Integration  | Behavioral             | High     | Revoke token   | Yes      |
| Workflow abuse       | Workflow     | Behavioral             | High     | Pause workflow | Yes      |
| Network intrusion    | Network      | Signature + Behavioral | High     | Block          | Yes      |
| Security tampering   | Audit        | Rule                   | Critical | Lockdown       | Yes      |

---

## 131. Detection Quality Requirements

The platform SHOULD optimize for:

```text
High Recall
+
High Precision
+
Low Detection Latency
+
Low Alert Fatigue
+
Explainability
+
Operational Reliability
```

No single metric should be optimized at the expense of overall security effectiveness.

---

## 132. Threat Detection SLOs

Recommended targets:

| Metric                            |       Target |
| --------------------------------- | -----------: |
| Detection platform availability   |    >= 99.99% |
| Critical threat detection latency | < 60 seconds |
| High threat detection latency     |  < 2 minutes |
| Critical alert delivery           | < 60 seconds |
| Threat-query p95                  |     < 500 ms |
| Threat-query p99                  |  < 2 seconds |
| Critical event loss               |    Near-zero |
| Telemetry blind-spot detection    |  < 5 minutes |

Targets MUST be validated through production-like load testing.

---

## 133. Threat Detection Scalability

The platform MUST support the SalesGenie target architecture:

```text
10M+ users
500K+ concurrent conversations
Millions of daily security events
Large-scale AI tool calls
Large-scale workflow execution
High-volume API activity
Large-scale integration traffic
```

Detection services MUST scale horizontally.

---

## 134. Threat Detection Failure Modes

The platform MUST safely handle:

```text
event bus failure
telemetry source outage
rule engine outage
AI detector outage
database outage
notification outage
network partition
event duplication
event delay
high-volume event spikes
malformed events
storage exhaustion
```

Security controls MUST fail safely.

---

## 135. Degraded Detection Mode

If AI detection becomes unavailable:

```text
AI Detection
     X
     |
     v
Rule-Based Detection
     |
     v
Signature Detection
     |
     v
Policy Enforcement
```

Core security enforcement MUST remain operational.

---

## 136. Threat Detection Golden Path

```text
Activity
   |
   v
Telemetry
   |
   v
Normalize
   |
   v
Validate
   |
   v
Enrich
   |
   v
Correlate
   |
   +-------------------+
   |                   |
   v                   v
Rules              AI Detection
   |                   |
   +---------+---------+
             |
             v
       Risk Evaluation
             |
             v
       Threat Created
             |
             v
          Alert
             |
             v
       Investigation
             |
       +-----+------+
       |            |
       v            v
     Human         AI
   Analysis      Analysis
       |            |
       +-----+------+
             |
             v
        Response
             |
             v
        Verification
             |
             v
       Evidence Store
             |
             v
      Detection Feedback
```

---

## 137. Attack Chain Example

```text
1. Credential Stuffing
        |
        v
2. Successful Login
        |
        v
3. New Device
        |
        v
4. Session Created
        |
        v
5. Privilege Escalation
        |
        v
6. AI Agent Access
        |
        v
7. Sensitive RAG Retrieval
        |
        v
8. CRM Data Extraction
        |
        v
9. External API Call
        |
        v
10. Data Exfiltration
        |
        v
11. Critical Threat
        |
        v
12. Automated Containment
        |
        v
13. Human Investigation
```

The correlation engine SHOULD identify the sequence as a single attack chain when evidence supports the relationship.

---

## 138. Human + AI Threat Detection Operating Model

```text
                    SECURITY TELEMETRY
                           |
                           v
                 +---------------------+
                 | Deterministic Rules |
                 +----------+----------+
                            |
                            v
                 +---------------------+
                 | Behavioral Models   |
                 +----------+----------+
                            |
                            v
                 +---------------------+
                 | AI Threat Analysis  |
                 +----------+----------+
                            |
                            v
                 +---------------------+
                 | Correlation Engine  |
                 +----------+----------+
                            |
                            v
                 +---------------------+
                 | Risk + Confidence   |
                 +----------+----------+
                            |
                +-----------+-----------+
                |                       |
                v                       v
        Automated Policy         Human Analyst
                |                       |
                +-----------+-----------+
                            |
                            v
                    Security Response
```

---

## 139. Final Acceptance Criteria

## AC-001 — Authentication Threats

The system MUST detect:

* brute force
* credential stuffing
* password spraying
* suspicious login behavior
* session anomalies
* token replay
* MFA abuse

## AC-002 — Authorization Threats

The system MUST detect:

* privilege escalation
* unauthorized role changes
* RBAC abuse
* cross-tenant access
* IDOR-like patterns

## AC-003 — API Threats

The system MUST detect:

* API enumeration
* scraping
* rate-limit abuse
* abnormal request velocity
* unauthorized API access

## AC-004 — AI Threats

The system MUST detect or support detection of:

* prompt injection
* indirect prompt injection
* jailbreak attempts
* tool abuse
* unauthorized data access
* privilege escalation
* excessive tool usage
* AI-driven data exfiltration
* malicious RAG content

## AC-005 — Integration Threats

The system MUST monitor:

* OAuth authorization
* scope changes
* token activity
* webhook activity
* abnormal external API usage

## AC-006 — Data Threats

The system MUST detect:

* mass data access
* unusual exports
* sensitive-data access anomalies
* potential exfiltration

## AC-007 — Infrastructure Threats

The system SHOULD detect:

* network anomalies
* service compromise
* container anomalies
* database abuse
* storage abuse

## AC-008 — Detection Quality

The system MUST support:

* rule-based detection
* behavioral detection
* event correlation
* risk scoring
* confidence scoring
* false-positive classification

## AC-009 — Investigation

Investigators MUST be able to:

* inspect evidence
* reconstruct timelines
* correlate attack chains
* inspect affected resources
* use AI-assisted analysis

## AC-010 — Response

The platform MUST support:

* human response
* controlled automated response
* AI recommendations
* containment
* rollback where possible
* complete response auditing

## AC-011 — Security of AI

AI MUST NOT:

* bypass authorization
* access unauthorized tenants
* modify evidence
* disable detection
* suppress threats without authorization
* execute unauthorized destructive actions

## AC-012 — Reliability

The detection platform MUST:

* detect telemetry outages
* prevent silent loss of critical events
* support event replay
* handle duplicates
* handle delayed events
* operate in degraded mode

---

## 140. FAANG-Level Non-Functional Requirements

| Category         | Requirement                                    |
| ---------------- | ---------------------------------------------- |
| Detection        | Multi-layer threat detection                   |
| AI Security      | Dedicated AI-agent and tool monitoring         |
| Accuracy         | High precision and high recall                 |
| Latency          | Near-real-time critical threat detection       |
| Scalability      | Millions of events across distributed services |
| Availability     | >= 99.99% target for detection control plane   |
| Reliability      | Durable security telemetry                     |
| Tenant Isolation | Strict tenant-level isolation                  |
| Privacy          | Data minimization and secret redaction         |
| Explainability   | Evidence-backed detections                     |
| AI Governance    | Human oversight for high-impact actions        |
| Automation       | Policy-controlled automated containment        |
| Forensics        | Attack-chain reconstruction                    |
| Integrity        | Tamper-resistant evidence                      |
| Observability    | Detection-pipeline self-monitoring             |
| Extensibility    | Versioned detection rules and event schemas    |
| Resilience       | Safe degraded operation                        |
| Governance       | Rule/model approval and rollback               |
| Compliance       | Retention and evidence preservation            |
| Security         | Defense in depth                               |

---

## 141. Ultimate Threat Detection Requirement

SalesGenie MUST evolve from simple event monitoring into an **intelligent, distributed threat-detection control plane** capable of understanding:

```text
WHO
 |
 +--> Human
 +--> AI Agent
 +--> Service
 +--> Integration
 +--> Workflow

WHAT
 |
 +--> Login
 +--> API Request
 +--> Data Access
 +--> AI Action
 +--> Tool Call
 +--> Workflow
 +--> Integration
 +--> Configuration

WHERE
 |
 +--> Tenant
 +--> Service
 +--> Resource
 +--> Network
 +--> External System

WHEN
 |
 +--> Timestamp
 +--> Sequence
 +--> Velocity
 +--> Historical Baseline

WHY
 |
 +--> Normal Behavior
 +--> Policy
 +--> Workflow
 +--> Threat Indicator

RISK
 |
 +--> Severity
 +--> Confidence
 +--> Impact
 +--> Attack Chain

WHAT NEXT
 |
 +--> Observe
 +--> Alert
 +--> Investigate
 +--> Contain
 +--> Remediate
 +--> Verify
```

The complete threat-detection lifecycle MUST be:

```text
OBSERVE
   |
   v
COLLECT
   |
   v
NORMALIZE
   |
   v
ENRICH
   |
   v
DETECT
   |
   v
CORRELATE
   |
   v
SCORE
   |
   v
CLASSIFY
   |
   v
ALERT
   |
   v
INVESTIGATE
   |
   v
DECIDE
   |
   v
CONTAIN
   |
   v
REMEDIATE
   |
   v
VERIFY
   |
   v
PRESERVE
   |
   v
LEARN
   |
   v
IMPROVE
```

SalesGenie MUST provide this threat-detection capability across:

```text
HUMANS
+
AI AGENTS
+
AI MODELS
+
AI TOOLS
+
RAG
+
WORKFLOWS
+
APIs
+
MICROSERVICES
+
IDENTITIES
+
SESSIONS
+
INTEGRATIONS
+
DATA
+
DATABASES
+
OBJECT STORAGE
+
NETWORKS
+
CONTAINERS
+
INFRASTRUCTURE
+
SECRETS
+
KEYS
+
BILLING
+
SECURITY CONTROLS
```

> **Core requirement:** Every significant attack signal must be observable, every meaningful threat must be detectable, every detection must be explainable through evidence, every high-risk attack must be actionable, every AI security decision must be governed, and every containment action must remain authorized, auditable, reversible where possible, and tenant-safe.
