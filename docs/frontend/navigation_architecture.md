# Navigation Architecture — SalesGenie

**Document:** `navigation_architecture.md`  
**Product:** SalesGenie  
**Document Type:** User Requirements + System Requirements + Functional Requirements  
**Architecture:** Enterprise SaaS + Multi-Tenant + RBAC/ABAC + AI/Human Hybrid + Microservices + Event-Driven  
**Status:** Production Specification  
**Target Scale:** 10M+ users, 500K+ concurrent conversations

---

## 1. Purpose

SalesGenie requires a scalable navigation architecture that provides every user with a role-aware, permission-aware, organization-aware, workspace-aware, and context-aware navigation experience.

The navigation system MUST dynamically expose functionality based on:

- Authentication state
- User identity
- Organization
- Workplace
- Team
- Role
- Permissions
- Subscription plan
- Feature entitlements
- Feature flags
- Product configuration
- Workspace configuration
- Integration availability
- AI capabilities
- Geographic/regulatory restrictions
- Account status
- Resource ownership
- Resource-level permissions
- System health
- User preferences

Navigation MUST NOT be implemented as a static frontend-only menu.

The backend MUST remain the authoritative source for authorization, entitlements, resource visibility, and access decisions.

---

## 2. Navigation Architecture Principles

SalesGenie navigation MUST follow these principles:

1. **Backend-authoritative authorization**
2. **Least-privilege navigation**
3. **RBAC + ABAC enforcement**
4. **Multi-tenant isolation**
5. **Workspace-aware navigation**
6. **Subscription-aware navigation**
7. **Feature-flag-aware navigation**
8. **Context-aware navigation**
9. **AI/human workflow awareness**
10. **Deep-link safety**
11. **URL-level authorization**
12. **API-level authorization**
13. **Consistent navigation state**
14. **Responsive navigation**
15. **Accessibility**
16. **Internationalization**
17. **Auditability**
18. **Observability**
19. **Progressive feature exposure**
20. **Graceful degradation**
21. **Backward-compatible route versioning**
22. **Secure handling of hidden and restricted routes**
23. **Fast navigation under high concurrency**
24. **Consistent experience across web and future mobile clients**

---

## 3. Navigation Hierarchy

SalesGenie SHOULD use the following conceptual hierarchy:

```text
Platform
│
├── Organization
│   │
│   ├── Workplace
│   │   │
│   │   ├── Team
│   │   │   │
│   │   │   └── Users
│   │   │
│   │   └── Projects
│   │
│   ├── Products
│   ├── Campaigns
│   ├── Customers
│   ├── Leads
│   ├── AI Agents
│   └── Integrations
│
└── Platform Administration
    ├── Organizations
    ├── Users
    ├── Security
    ├── Billing
    ├── System
    └── Monitoring
```

---

## 4. Primary Navigation Model

The primary application navigation SHOULD contain:

```text
Dashboard

Sales
├── Overview
├── Leads
├── Lead Discovery
├── Lead Intelligence
├── Lead Scoring
├── Lead Qualification
├── Lead Enrichment
├── Lead Verification
├── Lead Segmentation
├── Lead Routing
├── Lead Assignment
├── Lead Nurturing
├── Contacts
├── Accounts
├── Opportunities
├── Deals
├── Pipeline
├── Funnel
├── Forecasting
├── Sales Analytics
├── Sales Automation
├── Sales Workflows
├── Sales Playbooks
├── Sequences
└── Outreach

Marketing
├── Overview
├── Campaigns
├── Audiences
├── Segmentation
├── Content
├── Social Media
├── Email Marketing
├── Advertising
├── Automation
├── Marketing Workflows
├── Attribution
├── Analytics
├── ROI
└── Budget Optimization

SEO
├── Overview
├── SEO Audit
├── Technical SEO
├── On-Page SEO
├── Off-Page SEO
├── Keywords
├── Keyword Intelligence
├── Keyword Clusters
├── Content Gaps
├── Competitor SEO
├── Backlinks
├── SERP
├── Rank Tracking
├── SEO Content
├── SEO Automation
└── SEO Analytics

Product Intelligence
├── Product Launch
├── Market Analysis
├── Market Trends
├── Competitors
├── Competitor Products
├── Competitor Pricing
├── Competitor Strategy
├── Market Gaps
├── Opportunities
├── Risks
├── Positioning
├── GTM Strategy
├── Launch Strategy
├── Forecasting
└── AI Recommendations

AI
├── AI Overview
├── AI Agents
├── Agent Builder
├── Agent Marketplace
├── Agent Templates
├── Agent Runs
├── Agent Memory
├── Agent Tools
├── Agent Evaluations
├── Agent Versions
├── AI Models
├── Model Routing
├── Prompt Management
├── Prompt Evaluation
├── AI Usage
└── AI Cost

Support
├── Overview
├── Inbox
├── Conversations
├── Tickets
├── Customers
├── Knowledge Base
├── AI Support
├── Human Support
├── Escalations
├── SLA
├── Automation
├── Analytics
└── Customer Satisfaction

Workflows
├── Overview
├── Workflow Builder
├── Workflows
├── Templates
├── Executions
├── Schedules
├── Marketplace
├── Monitoring
└── Errors

Knowledge
├── Knowledge Base
├── Documents
├── Collections
├── Search
├── Semantic Search
├── Knowledge Graph
├── RAG
├── Embeddings
└── Evaluations

Analytics
├── Overview
├── Sales
├── Marketing
├── SEO
├── Advertising
├── Finance
├── Support
├── Customers
├── Products
├── Revenue
├── Profitability
├── Growth
├── Forecasts
└── AI Insights

Reports
├── Overview
├── Report Builder
├── Sales Reports
├── Marketing Reports
├── SEO Reports
├── Advertising Reports
├── Financial Reports
├── Product Reports
├── Executive Reports
├── Scheduled Reports
└── Exports

Finance
├── Overview
├── Revenue
├── Expenses
├── Profit & Loss
├── Cash Flow
├── Products
├── Profitability
├── Forecasting
├── Budgets
└── Financial AI

Integrations
├── Overview
├── Connected Apps
├── Google
├── Gmail
├── Google Drive
├── LinkedIn
├── Facebook
├── Instagram
├── WhatsApp
├── YouTube
├── TikTok
├── Slack
├── HubSpot
├── Salesforce
├── Zendesk
├── Jira
├── Notion
└── Microsoft Teams

Notifications
├── All
├── Mentions
├── Tasks
├── Alerts
├── AI
├── Security
├── Billing
└── System

Settings
├── Account
├── Organization
├── Workplace
├── Team
├── Members
├── Roles
├── Permissions
├── Security
├── Authentication
├── MFA
├── Sessions
├── Billing
├── Subscription
├── Usage
├── Integrations
├── API
├── Webhooks
├── Notifications
├── Appearance
├── Language
└── Audit Logs
```

