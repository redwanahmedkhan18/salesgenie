# SalesGenie — MCP Server Management Requirements Specification

> **Document:** `mcp_server_management.md`
> **Product:** SalesGenie Enterprise AI Customer Support & Sales Agent Platform
> **Subsystem:** Model Context Protocol (MCP) Server Management
> **Requirement Level:** FAANG / Enterprise Production
> **Actors:** Super Admin, Organization Admin, Manager, Human Operator, AI Agent, MCP Gateway, MCP Registry, MCP Server, Workflow Engine, Policy Engine, Security Service, Audit Service, Monitoring Service
> **Scope:** Complete lifecycle management of MCP servers for both human-operated and AI-operated SalesGenie workflows
> **Architecture:** Multi-Tenant + Microservices + Event-Driven + AI-Native + Policy-Driven + Zero-Trust

---

## 1. Purpose

SalesGenie SHALL provide a centralized MCP Server Management subsystem for registering, validating, approving, configuring, enabling, disabling, monitoring, updating, versioning, securing, and decommissioning MCP servers.

The subsystem SHALL provide a strict control boundary between:

- Human users and MCP servers.
- AI agents and MCP servers.
- Workflows and MCP servers.
- SalesGenie internal services and MCP servers.
- External MCP servers and tenant data.

The system SHALL prevent any AI agent, workflow, or human user from directly bypassing the MCP governance layer.

---

## 2. Objectives

The MCP Server Management subsystem SHALL:

1. Provide centralized MCP server lifecycle management.
2. Support both human and AI initiated MCP server operations.
3. Enforce tenant isolation.
4. Enforce RBAC and policy-based authorization.
5. Validate MCP server compatibility.
6. Discover MCP capabilities.
7. Manage MCP server versions.
8. Manage MCP server health.
9. Manage MCP credentials securely.
10. Support approval-based activation.
11. Support automated AI-assisted configuration.
12. Support manual human configuration.
13. Prevent unauthorized server activation.
14. Support server-level tool governance.
15. Support server-level resource governance.
16. Support server-level prompt governance.
17. Support server-level rate limits.
18. Support server-level execution budgets.
19. Support server-level risk controls.
20. Provide complete auditability.
21. Support safe upgrades and rollback.
22. Support emergency server isolation.
23. Support enterprise observability.
24. Support high-scale MCP deployments.

---

## 3. Core Design Principles

The subsystem SHALL follow:

- Zero Trust.
- Least Privilege.
- Defense in Depth.
- Secure by Default.
- Explicit Authorization.
- Runtime Policy Enforcement.
- Tenant Isolation.
- AI Bounded Autonomy.
- Human Oversight.
- Immutable Auditability.
- Fail-Safe Defaults.
- Provider Isolation.
- Version Pinning.
- Idempotent Operations.
- Observable State Transitions.
- Backward Compatibility.
- Controlled Deployment.
- No Silent Configuration Changes.

---

## 4. Actors

## 4.1 Super Admin

The Super Admin SHALL be able to:

- Register global MCP servers.
- Approve MCP servers.
- Reject MCP servers.
- Disable MCP servers globally.
- Configure global MCP policies.
- Review server security posture.
- Review server health.
- Review server usage.
- Review global audit events.
- Configure trusted providers.
- Configure server risk policies.
- Configure global limits.
- Perform emergency shutdown.
- Restore servers.
- Decommission servers.

The Super Admin SHALL NOT automatically gain access to tenant business data.

---

## 4.2 Organization Admin

The Organization Admin SHALL be able to:

- Discover approved MCP servers.
- Request server activation.
- Configure organization-specific servers.
- Enable approved servers.
- Disable organization servers.
- Configure allowed tools.
- Configure allowed resources.
- Configure allowed prompts.
- Configure AI agent access.
- Configure human access.
- Configure workflow access.
- Configure server limits.
- Configure approval requirements.
- Manage organization-level MCP credentials.
- Review server health.
- Review server usage.
- Review server audit events.

---

## 4.3 Manager

Managers SHALL be able to:

- Configure MCP servers for teams.
- Assign MCP servers to workflows.
- Assign MCP capabilities to AI agents.
- Configure execution policies.
- Configure approval policies.
- Review server execution history.
- Review server failures.

---

## 4.4 Human Operator

Authorized human operators SHALL be able to:

- View authorized servers.
- View server status.
- Request server activation.
- Execute permitted validation tests.
- Review server configuration.
- Trigger permitted health checks.
- Request disablement.
- Review server events.

---

## 4.5 AI Agent

AI Agents SHALL be able to:

- Discover authorized MCP servers.
- Discover server capabilities.
- Recommend MCP servers.
- Request MCP server access.
- Request capability activation.
- Request configuration changes.
- Trigger permitted health checks.
- Report server failures.

AI Agents SHALL NOT be able to:

- Grant themselves access.
- Approve their own server requests.
- Disable security controls.
- Access server credentials.
- Modify tenant isolation.
- Modify global policies.
- Bypass approval requirements.
- Activate unapproved servers.
- Change their own MCP permissions.

---

## 5. User Requirements

## UR-MCP-SM-001 — Server Discovery

Users SHALL be able to discover available MCP servers from the SalesGenie MCP catalog.

The catalog SHALL display:

- Server name.
- Provider.
- Description.
- Version.
- Protocol compatibility.
- Capabilities.
- Security status.
- Trust level.
- Health status.
- Risk level.
- Availability.
- Required permissions.
- Supported tools.
- Supported resources.
- Supported prompts.

---

## UR-MCP-SM-002 — Server Registration

Authorized administrators SHALL be able to register an MCP server.

Registration SHALL support:

```yaml
server:
  name:
  description:
  provider:
  endpoint:
  protocol_version:
  authentication:
  transport:
  metadata:
  tags:
```

---

## UR-MCP-SM-003 — AI Server Recommendation

AI Agents SHALL be able to recommend an MCP server based on a user or workflow objective.

Example:

```text
User:
"Connect SalesGenie to our CRM."

AI:
Recommended MCP Server:
CRM MCP Server

Reason:
Provides:
- Customer lookup
- Lead creation
- Contact updates
- Opportunity management
```

AI recommendations SHALL NOT automatically enable the server.

---

