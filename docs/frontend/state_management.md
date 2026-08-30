# SalesGenie — State Management Requirements

**Document:** `state_management.md`  
**Product:** SalesGenie Enterprise AI Customer Support & Sales Agent Platform  
**Document Type:** User Requirements + System Requirements + Functional Requirements  
**Architecture Scope:** Frontend State Management, Backend Synchronization, Distributed State, AI/Agent State, Real-Time State, Multi-Tenant State  
**Target Standard:** FAANG-Level Enterprise SaaS  
**Primary Frontend:** Astro + React/TypeScript components  
**Backend:** Enterprise Microservices + REST APIs + Event-Driven Architecture + WebSockets/SSE  
**Target Scale:** 10M+ users, 500K+ concurrent conversations  
**Status:** Architecture Specification  

---

## 1. Purpose

SalesGenie requires a centralized, predictable, observable, secure, scalable, and fault-tolerant state-management architecture capable of coordinating:

- Authentication state
- User identity
- Organization state
- Workplace state
- Role and permission state
- Subscription and billing state
- Feature entitlement state
- UI state
- Server/API state
- Real-time state
- Sales state
- Lead state
- CRM state
- Marketing state
- SEO state
- Advertising state
- Customer-support state
- Conversation state
- AI agent state
- AI model state
- RAG state
- Workflow state
- Notification state
- Analytics state
- Dashboard state
- Search state
- Integration state
- Human-in-the-loop state
- Administrative state
- Security state
- Audit state

The state-management architecture SHALL prevent inconsistent frontend state, stale server data, unauthorized state exposure, race conditions, duplicate mutations, lost updates, and cross-tenant state leakage.

---

## 2. State Management Principles

The SalesGenie frontend SHALL follow these principles:

1. Server state SHALL be treated separately from client/UI state.
2. Authentication state SHALL be centrally managed.
3. Authorization state SHALL be derived from backend-issued permissions.
4. Tenant context SHALL never be trusted solely from frontend state.
5. Backend SHALL remain the source of truth for persistent business state.
6. Frontend SHALL remain responsible for ephemeral presentation state.
7. Server state SHALL support caching, invalidation, revalidation, and optimistic updates.
8. Real-time events SHALL reconcile with server state.
9. State mutations SHALL be idempotent where possible.
10. State transitions SHALL be deterministic.
11. Sensitive state SHALL never be persisted unnecessarily.
12. State SHALL be scoped by tenant, organization, workplace, user, and resource.
13. State synchronization SHALL tolerate network failures.
14. Concurrent updates SHALL use versioning or conflict-resolution mechanisms.
15. AI-generated state SHALL be distinguishable from human-approved state.
16. State changes affecting critical business operations SHALL be auditable.
17. State management SHALL support progressive enhancement and graceful degradation.
18. State SHALL be observable without exposing sensitive information.
19. State management SHALL support feature flags and entitlement-based rendering.
20. State architecture SHALL scale independently from individual UI components.

---

## 3. State Classification

SalesGenie SHALL classify application state into the following categories.

## 3.1 Local UI State

Examples:

- Modal visibility
- Dropdown state
- Tooltip visibility
- Tab selection
- Form input state
- Accordion state
- Temporary filters
- Temporary sorting
- Wizard step
- Drag-and-drop state
- Component loading state

This state SHOULD remain local unless shared by multiple components.

---

## 3.2 Global Client State

Examples:

- Current user
- Current organization
- Current workplace
- Current team
- Current theme
- Current locale
- Navigation state
- Global UI preferences
- Notification center state
- Application feature flags

---

## 3.3 Server State

Examples:

- Users
- Organizations
- Workplaces
- Leads
- Contacts
- Accounts
- Opportunities
- Deals
- Campaigns
- Tickets
- Conversations
- AI agents
- Workflows
- Documents
- Knowledge bases
- Integrations
- Subscriptions
- Billing records
- Reports
- Analytics
- Search results

Server state SHALL NOT be duplicated unnecessarily into permanent client state.

---

## 3.4 Real-Time State

Examples:

- Active conversations
- Agent availability
- Human-agent presence
- Support queue
- Lead assignment changes
- Workflow execution
- AI agent execution
- Notifications
- Incident state
- Live analytics
- Collaboration state

---

## 3.5 Persistent Client State

Allowed examples:

- Theme preference
- Locale preference
- Non-sensitive UI preferences
- Dashboard layout
- Table column preferences
- Saved filters
- Recently used navigation items

Sensitive authentication or authorization information SHALL NOT be stored in insecure browser persistence mechanisms.

---

## 3.6 Ephemeral State

Examples:

- Temporary AI generation
- Draft messages
- Unsaved forms
- Drag state
- Temporary wizard state
- Streaming response buffers
- Upload progress

---

## 4. User Requirements

## UR-001 — Consistent Application State

Users SHALL see consistent application state across SalesGenie pages and components.

---

## UR-002 — Persistent User Experience

Users SHALL retain permitted preferences such as:

- Theme
- Language
- Dashboard configuration
- Table preferences
- Saved filters
- Navigation preferences

across sessions where appropriate.

---

## UR-003 — Real-Time Updates

Users SHALL receive real-time updates for relevant events without requiring manual page refresh.

Examples:

- New support messages
- Lead assignment
- AI agent status
- Workflow execution
- Notifications
- Ticket updates
- Campaign changes
- Collaboration updates

---

## UR-004 — Accurate Business Data

Users SHALL always be able to distinguish:

- Current server data
- Cached data
- Pending changes
- Failed changes
- AI-generated data
- Human-approved data

---

## UR-005 — Secure State

Users SHALL only receive state permitted by their:

- Identity
- Organization
- Workplace
- Team
- Role
- Permissions
- Resource-level access policies

---

## UR-006 — Multi-Tenant Isolation

Users SHALL never see state belonging to another organization, workplace, tenant, or unauthorized resource.

---

## UR-007 — Reliable Mutations

When users modify business data, the UI SHALL clearly communicate:

- Pending state
- Success state
- Failure state
- Retry availability
- Conflict state

---

## UR-008 — Optimistic User Experience

Low-risk operations MAY provide optimistic UI updates when backend confirmation is not required before rendering.

---

## UR-009 — Safe Critical Operations

Critical operations SHALL require authoritative backend confirmation before displaying the operation as completed.

Examples:

- Payments
- Subscription changes
- User bans
- Permission changes
- Role changes
- Lead deletion
- Account deletion
- Security configuration
- AI deployment
- Workflow activation

---

## UR-010 — Offline/Intermittent Connectivity Handling

Users SHALL receive meaningful feedback when connectivity is lost.

The application SHALL:

- Detect connection failures
- Preserve safe temporary state
- Prevent accidental data loss
- Retry eligible requests
- Revalidate stale state after reconnection

---

## UR-011 — Search State

Users SHALL be able to maintain:

- Search query
- Filters
- Sort order
- Pagination
- Search scope
- Selected results

without inconsistent UI state.

---

## UR-012 — Dashboard State

Users SHALL be able to configure dashboards while preserving:

- Widget arrangement
- Widget visibility
- Filters
- Date ranges
- Selected metrics
- Visualization preferences

---

## UR-013 — AI Interaction State

Users SHALL see accurate AI execution state including:

- Queued
- Processing
- Streaming
- Completed
- Failed
- Cancelled
- Waiting for human approval
- Escalated

---

## UR-014 — Human Review State

Human operators SHALL be able to identify:

- Items awaiting review
- Items currently claimed
- Items approved
- Items rejected
- Items modified
- Items escalated

---

## UR-015 — Notification State

Users SHALL receive accurate notification counts and status.

The system SHALL distinguish:

- Unread
- Read
- Archived
- Dismissed
- Action-required
- Critical

---

## 5. System Requirements

## SR-001 — State Architecture

The frontend SHALL implement a layered state architecture:

```text
                    FRONTEND
                       |
        +--------------+--------------+
        |              |              |
   UI STATE      CLIENT STATE    SERVER STATE
        |              |              |
        +--------------+--------------+
                       |
                 STATE SELECTORS
                       |
                DOMAIN COMPONENTS
                       |
                 API CLIENT LAYER
                       |
              AUTH / API GATEWAY
                       |
          +------------+-------------+
          |            |             |
      REST APIs    WebSocket/SSE   Events
          |            |             |
          +------------+-------------+
                       |
                MICROSERVICES
```

---

## SR-002 — Single Source of Truth

Persistent business state SHALL be owned by backend services.

The frontend SHALL NOT become the authoritative source for:

* User identity
* Permissions
* Billing
* Subscription
* Lead records
* Customer records
* CRM records
* AI execution results
* Security state
* Audit state

---

## SR-003 — Domain-Based State Architecture

State SHALL be logically divided into domains:

```text
auth
identity
organization
workplace
permissions
billing
subscriptions
sales
leads
crm
marketing
seo
advertising
support
conversations
ai
agents
rag
workflows
integrations
notifications
analytics
search
admin
security
system
```

---

## SR-004 — Server-State Cache

The frontend SHALL implement a server-state caching mechanism supporting:

* Cache keys
* Cache invalidation
* TTL
* Stale-while-revalidate
* Background refresh
* Request deduplication
* Pagination
* Infinite queries
* Prefetching
* Mutation invalidation
* Error retry
* Garbage collection

---

## SR-005 — Query Key Isolation

Query/cache keys SHALL include appropriate resource scope.

Example:

```text
[
  "leads",
  tenantId,
  organizationId,
  workplaceId,
  filters,
  pagination
]
```

---

## SR-006 — Tenant-Aware State

All tenant-specific state SHALL include a tenant scope.

The frontend SHALL clear or replace tenant-specific state when:

* User logs out
* Organization changes
* Workplace changes
* Tenant context expires
* Session changes
* Authorization changes

---

## SR-007 — Authentication State

Authentication state SHALL include:

```text
authenticated
unauthenticated
authenticating
refreshing
session_expired
authentication_error
```

---

## SR-008 — Authorization State

Authorization state SHALL include:

```text
roles
permissions
policies
organization_scope
workplace_scope
team_scope
resource_scope
feature_entitlements
```

Authorization decisions SHALL ultimately be enforced server-side.

---

## SR-009 — Session State

The frontend SHALL support:

* Session initialization
* Session refresh
* Session expiration
* Logout
* Forced logout
* Concurrent session detection
* Session invalidation
* Unauthorized response handling

---

## SR-010 — State Hydration

The frontend SHALL support safe hydration for:

* SSR
* Static rendering
* Client-side rendering
* Partial hydration
* React islands

Sensitive state SHALL NOT be exposed through publicly rendered HTML.

---

## SR-011 — State Serialization

State serialized to the browser SHALL:

* Exclude secrets
* Exclude access tokens where possible
* Exclude private credentials
* Exclude sensitive personal data unless necessary
* Preserve type safety
* Validate schema

---

## SR-012 — Schema Validation

API responses SHALL be validated against typed schemas before entering application state.

Invalid responses SHALL be treated as errors.

---

## SR-013 — State Immutability

Shared application state SHALL be updated through controlled state transitions.

Components SHALL NOT mutate shared objects directly.

---

## SR-014 — State Selectors

Components SHALL consume minimal state through selectors.

Example:

```text
useCurrentUser()
useCurrentOrganization()
useCurrentWorkspace()
usePermissions()
useSubscription()
useUnreadNotifications()
useActiveConversation()
```

---

## SR-015 — Derived State

Derived values SHALL be calculated from authoritative state instead of being duplicated.

Examples:

```text
isAdmin
canEditLead
canDeleteUser
canDeployAgent
subscriptionRemainingQuota
unreadNotificationCount
leadConversionRate
```

---

## SR-016 — State Normalization

Highly relational datasets SHOULD be normalized where beneficial.

Example:

```text
entities:
  users
  organizations
  teams
  leads
  contacts
  accounts

relationships:
  user.organizationId
  lead.ownerId
  contact.accountId
```

---

## SR-017 — Pagination State

Large datasets SHALL support:

* Offset pagination
* Cursor pagination
* Infinite scrolling
* Page caching
* Filter-aware pagination
* Sort-aware pagination

---

## SR-018 — Request Deduplication

Identical concurrent requests SHALL be deduplicated where safe.

---

## SR-019 — Request Cancellation

The frontend SHALL cancel obsolete requests.

Examples:

* Search query changes
* User leaves page
* Component unmounts
* Filter changes
* Route changes

---

## SR-020 — Race Condition Prevention

The system SHALL prevent stale responses from overwriting newer state.

Each request SHALL be associated with:

* Request ID
* Timestamp or sequence
* Query key
* Resource version where applicable

---

## 6. Functional Requirements

## FR-001 — Global Application Store

The system SHALL provide a global state layer for cross-application concerns.

It SHALL support:

* Current user
* Current organization
* Current workplace
* Current team
* Theme
* Locale
* Global UI state
* Notification state
* Application status

---

## FR-002 — Authentication Store

The authentication state manager SHALL expose:

```text
currentUser
sessionStatus
authenticationStatus
sessionExpiry
authenticationError
logout()
refreshSession()
```

---

## FR-003 — Authorization Store

The authorization state manager SHALL expose:

```text
roles
permissions
resourcePermissions
organizationPermissions
workplacePermissions
featureEntitlements
```

It SHALL support:

```text
can(action, resource)
hasRole(role)
hasPermission(permission)
hasFeature(feature)
```

---

## FR-004 — Organization State

The system SHALL manage:

```text
currentOrganization
organizations
organizationSettings
organizationMembers
organizationPlan
organizationUsage
```

---

## FR-005 — Workplace State

The system SHALL manage:

```text
currentWorkplace
workplaces
workplaceSettings
workplaceMembers
workplaceTeams
```

---

## FR-006 — User State

The system SHALL manage:

```text
profile
preferences
roles
permissions
organizationMemberships
workplaceMemberships
notificationPreferences
```

---

## FR-007 — Subscription State

The system SHALL manage:

```text
plan
subscription
billingStatus
usage
quotas
limits
entitlements
trialStatus
renewalDate
```

Backend SHALL remain authoritative.

---

## FR-008 — Feature Flag State

The system SHALL support:

```text
global flags
organization flags
workplace flags
user flags
experiment flags
percentage rollouts
```

Feature flags SHALL be retrieved from backend services.

---

## FR-009 — Lead State

The lead-management state SHALL support:

```text
leadList
leadDetails
leadFilters
leadSorting
leadPagination
leadSelection
leadAssignment
leadScoring
leadQualification
leadEnrichment
leadActivity
```

---

## FR-010 — Lead Mutation State

Each lead mutation SHALL support:

```text
idle
pending
success
error
conflict
```

---

## FR-011 — CRM State

The CRM state SHALL support:

```text
contacts
accounts
opportunities
deals
activities
tasks
notes
pipelines
stages
```

---

## FR-012 — Sales Pipeline State

The frontend SHALL maintain synchronized state for:

```text
pipeline
stages
opportunities
deal values
forecast values
ownership
activities
```

---

## FR-013 — Marketing State

The system SHALL support:

```text
campaigns
audiences
segments
content
email campaigns
social campaigns
advertisements
marketing workflows
analytics
```

---

## FR-014 — SEO State

The system SHALL support:

```text
projects
keywords
keyword clusters
rankings
SERP results
SEO audits
backlinks
content gaps
competitor data
```

---

## FR-015 — Advertising State

The system SHALL support:

```text
ad accounts
campaigns
ad groups
ads
audiences
budgets
spend
revenue
ROAS
ROI
conversions
```

---

## FR-016 — Support State

The support state SHALL support:

```text
tickets
queues
agents
conversations
customers
SLAs
escalations
assignments
```

---

## FR-017 — Conversation State

Conversation state SHALL support:

```text
conversationId
participants
messages
messageStatus
typingStatus
presence
attachments
AI status
human handoff
escalation
```

---

## FR-018 — Message State

Messages SHALL support:

```text
queued
sending
sent
delivered
read
failed
retrying
```

---

## FR-019 — Real-Time Conversation State

The frontend SHALL synchronize conversation state through WebSocket/SSE events.

Example:

```text
MESSAGE_CREATED
MESSAGE_UPDATED
MESSAGE_DELIVERED
MESSAGE_READ
AGENT_STARTED
AGENT_STREAMING
AGENT_COMPLETED
AGENT_FAILED
HUMAN_HANDOFF
CONVERSATION_ESCALATED
```

---

## FR-020 — AI Agent State

AI agent state SHALL support:

```text
draft
configured
testing
published
deployed
running
paused
failed
disabled
archived
```

---

## FR-021 — AI Execution State

Each AI execution SHALL support:

```text
queued
running
streaming
waiting_for_tool
waiting_for_approval
completed
failed
cancelled
timed_out
escalated
```

---

## FR-022 — AI Streaming State

The system SHALL support incremental state updates for:

* Token streams
* Tool calls
* Intermediate results
* Reasoning status where exposed
* Agent status
* Citations
* Final response

Streaming buffers SHALL not overwrite authoritative persisted results.

---

## FR-023 — Human-in-the-Loop State

The system SHALL support:

```text
pending_review
claimed
reviewing
approved
rejected
modified
escalated
expired
```

---

## FR-024 — Workflow State

Workflow state SHALL support:

```text
draft
published
scheduled
running
paused
completed
failed
cancelled
```

---

## FR-025 — Workflow Execution State

Execution state SHALL include:

```text
executionId
workflowId
currentNode
executionStatus
input
output
error
retryCount
startedAt
completedAt
```

---

## FR-026 — RAG State

The frontend SHALL manage:

```text
knowledgeBase
documents
documentProcessingStatus
embeddingsStatus
indexingStatus
retrievalStatus
searchResults
citations
```

---

## FR-027 — Document Upload State

Document state SHALL support:

```text
selected
uploading
uploaded
processing
indexed
failed
cancelled
```

---

## FR-028 — Search State

Global search SHALL support:

```text
query
scope
filters
sort
pagination
results
loading
error
selectedResult
```

Search state SHALL be reset when the user changes search scope where appropriate.

---

## FR-029 — Notification State

Notification state SHALL support:

```text
notifications
unreadCount
readState
actionRequired
criticalNotifications
notificationPreferences
```

---

## FR-030 — Dashboard State

Dashboard state SHALL support:

```text
widgets
layout
filters
dateRange
selectedMetrics
refreshInterval
visualizationSettings
```

---

## FR-031 — Analytics State

Analytics state SHALL support:

```text
dateRange
filters
dimensions
metrics
segments
charts
tables
comparisonPeriods
loading
errors
```

---

## FR-032 — Report State

Report state SHALL support:

```text
reportDefinition
filters
columns
charts
schedule
exportStatus
generationStatus
downloadStatus
```

---

## FR-033 — Integration State

Integration state SHALL support:

```text
availableIntegrations
connectedIntegrations
connectionStatus
OAuthStatus
syncStatus
lastSync
syncErrors
```

---

## FR-034 — Integration Synchronization

The frontend SHALL display:

```text
connected
connecting
syncing
synced
failed
disconnected
reauthentication_required
```

---

## FR-035 — Admin State

Administrative interfaces SHALL manage state for:

```text
users
roles
permissions
organizations
workplaces
feature flags
system configuration
audit logs
incidents
platform metrics
```

---

## FR-036 — Audit State

Critical state changes SHALL be associated with audit information.

Example:

```text
actorId
actorType
action
resourceType
resourceId
timestamp
previousVersion
newVersion
requestId
```

---

## 7. Backend Synchronization Requirements

## BSR-001 — API Synchronization

All persistent frontend state SHALL synchronize through approved API clients.