---

## 5. Global Navigation

## UR-GN-001 — Global Application Navigation

Users MUST be able to navigate to authorized application modules from a persistent global navigation interface.

The interface SHOULD provide:

* Product logo
* Organization selector
* Workplace selector
* Global search
* Primary navigation
* Quick-create actions
* Notifications
* Tasks
* AI assistant
* Help
* User profile
* Settings
* Logout

---

## UR-GN-002 — Organization Selector

Authorized users MUST be able to switch between organizations where they have membership.

The system MUST:

* Retrieve memberships from backend
* Validate organization access
* Switch active organization context
* Refresh permissions
* Refresh feature entitlements
* Refresh navigation configuration
* Refresh workspace context
* Invalidate unauthorized cached resources

---

## UR-GN-003 — Workplace Selector

If a user belongs to multiple workplaces, the UI MUST allow workplace switching.

Changing workplace MUST trigger:

```text
Workplace Change
      ↓
Backend Validation
      ↓
Membership Validation
      ↓
Permission Resolution
      ↓
Entitlement Resolution
      ↓
Navigation Reconfiguration
      ↓
Context Refresh
```

---

## 6. User Requirements

## UR-001 — Personalized Navigation

Users MUST receive navigation appropriate to their:

* Role
* Permissions
* Organization
* Workplace
* Team
* Subscription
* Feature access
* Account status

---

## UR-002 — Role-Based Navigation

Users MUST see different navigation structures according to their role.

Supported roles include:

* Super Admin
* Platform Admin
* Security Admin
* Billing Admin
* Organization Owner
* Organization Admin
* Workplace Admin
* Team Manager
* Sales Manager
* Sales Agent
* Marketing Manager
* Marketing Specialist
* SEO Manager
* SEO Specialist
* Product Manager
* Finance Manager
* Business Analyst
* Support Manager
* Support Agent
* AI Agent Builder
* Developer
* End User
* External Client

---

## UR-003 — Permission-Based Navigation

Navigation items MUST be filtered based on effective permissions.

Example:

```text
permission:
sales.leads.read

→ Leads visible
```

```text
permission:
sales.leads.write

→ Create/Edit Leads available
```

```text
permission:
sales.leads.delete

→ Delete actions available
```

---

## UR-004 — Subscription-Aware Navigation

Navigation MUST respect plan entitlements.

Example:

```text
Free
├── Basic Sales
├── Limited AI
└── Limited Reports

Professional
├── Advanced Sales
├── Marketing
├── AI Agents
└── Advanced Analytics

Enterprise
├── Full Platform
├── Advanced AI
├── Enterprise Security
├── Advanced Analytics
└── Enterprise Administration
```

---

## UR-005 — Feature Flag Navigation

Feature flags MUST determine whether experimental or staged functionality is exposed.

Feature flags MUST be resolved server-side or through a trusted configuration service.

---

## UR-006 — Contextual Navigation

Navigation MUST adapt according to the current resource.

Example:

```text
Organization
   ↓
Workplace
   ↓
Campaign
   ↓
Campaign Details
   ↓
Audience
   ↓
Analytics
```

---

## UR-007 — Breadcrumb Navigation

Users MUST receive breadcrumbs for deeply nested resources.

Example:

```text
Sales
/
Leads
/
Lead Intelligence
/
Company
/
Contact
```

---

## UR-008 — Global Search

Authorized users MUST be able to search across accessible:

* Leads
* Contacts
* Accounts
* Opportunities
* Deals
* Customers
* Campaigns
* Workflows
* Documents
* AI Agents
* Conversations
* Tickets
* Reports
* Products
* Organizations
* Users

Search results MUST respect authorization.

---

## UR-009 — Quick Actions

Users SHOULD have access to context-aware quick actions.

Examples:

```text
Create Lead
Create Contact
Create Campaign
Create Workflow
Create AI Agent
Upload Document
Create Report
Start Conversation
Create Ticket
```

---

## UR-010 — Recent Items

The UI SHOULD provide recently accessed resources.

Recent items MUST be scoped by:

* User
* Organization
* Workplace

---

## UR-011 — Favorites

Users SHOULD be able to favorite:

* Pages
* Dashboards
* Reports
* Leads
* Accounts
* Workflows
* AI Agents
* Knowledge Bases

Favorites MUST persist through backend storage.

---

## UR-012 — Navigation Preferences

Users SHOULD be able to configure:

* Collapsed sidebar
* Expanded sidebar
* Pinned modules
* Favorites
* Recent items
* Default landing page