## UR-MCP-SM-004 — AI Server Access Request

AI Agents SHALL be able to request server access when a workflow requires capabilities not currently enabled.

```text
AI Agent
   ↓
Detect Missing Capability
   ↓
Identify MCP Server
   ↓
Create Access Request
   ↓
Policy Evaluation
   ↓
Human/Admin Approval
   ↓
Activation
```

---

## UR-MCP-SM-005 — Human Server Activation

Authorized administrators SHALL be able to activate approved MCP servers.

Activation SHALL require:

```text
Server Validation
+
Authentication Validation
+
Security Policy Validation
+
Permission Configuration
+
Approval
```

where applicable.

---

## UR-MCP-SM-006 — Server Configuration

Authorized administrators SHALL be able to configure:

* Server endpoint.
* Transport.
* Authentication.
* Allowed users.
* Allowed roles.
* Allowed agents.
* Allowed workflows.
* Allowed tools.
* Allowed resources.
* Allowed prompts.
* Rate limits.
* Timeouts.
* Retry policies.
* Approval policies.
* Execution budgets.
* Risk controls.

---

## UR-MCP-SM-007 — Server Status

Users SHALL be able to view:

```text
REGISTERED
VALIDATING
APPROVED
ENABLED
HEALTHY
UNHEALTHY
DEGRADED
DISABLED
MAINTENANCE
BLOCKED
DEPRECATED
DECOMMISSIONED
```

---

## UR-MCP-SM-008 — Server Health

Users SHALL be able to inspect:

* Availability.
* Latency.
* Error rate.
* Connection state.
* Authentication status.
* Capability discovery status.
* Tool availability.
* Resource availability.
* Rate-limit state.
* Circuit-breaker state.

---

## UR-MCP-SM-009 — Server Disablement

Authorized administrators SHALL be able to immediately disable an MCP server.

Disabling a server SHALL:

* Prevent new executions.
* Prevent new workflow assignments.
* Prevent AI tool execution.
* Preserve audit records.
* Preserve historical execution data.
* Optionally cancel active executions according to policy.

---

## UR-MCP-SM-010 — Server Version Management

Administrators SHALL be able to:

* View available versions.
* Pin versions.
* Upgrade versions.
* Roll back versions.
* Mark versions deprecated.
* Configure upgrade policies.

---

## UR-MCP-SM-011 — Server Decommissioning

Administrators SHALL be able to decommission servers through a controlled lifecycle.

```text
Active
 ↓
Disable
 ↓
Drain
 ↓
Archive
 ↓
Decommission
```

Historical records SHALL remain available according to retention policy.

---

## 6. System Requirements

## SR-MCP-SM-001 — MCP Server Registry

SalesGenie SHALL maintain a centralized MCP Server Registry.

```yaml
MCPServer:
  server_id:
  organization_id:
  provider_id:
  name:
  description:
  endpoint:
  transport:
  protocol_version:
  server_version:
  trust_level:
  risk_level:
  status:
  health_status:
  capabilities:
  enabled:
  created_by:
  created_at:
  updated_at:
```

---

## SR-MCP-SM-002 — Multi-Tenant Isolation

Every server record SHALL be associated with an explicit tenant scope.

Tenant isolation SHALL be enforced at:

* API gateway.
* Application service.
* Authorization layer.
* Database.
* MCP gateway.
* Credential store.
* Cache.
* Queue.
* Audit system.

---

## SR-MCP-SM-003 — Server Identity

Every MCP server SHALL have a globally unique immutable identifier.

Example:

```text
mcp_srv_01JXXXXXXXXXXXX
```

Server IDs SHALL NOT be reused.

---

## SR-MCP-SM-004 — Server Fingerprinting

The platform SHOULD maintain a server fingerprint based on trusted metadata and validated configuration.

Fingerprint changes SHALL trigger security review when appropriate.

---

## SR-MCP-SM-005 — MCP Gateway Enforcement

All production MCP server traffic SHALL pass through the MCP Gateway.

```text
AI / Human / Workflow
        ↓
Authorization
        ↓
Policy Engine
        ↓
MCP Gateway
        ↓
MCP Server
```

Direct external access from application components SHALL be prohibited unless explicitly approved by architecture policy.

---

## SR-MCP-SM-006 — Capability Registry

The platform SHALL maintain discovered server capabilities.

Supported capability categories SHALL include:

```text
TOOLS
RESOURCES
PROMPTS
NOTIFICATIONS
SAMPLING
OTHER_SUPPORTED_CAPABILITIES
```

---

## SR-MCP-SM-007 — Credential Isolation

Credentials SHALL be stored outside MCP server configuration records.

Configuration SHALL reference credentials indirectly.

```yaml
authentication:
  type: oauth2
  credential_reference: cred_xxxxx
```

---

## SR-MCP-SM-008 — Secret Protection

Secrets SHALL:

* Be encrypted at rest.
* Be encrypted in transit.
* Never enter AI context.
* Never appear in browser payloads.
* Never appear in standard logs.
* Never be embedded in workflow definitions.

---

## SR-MCP-SM-009 — Server Health Service

The platform SHALL continuously or periodically monitor server health.

Health checks SHALL support:

* Connectivity.
* Authentication.
* Protocol compatibility.
* Capability discovery.
* Tool availability.
* Response latency.

---

## SR-MCP-SM-010 — Configuration Store

Server configuration SHALL be versioned.

Every configuration change SHALL create a new configuration revision.

```text
Configuration v1
Configuration v2
Configuration v3
```

---

## SR-MCP-SM-011 — Immutable Configuration History

Historical configuration versions SHALL remain auditable.

Authorized users SHALL be able to identify:

* Who changed the configuration.
* What changed.
* Why it changed.
* When it changed.
* Previous value.
* New value.
* Approval.
* Result.

Sensitive values SHALL remain redacted.

---

## SR-MCP-SM-012 — Policy Engine

The MCP Server Management subsystem SHALL integrate with the centralized SalesGenie policy engine.

Policy evaluation SHALL consider:

```text
User
Role
Tenant
Agent
Workflow
Server
Tool
Resource
Prompt
Risk
Environment
Time
Budget
Approval
```

---

## SR-MCP-SM-013 — Server Risk Classification

Each server SHALL have a configurable risk classification:

```text
TRUSTED
LOW
MEDIUM
HIGH
CRITICAL
```

Risk classification SHALL influence:

* Approval.
* Access.
* Execution.
* Monitoring.
* Rate limits.
* Audit requirements.

---

## SR-MCP-SM-014 — Server Trust Model

Servers SHALL support trust states:

```text
UNVERIFIED
VERIFIED
TRUSTED
ORGANIZATION_APPROVED
BLOCKED
DEPRECATED
```

Trust status SHALL NOT replace authorization.

---

## SR-MCP-SM-015 — Environment Separation

The platform SHALL distinguish:

```text
DEVELOPMENT
STAGING
PRODUCTION
```

A server approved in development SHALL NOT automatically become production-enabled.

---

## SR-MCP-SM-016 — Server Deployment Isolation

Server configuration SHALL be environment-scoped.

Production credentials SHALL never be automatically copied into development environments.

---

## 7. Functional Requirements

## 7.1 Registration

## FR-MCP-SM-001 — Create Server

The system SHALL allow authorized users to create an MCP server record.

Required fields SHALL include:

```text
Name
Provider
Endpoint
Transport
Protocol Version
Authentication Type
```

---

## FR-MCP-SM-002 — Duplicate Detection

The system SHALL detect likely duplicate MCP server registrations.

Duplicate detection SHOULD consider:

* Provider.
* Endpoint.
* Server identity.
* Server metadata.
* Fingerprint.

---

## FR-MCP-SM-003 — Registration Validation

The platform SHALL validate:

* Required fields.
* Endpoint format.
* Transport compatibility.
* Authentication configuration.
* Protocol compatibility.
* Tenant scope.

---

## 7.2 Server Validation

## FR-MCP-SM-004 — Connectivity Test

The platform SHALL test connectivity before activation.

---

## FR-MCP-SM-005 — Protocol Test

The platform SHALL verify MCP protocol compatibility.

---

## FR-MCP-SM-006 — Capability Discovery

The system SHALL discover:

```text
Tools
Resources
Prompts
Supported Capabilities
```

---

## FR-MCP-SM-007 — Schema Validation

Discovered schemas SHALL be validated before being exposed to AI Agents or workflows.

---

## FR-MCP-SM-008 — Security Validation

The platform SHALL perform configurable security checks before approving a server.

---

## 7.3 Approval

## FR-MCP-SM-009 — Approval Workflow

Servers requiring approval SHALL follow:

```text
Registered
   ↓
Validated
   ↓
Security Review
   ↓
Policy Evaluation
   ↓
Human Approval
   ↓
Approved
   ↓
Enabled
```

---

## FR-MCP-SM-010 — AI-Initiated Approval

AI Agents SHALL be able to create server access requests.

The request SHALL contain:

```yaml
request:
  agent_id:
  workflow_id:
  objective:
  server_id:
  requested_capabilities:
  business_reason:
  expected_actions:
  risk:
```

---

## FR-MCP-SM-011 — Human Approval

Approvers SHALL be able to:

```text
Approve
Reject
Request More Information
Modify Scope
Set Expiration
```

---

## FR-MCP-SM-012 — Approval Expiration

Approval decisions MAY have expiration timestamps.

Expired approvals SHALL NOT authorize server activation.

---

## 7.4 Enablement

## FR-MCP-SM-013 — Enable Server

Only servers satisfying required validation and approval policies SHALL be enabled.

---

## FR-MCP-SM-014 — Enablement Preconditions

Before enabling:

```text
Server Valid
AND
Authentication Valid
AND
Policy Valid
AND
Required Permissions Configured
AND
Security Status Acceptable
```

must be satisfied.

---

## 7.5 Disablement

## FR-MCP-SM-015 — Disable Server

Authorized administrators SHALL be able to disable servers.

---

## FR-MCP-SM-016 — Immediate Blocking

Emergency disablement SHALL block new requests at the MCP Gateway.

---

## FR-MCP-SM-017 — Drain Mode

The platform SHOULD support graceful server draining.

```text
DISABLE NEW EXECUTIONS
        ↓
WAIT FOR ACTIVE OPERATIONS
        ↓
COMPLETE / CANCEL
        ↓
DISABLED
```

---

## 7.6 AI-Based Server Management

## FR-MCP-SM-018 — AI Capability Matching

AI Agents SHALL be able to map user objectives to MCP server capabilities.

Example:

```text
Objective:
"Update Salesforce leads."

Required capabilities:
- Lead lookup
- Lead update

Candidate:
Salesforce MCP Server
```

---

## FR-MCP-SM-019 — AI Server Recommendation

AI SHALL rank candidate servers using:

```text
Capability Match
Authorization
Trust
Risk
Availability
Latency
Cost
Tenant Policy
```

---

## FR-MCP-SM-020 — AI Cannot Bypass Policy

AI recommendations SHALL remain advisory.

Final authorization SHALL be performed by the server-side policy engine.

---

## FR-MCP-SM-021 — AI Health Diagnosis

AI MAY analyze server telemetry to identify:

* Repeated failures.
* Latency degradation.
* Authentication failures.
* Tool-specific failures.
* Provider outages.

AI recommendations SHALL NOT automatically modify critical server configuration without authorization.

---

## FR-MCP-SM-022 — AI Configuration Recommendation

AI MAY recommend:

* Timeout changes.
* Rate-limit adjustments.
* Tool restrictions.
* Server replacement.
* Version upgrades.
* Retry adjustments.

High-impact configuration changes SHALL require human/admin approval.

---

## 7.7 Human-Based Server Management

## FR-MCP-SM-023 — Manual Configuration

Administrators SHALL be able to manually configure server settings.

---

## FR-MCP-SM-024 — Configuration Preview

Before publishing a configuration change, the UI SHALL show a diff.

```text
Before:
timeout = 30s

After:
timeout = 60s
```

---

## FR-MCP-SM-025 — Configuration Approval

Production configuration changes MAY require approval based on policy.

---

## 7.8 Server Capability Management

## FR-MCP-SM-026 — Tool Discovery

The system SHALL discover tools exposed by a server.

---

## FR-MCP-SM-027 — Resource Discovery

The system SHALL discover resources exposed by a server.

---

