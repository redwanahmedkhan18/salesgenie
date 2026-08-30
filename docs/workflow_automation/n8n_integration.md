# SalesGenie — FAANG-Level n8n Integration Requirements

## User Requirements, System Requirements & Functional Requirements

### AI + Human Workflow Automation, n8n Integration, Orchestration, Governance, Security & Enterprise Operations

---

## 1. Document Purpose

This document defines enterprise-grade requirements for integrating **n8n** with the SalesGenie Workflow Automation Platform.

The integration SHALL enable SalesGenie to use n8n as an external workflow automation and integration execution layer while retaining SalesGenie's:

- Multi-tenant architecture
- Workflow orchestration
- AI agent capabilities
- Human-in-the-loop execution
- RBAC
- Security controls
- Workflow versioning
- Scheduling
- Conditions
- Actions
- Monitoring
- Error handling
- Audit logging
- Cost management
- Governance
- Observability

The integration SHALL support both:

```text
AI-Initiated Automation
Human-Initiated Automation
Scheduled Automation
Event-Driven Automation
Webhook-Driven Automation
Workflow-to-Workflow Automation
External-System Automation
```

---

## 2. Integration Philosophy

SalesGenie SHALL treat n8n as an **automation execution and integration capability**, not as the authoritative source of:

* Identity
* Tenant ownership
* Authorization
* Billing
* Workflow governance
* Audit policy
* AI safety policy
* Business ownership
* SalesGenie workflow state

SalesGenie SHALL remain the system of record for platform-level workflow governance.

```text
                    SALESGENIE
                        │
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
   AI Agents       Human Users      External Events
        │               │                │
        └───────────────┼────────────────┘
                        ↓
                Workflow Orchestrator
                        │
                Policy / RBAC / Guardrails
                        │
                        ↓
                  n8n Integration
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
       n8n Cloud    n8n Self-Host   n8n Webhooks
          │             │             │
          └─────────────┼─────────────┘
                        ↓
             External Applications
```

---

## 3. Scope

The integration SHALL support:

```text
n8n Workflow Discovery
n8n Workflow Registration
n8n Workflow Execution
n8n Workflow Activation
n8n Workflow Deactivation
n8n Webhooks
n8n Credentials
n8n Node/Action Mapping
Execution Tracking
Execution Status Synchronization
Error Synchronization
Retry Coordination
Workflow Version Mapping
AI Workflow Invocation
Human Workflow Invocation
Event-Driven Invocation
Scheduled Invocation
Bidirectional Data Exchange
Observability
Audit Logging
Security
Rate Limiting
Quota Management
Tenant Isolation
```

---

## 4. Actors

## 4.1 Human Actors

### ACTOR-HUMAN-001 — End User

Initiates customer-facing automation where permitted.

### ACTOR-HUMAN-002 — Sales Agent

Uses n8n-powered automation for lead, CRM, communication, and sales processes.

### ACTOR-HUMAN-003 — Support Agent

Uses automation for customer support workflows.

### ACTOR-HUMAN-004 — Workflow Designer

Creates and configures SalesGenie workflows that invoke n8n.

### ACTOR-HUMAN-005 — Organization Administrator

Configures organization-level n8n integrations.

### ACTOR-HUMAN-006 — Integration Administrator

Manages n8n connections, credentials, mappings, and health.

### ACTOR-HUMAN-007 — Platform Administrator

Manages platform-wide n8n integration policies.

### ACTOR-HUMAN-008 — SRE / DevOps Engineer

Monitors infrastructure, availability, performance, and failures.

### ACTOR-HUMAN-009 — Security Administrator

Manages n8n security policies and incidents.

---

## 4.2 AI Actors

### ACTOR-AI-001 — AI Workflow Planner

Generates workflow plans that may use n8n capabilities.

### ACTOR-AI-002 — AI Workflow Builder

Generates or modifies workflow configurations subject to policy.

### ACTOR-AI-003 — AI Integration Agent

Selects appropriate n8n integrations and nodes.

### ACTOR-AI-004 — AI Execution Agent

Initiates permitted n8n executions.

### ACTOR-AI-005 — AI Error Recovery Agent

Analyzes n8n failures and recommends recovery.

### ACTOR-AI-006 — AI Optimization Agent

Identifies workflow performance and cost improvements.

### ACTOR-AI-007 — AI Governance Agent

Detects unsafe or unauthorized n8n operations.

---

## 5. Core User Requirements

## 5.1 n8n Connection

### UR-N8N-001

Administrators SHALL be able to connect SalesGenie to an authorized n8n instance.

### UR-N8N-002

The platform SHALL support configurable n8n instances per organization where permitted.

### UR-N8N-003

Users SHALL be able to view n8n connection health.

### UR-N8N-004

Users SHALL be able to disconnect an n8n integration.

### UR-N8N-005

Only authorized users SHALL manage n8n connections.

---

## 5.2 n8n Instance Management

Users SHALL be able to configure:

```text
Instance Name
Instance URL
Connection Type
Authentication Method
Environment
Organization
Status
Health Check
Default Execution Policy
Rate Limits
Timeouts
```

---

## 5.3 Workflow Discovery

Authorized users SHALL be able to view available n8n workflows.

Information SHOULD include:

```text
Workflow ID
Workflow Name
Description
Status
Active/Inactive
Version
Last Updated
Owner
Trigger Type
Execution Count
Last Execution
Health
```

---

## 5.4 Workflow Registration

Users SHALL be able to register an n8n workflow as a SalesGenie automation.

Example:

```text
n8n Workflow
      ↓
Register
      ↓
SalesGenie Workflow Catalog
      ↓
Available to Authorized Users / AI
```

---

## 5.5 Workflow Invocation

Users SHALL be able to invoke registered n8n workflows from SalesGenie.

---

## 5.6 Manual Execution

Authorized users SHALL be able to execute an n8n workflow manually.

---

## 5.7 AI Execution

Authorized AI agents SHALL be able to invoke n8n workflows through controlled tools.

---

## 5.8 Scheduled Execution

SalesGenie SHALL be able to invoke n8n workflows according to SalesGenie schedules.

---

## 5.9 Event-Driven Execution

SalesGenie SHALL be able to invoke n8n workflows based on events.

Examples:

```text
New Lead
New Customer
Ticket Created
Email Received
Payment Completed
Deal Updated
Customer Replied
Workflow Completed
Workflow Failed
```

---

## 5.10 Webhook Execution

SalesGenie SHALL support triggering n8n workflows through configured webhooks.

---

## 5.11 Workflow Results

Users SHALL be able to inspect execution results.

---

## 5.12 Execution History

Users SHALL be able to view:

```text
Execution ID
Workflow ID
Start Time
End Time
Duration
Status
Trigger
Initiator
Input
Output
Error
Retry Count
```

Sensitive data SHALL be redacted.

---

## 6. System Requirements

## 6.1 Integration Gateway

SalesGenie SHALL provide a dedicated n8n Integration Gateway.

```text
Client
  ↓
SalesGenie API
  ↓
Authorization
  ↓
Policy Engine
  ↓
n8n Integration Gateway
  ↓
n8n Instance
```

---

## 6.2 Separation of Responsibilities

The architecture SHALL separate:

```text
SalesGenie
    │
    ├── Identity
    ├── RBAC
    ├── Tenant Management
    ├── Workflow Governance
    ├── AI Governance
    ├── Audit
    ├── Billing
    ├── Monitoring
    └── Policy
            │
            ↓
           n8n
            │
            ├── Node Execution
            ├── Integrations
            ├── External APIs
            ├── Data Transformations
            └── Automation Runtime
```

---

## 6.3 Multi-Tenant Architecture

The integration SHALL support tenant isolation.

Each execution SHALL be associated with:

```text
Tenant ID
Organization ID
User ID
Workflow ID
n8n Instance ID
n8n Workflow ID
Execution ID
```

---

## 6.4 Tenant Isolation

Tenant A SHALL NOT:

```text
View Tenant B Workflows
Execute Tenant B Workflows
View Tenant B Credentials
View Tenant B Executions
View Tenant B Logs
Access Tenant B Webhooks
```

---

## 7. Functional Requirements — Connection Management

### FR-CONN-001

The system SHALL support registering an n8n instance.

### FR-CONN-002

The system SHALL validate n8n connectivity.

### FR-CONN-003

The system SHALL perform health checks.

### FR-CONN-004

The system SHALL track connection state.

### FR-CONN-005

The system SHALL support connection rotation.

### FR-CONN-006

The system SHALL support connection revocation.

### FR-CONN-007

The system SHALL prevent unauthorized connection usage.

---

## 8. Connection States

```text
PENDING
CONNECTING
CONNECTED
DEGRADED
UNAVAILABLE
AUTH_FAILED
DISABLED
REVOKED
```

---

## 9. n8n Connection Configuration

```yaml
n8n_connection:
  instance_id:
  organization_id:

  base_url:

  authentication:
    type:
    credential_reference:

  environment:
    type: development

  timeout_ms:
  rate_limit:

  enabled:
```

Secrets SHALL be stored using a secure secret-management mechanism.