Components SHALL NOT directly call arbitrary backend endpoints.

---

## BSR-002 — API Client Layer

The frontend SHALL provide a centralized API client supporting:

* Authentication
* Authorization
* Request IDs
* Retries
* Timeouts
* Error normalization
* Response validation
* Cancellation
* Telemetry
* Correlation IDs

---

## BSR-003 — Query Invalidation

Successful mutations SHALL invalidate affected queries.

Example:

```text
CREATE_LEAD
    ↓
invalidate:
  leads
  lead-count
  lead-analytics
  sales-dashboard
```

---

## BSR-004 — Mutation Synchronization

Mutation state SHALL transition:

```text
idle
  ↓
pending
  ↓
success
```

or:

```text
idle
  ↓
pending
  ↓
error
  ↓
retry
```

---

## BSR-005 — Optimistic Updates

Optimistic updates SHALL:

1. Snapshot previous state.
2. Apply temporary state.
3. Execute backend mutation.
4. Confirm successful response.
5. Roll back on failure.
6. Revalidate authoritative state.

---

## BSR-006 — Conflict Detection

The frontend SHALL support backend conflict responses such as:

```text
409 Conflict
412 Precondition Failed
423 Locked
```

---

## BSR-007 — Versioned Resources

Where required, resources SHALL expose:

```text
version
updatedAt
etag
revision
```

to prevent lost updates.

---

## BSR-008 — Event-Based Synchronization

Backend events SHALL update frontend state without requiring full page reload.

---

## 8. Real-Time State Management

## RT-001 — Connection State

The real-time client SHALL expose:

```text
disconnected
connecting
connected
reconnecting
failed
```

---

## RT-002 — Event Ordering

The system SHALL preserve event ordering where required.

Events SHALL contain:

```text
eventId
eventType
aggregateId
sequence
timestamp
tenantId
```

---

## RT-003 — Duplicate Events

Duplicate events SHALL be safely ignored through event IDs or idempotency keys.

---

## RT-004 — Missed Events

After reconnecting, the frontend SHALL revalidate affected server state.

---

## RT-005 — Real-Time Authorization

Real-time subscriptions SHALL be authorized by backend services.

Frontend state SHALL never assume authorization based solely on subscription parameters.

---

## 9. State Persistence

## SP-001 — Safe Persistence

Only explicitly approved state SHALL be persisted locally.

---

## SP-002 — Sensitive Data Protection

The application SHALL NOT persist:

* Passwords
* API secrets
* Payment credentials
* Private keys
* OAuth client secrets
* Long-lived authentication secrets

in ordinary browser storage.

---

## SP-003 — Persistence Versioning

Persisted state SHALL include schema versions.

Example:

```text
stateVersion: 3
```

---

## SP-004 — Migration

Application updates SHALL migrate or invalidate incompatible persisted state.

---

## SP-005 — Logout Cleanup

Logout SHALL clear all user-specific and tenant-specific persisted state.

---

## 10. State Security Requirements

## SEC-001 — Tenant Isolation

State caches SHALL be tenant-aware.

---

## SEC-002 — Permission Changes

When backend permissions change, cached authorization state SHALL be invalidated.

---

## SEC-003 — Role Changes

When a user's role changes, the frontend SHALL re-fetch:

* User identity
* Roles
* Permissions
* Feature entitlements
* Navigation permissions

---

## SEC-004 — Session Expiration

On session expiration:

```text
clear sensitive state
invalidate protected queries
stop real-time subscriptions
redirect to authentication
```

---

## SEC-005 — Unauthorized Requests

HTTP `401` SHALL trigger authentication recovery.

HTTP `403` SHALL trigger authorization handling.

---

## SEC-006 — Cross-Tenant Cache Protection

Cache keys SHALL prevent collisions between tenants.

Invalid:

```text
["leads"]
```

Preferred:

```text
["tenant", tenantId, "organization", organizationId, "leads"]
```

---

## 11. Loading and Error State Requirements

## LS-001 — Granular Loading State

The application SHALL distinguish:

```text
initial_loading
background_refresh
mutation_pending
streaming
pagination_loading
uploading
processing
```

---

## LS-002 — Error State

Errors SHALL distinguish:

```text
network_error
authentication_error
authorization_error
validation_error
conflict_error
rate_limit_error
server_error
timeout_error
unknown_error
```

---

## LS-003 — Retry Strategy

Retry SHALL be used only for eligible errors.

Examples:

```text
network failure → retry
timeout → retry
429 → backoff
5xx → controlled retry
400 → no automatic retry
401 → refresh/re-authenticate
403 → no retry
```

---

## LS-004 — Error Recovery

The UI SHALL support:

* Retry
* Refresh
* Re-authentication
* Rollback
* Revalidation
* User correction

---

## 12. Concurrency Requirements

## CR-001 — Concurrent Mutations

The system SHALL handle simultaneous mutations safely.

---

## CR-002 — Duplicate Submission Prevention

Critical operations SHALL prevent duplicate submissions through:

* Disabled controls
* Idempotency keys
* Request tracking
* Backend idempotency

---

## CR-003 — Stale Response Prevention

Older responses SHALL NOT overwrite newer state.

---

## CR-004 — Multi-Tab Synchronization

Where appropriate, state SHALL synchronize across browser tabs.

Examples:

* Logout
* Session expiration
* Theme
* User preferences
* Notification state

---

## CR-005 — Collaborative State

Collaborative resources SHALL support conflict detection.

Examples:

* Workflow builder
* AI agent builder
* Dashboard builder
* Campaign builder
* Shared reports

---

## 13. AI-Specific State Requirements

## AI-STATE-001 — AI Provenance

AI-generated state SHALL identify:

```text
generatedByAI
model
provider
generationId
timestamp
confidence
approvalStatus
```

---

## AI-STATE-002 — Human Approval

AI-generated actions requiring approval SHALL remain in:

```text
pending_approval
```

until backend confirmation.

---

## AI-STATE-003 — AI Confidence

AI state MAY include:

```text
confidenceScore
confidenceLevel
riskLevel
```

---

## AI-STATE-004 — AI Failure State

AI execution failures SHALL expose:

```text
provider_failure
model_failure
timeout
tool_failure
retrieval_failure
policy_failure
validation_failure
```

---

## AI-STATE-005 — Model Switching

When LLM fallback occurs, frontend state SHALL remain stable while backend records provider/model changes.

---

## 14. State Observability

## OBS-001 — State Metrics

The application SHALL track:

* Cache hit rate
* Cache miss rate
* Query latency
* Mutation latency
* State synchronization failures
* WebSocket reconnects
* Event processing latency
* Stale state incidents
* Optimistic rollback rate
* API error rate

---

## OBS-002 — State Debugging

Development environments SHALL provide safe state inspection.

Production state inspection SHALL exclude sensitive data.

---

## OBS-003 — Correlation IDs

State-affecting API operations SHALL support:

```text
requestId
traceId
correlationId
userId
tenantId
```

where appropriate and permitted.

---

## 15. Performance Requirements

## PERF-001 — Minimal Re-rendering

State updates SHALL only re-render affected components.

---

## PERF-002 — Selector Optimization

Components SHALL subscribe only to the state they require.

---

## PERF-003 — Large Dataset Handling

Large datasets SHALL use:

* Pagination
* Virtualization
* Incremental fetching
* Server-side filtering
* Server-side sorting

---

## PERF-004 — Cache Efficiency

The frontend SHALL minimize redundant API requests.

---

## PERF-005 — Prefetching

The application MAY prefetch predictable data.

Examples:

```text
hover lead → prefetch lead details
open organization menu → prefetch organizations
navigate dashboard → prefetch dashboard metrics
```

---

## PERF-006 — Streaming

Long-running AI operations SHALL support streaming where supported.

---

## 16. State Lifecycle

Every server-backed resource SHOULD follow:

```text
UNINITIALIZED
      ↓
LOADING
      ↓
AVAILABLE
      ↓
STALE
      ↓
REFRESHING
      ↓
UPDATED
```

Failure path:

```text
LOADING
   ↓
ERROR
   ↓
RETRY
   ↓
LOADING
```

Mutation path:

```text
IDLE
 ↓
PENDING
 ↓
SUCCESS
```

or:

```text
IDLE
 ↓
PENDING
 ↓
FAILED
 ↓
ROLLBACK
```

---

## 17. Domain State Model

```text
APPLICATION STATE
│
├── Identity
│   ├── User
│   ├── Organization
│   ├── Workplace
│   └── Team
│
├── Security
│   ├── Authentication
│   ├── Authorization
│   ├── Roles
│   └── Permissions
│
├── Commercial
│   ├── Subscription
│   ├── Billing
│   ├── Usage
│   └── Entitlements
│
├── Sales
│   ├── Leads
│   ├── Contacts
│   ├── Accounts
│   ├── Opportunities
│   └── Deals
│
├── Marketing
│   ├── Campaigns
│   ├── Audiences
│   ├── Content
│   └── Attribution
│
├── SEO
│   ├── Keywords
│   ├── Rankings
│   ├── Audits
│   └── Backlinks
│
├── Advertising
│   ├── Campaigns
│   ├── Spend
│   ├── Revenue
│   └── ROAS
│
├── Support
│   ├── Tickets
│   ├── Conversations
│   ├── Agents
│   └── SLAs
│
├── AI
│   ├── Agents
│   ├── Executions
│   ├── Models
│   ├── Prompts
│   └── Guardrails
│
├── RAG
│   ├── Knowledge Bases
│   ├── Documents
│   ├── Retrieval
│   └── Citations
│
├── Automation
│   ├── Workflows
│   ├── Executions
│   └── Schedules
│
├── Analytics
│   ├── Metrics
│   ├── Reports
│   ├── Dashboards
│   └── KPIs
│
├── Integrations
│   ├── Connections
│   ├── Sync
│   └── Errors
│
└── UI
    ├── Navigation
    ├── Theme
    ├── Locale
    ├── Modals
    └── Preferences
```

