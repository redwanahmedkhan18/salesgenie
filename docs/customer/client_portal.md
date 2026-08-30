# SalesGenie — Client Portal

## User Requirements, System Requirements & Functional Requirements

### FAANG-Level Enterprise Specification

**Document:** `client_portal.md`  
**Product:** SalesGenie / FlowMind AI  
**Document Type:** Product + System + Functional Requirements  
**Scope:** External Client Portal  
**Architecture:** Multi-Tenant Enterprise SaaS + Microservices + Event-Driven + Multi-Agent AI  
**Interfaces:** Web + Mobile-ready APIs  
**Actors:** External Client, Client User, Organization Owner, Organization Admin, Sales/Marketing/Support Users, AI Agents, Platform Admin, Security Admin, Billing Admin

---

## 1. Purpose

The SalesGenie Client Portal is the secure, multi-tenant customer-facing interface through which external clients interact with SalesGenie services, monitor business activity, consume AI capabilities, manage approved users and resources, review AI-generated outputs, access reports, manage integrations, communicate with support teams, and monitor subscription usage.

The Client Portal MUST provide a controlled abstraction layer between external clients and internal SalesGenie administrative infrastructure.

External clients MUST NOT receive direct access to:

- Super Admin functionality
- Platform Admin functionality
- Internal operational tools
- Internal tenant-management controls
- Security administration
- Internal service infrastructure
- Other organizations' data
- Internal AI system configuration
- Internal databases
- Internal observability systems
- Internal secrets
- Other clients' billing information
- Platform-wide analytics

---

## 2. Product Goals

The Client Portal SHALL:

1. Provide secure client access to SalesGenie.
2. Enforce strict tenant isolation.
3. Provide role-based and permission-based access.
4. Provide organization/workspace visibility.
5. Provide sales, marketing, SEO, advertising, analytics and support capabilities according to entitlements.
6. Provide controlled AI-agent interaction.
7. Provide human-AI collaboration.
8. Provide client-facing dashboards.
9. Provide AI-generated business insights.
10. Provide reports and exports.
11. Provide subscription and usage visibility.
12. Provide integration management.
13. Provide notifications.
14. Provide support access.
15. Provide audit visibility appropriate for the client.
16. Provide approval workflows for AI-generated actions.
17. Protect client data using enterprise security controls.
18. Support scalable asynchronous operations.
19. Provide a consistent web application experience.
20. Expose all necessary functionality through backend APIs rather than frontend-only logic.

---

## 3. Actors

## 3.1 External Client

The primary customer organization using SalesGenie.

Capabilities depend on organization subscription, role and permissions.

## 3.2 Client Owner

Responsible for the client organization's SalesGenie account.

Can manage:

- Organization settings
- Users
- Workspaces
- Billing
- Integrations
- AI agents
- Reports
- Permissions
- Subscription
- Security settings

subject to entitlement and platform policies.

## 3.3 Client Admin

Manages operational configuration within the client organization.

## 3.4 Client User

Consumes SalesGenie functionality according to assigned permissions.

## 3.5 Client Viewer

Read-only access to permitted dashboards, reports and resources.

## 3.6 Client Analyst

Accesses analytics, reporting, dashboards and business intelligence.

## 3.7 Client Sales User

Accesses sales and lead-generation functionality.

## 3.8 Client Marketing User

Accesses marketing and advertising functionality.

## 3.9 Client Support User

Accesses support functionality.

## 3.10 AI Agent

Performs authorized AI operations on behalf of the client.

## 3.11 Human Reviewer

Reviews AI-generated decisions or actions when human approval is required.

---

## 4. Client Portal Scope

The Client Portal SHOULD provide the following major areas:

```text
Client Portal
│
├── Authentication
├── Dashboard
├── Organization
├── Workspaces
├── Users
├── Sales
├── Leads
├── CRM
├── Marketing
├── Advertising
├── SEO
├── Product Launch Intelligence
├── Business Intelligence
├── Analytics
├── AI Agents
├── AI Conversations
├── Human Review
├── Knowledge Base
├── Workflows
├── Integrations
├── Reports
├── Notifications
├── Support
├── Billing
├── Usage
├── Security
├── Audit
├── Settings
└── Help
```

Visibility MUST be dynamically controlled by:

```text
Identity
    +
Organization
    +
Workspace
    +
Role
    +
Permissions
    +
Subscription
    +
Feature Entitlements
    +
Resource Ownership
    +
Policy
```

---

## 5. User Requirements

## UR-001 — Secure Client Authentication

The system SHALL allow external clients to securely authenticate.

The client SHALL be able to:

* Sign in
* Sign out
* Recover password
* Reset password
* Enable MFA
* Verify identity
* Manage sessions
* Review active sessions
* Revoke sessions
* Use supported OAuth providers
* Handle expired sessions

---

## UR-002 — Client Organization Access

The authenticated user SHALL only access organizations for which they have valid membership.

The system SHALL prevent unauthorized organization switching.

---

## UR-003 — Multi-Workspace Access

A client user SHALL be able to access authorized workspaces.

Workspace access SHALL be permission-controlled.

---

## UR-004 — Client Dashboard

The client SHALL receive a personalized dashboard showing permitted:

* KPIs
* Sales metrics
* Lead metrics
* Marketing metrics
* Advertising metrics
* SEO metrics
* Revenue metrics
* Business health
* AI insights
* Recent activities
* Alerts
* Tasks
* Reports
* Usage
* Support status

---

## UR-005 — Personalized Experience

The portal SHALL personalize navigation and dashboards according to:

* User role
* Permissions
* Organization configuration
* Workspace
* Subscription plan
* Feature entitlements
* User preferences

---

## UR-006 — Client User Management

Authorized client administrators SHALL be able to:

* Invite users
* Remove users
* Suspend users
* Reactivate users
* Assign roles
* Assign permissions
* Assign workspaces
* View user activity
* Manage invitations

---

## UR-007 — Organization Management

Authorized users SHALL be able to manage:

* Organization profile
* Organization name
* Logo
* Contact information
* Time zone
* Locale
* Currency
* Business information
* Default workspace
* Organization preferences