Preferences MUST synchronize across authenticated devices where applicable.

---

## 7. System Requirements

## SR-001 — Navigation Configuration Service

SalesGenie MUST provide a navigation configuration layer capable of generating navigation based on:

```text
User
Organization
Workplace
Team
Role
Permissions
Plan
Entitlements
Feature Flags
Resource Context
```

---

## SR-002 — Backend Authorization

The frontend MUST NOT be considered an authorization boundary.

Every protected route and backend operation MUST validate authorization server-side.

---

## SR-003 — Navigation Resolution

The backend SHOULD expose an endpoint similar to:

```http
GET /api/v1/navigation
```

Response:

```json
{
  "organization_id": "org_123",
  "workplace_id": "workspace_123",
  "role": "sales_manager",
  "permissions": [
    "sales.leads.read",
    "sales.leads.write",
    "sales.pipeline.read"
  ],
  "entitlements": [
    "lead_intelligence",
    "sales_automation"
  ],
  "navigation": []
}
```

---

## SR-004 — Route Authorization

Every route MUST have:

```text
route
required_permission
required_role
required_entitlement
required_feature_flag
resource_scope
```

---

## SR-005 — Deep-Link Security

A user MUST NOT gain access to a restricted resource merely by entering its URL directly.

Example:

```text
/user/security/admin
```

MUST return an authorization failure if the user lacks permission.

---

## SR-006 — Multi-Tenant Isolation

Navigation MUST never expose resources belonging to another tenant.

Tenant context MUST be derived from trusted authentication/session context rather than arbitrary frontend parameters.

---

## SR-007 — Workspace Isolation

Workspace-level permissions MUST be enforced independently from organization-level permissions.

---

## SR-008 — Permission Cache

Navigation permission resolution SHOULD be cached using a short-lived, invalidatable cache.

Cache keys SHOULD include:

```text
user_id
organization_id
workplace_id
role_version
permission_version
entitlement_version
feature_flag_version
```

---

## SR-009 — Cache Invalidation

Changes to:

* Role
* Permission
* Organization membership
* Workplace membership
* Subscription
* Feature entitlement
* Feature flag
* Account status

MUST invalidate relevant navigation caches.

---

## SR-010 — Navigation Versioning

Navigation configurations MUST be versioned.

Example:

```text
navigation_version:
2026.08.1
```

---

## 8. Functional Requirements

## 8.1 Authentication Navigation

## FR-AUTH-001

Unauthenticated users MUST see:

```text
Landing
Pricing
Documentation
Login
Signup
Forgot Password
```

---

## FR-AUTH-002

Authenticated users MUST be redirected to their authorized default landing page.

---

## FR-AUTH-003

Users with suspended accounts MUST NOT access protected application navigation.

---

## FR-AUTH-004

Users with expired sessions MUST be redirected to authentication.

---

## 8.2 Dashboard Navigation

## FR-DASH-001

Every authenticated user MUST have access to an appropriate dashboard when authorized.

---

## FR-DASH-002

Dashboard contents MUST be role-aware.

---

## FR-DASH-003

Dashboard widgets MUST respect:

* RBAC
* ABAC
* Organization
* Workplace
* Subscription
* Feature flags

---

## 8.3 Sales Navigation

## FR-SALES-001

Authorized users MUST access:

* Leads
* Contacts
* Accounts
* Opportunities
* Deals
* Pipeline
* Forecasting
* Analytics

---

## FR-SALES-002

Lead navigation MUST support:

```text
Discovery
→ Intelligence
→ Enrichment
→ Verification
→ Scoring
→ Qualification
→ Segmentation
→ Routing
→ Assignment
→ Nurturing
```

---

## FR-SALES-003

Sales managers MUST be able to access manager-level analytics and team navigation.

---

## FR-SALES-004

Sales agents MUST only see resources permitted by their scope.

---

## 8.4 Lead Intelligence Navigation

## FR-LEAD-001

Authorized users MUST access:

* Lead Discovery
* Company Intelligence
* Person Intelligence
* Intent
* Buying Signals
* Competitive Intelligence
* Recommendations

---

## FR-LEAD-002

Lead navigation MUST preserve context between:

```text
Company
→ Contacts
→ Intelligence
→ Intent
→ Score
→ Qualification
→ Outreach
```

---

## 8.5 Marketing Navigation

## FR-MKT-001

Authorized users MUST access marketing modules according to permissions.

---

## FR-MKT-002

Marketing navigation MUST support:

```text
Strategy
→ Audience
→ Campaign
→ Content
→ Execution
→ Attribution
→ Analytics
→ Optimization
```

---

## 8.6 AI Navigation

## FR-AI-001

Authorized users MUST have an AI workspace.

---

## FR-AI-002

AI navigation MUST support:

```text
AI Overview
Agents
Agent Builder
Agent Runs
Agent Memory
Agent Tools
Agent Evaluations
Models
Prompts
Usage
Cost
```

---

## FR-AI-003

AI Agent Builder users MUST receive builder-specific navigation.

---

## FR-AI-004

AI agents MUST NOT expose tools or configuration pages that the current user cannot access.

---

## 8.7 Agent Navigation

## FR-AGENT-001

Agent detail navigation SHOULD include:

```text
Overview
Instructions
Tools
Memory
Knowledge
Permissions
Triggers
Workflows
Testing
Evaluations
Versions
Observability
Deployments
Audit
```

---

## FR-AGENT-002

Agent navigation MUST support agent lifecycle states:

```text
Draft
Testing
Review
Approved
Published
Paused
Deprecated
Archived
```

---

## 8.8 Support Navigation

## FR-SUPPORT-001

Support users MUST access:

