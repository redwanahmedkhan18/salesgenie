# SalesGenie — Frontend Architecture Requirements

**Document:** `frontend_architecture.md`  
**System:** SalesGenie Enterprise AI Customer Support, Sales, Marketing, SEO, Business Intelligence & Automation Platform  
**Architecture Level:** Enterprise / FAANG-Level  
**Frontend Type:** Multi-tenant, role-aware, AI-native, real-time enterprise web application  
**Primary UI:** Desktop-first responsive web application  
**Future UI:** Mobile / PWA / Native applications  
**Frontend Architecture Pattern:** Modular Monolith → Domain Modules → Federated/Distributed Modules where required  
**Rendering Strategy:** SSR/SSG/CSR/ISR depending on feature characteristics  
**API Pattern:** API Gateway + BFF/API Client + domain APIs  
**Communication:** REST + WebSocket/SSE + Webhooks through backend services  
**State:** Server state + client state + URL state + persistent state  
**Design Principle:** Backend-authoritative, permission-aware, tenant-isolated, observable, accessible and AI-native

---

## 1. Purpose

The SalesGenie frontend shall provide a unified enterprise interface for:

- Human users
- AI agents
- Hybrid AI + human workflows
- Super administrators
- Platform administrators
- Organization administrators
- Workplace administrators
- Team managers
- Sales teams
- Marketing teams
- SEO teams
- Finance teams
- Business analysts
- Customer support teams
- Developers
- AI agent builders
- External clients
- End users

The frontend shall consume backend APIs and event streams rather than implementing business-critical logic independently.

The frontend SHALL NOT become the source of truth for:

- Authorization
- Billing
- Subscription entitlement
- Tenant isolation
- Security policy
- Financial calculations
- Lead scoring
- AI decisions
- Workflow execution
- Data ownership
- Audit records
- Compliance decisions

These shall remain backend-controlled.

---

## 2. Frontend Architecture Goals

## FR-ARCH-001 — Enterprise Modularity

The frontend SHALL be organized into independently maintainable business domains.

Minimum domains:

- Identity
- Authentication
- Authorization
- Organizations
- Workplaces
- Teams
- Administration
- Sales
- Lead Generation
- CRM
- Marketing
- SEO
- Product Launch Intelligence
- Advertising
- Finance
- Business Intelligence
- Customer Support
- Omnichannel Communication
- AI Agents
- LLM Management
- RAG / Knowledge
- Workflow Automation
- MCP
- Integrations
- Billing
- Analytics
- Reporting
- Notifications
- Search
- Developer Platform
- Security
- Privacy
- Observability
- Onboarding
- Customer Portal
- AI + Human Operations

---

## 3. Core Frontend Principles

## FR-PRINCIPLE-001 — Backend Authority

Frontend applications SHALL treat backend APIs as authoritative.

## FR-PRINCIPLE-002 — Permission Enforcement

Frontend permission checks SHALL improve UX but SHALL NOT replace backend authorization.

## FR-PRINCIPLE-003 — Tenant Isolation

Every tenant-scoped request SHALL carry the appropriate authenticated tenant/workspace context through backend-approved mechanisms.

The frontend SHALL never allow users to arbitrarily manipulate tenant identifiers to access another tenant.

## FR-PRINCIPLE-004 — Secure Rendering

Sensitive information SHALL not be exposed through:

- Browser source
- Client-side configuration
- Public environment variables
- Local storage unless explicitly justified
- URL query parameters unless non-sensitive
- Debug logs

## FR-PRINCIPLE-005 — Progressive Enhancement

Core business workflows SHALL remain usable under:

- Slow networks
- Temporary API failures
- Partial service failures
- WebSocket disconnections
- Token refresh
- Browser tab suspension
- Backend deployment

## FR-PRINCIPLE-006 — Observable Frontend

Every important frontend operation SHALL support:

- Request correlation
- Error tracking
- Performance monitoring
- User interaction tracing
- API latency measurement
- AI operation tracing where appropriate

---

## 4. Frontend Technology Requirements

## FR-TECH-001 — Framework

The frontend SHALL use a modern component-based framework.

The current SalesGenie frontend SHALL support:

- Astro
- React
- TypeScript

## FR-TECH-002 — Type Safety

TypeScript SHALL be used for application logic.

Strict type checking SHALL be enabled.

## FR-TECH-003 — API Client

All backend communication SHALL occur through centralized API clients or domain-specific service clients.

Example domains:

```text
src/
├── api/
│   ├── auth/
│   ├── admin/
│   ├── sales/
│   ├── leads/
│   ├── crm/
│   ├── marketing/
│   ├── seo/
│   ├── finance/
│   ├── support/
│   ├── agents/
│   ├── rag/
│   ├── workflows/
│   ├── integrations/
│   ├── billing/
│   ├── analytics/
│   └── reports/
```

## FR-TECH-004 — Environment Configuration

Frontend configuration SHALL support:

* Development
* Test
* Staging
* Production
* Disaster recovery

Environment-specific configuration SHALL NOT contain secrets.

---

## 5. Recommended Frontend Repository Structure

```text
src/
├── app/
│   ├── routes/
│   ├── layouts/
│   ├── providers/
│   ├── middleware/
│   └── bootstrap/
│
├── components/
│   ├── ui/
│   ├── forms/
│   ├── tables/
│   ├── charts/
│   ├── dialogs/
│   ├── navigation/
│   ├── notifications/
│   ├── ai/
│   ├── command-center/
│   └── accessibility/
│
├── features/
│   ├── auth/
│   ├── admin/
│   ├── organizations/
│   ├── workplaces/
│   ├── teams/
│   ├── sales/
│   ├── leads/
│   ├── crm/
│   ├── marketing/
│   ├── seo/
│   ├── product-launch/
│   ├── advertising/
│   ├── finance/
│   ├── business-intelligence/
│   ├── support/
│   ├── omnichannel/
│   ├── agents/
│   ├── llm/
│   ├── rag/
│   ├── workflows/
│   ├── mcp/
│   ├── integrations/
│   ├── billing/
│   ├── analytics/
│   ├── reporting/
│   ├── notifications/
│   ├── search/
│   ├── developer/
│   ├── security/
│   ├── privacy/
│   ├── onboarding/
│   └── client-portal/
│
├── lib/
│   ├── api-client.ts
│   ├── auth/
│   ├── permissions/
│   ├── routing/
│   ├── websocket/
│   ├── events/
│   ├── telemetry/
│   ├── storage/
│   ├── validation/
│   ├── formatting/
│   └── utilities/
│
├── stores/
│   ├── auth-store.ts
│   ├── tenant-store.ts
│   ├── workspace-store.ts
│   ├── notification-store.ts
│   ├── ui-store.ts
│   └── ai-session-store.ts
│
├── hooks/
├── schemas/
├── types/
├── constants/
├── i18n/
├── styles/
└── tests/
```

---

## 6. User Requirements

## 6.1 General User Requirements

## UR-FE-001 — Unified Workspace

Users SHALL have a unified dashboard appropriate to their role, organization and workplace.

## UR-FE-002 — Personalized Navigation

Users SHALL see navigation items based on:

* Role
* Permissions
* Organization
* Workplace
* Subscription
* Feature entitlements
* Enabled integrations
* Assigned responsibilities

## UR-FE-003 — Fast Navigation

Users SHALL be able to navigate between frequently used modules without unnecessary page reloads.

## UR-FE-004 — Global Search

Users SHALL be able to search across authorized:

* Leads
* Contacts
* Accounts
* Opportunities
* Conversations
* Tickets
* Documents
* Agents
* Workflows
* Campaigns
* Reports
* Products
* Organizations
* Users

## UR-FE-005 — Command Center

The frontend SHALL provide an optional command palette supporting actions such as:

* Search
* Navigate
* Create lead
* Create contact
* Create campaign
* Create workflow
* Create AI agent
* Start report
* Open support conversation
* Run AI analysis

## UR-FE-006 — Responsive Interface

The frontend SHALL support:

* Desktop
* Laptop
* Tablet
* Mobile-responsive layouts

---

## 6.2 Authentication User Requirements

Users SHALL be able to:

* Sign up
* Sign in
* Sign out
* Recover password
* Reset password
* Change password
* Enable MFA
* Verify MFA
* Manage sessions
* View active sessions
* Revoke sessions
* Connect OAuth providers
* Manage account profile

Authentication SHALL communicate with the authentication backend.

---

## 6.3 Organization Requirements

Organization owners/admins SHALL be able to:

* Create organizations
* View organizations
* Configure organizations
* Manage members
* Invite users
* Remove users
* Assign roles
* Manage workspaces
* Manage teams
* Configure organization settings
* View organization usage
* View organization billing

---

## 6.4 Workplace Requirements

Users SHALL be able to:

* Switch workplaces
* View workplace dashboards
* Manage workplace members where permitted
* Configure workplace settings
* Manage teams
* Manage workplace AI agents
* Manage workplace integrations

---

## 6.5 Sales Requirements

Sales users SHALL be able to:

* View leads
* Search leads
* Generate leads
* Enrich leads
* Score leads
* Qualify leads
* Assign leads
* Route leads
* Deduplicate leads
* Verify leads
* Create contacts
* Create accounts
* Create opportunities
* Manage deals
* Manage pipelines
* Manage sales activities
* Manage sequences
* Execute outreach
* View forecasts
* View sales analytics

---

## 6.6 AI Lead Generation Requirements

Users SHALL be able to provide:

* ICP
* Industry
* Geography
* Company size
* Revenue range
* Job titles
* Technology stack
* Buyer persona
* Intent criteria
* Buying signals
* Competitive requirements

The frontend SHALL submit these criteria to backend lead-generation services.

The frontend SHALL display:

* Generated leads
* Lead confidence
* Lead score
* Company intelligence
* Person intelligence
* Intent signals
* Buying signals
* Enrichment status
* Verification status
* Data source
* Recommendation explanation

---

## 6.7 Marketing Requirements

Marketing users SHALL be able to:

* Create campaigns
* Manage audiences
* Segment audiences
* Generate content
* Schedule campaigns
* Manage email campaigns
* Manage social campaigns
* Manage advertising campaigns
* View campaign analytics
* Analyze ROI
* Optimize budgets
* Request AI recommendations

---

## 6.8 SEO Requirements

Users SHALL be able to:

* Perform SEO audits
* Research keywords
* Cluster keywords
* Analyze competitors
* Analyze backlinks
* Track rankings
* Analyze SERPs
* Identify content gaps
* Generate SEO content
* View SEO analytics
* Request AI SEO recommendations

---

## 6.9 Product Launch Intelligence Requirements

Users SHALL be able to enter product information and request:

* Market analysis
* Competitor discovery
* Competitor analysis
* Pricing analysis
* Market trend analysis
* Buyer analysis
* Market gap analysis
* Opportunity detection
* Risk analysis
* Positioning analysis
* Go-to-market recommendations
* Launch forecasts

The frontend SHALL display AI-generated recommendations with:

* Confidence
* Evidence
* Data sources
* Assumptions
* Risks
* Recommended actions

---

## 6.10 Finance Requirements

Authorized users SHALL be able to view:

* Revenue
* Expenses
* Profit
* Loss
* Cash flow
* Budgets
* Product profitability
* Product losses
* Financial forecasts
* Financial KPIs

The frontend SHALL consume backend-authoritative financial calculations.

---

## 6.11 Business Intelligence Requirements

Users SHALL be able to analyze:

* Monthly growth
* Yearly growth
* Revenue growth
* Expense growth
* Profit growth
* Loss
* Customer growth
* Product performance
* Marketing performance
* Sales performance
* Advertising performance

AI SHALL be able to provide:

* Business health score
* Growth recommendations
* Profitability recommendations
* Risk identification
* Product recommendations
* Cost optimization recommendations

---

## 6.12 Customer Support Requirements

Support users SHALL be able to:

* View tickets
* Create tickets
* Assign tickets
* Route tickets
* Respond to customers
* Transfer conversations
* Escalate conversations
* Review AI responses
* Approve AI responses
* Take over AI conversations
* Return conversations to AI
* View customer history
* View SLA status
* View sentiment
* View conversation intelligence

---

## 6.13 Omnichannel Requirements

The frontend SHALL support unified interfaces for:

* Web chat
* Email
* WhatsApp
* Facebook Messenger
* Instagram
* Telegram
* SMS
* Voice
* Social inbox

The frontend SHALL communicate with channel services through backend APIs.

---

## 6.14 AI Agent Requirements

Authorized users SHALL be able to:

* Create agents
* Configure agents
* Define agent instructions
* Select models
* Add tools
* Add knowledge bases
* Configure memory
* Configure permissions
* Configure guardrails
* Test agents
* Version agents
* Deploy agents
* Pause agents
* Monitor agents
* Review agent execution
* Configure human handoff

---

## 6.15 AI + Human Requirements

The frontend SHALL support:

```text
REQUEST
   ↓
AI PROCESSING
   ↓
CONFIDENCE
   ↓
HIGH ─────────────→ AI EXECUTION
   │
MEDIUM ───────────→ HUMAN REVIEW
   │
LOW ──────────────→ HUMAN HANDOFF
```

Users SHALL be able to:

* Review AI decisions
* Approve AI actions
* Reject AI actions
* Modify AI output
* Escalate AI output
* Take control
* Return control to AI
* Provide feedback
* View AI reasoning/evidence where policy permits

---

## 6.16 RAG Requirements

Users SHALL be able to:

* Upload documents
* Connect knowledge sources
* View ingestion status
* Search knowledge
* Browse documents
* View chunks where permitted
* View citations
* Configure knowledge permissions
* Test retrieval
* Evaluate RAG responses

The frontend SHALL display retrieval metadata returned by backend services.

---

## 6.17 Workflow Requirements

Users SHALL be able to:

* Create workflows
* Add triggers
* Add actions
* Add conditions
* Configure schedules
* Connect integrations
* Test workflows
* Run workflows
* Pause workflows
* Resume workflows
* Version workflows
* View execution logs
* Retry failed executions

---

## 6.18 Integration Requirements

Users SHALL be able to:

* Browse integrations
* Connect integrations
* Disconnect integrations
* Reauthorize integrations
* View integration health
* Configure synchronization
* View synchronization history
* View integration errors

The frontend SHALL never expose OAuth secrets or API secrets.

---

## 6.19 Billing Requirements

Users SHALL be able to:

* View plans
* Compare plans
* Subscribe
* Upgrade
* Downgrade
* Cancel
* Resume subscriptions
* View usage
* View limits
* View invoices
* Download invoices
* Manage payment methods
* Apply coupons where permitted
* Request refunds where supported

Billing state SHALL be backend authoritative.

---

## 7. Role-Based Frontend Architecture

The frontend SHALL support at minimum:

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

---

## 8. Role-Aware Navigation

The frontend SHALL calculate effective navigation from:

```text
User
  ↓
Identity
  ↓
Organization
  ↓
Workplace
  ↓
Role
  ↓
Permissions
  ↓
Feature Entitlements
  ↓
Subscription
  ↓
Navigation
```

Example:

```typescript
interface NavigationItem {
  id: string;
  label: string;
  route: string;
  requiredPermissions?: string[];
  requiredFeatures?: string[];
  requiredRoles?: string[];
  requiresSubscription?: boolean;
}
```

The frontend SHALL hide unauthorized navigation items.

Backend authorization SHALL remain mandatory.

---

## 9. Super Admin Frontend

Super Admin SHALL have access to a dedicated control center containing:

* Platform overview
* Users
* Organizations
* Workplaces
* Roles
* Permissions
* Subscriptions
* Billing
* System configuration
* Feature flags
* Platform metrics
* Infrastructure status
* Security events
* Audit logs
* Incidents
* Service health
* AI provider health
* Model usage
* Platform-wide analytics

---

## 10. Platform Admin Frontend

Platform Admin SHALL manage:

* Users
* Organizations
* Workplaces
* System configuration
* Feature flags
* Platform operations
* Platform analytics
* Service health
* Operational incidents

---

## 11. Security Admin Frontend

Security Admin SHALL have:

* Security dashboard
* Authentication events
* Access events
* Audit logs
* Threat events
* Suspicious activity
* Session management
* Security incidents
* Vulnerability status
* Security policies

---

## 12. Billing Admin Frontend

Billing Admin SHALL manage:

* Plans
* Pricing
* Subscriptions
* Usage
* Invoices
* Refunds
* Coupons
* Credits
* Revenue analytics
* Payment failures

---

## 13. Organization Admin Frontend

Organization Admin SHALL manage:

* Organization settings
* Users
* Roles
* Permissions
* Workplaces
* Teams
* Integrations
* Usage
* Billing
* Security policies

---

## 14. Sales Dashboard

The sales dashboard SHALL provide:

* Total leads
* Qualified leads
* New leads
* Lead conversion
* Pipeline value
* Open opportunities
* Won deals
* Lost deals
* Forecast
* Sales velocity
* Activity metrics
* AI recommendations

---

## 15. Lead Intelligence UI

Lead pages SHALL include:

```text
Lead
├── Identity
├── Company
├── Contact
├── ICP Fit
├── Lead Score
├── Qualification
├── Intent
├── Buying Signals
├── Company Intelligence
├── Person Intelligence
├── Enrichment
├── Verification
├── Activity
├── Communication
├── AI Recommendations
└── Audit History
```

---

## 16. CRM UI

CRM SHALL provide:

* Accounts
* Contacts
* Leads
* Opportunities
* Deals
* Activities
* Pipelines
* Tasks
* Notes
* Communication history
* Relationship history

---

## 17. Marketing Dashboard

Marketing dashboard SHALL include:

* Campaign performance
* Audience growth
* Conversion
* Engagement
* Spend
* Revenue
* ROI
* ROAS
* AI recommendations

---

## 18. SEO Dashboard

SEO dashboard SHALL include:

* Organic traffic
* Keyword rankings
* Search visibility
* Technical health
* Backlinks
* Content gaps
* Competitor position
* AI recommendations

---

## 19. Finance Dashboard

Finance dashboard SHALL include:

* Revenue
* Expenses
* Gross profit
* Net profit
* Loss
* Cash flow
* Budget utilization
* Product profitability
* Forecast
* Financial risks

---

## 20. Executive Dashboard

Executive dashboard SHALL aggregate:

```text
Sales
Marketing
Advertising
Finance
Products
Customers
Support
SEO
AI
Operations
```

The dashboard SHALL provide:

* Business health score
* Growth rate
* Revenue
* Profit
* Loss
* Expenses
* Customer growth
* Product profitability
* Marketing ROI
* Sales conversion
* Support health
* AI insights

---

## 21. AI Command Center

The frontend SHALL provide an AI command center where authorized users can:

* Ask questions
* Request analysis
* Generate reports
* Generate leads
* Analyze campaigns
* Analyze products
* Analyze competitors
* Analyze business performance
* Create workflows
* Create content
* Query knowledge
* Interact with AI agents

Example:

```text
User:
"Show me why revenue dropped this month."

Frontend
   ↓
AI API
   ↓
Analytics Services
   ↓
Sales + Marketing + Finance Data
   ↓
AI Analysis
   ↓
Frontend
   ↓
Evidence + Explanation + Recommendations
```

---

## 22. AI Response UI Requirements

AI responses SHALL support:

* Streaming
* Markdown
* Structured tables
* Charts
* Citations
* Sources
* Confidence
* Warnings
* Tool activity
* Human approval
* Feedback
* Copy
* Export
* Retry

The frontend SHALL clearly distinguish:

```text
AI Generated
Human Generated
AI Suggested
Human Approved
AI Executed
Human Executed
```

---

## 23. AI Tool Execution UI

When AI invokes tools, the frontend SHALL display appropriate status:

```text
Thinking
   ↓
Planning
   ↓
Calling Tool
   ↓
Tool Running
   ↓
Tool Result
   ↓
Reasoning
   ↓
Response
```

Sensitive internal reasoning SHALL not be exposed unless explicitly designed and approved.

---

## 24. Agent Monitoring UI

Agent observability SHALL expose:

* Agent runs
* Run status
* Duration
* Model
* Tokens
* Cost
* Tools
* Tool failures
* Retrieval
* Errors
* Human handoffs
* Success rate
* Quality score

---

## 25. Workflow Builder Frontend

The workflow builder SHALL provide a visual interface:

```text
Trigger
   ↓
Condition
   ↓
Action
   ↓
Condition
   ├── TRUE → Action
   └── FALSE → Action
```

Supported node categories:

* Trigger
* Action
* Condition
* Loop
* Delay
* AI Agent
* HTTP Request
* Integration
* Database
* Notification
* Human Approval
* MCP Tool
* Transform
* Branch
* Webhook

---

## 26. Workflow Execution UI

Users SHALL be able to inspect:

* Execution ID
* Workflow version
* Start time
* End time
* Duration
* Current node
* Completed nodes
* Failed nodes
* Inputs
* Outputs
* Error
* Retry status

---

## 27. Knowledge Management UI

Knowledge management SHALL provide:

```text
Knowledge Base
├── Documents
├── Websites
├── APIs
├── Cloud Drives
├── FAQs
├── Data Sources
├── Permissions
├── Ingestion
├── Embeddings
├── Retrieval
└── Evaluation
```

---

## 28. Document Management UI

Users SHALL be able to:

* Upload files
* Drag/drop files
* Browse documents
* Preview documents
* Delete documents
* Reprocess documents
* View processing state
* View metadata
* Configure permissions

Supported states:

```text
Uploaded
Queued
Processing
Chunking
Embedding
Indexed
Failed
Deleted
```

---

## 29. Search Architecture

Global search SHALL support:

* Exact search
* Fuzzy search
* Semantic search
* Filters
* Sorting
* Permissions
* Entity search
* Recent search
* Saved searches

Search results SHALL be filtered by backend authorization.

---

## 30. Notification Center

The frontend SHALL provide:

* In-app notifications
* Email notification status
* System alerts
* AI alerts
* Workflow alerts
* Billing alerts
* Security alerts
* Assignment notifications
* Mention notifications

Notification categories SHALL be configurable.

---

## 31. Real-Time Architecture

The frontend SHALL support:

* WebSocket
* Server-Sent Events
* Long-running job polling fallback

Real-time use cases include:

* AI streaming
* Agent execution
* Workflow execution
* Chat
* Support conversations
* Notifications
* Lead generation progress
* Report generation
* Document processing
* Integration synchronization
* Incident updates

---

## 32. Real-Time Connection Lifecycle

```text
CONNECT
  ↓
AUTHENTICATE
  ↓
SUBSCRIBE
  ↓
RECEIVE EVENTS
  ↓
UPDATE UI
  ↓
HEARTBEAT
  ↓
DISCONNECT
  ↓
RECONNECT
  ↓
RESYNC
```

The frontend SHALL recover from lost connections.

---

## 33. Event Architecture

Frontend events SHALL be treated as notifications rather than authoritative state.

Example events:

```text
user.updated
organization.updated
lead.created
lead.updated
lead.scored
lead.qualified
campaign.updated
workflow.started
workflow.completed
workflow.failed
agent.started
agent.completed
agent.failed
ticket.created
ticket.updated
message.received
document.processed
subscription.updated
payment.failed
security.alert
incident.created
```

---

## 34. API Integration Requirements

All API calls SHALL support:

* Authentication
* Authorization context
* Tenant context
* Correlation ID
* Request ID
* Timeout
* Retry policy
* Error normalization
* Rate-limit handling
* Cancellation
* Telemetry

---

## 35. API Client Architecture

Recommended structure:

```text
API Client
    │
    ├── Auth Client
    ├── Admin Client
    ├── Sales Client
    ├── Lead Client
    ├── CRM Client
    ├── Marketing Client
    ├── SEO Client
    ├── Finance Client
    ├── Support Client
    ├── Agent Client
    ├── RAG Client
    ├── Workflow Client
    ├── Integration Client
    ├── Billing Client
    ├── Analytics Client
    └── Reporting Client
```

---

## 36. Backend Connectivity Matrix

| Frontend Domain | Backend Dependency        |
| --------------- | ------------------------- |
| Authentication  | Auth Service              |
| Users           | Identity Service          |
| Organizations   | Organization Service      |
| Roles           | Authorization Service     |
| Admin           | Admin/Platform Service    |
| Sales           | Sales Service             |
| Leads           | Lead Intelligence Service |
| CRM             | CRM Service               |
| Marketing       | Marketing Service         |
| SEO             | SEO Service               |
| Product Launch  | Intelligence/AI Services  |
| Finance         | Finance Service           |
| Analytics       | Analytics Service         |
| Support         | Support Service           |
| Omnichannel     | Channel Services          |
| AI Agents       | Agent Service             |
| LLM             | LLM Gateway               |
| RAG             | Knowledge/RAG Services    |
| Workflows       | Workflow Engine           |
| MCP             | MCP Platform              |
| Integrations    | Integration Service       |
| Billing         | Billing Service           |
| Notifications   | Notification Service      |
| Search          | Search Service            |
| Reports         | Reporting Service         |
| Security        | Security Service          |
| Observability   | Observability Platform    |

---

## 37. Error Handling

The frontend SHALL normalize backend errors.

Error categories:

```text
400 Validation
401 Authentication
403 Authorization
404 Resource Not Found
409 Conflict
408 Timeout
422 Business Validation
429 Rate Limited
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```

---

## 38. Authentication Error Handling

For `401`:

```text
API Request
   ↓
401
   ↓
Attempt Token Refresh
   ↓
Success → Retry Request
   ↓
Failure → Clear Session
   ↓
Login
```

The frontend SHALL prevent infinite refresh loops.

---

## 39. Authorization Error Handling

For `403`, the frontend SHALL:

* Display an appropriate message
* Avoid exposing protected information
* Provide navigation back to authorized content
* Record telemetry
* Not retry automatically

---

## 40. Rate Limit Handling

For `429`, the frontend SHALL:

* Respect backend retry instructions
* Apply exponential backoff where appropriate
* Show user-friendly status
* Prevent request storms
* Avoid duplicate requests

---

## 41. Offline / Degraded Mode

The frontend SHALL detect:

* Network failure
* API failure
* WebSocket failure
* Service degradation

The UI SHALL distinguish:

```text
Browser Offline
Backend Unavailable
Permission Denied
Resource Missing
Request Failed
Service Degraded
```

---

## 42. Loading State Architecture

Every asynchronous feature SHALL support:

* Initial loading
* Background loading
* Empty state
* Error state
* Partial state
* Retry state
* Success state

Skeleton loaders SHALL be preferred over blocking spinners for large pages.

---

## 43. Empty State Requirements

Empty states SHALL explain:

* What is missing
* Why it is missing
* What the user can do
* Primary action

Example:

```text
No leads found.

Try:
[Generate Leads]
[Adjust Filters]
[Import Leads]
```

---

## 44. Forms Architecture

Forms SHALL support:

* Client-side validation
* Server-side validation
* Async validation
* Dirty state
* Unsaved-change detection
* Draft persistence where appropriate
* Error summaries
* Field-level errors
* Accessible labels

---

## 45. Tables

Enterprise tables SHALL support:

* Pagination
* Server-side filtering
* Sorting
* Column selection
* Search
* Bulk actions
* Row actions
* Export
* Saved views
* Virtualization where needed

---

## 46. Charts

Charts SHALL support:

* Time-series
* Bar
* Line
* Area
* Pie/donut where appropriate
* Funnel
* Scatter
* Heatmap
* KPI cards

Charts SHALL obtain data from backend analytics APIs.

---

## 47. Dashboard Architecture

Dashboards SHALL support:

* Widgets
* KPI cards
* Tables
* Charts
* AI insights
* Filters
* Date ranges
* Saved layouts
* Role-based widgets
* Organization-specific widgets
* Export

---

## 48. Dashboard Builder

Authorized users SHALL be able to:

* Add widgets
* Remove widgets
* Resize widgets
* Rearrange widgets
* Configure metrics
* Configure filters
* Save dashboard
* Share dashboard
* Duplicate dashboard

Backend SHALL validate data access.

---

## 49. Reporting Frontend

Reporting SHALL support:

* Report creation
* Report templates
* Custom reports
* Scheduled reports
* Filters
* Grouping
* Aggregations
* Charts
* Tables
* AI insights
* Export

Formats:

```text
XLSX
CSV
PDF
JSON
```

---

## 50. Export Architecture

Large exports SHALL be asynchronous.

```text
User
 ↓
Export Request
 ↓
Backend Job
 ↓
Queue
 ↓
Report Generation
 ↓
Object Storage
 ↓
Download URL
 ↓
Frontend
```

The frontend SHALL display export progress and status.

---

## 51. File Upload Architecture

Uploads SHALL support:

* Chunked uploads
* Progress
* Cancellation
* Retry
* File validation
* Virus/security scan status
* Backend processing status

Large files SHALL NOT be transmitted unnecessarily through the frontend application server.