---

## UR-008 — Workspace Management

Authorized users SHALL be able to:

* Create workspaces
* Rename workspaces
* Archive workspaces
* Manage workspace members
* Assign permissions
* Configure workspace settings

---

## UR-009 — Sales Management

Authorized users SHALL be able to access:

* Leads
* Prospects
* Contacts
* Accounts
* Opportunities
* Deals
* Sales pipeline
* Sales funnel
* Sales activities
* Lead scoring
* Lead qualification
* Lead enrichment
* Lead routing
* Sales analytics
* Sales forecasting

---

## UR-010 — Lead Generation

Authorized clients SHALL be able to:

* Define ICP
* Search for leads
* Generate lead lists
* Filter prospects
* Score prospects
* Enrich prospects
* Verify prospects
* Segment leads
* Export leads
* Assign leads
* Route leads
* Initiate outreach

---

## UR-011 — AI Lead Generation

Clients SHALL be able to request AI-powered lead discovery.

The AI system MAY:

* Identify potential companies
* Identify potential buyers
* Analyze intent
* Detect buying signals
* Rank prospects
* Recommend prospects
* Explain recommendations

AI-generated lead recommendations SHALL remain subject to client permissions and system policies.

---

## UR-012 — CRM Access

Authorized users SHALL be able to manage:

* Contacts
* Companies
* Accounts
* Opportunities
* Deals
* Activities
* Notes
* Tasks
* Pipeline stages
* CRM relationships

---

## UR-013 — Marketing Access

Authorized users SHALL be able to:

* Create campaigns
* Manage audiences
* Create content
* Schedule campaigns
* Review campaign performance
* Analyze attribution
* Monitor ROI
* Automate marketing workflows

---

## UR-014 — Advertising Management

Authorized users SHALL be able to monitor connected advertising platforms including supported:

* Google Ads
* Facebook Ads
* Instagram Ads
* WhatsApp Ads
* YouTube Ads
* TikTok Ads
* LinkedIn Ads

Capabilities SHALL depend on integration availability and permissions.

---

## UR-015 — Advertising Analytics

The portal SHALL display:

* Spend
* Revenue
* Reach
* Impressions
* Clicks
* Conversions
* CTR
* CPC
* CPA
* ROAS
* ROI
* Audience demographics
* Campaign performance
* Product performance

---

## UR-016 — SEO Management

Authorized users SHALL be able to access:

* SEO audits
* Keyword research
* Keyword tracking
* SERP analysis
* Content gaps
* Competitor SEO
* Backlink analysis
* Ranking data
* SEO analytics
* AI SEO recommendations

---

## UR-017 — Product Launch Intelligence

Clients SHALL be able to submit product information for AI-assisted analysis.

The platform SHALL support:

* Market analysis
* Competitor discovery
* Competitor analysis
* Market trends
* Buyer analysis
* Market gaps
* Opportunity detection
* Risk analysis
* Product positioning
* Go-to-market recommendations

---

## UR-018 — Business Intelligence

Authorized users SHALL be able to monitor:

* Revenue
* Expenses
* Profit
* Loss
* Cash flow
* Product profitability
* Product losses
* Growth
* Business health
* Forecasts

---

## UR-019 — AI Business Advisor

Clients SHALL be able to request AI-generated business insights.

The AI MAY provide:

* Growth recommendations
* Cost optimization
* Product recommendations
* Marketing recommendations
* Sales recommendations
* Risk identification
* Profitability insights
* Forecasts

Recommendations SHALL identify relevant evidence where available.

---

## UR-020 — AI Agent Access

Clients SHALL be able to:

* View authorized AI agents
* Start conversations
* Submit tasks
* View task status
* Review AI outputs
* Approve actions
* Reject actions
* Request revisions
* Stop running agents
* View permitted agent history

---

## UR-021 — AI Agent Execution

AI agents SHALL only execute tools and workflows authorized for:

```text
Organization
    +
Workspace
    +
Agent
    +
User
    +
Permission
    +
Policy
```

---

## UR-022 — Human-AI Collaboration

Clients SHALL be able to:

* Review AI outputs
* Approve AI actions
* Reject AI actions
* Modify AI-generated content
* Escalate AI decisions
* Request human support
* Take over conversations
* Return control to AI

---

## UR-023 — Human Review Queue

Authorized reviewers SHALL receive AI tasks requiring human approval.

Each task SHALL provide:

* Request
* AI recommendation
* Confidence
* Evidence
* Proposed action
* Risk
* Required decision
* Deadline
* Audit history

---

## UR-024 — Knowledge Base

Authorized users SHALL be able to:

* Upload documents
* View documents
* Search documents
* Organize knowledge
* Update documents
* Delete documents
* Manage document permissions
* Use knowledge through AI agents

---

## UR-025 — RAG Interaction

AI responses MAY use authorized client knowledge.

The system MUST enforce:

```text
Tenant Isolation
+
Workspace Isolation
+
Document Permissions
+
Retrieval Permissions
```

---

## UR-026 — Workflow Automation

Clients SHALL be able to:

* Create workflows
* Configure triggers
* Configure actions
* Add conditions
* Schedule workflows
* Execute workflows
* Pause workflows
* Resume workflows
* View execution history
* Review failures

---

## UR-027 — Integration Management

Authorized clients SHALL be able to:

* Connect integrations
* Authenticate integrations
* Disconnect integrations
* Reauthorize integrations
* Test connections
* View integration status
* Configure synchronization
* View synchronization errors

---

## UR-028 — Reporting

Clients SHALL be able to:

* View reports
* Generate reports
* Schedule reports
* Customize reports
* Export reports
* Share authorized reports

Supported formats SHOULD include:

* XLSX
* CSV
* PDF
* JSON

---

## UR-029 — Dashboard Customization

Authorized clients SHALL be able to:

* Add widgets
* Remove widgets
* Reorder widgets
* Configure widgets
* Save dashboards
* Create multiple dashboards
* Set default dashboards

---

## UR-030 — Notifications