```text
Inbox
Conversations
Tickets
Customers
Knowledge Base
Escalations
SLA
Analytics
```

---

## FR-SUPPORT-002

AI support users MUST have AI-specific navigation.

---

## FR-SUPPORT-003

Human support users MUST have access to human-agent queues.

---

## 8.9 Omnichannel Navigation

## FR-OMNI-001

Authorized users MUST access supported communication channels.

Channels include:

* Web Chat
* Email
* WhatsApp
* Facebook Messenger
* Instagram
* Telegram
* SMS
* Voice

---

## FR-OMNI-002

Channel visibility MUST depend on:

```text
Integration status
+
Permission
+
Subscription entitlement
+
Organization configuration
```

---

## 8.10 Workflow Navigation

## FR-WORKFLOW-001

Authorized users MUST access:

```text
Workflow Builder
Workflows
Templates
Executions
Schedules
Marketplace
Monitoring
Errors
```

---

## FR-WORKFLOW-002

Workflow execution pages MUST display execution-specific context.

---

## FR-WORKFLOW-003

Users MUST NOT access workflows outside their authorization scope.

---

## 8.11 Knowledge Navigation

## FR-KB-001

Knowledge navigation MUST support:

```text
Knowledge Bases
Documents
Collections
Search
Semantic Search
RAG
Knowledge Graph
Evaluations
```

---

## FR-KB-002

Documents MUST be displayed only when the current user has access.

---

## 8.12 Analytics Navigation

## FR-AN-001

Analytics navigation MUST provide role-appropriate analytics.

---

## FR-AN-002

Analytics MUST support:

* Sales
* Marketing
* Advertising
* SEO
* Support
* Finance
* Revenue
* Profitability
* Growth
* Product
* Customers

---

## FR-AN-003

Analytics navigation MUST respect data-level permissions.

---

## 8.13 Finance Navigation

## FR-FIN-001

Finance users MUST access:

```text
Revenue
Expenses
Profit & Loss
Cash Flow
Profitability
Forecasting
Budgets
```

---

## FR-FIN-002

Financial data MUST never be exposed through unauthorized navigation.

---

## 8.14 Reporting Navigation

## FR-REPORT-001

Users MUST access authorized reports.

---

## FR-REPORT-002

Report navigation MUST support:

```text
Report Builder
Saved Reports
Scheduled Reports
Exports
Templates
```

---

## FR-REPORT-003

Export functionality MUST respect resource permissions.

---

## 8.15 Integration Navigation

## FR-INT-001

Users MUST be able to view authorized integrations.

---

## FR-INT-002

Integration navigation MUST expose:

```text
Connection Status
Configuration
Authentication
Sync
Webhooks
Logs
Errors
Usage
```

only when authorized.

---

## 8.16 Settings Navigation

## FR-SET-001

Settings MUST be divided into:

```text
Personal Settings
Organization Settings
Workplace Settings
Team Settings
Security Settings
Billing Settings
Integration Settings
Developer Settings
AI Settings
Notification Settings
```

---

## FR-SET-002

Users MUST only see settings they are authorized to manage.

---

## 8.17 Administrative Navigation

## FR-ADMIN-001

Super Admin navigation MUST include:

```text
Platform Dashboard
Users
Organizations
Workplaces
Roles
Permissions
Subscriptions
Billing
Feature Flags
System Configuration
Services
Infrastructure
Security
Audit Logs
Incidents
Monitoring
```

---

## FR-ADMIN-002

Platform Admin navigation MUST exclude security and billing administration unless explicitly authorized.

---

## FR-ADMIN-003

Security Admin navigation MUST include:

```text
Security Dashboard
Threat Detection
Sessions
Authentication
MFA
Security Events
Audit Logs
Incidents
Vulnerabilities
Security Policies
```

---

## FR-ADMIN-004

Billing Admin navigation MUST include:

```text
Billing Dashboard
Subscriptions
Plans
Invoices
Payments
Refunds
Coupons
Credits
Usage
Billing Analytics
```

---

## 9. Role-Based Navigation Matrix

| Role                 | Dashboard | Sales        | Marketing    | SEO          | AI           | Support      | Finance      | Admin     | Security      | Billing      |
| -------------------- | --------- | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | --------- | ------------- | ------------ |
| Super Admin          | Full      | Full         | Full         | Full         | Full         | Full         | Full         | Full      | Full          | Full         |
| Platform Admin       | Full      | Configurable | Configurable | Configurable | Configurable | Configurable | Limited      | Full      | Limited       | Limited      |
| Security Admin       | Security  | Limited      | Limited      | Limited      | Security     | Limited      | Limited      | Security  | Full          | Limited      |
| Billing Admin        | Billing   | Limited      | Limited      | Limited      | Usage        | Limited      | Full         | Billing   | Limited       | Full         |
| Organization Owner   | Full      | Full         | Full         | Full         | Full         | Full         | Full         | Org       | Org           | Full         |
| Organization Admin   | Full      | Configurable | Configurable | Configurable | Configurable | Configurable | Configurable | Org       | Limited       | Limited      |
| Workplace Admin      | Full      | Configurable | Configurable | Configurable | Configurable | Configurable | Limited      | Workplace | Limited       | Limited      |
| Team Manager         | Full      | Team         | Team         | Team         | Team         | Team         | Limited      | Team      | No            | No           |
| Sales Manager        | Sales     | Full         | Limited      | Limited      | Sales AI     | Limited      | Limited      | No        | No            | No           |
| Sales Agent          | Sales     | Scoped       | No           | No           | Scoped       | Limited      | No           | No        | No            | No           |
| Marketing Manager    | Marketing | Limited      | Full         | Limited      | Marketing AI | Limited      | Limited      | No        | No            | No           |
| Marketing Specialist | Marketing | Limited      | Scoped       | Limited      | Scoped       | No           | No           | No        | No            | No           |
| SEO Manager          | SEO       | Limited      | Limited      | Full         | SEO AI       | No           | No           | No        | No            | No           |
| SEO Specialist       | SEO       | Limited      | Limited      | Scoped       | Scoped       | No           | No           | No        | No            | No           |
| Product Manager      | Product   | Limited      | Full         | Full         | Full         | Limited      | Analytics    | No        | No            | No           |
| Finance Manager      | Finance   | Analytics    | Analytics    | Analytics    | Finance AI   | Analytics    | Full         | No        | No            | Limited      |
| Business Analyst     | Analytics | Analytics    | Analytics    | Analytics    | Analytics    | Analytics    | Analytics    | No        | No            | No           |
| Support Manager      | Support   | Limited      | Limited      | No           | Support AI   | Full         | Limited      | No        | No            | No           |
| Support Agent        | Support   | Limited      | No           | No           | AI Support   | Scoped       | No           | No        | No            | No           |
| AI Agent Builder     | AI        | AI           | AI           | AI           | Full         | AI           | No           | No        | Limited       | No           |
| Developer            | Developer | API          | API          | API          | AI APIs      | API          | API          | Developer | Security APIs | Billing APIs |
| End User             | Client    | Limited      | Limited      | No           | Authorized   | Support      | No           | No        | No            | No           |
| External Client      | Client    | Scoped       | Scoped       | Scoped       | Scoped       | Support      | Billing      | Client    | Limited       | Billing      |