## FR-MCP-SM-028 — Prompt Discovery

The system SHALL discover prompts exposed by a server.

---

## FR-MCP-SM-029 — Capability Refresh

Administrators SHALL be able to trigger capability refresh.

The platform SHOULD also support scheduled capability synchronization.

---

## FR-MCP-SM-030 — Capability Drift Detection

The platform SHALL detect changes between previously known and newly discovered capabilities.

Example:

```text
Previous:
create_lead
update_lead

Current:
create_lead
update_lead
delete_lead
```

New high-risk capabilities SHALL NOT automatically become available to AI Agents.

---

## 7.9 Server-Level Tool Governance

## FR-MCP-SM-031

Administrators SHALL be able to disable individual tools without disabling the entire server.

Example:

```text
Salesforce MCP Server
 ├── search_lead       ENABLED
 ├── create_lead       ENABLED
 ├── update_lead       ENABLED
 └── delete_lead       DISABLED
```

---

## FR-MCP-SM-032

Tool access SHALL support:

```text
Allow
Deny
Approval Required
Read Only
Role Restricted
Agent Restricted
Workflow Restricted
```

---

## 7.10 Server-Level Resource Governance

## FR-MCP-SM-033

Administrators SHALL be able to restrict resource access.

Restrictions MAY include:

* Resource URI.
* Tenant.
* User.
* Role.
* Agent.
* Workflow.

---

## 7.11 Server-Level Prompt Governance

## FR-MCP-SM-034

Administrators SHALL be able to control MCP prompt access.

MCP prompts SHALL never override SalesGenie system-level security policies.

---

## 8. Server Lifecycle State Machine

The platform SHALL implement a deterministic state machine.

```text
                    ┌─────────────┐
                    │ REGISTERED  │
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │ VALIDATING  │
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │  APPROVED   │
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │   ENABLED   │
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │   HEALTHY   │
                    └──────┬──────┘
                           │
              ┌────────────┼─────────────┐
              ↓            ↓             ↓
         UNHEALTHY     MAINTENANCE    DEPRECATED
              │            │             │
              ↓            ↓             ↓
          RECOVERY       ENABLED       DISABLED
              │
              ↓
           HEALTHY
```

Terminal state:

```text
DECOMMISSIONED
```

---

## 9. State Transition Requirements

## FR-MCP-SM-035

Only valid state transitions SHALL be accepted.

## FR-MCP-SM-036

Every state transition SHALL create an audit event.

## FR-MCP-SM-037

AI Agents SHALL NOT directly transition servers into:

```text
APPROVED
ENABLED
TRUSTED
```

without required authorization.

---

## 10. Health Monitoring

## FR-MCP-SM-038 — Health Checks

Health checks SHALL run:

* On registration.
* Before activation.
* Periodically.
* After configuration changes.
* After upgrades.
* On administrator request.

---

## FR-MCP-SM-039 — Health Score

The platform MAY calculate a server health score using:

```text
Availability
Latency
Error Rate
Authentication
Capability Availability
Timeouts
Rate Limits
```

---

## FR-MCP-SM-040 — Degradation Detection

The platform SHALL detect abnormal degradation.

Example:

```text
P95 latency:
400ms → 2.8s

Error rate:
1% → 18%
```

---

## FR-MCP-SM-041 — Automatic Isolation

The platform MAY automatically isolate a server when configured thresholds are exceeded.

Automatic isolation SHALL be policy-controlled.

---

## 11. Version Management

## FR-MCP-SM-042 — Version Registry

The platform SHALL maintain server versions.

```yaml
version:
  server_id:
  version:
  protocol_version:
  compatibility:
  release_status:
  security_status:
  created_at:
```

---

## FR-MCP-SM-043 — Version Pinning

Production workflows SHOULD be able to pin a specific server version.

---

## FR-MCP-SM-044 — Upgrade Validation

Before upgrade:

```text
Compatibility Check
+
Security Check
+
Capability Diff
+
Workflow Impact Analysis
```

SHALL be performed where applicable.

---

## FR-MCP-SM-045 — Rollback

The platform SHALL support rollback to the previous validated version.

---

## 12. Configuration Management

## FR-MCP-SM-046 — Configuration Revision

Every configuration update SHALL create a revision.

---

## FR-MCP-SM-047 — Configuration Diff

The platform SHALL provide before/after comparison.

---

## FR-MCP-SM-048 — Configuration Rollback

Authorized administrators SHALL be able to restore a previous configuration.

---

## FR-MCP-SM-049 — Configuration Validation

Configuration SHALL be validated before deployment.

---

## 13. Rate Limiting

Server-level rate limits SHALL support:

```yaml
rate_limit:
  requests_per_second:
  requests_per_minute:
  requests_per_hour:
  burst:
  concurrency:
```

Limits SHALL be configurable by:

```text
Platform
Tenant
User
Agent
Workflow
Server
Tool
```

---

## 14. Timeout Management

Server configuration SHALL support:

```yaml
timeout:
  connection:
  request:
  tool_execution:
  discovery:
```

Timeouts SHALL be enforced by the gateway rather than relying solely on external servers.

---

## 15. Retry Management

Server-level retry policies SHALL support:

```yaml
retry:
  enabled:
  max_attempts:
  backoff:
  jitter:
  retryable_errors:
  non_retryable_errors:
```

The platform SHALL prevent unsafe retries of non-idempotent operations.

---

## 16. Circuit Breaker

Each MCP server SHOULD have an independent circuit breaker.

```text
CLOSED
   ↓
Failure Threshold
   ↓
OPEN
   ↓
Recovery Window
   ↓
HALF_OPEN
   ↓
Successful Probe
   ↓
CLOSED
```

---

## 17. Security Requirements

## SEC-MCP-SM-001 — Zero Trust

Every request SHALL be authenticated and authorized independently.

---

## SEC-MCP-SM-002 — Tenant Isolation

An MCP server belonging to Tenant A SHALL NOT be accessible by Tenant B unless explicitly configured through a shared trusted platform mechanism.

---

## SEC-MCP-SM-003 — Credential Isolation

AI Agents SHALL never receive MCP credentials.

---

## SEC-MCP-SM-004 — Credential Rotation

The system SHALL support credential rotation without requiring workflow redesign.