Clients SHALL receive notifications for:

* AI events
* Human review
* Workflow failures
* Lead events
* Campaign events
* Integration failures
* Billing events
* Security events
* Support events
* System events

---

## UR-031 — Support

Clients SHALL be able to:

* Create support tickets
* View tickets
* Reply to tickets
* Attach files
* Track ticket status
* Request human assistance
* View support history

---

## UR-032 — Billing

Authorized users SHALL be able to view:

* Subscription
* Current plan
* Usage
* Limits
* Billing cycle
* Invoices
* Payment status
* Credits
* Add-ons

---

## UR-033 — Subscription Management

Authorized users SHALL be able to:

* Upgrade
* Downgrade
* Renew
* Cancel
* Resume
* Change billing cycle
* View plan entitlements

---

## UR-034 — Usage Monitoring

The client SHALL be able to monitor:

* AI usage
* Token usage
* API usage
* Lead usage
* Storage usage
* Workflow executions
* Agent executions
* Integration usage
* Report generation usage

---

## UR-035 — Client Audit Visibility

Authorized users SHALL be able to view permitted audit events including:

* Login
* Logout
* User changes
* Permission changes
* AI actions
* Approvals
* Rejections
* Integration changes
* Billing events
* Security events

Sensitive internal security information MUST NOT be exposed.

---

## UR-036 — Security Management

Authorized users SHALL be able to manage:

* MFA
* Password
* Sessions
* Login security
* Trusted devices
* Security notifications

---

## UR-037 — Localization

Clients SHALL be able to configure:

* Language
* Time zone
* Date format
* Number format
* Currency
* Regional preferences

---

## UR-038 — Accessibility

The portal SHALL support accessible interaction using:

* Keyboard navigation
* Screen readers
* Accessible labels
* Focus management
* Appropriate contrast
* Reduced-motion preferences

---

## UR-039 — Mobile Compatibility

The portal SHALL provide responsive experiences for:

* Desktop
* Tablet
* Mobile

Critical workflows SHALL remain usable on mobile devices.

---

## 6. System Requirements

## SR-001 — Multi-Tenant Architecture

The Client Portal MUST operate within a strict multi-tenant architecture.

Every request SHALL resolve:

```text
User
↓
Organization
↓
Workspace
↓
Resource
↓
Permission
↓
Entitlement
↓
Policy
```

---

## SR-002 — Tenant Isolation

The backend MUST enforce tenant isolation independently of frontend controls.

The frontend MUST NOT be considered a security boundary.

---

## SR-003 — Authorization Enforcement

Authorization MUST be enforced server-side.

The system SHALL support:

* RBAC
* ABAC
* Resource-level authorization
* Workspace-level authorization
* Organization-level authorization
* Feature entitlements

---

## SR-004 — API-First Architecture

Every backend-connected feature SHALL have a corresponding API contract.

Frontend components MUST NOT directly access:

* Databases
* Internal service credentials
* Internal microservice endpoints
* Secrets
* Infrastructure APIs

---

## SR-005 — API Gateway

Client requests SHOULD pass through an API gateway or controlled edge layer.

```text
Client
  ↓
Frontend
  ↓
API Gateway
  ↓
Authentication
  ↓
Authorization
  ↓
Service Routing
  ↓
Microservices
```

---

## SR-006 — Backend Service Integration

The portal SHALL integrate with relevant SalesGenie services including:

```text
Auth Service
Organization Service
User Service
RBAC Service
Sales Service
Lead Intelligence Service
CRM Service
Marketing Service
Advertising Service
SEO Service
Analytics Service
AI Gateway
Agent Service
RAG Service
Knowledge Service
Workflow Service
Integration Service
Notification Service
Reporting Service
Billing Service
Support Service
Audit Service
```

---

## SR-007 — API Security

All APIs SHALL implement:

* Authentication
* Authorization
* Rate limiting
* Input validation
* Output validation
* Request correlation
* Audit logging
* Abuse protection

---

## SR-008 — Session Security

Sessions SHALL support:

* Secure token handling
* Expiration
* Refresh
* Revocation
* Concurrent session management
* Device tracking
* Session anomaly detection

---

## SR-009 — Feature Entitlement Enforcement

Frontend feature visibility SHALL be driven by backend-provided entitlements.

Example:

```json
{
  "feature": "ai_lead_generation",
  "enabled": true,
  "quota": 10000,
  "used": 3240
}
```

Frontend visibility MUST NOT replace backend authorization.

---

## SR-010 — Subscription Enforcement

Backend services SHALL enforce subscription limitations.

Example:

```text
Free
 ├── Limited AI usage
 ├── Limited leads
 ├── Limited storage
 └── Limited integrations

Monthly
 ├── Expanded limits
 └── Additional features

Yearly
 ├── Expanded limits
 ├── Additional features
 └── Premium capabilities
```

---

## SR-011 — Asynchronous Processing

Long-running operations SHALL use asynchronous jobs.

Examples:

* Lead discovery
* Lead enrichment
* Market analysis
* AI analysis
* Report generation
* Excel generation
* Data synchronization
* RAG ingestion
* Workflow execution

---

## SR-012 — Job Status

The frontend SHALL receive job states:

```text
QUEUED
RUNNING
WAITING_FOR_APPROVAL
SUCCEEDED
FAILED
CANCELLED
EXPIRED
```

---

## SR-013 — Real-Time Communication

The portal SHOULD support:

* WebSockets
* Server-Sent Events
* Event streams
* Push notifications

for real-time:

* AI execution
* Agent events
* Workflow execution
* Support messages
* Notifications
* Human handoffs

---

## SR-014 — Event-Driven Architecture

Important client events SHOULD be published through an event bus.

Example:

```text
lead.created
lead.updated
lead.scored
campaign.created
campaign.completed
agent.started
agent.completed
agent.failed
approval.requested
approval.approved
approval.rejected
workflow.started
workflow.failed
integration.connected
integration.failed
billing.payment_succeeded
support.ticket_created
```

---

## SR-015 — Caching

The platform SHOULD cache:

* Dashboard summaries
* Feature entitlements
* User permissions
* Organization metadata
* Static configuration

Sensitive data MUST follow appropriate cache isolation.

---

## SR-016 — Data Consistency

The system SHALL distinguish:

* Strongly consistent operations
* Eventually consistent analytics
* Cached data
* Real-time data

The UI SHALL display data freshness where meaningful.

---

## SR-017 — Idempotency

Backend operations involving state changes SHOULD support idempotency.

Especially:

* Payments
* User invitations
* Integration creation
* Workflow execution
* AI actions
* Lead creation
* Campaign execution

---

## SR-018 — Auditability

Every security-sensitive client action SHALL generate an auditable event.

---

## SR-019 — Observability

Client portal requests SHALL generate:

* Metrics
* Logs
* Distributed traces
* Error events
* Performance telemetry

with tenant-safe identifiers.

---

## SR-020 — Reliability

The Client Portal SHALL tolerate:

* Service failures
* API timeouts
* Network interruptions
* Partial failures
* AI provider failures
* Integration failures

without exposing internal infrastructure details.

---

## 7. Functional Requirements

## 7.1 Authentication

## FR-AUTH-001

The frontend SHALL provide a login interface.

## FR-AUTH-002

The frontend SHALL submit authentication requests to the authentication backend.

## FR-AUTH-003

The backend SHALL validate credentials.

## FR-AUTH-004

The system SHALL support MFA challenges.

## FR-AUTH-005

The frontend SHALL handle authentication states:

```text
UNAUTHENTICATED
AUTHENTICATING
MFA_REQUIRED
AUTHENTICATED
SESSION_EXPIRED
SESSION_REVOKED
ACCOUNT_LOCKED
```

---

## 7.2 Organization

## FR-ORG-001

The frontend SHALL request organization metadata from the backend.

## FR-ORG-002

The frontend SHALL display only organizations returned by the authorization service.

## FR-ORG-003

Organization switching SHALL trigger a backend authorization context update.

## FR-ORG-004

The system SHALL invalidate unauthorized cached organization data after switching.

---

## 7.3 Workspace

## FR-WORKSPACE-001

Users SHALL be able to list authorized workspaces.

## FR-WORKSPACE-002

Users SHALL be able to switch workspaces.

## FR-WORKSPACE-003

Workspace switching SHALL update:

* API context
* Permissions
* Dashboard
* Navigation
* Data queries
* AI context

---

## 7.4 Dashboard

## FR-DASH-001

Dashboard widgets SHALL load data through backend APIs.

## FR-DASH-002

Widgets SHALL support:

* Loading
* Success
* Empty
* Error
* Stale
* Unauthorized states.

## FR-DASH-003

Dashboard data SHALL support date ranges.

## FR-DASH-004

Dashboard filters SHALL be persisted where permitted.

## FR-DASH-005

Dashboard configuration SHALL be stored server-side for synchronized access.

---

## 7.5 Sales

## FR-SALES-001

The portal SHALL provide lead lists backed by the lead service.

## FR-SALES-002

Users SHALL be able to search leads.

## FR-SALES-003

Users SHALL be able to filter leads.

## FR-SALES-004

Users SHALL be able to view lead intelligence.

## FR-SALES-005

Users SHALL be able to view lead scores.

## FR-SALES-006

Users SHALL be able to assign authorized leads.

## FR-SALES-007

Users SHALL be able to update lead status.

---

## 7.6 AI Lead Generation

## FR-AILEAD-001

Users SHALL be able to submit lead-generation requests.

## FR-AILEAD-002

The backend SHALL create an asynchronous generation job.

## FR-AILEAD-003

The frontend SHALL display job progress.

## FR-AILEAD-004

Generated leads SHALL be persisted through the lead service.

## FR-AILEAD-005

Generated results SHALL be tenant-scoped.

---

## 7.7 CRM

## FR-CRM-001

Users SHALL be able to create authorized CRM records.

## FR-CRM-002

Users SHALL be able to update CRM records.

## FR-CRM-003

Users SHALL be able to delete records where permitted.

## FR-CRM-004

CRM actions SHALL generate audit events.

---

## 7.8 Marketing

## FR-MKT-001

Users SHALL be able to create marketing campaigns.

## FR-MKT-002

Campaign creation SHALL be persisted through the marketing service.

## FR-MKT-003

Campaign execution SHALL require appropriate permission.

## FR-MKT-004

High-risk campaigns MAY require human approval.

---

## 7.9 Advertising

## FR-ADS-001

The portal SHALL display connected advertising accounts.

## FR-ADS-002

The frontend SHALL retrieve campaign metrics through backend APIs.

## FR-ADS-003

Advertising write actions SHALL require explicit authorization.

## FR-ADS-004

The system SHALL prevent unauthorized advertising-account access.

---

## 7.10 SEO

## FR-SEO-001

Users SHALL be able to submit SEO analysis jobs.

## FR-SEO-002

The backend SHALL process SEO analysis asynchronously where necessary.

## FR-SEO-003

Results SHALL be persisted and associated with the correct organization/workspace.

---

## 7.11 Product Launch Intelligence

## FR-PLI-001

Users SHALL be able to create product analysis projects.

## FR-PLI-002

Users SHALL be able to submit product information.

## FR-PLI-003

The AI system SHALL generate analysis jobs.

## FR-PLI-004

The portal SHALL display:

* Market findings
* Competitors
* Opportunities
* Risks
* Recommendations

---

## 7.12 Analytics

## FR-AN-001

Analytics dashboards SHALL retrieve data from analytics APIs.

## FR-AN-002

Users SHALL be able to configure:

* Date range
* Filters
* Dimensions
* Metrics

subject to permissions.

## FR-AN-003

Analytics responses SHALL identify data freshness where applicable.

---

## 7.13 AI Agents

## FR-AGENT-001

The portal SHALL list authorized agents.

## FR-AGENT-002

The portal SHALL retrieve agent metadata from the agent service.

## FR-AGENT-003

Users SHALL be able to start authorized agents.

## FR-AGENT-004

Agent execution SHALL generate a backend execution ID.