---

## 10. Functional Requirements — Workflow Discovery

### FR-DISCOVERY-001

The system SHALL retrieve registered n8n workflows.

### FR-DISCOVERY-002

The system SHALL synchronize workflow metadata.

### FR-DISCOVERY-003

The system SHALL detect workflow activation state.

### FR-DISCOVERY-004

The system SHALL detect changes to registered workflows.

### FR-DISCOVERY-005

The system SHALL maintain SalesGenie-to-n8n workflow mappings.

---

## 11. Workflow Mapping

```yaml
workflow_mapping:
  salesgenie_workflow_id:
  salesgenie_version_id:

  n8n_instance_id:
  n8n_workflow_id:

  mapping_status:
  created_at:
  updated_at:
```

---

## 12. Workflow Registration

The registration process SHALL validate:

```text
Workflow Exists
Workflow Accessible
Tenant Ownership
Trigger Compatibility
Input Schema
Output Schema
Required Credentials
Required Permissions
Security Policy
Execution Limits
```

---

## 13. Workflow Capability Discovery

SalesGenie SHOULD determine which n8n workflows are capable of:

```text
Create Lead
Update CRM
Send Email
Send Message
Create Ticket
Update Ticket
Search Customer
Enrich Company
Generate Report
Sync Data
Transform Data
Call API
Process Webhook
```

---

## 14. n8n Node Capability Catalog

SalesGenie SHOULD maintain a normalized representation of available n8n capabilities.

Example:

```yaml
capability:
  id: crm.create_contact
  provider: n8n
  node_type:
  operation:
  input_schema:
  output_schema:
  risk_level:
  required_permissions:
```

---

## 15. AI Tool Registry

n8n capabilities exposed to AI SHALL be registered as controlled tools.

Example:

```text
AI Agent
   ↓
Tool Registry
   ↓
n8n CRM Tool
   ↓
Policy Validation
   ↓
Execution
```

---

## 16. AI n8n Tool Requirements

### FR-AI-N8N-001

AI SHALL only access explicitly permitted n8n tools.

### FR-AI-N8N-002

AI SHALL NOT directly access arbitrary n8n endpoints.

### FR-AI-N8N-003

AI tool calls SHALL be validated before execution.

### FR-AI-N8N-004

AI tool calls SHALL enforce tenant boundaries.

### FR-AI-N8N-005

AI tool calls SHALL be auditable.

---

## 17. AI Workflow Planning

AI MAY generate an automation plan.

Example:

```text
Customer submits contact form
        ↓
Validate lead
        ↓
Create CRM contact
        ↓
Enrich company
        ↓
Score lead
        ↓
Notify sales agent
        ↓
Create follow-up task
```

The AI plan SHALL be validated before execution.

---

## 18. AI Workflow Generation

AI MAY generate n8n workflow configurations subject to:

```text
Allowed Node Types
Allowed Credentials
Allowed Integrations
Allowed Operations
Data Policies
Security Policies
Tenant Policies
Risk Policies
Human Approval Policies
```

---

## 19. AI-Generated Workflow Lifecycle

```text
AI Request
    ↓
Plan
    ↓
Generate
    ↓
Schema Validation
    ↓
Security Validation
    ↓
Policy Validation
    ↓
Risk Assessment
    ↓
Human Approval?
    ↓
Deploy / Execute
    ↓
Monitor
```

---

## 20. AI Workflow Modification

AI MAY recommend workflow modifications.

High-risk modifications SHALL require human approval.

---

## 21. High-Risk n8n Operations

Examples:

```text
Delete Records
Delete Files
Delete Workflows
Modify Credentials
Send Bulk Messages
Send Bulk Email
Financial Operations
Change Access Controls
Export Sensitive Data
Execute Arbitrary Code
Modify Production Automation
```

These SHALL require explicit authorization.

---

## 22. n8n Code Execution

If n8n workflows contain code execution capabilities:

```text
Code Node
Execute Command
Custom Script
Arbitrary HTTP Request
```

SalesGenie SHALL classify these as elevated-risk capabilities.

---

## 23. Code Execution Policy

The platform SHALL support policies such as:

```yaml
code_execution:
  allowed: false
  environments:
    - development
  approval_required: true
```

---

## 24. Human-Initiated Workflow

```text
Human User
    ↓
Select Automation
    ↓
Provide Input
    ↓
Validate Input
    ↓
Authorization
    ↓
Policy Check
    ↓
Execute n8n
    ↓
Monitor
    ↓
Return Result
```

---

## 25. AI-Initiated Workflow

```text
AI Agent
    ↓
Tool Selection
    ↓
Input Generation
    ↓
Schema Validation
    ↓
Authorization
    ↓
Risk Assessment
    ↓
Policy Check
    ↓
Human Approval?
    ↓
Execute n8n
    ↓
Verify Result
    ↓
Continue AI Workflow
```

---

## 26. Human + AI Collaboration

Example:

```text
AI:
"Lead score is 91. I recommend creating a Salesforce opportunity."

        ↓

Policy:
CRM mutation allowed.

        ↓

Risk:
MEDIUM.

        ↓

Human:
Approve.

        ↓

n8n:
Create opportunity.

        ↓

SalesGenie:
Verify result.

        ↓

AI:
Continue workflow.
```

---

## 27. Input Schema Validation

Before execution, SalesGenie SHALL validate n8n inputs.

```yaml
input:
  email:
    type: string
    format: email

  company:
    type: string

  lead_score:
    type: number
```

Invalid input SHALL prevent execution.

---

## 28. Output Schema Validation

n8n outputs SHALL be validated before being consumed by SalesGenie.

```text
n8n Output
    ↓
Schema Validation
    ↓
Business Validation
    ↓
Security Filtering
    ↓
SalesGenie Workflow
```

---

## 29. Data Transformation

SalesGenie SHALL support mapping between:

```text
SalesGenie Schema
        ↕
n8n Schema
        ↕
External Provider Schema
```

---

## 30. Data Mapping Example

```yaml
mapping:
  lead.email: contact.email
  lead.name: contact.full_name
  lead.company: company.name
  lead.phone: contact.phone
```

---

## 31. Sensitive Data Handling

The system SHALL classify and protect:

```text
PII
Credentials
Tokens
Financial Information
Customer Data
Internal Business Data
Authentication Data
```

---

## 32. Credential Requirements

SalesGenie SHALL NOT expose raw n8n credentials to:

```text
End Users
AI Agents
Frontend Clients
Logs
Audit Records
Error Messages
Workflow Inputs
```

---

## 33. Credential Reference Model

Workflows SHALL use credential references rather than raw secrets.

```yaml
credential:
  credential_id:
  provider:
  tenant_id:
  secret_reference:
```

---

## 34. Credential Scope

Credentials SHALL be scoped to the smallest practical boundary.

```text
Platform
Organization
Tenant
Workflow
Integration
Action
```

---

## 35. Credential Rotation

The system SHOULD support credential rotation without requiring workflow redesign.

---

## 36. Credential Failure

When credentials fail:

```text
Detect
 ↓
Classify
 ↓
Stop Unsafe Operations
 ↓
Notify Authorized Administrator
 ↓
Credential Refresh / Rotation
 ↓
Retry
```

---

## 37. Webhook Integration

SalesGenie SHALL support n8n webhook triggers.

---

## 38. Webhook Security

Webhook requests SHOULD support:

```text
Authentication
Signature Verification
Timestamp Validation
Replay Protection
IP Restrictions
Rate Limiting
Schema Validation
Tenant Validation
```

---

## 39. Webhook Event Schema

```yaml
webhook_event:
  event_id:
  tenant_id:
  source:
  event_type:
  timestamp:
  signature:
  payload:
```

---

## 40. Webhook Replay Protection

Webhook events SHALL support unique event identifiers and idempotency.

Duplicate webhook deliveries SHALL NOT create duplicate critical side effects.

---

## 41. Event-Driven n8n Execution

```text
SalesGenie Event Bus
       ↓
Event Router
       ↓
Policy Engine
       ↓
n8n Trigger
       ↓
n8n Workflow
       ↓
Execution Result
       ↓
SalesGenie Event
```

---

## 42. Event Filtering

Users SHALL be able to configure which events can trigger n8n workflows.

Example:

```yaml
trigger:
  event: lead.created
  filters:
    lead_score:
      operator: ">="
      value: 80
```

---

## 43. Schedule Integration

SalesGenie Scheduler SHALL be able to invoke n8n workflows.

```text
SalesGenie Scheduler
       ↓
Schedule Policy
       ↓
n8n Invocation
       ↓
Execution
```

---

## 44. Scheduler Ownership

SalesGenie SHALL remain the authoritative scheduler for SalesGenie-managed schedules.

n8n-native schedules MAY be supported when explicitly registered and governed.

---

## 45. Execution Tracking

Every n8n invocation SHALL generate a SalesGenie execution record.

```yaml
execution:
  salesgenie_execution_id:
  n8n_execution_id:

  tenant_id:
  workflow_id:
  workflow_version_id:

  started_at:
  completed_at:

  status:
  trigger_type:

  initiated_by:
    type:
    id:
```