---

## 52. Object Storage Integration

The frontend SHALL use backend-generated signed URLs or equivalent secure mechanisms for object storage.

The frontend SHALL never expose:

* Storage credentials
* Root buckets
* Internal storage credentials
* Private access keys

---

## 53. Subscription-Aware UI

The frontend SHALL consume backend feature entitlements.

Example:

```text
User
 ↓
Subscription
 ↓
Entitlements
 ↓
Feature Availability
 ↓
UI
```

The frontend SHALL support:

* Feature unavailable
* Quota exhausted
* Upgrade required
* Trial expired
* Subscription expired

---

## 54. Usage UI

Users SHALL be able to view:

* API usage
* AI usage
* Token usage
* Lead usage
* Workflow executions
* Storage usage
* Seats
* Message usage
* Support usage

Usage SHALL come from backend billing/usage services.

---

## 55. AI Cost UI

Authorized users SHALL be able to view:

* Model usage
* Token usage
* Estimated cost
* Cost by user
* Cost by organization
* Cost by agent
* Cost by workflow
* Cost by model
* Cost trends

---

## 56. Model Selection UI

AI Agent Builder users SHALL be able to select supported models based on backend-provided availability.

Example:

```text
Provider
  ↓
Model
  ↓
Capabilities
  ↓
Cost
  ↓
Latency
  ↓
Availability
```

The frontend SHALL not assume a provider/model is available.

---

## 57. Model Fallback UI

When model fallback occurs, the frontend MAY display:

```text
Primary model unavailable.
Request processed using fallback model.
```

Detailed infrastructure information SHALL be shown only to authorized users.

---

## 58. Prompt Management UI

Authorized users SHALL be able to:

* View prompts
* Create prompts
* Edit prompts
* Version prompts
* Test prompts
* Compare versions
* Evaluate prompts
* Roll back versions

---

## 59. AI Evaluation UI

AI evaluation dashboards SHALL display:

* Accuracy
* Relevance
* Groundedness
* Safety
* Hallucination rate
* Tool success
* Human approval rate
* User feedback
* Latency
* Cost

---

## 60. Agent Permissions UI

Agent permissions SHALL support:

* Tool access
* Data access
* Knowledge access
* Integration access
* Action permissions
* Human approval requirements

Example:

```text
Agent
 ├── Read CRM
 ├── Write CRM
 ├── Send Email
 ├── Generate Lead
 ├── Execute Workflow
 └── Require Human Approval
```

---

## 61. Human Approval UI

Human approval queues SHALL show:

* Request
* AI recommendation
* Confidence
* Evidence
* Proposed action
* Risk
* Required permission
* Approve
* Reject
* Modify
* Escalate

---

## 62. Audit UI

Authorized users SHALL be able to view:

* User actions
* Admin actions
* AI actions
* Agent actions
* Workflow actions
* Security events
* Billing actions
* Configuration changes

Audit logs SHALL be read-only from the frontend unless backend explicitly supports controlled remediation.

---

## 63. Security Frontend Requirements

The frontend SHALL implement:

* Secure authentication handling
* CSP-compatible architecture
* XSS protections
* CSRF protections where applicable
* Secure cookies where applicable
* Input validation
* Output escaping
* Dependency security
* Secure iframe policy
* Clickjacking protections
* Sensitive-data masking

---

## 64. Secrets Handling

The frontend SHALL NEVER contain:

```text
Database passwords
Private API keys
Cloud credentials
JWT signing secrets
OAuth client secrets
Encryption keys
Webhook signing secrets
Payment secrets
```

---

## 65. Local Storage Requirements

Local storage SHALL only contain non-sensitive information such as:

* Theme preference
* Language preference
* UI preferences

Authentication tokens SHALL use the most secure architecture supported by the authentication design.

---

## 66. Session Management

Frontend SHALL support:

* Session initialization
* Token refresh
* Session expiration
* Logout
* Multi-tab synchronization
* Session revocation
* Idle timeout where required

---

## 67. Multi-Tab Synchronization

Authentication state SHALL remain consistent across tabs.

Example:

```text
Tab A Logout
     ↓
Broadcast
     ↓
Tab B
     ↓
Session Cleared
```

---

## 68. Tenant Context

Frontend SHALL maintain explicit application context:

```text
User
 ↓
Organization
 ↓
Workplace
 ↓
Team
```

Changing organization/workplace SHALL trigger appropriate backend context refresh.

---

## 69. Permission Cache

Permission information MAY be cached temporarily for UX.

The frontend SHALL refresh permission state after:

* Login
* Role change
* Organization switch
* Workplace switch
* Session refresh
* Permission update

---

## 70. Internationalization

Frontend SHALL support:

* English
* Future languages
* Locale-aware dates
* Locale-aware numbers
* Currency formatting
* Time zones
* RTL where required

Language preference SHALL persist across sessions.

---

## 71. Accessibility Requirements

The frontend SHALL target:

* WCAG 2.2 AA
* Keyboard navigation
* Screen reader compatibility
* Focus management
* Color-independent status
* Accessible forms
* Accessible dialogs
* Accessible tables
* Accessible charts
* Reduced motion

---

## 72. Performance Requirements

Frontend SHALL optimize:

* First Contentful Paint
* Largest Contentful Paint
* Interaction to Next Paint
* JavaScript bundle size
* CSS size
* Image size
* API request count
* API payload size
* Rendering cost

---

## 73. Code Splitting

Large domains SHALL be lazy-loaded.

Example:

```text
Core Shell
   ↓
Load Sales Module
Load Marketing Module
Load SEO Module
Load AI Module
Load Admin Module
```

Only required code SHALL be loaded where practical.

---

## 74. Caching

Frontend caching SHALL distinguish:

```text
Static Assets
Public Data
User Data
Tenant Data
Sensitive Data
Real-Time Data
```

Sensitive data SHALL not be cached insecurely.

---

## 75. Server State

Server state SHALL be managed separately from local UI state.

Examples:

```text
Server State:
- Leads
- Users
- Campaigns
- Tickets
- Agents
- Workflows
- Billing

Client State:
- Modal state
- Sidebar state
- Selected rows
- Theme
- Temporary UI state
```

---

## 76. Optimistic UI

Optimistic updates MAY be used for low-risk operations.

They SHALL NOT be used blindly for:

* Payments
* Permissions
* Security changes
* Subscription changes
* Financial transactions
* Irreversible actions

---

## 77. Idempotency

Frontend requests that can trigger duplicate side effects SHALL use backend-supported idempotency mechanisms.

Examples:

* Payments
* Workflow execution
* Campaign sending
* Bulk operations
* Agent actions

---

## 78. Bulk Operations

Bulk operations SHALL support:

* Selection
* Validation
* Confirmation
* Progress
* Partial success
* Failure reporting
* Retry

Example:

```text
100 Leads Selected
 ↓
Backend Job
 ↓
72 Success
20 Failed
8 Skipped
```

---

## 79. Confirmation Requirements

High-risk actions SHALL require confirmation.

Examples:

* Delete organization
* Delete user
* Remove integration
* Cancel subscription
* Send mass campaign
* Execute high-risk AI action
* Change security policy

---

## 80. Undo Architecture

Undo SHALL be supported where backend operations permit reversible transactions.

Frontend SHALL not fake undo for irreversible backend actions.

---

## 81. Notifications and Toasts

Toasts SHALL be used for:

* Success
* Minor warnings
* Background completion
* Non-blocking failures

Critical actions SHALL use persistent dialogs or notification center entries.

---

## 82. Global Error Boundary

The frontend SHALL provide:

* Application error boundary
* Route-level error boundary
* Feature-level error boundary
* Recovery UI
* Error telemetry

A failure in one domain SHALL not crash the entire application where practical.

---

## 83. Observability Requirements

Frontend telemetry SHALL capture:

* Page views
* Route transitions
* API latency
* API failures
* JavaScript errors
* Component errors
* WebSocket failures
* User interaction latency
* AI latency
* Workflow latency

Sensitive user content SHALL not be automatically captured.

---

## 84. Distributed Tracing

Frontend requests SHALL propagate correlation metadata when supported.

Example:

```text
Browser
 ↓
API Gateway
 ↓
Service
 ↓
Database
 ↓
AI Gateway
 ↓
LLM
```

The same trace/correlation context SHOULD be available to backend observability systems.

---

## 85. Frontend Metrics

Minimum metrics:

```text
frontend.page_load_time
frontend.route_transition_time
frontend.api_latency
frontend.api_error_rate
frontend.js_error_rate
frontend.websocket_disconnects
frontend.ai_response_latency
frontend.workflow_ui_latency
frontend.interaction_latency
```

---

## 86. Feature Flags

Frontend SHALL support backend-controlled feature flags.

Feature flags SHALL support:

* Global
* Environment
* Organization
* Workplace
* User
* Role
* Percentage rollout

Security-critical authorization SHALL NOT rely solely on feature flags.

---

## 87. Progressive Rollouts

Frontend SHALL support:

```text
Development
 ↓
Internal
 ↓
Canary
 ↓
Small Percentage
 ↓
Larger Percentage
 ↓
100%
```

---

## 88. Deployment Compatibility

Frontend SHALL support backend version compatibility.

The application SHALL handle:

* API version differences
* Deprecated fields
* Feature negotiation
* Graceful degradation

---

## 89. API Versioning

The frontend SHALL use explicit API versions where backend architecture requires them.

Example:

```text
/api/v1/
/api/v2/
```

API contracts SHALL be generated or centrally maintained where practical.

---

## 90. Contract Safety

Frontend CI SHALL validate:

* API schemas
* Response types
* Request types
* Required fields
* Deprecated fields
* Error schemas

---

## 91. Security Headers Compatibility

Frontend deployment SHALL support:

* Content-Security-Policy
* HSTS
* X-Content-Type-Options
* Referrer-Policy
* Permissions-Policy
* Frame restrictions

---

## 92. Content Security Policy

The frontend SHALL avoid unnecessary:

* Inline scripts
* Inline event handlers
* Unsafe eval
* Unknown third-party scripts

External resources SHALL be explicitly allowlisted.

---

## 93. Third-Party Script Management

Third-party scripts SHALL be:

* Reviewed
* Version-controlled
* Permission-scoped
* Monitored
* Loaded only when necessary

---

## 94. Privacy Requirements

Frontend SHALL support:

* Cookie preferences
* Consent management
* Data export requests
* Account deletion requests
* Privacy settings
* Tracking preferences

---

## 95. Data Masking

Sensitive fields SHALL support masking.

Examples:

```text
Email
Phone
Payment information
API keys
Security tokens
Personal information
```

---

## 96. Customer Portal

External clients SHALL receive a separate restricted experience.

Customer portal SHALL provide:

* Client dashboard
* Projects
* Reports
* Analytics
* Billing
* Support
* AI agents
* Integrations
* Documents
* Team management where permitted

---

## 97. Client Isolation

External clients SHALL never access:

* Platform administration
* Other organizations
* Internal users
* Internal audit data
* Internal infrastructure
* Other clients
* Unauthorized AI agents
* Unauthorized knowledge bases

---

## 98. Onboarding Frontend

Onboarding SHALL support:

```text
Account
 ↓
Organization
 ↓
Workplace
 ↓
Team
 ↓
Role
 ↓
Product Configuration
 ↓
Integrations
 ↓
Knowledge Base
 ↓
AI Agent
 ↓
First Workflow
 ↓
First Business Result
```

---

## 99. Guided Setup

The frontend SHALL provide:

* Setup checklist
* Progress indicators
* Contextual help
* Recommended configuration
* AI-assisted setup
* Validation
* Completion tracking

---

## 100. AI-Assisted Onboarding

AI MAY assist with:

* ICP creation
* Agent configuration
* Knowledge ingestion
* Workflow generation
* Campaign creation
* Dashboard setup
* Integration configuration

All consequential actions SHALL respect authorization and approval policies.

---

## 101. Mobile Readiness

Frontend architecture SHALL avoid desktop-only assumptions.

Mobile future support SHALL include:

* Responsive layouts
* Touch interactions
* Mobile navigation
* Push notification compatibility
* Mobile-safe tables
* Mobile-safe AI chat
* Mobile-safe approval workflows

---

## 102. State Machine Requirements

Critical frontend workflows SHALL use explicit state machines where complexity requires them.

Example:

```text
Lead:
DISCOVERED
 ↓
ENRICHING
 ↓
ENRICHED
 ↓
VERIFYING
 ↓
VERIFIED
 ↓
SCORED
 ↓
QUALIFIED
 ↓
ASSIGNED
 ↓
CONTACTED
 ↓
CONVERTED
```

Frontend SHALL render backend-provided state rather than independently deriving authoritative business state.

---

## 103. AI Job State

AI jobs SHALL support:

```text
QUEUED
RUNNING
WAITING_FOR_TOOL
WAITING_FOR_HUMAN
COMPLETED
FAILED
CANCELLED
TIMED_OUT
```

---

## 104. Report Job State

```text
REQUESTED
QUEUED
GENERATING
UPLOADING
READY
FAILED
EXPIRED
```

---

## 105. Workflow State

```text
DRAFT
VALIDATING
ACTIVE
PAUSED
RUNNING
FAILED
COMPLETED
ARCHIVED
```

---

## 106. Integration State

```text
DISCONNECTED
CONNECTING
CONNECTED
SYNCING
DEGRADED
AUTH_REQUIRED
ERROR
DISCONNECTED_BY_USER
```

---

## 107. Security Session State

```text
ACTIVE
EXPIRING
EXPIRED
REVOKED
LOCKED
```

---

## 108. Search Permission Requirements

Search UI SHALL never display unauthorized entities.

Backend SHALL perform final authorization filtering.

---

## 109. URL State

URL parameters MAY store:

* Filters
* Search query
* Sort
* Pagination
* Tab
* Date range
* View

Sensitive information SHALL NOT be placed in URLs.

---

## 110. Deep Linking

Users SHALL be able to directly access authorized resources.

Examples:

```text
/leads/{id}
/contacts/{id}
/accounts/{id}
/opportunities/{id}
/agents/{id}
/workflows/{id}
/tickets/{id}
/reports/{id}
```

---

## 111. Breadcrumbs

Complex enterprise pages SHALL provide breadcrumbs.

Example:

```text
Organization
  > Workplace
    > Sales
      > Leads
        > Lead
```

---

## 112. Navigation Architecture

Primary navigation SHOULD include:

```text
Home
AI Command Center
Sales
Marketing
SEO
Product Intelligence
Advertising
Finance
Business Intelligence
Support
AI Agents
Knowledge
Workflows
Integrations
Reports
Analytics
Notifications
Administration
Developer
Security
Billing
```

Only authorized/entitled items SHALL appear.

---

## 113. Global Header

Header SHALL support:

* Organization switcher
* Workplace switcher
* Search
* Command palette
* Notifications
* Help
* AI assistant
* User menu

---

## 114. User Menu

User menu SHALL provide:

* Profile
* Account settings
* Security
* Sessions
* Preferences
* Language
* Theme
* Billing where permitted
* Logout

---

## 115. Workspace Switcher

Workspace switcher SHALL retrieve available contexts from backend.

It SHALL not allow arbitrary tenant/workplace IDs.

---

## 116. Permission-Aware Components

Reusable components SHALL support permissions.

Example:

```tsx
<PermissionGate permission="lead.create">
  <CreateLeadButton />
</PermissionGate>
```

This SHALL only affect UI visibility.

Backend authorization remains mandatory.

---

## 117. Entitlement-Aware Components

Example:

```tsx
<FeatureGate feature="advanced_lead_intelligence">
  <LeadIntelligencePanel />
</FeatureGate>
```

---

## 118. AI Confidence UI

Confidence indicators SHALL avoid misleading precision.

Recommended categories:

```text
High Confidence
Medium Confidence
Low Confidence
Unknown
```

Where numerical confidence is shown, the UI SHALL explain its meaning.

---

## 119. AI Evidence UI

AI recommendations SHOULD provide:

* Source
* Timestamp
* Data used
* Supporting signals
* Confidence
* Limitations

---

## 120. AI Safety UI

The frontend SHALL display safety warnings for:

* Potentially destructive actions
* Sensitive data operations
* External communications
* High-impact decisions
* Unverified information
* Low-confidence recommendations

---

## 121. Human Review Queue

Review queue SHALL support:

* Priority
* SLA
* Assignee
* AI confidence
* Risk
* Age
* Status
* Filters
* Bulk assignment

---

## 122. Human Handoff

Support and AI-agent interfaces SHALL allow:

```text
AI
 ↓
Human Handoff
 ↓
Human Agent
 ↓
Resolution
 ↓
AI Return
```

---

## 123. Feedback Architecture

Users SHALL be able to provide:

* Thumbs up/down
* Rating
* Structured feedback
* Free-text feedback
* Incorrect answer report
* AI hallucination report
* Tool failure report

Feedback SHALL be sent to backend evaluation systems.

---

## 124. Frontend Testing Requirements

The frontend SHALL implement:

* Unit tests
* Component tests
* Integration tests
* API contract tests
* E2E tests
* Accessibility tests
* Visual regression tests
* Performance tests
* Security tests
* AI UI tests

---

## 125. Unit Testing

Unit tests SHALL cover:

* Utilities
* Validation
* State logic
* Permission helpers
* Formatters
* API transformations
* UI state machines

---

## 126. Integration Testing

Integration tests SHALL cover:

* Authentication
* API clients
* Role-based navigation
* Tenant switching
* Billing
* AI streaming
* WebSocket handling
* File uploads
* Workflow UI

---

## 127. E2E Testing

Critical journeys SHALL include:

```text
Signup
Login
MFA
Organization creation
User invitation
Role assignment
Lead generation
Lead qualification
CRM workflow
Campaign creation
AI agent creation
Knowledge ingestion
Workflow execution
Support handoff
Subscription upgrade
Report generation
Logout
```

---

## 128. Accessibility Testing

CI SHALL validate:

* Keyboard navigation
* ARIA
* Focus
* Labels
* Contrast
* Screen reader compatibility
* Form accessibility
* Dialog accessibility

---

## 129. Visual Regression

Critical pages SHALL have visual regression coverage:

* Login
* Dashboard
* Lead page
* CRM
* AI agent builder
* Workflow builder
* Support inbox
* Billing
* Admin dashboard

---

## 130. Frontend Performance Budgets

The frontend SHALL define budgets for:

```text
Initial JS
Route JS
CSS
Images
Fonts
API payloads
Largest content
Interaction latency
```

CI SHOULD fail builds that significantly exceed approved budgets.

---

## 131. Security Testing

Frontend security testing SHALL include:

* XSS
* CSRF
* CSP
* Dependency vulnerabilities
* Authorization bypass attempts
* Sensitive data exposure
* Token leakage
* Open redirects
* Clickjacking
* DOM vulnerabilities

---

## 132. AI UI Testing

AI interfaces SHALL test:

* Streaming
* Tool execution
* Error handling
* Timeout
* Retry
* Human approval
* Hallucination reporting
* Citation rendering
* Long responses
* Concurrent requests

---

## 133. WebSocket Testing

Tests SHALL include:

* Connection
* Authentication
* Subscription
* Event reception
* Disconnect
* Reconnect
* Duplicate event handling
* Out-of-order events
* Resynchronization