## FR-AGENT-005

Frontend SHALL subscribe to agent execution status.

## FR-AGENT-006

Users SHALL be able to stop agents where permitted.

---

## 7.14 Agent Tools

The backend SHALL determine which tools an agent can use.

The frontend SHALL NOT independently grant tool permissions.

Example:

```text
Agent
 ↓
Policy Engine
 ↓
Tool Authorization
 ↓
Tool Execution
 ↓
Audit Event
```

---

## 7.15 AI Conversations

## FR-CONV-001

Users SHALL be able to create AI conversations.

## FR-CONV-002

Conversation history SHALL be stored server-side.

## FR-CONV-003

Conversation access SHALL be tenant and permission scoped.

## FR-CONV-004

The frontend SHALL support streaming AI responses.

## FR-CONV-005

The frontend SHALL display AI execution states.

---

## 7.16 Human Handoff

## FR-HANDOFF-001

AI SHALL be able to request human intervention.

## FR-HANDOFF-002

The backend SHALL create a human-review task.

## FR-HANDOFF-003

Authorized humans SHALL receive the task.

## FR-HANDOFF-004

The client SHALL see handoff status where appropriate.

---

## 7.17 Human Approval

## FR-APPROVAL-001

The system SHALL create approval requests for configured AI actions.

## FR-APPROVAL-002

Reviewers SHALL see:

* Action
* Context
* AI reasoning summary
* Evidence
* Confidence
* Risk
* Proposed changes

## FR-APPROVAL-003

Reviewers SHALL be able to:

* Approve
* Reject
* Modify
* Request revision

## FR-APPROVAL-004

Approval decisions SHALL be persisted and audited.

---

## 7.18 Knowledge Base

## FR-KB-001

Users SHALL be able to upload authorized documents.

## FR-KB-002

Uploads SHALL be sent to backend document ingestion services.

## FR-KB-003

The system SHALL display ingestion status.

```text
UPLOADED
PROCESSING
CHUNKING
EMBEDDING
INDEXING
READY
FAILED
```

## FR-KB-004

Documents SHALL inherit appropriate organization/workspace permissions.

---

## 7.19 Workflow Automation

## FR-WF-001

Users SHALL be able to create workflows.

## FR-WF-002

Workflow definitions SHALL be stored by the workflow service.

## FR-WF-003

Workflow execution SHALL occur server-side.

## FR-WF-004

Frontend SHALL display execution status.

## FR-WF-005

Workflow failures SHALL be visible to authorized users.

---

## 7.20 Integrations

## FR-INT-001

Users SHALL be able to view available integrations.

## FR-INT-002

Users SHALL be able to initiate OAuth authorization.

## FR-INT-003

OAuth callbacks SHALL be processed by backend services.

## FR-INT-004

Access tokens SHALL NEVER be exposed to frontend application storage.

## FR-INT-005

Users SHALL be able to disconnect integrations.

## FR-INT-006

Users SHALL be able to test integrations.

## FR-INT-007

Integration failures SHALL be displayed with actionable remediation.

---

## 7.21 Reporting

## FR-REPORT-001

Users SHALL be able to generate reports.

## FR-REPORT-002

Large report generation SHALL execute asynchronously.

## FR-REPORT-003

Frontend SHALL display report generation status.

## FR-REPORT-004

Generated reports SHALL be securely stored.

## FR-REPORT-005

Downloads SHALL use authorized, time-limited access.

---

## 7.22 Excel Reporting

## FR-EXCEL-001

Users SHALL be able to request XLSX reports.

## FR-EXCEL-002

The reporting backend SHALL generate the XLSX file.

## FR-EXCEL-003

The generated file SHALL be associated with the requesting organization.

## FR-EXCEL-004

Unauthorized users SHALL be denied download access.

---

## 7.23 Notifications

## FR-NOTIFY-001

The backend SHALL create notification events.

## FR-NOTIFY-002

The frontend SHALL retrieve unread notifications.

## FR-NOTIFY-003

Users SHALL be able to mark notifications as read.

## FR-NOTIFY-004

Users SHALL be able to configure notification preferences.

---

## 7.24 Support

## FR-SUPPORT-001

Users SHALL be able to create support tickets.

## FR-SUPPORT-002

Tickets SHALL be persisted through the support service.

## FR-SUPPORT-003

Users SHALL be able to view only authorized tickets.

## FR-SUPPORT-004

Ticket messages SHALL support asynchronous updates.

---

## 7.25 Billing

## FR-BILL-001

Authorized users SHALL be able to retrieve subscription information.

## FR-BILL-002

Users SHALL be able to retrieve invoices.

## FR-BILL-003

Billing actions SHALL be processed exclusively by the billing backend.

## FR-BILL-004

Payment credentials SHALL NOT be stored in the frontend.

---

## 7.26 Usage

## FR-USAGE-001

The frontend SHALL retrieve usage metrics from the billing/usage service.

## FR-USAGE-002

Usage SHALL be displayed by:

* Feature
* Period
* Current usage
* Limit
* Remaining quota

## FR-USAGE-003

The system SHALL display approaching quota limits.

---

## 7.27 Audit

## FR-AUDIT-001

Authorized users SHALL be able to retrieve client-visible audit events.

## FR-AUDIT-002

Audit events SHALL be immutable.

## FR-AUDIT-003

Users SHALL be unable to modify audit history.

---

## 7.28 Security

## FR-SEC-001

Users SHALL be able to change passwords.

## FR-SEC-002

Users SHALL be able to configure MFA.

## FR-SEC-003

Users SHALL be able to view active sessions.

## FR-SEC-004

Users SHALL be able to revoke sessions.

## FR-SEC-005

Security-sensitive changes SHALL require re-authentication where configured.

---

## 7.29 Localization

## FR-I18N-001

Frontend locale SHALL be synchronized with supported backend preferences.

## FR-I18N-002

User locale preferences SHALL be persisted server-side.

## FR-I18N-003

Organization locale defaults SHALL be available through configuration APIs.

---

## 7.30 Error Handling