---

## 46. Execution States

```text
QUEUED
STARTING
RUNNING
WAITING
SUCCESS
FAILED
CANCELLED
TIMED_OUT
RETRYING
PARTIALLY_COMPLETED
UNKNOWN
```

---

## 47. Execution Synchronization

SalesGenie SHALL synchronize n8n execution states.

Where real-time synchronization is unavailable, the system SHALL use controlled polling.

---

## 48. Execution Correlation

Every execution SHALL preserve:

```text
Correlation ID
Trace ID
SalesGenie Execution ID
n8n Execution ID
Workflow ID
Node ID
Tenant ID
```

---

## 49. Idempotency

Every externally triggered n8n execution SHOULD support an idempotency key.

```yaml
idempotency:
  key:
  scope:
  ttl:
```

---

## 50. Duplicate Execution Prevention

SalesGenie SHALL prevent accidental duplicate execution caused by:

```text
Webhook Retries
Network Retries
Worker Restarts
Scheduler Retries
User Double-Click
AI Repeated Tool Call
Message Redelivery
```

---

## 51. n8n Execution Cancellation

Where supported, authorized users SHALL be able to cancel running n8n executions.

---

## 52. Cancellation Policy

```text
IMMEDIATE
GRACEFUL
WAIT_FOR_CURRENT_NODE
COMPENSATE
```

---

## 53. n8n Error Handling

SalesGenie SHALL normalize n8n failures into its standard workflow error model.

Example:

```yaml
error:
  source: n8n
  n8n_workflow_id:
  n8n_execution_id:

  code:
  type:
  severity:

  retryable:
  recoverable:

  node:
  message:

  trace_id:
```

---

## 54. n8n Retry Coordination

SalesGenie SHALL prevent duplicate retry systems from creating retry storms.

The platform SHALL coordinate:

```text
SalesGenie Retry Policy
+
n8n Retry Policy
+
External Provider Retry Policy
```

---

## 55. Retry Ownership

Every integration SHALL explicitly define retry ownership.

Example:

```yaml
retry:
  owner: salesgenie
  n8n_retry_enabled: false
```

or:

```yaml
retry:
  owner: n8n
  salesgenie_retry_enabled: false
```

---

## 56. Retry Storm Prevention

The system SHALL prevent:

```text
SalesGenie Retry
    ↓
n8n Retry
    ↓
Provider Retry
    ↓
Provider Retry Again
```

from creating uncontrolled request amplification.

---

## 57. n8n Failure Recovery

The recovery flow SHALL support:

```text
Detect Failure
      ↓
Classify
      ↓
Retry?
      ↓
Fallback?
      ↓
Compensate?
      ↓
AI Diagnosis
      ↓
Human Approval?
      ↓
Recover
      ↓
Verify
```

---

## 58. AI Error Analysis

AI SHOULD analyze:

```text
n8n Execution
n8n Node
Input
Output
Error
Execution History
Provider Response
Retry History
Workflow Version
Dependency Health
```

---

## 59. AI Error Diagnosis Example

```text
n8n workflow failed.

Failed node:
Salesforce Update

Observed error:
HTTP 429

Historical behavior:
Salesforce rate limit exceeded.

AI diagnosis:
Transient dependency rate limit.

Confidence:
97%

Recommended action:
Wait according to Retry-After and retry once.
```

---

## 60. AI Recovery Guardrails

AI recovery SHALL respect:

```text
RBAC
Tenant Policy
Workflow Policy
Integration Policy
Risk Level
Retry Budget
Rate Limits
Credential Policy
Human Approval Policy
```

---

## 61. Autonomous AI Recovery

Low-risk failures MAY be automatically recovered.

Examples:

```text
Temporary timeout
HTTP 503
Transient connection failure
Temporary rate limit
```

---

## 62. Human Approval Recovery

Human approval SHALL be required for configured high-risk recovery.

Examples:

```text
Production workflow modification
Data deletion
Financial mutation
Credential replacement
Bulk communication
Rollback
```

---

## 63. n8n Workflow Version Mapping

SalesGenie SHALL maintain mapping between:

```text
SalesGenie Workflow Version
        ↕
n8n Workflow Version / Snapshot
```

---

## 64. Version Integrity

Production executions SHALL identify the exact n8n workflow configuration used.

---

## 65. Version Drift Detection

SalesGenie SHALL detect when a registered n8n workflow changes outside SalesGenie's governance process.

```text
Registered Workflow
       ↓
External Modification
       ↓
Drift Detected
       ↓
Policy
       ↓
Warn / Disable / Revalidate
```

---

## 66. Workflow Drift

The system SHOULD detect changes to:

```text
Nodes
Connections
Credentials
Triggers
Parameters
Code
HTTP Requests
Permissions
Environment
```

---

## 67. External Modification Policy

Organizations SHALL be able to configure:

```text
ALLOW
WARN
REQUIRE_REVIEW
BLOCK
```

---

## 68. Workflow Import

SalesGenie MAY allow importing an n8n workflow definition.

Import SHALL perform:

```text
Schema Validation
Security Scan
Credential Scan
Node Capability Scan
Code Scan
Data Flow Analysis
Policy Validation
```

---

## 69. Workflow Export

Authorized users MAY export SalesGenie-compatible workflow definitions.

Sensitive credentials SHALL never be exported as plaintext.

---

## 70. Workflow Templates

SalesGenie SHALL support n8n-based reusable templates.

Templates SHOULD contain:

```text
Template ID
Name
Description
Version
Trigger
Nodes
Inputs
Outputs
Required Integrations
Risk Level
Permissions
```

---

## 71. AI Template Selection

AI MAY select an approved n8n template based on user intent.

Example:

```text
User:
"When a high-value lead arrives, notify the sales team."

AI:
Select:
HIGH_VALUE_LEAD_ALERT_V3
```

AI SHALL only select approved templates.

---

## 72. Template Instantiation

Template instantiation SHALL validate:

```text
Tenant
Inputs
Credentials
Permissions
Environment
Risk
Data Policy
```

---

## 73. Human Approval for Template Deployment

Organizations MAY require human approval before activating AI-generated or AI-modified templates.

---

## 74. n8n Integration Marketplace

SalesGenie MAY expose approved n8n integration templates.

Categories:

```text
CRM
Email
Messaging
Support
Marketing
Productivity
Storage
Analytics
Finance
E-commerce
Developer Tools
AI
```

---

## 75. Integration Capability Registry

Each integration SHALL define:

```yaml
integration:
  provider:
  capability:
  operations:
  required_permissions:
  supported_regions:
  risk_level:
  rate_limits:
  data_classification:
```

---

## 76. External API Integration

n8n workflows MAY connect to external services.

SalesGenie SHALL track:

```text
Provider
Operation
Request
Response Status
Latency
Error
Cost
```

where technically available and policy-permitted.

---

## 77. Rate Limiting

SalesGenie SHALL enforce rate limits for n8n invocation.

Rate limits MAY exist at:

```text
Platform
Organization
Tenant
Workflow
User
AI Agent
Integration
Provider
```

---

## 78. Quota Management

Organizations MAY have:

```text
Execution Quota
Monthly Workflow Runs
Concurrent Executions
API Calls
AI Calls
Data Transfer
```

---

## 79. Quota Enforcement

When quota is exceeded:

```text
Reject
Queue
Defer
Notify
Upgrade
```

according to policy.

---

## 80. Cost Tracking

SalesGenie SHOULD estimate and track n8n-related operational costs.

Metrics MAY include:

```text
Execution Count
Execution Duration
External API Calls
AI Calls
Data Processing
Infrastructure Usage
```

---

## 81. Cost-Aware AI

AI MAY select between automation strategies based on:

```text
Cost
Latency
Reliability
Capability
Risk
```

Example:

```text
Strategy A:
5 n8n executions

Strategy B:
2 n8n executions

AI selects B
because required outcome is equivalent
and policy permits.
```

---

## 82. Performance Requirements

The integration SHOULD provide:

```text
Low Invocation Latency
Connection Pooling
Async Execution
Efficient Polling
Event-Based Status Updates
Backpressure
Request Batching
```

where applicable.

---

## 83. Async Execution

Long-running n8n workflows SHOULD execute asynchronously.

```text
Request
 ↓
Accepted
 ↓
Execution ID
 ↓
Background Execution
 ↓
Status Updates
 ↓
Completion Event
```

---

## 84. Synchronous Execution

Short-running workflows MAY support synchronous execution.

The platform SHALL enforce a maximum synchronous execution timeout.

---

## 85. Queue-Based Execution

SalesGenie SHOULD use a queue between workflow orchestration and n8n invocation when appropriate.

```text
Workflow Engine
      ↓
Execution Queue
      ↓
n8n Worker
      ↓
n8n
```

---

## 86. Backpressure

The system SHALL apply backpressure when n8n or external dependencies are overloaded.

---

## 87. Circuit Breaker

SalesGenie SHALL support circuit breakers for unavailable n8n instances.