---

## SEC-MCP-SM-005 — Secret Redaction

Secrets SHALL be redacted from:

* Logs.
* Errors.
* Traces.
* UI responses.
* AI context.
* Audit payloads.

---

## SEC-MCP-SM-006 — Endpoint Validation

Server endpoints SHALL be validated against configurable network security policies.

---

## SEC-MCP-SM-007 — SSRF Protection

MCP server registration SHALL include SSRF protections.

The platform SHALL prevent unauthorized access to:

* Internal metadata endpoints.
* Private network resources.
* Restricted internal services.
* Unauthorized localhost services.

---

## SEC-MCP-SM-008 — Tool Injection Protection

Malicious tool descriptions SHALL not be allowed to alter SalesGenie's system instructions or authorization policies.

---

## SEC-MCP-SM-009 — Prompt Injection Protection

MCP server metadata, prompts, resources, and tool responses SHALL be treated as untrusted input.

---

## SEC-MCP-SM-010 — Supply Chain Risk

Third-party MCP servers SHALL support configurable trust and security review states.

---

## 18. AI Safety Requirements

## AI-SEC-MCP-001

AI Agents SHALL only see MCP servers authorized for their tenant and execution context.

## AI-SEC-MCP-002

AI Agents SHALL only see permitted capabilities.

## AI-SEC-MCP-003

AI Agents SHALL not receive hidden administrative capabilities.

## AI-SEC-MCP-004

AI Agents SHALL not modify their own server permissions.

## AI-SEC-MCP-005

AI Agents SHALL not approve their own access requests.

## AI-SEC-MCP-006

AI Agents SHALL stop when server authorization fails.

## AI-SEC-MCP-007

AI Agents SHALL escalate when server configuration requires human authorization.

---

## 19. Human Governance Requirements

## HUMAN-MCP-SM-001

Production MCP server activation SHALL support configurable human approval.

## HUMAN-MCP-SM-002

High-risk servers SHALL require explicit administrator approval.

## HUMAN-MCP-SM-003

Critical configuration changes SHALL support multi-party approval.

## HUMAN-MCP-SM-004

Emergency actions SHALL be restricted to authorized administrators.

## HUMAN-MCP-SM-005

Approval decisions SHALL be immutable.

---

## 20. Server Access Control

The platform SHALL support permissions including:

```text
mcp.server.read
mcp.server.register
mcp.server.validate
mcp.server.approve
mcp.server.enable
mcp.server.disable
mcp.server.update
mcp.server.delete
mcp.server.decommission
mcp.server.health.read
mcp.server.health.execute
mcp.server.version.read
mcp.server.version.manage
mcp.server.credentials.manage
mcp.server.policy.read
mcp.server.policy.manage
mcp.server.audit.read
mcp.server.metrics.read
```

---

## 21. AI vs Human Authority Matrix

| Operation              |      Human Admin |     AI Agent |
| ---------------------- | ---------------: | -----------: |
| Discover Server        |              YES |          YES |
| View Server Metadata   |              YES |          YES |
| Recommend Server       |              N/A |          YES |
| Register Server        |              YES | REQUEST ONLY |
| Validate Server        |              YES |      LIMITED |
| Approve Server         |              YES |           NO |
| Enable Server          |              YES |           NO |
| Disable Server         |              YES |          NO* |
| Modify Security Policy |              YES |           NO |
| Modify Credentials     |              YES |           NO |
| Discover Capabilities  |              YES |          YES |
| Enable Low-Risk Tool   |              YES |      REQUEST |
| Enable High-Risk Tool  |     YES + Policy |           NO |
| Upgrade Server         |              YES |      REQUEST |
| Rollback Server        |              YES |      REQUEST |
| Health Check           |              YES |      LIMITED |
| Decommission Server    |              YES |           NO |
| Emergency Shutdown     | AUTHORIZED ADMIN |           NO |

`*` AI may request emergency disablement, but the final action SHALL be policy-controlled and SHALL NOT grant the AI broader authority.

---

## 22. MCP Server Management Workflow

```text
                 ┌───────────────────┐
                 │ Human / AI Request │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Identity Context  │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Authorization     │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Policy Evaluation │
                 └─────────┬─────────┘
                           ↓
                  ┌────────┴────────┐
                  │                 │
                DENY             ALLOW
                  │                 │
                  ↓                 ↓
                Audit        Validation
                                    ↓
                              Security Check
                                    ↓
                              Configuration
                                    ↓
                              Approval
                                    ↓
                                Enable
                                    ↓
                              Health Check
                                    ↓
                                Active
```

---

## 23. AI-Driven Server Selection Workflow

```text
User Objective
      ↓
AI Intent Analysis
      ↓
Required Capability Extraction
      ↓
MCP Server Candidate Search
      ↓
Authorization Filtering
      ↓
Trust Filtering
      ↓
Risk Filtering
      ↓
Availability Filtering
      ↓
Cost / Latency Ranking
      ↓
Server Recommendation
      ↓
Human / Policy Approval
      ↓
MCP Server Activation
```

---

## 24. AI-Driven Server Failure Workflow

```text
MCP Server Failure
       ↓
Telemetry
       ↓
Failure Classification
       ↓
AI Diagnosis
       ↓
Determine Recovery Option
       ↓
┌───────────────┬────────────────┬─────────────────┐
│ Retry         │ Failover       │ Human Escalate  │
└──────┬────────┴───────┬────────┴────────┬────────┘
       ↓                ↓                 ↓
     Retry       Alternative Server    Approval
       ↓                ↓                 ↓
       └────────────────┴─────────────────┘
                        ↓
                     Audit
```

---

## 25. Human Server Management Workflow

```text
Administrator
      ↓
MCP Server Catalog
      ↓
Select Server
      ↓
Review Security
      ↓
Review Capabilities
      ↓
Configure Access
      ↓
Configure Policies
      ↓
Test Connection
      ↓
Review Configuration Diff
      ↓
Approve
      ↓
Enable
      ↓
Monitor
```

---

## 26. MCP Server Upgrade Workflow

```text
New Version Detected
        ↓
Compatibility Analysis
        ↓
Capability Diff
        ↓
Security Analysis
        ↓
Workflow Impact Analysis
        ↓
AI Recommendation
        ↓
Human Review
        ↓
Staging Validation
        ↓
Production Approval
        ↓
Upgrade
        ↓
Health Validation
        ↓
Success
```