The frontend SHALL distinguish:

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Validation Error
429 Rate Limited
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

The UI SHALL present safe user-facing messages without leaking internal errors.

---

## 8. Frontend ↔ Backend Contract

Every backend-connected frontend feature SHALL follow:

```text
UI Component
    ↓
Client State
    ↓
API Client
    ↓
API Gateway
    ↓
Authentication
    ↓
Authorization
    ↓
Service
    ↓
Database / Queue / AI / Integration
    ↓
Response / Event
    ↓
API Client
    ↓
State Update
    ↓
UI
```

---

## 9. Required API Domains

The Client Portal SHOULD consume APIs covering:

```text
/api/v1/auth/*
/api/v1/me/*
/api/v1/organizations/*
/api/v1/workspaces/*
/api/v1/users/*
/api/v1/permissions/*
/api/v1/dashboard/*
/api/v1/leads/*
/api/v1/crm/*
/api/v1/sales/*
/api/v1/marketing/*
/api/v1/advertising/*
/api/v1/seo/*
/api/v1/product-launch/*
/api/v1/analytics/*
/api/v1/ai/*
/api/v1/agents/*
/api/v1/conversations/*
/api/v1/approvals/*
/api/v1/reviews/*
/api/v1/knowledge/*
/api/v1/rag/*
/api/v1/workflows/*
/api/v1/integrations/*
/api/v1/reports/*
/api/v1/notifications/*
/api/v1/support/*
/api/v1/billing/*
/api/v1/usage/*
/api/v1/security/*
/api/v1/audit/*
/api/v1/settings/*
```

Exact endpoint naming MAY differ according to the final API architecture.

---

## 10. Frontend State Requirements

The frontend SHALL distinguish:

## Server State

Examples:

* Users
* Leads
* Campaigns
* Analytics
* Agents
* Conversations
* Reports
* Billing
* Integrations

## Client State

Examples:

* Modal visibility
* Sidebar state
* Selected filters
* Temporary form state
* UI preferences

## Authentication State

Examples:

* User
* Organization
* Workspace
* Token/session state
* Permissions
* Entitlements

Server state MUST NOT be duplicated unnecessarily into independent client stores.

---

## 11. Security Requirements

## SEC-001

All communication SHALL use HTTPS/TLS.

## SEC-002

Authorization SHALL be enforced server-side.

## SEC-003

Tenant identifiers SHALL NOT be trusted solely from client-provided input.

## SEC-004

The backend SHALL derive authorized tenant context from authenticated identity.

## SEC-005

Frontend routes SHALL be protected.

## SEC-006

Backend APIs SHALL remain protected even if frontend route guards are bypassed.

## SEC-007

Sensitive tokens SHALL not be stored in insecure browser storage.

## SEC-008

CSRF protection SHALL be applied where applicable.

## SEC-009

Content Security Policy SHALL be configured.

## SEC-010

Security-sensitive events SHALL be audited.

---

## 12. AI Security Requirements

AI agents operating through the Client Portal SHALL enforce:

```text
Identity
 ↓
Tenant
 ↓
Workspace
 ↓
Agent
 ↓
Tool Permission
 ↓
Data Permission
 ↓
Policy
 ↓
Guardrails
 ↓
Execution
```

The system SHALL defend against:

* Prompt injection
* Data exfiltration
* Cross-tenant retrieval
* Unauthorized tool use
* Excessive agency
* Malicious uploaded documents
* Indirect prompt injection
* Unauthorized external actions

---

## 13. AI Action Risk Classification

AI actions SHALL be classified as:

```text
LOW RISK
    ↓
AI executes automatically

MEDIUM RISK
    ↓
AI executes with monitoring or optional review

HIGH RISK
    ↓
Human approval required

CRITICAL RISK
    ↓
Human authorization + additional policy checks
```

Examples of high-risk operations MAY include:

* Sending external communications
* Changing advertising budgets
* Publishing campaigns
* Executing financial operations
* Deleting business data
* Changing security configuration
* Changing user permissions

---

## 14. Data Requirements

Every client resource SHALL contain appropriate ownership metadata.

Example:

```json
{
  "id": "resource-id",
  "organization_id": "org-id",
  "workspace_id": "workspace-id",
  "created_by": "user-id",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

The exact schema SHALL follow the centralized data architecture.

---

## 15. Data Isolation

The platform MUST enforce:

```text
Organization A
    ├── Workspace A1
    └── Workspace A2

Organization B
    ├── Workspace B1
    └── Workspace B2