```text
CLOSED
   ↓
Failure Threshold
   ↓
OPEN
   ↓
Recovery Interval
   ↓
HALF_OPEN
   ↓
Success
   ↓
CLOSED
```

---

## 88. n8n Health Monitoring

SalesGenie SHALL monitor:

```text
Connectivity
Latency
Availability
Execution Success Rate
Execution Failure Rate
Queue Depth
Error Rate
Authentication Status
API Health
```

---

## 89. Integration Health States

```text
HEALTHY
DEGRADED
UNAVAILABLE
AUTHENTICATION_FAILED
RATE_LIMITED
OVERLOADED
MISCONFIGURED
DISABLED
```

---

## 90. Observability

Every n8n execution SHOULD emit:

```text
Metrics
Logs
Traces
Events
Audit Records
```

---

## 91. Distributed Tracing

The platform SHOULD propagate tracing context across:

```text
SalesGenie
    ↓
Integration Gateway
    ↓
n8n
    ↓
External Provider
```

---

## 92. Monitoring Metrics

SalesGenie SHOULD expose:

```text
n8n Execution Rate
Success Rate
Failure Rate
P95 Latency
P99 Latency
Retry Rate
Timeout Rate
Webhook Rate
Queue Depth
Active Executions
Circuit Breaker State
```

---

## 93. AI Reliability Analytics

AI SHOULD identify:

```text
Repeated n8n Failures
Slow Workflows
Problematic Nodes
Provider Instability
Credential Expiration
Rate Limit Trends
Workflow Regressions
Cost Anomalies
```

---

## 94. Security Requirements

### SEC-N8N-001

All n8n communication SHALL use secure transport where applicable.

### SEC-N8N-002

Authentication credentials SHALL be protected.

### SEC-N8N-003

Authorization SHALL be enforced before every protected operation.

### SEC-N8N-004

Tenant isolation SHALL be enforced.

### SEC-N8N-005

Webhook signatures SHALL be validated where configured.

### SEC-N8N-006

Secrets SHALL be redacted from logs.

### SEC-N8N-007

Sensitive execution data SHALL be access controlled.

---

## 95. RBAC

n8n capabilities SHALL integrate with SalesGenie RBAC.

Example:

```text
SUPER_ADMIN
ORGANIZATION_ADMIN
WORKFLOW_ADMIN
WORKFLOW_EDITOR
SALES_MANAGER
SALES_AGENT
SUPPORT_AGENT
VIEWER
AI_AGENT
```

---

## 96. Permission Model

Example permissions:

```text
n8n.instance.view
n8n.instance.manage
n8n.workflow.view
n8n.workflow.create
n8n.workflow.edit
n8n.workflow.execute
n8n.workflow.activate
n8n.workflow.deactivate
n8n.workflow.delete
n8n.execution.view
n8n.execution.cancel
n8n.execution.retry
n8n.credentials.manage
n8n.webhook.manage
n8n.ai.execute
n8n.ai.modify
```

---

## 97. Least Privilege

AI agents and human users SHALL receive only the permissions required for their tasks.

---

## 98. AI Permission Boundary

AI SHALL NOT inherit unrestricted permissions from the human who initiated an interaction.

AI permissions SHALL be independently evaluated.

---

## 99. Impersonation Protection

An AI agent SHALL NOT impersonate an administrator merely because the initiating user has administrator privileges unless explicitly supported by policy.

---

## 100. Audit Requirements

The system SHALL audit:

```text
Connection Created
Connection Modified
Connection Deleted
Workflow Registered
Workflow Imported
Workflow Exported
Workflow Executed
Workflow Activated
Workflow Deactivated
Workflow Modified
Execution Retried
Execution Cancelled
Credential Changed
Permission Changed
AI Tool Call
AI Workflow Generation
AI Workflow Modification
Human Approval
Human Rejection
Policy Violation
Security Event
```

---

## 101. Audit Event Example

```yaml
audit_event:
  event_id:
  event_type: N8N_WORKFLOW_EXECUTED

  tenant_id:
  organization_id:

  salesgenie_workflow_id:
  salesgenie_version_id:

  n8n_instance_id:
  n8n_workflow_id:
  n8n_execution_id:

  actor:
    type:
    id:

  timestamp:
  trace_id:
  correlation_id:
```

---

## 102. AI Audit Example

```yaml
audit_event:
  event_type: AI_N8N_TOOL_CALL

  actor:
    type: AI_AGENT
    id:

  requested_tool:
    name:
    operation:

  policy_decision:
    result:
    reason:

  human_approval:
    required:
    approved_by:

  execution:
    n8n_workflow_id:
    n8n_execution_id:
```

---

## 103. Data Governance

SalesGenie SHALL support policies for:

```text
Data Residency
Data Classification
Retention
Encryption
Access
Export
Deletion
Masking
Logging
```

---

## 104. Data Minimization

Only data required by the n8n workflow SHALL be sent to n8n.

---

## 105. Output Filtering

n8n outputs SHALL be filtered before being exposed to:

```text
Frontend
AI Agent
Human User
Audit System
External System
```

---

## 106. Prompt Injection Protection

If n8n processes external or customer-generated content:

```text
Email
Web Pages
Documents
CRM Notes
Support Tickets
Messages
Forms
```

SalesGenie SHALL treat the content as untrusted input.

AI agents SHALL NOT follow arbitrary instructions contained within external data.

---

## 107. AI Tool Injection Protection

External data SHALL NOT be allowed to directly generate unrestricted n8n tool calls.

The execution pipeline SHALL be:

```text
External Data
      ↓
AI Reasoning
      ↓
Structured Tool Request
      ↓
Schema Validation
      ↓
Policy Validation
      ↓
Permission Validation
      ↓
Risk Assessment
      ↓
Execution
```

---

## 108. Arbitrary URL Protection

If n8n supports arbitrary HTTP requests, SalesGenie SHOULD enforce:

```text
Domain Allowlist
IP Restrictions
Private Network Protection
Protocol Restrictions
Port Restrictions
```

to reduce SSRF and data-exfiltration risk.

---

## 109. Webhook Abuse Protection

Webhook endpoints SHALL support:

```text
Rate Limiting
Authentication
Signature Validation
Replay Protection
Payload Limits
Schema Validation
Abuse Detection
```

---

## 110. Workflow Import Security

Imported workflows SHALL undergo static analysis where possible.

Checks SHOULD include:

```text
Dangerous Nodes
Code Execution
External URLs
Credential References
Sensitive Data Flow
Unexpected Webhooks
Unapproved Integrations
Excessive Permissions
```

---

## 111. Workflow Activation Policy

A workflow SHALL NOT become production-active unless required validation succeeds.

```text
Draft
 ↓
Validate
 ↓
Security Scan
 ↓
Policy Check
 ↓
Approval
 ↓
Activate
```

---

## 112. Production Deployment

Production n8n workflows SHOULD support:

```text
Draft
Testing
Staging
Canary
Production
Disabled
Archived
```

---

## 113. Canary Execution

New n8n workflow versions MAY be exposed to a limited percentage of executions.

```text
Version A → 95%
Version B → 5%
```

The platform SHALL compare:

```text
Success Rate
Latency
Errors
Cost
Business Outcome
```

---

## 114. Automatic Rollback

Configured regressions MAY trigger automatic rollback.

---

## 115. Disaster Recovery

SalesGenie SHALL maintain sufficient metadata to recover n8n integration configuration.

Critical records SHOULD include:

```text
Workflow Mapping
Version Mapping
Execution Metadata
Credential References
Policy Configuration
Webhook Configuration
Integration State
```

---

## 116. n8n Instance Failure

When an n8n instance becomes unavailable:

```text
Detect
 ↓
Circuit Breaker
 ↓
Queue New Requests
 ↓
Fallback Instance?
 ↓
Retry
 ↓
Escalate
```

---

## 117. Multi-Instance Failover

Organizations MAY configure:

```text
Primary n8n Instance
Secondary n8n Instance
Disaster Recovery Instance
```

Failover SHALL be policy controlled.

---

## 118. n8n Cloud + Self-Hosted

The architecture SHOULD support both:

```text
n8n Cloud
Self-Hosted n8n
Private n8n Deployment
```

subject to supported integration capabilities.

---

## 119. Environment Separation

The platform SHOULD support:

```text
Development n8n
Staging n8n
Production n8n
```

---

## 120. Environment Promotion

Workflow promotion SHOULD follow:

```text
Development
   ↓
Validation
   ↓
Staging
   ↓
Testing
   ↓
Approval
   ↓
Production
```

---

## 121. Configuration Promotion

Promotion SHALL avoid copying production secrets into lower environments.

---

## 122. Test Mode

SalesGenie SHALL support testing n8n integrations without triggering unintended production side effects.

---

## 123. Dry Run

Where supported, workflows SHOULD support dry-run or simulated execution.

---

## 124. Test Data Isolation

Test executions SHALL be clearly identified.

```yaml
execution:
  environment: staging
  mode: test
```

---

## 125. Functional Requirements — API Gateway

The integration gateway SHOULD provide operations conceptually equivalent to:

```text
POST   /integrations/n8n
GET    /integrations/n8n
GET    /integrations/n8n/{instance_id}
DELETE /integrations/n8n/{instance_id}

GET    /integrations/n8n/{instance_id}/workflows
POST   /integrations/n8n/{instance_id}/workflows/register

GET    /integrations/n8n/workflows/{workflow_id}
POST   /integrations/n8n/workflows/{workflow_id}/execute
POST   /integrations/n8n/workflows/{workflow_id}/activate
POST   /integrations/n8n/workflows/{workflow_id}/deactivate

GET    /integrations/n8n/executions/{execution_id}
POST   /integrations/n8n/executions/{execution_id}/retry
POST   /integrations/n8n/executions/{execution_id}/cancel

POST   /integrations/n8n/webhooks
GET    /integrations/n8n/health
```

Actual endpoint design SHALL follow SalesGenie's existing API conventions.

---

## 126. Execute Request

Example:

```json
{
  "workflow_id": "n8n_workflow_123",
  "input": {
    "lead_id": "lead_456",
    "priority": "high"
  },
  "execution_mode": "async",
  "idempotency_key": "exec-lead-456-v1"
}
```

---

## 127. Execute Response

Example:

```json
{
  "salesgenie_execution_id": "sg_exec_123",
  "n8n_execution_id": "n8n_exec_456",
  "status": "QUEUED",
  "workflow_id": "n8n_workflow_123"
}
```

---

## 128. Webhook Response

Webhook handlers SHOULD acknowledge accepted events quickly and process long-running work asynchronously.

```text
Webhook
  ↓
Validate
  ↓
Persist Event
  ↓
Return Accepted
  ↓
Process Asynchronously
```

---

## 129. Event Delivery Guarantees

The system SHOULD support:

```text
At-Least-Once Delivery
Idempotent Consumers
Duplicate Detection
Dead-Letter Handling
Retry
Backoff
```

Exactly-once semantics SHALL only be claimed where technically guaranteed.

---

## 130. n8n Execution Event

```yaml
event:
  type: n8n.execution.completed

  execution_id:
  workflow_id:

  status: success

  started_at:
  completed_at:

  duration_ms:
```

---

## 131. Error Event

```yaml
event:
  type: n8n.execution.failed

  execution_id:
  workflow_id:

  error:
    type:
    code:
    message:
    retryable:

  node:
    id:
    name:
```

---

## 132. Human Approval Event

```yaml
event:
  type: n8n.execution.approval_required

  execution_id:

  action:
  risk_level:

  requested_by:
    type:
    id:

  approval:
    required_roles:
      - WORKFLOW_ADMIN
```

---

## 133. Human Approval UX

The approval interface SHOULD display:

```text
Workflow
Version
n8n Instance
Requested Operation
Input Summary
Expected Side Effects
Risk Level
AI Recommendation
AI Confidence
Affected Systems
Rollback Strategy
```

---

## 134. Human Decision

Users SHALL be able to:

```text
Approve
Reject
Request Changes
Pause
Escalate
```

---

## 135. Approval Expiration

Approvals SHOULD expire after a configurable period.

Expired approvals SHALL not automatically execute the operation.

---

## 136. AI Confidence Thresholds

Organizations MAY define:

```yaml
ai_policy:
  autonomous_execution:
    minimum_confidence: 0.95

  human_approval:
    below_confidence: 0.95
```

Confidence SHALL never replace authorization.

---

## 137. AI + n8n Optimization

AI SHOULD recommend:

```text
Node Reduction
Execution Batching
Caching
Parallelization
Retry Optimization
Provider Selection
Workflow Simplification
Cost Reduction
Latency Reduction
```

---

## 138. Workflow Optimization Example

```text
Current:

CRM Lookup
 ↓
CRM Lookup
 ↓
CRM Lookup

AI Recommendation:

Cache Customer
 ↓
Reuse Result
 ↓
Reduce API Calls by 66%
```

---

## 139. AI Anomaly Detection

AI SHOULD detect:

```text
Execution Spikes
Unexpected Workflow Growth
Abnormal Latency
Unexpected External Calls
Unexpected Cost
Repeated Errors
Unusual Data Volume
```

---

## 140. Business Outcome Verification

For critical workflows, successful n8n execution SHALL NOT necessarily imply successful business outcome.

Example:

```text
n8n:
HTTP 200

SalesGenie:
CRM record not actually created.

Result:
BUSINESS_FAILURE
```

SalesGenie SHALL support post-execution verification.

---

## 141. Side-Effect Verification

Critical operations SHOULD verify:

```text
CRM Record Exists
Email Delivered / Accepted
Ticket Created
Payment State Updated
Lead Created
Message Accepted
```

where technically possible.

---

## 142. Compensation

If an n8n workflow partially succeeds:

```text
Node A ✓
Node B ✓
Node C ✗
```

SalesGenie SHALL support configured compensation or manual recovery.

---

## 143. Partial Execution State

```text
PARTIALLY_COMPLETED
```

SHALL preserve execution details.

---

## 144. Dead-Letter Integration

Failed n8n events MAY be routed to SalesGenie's dead-letter infrastructure.

```text
n8n Failure
    ↓
Retry Exhausted
    ↓
Dead-Letter Queue
    ↓
AI Analysis
    ↓
Human Review
    ↓
Replay
```

---

## 145. Replay

Authorized users SHALL be able to replay eligible n8n executions.

Replay modes:

```text
FULL
FROM_NODE
FROM_CHECKPOINT
DRY_RUN
```

---

## 146. Replay Safety

Replay SHALL evaluate:

```text
Idempotency
Side Effects
Credentials
Workflow Version
External State
Tenant
Authorization
```

---

## 147. Auditability of Replay

Every replay SHALL record:

```text
Original Execution
New Execution
Initiator
Reason
Version
Input Source
Approval
Result
```

---

## 148. Rate Limit Handling

When n8n or an external provider reports rate limiting:

```text
Detect
 ↓
Read Retry Metadata
 ↓
Apply Backoff
 ↓
Retry Within Budget
 ↓
Fallback / Queue
```

---

## 149. Timeout Handling

n8n calls SHALL have configurable timeouts.

Timeouts SHALL produce structured errors.

---

## 150. Integration Error Taxonomy

```text
N8N_CONNECTION_ERROR
N8N_AUTHENTICATION_ERROR
N8N_AUTHORIZATION_ERROR
N8N_TIMEOUT
N8N_RATE_LIMIT
N8N_WORKFLOW_NOT_FOUND
N8N_WORKFLOW_INACTIVE
N8N_EXECUTION_FAILED
N8N_EXECUTION_CANCELLED
N8N_WEBHOOK_FAILURE
N8N_SCHEMA_ERROR
N8N_CREDENTIAL_ERROR
N8N_NODE_ERROR
N8N_DEPENDENCY_ERROR
N8N_INSTANCE_UNAVAILABLE
N8N_CONFIGURATION_ERROR
N8N_SECURITY_VIOLATION
N8N_POLICY_VIOLATION
```

---

## 151. Error Handling Strategy

```text
Transient
   ↓
Retry

Rate Limited
   ↓
Backoff

n8n Unavailable
   ↓
Circuit Breaker

Credential Failure
   ↓
Admin Intervention

Policy Violation
   ↓
Block

High-Risk Failure
   ↓
Human Escalation

Permanent Failure
   ↓
Dead-Letter / Incident
```

---

## 152. Monitoring Dashboard

SalesGenie SHOULD provide:

```text
┌───────────────────────────────────────────────┐
│ n8n INTEGRATION CONTROL CENTER                │
├───────────────────────────────────────────────┤
│ Instances           4                         │
│ Healthy             3                         │
│ Degraded            1                         │
│ Active Executions   127                       │
│ Success Rate        98.7%                     │
│ Error Rate          1.3%                      │
│ Avg Latency         1.8s                      │
├───────────────────────────────────────────────┤
│ TOP WORKFLOWS                                  │
│ Lead Enrichment                                │
│ CRM Synchronization                            │
│ Customer Notification                          │
├───────────────────────────────────────────────┤
│ ACTIVE INCIDENTS                               │
│ CRM Rate Limit                                 │
│ Webhook Authentication                         │
└───────────────────────────────────────────────┘
```

---

## 153. Workflow Detail Dashboard

The dashboard SHOULD expose:

```text
Overview
Configuration
Inputs
Outputs
Executions
Errors
Logs
Metrics
Traces
Versions
Dependencies
Credentials
Permissions
AI Analysis
Audit
```

---

## 154. Integration Health Dashboard

Administrators SHALL be able to see:

```text
Instance Health
Authentication
Latency
Execution Success
Execution Failure
Queue State
API Availability
Rate Limits
Credential Expiration
```

---

## 155. SLO Requirements

Organizations SHOULD define n8n integration SLOs.

Example:

```yaml
slo:
  availability: 99.9%
  execution_success_rate: 99.5%
  webhook_acceptance: 99.9%
  p95_invocation_latency_ms: 1000
```

---

## 156. SLA Management

Critical automation MAY define:

```text
Detection SLA
Execution SLA
Recovery SLA
Human Approval SLA
Incident Resolution SLA
```

---

## 157. Capacity Management

SalesGenie SHOULD monitor:

```text
Concurrent Executions
Queue Depth
Worker Utilization
CPU
Memory
Execution Duration
External API Limits
```

where available.

---

## 158. Backpressure Strategy

```text
Capacity Normal
      ↓
Normal Execution

Capacity High
      ↓
Queue New Requests

Capacity Critical
      ↓
Throttle

Capacity Exhausted
      ↓
Reject / Defer
```

---

## 159. Bulkhead Isolation

The platform SHOULD isolate resource consumption by:

```text
Tenant
Organization
Workflow
Integration
AI Agent
Priority
Environment
```

---

## 160. Priority Queues

Executions MAY be prioritized:

```text
CRITICAL
HIGH
NORMAL
LOW
BACKGROUND
```

---

## 161. AI Priority Selection

AI MAY recommend execution priority, but the final priority SHALL be constrained by policy.

---

## 162. Security Monitoring

SalesGenie SHOULD detect:

```text
Unusual n8n Calls
Credential Abuse
Webhook Abuse
Unexpected External Domains
Large Data Transfers
Repeated Authorization Failures
Unauthorized Workflow Modification
Unexpected Code Execution
```

---

## 163. Security Incident

Suspicious n8n behavior SHALL be capable of generating a security incident.

---

## 164. Integration Disablement

Authorized administrators SHALL be able to disable an n8n integration immediately.

```text
Security Incident
      ↓
Disable Integration
      ↓
Stop New Executions
      ↓
Preserve Existing State
      ↓
Investigate
```

---

## 165. Emergency Kill Switch

SalesGenie SHOULD provide a platform-level emergency control to stop n8n executions.

The control SHALL be:

```text
RBAC Protected
Audited
Highly Visible
Fail-Safe
```

---

## 166. Tenant Kill Switch

Organizations SHOULD be able to disable n8n automation for their tenant without affecting other tenants.

---

## 167. Workflow Kill Switch

Administrators SHALL be able to immediately disable an individual automation.

---

## 168. AI Kill Switch

Organizations SHOULD be able to disable AI-initiated n8n execution independently from human execution.

```text
AI Execution:
DISABLED

Human Execution:
ENABLED
```

---

## 169. Human-Only Mode

The platform SHOULD support:

```yaml
execution_policy:
  ai_execution: false
  human_execution: true
```

---

## 170. AI-Only Automation

Where appropriate, organizations MAY allow:

```yaml
execution_policy:
  ai_execution: true
  human_execution: true
  approval_required: false
```

subject to risk policy.

---

## 171. Human-Approval Mode

```yaml
execution_policy:
  ai_execution: true
  approval_required: true
  risk_level: high
```

---

## 172. Workflow Governance

Every n8n workflow registered with SalesGenie SHALL have:

```text
Owner
Tenant
Environment
Risk Classification
Permission Policy
Execution Policy
Data Policy
Version
Approval Status
```

---

## 173. Risk Classification

```text
LOW
MEDIUM
HIGH
CRITICAL
```

Example:

```text
Send Internal Notification → LOW

Create CRM Lead → MEDIUM

Send Bulk Customer Email → HIGH

Financial Mutation → CRITICAL
```

---

## 174. Risk-Based Execution

```text
LOW
 ↓
Automatic

MEDIUM
 ↓
Policy Controlled

HIGH
 ↓
Human Approval

CRITICAL
 ↓
Explicit Authorization + Human Approval
```

---

## 175. AI Risk Assessment

AI SHOULD estimate risk based on:

```text
Operation
Data
External Systems
Side Effects
Scale
Reversibility
Financial Impact
Customer Impact
Security Impact
```

AI risk estimates SHALL not override platform policy.

---

## 176. Workflow Ownership

Each registered n8n workflow SHALL have an accountable owner.

The owner MAY be:

```text
User
Team
Organization
System
```

---

## 177. Ownership Transfer

Authorized administrators SHALL be able to transfer ownership.

---

## 178. Orphan Workflow Detection

SalesGenie SHOULD detect workflows whose owners are:

```text
Deleted
Disabled
Deactivated
No Longer Authorized
```

and apply policy.

---

## 179. Orphan Workflow Policy

Possible actions:

```text
Reassign
Disable
Escalate
Archive
```

---

## 180. Integration Lifecycle

```text
DISCOVER
   ↓
REGISTER
   ↓
VALIDATE
   ↓
APPROVE
   ↓
ACTIVATE
   ↓
MONITOR
   ↓
OPTIMIZE
   ↓
SUSPEND
   ↓
ARCHIVE
   ↓
REMOVE
```

---

## 181. n8n Workflow Lifecycle

```text
DISCOVERED
REGISTERED
DRAFT
VALIDATING
APPROVAL_PENDING
APPROVED
ACTIVE
DEGRADED
DISABLED
ARCHIVED
```

---

## 182. Functional Requirements — Lifecycle

### FR-LIFE-001

The system SHALL support workflow registration.

### FR-LIFE-002

The system SHALL support workflow validation.

### FR-LIFE-003

The system SHALL support activation.

### FR-LIFE-004

The system SHALL support deactivation.

### FR-LIFE-005

The system SHALL support archival.

### FR-LIFE-006

The system SHALL detect external workflow changes.

### FR-LIFE-007

The system SHALL enforce lifecycle permissions.

---

## 183. API Reliability

The integration gateway SHALL support:

```text
Timeouts
Retries
Circuit Breakers
Connection Pooling
Request Validation
Response Validation
Rate Limiting
Tracing
Logging
```

---

## 184. API Compatibility

The integration SHALL isolate SalesGenie from direct dependency on unstable n8n API details where practical.

A dedicated adapter layer SHOULD be used.

```text
SalesGenie
    ↓
n8n Adapter
    ↓
n8n API
```

---

## 185. Adapter Architecture

```text
N8NIntegrationService
        │
        ├── WorkflowAdapter
        ├── ExecutionAdapter
        ├── WebhookAdapter
        ├── CredentialAdapter
        ├── HealthAdapter
        └── EventAdapter
```

---

## 186. Provider Abstraction

The architecture SHOULD allow future automation providers.

```text
AutomationGateway
       │
       ├── n8n
       ├── Internal Workflow Engine
       ├── Other Automation Provider
       └── Custom Enterprise Connector
```

n8n-specific functionality SHALL remain encapsulated.

---

## 187. Functional Requirements — Provider Abstraction

### FR-PROVIDER-001

The platform SHALL define a normalized automation execution contract.

### FR-PROVIDER-002

n8n SHALL implement the contract through an adapter.

### FR-PROVIDER-003

Provider-specific failures SHALL be normalized.

### FR-PROVIDER-004

Provider-specific capabilities SHALL be discoverable.

---

## 188. Normalized Execution Contract

```yaml
automation_execution:
  execution_id:
  provider:
  workflow_id:

  tenant_id:

  status:

  input:
  output:

  started_at:
  completed_at:

  error:

  metadata:
```

---

## 189. AI Provider Selection

If multiple automation providers are available, AI MAY recommend a provider based on:

```text
Capability
Cost
Latency
Reliability
Policy
Availability
```

The platform SHALL make the final policy decision.

---

## 190. Human Override

Authorized users SHALL be able to override AI provider recommendations.

---

## 191. Integration Documentation

Registered n8n workflows SHOULD include:

```text
Description
Purpose
Owner
Input Schema
Output Schema
Side Effects
Dependencies
Required Credentials
Risk
SLA
Error Policy
```

---

## 192. Workflow Documentation Generation

AI MAY generate documentation for registered n8n workflows.

Generated documentation SHALL be clearly identified as AI-generated unless verified.

---

## 193. AI Workflow Explanation

Users SHALL be able to ask:

```text
"What does this n8n workflow do?"
```

AI SHOULD explain:

```text
Trigger
Nodes
Data Flow
External Systems
Side Effects
Potential Failures
Permissions
Risk
```

---

## 194. AI Data-Flow Analysis

AI SHOULD identify:

```text
Input
Transformations
External Destinations
Sensitive Data
Outputs
Side Effects
```

---

## 195. AI Security Analysis

AI SHOULD flag:

```text
Untrusted HTTP Requests
Sensitive Data Exposure
Broad Credentials
Unexpected External Domains
Code Execution
Weak Webhook Security
Missing Validation
```

---

## 196. AI Optimization Loop

```text
Execute
 ↓
Monitor
 ↓
Analyze
 ↓
Identify Bottleneck
 ↓
Recommend Change
 ↓
Human Approval
 ↓
Deploy New Version
 ↓
Canary
 ↓
Measure
 ↓
Promote / Rollback
```

---

## 197. Business Continuity

SalesGenie SHALL preserve workflow intent if n8n becomes temporarily unavailable.

Possible strategies:

```text
Queue
Retry
Fallback
Alternative Provider
Manual Task
Human Escalation
```

---

## 198. Manual Fallback

If automation is unavailable:

```text
Automation Failure
      ↓
Create Human Task
      ↓
Assign Agent
      ↓
Complete Manually
      ↓
Record Outcome
```

---

## 199. Human Fallback Example

```text
CRM Automation Unavailable

SalesGenie:
"CRM synchronization could not be completed automatically."

Fallback:
Create task for Sales Operations.

Task:
Create CRM contact manually.

SLA:
15 minutes.
```

---

## 200. AI + Human Fallback

```text
n8n Failure
    ↓
AI Diagnosis
    ↓
Can Recover Automatically?
    │
 ┌──┴──┐
YES    NO
 │      │
 ↓      ↓
Recover Human Task
 │      │
 └──┬───┘
    ↓
Verify
    ↓
Complete
```

---

## 201. Functional Requirements — Human Task Integration

### FR-HUMAN-001

The system SHALL create human tasks when configured automation fails.

### FR-HUMAN-002

Human tasks SHALL contain failure context.

### FR-HUMAN-003

Human tasks SHALL respect RBAC.

### FR-HUMAN-004

Human tasks SHALL have configurable SLAs.

### FR-HUMAN-005

Human completion SHALL update workflow state.

---

## 202. Human Task Context

A task SHOULD contain:

```text
Workflow
Execution
n8n Workflow
Failed Node
Error
Customer
Required Action
AI Recommendation
SLA
Priority
```

---

## 203. Completion Verification

Manual completion SHALL be recorded and, where possible, verified.

---

## 204. Enterprise Audit Requirements

The platform SHALL maintain immutable or tamper-evident records for critical operations where required.

---

## 205. Compliance Readiness

The integration architecture SHOULD support enterprise controls for:

```text
SOC 2
ISO 27001
GDPR
Data Retention
Access Reviews
Audit Trails
Security Monitoring
```

Actual compliance SHALL depend on implementation and organizational controls.

---

## 206. Reliability Invariants

```text
INVARIANT-001:
Every n8n execution SHALL belong to exactly one authorized tenant context.

INVARIANT-002:
Every execution SHALL have a SalesGenie correlation identifier.

INVARIANT-003:
Every production execution SHALL identify the workflow version.

INVARIANT-004:
AI SHALL never bypass SalesGenie authorization.

INVARIANT-005:
AI SHALL never receive unrestricted n8n access.

INVARIANT-006:
Raw credentials SHALL never be exposed to AI.

INVARIANT-007:
Raw credentials SHALL never be exposed to frontend clients.

INVARIANT-008:
Secrets SHALL never appear in logs.

INVARIANT-009:
Critical operations SHALL be idempotent.

INVARIANT-010:
Retries SHALL be bounded.

INVARIANT-011:
Retry ownership SHALL be explicitly defined.

INVARIANT-012:
n8n failures SHALL be normalized into SalesGenie error handling.

INVARIANT-013:
Critical failures SHALL remain observable.

INVARIANT-014:
Tenant data SHALL remain isolated.

INVARIANT-015:
Unauthorized workflow execution SHALL fail closed.

INVARIANT-016:
High-risk operations SHALL require explicit authorization.

INVARIANT-017:
AI-generated workflows SHALL pass validation before execution.

INVARIANT-018:
AI-generated workflows SHALL not automatically gain production privileges.

INVARIANT-019:
External workflow modifications SHALL be detectable.

INVARIANT-020:
Workflow drift SHALL be policy controlled.

INVARIANT-021:
Webhook events SHALL support replay protection.

INVARIANT-022:
Duplicate webhook events SHALL not duplicate critical side effects.

INVARIANT-023:
Workflow replay SHALL not silently duplicate side effects.

INVARIANT-024:
Execution state SHALL survive worker failures.

INVARIANT-025:
n8n instance failures SHALL not create uncontrolled retry storms.

INVARIANT-026:
Critical automation SHALL support human fallback.

INVARIANT-027:
AI recovery SHALL be policy governed.

INVARIANT-028:
Human approvals SHALL be auditable.

INVARIANT-029:
AI tool calls SHALL be auditable.

INVARIANT-030:
Production workflow activation SHALL require required validation.

INVARIANT-031:
Production secrets SHALL never be copied into lower environments.

INVARIANT-032:
Emergency kill switches SHALL be RBAC protected.

INVARIANT-033:
Integration disablement SHALL stop unauthorized new executions.

INVARIANT-034:
Business success SHALL not be inferred solely from HTTP success.

INVARIANT-035:
Critical business outcomes SHOULD be independently verified.

INVARIANT-036:
n8n integration shall not become a single point of failure for SalesGenie.

INVARIANT-037:
The platform SHALL preserve sufficient execution metadata for debugging.

INVARIANT-038:
The platform SHALL distinguish human, AI, scheduled, and event-driven execution origins.

INVARIANT-039:
AI confidence SHALL never replace authorization.

INVARIANT-040:
Policy conflicts SHALL fail closed.

INVARIANT-041:
Sensitive output SHALL be filtered before AI or user exposure.

INVARIANT-042:
Imported workflows SHALL be security validated before activation.

INVARIANT-043:
Arbitrary external destinations SHALL be policy controlled.

INVARIANT-044:
Production workflow modifications SHALL be traceable to an authorized actor.

INVARIANT-045:
Integration health SHALL be continuously observable.

INVARIANT-046:
A failed automation SHALL never silently disappear.

INVARIANT-047:
A workflow SHALL not remain indefinitely stuck without detection.

INVARIANT-048:
The n8n integration subsystem SHALL monitor its own health.

INVARIANT-049:
Tenant-level failures SHALL not exhaust shared platform resources.

INVARIANT-050:
Emergency shutdown mechanisms SHALL themselves be tested.
```

---

## 207. End-to-End Human Automation Flow

```text
Human User
     ↓
SalesGenie Dashboard
     ↓
Select n8n Automation
     ↓
Input Data
     ↓
Input Validation
     ↓
RBAC
     ↓
Tenant Policy
     ↓
Risk Assessment
     ↓
Approval Required?
     │
 ┌───┴────┐
NO       YES
 │        │
 │     Human Approval
 │        │
 └───┬────┘
      ↓
Execution Queue
      ↓
n8n Adapter
      ↓
n8n Workflow
      ↓
External Integrations
      ↓
Execution Result
      ↓
Output Validation
      ↓
Business Verification
      ↓
SalesGenie Workflow
      ↓
Audit + Metrics + Trace
```

---

## 208. End-to-End AI Automation Flow

```text
User Intent
     ↓
AI Agent
     ↓
Intent Understanding
     ↓
Workflow Planning
     ↓
Capability Discovery
     ↓
n8n Tool Selection
     ↓
Input Generation
     ↓
Schema Validation
     ↓
Permission Validation
     ↓
Policy Validation
     ↓
Risk Assessment
     ↓
Human Approval?
     │
 ┌───┴────┐
YES      NO
 │        │
 ↓        ↓
Human    Policy
Review   Controlled
 │        │
 └───┬────┘
      ↓
Execute n8n
      ↓
Monitor
      ↓
Validate Output
      ↓
Verify Business Outcome
      ↓
AI Continues Reasoning
      ↓
Audit
```

---

## 209. Event-Driven Flow

```text
External Event
      ↓
Event Gateway
      ↓
Authentication
      ↓
Signature Verification
      ↓
Schema Validation
      ↓
Tenant Resolution
      ↓
Deduplication
      ↓
Event Router
      ↓
SalesGenie Policy
      ↓
n8n Workflow
      ↓
Execution
      ↓
Result
      ↓
Event Bus
      ↓
Downstream Workflow
```

---

## 210. AI-Generated n8n Workflow Flow

```text
User:
"Automatically qualify new enterprise leads."

        ↓

AI Planner

        ↓

Workflow Plan

        ↓

Capability Discovery

        ↓

Select Approved n8n Template

        ↓

Configure:
- Lead Trigger
- Enrichment
- Scoring
- CRM Update
- Sales Notification

        ↓

Schema Validation

        ↓

Security Analysis

        ↓

Policy Validation

        ↓

Risk Assessment

        ↓

Human Approval

        ↓

Create / Update n8n Workflow

        ↓

Test

        ↓

Staging

        ↓

Canary

        ↓

Production

        ↓

Continuous Monitoring
```

---

## 211. n8n Failure Recovery Flow

```text
n8n Execution
      ↓
Failure
      ↓
Normalize Error
      ↓
Classify
      ↓
Retryable?
 ┌────┴────┐
YES       NO
 │          │
 ↓          ↓
Retry    Recoverable?
 │        ┌──┴──┐
 │       YES   NO
 │        │      │
 ↓        ↓      ↓
Success Fallback Incident
 │        │      │
 └───┬────┘      ↓
     ↓        AI Diagnosis
 Verification    ↓
     │       Human Review
 ┌───┴───┐       ↓
YES     NO     Recovery
 │       │       ↓
 ↓       ↓   Verification
Done   Escalate   ↓
             ┌───┴───┐
             ↓       ↓
          Success   Failure
             │       │
             ↓       ↓
          Complete Incident
```

---

## 212. Enterprise n8n Control Plane