---

## 10. Navigation Permission Model

Navigation permissions SHOULD follow a hierarchical model.

```text
module.resource.action
```

Examples:

```text
sales.leads.read
sales.leads.create
sales.leads.update
sales.leads.delete

sales.pipeline.read
sales.forecasting.read

marketing.campaigns.read
marketing.campaigns.create

ai.agents.read
ai.agents.create
ai.agents.deploy

support.tickets.read
support.tickets.assign

finance.revenue.read
finance.expenses.read

admin.users.read
admin.users.manage

security.audit.read

billing.subscriptions.read
billing.subscriptions.manage
```

---

## 11. ABAC Requirements

Navigation MUST support attribute-based access control.

Example attributes:

```text
user.department
user.team_id
user.region
user.role
user.clearance_level

resource.organization_id
resource.workplace_id
resource.owner_id
resource.team_id
resource.classification

request.ip
request.device
request.location
request.time

subscription.plan
subscription.status

feature.enabled
```

Example policy:

```text
ALLOW
IF

user.organization_id == resource.organization_id

AND

user.team_id == resource.team_id

AND

user.permission == "sales.leads.read"
```

---

## 12. Resource-Level Navigation

Navigation MUST support resource-aware menus.

Example:

```text
Lead #123
├── Overview
├── Intelligence
├── Activity
├── Contacts
├── Score
├── Qualification
├── Outreach
├── Tasks
├── Notes
├── Documents
├── AI Insights
└── Audit
```

Each item MUST independently respect authorization.

---

## 13. Navigation State

The frontend MUST maintain:

```text
activeRoute
activeOrganization
activeWorkplace
activeTeam
activeResource
expandedSections
collapsedSections
breadcrumbs
navigationVersion
permissionVersion
entitlementVersion
```

---

## 14. Backend Integration Requirements

Navigation MUST integrate with:

```text
Authentication Service
Authorization Service
RBAC Service
ABAC Policy Engine
Organization Service
Workplace Service
User Service
Subscription Service
Billing Service
Feature Flag Service
Integration Service
AI Gateway
Agent Service
Workflow Service
Knowledge Service
Analytics Service
Notification Service
Audit Service
Search Service
```

---

## 15. Navigation API Requirements

The platform SHOULD provide:

```http
GET /api/v1/navigation
GET /api/v1/navigation/modules
GET /api/v1/navigation/routes
GET /api/v1/navigation/permissions
GET /api/v1/navigation/context
```

---

## 16. Navigation Response Model

Example:

```json
{
  "version": "2026.08.1",
  "context": {
    "organization_id": "org_123",
    "workplace_id": "workspace_123",
    "team_id": "team_123"
  },
  "user": {
    "id": "user_123",
    "roles": ["sales_manager"]
  },
  "navigation": [
    {
      "id": "sales",
      "label": "Sales",
      "icon": "sales",
      "route": "/sales",
      "required_permissions": [
        "sales.read"
      ],
      "children": [
        {
          "id": "leads",
          "label": "Leads",
          "route": "/sales/leads",
          "required_permissions": [
            "sales.leads.read"
          ]
        }
      ]
    }
  ]
}
```

---

## 17. Navigation Events

The system SHOULD publish events such as:

```text
navigation.loaded
navigation.updated
navigation.permission_changed
navigation.entitlement_changed
navigation.organization_changed
navigation.workspace_changed
navigation.route_access_denied
navigation.preference_changed
navigation.favorite_added
navigation.favorite_removed
navigation.search_executed
```

---

## 18. Audit Requirements

The system MUST audit security-sensitive navigation events.

Audit events SHOULD include:

```text
user_id
organization_id
workplace_id
route
resource_id
action
authorization_result
permission
timestamp
ip
device
request_id
trace_id
```

Examples:

```text
ADMIN_ROUTE_ACCESSED
SECURITY_ROUTE_ACCESSED
BILLING_ROUTE_ACCESSED
ROUTE_ACCESS_DENIED
PRIVILEGED_NAVIGATION_CHANGED
```

---

## 19. Observability Requirements

Navigation MUST be observable.

Metrics SHOULD include:

```text
navigation_load_latency
navigation_api_latency
navigation_error_rate
route_access_denied_rate
route_not_found_rate
navigation_search_latency
navigation_cache_hit_rate
navigation_cache_miss_rate
navigation_permission_resolution_latency
```

---

## 20. Performance Requirements

Navigation MUST:

* Load quickly
* Avoid unnecessary backend calls
* Cache safe configuration
* Lazy-load large modules
* Avoid loading unauthorized modules
* Prefetch likely destinations
* Support code splitting
* Support route-level chunking

Target:

```text
Initial navigation configuration:
P50 < 100 ms
P95 < 300 ms
P99 < 750 ms
```

These targets exclude cold-start infrastructure latency outside the navigation service's control.

---

## 21. Responsive Navigation

The navigation system MUST support:

```text
Desktop
Laptop
Tablet
Mobile Web
```

Desktop:

```text
Sidebar
Top Navigation
Command Palette
```

Mobile:

```text
Bottom Navigation
Drawer
Contextual Menus
```

---

## 22. Accessibility Requirements

Navigation MUST comply with WCAG 2.2 AA-level expectations.

The system MUST support:

* Keyboard navigation
* Screen readers
* Focus management
* Visible focus indicators
* ARIA landmarks
* Accessible labels
* Accessible expandable menus
* Skip navigation
* Logical tab order
* Reduced motion
* Sufficient contrast
* Error announcements

---

## 23. Internationalization

Navigation MUST support localization.

The system MUST NOT hard-code user-facing navigation labels.

Example:

```text
navigation.sales
navigation.leads
navigation.analytics
navigation.settings
```

Translations MUST be resolved according to user locale.

---

## 24. Search Architecture

Global navigation search SHOULD use:

```text
Query
 ↓
Authentication
 ↓
Tenant Resolution
 ↓
Permission Filtering
 ↓
Search
 ↓
Ranking
 ↓
Resource Authorization
 ↓
Results
```

Search MUST never return unauthorized resources.

---

## 25. Command Palette

SalesGenie SHOULD provide an enterprise command palette.

Example:

```text
⌘ / Ctrl + K
```

Users SHOULD be able to execute:

```text
Go to Leads
Create Lead
Create Campaign
Create Workflow
Open AI Agents
Search Customer
Open Report
Upload Document
Open Settings
Switch Workspace
Switch Organization
```

Actions MUST be permission-aware.

---

## 26. Notification Navigation

Notifications MUST link to authorized resources.

Example:

```text
AI Agent failed
↓
Agent Execution
↓
Execution Details
```

The target MUST be re-authorized before displaying the resource.

---

## 27. Error Navigation

The system MUST support:

```text
401 → Login
403 → Access Denied
404 → Not Found
409 → Conflict
429 → Rate Limited
500 → Error
503 → Service Unavailable
```

The UI MUST NOT expose sensitive authorization details.

---

## 28. Graceful Degradation

If navigation configuration services become temporarily unavailable:

The system MAY use a safe, short-lived cached navigation configuration.

However:

```text
Cached Navigation ≠ Authorization
```

Backend authorization MUST still be enforced.

---

## 29. Offline / Degraded Navigation

The application MAY provide limited navigation during network degradation.

Allowed:

```text
Previously loaded static pages
Cached UI shell
Local preferences
```

Disallowed:

```text
Privileged backend operations
Sensitive data retrieval
Authorization bypass
Administrative operations
```

---

## 30. Feature Flags

Navigation MUST support flags such as:

```text
ai_agents_enabled
lead_intelligence_enabled
marketing_ai_enabled
seo_ai_enabled
product_launch_enabled
advanced_analytics_enabled
enterprise_reports_enabled
voice_enabled
whatsapp_enabled
mcp_enabled
workflow_marketplace_enabled
```

---

## 31. Subscription Entitlements

Example:

```text
FREE
├── dashboard
├── basic_sales
├── limited_reports
└── limited_ai

PRO
├── advanced_sales
├── marketing
├── seo
├── ai_agents
├── workflows
└── advanced_analytics

ENTERPRISE
├── everything
├── advanced_security
├── audit
├── enterprise_integrations
├── advanced_ai
├── custom_roles
├── advanced_reporting
└── dedicated_features
```

---

## 32. Client Portal Navigation

External clients MUST receive a separate navigation experience.

```text
Client Portal
├── Dashboard
├── Projects
├── Reports
├── Analytics
├── Campaigns
├── Leads
├── AI Agents
├── Conversations
├── Support
├── Integrations
├── Billing
└── Settings
```

Clients MUST NOT see internal administrative navigation.

---

## 33. AI + Human Hybrid Navigation

AI/human workflows MUST provide navigation for:

```text
AI Tasks
Human Review
Approval Queue
Escalations
AI Decisions
Human Decisions
Handoff Queue
Failed AI Actions
Confidence Reviews
```

Example:

```text
AI Agent
   ↓
Low Confidence
   ↓
Human Review Queue
   ↓
Human Decision
   ↓
AI Learning / Feedback
```

---

## 34. Human Review Navigation

Authorized reviewers MUST have:

```text
Review Queue
Pending Reviews
Assigned Reviews
Completed Reviews
Escalations
AI Decisions
Confidence
Feedback
```

---

## 35. Developer Navigation

Developer users SHOULD have:

```text
Developer Portal
API Keys
Service Accounts
API Documentation
Webhooks
SDKs
Sandbox
API Usage
Logs
API Versions
MCP
Developer Settings
```

---

## 36. MCP Navigation

Authorized users MUST be able to access:

```text
MCP Overview
MCP Servers
MCP Tools
MCP Registry
MCP Marketplace
MCP Credentials
MCP Permissions
MCP Security
MCP Usage
MCP Logs
```