```

A request originating from Organization A MUST NEVER retrieve Organization B data.

---

## 16. Client Portal Navigation

Recommended navigation:

```text
Home
│
├── Dashboard
│
├── Sales
│   ├── Leads
│   ├── Prospects
│   ├── Contacts
│   ├── Accounts
│   ├── Opportunities
│   ├── Deals
│   └── Pipeline
│
├── Marketing
│   ├── Campaigns
│   ├── Audiences
│   ├── Content
│   └── Analytics
│
├── Advertising
│   ├── Campaigns
│   ├── Spend
│   ├── ROI
│   └── Audience
│
├── SEO
│   ├── Audit
│   ├── Keywords
│   ├── Rankings
│   └── Competitors
│
├── Intelligence
│   ├── Product Launch
│   ├── Market Intelligence
│   ├── Competitor Intelligence
│   └── Business Intelligence
│
├── AI
│   ├── Agents
│   ├── Conversations
│   ├── Tasks
│   └── Reviews
│
├── Knowledge
│   ├── Documents
│   ├── Knowledge Base
│   └── Search
│
├── Automation
│   ├── Workflows
│   ├── Executions
│   └── Templates
│
├── Analytics
│   ├── Business
│   ├── Sales
│   ├── Marketing
│   ├── Advertising
│   └── SEO
│
├── Reports
│
├── Integrations
│
├── Support
│
├── Billing
│
└── Settings
```

Navigation visibility SHALL be dynamically determined by backend authorization and entitlements.

---

## 17. Performance Requirements

The portal SHALL:

* Lazy-load non-critical modules.
* Cache safe read-heavy data.
* Paginate large datasets.
* Virtualize large tables.
* Debounce search.
* Cancel obsolete API requests.
* Use asynchronous processing for expensive operations.
* Stream AI responses where appropriate.
* Avoid blocking the main thread.
* Support resilient retries.

---

## 18. Scalability Requirements

The Client Portal architecture SHALL support:

* Millions of client users
* Large organizations
* Multiple workspaces
* High API concurrency
* Large lead datasets
* Large analytics datasets
* Concurrent AI tasks
* Concurrent report generation
* High-volume notifications

The frontend SHALL remain stateless wherever practical.

---

## 19. Reliability Requirements

The Client Portal SHALL gracefully handle:

```text
API timeout
Service unavailable
AI provider failure
Integration failure
Database failure
Queue delay
Network interruption
Expired authentication
Permission changes
Subscription expiration
Rate limiting
Partial data availability
```

---

## 20. Observability Requirements

Every major request SHOULD include:

```text
request_id
trace_id
user_id
organization_id
workspace_id
service
operation
timestamp
```

Sensitive personal or secret information MUST NOT be logged.

---

## 21. Accessibility Requirements

The Client Portal SHALL target WCAG 2.2 AA.

Requirements include:

* Keyboard navigation
* Screen-reader compatibility
* Semantic HTML
* Focus management
* Accessible forms
* Accessible error messages
* Accessible dialogs
* Sufficient contrast
* Reduced motion
* Accessible data tables
* Accessible charts with textual alternatives

---

## 22. Audit Requirements

The system SHALL audit:

```text
Authentication
User management
Role changes
Permission changes
Organization changes
Workspace changes
Integration changes
AI actions
Agent executions
Approvals
Rejections
Workflow executions
Data deletion
Exports
Billing operations
Security changes
```

---

## 23. API Failure Recovery

The frontend SHALL implement:

```text
Request
  ↓
Failure?
  ├── Retryable → Retry with backoff
  ├── 401 → Refresh/re-authenticate
  ├── 403 → Permission UI
  ├── 404 → Not-found state
  ├── 409 → Conflict resolution
  ├── 429 → Rate-limit handling
  ├── 5xx → Retry/fallback
  └── Network → Offline/retry state
```

---

## 24. Offline / Degraded Mode

Where practical, the portal SHOULD support limited degraded experiences:

* Cached navigation
* Cached preferences
* Draft preservation
* Retry queues
* Read-only cached data

The system MUST NOT perform unauthorized or unsafe mutations while offline.

---

## 25. Feature Flag Requirements

Client Portal functionality SHALL support server-controlled feature flags.

Example:

```json
{
  "feature": "product_launch_intelligence",
  "enabled": true,
  "rollout_percentage": 100,
  "organization_allowed": true
}
```

---

## 26. Subscription-Gated UI

The frontend SHALL display appropriate states:

```text
AVAILABLE
AVAILABLE_WITH_QUOTA
UPGRADE_REQUIRED
TRIAL
LIMIT_REACHED
FEATURE_DISABLED
ADMIN_ONLY
NOT_AUTHORIZED
```

Backend enforcement remains authoritative.

---

## 27. Empty-State Requirements

Every major backend-connected resource SHALL define:

* Empty state
* Loading state
* Error state
* Permission state
* Subscription state
* Stale-data state

Example:

```text
No Leads Found
     ↓
Create Lead
     OR
Generate Leads with AI
```

---

## 28. Confirmation Requirements

Destructive or high-risk actions SHALL require appropriate confirmation.

Examples:

* Delete user
* Delete integration
* Delete knowledge
* Delete workflow
* Cancel subscription
* Publish campaign
* Send bulk outreach
* Change permissions
* Execute high-risk AI action

---

## 29. Human-AI Transparency

The Client Portal SHALL clearly distinguish:

```text
Human Generated
AI Generated
AI Assisted
AI Recommended
Human Approved
Automatically Executed
```

AI-generated information SHOULD expose relevant:

* Confidence
* Sources
* Evidence
* Timestamp
* Model/version where appropriate

---

## 30. Client Data Export

Authorized clients SHOULD be able to export permitted business data.

Exports SHALL be:

* Authenticated
* Authorized
* Audited
* Tenant-scoped
* Time-limited
* Rate-limited

---

## 31. Client Data Deletion

Authorized users SHALL be able to initiate permitted deletion requests.

Deletion SHALL:

1. Validate authorization.
2. Create deletion job where necessary.
3. Apply retention policies.
4. Delete eligible data.
5. Propagate deletion to dependent systems.
6. Record audit events.
7. Notify authorized users.

---

## 32. Notification Routing

Notifications SHALL be routed according to:

```text
Event
 ↓
Notification Policy
 ↓
User Preferences
 ↓
Severity
 ↓
Channel
 ├── In-App
 ├── Email
 ├── SMS
 └── Push
```

---

## 33. Search Requirements

The portal SHALL support:

* Global search
* Lead search
* CRM search
* Knowledge search
* Workflow search
* Agent search
* Report search

Search results SHALL respect authorization.

---

## 34. Backend Authorization Matrix

Example:

| Resource     | Viewer |        User | Manager | Admin | Owner |
| ------------ | -----: | ----------: | ------: | ----: | ----: |
| Dashboard    |   Read |        Read |    Read |  Read |  Read |
| Leads        |   Read |        CRUD |    CRUD |  CRUD |  CRUD |
| CRM          |   Read |        CRUD |    CRUD |  CRUD |  CRUD |
| Users        |     No |          No | Limited |  CRUD |  CRUD |
| Billing      |     No |          No |      No |  Read |  CRUD |
| Integrations |     No |     Limited |    CRUD |  CRUD |  CRUD |
| AI Agents    |   Read |     Execute | Execute |  CRUD |  CRUD |
| Workflows    |   Read |     Execute |    CRUD |  CRUD |  CRUD |
| Reports      |   Read | Read/Create |    CRUD |  CRUD |  CRUD |
| Organization |     No |          No | Limited |  CRUD |  CRUD |
| Security     |     No |     Limited | Limited |  CRUD |  CRUD |

The final authorization matrix SHALL be maintained by the centralized authorization system.

---

## 35. Client Portal Backend Dependency Map

```text
CLIENT FRONTEND
      │
      ▼