---

## 134. API Failure Testing

Frontend SHALL be tested against:

```text
401
403
404
409
422
429
500
502
503
504
Timeout
Network Offline
```

---

## 135. Browser Compatibility

The frontend SHALL support current versions of:

* Chrome
* Firefox
* Safari
* Edge

Mobile browser compatibility SHALL be considered for responsive interfaces.

---

## 136. Browser Security

The frontend SHALL avoid:

* `eval`
* Unsafe dynamic script execution
* Untrusted HTML injection
* Unsanitized rich text
* Untrusted iframe embedding

---

## 137. Rich Text Security

AI-generated and user-generated HTML SHALL be sanitized before rendering.

Markdown rendering SHALL use a trusted/sanitized pipeline.

---

## 138. File Security

Uploaded files SHALL be treated as untrusted.

Frontend SHALL not assume:

* File extension is trustworthy
* MIME type is trustworthy
* File content is safe

Backend security scanning SHALL be authoritative.

---

## 139. Audit Correlation

High-value UI operations SHOULD propagate:

```text
user_id
organization_id
workplace_id
request_id
trace_id
operation_id
```

Where appropriate and without exposing sensitive information.

---

## 140. Idempotent Navigation

Repeated navigation actions SHALL not trigger unnecessary duplicate backend mutations.

---

## 141. Request Cancellation

Long-running frontend requests SHALL support cancellation.

Examples:

* AI generation
* Lead generation
* Search
* Reports
* Large queries

---

## 142. Pagination

Large backend collections SHALL use server-side pagination.

Frontend SHALL support:

* Cursor pagination
* Offset pagination where appropriate
* Infinite scrolling
* Virtualized rendering

---

## 143. Data Freshness

The frontend SHALL distinguish:

```text
Fresh
Stale
Refreshing
Unavailable
```

Stale data SHALL not be presented as real-time data.

---

## 144. Real-Time Data Indicators

Where appropriate, UI SHALL display:

```text
Live
Updated X seconds ago
Refreshing
Offline
```

---

## 145. Search Debouncing

Search inputs SHALL use debouncing where appropriate to prevent excessive API requests.

---

## 146. Request Deduplication

Identical concurrent requests SHOULD be deduplicated.

---

## 147. Retry Policy

Retries SHALL be applied only to safe/idempotent operations unless backend explicitly supports idempotency.

---

## 148. Frontend Rate Protection

The frontend SHALL prevent:

* Double clicks
* Request storms
* Infinite polling
* Duplicate submissions
* Duplicate workflow execution

---

## 149. Polling

Polling SHALL have:

* Maximum duration
* Backoff
* Cancellation
* Visibility awareness
* Failure handling

WebSocket/SSE SHOULD be preferred where appropriate.

---

## 150. Background Processing

Long operations SHALL use backend jobs.

The frontend SHALL display:

```text
Queued
Processing
Progress
Completed
Failed
```

---

## 151. Multi-Service Failure Handling

If one backend service fails, unrelated modules SHOULD remain operational.

Example:

```text
Marketing Service DOWN

Sales        → Available
CRM          → Available
Billing      → Available
Marketing    → Degraded
```

---

## 152. Service Health UI

Authorized administrators SHALL be able to view:

* Service status
* API health
* Dependency health
* Latency
* Error rate
* Incident state

---

## 153. Incident Management UI

Administrators SHALL be able to:

* View incidents
* Acknowledge incidents
* Assign incidents
* Update status
* Add notes
* View affected services
* View timeline

---

## 154. Feature Degradation

Frontend SHALL support graceful degradation.

Example:

```text
AI Service Unavailable

→ Existing CRM remains available
→ Manual lead management remains available
→ AI buttons disabled
→ Retry option displayed
```

---

## 155. Design System

SalesGenie SHALL maintain a centralized design system containing:

* Colors
* Typography
* Spacing
* Icons
* Buttons
* Inputs
* Tables
* Cards
* Modals
* Dropdowns
* Tabs
* Navigation
* Alerts
* Charts
* AI components

---

## 156. Component Standards

Reusable components SHALL have:

* Typed props
* Accessibility support
* Loading state
* Error state where appropriate
* Documentation
* Unit tests

---

## 157. Design Tokens

Design tokens SHALL be centralized.

Example:

```text
Typography
Spacing
Radius
Shadows
Breakpoints
Motion
Z-index
Colors
```

---

## 158. Theme Architecture

Frontend SHALL support:

* Light
* Dark
* System

Theme preference MAY persist locally.

---

## 159. Localization Architecture

Translation keys SHALL be centralized.

Example:

```text
i18n/
├── en/
├── bn/
├── es/
└── ...
```

---

## 160. Date and Time

All timestamps SHALL be interpreted consistently.

Frontend SHALL support:

* User timezone
* Organization timezone
* UTC backend timestamps
* Locale-aware formatting

---

## 161. Currency

Financial values SHALL use backend-provided currency metadata.

Frontend SHALL not assume a default currency for financial calculations.

---

## 162. Data Formatting

Formatting SHALL be centralized for:

* Currency
* Percentages
* Dates
* Numbers
* Durations
* File sizes
* Token counts

---

## 163. Accessibility of AI

AI interfaces SHALL support:

* Screen readers
* Keyboard operation
* Focus management
* Streaming announcements where appropriate
* Accessible status messages

---

## 164. Accessibility of Charts

Charts SHALL provide:

* Accessible summaries
* Tabular alternatives
* Keyboard access where applicable

---

## 165. Accessibility of Tables

Tables SHALL support:

* Headers
* Scope
* Keyboard navigation
* Row actions
* Responsive alternatives

---

## 166. Frontend Documentation

Frontend architecture SHALL document:

* Component usage
* API usage
* State management
* Routing
* Permissions
* Feature flags
* Error handling
* Testing
* Deployment

---

## 167. Developer Experience

Developers SHALL have:

* Local development environment
* Environment templates
* Type checking
* Linting
* Formatting
* Unit tests
* E2E tests
* API mocks
* Storybook/design-system environment where applicable

---

## 168. CI Requirements

CI SHALL execute:

```text
Install
 ↓
Type Check
 ↓
Lint
 ↓
Unit Tests
 ↓
Component Tests
 ↓
API Contract Tests
 ↓
Build
 ↓
Accessibility Tests
 ↓
Security Checks
 ↓
E2E Tests
 ↓
Artifact Generation
```

---

## 169. Build Requirements

Production build SHALL:

* Fail on type errors
* Fail on critical lint errors
* Fail on broken imports
* Fail on invalid configuration
* Validate environment requirements
* Generate immutable artifacts

---

## 170. Deployment Architecture

Recommended:

```text
User
 ↓
CDN
 ↓
Load Balancer
 ↓
Frontend Application
 ↓
API Gateway
 ↓
Backend Services
```

Static assets SHOULD be served through CDN.

---

## 171. CDN Requirements

CDN SHALL serve:

* JavaScript
* CSS
* Images
* Fonts
* Static assets

Sensitive API responses SHALL not be publicly cached.

---

## 172. Frontend Deployment Environments

Required:

```text
local
development
test
staging
production
disaster-recovery
```

---

## 173. Environment Isolation

Environment configuration SHALL prevent:

```text
Development → Production API
Test → Production Database
Staging → Production Credentials
```

unless explicitly controlled and authorized.

---

## 174. Runtime Configuration

Where runtime configuration is required, frontend SHALL obtain only non-secret configuration.

Example:

```text
API Base URL
Environment
Feature Flag Endpoint
Public Analytics ID
Public Configuration
```

---

## 175. Source Maps

Production source maps SHALL be handled securely.

They SHALL not expose sensitive information.

---

## 176. Frontend Logging

Logs SHALL avoid:

* Passwords
* Tokens
* API keys
* Personal sensitive information
* Private customer content
* Authentication secrets

---

## 177. Error Reporting

Errors SHALL contain enough context to debug:

* Route
* Browser
* Version
* Request ID
* Trace ID
* Feature
* Error category

Sensitive content SHALL be redacted.

---

## 178. Version Display

Frontend SHALL expose application version where useful for support and debugging.

Example:

```text
SalesGenie vX.Y.Z
Environment: Production
```

---

## 179. Release Compatibility

Frontend releases SHALL support rollback.

The system SHALL allow:

```text
Version N
 ↓
Version N+1
 ↓
Problem
 ↓
Rollback to N
```

---

## 180. Backend Compatibility

Frontend SHALL gracefully handle backend deployments where old and new versions coexist.

---

## 181. API Gateway Connectivity

The frontend SHOULD communicate through a controlled API Gateway/BFF rather than directly connecting to every internal microservice.

Preferred:

```text
Frontend
   ↓
API Gateway / BFF
   ↓
Microservices
```

Not preferred:

```text
Frontend
 ├── Service A
 ├── Service B
 ├── Service C
 ├── Service D
 └── Service E
```

Internal services SHOULD remain inaccessible directly from public browsers.

---

## 182. Frontend BFF Requirements

Where required, BFF SHALL handle:

* Aggregation
* Backend-specific authentication
* API composition
* Response shaping
* Pagination
* Caching
* Authorization context
* Version compatibility

---

## 183. Aggregated Dashboard API

Dashboards SHOULD use backend aggregation rather than issuing dozens of browser requests.

Example:

```text
Dashboard Request
       ↓
BFF
 ├── Sales
 ├── Marketing
 ├── Finance
 ├── Support
 └── Analytics
       ↓
Aggregated Response
```

---

## 184. API Payload Optimization

Backend APIs SHOULD provide:

* Field selection
* Pagination
* Aggregation
* Compression
* Incremental updates

Frontend SHALL avoid requesting unnecessary fields.

---

## 185. GraphQL / REST Compatibility

The architecture MAY support:

* REST
* GraphQL
* WebSocket
* SSE

The frontend abstraction layer SHOULD hide protocol-specific implementation from feature components.

---

## 186. MCP Frontend

Authorized developers and AI Agent Builders SHALL be able to:

* Browse MCP servers
* Browse MCP tools
* Configure MCP connections
* View permissions
* Test tools
* View execution logs
* Enable/disable tools

---

## 187. Developer Portal

Developer frontend SHALL support:

* API documentation
* API keys
* OAuth applications
* Webhooks
* SDKs
* Sandbox
* Usage
* Logs
* API versioning

---

## 188. API Key Security UI

API keys SHALL be:

* Created
* Rotated
* Revoked
* Scoped
* Expired

The full secret SHOULD only be displayed at creation where appropriate.

---

## 189. Webhook UI

Developers SHALL be able to:

* Create webhook
* Configure events
* Rotate secret
* Test webhook
* View delivery attempts
* Retry failed delivery

---

## 190. Integration Health UI

Integration status SHALL show:

```text
Connected
Healthy
Syncing
Degraded
Authentication Required
Error
Disconnected
```

---

## 191. Customer Support Inbox

Support inbox SHALL support:

* Queue
* Assignment
* Filters
* SLA
* Customer context
* AI suggestions
* Conversation history
* Internal notes
* Handoff
* Escalation

---

## 192. Conversation UI

Conversation interface SHALL show:

```text
Customer
 ↓
Channel
 ↓
Messages
 ↓
AI/Human attribution
 ↓
Attachments
 ↓
Sentiment
 ↓
Intent
 ↓
Suggested Actions
```

---

## 193. AI Suggested Reply

AI-generated replies SHALL provide:

* Generate
* Edit
* Approve
* Send
* Regenerate
* Reject

The AI SHALL NOT automatically send messages unless backend policy allows it.

---

## 194. Bulk Import

Users SHALL be able to import:

* Leads
* Contacts
* Accounts
* Products
* Data

Import flow:

```text
Upload
 ↓
Validate
 ↓
Preview
 ↓
Map Fields
 ↓
Deduplicate
 ↓
Confirm
 ↓
Import
 ↓
Results
```

---

## 195. Import Results

Results SHALL include:

```text
Total
Imported
Updated
Skipped
Duplicated
Failed
```

---

## 196. Data Validation

Frontend validation SHALL improve UX.

Backend SHALL perform authoritative validation.

---

## 197. Data Export

Authorized users SHALL be able to export permitted data.

Exports SHALL respect:

* Permissions
* Tenant isolation
* Data privacy
* Subscription limits
* Rate limits

---

## 198. Auditability of Export

Sensitive exports SHOULD create backend audit events.

---

## 199. Security-Critical UI

Security-sensitive actions SHALL use:

* Confirmation
* Re-authentication where required
* MFA where required
* Clear warnings
* Audit logging

---

## 200. Reauthentication UI

For high-risk operations:

```text
Action
 ↓
Reauthentication
 ↓
MFA
 ↓
Confirmation
 ↓
Backend
```

---

## 201. Account Deletion

Account deletion UI SHALL:

* Explain consequences
* Confirm identity where required
* Confirm irreversible actions
* Submit deletion request to backend
* Show deletion status

---

## 202. Data Subject Request UI

Where compliance requires, users SHALL be able to request:

* Data export
* Data deletion
* Data correction
* Consent withdrawal

---

## 203. Admin Impersonation

If platform policy permits impersonation:

* It SHALL be backend-authorized.
* It SHALL require explicit permissions.
* It SHALL be strongly audited.
* The frontend SHALL clearly display impersonation state.
* Sensitive operations MAY require additional confirmation.

---

## 204. Impersonation Banner

Example:

```text
⚠ IMPERSONATION MODE

You are viewing this account as:
user@example.com

[Exit Impersonation]
```

---

## 205. Accessibility-Friendly Error Messages

Errors SHALL:

* Identify problem
* Explain corrective action
* Be announced appropriately
* Avoid technical jargon for end users

---

## 206. User Experience Analytics

Frontend MAY capture product analytics for:

* Feature adoption
* Funnel conversion
* Onboarding completion
* Search usage
* AI usage
* Workflow usage
* Dashboard usage

Analytics SHALL respect privacy/consent policies.

---

## 207. Product Analytics

Important events:

```text
user.signup
user.login
onboarding.started
onboarding.completed
lead.generated
lead.qualified
campaign.created
agent.created
agent.deployed
workflow.created
workflow.executed
report.created
subscription.upgraded
```

---

## 208. Frontend Event Naming

Events SHALL use standardized names.

Recommended:

```text
domain.entity.action
```

Example:

```text
sales.lead.created
sales.lead.qualified
ai.agent.deployed
workflow.execution.completed
billing.subscription.upgraded
```

---

## 209. Event Payload Governance

Frontend event payloads SHALL:

* Be versioned
* Avoid sensitive information
* Follow schema
* Be backward compatible

---

## 210. Data Privacy in Analytics

Frontend analytics SHALL NOT automatically capture:

* Passwords
* Tokens
* Full customer conversations
* Sensitive financial information
* Private documents
* Secrets

---

## 211. Session Replay

If enabled, session replay SHALL:

* Mask sensitive fields
* Respect consent
* Exclude confidential screens
* Support opt-out

---

## 212. Frontend Architecture Quality Gates

A feature SHALL NOT be considered production-ready until it has:

```text
UI
+
API Integration
+
Authentication
+
Authorization
+
Loading State
+
Empty State
+
Error State
+
Accessibility
+
Responsive Design
+
Telemetry
+
Testing
+
Security Review
```

---

## 213. Definition of Done

Every frontend feature SHALL satisfy:

* Type-safe implementation
* API contract implemented
* Permission checks implemented
* Backend integration verified
* Error handling implemented
* Loading states implemented
* Empty states implemented
* Accessibility verified
* E2E coverage where critical
* Telemetry implemented
* Security reviewed
* Documentation updated

---

## 214. Functional Requirements Summary

## Authentication

```text
FR-AUTH-001 Login
FR-AUTH-002 Signup
FR-AUTH-003 Logout
FR-AUTH-004 Token refresh
FR-AUTH-005 MFA
FR-AUTH-006 Password recovery
FR-AUTH-007 Session management
FR-AUTH-008 OAuth
```

## Administration

```text
FR-ADMIN-001 User management
FR-ADMIN-002 Organization management
FR-ADMIN-003 Workplace management
FR-ADMIN-004 Role management
FR-ADMIN-005 Permission management
FR-ADMIN-006 Feature flags
FR-ADMIN-007 Audit logs
FR-ADMIN-008 System monitoring
FR-ADMIN-009 Incident management
```

## Sales

```text
FR-SALES-001 Lead generation
FR-SALES-002 Lead discovery
FR-SALES-003 Lead enrichment
FR-SALES-004 Lead scoring
FR-SALES-005 Lead qualification
FR-SALES-006 Lead routing
FR-SALES-007 Lead assignment
FR-SALES-008 Lead deduplication
FR-SALES-009 CRM
FR-SALES-010 Pipeline
FR-SALES-011 Opportunities
FR-SALES-012 Forecasting
FR-SALES-013 Sales analytics
```

## Marketing

```text
FR-MKT-001 Campaigns
FR-MKT-002 Audiences
FR-MKT-003 Segmentation
FR-MKT-004 Content generation
FR-MKT-005 Email
FR-MKT-006 Social
FR-MKT-007 Advertising
FR-MKT-008 Analytics
FR-MKT-009 Attribution
FR-MKT-010 ROI
```

## SEO

```text
FR-SEO-001 Audit
FR-SEO-002 Keyword research
FR-SEO-003 Keyword clustering
FR-SEO-004 Competitor analysis
FR-SEO-005 Backlink analysis
FR-SEO-006 SERP analysis
FR-SEO-007 Rank tracking
FR-SEO-008 Content gap analysis
FR-SEO-009 SEO content generation
```

## AI

```text
FR-AI-001 AI assistant
FR-AI-002 Agent builder
FR-AI-003 Agent deployment
FR-AI-004 Agent testing
FR-AI-005 Agent monitoring
FR-AI-006 Tool execution
FR-AI-007 Memory
FR-AI-008 Guardrails
FR-AI-009 Human handoff
FR-AI-010 Human approval
FR-AI-011 AI evaluation
```

## RAG

```text
FR-RAG-001 Document upload
FR-RAG-002 Ingestion monitoring
FR-RAG-003 Knowledge search
FR-RAG-004 Semantic search
FR-RAG-005 Hybrid search
FR-RAG-006 Retrieval evaluation
FR-RAG-007 Citation rendering
FR-RAG-008 Knowledge permissions
```

## Workflow

```text
FR-WF-001 Workflow builder
FR-WF-002 Triggers
FR-WF-003 Actions
FR-WF-004 Conditions
FR-WF-005 Scheduling
FR-WF-006 Execution
FR-WF-007 Retry
FR-WF-008 Versioning
FR-WF-009 Monitoring
FR-WF-010 Human approval
```

## Billing

```text
FR-BILL-001 Plans
FR-BILL-002 Subscription
FR-BILL-003 Upgrade
FR-BILL-004 Downgrade
FR-BILL-005 Usage
FR-BILL-006 Invoices
FR-BILL-007 Payment methods
FR-BILL-008 Refunds
FR-BILL-009 Credits
FR-BILL-010 Entitlements
```

## Reporting

```text
FR-REPORT-001 Dashboards
FR-REPORT-002 Custom reports
FR-REPORT-003 Scheduled reports
FR-REPORT-004 Charts
FR-REPORT-005 Tables
FR-REPORT-006 AI insights
FR-REPORT-007 XLSX export
FR-REPORT-008 CSV export
FR-REPORT-009 PDF export
FR-REPORT-010 JSON export
```