```text
                 SALESGENIE CONTROL PLANE
 ┌──────────────────────────────────────────────────┐
 │ Identity & RBAC                                  │
 │ Tenant Management                                │
 │ Workflow Governance                              │
 │ AI Governance                                    │
 │ Policy Engine                                    │
 │ Security                                         │
 │ Audit                                            │
 │ Billing / Quotas                                 │
 │ Monitoring                                       │
 │ Versioning                                       │
 └───────────────────────┬──────────────────────────┘
                         │
                         ↓
                N8N INTEGRATION GATEWAY
 ┌──────────────────────────────────────────────────┐
 │ Connection Manager                               │
 │ Workflow Adapter                                 │
 │ Execution Adapter                                │
 │ Webhook Adapter                                  │
 │ Credential Adapter                               │
 │ Event Adapter                                    │
 │ Health Monitor                                   │
 │ Retry Controller                                 │
 │ Circuit Breaker                                  │
 │ Rate Limiter                                     │
 └───────────────────────┬──────────────────────────┘
                         │
              ┌──────────┴──────────┐
              ↓                     ↓
         n8n Cloud             Self-Hosted n8n
              │                     │
              └──────────┬──────────┘
                         ↓
             External Applications
```

---

## 213. Recommended SalesGenie Integration Services

The implementation SHOULD logically separate the following services:

```text
n8n-integration-service
n8n-workflow-service
n8n-execution-service
n8n-webhook-service
n8n-credential-service
n8n-policy-service
n8n-monitoring-service
n8n-event-service
n8n-ai-gateway
n8n-audit-service
```

These MAY be implemented as separate microservices or modular components depending on deployment scale.

---

## 214. Recommended Event Types

```text
N8N_INSTANCE_CONNECTED
N8N_INSTANCE_DISCONNECTED

N8N_WORKFLOW_REGISTERED
N8N_WORKFLOW_UPDATED
N8N_WORKFLOW_ACTIVATED
N8N_WORKFLOW_DEACTIVATED
N8N_WORKFLOW_DRIFT_DETECTED

N8N_EXECUTION_QUEUED
N8N_EXECUTION_STARTED
N8N_EXECUTION_WAITING
N8N_EXECUTION_COMPLETED
N8N_EXECUTION_FAILED
N8N_EXECUTION_CANCELLED
N8N_EXECUTION_TIMED_OUT

N8N_RETRY_STARTED
N8N_RECOVERY_STARTED
N8N_RECOVERY_COMPLETED

N8N_WEBHOOK_RECEIVED
N8N_WEBHOOK_REJECTED

N8N_CREDENTIAL_UPDATED
N8N_CREDENTIAL_FAILED

N8N_AI_TOOL_CALLED
N8N_AI_APPROVAL_REQUIRED
N8N_AI_APPROVAL_GRANTED
N8N_AI_APPROVAL_REJECTED

N8N_POLICY_VIOLATION
N8N_SECURITY_INCIDENT

N8N_INSTANCE_DEGRADED
N8N_INSTANCE_RECOVERED
```

---

## 215. Recommended Database Entities

```text
N8NInstance
N8NWorkflow
N8NWorkflowVersion
N8NWorkflowMapping
N8NWorkflowCapability
N8NExecution
N8NExecutionAttempt
N8NExecutionNode
N8NWebhook
N8NCredentialReference
N8NIntegrationPolicy
N8NRetryPolicy
N8NApproval
N8NIncident
N8NHealthSnapshot
N8NEvent
N8NAuditEvent
N8NToolDefinition
N8NWorkflowTemplate
N8NWorkflowDependency
N8NExecutionArtifact
```

---

## 216. Recommended Execution Relationship

```text
Tenant
  │
  └── Organization
        │
        └── SalesGenie Workflow
              │
              └── Workflow Version
                    │
                    └── n8n Mapping
                          │
                          └── n8n Workflow
                                │
                                └── n8n Execution
                                      │
                                      ├── Attempts
                                      ├── Nodes
                                      ├── Errors
                                      ├── Artifacts
                                      └── Audit Events
```

---

## 217. Recommended Execution Metadata

Every execution SHOULD capture:

```text
salesgenie_execution_id
n8n_execution_id
tenant_id
organization_id
workflow_id
workflow_version_id
n8n_instance_id
n8n_workflow_id
trigger_type
initiator_type
initiator_id
ai_agent_id
human_approval_id
environment
priority
started_at
completed_at
duration
status
retry_count
error_id
trace_id
correlation_id
idempotency_key
```

---

## 218. Enterprise Reliability Model

SalesGenie SHALL provide:

```text
               RELIABLE n8n AUTOMATION

                       ┌───────┐
                       │  AI   │
                       └───┬───┘
                           ↓
                     Policy Engine
                           ↓
                    Authorization
                           ↓
                     Risk Engine
                           ↓
                    n8n Gateway
                           ↓
                  ┌────────┴────────┐
                  ↓                 ↓
                n8n              Fallback
                  ↓                 ↓
             Execution          Human Task
                  │                 │
                  └────────┬────────┘
                           ↓
                       Verification
                           ↓
                    Observability
                           ↓
                         Audit
                           ↓
                    AI Optimization
```

---

## 219. Final Acceptance Criteria

The n8n integration SHALL be considered production-ready only when:

```text
✓ n8n instances can be securely registered.

✓ Tenant isolation is enforced.

✓ RBAC is enforced.

✓ n8n workflows can be discovered.

✓ Workflows can be registered.

✓ Workflows can be executed.

✓ Human-triggered executions work.

✓ AI-triggered executions work through controlled tools.

✓ Scheduled executions work.

✓ Event-driven executions work.

✓ Webhooks are securely validated.

✓ Inputs are schema validated.

✓ Outputs are schema validated.

✓ Credentials are protected.

✓ Secrets are never exposed to AI or frontend clients.

✓ Execution IDs are correlated.

✓ Execution states are synchronized.

✓ Errors are normalized.

✓ Retries are bounded.

✓ Retry storms are prevented.

✓ Circuit breakers are implemented.

✓ Rate limits are enforced.

✓ Timeouts are enforced.

✓ Idempotency is supported.

✓ Replay is controlled.

✓ Dead-letter handling exists.

✓ Human fallback exists.

✓ AI diagnosis exists.

✓ AI recovery is policy governed.

✓ High-risk actions require appropriate approval.

✓ Workflow version mapping exists.

✓ Workflow drift can be detected.

✓ Production activation is controlled.

✓ Audit logs exist.

✓ Distributed tracing exists.

✓ Integration health is monitored.

✓ Cost and quota controls exist.

✓ Emergency kill switches exist.

✓ AI execution can be disabled independently.

✓ Human execution can continue during AI disablement.

✓ n8n failure does not silently lose workflow intent.

✓ Critical business outcomes can be verified.

✓ Security events are observable.

✓ Failure recovery is tested.

✓ Multi-tenant resource isolation is validated.

✓ Disaster recovery procedures are documented and tested.
```

---

## 220. Ultimate SalesGenie n8n Requirement

SalesGenie SHALL transform n8n from a standalone automation tool into a **policy-governed enterprise automation execution layer**.

The complete architecture SHALL combine:

```text
                 SALESGENIE
                     │
     ┌───────────────┼────────────────┐
     ↓               ↓                ↓
    HUMAN            AI             EVENTS
     │               │                │
     └───────────────┼────────────────┘
                     ↓
              INTENT / TRIGGER
                     ↓
             WORKFLOW ENGINE
                     ↓
              POLICY ENGINE
                     ↓
             RBAC + TENANT
                     ↓
              RISK ASSESSMENT
                     ↓
          ┌──────────┴──────────┐
          ↓                     ↓
       APPROVED              BLOCKED
          ↓                     ↓
     n8n EXECUTION          AUDIT/ALERT
          ↓
     EXTERNAL SYSTEMS
          ↓
       VALIDATION
          ↓
     BUSINESS VERIFICATION
          ↓
    ┌─────┴──────┐
    ↓            ↓
 SUCCESS       FAILURE
    ↓            ↓
 COMPLETE     RECOVERY
                 ↓
        ┌────────┼─────────┐
        ↓        ↓         ↓
      RETRY    FALLBACK   HUMAN
        │        │         │
        └────────┼─────────┘
                 ↓
             VERIFY
                 ↓
               AUDIT
                 ↓
          AI OPTIMIZATION
                 ↓
        CONTINUOUS IMPROVEMENT
```

The fundamental principle SHALL be:

```text
n8n EXECUTES.
SALESGENIE GOVERNS.

HUMANS AUTHORIZE.
AI ASSISTS.

POLICIES CONTROL.
AUDIT RECORDS.

ERRORS RECOVER.
SIDE EFFECTS VERIFY.

TENANTS REMAIN ISOLATED.
SECRETS REMAIN PROTECTED.

NO UNAUTHORIZED AUTOMATION.
NO UNCONTROLLED AI EXECUTION.
NO SILENT FAILURES.
NO UNBOUNDED RETRIES.
NO UNVERIFIED CRITICAL SIDE EFFECTS.
```