API GATEWAY
      │
      ├── Auth Service
      ├── Identity Service
      ├── Organization Service
      ├── RBAC/ABAC Service
      │
      ├── Sales Service
      ├── Lead Intelligence
      ├── CRM Service
      │
      ├── Marketing Service
      ├── Advertising Service
      ├── SEO Service
      │
      ├── Product Intelligence
      ├── Analytics Service
      ├── BI Service
      │
      ├── AI Gateway
      ├── Agent Platform
      ├── RAG Platform
      ├── Knowledge Service
      │
      ├── Workflow Engine
      ├── Integration Platform
      │
      ├── Reporting Service
      ├── Notification Service
      ├── Support Service
      │
      ├── Billing Service
      ├── Usage Service
      │
      ├── Audit Service
      └── Security Service
```

---

## 36. Event Architecture

The Client Portal SHOULD consume events such as:

```text
user.invited
user.updated
workspace.updated

lead.created
lead.scored
lead.qualified
lead.assigned

campaign.started
campaign.completed
campaign.failed

agent.started
agent.thinking
agent.tool_called
agent.waiting_for_approval
agent.completed
agent.failed

approval.created
approval.approved
approval.rejected

workflow.started
workflow.completed
workflow.failed

integration.connected
integration.disconnected
integration.sync_failed

report.started
report.completed
report.failed

billing.updated
billing.payment_failed
subscription.changed

support.ticket_created
support.ticket_updated

security.alert
session.revoked
```

---

## 37. Client Portal State Machine

```text
LOGIN
  ↓
AUTHENTICATED
  ↓
ORGANIZATION_SELECTED
  ↓
WORKSPACE_SELECTED
  ↓
ENTITLEMENTS_LOADED
  ↓
PERMISSIONS_LOADED
  ↓
DASHBOARD_READY
  ↓
APPLICATION_ACTIVE
```

Failures SHALL transition into appropriate recovery states.

---

## 38. AI Agent Execution State

```text
REQUESTED
   ↓
AUTHORIZED
   ↓
QUEUED
   ↓
RUNNING
   ↓
├── TOOL_EXECUTION
├── RETRIEVAL
├── MODEL_INFERENCE
├── HUMAN_REVIEW
└── EXTERNAL_ACTION
   ↓
COMPLETED
```

Failure:

```text
RUNNING
   ↓
FAILED
   ↓
RETRY / FALLBACK / HUMAN_HANDOFF
```

---

## 39. Security Boundary

The architecture SHALL maintain:

```text
                    INTERNET
                       │
                       ▼
                 CDN / WAF
                       │
                       ▼
                Client Frontend
                       │
                       ▼
                  API Gateway
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Authentication       Authorization
             │                   │
             └─────────┬─────────┘
                       ▼
                Client Services
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Database      Queue        AI
          │            │            │
          └────────────┼────────────┘
                       ▼
                External Systems
```

No external client SHALL cross internal administrative security boundaries.

---

## 40. Acceptance Criteria

The Client Portal SHALL be considered production-ready when:

* Authentication works reliably.
* MFA works where enabled.
* Tenant isolation is verified.
* Authorization is enforced server-side.
* Workspace isolation is verified.
* Subscription entitlements work.
* Client dashboard loads from backend APIs.
* Sales functionality is backend-connected.
* Lead generation is backend-connected.
* CRM functionality is backend-connected.
* Marketing functionality is backend-connected.
* Advertising functionality is backend-connected.
* SEO functionality is backend-connected.
* Product intelligence is backend-connected.
* Analytics are backend-connected.
* AI agents are backend-connected.
* AI actions are permission-controlled.
* Human approvals work.
* Knowledge/RAG functionality is permission-controlled.
* Workflows execute server-side.
* Integrations are securely connected.
* Reports are generated asynchronously.
* Excel exports are tenant-isolated.
* Billing is backend-controlled.
* Usage limits are enforced.
* Notifications work.
* Support workflows work.
* Audit events are generated.
* Security events are protected.
* Errors are handled gracefully.
* Accessibility requirements are satisfied.
* Responsive layouts work.
* Observability is implemented.
* Critical operations are idempotent.
* Rate limiting is enforced.
* No secrets are exposed to the frontend.
* No cross-tenant data leakage exists.
* No client can access internal administrative functionality.

---

## 41. Definition of Done

A Client Portal feature is **DONE** only when all of the following exist:

```text
UI
+
UX
+
Frontend State
+
API Contract
+
Authentication
+
Authorization
+
Backend Service
+
Database Model
+
Validation
+
Error Handling
+
Loading State
+
Empty State
+
Audit Logging
+
Observability
+
Security Testing
+
Unit Testing
+
Integration Testing
+
E2E Testing
+
Accessibility Testing
+
Performance Testing
+
Documentation
```

A frontend-only implementation SHALL NOT be considered complete.

---

## 42. Final Architecture Principle

The SalesGenie Client Portal SHALL operate as a secure enterprise control surface:

```text
                         CLIENT
                           │
                           ▼
                    CLIENT PORTAL
                           │
                           ▼
                    EXPERIENCE API
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
    AUTHORIZATION      ENTITLEMENTS      POLICY
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                     API GATEWAY
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
      SALES              AI/AGENTS         MARKETING
        │                  │                  │
        ▼                  ▼                  ▼
      CRM                 RAG               ADS/SEO
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                      ANALYTICS/BI
                           │
                           ▼
                     WORKFLOWS
                           │
                           ▼
                    INTEGRATIONS
                           │
                           ▼
                    REPORTING/BILLING
                           │
                           ▼
                    AUDIT/OBSERVABILITY
```

The core architectural rule is:

> **The frontend presents capabilities; the backend authorizes, executes, persists, audits, and enforces them.**

No client-facing UI control, hidden route, feature flag, or frontend permission check SHALL be treated as a substitute for backend authorization.