---

## 37. Security Navigation

Security administrators MUST receive:

```text
Security Overview
Authentication
MFA
Sessions
Access Control
Audit Logs
Threat Detection
Anomaly Detection
Fraud Detection
Vulnerabilities
Security Incidents
Security Policies
AI Security
LLM Security
Prompt Injection
DLP
```

---

## 38. Billing Navigation

Billing administrators and authorized owners MUST receive:

```text
Billing Overview
Plans
Subscription
Usage
Invoices
Payments
Refunds
Coupons
Credits
Taxes
Billing Analytics
```

---

## 39. Navigation Lifecycle

Navigation configuration SHOULD follow:

```text
Draft
 ↓
Validated
 ↓
Published
 ↓
Active
 ↓
Deprecated
 ↓
Removed
```

---

## 40. Navigation Configuration Validation

Before publication, the system MUST validate:

* Duplicate routes
* Duplicate navigation IDs
* Missing permissions
* Invalid routes
* Circular menus
* Invalid parent-child relationships
* Missing translations
* Missing icons
* Unauthorized modules
* Invalid feature flags
* Invalid entitlement references

---

## 41. Security Requirements

The navigation system MUST prevent:

* Privilege escalation
* Tenant escape
* Workspace escape
* Route manipulation
* Permission spoofing
* Client-side authorization bypass
* IDOR
* Unauthorized deep links
* Navigation injection
* Malicious redirect
* Sensitive route enumeration

---

## 42. URL Security

Routes MUST be normalized.

The system MUST protect against:

```text
Path traversal
Open redirects
Encoded path bypass
Case manipulation
Parameter pollution
Unauthorized resource IDs
```

---

## 43. Navigation Analytics

The system SHOULD track:

```text
navigation_module_opened
navigation_item_clicked
navigation_search
command_executed
route_access_denied
favorite_created
recent_item_opened
workspace_switched
organization_switched
```

Analytics MUST respect privacy and tenant isolation.

---

## 44. User Experience Requirements

Navigation MUST provide:

* Consistent terminology
* Predictable hierarchy
* Maximum reasonable depth
* Clear active-state indicators
* Search for large menus
* Keyboard shortcuts
* Breadcrumbs
* Contextual actions
* Loading states
* Empty states
* Error states
* Permission-aware explanations

---

## 45. Navigation Depth

The system SHOULD avoid excessive nesting.

Recommended:

```text
Level 1 → Product
Level 2 → Module
Level 3 → Resource
Level 4 → Resource Detail
Level 5 → Detail Tab
```

Example:

```text
Sales
 → Leads
   → Lead
     → Intelligence
```

---

## 46. Backend-Connected Features

The following navigation features MUST be backend-connected:

| Feature                         | Backend Required |
| ------------------------------- | ---------------: |
| Authentication-aware navigation |              Yes |
| Role-aware navigation           |              Yes |
| Permission-aware navigation     |              Yes |
| ABAC navigation                 |              Yes |
| Organization switching          |              Yes |
| Workplace switching             |              Yes |
| Subscription-aware navigation   |              Yes |
| Feature flags                   |              Yes |
| Entitlements                    |              Yes |
| Favorites                       |              Yes |
| Recent items                    |              Yes |
| Global search                   |              Yes |
| Notifications                   |              Yes |
| AI agent navigation             |              Yes |
| Workflow navigation             |              Yes |
| Knowledge navigation            |              Yes |
| Integration status              |              Yes |
| Billing navigation              |              Yes |
| Usage navigation                |              Yes |
| Admin navigation                |              Yes |
| Security navigation             |              Yes |
| Audit navigation                |              Yes |
| Navigation analytics            |              Yes |
| User preferences                |              Yes |
| Command palette actions         |              Yes |
| Resource-level menus            |              Yes |
| Breadcrumb resource validation  |              Yes |
| Client portal navigation        |              Yes |

---

## 47. Frontend-Only Features

The following MAY remain primarily frontend-controlled:

```text
Sidebar animation
Menu expansion
Collapse state
Visual hover state
Keyboard shortcuts
Loading skeletons
Static icons
Static layout
Responsive layout
```

However, these MUST NOT control authorization.

---

## 48. Navigation Architecture

Recommended architecture:

```text
                    USER
                     │
                     ▼
             FRONTEND APPLICATION
                     │
             ┌───────┴────────┐
             │                │
             ▼                ▼
      ROUTER / SHELL      COMMAND PALETTE
             │                │
             └───────┬────────┘
                     ▼
             NAVIGATION CLIENT
                     │
                     ▼
             NAVIGATION API
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
 AUTH SERVICE   RBAC/ABAC      ENTITLEMENTS
       │             │             │
       └─────────────┼─────────────┘
                     ▼
              FEATURE FLAGS
                     │
                     ▼
            NAVIGATION RESOLVER
                     │
          ┌──────────┼───────────┐
          ▼          ▼           ▼
      ORGANIZATION WORKPLACE    TEAM
          │          │           │
          └──────────┼───────────┘
                     ▼
             NAVIGATION CONFIG
                     │
                     ▼
             FRONTEND NAVIGATION
                     │
                     ▼
                ROUTE GUARD
                     │
                     ▼
              BACKEND API
                     │
                     ▼
            RESOURCE AUTHORIZATION
```

---

## 49. Navigation Resolver

The navigation resolver SHOULD execute:

```text
resolveUser()
        ↓
resolveOrganization()
        ↓
resolveWorkplace()
        ↓
resolveRoles()
        ↓
resolvePermissions()
        ↓
resolveABACContext()
        ↓
resolveSubscription()
        ↓
resolveEntitlements()
        ↓
resolveFeatureFlags()
        ↓
resolveNavigation()
        ↓
returnNavigation()
```