Failure:

```text
Upgrade Failure
      ↓
Health Check
      ↓
Automatic Rollback / Manual Rollback
      ↓
Incident
      ↓
Audit
```

---

## 27. MCP Server Decommission Workflow

```text
Decommission Request
        ↓
Dependency Analysis
        ↓
Active Workflow Analysis
        ↓
AI Impact Assessment
        ↓
Human Approval
        ↓
Disable
        ↓
Drain
        ↓
Archive
        ↓
Credential Revocation
        ↓
Decommission
```

---

## 28. Dependency Management

Before disabling, upgrading, or decommissioning a server, the platform SHALL identify:

```text
Agents
Workflows
Tools
Resources
Prompts
Users
Tenants
Scheduled Jobs
Active Executions
```

The platform SHALL warn administrators about affected dependencies.

---

## 29. Impact Analysis

The system SHALL support impact analysis such as:

```text
Server:
Salesforce MCP

Affected:
12 AI Agents
38 Workflows
14 Scheduled Jobs
246 Users
3 Organizations
```

---

## 30. Emergency Server Shutdown

Authorized administrators SHALL be able to trigger:

```text
Emergency Disable
```

The operation SHALL:

1. Block new executions.
2. Stop capability exposure.
3. Optionally terminate active operations.
4. Revoke temporary access.
5. Generate a critical audit event.
6. Notify configured administrators.
7. Preserve historical data.

---

## 31. Audit Requirements

Every significant server event SHALL produce an audit record.

Events SHALL include:

```text
MCP_SERVER_REGISTERED
MCP_SERVER_VALIDATED
MCP_SERVER_APPROVED
MCP_SERVER_REJECTED
MCP_SERVER_ENABLED
MCP_SERVER_DISABLED
MCP_SERVER_UPDATED
MCP_SERVER_CONFIG_CHANGED
MCP_SERVER_VERSION_CHANGED
MCP_SERVER_HEALTH_CHANGED
MCP_SERVER_CAPABILITIES_CHANGED
MCP_SERVER_CREDENTIAL_CHANGED
MCP_SERVER_POLICY_CHANGED
MCP_SERVER_DECOMMISSIONED
MCP_SERVER_EMERGENCY_DISABLED
```

Each event SHOULD include:

```yaml
audit:
  event_id:
  event_type:
  timestamp:
  organization_id:
  actor_type:
  actor_id:
  server_id:
  request_id:
  trace_id:
  workflow_id:
  reason:
  result:
```

---

## 32. Observability Requirements

The platform SHALL expose:

## Server Metrics

```text
Availability
Uptime
Latency
P50
P95
P99
Error Rate
Timeout Rate
Authentication Failure Rate
```

## Capability Metrics

```text
Tool Count
Resource Count
Prompt Count
Capability Drift
Disabled Tools
Blocked Tools
```

## Usage Metrics

```text
Executions
Tool Calls
Resource Reads
AI Calls
Human Calls
Workflow Calls
```

---

## 33. Cost Management

The system SHALL track server usage by:

```text
Organization
User
Agent
Workflow
Server
Tool
Execution
```

Cost information MAY include:

```text
External API Cost
AI Processing Cost
Execution Cost
Data Transfer Cost
Provider Cost
```

---

## 34. Quotas

Server-level quotas SHALL support:

```yaml
quota:
  max_requests_per_day:
  max_requests_per_month:
  max_concurrent_requests:
  max_execution_time:
  max_cost:
  max_payload_size:
```

Quota violations SHALL trigger configurable behavior:

```text
BLOCK
QUEUE
DEGRADE
REQUIRE_APPROVAL
ALERT
```

---

## 35. API Requirements

The MCP Server Management subsystem SHALL expose APIs conceptually equivalent to:

```text
POST   /api/v1/mcp/servers
GET    /api/v1/mcp/servers
GET    /api/v1/mcp/servers/{server_id}
PATCH  /api/v1/mcp/servers/{server_id}
DELETE /api/v1/mcp/servers/{server_id}

POST   /api/v1/mcp/servers/{server_id}/validate
POST   /api/v1/mcp/servers/{server_id}/approve
POST   /api/v1/mcp/servers/{server_id}/reject
POST   /api/v1/mcp/servers/{server_id}/enable
POST   /api/v1/mcp/servers/{server_id}/disable
POST   /api/v1/mcp/servers/{server_id}/health
POST   /api/v1/mcp/servers/{server_id}/refresh

GET    /api/v1/mcp/servers/{server_id}/capabilities
GET    /api/v1/mcp/servers/{server_id}/tools
GET    /api/v1/mcp/servers/{server_id}/resources
GET    /api/v1/mcp/servers/{server_id}/prompts

GET    /api/v1/mcp/servers/{server_id}/versions
POST   /api/v1/mcp/servers/{server_id}/upgrade
POST   /api/v1/mcp/servers/{server_id}/rollback

GET    /api/v1/mcp/servers/{server_id}/configuration
GET    /api/v1/mcp/servers/{server_id}/configuration/history
POST   /api/v1/mcp/servers/{server_id}/configuration/validate
POST   /api/v1/mcp/servers/{server_id}/configuration/publish
POST   /api/v1/mcp/servers/{server_id}/configuration/rollback

GET    /api/v1/mcp/servers/{server_id}/dependencies
GET    /api/v1/mcp/servers/{server_id}/impact-analysis
GET    /api/v1/mcp/servers/{server_id}/health
GET    /api/v1/mcp/servers/{server_id}/metrics
GET    /api/v1/mcp/servers/{server_id}/audit
```

Actual endpoints SHALL remain consistent with SalesGenie's established API gateway and service conventions.

---

## 36. Event Requirements

The subsystem SHALL publish events including:

```text
MCP_SERVER_REGISTERED
MCP_SERVER_VALIDATION_STARTED
MCP_SERVER_VALIDATED
MCP_SERVER_VALIDATION_FAILED

MCP_SERVER_APPROVAL_REQUESTED
MCP_SERVER_APPROVED
MCP_SERVER_REJECTED

MCP_SERVER_ENABLED
MCP_SERVER_DISABLED
MCP_SERVER_DRAINING

MCP_SERVER_HEALTHY
MCP_SERVER_UNHEALTHY
MCP_SERVER_DEGRADED
MCP_SERVER_RECOVERED

MCP_SERVER_CAPABILITIES_DISCOVERED
MCP_SERVER_CAPABILITIES_CHANGED

MCP_SERVER_CONFIGURATION_CREATED
MCP_SERVER_CONFIGURATION_PUBLISHED
MCP_SERVER_CONFIGURATION_ROLLED_BACK

MCP_SERVER_VERSION_DETECTED
MCP_SERVER_UPGRADE_STARTED
MCP_SERVER_UPGRADED
MCP_SERVER_ROLLBACK_STARTED
MCP_SERVER_ROLLED_BACK

MCP_SERVER_CREDENTIAL_ROTATED
MCP_SERVER_POLICY_CHANGED

MCP_SERVER_DECOMMISSION_REQUESTED
MCP_SERVER_DECOMMISSIONED

MCP_SERVER_EMERGENCY_DISABLED
MCP_SERVER_SECURITY_EVENT
```

---

## 37. Data Model

Core entities SHALL include:

```text
MCPServer
MCPServerProvider
MCPServerVersion
MCPServerConfiguration
MCPServerConfigurationRevision
MCPServerCapability
MCPServerHealth
MCPServerDependency
MCPServerCredentialReference
MCPServerPolicy
MCPServerAccessGrant
MCPServerApproval
MCPServerAuditEvent
MCPServerUsage
MCPServerQuota
MCPServerRateLimit
MCPServerIncident
MCPServerSecurityFinding
MCPServerUpgrade
MCPServerDecommissionRequest
```

---

## 38. Example Server Object

```yaml
mcp_server:
  server_id: "mcp_srv_salesforce"
  organization_id: "org_123"

  identity:
    name: "Salesforce MCP Server"
    provider: "Salesforce"
    description: "CRM integration for SalesGenie"

  connection:
    endpoint: "managed-reference"
    transport: "configured"
    protocol_version: "supported-version"

  security:
    trust_level: "ORGANIZATION_APPROVED"
    risk_level: "MEDIUM"
    authentication: "oauth2"

  capabilities:
    tools:
      - search_lead
      - create_lead
      - update_lead

    resources:
      - crm://leads
      - crm://contacts

    prompts:
      - lead_analysis

  policy:
    ai_access: true
    human_access: true
    approval_required_for:
      - update_lead

  limits:
    requests_per_minute: 100
    concurrency: 20

  lifecycle:
    status: "ENABLED"
    health: "HEALTHY"
```

---

## 39. Example AI Server Request

```yaml
ai_request:
  agent_id: "agent_sales_research"
  workflow_id: "workflow_lead_generation"

  objective:
    "Identify qualified leads and synchronize them with the CRM."

  required_capabilities:
    - company_search
    - lead_enrichment
    - crm_create_lead

  requested_server:
    "CRM MCP Server"

  reason:
    "Workflow requires CRM synchronization."

  expected_risk:
    "MEDIUM"
```

The request SHALL be evaluated by the authorization and policy engines before access is granted.

---

## 40. Example Human Server Request

```yaml
human_request:
  user_id: "user_123"
  organization_id: "org_123"

  server:
    "Salesforce MCP Server"

  requested_access:
    tools:
      - search_lead
      - create_lead

  reason:
    "Sales team CRM synchronization"

  duration:
    "organization-defined"
```

---

## 41. Enterprise Dashboard Requirements

The MCP Server Management dashboard SHALL display:

```text
Total Servers
Active Servers
Pending Approvals
Unhealthy Servers
Degraded Servers
Blocked Servers
Deprecated Servers

Total Tools
Total Resources
Total Prompts

Executions
Success Rate
Failure Rate
P95 Latency
P99 Latency

Security Findings
Policy Violations
Authentication Failures

Active AI Agents
Active Workflows
Active Executions

Usage
Quota
Cost
```

---

## 42. Server Detail Page

The server detail page SHALL contain:

```text
Overview
Health
Capabilities
Tools
Resources
Prompts
Configuration
Authentication
Permissions
Policies
Versions
Dependencies
Executions
Metrics
Audit Logs
Security
Incidents
```

---

## 43. Configuration UX Requirements

The configuration interface SHALL:

* Clearly distinguish editable and read-only values.
* Hide secrets.
* Show validation errors.
* Show security warnings.
* Show impact analysis.
* Show configuration diff.
* Require confirmation for destructive changes.
* Show approval requirements.
* Show affected agents/workflows.
* Show rollback availability.

---

## 44. Failure Handling

The subsystem SHALL distinguish:

```text
VALIDATION_FAILURE
AUTHENTICATION_FAILURE
AUTHORIZATION_FAILURE
NETWORK_FAILURE
TIMEOUT
PROTOCOL_FAILURE
CAPABILITY_FAILURE
SECURITY_FAILURE
CONFIGURATION_FAILURE
PROVIDER_FAILURE
RATE_LIMIT
QUOTA_EXCEEDED
```

---

## 45. Failure Recovery

Recovery SHALL support:

```text
Retry
Backoff
Circuit Breaker
Failover
Rollback
Disable
Human Escalation
AI Diagnosis
```

---

## 46. Failover

Where multiple equivalent MCP servers exist, the platform MAY support controlled failover.

Failover SHALL preserve:

```text
Tenant
User
Agent
Workflow
Authorization
Policy
Audit Context
```

The alternative server SHALL independently pass authorization and policy checks.

---

## 47. Disaster Recovery

The MCP Server Management subsystem SHALL support recovery of:

* Server metadata.
* Configuration history.
* Policy configuration.
* Version state.
* Access grants.
* Audit metadata.
* Dependency metadata.

Secrets SHALL be recovered only through the approved secrets-management system.

---

## 48. Compliance Requirements

The subsystem SHALL support enterprise compliance controls for:

* Access control.
* Auditability.
* Data isolation.
* Credential management.
* Configuration governance.
* Retention.
* Security monitoring.
* Incident response.

Specific regulatory controls SHALL be configurable according to deployment requirements.

---

## 49. Performance Requirements