---

## 215. System Requirements

## SR-FE-001 — Architecture

The frontend SHALL use a modular architecture supporting independent domain development.

## SR-FE-002 — Scalability

The architecture SHALL support:

* Millions of users
* Large tenant counts
* Large datasets
* High-frequency API requests
* Concurrent AI sessions
* Concurrent support conversations

## SR-FE-003 — Availability

Frontend deployment SHALL support high availability through:

* CDN
* Multiple application instances
* Load balancing
* Health checks
* Automated deployment
* Rollback

## SR-FE-004 — Reliability

The frontend SHALL tolerate:

* API failures
* Service failures
* Network failures
* WebSocket failures
* Backend deployments
* Token expiration

## SR-FE-005 — Security

The frontend SHALL implement secure-by-default practices.

## SR-FE-006 — Performance

The frontend SHALL maintain defined performance budgets.

## SR-FE-007 — Observability

Frontend telemetry SHALL integrate with centralized observability.

## SR-FE-008 — Accessibility

Frontend SHALL target WCAG 2.2 AA.

## SR-FE-009 — Internationalization

Architecture SHALL support multiple languages and locales.

## SR-FE-010 — Maintainability

Domain modules SHALL minimize coupling.

---

## 216. Non-Functional Frontend Requirements

| Category         | Requirement                  |
| ---------------- | ---------------------------- |
| Availability     | High availability deployment |
| Scalability      | Horizontal scaling           |
| Performance      | Strict frontend budgets      |
| Security         | Defense-in-depth             |
| Accessibility    | WCAG 2.2 AA                  |
| Reliability      | Graceful degradation         |
| Observability    | Logs + metrics + traces      |
| Compatibility    | Current major browsers       |
| Localization     | Multi-language ready         |
| Maintainability  | Modular architecture         |
| Testability      | Automated test pyramid       |
| Deployment       | Immutable builds             |
| Recovery         | Rollback support             |
| Privacy          | Data minimization            |
| Authorization    | Backend enforced             |
| Tenant isolation | Backend enforced             |

---

## 217. Critical Backend Connections

The frontend SHALL be explicitly integrated with the following backend capabilities:

```text
Authentication Service
Authorization Service
Identity Service
Organization Service
Workplace Service
Team Service

Admin Service
Security Service
Audit Service

Sales Service
Lead Generation Service
Lead Intelligence Service
Lead Scoring Service
CRM Service

Marketing Service
Campaign Service
Content Service
Advertising Service

SEO Service

Product Intelligence Service
Market Analysis Service
Competitive Intelligence Service

Finance Service
Business Intelligence Service
Analytics Service

Support Service
Conversation Service
Omnichannel Services

AI Gateway
LLM Gateway
Agent Service
Agent Orchestration Service
Agent Evaluation Service

Knowledge Service
RAG Service
Vector Search Service
Document Processing Service

Workflow Service
Workflow Execution Engine

MCP Service

Integration Service
OAuth Service
Webhook Service

Billing Service
Subscription Service
Payment Service
Usage Service

Notification Service

Search Service

Reporting Service
Export Service

Observability Service
Incident Service
```

---

## 218. Recommended Frontend-to-Backend Architecture

```text
                         USERS
                           │
                           ▼
                    SALES GENIE UI
                           │
              ┌────────────┴────────────┐
              │                         │
          WEB APP                 REAL-TIME
              │                  WS / SSE
              ▼                         │
         CDN / WAF                      │
              │                         │
              ▼                         │
        FRONTEND APP                    │
              │                         │
              ▼                         ▼
        API GATEWAY / BFF ◄──────── EVENTS
              │
      ┌───────┼───────────────────────────────┐
      │       │       │       │       │       │
      ▼       ▼       ▼       ▼       ▼       ▼
    AUTH    SALES    CRM   MARKETING   AI   BILLING
      │       │       │       │       │       │
      └───────┴───────┴───────┴───────┴───────┘
                           │
                           ▼
                    DOMAIN SERVICES
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          DATABASE       CACHE       MESSAGE BUS
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                      DATA PLATFORM
```

---

## 219. AI-Native Frontend Architecture

```text
                         USER
                           │
                           ▼
                    AI COMMAND CENTER
                           │
                           ▼
                    AI ORCHESTRATOR
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       SALES AI        MARKETING AI       SUPPORT AI
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    AGENT PLATFORM
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
           TOOLS         MEMORY        RAG
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                      AI GATEWAY
                           │
                ┌──────────┼──────────┐
                ▼          ▼          ▼
              GROK      GEMINI     MISTRAL
```

---

## 220. AI + Human Frontend Architecture

```text
                         REQUEST
                            │
                            ▼
                       AI AGENT
                            │
                            ▼
                      CONFIDENCE
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
            HIGH          MEDIUM         LOW
              │             │             │
              ▼             ▼             ▼
          AI ACTION     REVIEW QUEUE   HUMAN HANDOFF
              │             │             │
              │             ▼             │
              │       HUMAN APPROVAL      │
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                         RESULT
```

---

## 221. Frontend Domain Dependency Rules

Domains SHALL follow these principles:

```text
UI Components
      ↓
Feature Modules
      ↓
Domain Services
      ↓
API Layer
      ↓
Backend
```

Feature components SHALL NOT directly access arbitrary backend services.

---

## 222. Cross-Domain Communication

Cross-domain communication SHOULD occur through:

* Shared typed contracts
* Application events
* Backend APIs
* Shared state abstractions where justified

Circular feature dependencies SHALL be avoided.

---

## 223. Frontend Security Boundary

```text
                 INTERNET
                    │
                    ▼
                  WAF
                    │
                    ▼
                   CDN
                    │
                    ▼
               FRONTEND
                    │
             ┌──────┴──────┐
             ▼             ▼
          API/BFF       REAL-TIME
             │             │
             ▼             ▼
        AUTHZ CHECKS   AUTHENTICATED
             │
             ▼
       INTERNAL SERVICES
```

---

## 224. Critical Rule

The frontend SHALL NEVER be trusted for:

```text
Authorization
Tenant Isolation
Billing
Payment Validation
Financial Calculation
AI Safety Enforcement
Workflow Authorization
Data Ownership
Security Policy
Compliance Enforcement
Audit Integrity
```

These responsibilities SHALL be enforced by backend services.

---

## 225. Production Readiness Checklist

```text
[ ] Authentication connected
[ ] Token lifecycle connected
[ ] MFA connected
[ ] Authorization connected
[ ] RBAC connected
[ ] ABAC connected where required
[ ] Tenant isolation verified
[ ] Organization switching connected
[ ] Workplace switching connected
[ ] Admin modules connected
[ ] Sales APIs connected
[ ] Lead generation connected
[ ] Lead intelligence connected
[ ] CRM connected
[ ] Marketing connected
[ ] SEO connected
[ ] Product launch intelligence connected
[ ] Advertising connected
[ ] Finance connected
[ ] Business intelligence connected
[ ] Support connected
[ ] Omnichannel connected
[ ] AI gateway connected
[ ] Agent platform connected
[ ] LLM routing connected
[ ] RAG connected
[ ] Knowledge management connected
[ ] Workflow engine connected
[ ] MCP connected
[ ] Integrations connected
[ ] Billing connected
[ ] Subscription entitlements connected
[ ] Notifications connected
[ ] Search connected
[ ] Reporting connected
[ ] Export engine connected
[ ] Developer platform connected
[ ] Security monitoring connected
[ ] Audit logs connected
[ ] Observability connected
[ ] Distributed tracing connected
[ ] Error tracking connected
[ ] Accessibility tested
[ ] Security tested
[ ] Performance tested
[ ] E2E tested
[ ] Mobile responsive
[ ] Dark mode tested
[ ] Internationalization tested
[ ] CI/CD configured
[ ] Production build verified
[ ] Rollback verified
```

---

## 226. Final Architecture Principle

SalesGenie frontend SHALL be treated as an **enterprise application platform**, not merely a collection of web pages.

The frontend SHALL provide:

```text
                    SALESGENIE FRONTEND
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
    HUMAN UX            AI UX             ADMIN UX
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                    DOMAIN APPLICATIONS
                           │
 ┌─────────┬────────┬─────────┬────────┬──────────┬─────────┐
 ▼         ▼        ▼         ▼        ▼          ▼         ▼
Sales   Marketing   SEO     Finance  Support     AI      Admin
 │         │        │         │        │          │         │
 └─────────┴────────┴─────────┴────────┴──────────┴─────────┘
                           │
                           ▼
                    API GATEWAY / BFF
                           │
                           ▼
                   MICROSERVICE PLATFORM
                           │
       ┌───────────────────┼────────────────────┐
       ▼                   ▼                    ▼
    DATABASE            MESSAGE BUS          AI PLATFORM
       │                   │                    │
       ▼                   ▼                    ▼
  DATA PLATFORM        EVENT PLATFORM      LLM PROVIDERS
       │                   │                    │
       └───────────────────┼────────────────────┘
                           ▼
                   OBSERVABILITY + SECURITY
```

The resulting frontend SHALL be:

* **Multi-tenant**
* **Role-aware**
* **Permission-aware**
* **AI-native**
* **Human-in-the-loop capable**
* **Backend-connected**
* **Real-time**
* **Observable**
* **Secure**
* **Accessible**
* **Responsive**
* **Scalable**
* **Fault-tolerant**
* **Subscription-aware**
* **Enterprise-ready**
* **API-first**
* **Microservice-compatible**
* **Future mobile-ready**

The frontend is considered complete only when every major UI workflow has a corresponding authoritative backend workflow, API contract, authorization policy, error model, telemetry path, test suite, and production deployment path.