---

## 50. Route Guard Architecture

Every protected route SHOULD follow:

```text
Route Request
     ↓
Authentication Guard
     ↓
Organization Guard
     ↓
Workplace Guard
     ↓
Role Guard
     ↓
Permission Guard
     ↓
Entitlement Guard
     ↓
Feature Flag Guard
     ↓
Resource Authorization
     ↓
Render Page
```

---

## 51. Failure Handling

If authorization fails:

```text
403
 ↓
Access Denied
 ↓
Safe Navigation
```

If authentication fails:

```text
401
 ↓
Login
 ↓
Return URL
```

If subscription entitlement fails:

```text
Entitlement Required
 ↓
Plan Information
 ↓
Upgrade Flow
```

---

## 52. Navigation and Billing Integration

When a user accesses a premium module:

```text
Navigation Request
       ↓
Permission Check
       ↓
Entitlement Check
       ↓
Plan Check
       ↓
Feature Availability
       ↓
Allow / Upgrade
```

---

## 53. Navigation and AI Integration

AI navigation MUST consider:

```text
AI entitlement
Model availability
Provider availability
Agent permissions
Tool permissions
Knowledge permissions
AI safety policy
Organization AI policy
Usage quota
```

---

## 54. Navigation and Usage Limits

If a user reaches a quota:

```text
AI Usage Limit
      ↓
AI Module
      ↓
Usage Status
      ↓
Upgrade / Wait / Admin Request
```

The UI MUST NOT assume that hidden navigation alone enforces quotas.

---

## 55. Navigation and Notifications

Notification links MUST contain safe resource references.

Example:

```json
{
  "notification_id": "n_123",
  "target": {
    "type": "lead",
    "id": "lead_123",
    "route": "/sales/leads/lead_123"
  }
}
```

The backend MUST revalidate access when the route is opened.

---

## 56. Navigation and Audit Logs

Sensitive routes SHOULD be audited.

Examples:

```text
/security
/admin
/billing
/organizations
/users
/audit
/api
/developer
```

---

## 57. Navigation Testing Requirements

The navigation system MUST be tested for:

## Functional Testing

* Route resolution
* Menu rendering
* Role filtering
* Permission filtering
* Entitlement filtering
* Feature flag filtering
* Organization switching
* Workplace switching
* Deep links
* Breadcrumbs
* Search
* Favorites
* Recent items

## Security Testing

* RBAC bypass
* ABAC bypass
* IDOR
* Tenant escape
* Workspace escape
* Route manipulation
* Privilege escalation
* Unauthorized deep links
* JWT manipulation
* Session manipulation

## Accessibility Testing

* Keyboard navigation
* Screen readers
* Focus management
* ARIA
* Contrast
* Reduced motion

## Performance Testing

* Navigation load
* Large permission sets
* Large organizations
* 10M+ user platform scale
* High concurrent navigation requests
* Cache behavior
* API latency

---

## 58. Acceptance Criteria

The navigation architecture is considered production-ready when:

* Every protected route has backend authorization.
* Navigation is dynamically resolved.
* RBAC is enforced.
* ABAC is supported.
* Multi-tenant isolation is enforced.
* Workplace isolation is enforced.
* Subscription entitlements are enforced.
* Feature flags are supported.
* Deep links cannot bypass authorization.
* Administrative navigation is privileged.
* Client navigation is isolated.
* AI navigation is permission-aware.
* Agent navigation is permission-aware.
* Workflow navigation is permission-aware.
* Knowledge navigation is permission-aware.
* Global search respects authorization.
* Notifications respect authorization.
* Billing navigation is restricted.
* Security navigation is restricted.
* Navigation changes invalidate relevant caches.
* Navigation events are observable.
* Security-sensitive navigation is auditable.
* Navigation is accessible.
* Navigation is responsive.
* Navigation supports localization.
* Navigation degrades safely.
* Navigation is scalable for enterprise workloads.

---

## 59. Definition of Done

`navigation_architecture.md` is implemented when SalesGenie provides a unified navigation platform capable of dynamically determining:

```text
WHO
  ↓
IS THE USER?

WHERE
  ↓
ARE THEY?

WHAT
  ↓
ROLE DO THEY HAVE?

WHICH
  ↓
PERMISSIONS DO THEY HAVE?

WHICH
  ↓
RESOURCES CAN THEY ACCESS?

WHICH
  ↓
FEATURES DOES THEIR PLAN INCLUDE?

WHICH
  ↓
FEATURE FLAGS ARE ACTIVE?

WHICH
  ↓
AI CAPABILITIES ARE AVAILABLE?

WHICH
  ↓
WORKSPACE/TEAM CONTEXT APPLIES?

WHAT
  ↓
NAVIGATION SHOULD BE SHOWN?

AND FINALLY:

CAN THE BACKEND
AUTHORIZE THE REQUEST?
```

The frontend MUST provide the navigation experience, but the backend MUST remain the ultimate authority for access control.

```text
IDENTITY
   ↓
TENANT
   ↓
WORKSPACE
   ↓
ROLE
   ↓
PERMISSION
   ↓
ABAC POLICY
   ↓
ENTITLEMENT
   ↓
FEATURE FLAG
   ↓
RESOURCE AUTHORIZATION
   ↓
NAVIGATION
   ↓
ROUTE GUARD
   ↓
BACKEND AUTHORIZATION
   ↓
RESOURCE
```

This architecture ensures that SalesGenie navigation scales from a simple SaaS interface into a secure enterprise platform supporting sales, marketing, SEO, finance, support, AI agents, RAG, workflows, integrations, analytics, administration, and AI-human hybrid operations.