The system SHALL be designed for:

```text
High server counts
Large capability catalogs
High concurrent AI agents
High workflow concurrency
High tool execution volume
Multi-tenant workloads
```

Server discovery SHOULD be cacheable.

Authorization decisions MAY be cached only where policy semantics permit and cache invalidation is reliable.

---

## 50. Reliability Requirements

The subsystem SHALL provide:

* Horizontal scalability.
* Persistent queues.
* Retry handling.
* Circuit breakers.
* Idempotency.
* Graceful degradation.
* Health monitoring.
* Configuration recovery.
* Version rollback.
* Dependency tracking.

---

## 51. Security Threat Model

The subsystem SHALL defend against:

```text
Malicious MCP Server
Compromised MCP Provider
Fake MCP Server
Server Endpoint Hijacking
Credential Theft
SSRF
Tool Injection
Prompt Injection
Capability Injection
Privilege Escalation
Cross-Tenant Access
Unauthorized Server Activation
Unauthorized Tool Activation
Configuration Tampering
Replay
Credential Leakage
Data Exfiltration
Runaway AI Access
```

---

## 52. Threat Response

When a server is suspected of compromise:

```text
Detection
   ↓
Risk Classification
   ↓
Block New Requests
   ↓
Isolate Server
   ↓
Revoke / Rotate Credentials
   ↓
Terminate Active Access
   ↓
Notify Administrators
   ↓
Preserve Audit Evidence
   ↓
Investigate
   ↓
Recover / Replace
```

---

## 53. Testing Requirements

## Unit Tests

The platform SHALL test:

* State transitions.
* Authorization.
* Policy evaluation.
* Validation.
* Capability parsing.
* Configuration validation.
* Version comparison.
* Risk classification.
* Rate limiting.
* Quota enforcement.

---

## Integration Tests

The platform SHALL test:

* MCP registration.
* MCP discovery.
* MCP capability synchronization.
* MCP authentication.
* MCP gateway routing.
* Server enablement.
* Server disablement.
* Server upgrades.
* Server rollback.
* Credential rotation.

---

## Security Tests

The platform SHALL test:

* SSRF.
* Cross-tenant access.
* Privilege escalation.
* Credential leakage.
* Tool injection.
* Prompt injection.
* Malicious server metadata.
* Unauthorized server activation.
* Unauthorized capability exposure.

---

## Failure Tests

The platform SHALL test:

* Server outage.
* DNS failure.
* Network failure.
* Authentication failure.
* Timeout.
* Protocol mismatch.
* Capability drift.
* Rate limiting.
* Provider failure.
* Worker failure.

---

## 54. Acceptance Criteria

The MCP Server Management subsystem SHALL be considered production-ready only when:

* [ ] MCP servers can be registered.
* [ ] Server registration is tenant-aware.
* [ ] Server validation is implemented.
* [ ] MCP protocol compatibility is validated.
* [ ] Capabilities are discovered.
* [ ] Tools are cataloged.
* [ ] Resources are cataloged.
* [ ] Prompts are cataloged.
* [ ] Server approval is implemented.
* [ ] AI access requests are implemented.
* [ ] Human approval is implemented.
* [ ] Server activation is policy-controlled.
* [ ] Server disablement is implemented.
* [ ] Emergency shutdown is implemented.
* [ ] Server health monitoring is implemented.
* [ ] Capability drift detection is implemented.
* [ ] Server versioning is implemented.
* [ ] Rollback is implemented.
* [ ] Configuration history is implemented.
* [ ] Credential isolation is implemented.
* [ ] Credential rotation is supported.
* [ ] RBAC is enforced.
* [ ] Tenant isolation is tested.
* [ ] AI permissions are bounded.
* [ ] Tool-level permissions are implemented.
* [ ] Resource-level permissions are implemented.
* [ ] Prompt-level permissions are implemented.
* [ ] Rate limiting is implemented.
* [ ] Quotas are implemented.
* [ ] Circuit breakers are implemented.
* [ ] Audit logging is implemented.
* [ ] Distributed tracing is implemented.
* [ ] Security events are monitored.
* [ ] Dependency analysis is implemented.
* [ ] Upgrade impact analysis is implemented.
* [ ] Decommissioning is implemented.
* [ ] Disaster recovery is tested.

---

## 55. Golden Rules

1. **An MCP server SHALL never become executable merely because it is registered.**
2. **Registration SHALL NOT imply approval.**
3. **Approval SHALL NOT automatically imply tenant access.**
4. **Tenant access SHALL NOT automatically imply AI access.**
5. **AI recommendation SHALL never constitute authorization.**
6. **AI Agents SHALL never approve their own MCP server requests.**
7. **AI Agents SHALL never grant themselves MCP permissions.**
8. **Every MCP server SHALL have an explicit lifecycle state.**
9. **Every production server SHALL pass required validation before activation.**
10. **Every server SHALL be independently monitored.**
11. **Every server configuration change SHALL be auditable.**
12. **Every capability change SHALL be detectable.**
13. **New high-risk capabilities SHALL not automatically become executable.**
14. **Credentials SHALL never enter AI context.**
15. **Secrets SHALL never appear in logs.**
16. **Every production request SHALL pass through the MCP Gateway.**
17. **Tenant isolation SHALL be enforced server-side.**
18. **Human approval SHALL remain mandatory for configured high-impact operations.**
19. **Server-side authorization SHALL override AI decisions.**
20. **External MCP content SHALL be treated as untrusted.**
21. **MCP server failures SHALL not silently produce successful operations.**
22. **Retries SHALL not blindly repeat irreversible operations.**
23. **Production upgrades SHALL support validation and rollback.**
24. **Server decommissioning SHALL perform dependency analysis first.**
25. **Emergency server isolation SHALL always be available to authorized administrators.**
26. **Historical audit records SHALL survive server disablement and decommissioning.**
27. **AI autonomy SHALL always remain bounded by SalesGenie policy.**
28. **Human and AI operations SHALL use the same server-side security boundary.**
29. **No MCP server SHALL be trusted solely because it is listed in the marketplace.**
30. **No MCP capability SHALL be executable solely because it is discoverable.**
31. **MCP Server Management SHALL be a control plane; MCP execution SHALL remain a separately governed data plane.**