---

## 18. State Ownership Matrix

| State             | Frontend | Backend       | Real-Time | Persistent |
| ----------------- | -------- | ------------- | --------- | ---------- |
| Theme             | Yes      | Optional      | No        | Yes        |
| Locale            | Yes      | Optional      | No        | Yes        |
| Current User      | Cached   | Authoritative | Optional  | Limited    |
| Permissions       | Cached   | Authoritative | Optional  | No         |
| Subscription      | Cached   | Authoritative | Optional  | No         |
| Leads             | Cached   | Authoritative | Yes       | No         |
| CRM               | Cached   | Authoritative | Yes       | No         |
| Conversations     | Cached   | Authoritative | Yes       | No         |
| AI Execution      | Cached   | Authoritative | Yes       | No         |
| Workflow          | Cached   | Authoritative | Yes       | No         |
| Notifications     | Cached   | Authoritative | Yes       | Limited    |
| Dashboard Layout  | Yes      | Optional      | Optional  | Yes        |
| Billing           | Cached   | Authoritative | Optional  | No         |
| Security Policies | Cached   | Authoritative | Optional  | No         |
| Audit Logs        | Cached   | Authoritative | Optional  | No         |

---

## 19. Cache Invalidation Requirements

The system SHALL define explicit invalidation rules.

Example:

```text
Lead Created
    ↓
invalidate:
  lead list
  lead count
  lead analytics
  sales dashboard
```

```text
Subscription Changed
    ↓
invalidate:
  subscription
  usage
  quotas
  entitlements
  feature flags
```

```text
Role Changed
    ↓
invalidate:
  user
  roles
  permissions
  navigation
  feature entitlements
```

```text
Workflow Published
    ↓
invalidate:
  workflow
  workflow list
  execution history
  workflow analytics
```

---

## 20. State Synchronization Contract

Every backend-managed resource SHOULD expose:

```json
{
  "id": "resource-id",
  "version": 12,
  "updated_at": "2026-08-30T00:00:00Z",
  "updated_by": "user-id"
}
```

For event-driven synchronization:

```json
{
  "event_id": "event-id",
  "event_type": "lead.updated",
  "aggregate_id": "lead-id",
  "aggregate_version": 13,
  "tenant_id": "tenant-id",
  "timestamp": "2026-08-30T00:00:00Z"
}
```

---

## 21. State Transition Rules

State transitions SHALL be explicit.

Example:

```text
DRAFT
  ↓
SUBMITTED
  ↓
PROCESSING
  ↓
COMPLETED
```

Failure:

```text
PROCESSING
  ↓
FAILED
  ↓
RETRYING
  ↓
PROCESSING
```

Cancellation:

```text
PROCESSING
  ↓
CANCELLATION_REQUESTED
  ↓
CANCELLED
```

---

## 22. Form State Management

Forms SHALL support:

* Initial values
* Dirty state
* Validation state
* Submission state
* Server validation
* Draft state
* Unsaved changes
* Reset
* Rollback
* Retry

Example:

```text
PRISTINE
   ↓
DIRTY
   ↓
VALID
   ↓
SUBMITTING
   ↓
SUCCESS
```

or:

```text
SUBMITTING
   ↓
SERVER_ERROR
   ↓
DIRTY
```

---

## 23. File Upload State

Uploads SHALL support:

```text
selected
validating
uploading
paused
resuming
processing
completed
failed
cancelled
```

Progress SHALL be represented where supported.

---

## 24. Navigation State

Navigation state SHALL support:

* Current route
* Active module
* Active resource
* Breadcrumbs
* Sidebar state
* Workspace context
* Navigation permissions
* Feature availability

Navigation SHALL be derived from backend authorization and feature entitlements.

---

## 25. Role-Based State Visibility

The frontend SHALL support role-aware state visibility for all defined SalesGenie roles:

```text
Super Admin
Platform Admin
Security Admin
Billing Admin
Organization Owner
Organization Admin
Workplace Admin
Team Manager
Sales Manager
Sales Agent
Marketing Manager
Marketing Specialist
SEO Manager
SEO Specialist
Product Manager
Finance Manager
Business Analyst
Support Manager
Support Agent
AI Agent Builder
Developer
End User
External Client
```

The frontend SHALL never use role-based UI hiding as the sole security control.

---

## 26. State Management for Super Admin

Super Admin state SHALL support:

* Platform-wide users
* Organizations
* Workplaces
* Platform metrics
* Feature flags
* System configuration
* Incidents
* Security state
* Audit state
* Service health

All privileged state SHALL be protected by backend authorization.

---

## 27. State Management for External Clients

External Client state SHALL be strictly restricted to:

```text
client organization
client workspace
client projects
client reports
client analytics
client support
client AI agents
client integrations
client billing
```

No platform-internal state SHALL be exposed.

---

## 28. State Management Testing Requirements

The state layer SHALL be tested for:

## Unit Tests

* Reducers
* Stores
* Selectors
* State transitions
* Cache functions
* Permission selectors
* Derived state

## Integration Tests

* API synchronization
* Authentication state
* Query invalidation
* Mutation rollback
* Real-time events
* Tenant switching
* Role changes

## E2E Tests

* Login → dashboard
* Organization switching
* Lead creation
* Lead assignment
* AI agent execution
* Human approval
* Workflow execution
* Subscription upgrade
* Logout
* Session expiration

## Security Tests

* Cross-tenant cache leakage
* Unauthorized state access
* Role escalation
* Stale permission state
* Sensitive state persistence
* Session invalidation

---

## 29. Failure Scenarios

The system SHALL handle:

```text
API unavailable
Database unavailable
Redis unavailable
WebSocket unavailable
Network timeout
Expired session
Invalid token
Permission change
Tenant change
Concurrent mutation
Duplicate event
Out-of-order event
Stale cache
Cache corruption
Malformed API response
AI provider failure
AI timeout
Workflow failure
Upload failure
Browser refresh
Browser tab duplication
```

---

## 30. Acceptance Criteria

The state-management architecture SHALL be considered production-ready when:

* [ ] Server state and client state are clearly separated.
* [ ] Persistent business state is backend-authoritative.
* [ ] Authentication state is centralized.
* [ ] Authorization state is backend-derived.
* [ ] Tenant isolation exists at the cache/state level.
* [ ] Organization switching clears incompatible state.
* [ ] Workplace switching clears incompatible state.
* [ ] Logout clears user-specific state.
* [ ] Session expiration invalidates protected state.
* [ ] Query caching is implemented.
* [ ] Query invalidation is implemented.
* [ ] Request deduplication is implemented.
* [ ] Request cancellation is implemented.
* [ ] Race conditions are prevented.
* [ ] Optimistic updates support rollback.
* [ ] Conflict handling exists.
* [ ] Real-time events update application state.
* [ ] Duplicate events are handled.
* [ ] Missed events trigger revalidation.
* [ ] AI execution state is represented accurately.
* [ ] Human approval state is represented accurately.
* [ ] Workflow execution state is represented accurately.
* [ ] Notification state is synchronized.
* [ ] Dashboard state is persistent where appropriate.
* [ ] Feature flags are backend-controlled.
* [ ] Subscription entitlements are backend-controlled.
* [ ] Sensitive state is not stored insecurely.
* [ ] State schemas are validated.
* [ ] State transitions are testable.
* [ ] State changes are observable.
* [ ] State performance is measurable.
* [ ] Multi-tab synchronization works where required.
* [ ] Critical mutations use backend confirmation.
* [ ] State architecture supports 10M+ users.
* [ ] State architecture supports 500K+ concurrent conversations.
* [ ] State architecture supports horizontal frontend scaling.
* [ ] State architecture supports microservice-based backend synchronization.

---

## 31. FAANG-Level State Management Architecture

```text
                         USER
                          │
                          ▼
                 ┌─────────────────┐
                 │   UI COMPONENTS │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ STATE SELECTORS │
                 └────────┬────────┘
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
     LOCAL STATE     GLOBAL STATE     SERVER STATE
          │               │                │
          │               │         ┌──────┴──────┐
          │               │         │             │
          │               │       CACHE       QUERIES
          │               │         │             │
          └───────────────┼─────────┴─────────────┘
                          │
                          ▼
                    API CLIENT
                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
          REST API    WebSocket       SSE
             │            │            │
             └────────────┼────────────┘
                          │
                    API GATEWAY
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
      AUTH SERVICE    DOMAIN SERVICES   AI SERVICES
          │               │                │
          └───────────────┼────────────────┘
                          │
                     EVENT BUS
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
       REDIS          POSTGRESQL       MESSAGE QUEUE
          │               │                │
          └───────────────┼────────────────┘
                          │
                    STATE EVENTS
                          │
                          ▼
                 FRONTEND RECONCILIATION
                          │
                          ▼
                  AUTHORITATIVE UI
```

---

## 32. Final Architectural Requirement

SalesGenie SHALL implement state management as a **distributed state synchronization architecture**, not merely as a frontend global store.

The architecture SHALL provide:

```text
Predictability
+
Type Safety
+
Server Authority
+
Tenant Isolation
+
Authorization Awareness
+
Caching
+
Invalidation
+
Real-Time Synchronization
+
Optimistic Updates
+
Conflict Resolution
+
AI State Management
+
Human-in-the-Loop State
+
Workflow State
+
Observability
+
Fault Tolerance
+
Performance
+
Security
+
Scalability
```

The final implementation SHALL ensure that **every backend-connected frontend feature has an explicit state lifecycle, ownership model, synchronization mechanism, authorization boundary, error model, cache strategy, and invalidation strategy**.

No production feature SHALL rely on uncontrolled component-local state for authoritative business data.

The frontend SHALL remain a state consumer and interaction layer, while backend microservices remain the authoritative source of persistent enterprise state.
