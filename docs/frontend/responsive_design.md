# SalesGenie Responsive Design Requirements

**Document:** `responsive_design.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Document Type:** User Requirements + System Requirements + Functional Requirements  
**Scope:** Responsive Web Application, Enterprise SaaS, AI + Human Operations  
**Requirement Level:** FAANG / Enterprise Production Grade  
**Status:** Required  
**Priority:** P0 unless otherwise specified  

---

## 1. Document Purpose

This document defines the responsive design requirements for SalesGenie.

SalesGenie must provide a consistent, accessible, performant, secure, and adaptive user experience across:

- Desktop
- Laptop
- Tablet
- Mobile browser
- Large enterprise displays
- Touch devices
- Keyboard-only environments
- Assistive technology environments
- Low-bandwidth environments
- Different browser viewport sizes
- Different device pixel densities

Responsive behavior must not be implemented as a purely visual frontend concern.

Any UI state that depends on:

- User identity
- Organization
- Workplace
- Role
- Permissions
- Subscription
- Feature entitlements
- Backend configuration
- AI agent state
- Workflow state
- Integration state
- Notification state
- Data availability
- Security policy
- Usage limits
- Billing state

must be driven by authoritative backend APIs.

---

## 2. Product Context

SalesGenie is an enterprise multi-tenant AI platform supporting:

- AI customer support
- Human customer support
- Sales
- Marketing
- SEO
- Lead generation
- CRM
- Product launch intelligence
- Business intelligence
- Financial analytics
- Advertising intelligence
- AI agents
- Multi-agent orchestration
- RAG
- Knowledge management
- Workflow automation
- Omnichannel communication
- Integrations
- Reporting
- Billing
- Administration
- Security
- Observability
- AI + human hybrid operations

The responsive architecture must therefore support highly complex enterprise workflows rather than only simple marketing pages.

---

## 3. Responsive Design Goals

## UR-RD-001 — Device Independence

Users SHALL be able to access SalesGenie functionality across supported viewport sizes without loss of core functionality.

## UR-RD-002 — Progressive Adaptation

The interface SHALL progressively adapt layout, navigation, density, controls, and interaction patterns based on available viewport space.

## UR-RD-003 — Functional Preservation

Responsive transformations SHALL NOT silently remove business-critical functionality.

## UR-RD-004 — Enterprise Usability

Users SHALL be able to efficiently operate complex enterprise workflows on large and medium screens.

## UR-RD-005 — Mobile Usability

Users SHALL be able to perform critical operational tasks on mobile devices.

## UR-RD-006 — Accessibility

Responsive behavior SHALL preserve accessibility across viewport sizes and input methods.

## UR-RD-007 — Performance

Responsive layouts SHALL minimize unnecessary rendering, data fetching, asset loading, and JavaScript execution.

## UR-RD-008 — Backend Consistency

Frontend responsive states SHALL remain synchronized with backend authorization, configuration, tenant, subscription, workflow, AI, and operational state.

---

## 4. Supported Viewport Classes

SalesGenie SHALL support the following logical responsive classes.

| Class | Width | Primary Use |
|---|---:|---|
| XS | `< 480px` | Small mobile |
| SM | `480–767px` | Mobile |
| MD | `768–1023px` | Tablet |
| LG | `1024–1279px` | Small desktop |
| XL | `1280–1535px` | Standard desktop |
| 2XL | `1536–1919px` | Large desktop |
| 3XL | `1920px+` | Enterprise / large display |

The implementation SHALL avoid excessive dependence on fixed device-specific breakpoints.

Responsive behavior SHOULD primarily be based on available container space.

---

## 5. User Requirements

## 5.1 General Responsive Requirements

## UR-RD-010 — Consistent Experience

Users SHALL receive a consistent SalesGenie experience regardless of supported screen size.

## UR-RD-011 — Content Preservation

Important business information SHALL remain accessible when the viewport becomes smaller.

## UR-RD-012 — No Horizontal Overflow

Primary application screens SHALL NOT require horizontal scrolling under normal supported viewport sizes.

## UR-RD-013 — Touch Compatibility

Interactive controls SHALL support touch interaction on touch-capable devices.

## UR-RD-014 — Keyboard Compatibility

Responsive transformations SHALL preserve keyboard navigation.

## UR-RD-015 — Orientation Support

Tablet and mobile interfaces SHALL support portrait and landscape orientations where practical.

## UR-RD-016 — Zoom Support

The application SHALL remain usable when users increase browser zoom.

## UR-RD-017 — Dynamic Content

Long names, large numbers, translated text, AI-generated content, and user-generated content SHALL not break layouts.

---

## 5.2 Authentication and Identity

Responsive authentication interfaces SHALL support:

- Login
- Signup
- Logout
- Password reset
- Password recovery
- MFA
- OAuth
- Account verification
- Session expiration
- Session recovery
- Device/session management
- Organization selection
- Workplace selection

Backend-connected requirements:

- Authentication API
- Session API
- MFA API
- OAuth API
- User profile API
- Organization API
- Workplace API
- Authorization API

The frontend SHALL display authentication states based on backend responses rather than local assumptions.

---

## 5.3 Role-Based Responsive Experiences

SalesGenie supports:

- Super Admin
- Platform Admin
- Security Admin
- Billing Admin
- Organization Owner
- Organization Admin
- Workplace Admin
- Team Manager
- Sales Manager
- Sales Agent
- Marketing Manager
- Marketing Specialist
- SEO Manager
- SEO Specialist
- Product Manager
- Finance Manager
- Business Analyst
- Support Manager
- Support Agent
- AI Agent Builder
- Developer
- End User
- External Client

The responsive interface SHALL dynamically adapt based on:

```text
User
  ↓
Organization
  ↓
Workplace
  ↓
Team
  ↓
Role
  ↓
Permissions
  ↓
Feature Entitlements
  ↓
Responsive UI
```

Frontend SHALL NOT independently determine authorization.

---

## 5.4 Navigation

Desktop navigation SHALL support:

* Sidebar
* Secondary navigation
* Breadcrumbs
* Workspace switcher
* Organization switcher
* Global search
* Notifications
* User menu

Tablet navigation SHOULD support:

* Collapsible sidebar
* Drawer navigation
* Condensed navigation

Mobile navigation SHOULD support:

* Bottom navigation for high-frequency functions
* Hamburger/drawer navigation
* Contextual navigation
* Mobile command menu
* Mobile workspace selector

Navigation visibility SHALL be permission-aware.

Backend dependencies:

* `/auth/me`
* `/organizations`
* `/workplaces`
* `/permissions`
* `/roles`
* `/feature-entitlements`
* `/navigation`
* `/notifications`

---

## 5.5 Responsive Dashboard

Users SHALL be able to access dashboards across device sizes.

Dashboard components SHALL include:

* KPI cards
* Charts
* Tables
* AI insights
* Alerts
* Activity feeds
* Tasks
* Recommendations
* Recent conversations
* Recent leads
* Sales pipeline
* Campaign performance
* Revenue
* Profit/loss
* AI agent metrics
* System status

Desktop:

```text
┌────────────────────────────────────────────────────┐
│ Header                                             │
├────────────┬───────────────────────────────────────┤
│ Sidebar    │ KPI KPI KPI KPI                      │
│            │                                       │
│            │ Charts        AI Insights             │
│            │                                       │
│            │ Tables        Activity                │
└────────────┴───────────────────────────────────────┘
```

Mobile:

```text
┌──────────────────────┐
│ Header               │
├──────────────────────┤
│ KPI                  │
│ KPI                  │
│ KPI                  │
│                      │
│ Chart                │
│                      │
│ AI Insight           │
│                      │
│ Activity              │
├──────────────────────┤
│ Bottom Navigation    │
└──────────────────────┘
```

Dashboard data SHALL be fetched through backend APIs.

---

## 5.6 Sales Interface

Responsive sales functionality SHALL support:

* Lead list
* Lead details
* Lead scoring
* Lead enrichment
* Lead qualification
* Lead routing
* Lead assignment
* Lead segmentation
* Lead discovery
* Lead intelligence
* Contacts
* Accounts
* Opportunities
* Deals
* Pipeline
* Sales funnel
* Forecasting
* Sales analytics
* Sales sequences
* Outreach
* Tasks
* Notes
* Activities

Desktop SHALL support multi-column workflows.

Mobile SHALL prioritize:

1. Lead identity
2. Lead score
3. Contact actions
4. Qualification
5. Assignment
6. Next action
7. AI recommendations

Backend connections SHALL include lead, CRM, scoring, enrichment, assignment, activity, and AI recommendation APIs.

---

## 5.7 Lead Generation

Responsive lead-generation screens SHALL support:

* Search
* Filters
* Advanced filters
* Saved searches
* Lead results
* Company intelligence
* Person intelligence
* Intent signals
* Buying signals
* AI recommendations
* Lead scoring
* Lead enrichment
* Lead verification
* Lead export
* Lead assignment

Mobile SHALL provide a filter drawer rather than attempting to display all filter controls simultaneously.

---

## 5.8 Customer Support

Responsive support interfaces SHALL support:

* Ticket queue
* Conversation queue
* Customer profile
* Conversation history
* AI responses
* Human responses
* AI/human handoff
* Internal notes
* SLA status
* Priority
* Assignment
* Escalation
* Sentiment
* Customer satisfaction
* Knowledge base
* Suggested responses

Desktop SHALL support:

```text
Conversation List | Conversation | Customer Context
```

Tablet SHALL support:

```text
Conversation List
        ↓
Conversation
        ↓
Customer Context
```

Mobile SHALL use navigable panels/screens.

Backend dependencies:

* Conversation APIs
* Ticket APIs
* Customer APIs
* AI agent APIs
* Human agent APIs
* SLA APIs
* Assignment APIs
* Knowledge APIs
* Escalation APIs

---

## 5.9 AI Agent Interface

Responsive AI-agent interfaces SHALL support:

* Agent list
* Agent creation
* Agent configuration
* Agent tools
* Agent memory
* Agent permissions
* Agent instructions
* Agent knowledge
* Agent workflows
* Agent testing
* Agent deployment
* Agent versioning
* Agent observability
* Agent evaluation
* Agent analytics
* Agent human handoff

Mobile SHALL provide simplified configuration while preserving access to advanced configuration through expandable sections.

---

## 5.10 Workflow Builder

Workflow builder functionality SHALL adapt to available screen space.

Desktop SHALL support:

```text
Trigger → Condition → Action → Condition → Action
```

Tablet SHALL support collapsible side panels.

Mobile SHALL use:

```text
Node
 ↓
Node
 ↓
Node
 ↓
Node
```

The workflow canvas SHALL NOT depend exclusively on desktop dimensions.

Backend dependencies:

* Workflow CRUD API
* Workflow execution API
* Workflow validation API
* Workflow version API
* Workflow trigger API
* Workflow action API
* Workflow execution logs API
* Workflow template API

---

## 5.11 RAG and Knowledge Management

Responsive knowledge management SHALL support:

* Document upload
* Document browsing
* Search
* Semantic search
* Hybrid search
* Document preview
* Metadata
* Permissions
* Knowledge bases
* Chunking status
* Embedding status
* Indexing status
* Retrieval testing
* RAG evaluation

Mobile SHALL replace wide data tables with card/list views.

Backend dependencies:

* Document API
* Object storage API
* Processing status API
* Embedding API
* Vector search API
* Knowledge-base API
* Permission API

---

## 5.12 Marketing

Responsive marketing interfaces SHALL support:

* Campaign management
* Audience management
* Content generation
* Email marketing
* Social media
* Advertising
* Campaign analytics
* Attribution
* Budget management
* AI recommendations

Charts SHALL resize according to container dimensions.

Large datasets SHALL use pagination or virtualization.

---

## 5.13 SEO

Responsive SEO interfaces SHALL support:

* SEO audits
* Keyword research
* Keyword clustering
* SERP analysis
* Rank tracking
* Backlink analysis
* Competitor SEO
* Content gaps
* SEO content generation
* SEO analytics

Mobile data tables SHALL use:

* Horizontal scroll only where unavoidable
* Priority columns
* Expandable rows
* Detail pages

---

## 5.14 Financial and Business Intelligence

Responsive financial interfaces SHALL support:

* Revenue
* Expenses
* Profit
* Loss
* Cash flow
* Product profitability
* Forecasts
* Budgets
* Business health
* Growth analytics
* AI recommendations

Financial information SHALL remain readable without truncating critical monetary values.

Backend data SHALL determine:

* Currency
* Decimal precision
* Fiscal period
* User permissions
* Organization settings
* Financial visibility

---

## 5.15 Reporting

Responsive reporting SHALL support:

* Report builder
* Dashboards
* Charts
* Tables
* Filters
* Saved reports
* Scheduled reports
* Excel export
* CSV export
* PDF export
* JSON export

Export actions SHALL be backend-controlled.

Long-running exports SHALL provide asynchronous job status.

---

## 5.16 Administration

Responsive admin interfaces SHALL support:

* User management
* Role management
* Permission management
* Organization management
* Workplace management
* System configuration
* Feature flags
* Audit logs
* Platform monitoring
* Incident management
* Billing administration

Dangerous administrative actions SHALL require appropriate confirmation and authorization.

---

## 5.17 Billing

Responsive billing interfaces SHALL support:

* Current plan
* Subscription status
* Usage
* Quotas
* Invoices
* Payment methods
* Billing history
* Upgrade
* Downgrade
* Cancellation
* Refund status
* Payment errors

Backend SHALL determine:

* Current plan
* Subscription state
* Usage
* Limits
* Entitlements
* Billing permissions
* Payment status

---

## 5.18 Notifications

Responsive notification interfaces SHALL support:

* In-app notifications
* Email notifications
* Push notifications
* Notification center
* Notification preferences
* Notification categories
* Read/unread state
* Notification actions

Unread counts SHALL be synchronized with backend state.

---

## 5.19 Global Search

Responsive global search SHALL support:

* Users
* Leads
* Companies
* Contacts
* Conversations
* Tickets
* Documents
* Workflows
* AI agents
* Reports
* Organizations
* Workplaces

Desktop SHALL support a global search modal.

Mobile SHALL support a dedicated search page.

Search results SHALL be permission-filtered server-side.

---

## 5.20 External Client Portal

External clients SHALL receive responsive access to:

* Dashboard
* Projects
* Reports
* Analytics
* Support
* AI agents
* Integrations
* Billing
* Documents
* Team members

External clients SHALL never receive UI access to unauthorized internal modules.

---

## 6. System Requirements

## 6.1 Responsive Layout Engine

## SR-RD-001

The frontend SHALL implement a centralized responsive layout system.

## SR-RD-002

Responsive breakpoints SHALL be centrally defined.

## SR-RD-003

Components SHALL use fluid sizing where appropriate.

## SR-RD-004

The system SHALL support CSS container queries where appropriate.

## SR-RD-005

Layout components SHALL avoid hard-coded viewport assumptions.

## SR-RD-006

The system SHALL support adaptive component composition.

---

## 6.2 Responsive Component Architecture

The frontend SHALL implement reusable responsive primitives:

```text
ResponsiveLayout
ResponsiveContainer
ResponsiveGrid
ResponsiveStack
ResponsiveSidebar
ResponsiveDrawer
ResponsiveModal
ResponsiveTable
ResponsiveCard
ResponsiveTabs
ResponsiveToolbar
ResponsiveForm
ResponsiveChart
ResponsiveNavigation
ResponsivePagination
ResponsiveCommandMenu
ResponsiveDataView
ResponsiveDetailView
```

Each component SHALL have predictable behavior across viewport classes.

---

## 6.3 Adaptive Navigation Architecture

The system SHALL implement:

```text
Desktop
   ↓
Sidebar + Header

Tablet
   ↓
Collapsible Sidebar + Header

Mobile
   ↓
Drawer + Header + Bottom Navigation
```

Navigation SHALL be generated from:

```text
User
+
Role
+
Permissions
+
Organization
+
Workplace
+
Subscription
+
Feature Flags
```

---

## 6.4 Backend-Driven UI Configuration

The backend SHOULD support a UI configuration endpoint such as:

```http
GET /api/v1/ui/config
```

Potential response:

```json
{
  "theme": {},
  "navigation": [],
  "features": {},
  "branding": {},
  "layout": {},
  "dashboard": {},
  "localization": {},
  "accessibility": {},
  "experiments": {}
}
```

The frontend SHALL validate and safely consume this configuration.

---

## 6.5 Responsive Feature Flags

Responsive behavior MAY be controlled through feature flags.

Example:

```json
{
  "mobile_bottom_navigation": true,
  "responsive_workflow_builder": true,
  "mobile_ai_agent_builder": true,
  "adaptive_dashboard": true
}
```

Feature flag evaluation SHALL respect:

* User
* Organization
* Workplace
* Environment
* Subscription
* Role
* Experiment assignment

---

## 6.6 Responsive Theming

The design system SHALL support:

* Light mode
* Dark mode
* System mode
* Organization branding
* Custom logos
* Custom typography
* Custom spacing
* Custom colors
* Accessibility contrast settings

Backend-controlled organization branding SHALL be sanitized before rendering.

---

## 6.7 Responsive Data Tables

Tables SHALL support:

* Desktop table mode
* Tablet condensed table
* Mobile card mode
* Column prioritization
* Row expansion
* Pagination
* Server-side filtering
* Server-side sorting
* Server-side search
* Virtualization for large datasets

Example:

```text
Desktop:

Name | Company | Score | Status | Owner | Revenue | Actions

Mobile:

Name
Company
Score
Status
Owner
[View Details]
```

---

## 6.8 Responsive Forms

Forms SHALL support:

* Single-column mobile layout
* Multi-column desktop layout
* Field grouping
* Validation
* Error summaries
* Inline errors
* Conditional fields
* Dynamic fields
* Autosave where required
* Draft state
* Backend validation

Form validation SHALL not rely exclusively on frontend validation.

---

## 6.9 Responsive Charts

Charts SHALL support:

* Dynamic dimensions
* Responsive legends
* Tooltip adaptation
* Touch interaction
* Reduced label density
* Accessible data alternatives
* Data table fallback

Charts SHALL NOT render unreadable labels on small screens.

---

## 6.10 Responsive Modals

Large desktop dialogs SHALL transform into:

* Centered modal on desktop
* Large modal on tablet
* Full-screen sheet on mobile

Critical actions SHALL remain accessible.

---

## 6.11 Responsive Drawers

Drawers SHALL support:

* Left drawer
* Right drawer
* Bottom sheet
* Full-screen mobile drawer

Drawer state SHALL be accessible and keyboard navigable.

---

## 6.12 Responsive Notifications

Notification presentation SHALL adapt:

```text
Desktop → Toast
Tablet  → Toast / Panel
Mobile  → Toast / Bottom Sheet / Notification Center
```

---

## 6.13 Responsive AI Streaming

AI-generated responses SHALL support streaming on all supported devices.

The UI SHALL handle:

* Partial tokens
* Long responses
* Markdown
* Tables
* Code blocks
* Citations
* Tool execution
* Agent status
* Loading state
* Cancellation
* Retry
* Errors

Backend streaming may use:

* SSE
* WebSocket
* HTTP streaming

The frontend SHALL gracefully fall back where streaming is unavailable.

---

## 6.14 Responsive Real-Time State

The frontend SHALL synchronize:

* Conversations
* Notifications
* AI agent status
* Workflow execution
* Lead updates
* Ticket updates
* Assignment changes
* Billing state
* System incidents

Possible mechanisms:

```text
WebSocket
SSE
Polling
Event-driven cache invalidation
```

---

## 6.15 Offline and Poor Network Handling

The application SHALL detect:

* Offline state
* Slow network
* Connection loss
* Reconnection
* Request timeout

The UI SHALL provide:

```text
Online
   ↓
Request
   ↓
Connection Lost
   ↓
Retry / Queue / Recover
```

Non-critical data MAY be cached locally.

Critical authorization and security state SHALL NOT rely solely on stale local data.

---

## 6.16 Responsive Loading Architecture

The system SHALL support:

* Skeleton loading
* Progressive rendering
* Lazy loading
* Code splitting
* Image lazy loading
* Component-level loading
* Route-level loading
* Streaming
* Virtualized lists

---

## 6.17 Performance Requirements

Responsive pages SHALL target:

| Metric                        |                            Target |
| ----------------------------- | --------------------------------: |
| Initial application response  |                       < 2s target |
| Interaction readiness         |                       < 3s target |
| API-dependent critical action | < 2s target where backend permits |
| Layout shift                  |                           Minimal |
| First Contentful Paint        |                     < 1.8s target |
| Largest Contentful Paint      |                     < 2.5s target |
| Cumulative Layout Shift       |                      < 0.1 target |
| Interaction responsiveness    |                    < 200ms target |

Targets SHALL be validated under realistic network and device conditions.

---

## 6.18 Mobile Performance

Mobile clients SHALL minimize:

* JavaScript bundle size
* Image size
* API requests
* Re-renders
* DOM size
* Memory consumption

Heavy modules such as:

* Workflow builder
* AI agent builder
* Advanced analytics
* Large data visualization
* Developer tools

SHALL be lazy-loaded.

---

## 6.19 Responsive Security

Responsive UI SHALL NOT weaken security.

Security requirements SHALL remain consistent across:

* Desktop
* Tablet
* Mobile

Security-sensitive functionality SHALL include:

* MFA
* Session management
* Permission checks
* Sensitive data masking
* Audit logging
* Re-authentication
* Confirmation
* Device/session management

The backend SHALL remain the authoritative security boundary.

---

## 6.20 Responsive Tenant Isolation

All tenant-scoped frontend requests SHALL include appropriate tenant context through authenticated backend mechanisms.

The frontend SHALL never allow users to select arbitrary:

* `tenant_id`
* `organization_id`
* `workplace_id`

without backend authorization.

---

## 6.21 Responsive Accessibility

The application SHALL support:

* WCAG 2.2 AA target
* Keyboard navigation
* Screen readers
* Focus management
* Reduced motion
* High contrast
* Text scaling
* Touch accessibility
* Accessible labels
* Semantic HTML
* ARIA where required

Responsive transformations SHALL preserve semantic structure.

---

## 7. Functional Requirements

## 7.1 Responsive Layout

## FR-RD-001

The system SHALL automatically select appropriate layouts based on available viewport dimensions.

## FR-RD-002

The system SHALL dynamically reflow grid components.

## FR-RD-003

The system SHALL collapse navigation when space becomes insufficient.

## FR-RD-004

The system SHALL convert desktop-only multi-column layouts into sequential mobile layouts.

## FR-RD-005

The system SHALL prevent accidental horizontal overflow.

---

## 7.2 Responsive Navigation

## FR-RD-010

The system SHALL retrieve authorized navigation items from frontend configuration and authorization state.

## FR-RD-011

The system SHALL hide unauthorized navigation items.

## FR-RD-012

The system SHALL support mobile navigation drawers.

## FR-RD-013

The system SHALL support mobile bottom navigation.

## FR-RD-014

The system SHALL preserve active route state during responsive transitions.

---

## 7.3 Responsive Dashboard

## FR-RD-020

The system SHALL request dashboard metrics from backend services.

## FR-RD-021

The system SHALL resize dashboard widgets according to available width.

## FR-RD-022

The system SHALL stack dashboard widgets on narrow screens.

## FR-RD-023

The system SHALL support user-configurable dashboard layouts.

## FR-RD-024

Dashboard configuration SHALL be persisted through backend APIs.

Example:

```http
GET    /api/v1/dashboard
POST   /api/v1/dashboard/layout
PATCH  /api/v1/dashboard/widgets/{id}
DELETE /api/v1/dashboard/widgets/{id}
```

---

## 7.4 Responsive Tables

## FR-RD-030

The system SHALL support desktop table mode.

## FR-RD-031

The system SHALL support mobile card mode.

## FR-RD-032

The system SHALL preserve sorting and filtering across responsive modes.

## FR-RD-033

The system SHALL preserve pagination state where appropriate.

## FR-RD-034

The system SHALL fetch paginated datasets from backend services.

---

## 7.5 Responsive Search

## FR-RD-040

Desktop search SHALL support command-style search.

## FR-RD-041

Mobile search SHALL support dedicated search interaction.

## FR-RD-042

Search results SHALL be permission-filtered.

## FR-RD-043

Search SHALL support backend pagination.

## FR-RD-044

Search SHALL support semantic search where configured.

---

## 7.6 Responsive Forms

## FR-RD-050

The system SHALL stack form fields on narrow screens.

## FR-RD-051

The system SHALL preserve validation state when layouts change.

## FR-RD-052

The system SHALL submit form data through backend APIs.

## FR-RD-053

The system SHALL display backend validation errors.

## FR-RD-054

The system SHALL prevent duplicate submissions.

---

## 7.7 Responsive AI

## FR-RD-060

The system SHALL support AI chat on mobile.

## FR-RD-061

The system SHALL support streaming AI responses.

## FR-RD-062

The system SHALL display AI tool execution state.

## FR-RD-063

The system SHALL support human handoff from mobile.

## FR-RD-064

The system SHALL display AI confidence information where configured.

## FR-RD-065

AI actions requiring human approval SHALL remain blocked until approval.

---

## 7.8 Responsive Human-in-the-Loop

The system SHALL support:

```text
AI Decision
     ↓
Confidence Evaluation
     ↓
Human Review Queue
     ↓
Approve / Reject / Modify
     ↓
Backend Execution
```

Mobile review interfaces SHALL expose:

* Decision
* Confidence
* Evidence
* AI reasoning summary
* Recommended action
* Approve
* Reject
* Edit
* Escalate

---

## 7.9 Responsive Workflow Execution

## FR-RD-070

Users SHALL be able to inspect workflow execution from mobile.

## FR-RD-071

Users SHALL be able to view workflow errors.

## FR-RD-072

Authorized users SHALL be able to retry failed workflows.

## FR-RD-073

Workflow execution status SHALL be synchronized with backend state.

---

## 7.10 Responsive Notifications

## FR-RD-080

The system SHALL display unread notification counts.

## FR-RD-081

The system SHALL synchronize read state with backend.

## FR-RD-082

Notification actions SHALL invoke authorized backend operations.

---

## 7.11 Responsive Billing

## FR-RD-090

Users SHALL be able to view subscription status on mobile.

## FR-RD-091

Users SHALL be able to view usage limits.

## FR-RD-092

Users SHALL be able to initiate authorized plan changes.

## FR-RD-093

Billing operations SHALL be confirmed server-side.

---

## 7.12 Responsive File Management

The system SHALL support:

* Upload
* Download
* Preview
* Delete
* Rename
* Search
* Filter
* Metadata
* Permissions

Mobile upload SHALL support native device file selection.

Backend SHALL validate:

* File type
* File size
* Malware status
* Authorization
* Tenant ownership

---

## 7.13 Responsive Reports

## FR-RD-100

Users SHALL be able to open reports on mobile.

## FR-RD-101

Reports SHALL automatically adapt chart and table layouts.

## FR-RD-102

Report exports SHALL be generated by backend services.

## FR-RD-103

Long-running report jobs SHALL expose job status.

---

## 7.14 Responsive Administration

## FR-RD-110

Authorized administrators SHALL be able to manage users from supported devices.

## FR-RD-111

Authorized administrators SHALL be able to view audit events.

## FR-RD-112

Security-sensitive actions SHALL require confirmation.

## FR-RD-113

Administrative permissions SHALL be validated by backend APIs.

---

## 8. Responsive Backend Integration Matrix

| Feature                   | Frontend   | Backend Required |
| ------------------------- | ---------- | ---------------- |
| Authentication            | Responsive | Yes              |
| Authorization             | Responsive | Yes              |
| RBAC                      | Responsive | Yes              |
| ABAC                      | Responsive | Yes              |
| Organization              | Responsive | Yes              |
| Workplace                 | Responsive | Yes              |
| Dashboard                 | Responsive | Yes              |
| Sales                     | Responsive | Yes              |
| Leads                     | Responsive | Yes              |
| CRM                       | Responsive | Yes              |
| Support                   | Responsive | Yes              |
| AI Agents                 | Responsive | Yes              |
| RAG                       | Responsive | Yes              |
| Workflows                 | Responsive | Yes              |
| Marketing                 | Responsive | Yes              |
| SEO                       | Responsive | Yes              |
| Finance                   | Responsive | Yes              |
| Analytics                 | Responsive | Yes              |
| Reporting                 | Responsive | Yes              |
| Notifications             | Responsive | Yes              |
| Billing                   | Responsive | Yes              |
| Integrations              | Responsive | Yes              |
| Search                    | Responsive | Yes              |
| Admin                     | Responsive | Yes              |
| Security                  | Responsive | Yes              |
| Audit                     | Responsive | Yes              |
| Feature Flags             | Responsive | Yes              |
| Usage Limits              | Responsive | Yes              |
| Subscription Entitlements | Responsive | Yes              |

---

## 9. Responsive API Requirements

The frontend SHALL use centralized API clients.

Recommended architecture:

```text
UI
 ↓
Responsive Components
 ↓
Feature Hooks / Services
 ↓
API Client
 ↓
API Gateway
 ↓
Microservices
```

The frontend SHALL NOT directly communicate with arbitrary internal microservices unless explicitly authorized by the architecture.

---

## 10. Recommended API Domains

Responsive UI SHALL integrate with:

```text
/api/v1/auth/*
/api/v1/users/*
/api/v1/organizations/*
/api/v1/workplaces/*
/api/v1/permissions/*
/api/v1/admin/*
/api/v1/dashboard/*
/api/v1/leads/*
/api/v1/crm/*
/api/v1/sales/*
/api/v1/support/*
/api/v1/conversations/*
/api/v1/agents/*
/api/v1/ai/*
/api/v1/rag/*
/api/v1/knowledge/*
/api/v1/workflows/*
/api/v1/marketing/*
/api/v1/seo/*
/api/v1/finance/*
/api/v1/analytics/*
/api/v1/reports/*
/api/v1/notifications/*
/api/v1/billing/*
/api/v1/integrations/*
/api/v1/search/*
/api/v1/files/*
/api/v1/audit/*
/api/v1/feature-flags/*
```

Exact endpoints SHALL follow the API architecture specification.

---

## 11. Responsive State Management

The frontend SHALL distinguish:

```text
Server State
Client State
UI State
Responsive State
Authentication State
Authorization State
Feature State
Connection State
```

Example:

```text
Server State
   ├── Leads
   ├── Conversations
   ├── AI Agents
   ├── Billing
   └── Analytics

Client/UI State
   ├── Sidebar Open
   ├── Modal Open
   ├── Active Tab
   └── Filters

Responsive State
   ├── Viewport
   ├── Input Mode
   └── Layout Mode
```

Responsive state SHALL NOT be used to duplicate authoritative server state.

---

## 12. Responsive Caching

The frontend SHALL cache appropriate non-sensitive server state.

Caching SHALL consider:

* Tenant
* Organization
* Workplace
* User
* Role
* Permission
* Subscription
* Resource version

Sensitive information SHALL NOT be persisted insecurely.

---

## 13. Responsive Error Handling

The system SHALL provide responsive error states for:

* 400
* 401
* 403
* 404
* 409
* 413
* 422
* 429
* 500
* 502
* 503
* Timeout
* Network failure
* Streaming failure

Example:

```text
Backend Error
      ↓
API Client
      ↓
Error Normalization
      ↓
Responsive Error Component
      ↓
Retry / Recovery / Escalation
```

---

## 14. Responsive Authentication Expiration

When a session expires:

```text
API Request
    ↓
401
    ↓
Authentication State
    ↓
Responsive Session Dialog
    ↓
Re-authenticate
    ↓
Retry Safe Request
```

The system SHALL avoid blindly retrying non-idempotent operations.

---

## 15. Responsive Authorization Changes

If permissions change during an active session:

```text
Permission Change
       ↓
Backend
       ↓
Session / Authorization Refresh
       ↓
Frontend State Update
       ↓
Navigation Update
       ↓
Component Update
```

The frontend SHALL immediately stop exposing newly unauthorized actions.

---

## 16. Responsive Subscription Enforcement

The UI SHALL adapt according to backend-provided entitlements.

Example:

```text
Subscription
     ↓
Entitlements
     ↓
Feature Access
     ↓
Responsive UI
```

The frontend MAY visually disable or hide unavailable features but SHALL NOT rely on frontend enforcement for billing security.

---

## 17. Responsive Empty States

Every major resource SHALL provide responsive empty states.

Examples:

* No leads
* No conversations
* No tickets
* No AI agents
* No workflows
* No documents
* No reports
* No notifications
* No integrations

Empty states SHALL provide contextual actions.

---

## 18. Responsive Skeleton States

Skeleton loaders SHALL match final component dimensions to reduce layout shift.

Examples:

```text
Dashboard → KPI skeletons
Table → Row skeletons
Conversation → Message skeletons
AI → Streaming skeleton
Chart → Chart skeleton
```

---

## 19. Responsive Accessibility Requirements

## FR-RD-150

All interactive elements SHALL be keyboard accessible.

## FR-RD-151

Focus SHALL remain visible.

## FR-RD-152

Modal focus SHALL be trapped appropriately.

## FR-RD-153

Closing a modal SHALL restore focus appropriately.

## FR-RD-154

Responsive navigation SHALL expose semantic labels.

## FR-RD-155

Charts SHALL have accessible alternatives.

## FR-RD-156

Color SHALL NOT be the only indicator of state.

## FR-RD-157

Touch targets SHALL be sufficiently large.

---

## 20. Responsive Internationalization

SalesGenie SHALL support localization.

Responsive layouts SHALL tolerate:

* Long translated strings
* RTL languages
* Different date formats
* Different number formats
* Different currencies
* Different text lengths

The system SHOULD support:

```text
LTR
RTL
```

Backend SHALL provide locale and organization settings where applicable.

---

## 21. Responsive Localization Data

The frontend SHALL retrieve applicable:

* Locale
* Timezone
* Currency
* Date format
* Number format
* Language
* Organization branding

from authoritative backend configuration where applicable.

---

## 22. Responsive Timezone Handling

Dates and times SHALL be rendered according to user or organization timezone configuration.

Examples:

* Conversation timestamp
* Lead activity
* Workflow execution
* AI agent execution
* Billing events
* Audit events
* Scheduled reports

Backend timestamps SHOULD use UTC.

Frontend SHALL convert timestamps for display.

---

## 23. Responsive Data Density

Desktop MAY display high-density information.

Tablet SHALL reduce density.

Mobile SHALL prioritize:

```text
Identity
Status
Priority
Critical Metric
Primary Action
```

Secondary information SHALL be available through expansion.

---

## 24. Responsive Interaction Priority

For every screen:

```text
Primary Action
      ↓
Primary Information
      ↓
Secondary Actions
      ↓
Advanced Information
```

Mobile interfaces SHALL not expose every desktop action simultaneously.

---

## 25. Responsive Command System

SalesGenie SHOULD support a command system accessible from:

* Desktop keyboard
* Tablet
* Mobile search

Examples:

```text
Create Lead
Create Campaign
Create AI Agent
Create Workflow
Search Customer
Open Dashboard
View Reports
Open Settings
```

Command availability SHALL respect backend authorization.

---

## 26. Responsive Deep Linking

All responsive views SHALL support direct URLs where appropriate.

Example:

```text
/sales/leads/123
/support/conversations/456
/agents/789
/workflows/123
/reports/456
```

Deep links SHALL enforce authentication and authorization.

---

## 27. Responsive URL State

The application MAY persist:

* Filters
* Search
* Sorting
* Pagination
* Selected tab

in URL state.

Sensitive data SHALL NOT be placed in URLs.

---

## 28. Responsive Browser Compatibility

The system SHALL support current production versions of:

* Chrome
* Firefox
* Safari
* Edge

The exact browser support matrix SHALL be defined by release policy.

---

## 29. Responsive Device Compatibility

The application SHALL support:

* Standard laptops
* Desktop monitors
* High-DPI displays
* Tablets
* Smartphones
* Touch laptops
* External keyboards
* Trackpads
* Mouse devices

---

## 30. Responsive Testing Requirements

The testing system SHALL validate:

```text
Desktop
Tablet
Mobile
Landscape
Portrait
Touch
Keyboard
Screen Reader
High Zoom
Dark Mode
Light Mode
Slow Network
Offline
Reconnect
Large Data
Long Text
Localization
RTL
```

---

## 31. Responsive Visual Regression Testing

Critical pages SHALL have automated responsive visual regression tests.

Required pages:

* Login
* Signup
* Dashboard
* Lead generation
* Lead details
* CRM
* Support inbox
* Conversation
* AI agent builder
* Workflow builder
* Knowledge base
* Marketing
* SEO
* Finance
* Reports
* Billing
* Admin
* Client portal

---

## 32. Responsive E2E Testing

E2E tests SHALL validate critical workflows at multiple viewport sizes.

Example:

```text
Desktop:
Login → Dashboard → Lead → Qualification → Assignment

Tablet:
Login → Support → Conversation → AI → Human Handoff

Mobile:
Login → Notification → Lead → Call/Email Action

Mobile:
Login → AI Agent → Conversation → Approval

Desktop:
Login → Workflow Builder → Publish → Execute
```

---

## 33. Responsive Performance Testing

Performance testing SHALL include:

* Cold load
* Warm load
* Mobile CPU
* Mobile memory
* Slow 3G
* 4G
* Wi-Fi
* High latency
* Large datasets
* Long AI responses
* Real-time updates

---

## 34. Responsive Observability

Frontend telemetry SHOULD capture:

* Viewport class
* Route
* Component performance
* API latency
* Render performance
* JavaScript errors
* Network errors
* Responsive layout errors
* User interaction latency

Sensitive personal information SHALL NOT be captured unnecessarily.

---

## 35. Responsive Analytics

The system MAY collect:

```text
viewport_class
device_category
orientation
feature_usage
navigation_usage
mobile_feature_usage
desktop_feature_usage
responsive_error_rate
```

Analytics SHALL respect privacy and consent requirements.

---

## 36. Responsive Feature Adoption

Product analytics SHALL identify whether functionality is usable across device classes.

Example:

```text
Feature
  ↓
Desktop Usage
Tablet Usage
Mobile Usage
  ↓
Conversion
  ↓
Error Rate
  ↓
Performance
```

---

## 37. Responsive Security and Privacy

Responsive UI SHALL not expose:

* API keys
* Secrets
* Passwords
* Access tokens
* Internal service credentials
* Sensitive customer data
* Unauthorized tenant data

Screenshots, browser storage, logs, and telemetry SHALL be considered potential data leakage surfaces.

---

## 38. Responsive Data Masking

Sensitive fields SHALL support masking on smaller devices and shared environments where appropriate.

Examples:

* Payment information
* Personal information
* API keys
* Customer contact details
* Financial data

Masking SHALL be controlled by backend authorization and policy.

---

## 39. Responsive Mobile Security

Mobile browser interfaces SHALL support:

* Session expiration
* MFA
* Secure logout
* Permission checks
* Re-authentication
* Sensitive action confirmation
* Session revocation

---

## 40. Responsive Deployment Requirements

Responsive frontend releases SHALL be deployed through:

```text
Source Control
     ↓
CI
     ↓
Unit Tests
     ↓
Integration Tests
     ↓
Visual Tests
     ↓
E2E Tests
     ↓
Performance Tests
     ↓
Security Tests
     ↓
Build
     ↓
Staging
     ↓
Production
```

---

## 41. Responsive Feature Rollout

Responsive functionality SHALL support:

* Feature flags
* Canary releases
* A/B testing
* Gradual rollout
* Rollback

Example:

```text
1%
 ↓
5%
 ↓
25%
 ↓
50%
 ↓
100%
```

---

## 42. Responsive Design Tokens

The design system SHALL define centralized tokens for:

```text
Spacing
Typography
Colors
Borders
Radius
Shadows
Breakpoints
Container Widths
Grid
Motion
Z-index
Touch Targets
```

Responsive components SHALL consume tokens rather than hard-coded values.

---

## 43. Responsive Grid System

The system SHALL support:

```text
Desktop:
12-column grid

Tablet:
8-column grid

Mobile:
4-column grid
```

Actual implementation SHOULD prefer fluid CSS grid behavior rather than rigid device assumptions.

---

## 44. Responsive Container System

Containers SHALL support:

* Fluid width
* Maximum width
* Minimum padding
* Nested containers
* Full-width sections

Example:

```text
Viewport
   ↓
Page Container
   ↓
Content Container
   ↓
Responsive Grid
   ↓
Components
```

---

## 45. Responsive Typography

Typography SHALL adapt without causing:

* Text overflow
* Excessive wrapping
* Unreadable text
* Layout collapse

The system SHOULD use fluid typography where appropriate.

---

## 46. Responsive Images

Images SHALL support:

* Responsive sizing
* Lazy loading
* Appropriate compression
* Modern formats
* Responsive sources
* Alt text

User-uploaded images SHALL be served through secure backend/object-storage infrastructure.

---

## 47. Responsive File Upload

Mobile file upload SHALL support:

* Camera capture where appropriate
* Gallery
* Files
* Drag-and-drop on desktop
* Progress
* Cancellation
* Retry
* Failure recovery

Upload state SHALL be backed by backend APIs.

---

## 48. Responsive Drag-and-Drop

Drag-and-drop SHALL support:

* Desktop mouse interaction
* Touch interaction where practical
* Keyboard alternatives

Critical functionality SHALL never depend exclusively on drag-and-drop.

---

## 49. Responsive AI Agent Builder

Desktop:

```text
Agent Configuration | Canvas | Preview
```

Tablet:

```text
Configuration
Canvas
Preview
```

Mobile:

```text
Agent
 ↓
Configuration
 ↓
Tools
 ↓
Knowledge
 ↓
Permissions
 ↓
Test
 ↓
Deploy
```

Backend SHALL persist:

* Agent configuration
* Versions
* Tools
* Permissions
* Knowledge sources
* Deployment state
* Evaluation state

---

## 50. Responsive Workflow Builder

Desktop SHALL provide an advanced visual canvas.

Mobile SHALL provide a sequential workflow editor.

Both modes SHALL operate on the same backend workflow model.

```text
Desktop Representation
        ↕
Same Workflow Model
        ↕
Mobile Representation
```

The responsive frontend SHALL NOT create incompatible workflow schemas.

---

## 51. Responsive Omnichannel Support

Users SHALL be able to manage:

* Webchat
* Email
* WhatsApp
* Facebook Messenger
* Instagram
* Telegram
* SMS
* Voice

from supported devices.

Channel availability SHALL be determined by:

* Integration status
* Organization configuration
* Permissions
* Subscription
* Backend health

---

## 52. Responsive Integration Management

Responsive integration pages SHALL support:

* Connect
* Disconnect
* Reauthorize
* Configure
* Sync
* View status
* View errors
* Retry

Secrets SHALL never be rendered in plaintext.

---

## 53. Responsive System Status

Administrators SHALL be able to view:

* Service health
* Incident status
* Integration health
* AI provider health
* Database health
* Queue health
* Workflow health

Mobile SHALL prioritize:

```text
Service
Status
Severity
Impact
Started
Action
```

---

## 54. Responsive Incident Management

Authorized administrators SHALL be able to:

* View incidents
* Acknowledge incidents
* Assign incidents
* Update status
* Add notes
* Resolve incidents

All incident actions SHALL be audited.

---

## 55. Responsive Audit Logs

Audit logs SHALL support:

* Search
* Filter
* Date range
* User
* Organization
* Action
* Resource
* Severity

Mobile SHALL prioritize event summary with expandable details.

---

## 56. Responsive Error Recovery

Every major backend-dependent operation SHALL define:

```text
Loading
Success
Empty
Error
Retry
Unauthorized
Forbidden
Offline
Timeout
```

No backend-dependent screen SHALL remain indefinitely blank during an error.

---

## 57. Responsive Optimistic Updates

Optimistic updates MAY be used for safe operations.

They SHALL:

* Reconcile with backend response
* Roll back on failure
* Avoid unauthorized state
* Avoid duplicate operations

Financial, security, permission, and destructive operations SHOULD generally avoid unsafe optimistic behavior.

---

## 58. Responsive Concurrency

The frontend SHALL handle concurrent updates from:

* Multiple users
* AI agents
* Workflows
* Integrations
* Background jobs

Potential mechanisms:

```text
Version IDs
ETags
Optimistic Concurrency Control
WebSocket Events
SSE
Conflict Detection
```

---

## 59. Responsive Autosave

Where enabled, autosave SHALL:

* Debounce updates
* Display save state
* Handle network failures
* Avoid data loss
* Resolve conflicts

Example:

```text
Editing
  ↓
Unsaved
  ↓
Saving
  ↓
Saved
```

---

## 60. Responsive Draft Recovery

Critical editors SHALL support draft recovery where appropriate.

Examples:

* AI prompts
* Workflow configuration
* Campaign content
* Reports
* Knowledge metadata
* Agent configuration

---

## 61. Responsive Confirmation Policies

The system SHALL require confirmation for destructive actions such as:

* Delete user
* Delete organization
* Delete workflow
* Delete AI agent
* Delete knowledge base
* Cancel subscription
* Disconnect integration
* Revoke access
* Delete financial data

Confirmation UI SHALL adapt to device size.

---

## 62. Responsive Progressive Disclosure

Advanced enterprise controls SHALL be progressively disclosed.

Example:

```text
Basic Configuration
        ↓
Advanced Configuration
        ↓
Expert Configuration
```

This prevents mobile interfaces from becoming unusably dense.

---

## 63. Responsive Personalization

Users MAY customize:

* Dashboard
* Navigation
* Density
* Theme
* Notifications
* Default workspace
* Default filters

Persistent personalization SHALL be stored server-side when it is expected to follow the user across devices.

---

## 64. Cross-Device State Synchronization

When a user moves between devices, server-backed preferences SHALL synchronize.

Examples:

```text
Desktop
  ↓
Dashboard layout saved
  ↓
Server
  ↓
Mobile
  ↓
Same user preference
```

---

## 65. Responsive Role Switching

If authorized users can switch organizational context:

```text
User
 ↓
Organization Selector
 ↓
Workplace Selector
 ↓
Backend Context Validation
 ↓
Refresh Permissions
 ↓
Refresh Navigation
 ↓
Refresh Data
```

---

## 66. Responsive Multi-Tenant Branding

External organizations MAY have custom:

* Logo
* Brand name
* Colors
* Favicon
* Email identity
* Login branding

Responsive branding SHALL not compromise usability or accessibility.

---

## 67. Responsive PWA Considerations

SalesGenie MAY support Progressive Web App capabilities.

Potential capabilities:

* Installability
* Push notifications
* Offline shell
* Background sync
* App-like navigation

Security-sensitive operations SHALL still require online backend validation.

---

## 68. Responsive Mobile Future Architecture

The responsive web architecture SHALL avoid blocking future:

* iOS application
* Android application
* React Native application
* Flutter application

The backend API contracts SHALL remain platform-neutral.

---

## 69. Backend Contract Principle

The responsive frontend SHALL consume stable backend contracts.

```text
Frontend Responsive UI
          ↓
Stable API Contract
          ↓
API Gateway
          ↓
Domain Services
```

Responsive layout changes SHALL NOT require unnecessary backend changes.

---

## 70. Definition of Done

Responsive design SHALL be considered complete only when:

* [ ] Desktop layouts work
* [ ] Tablet layouts work
* [ ] Mobile layouts work
* [ ] Portrait mode works
* [ ] Landscape mode works
* [ ] Touch interaction works
* [ ] Keyboard navigation works
* [ ] Screen reader behavior works
* [ ] Dark mode works
* [ ] Light mode works
* [ ] Long text does not break layouts
* [ ] Large numbers do not overflow
* [ ] Localization does not break layouts
* [ ] RTL is supported where required
* [ ] API loading states work
* [ ] API errors work
* [ ] Authentication expiration works
* [ ] Authorization changes work
* [ ] Subscription restrictions work
* [ ] Feature flags work
* [ ] Real-time updates work
* [ ] Offline/reconnect behavior works
* [ ] AI streaming works
* [ ] Human handoff works
* [ ] Workflow interfaces work
* [ ] Dashboard works
* [ ] Tables work
* [ ] Charts work
* [ ] Forms work
* [ ] Reports work
* [ ] Billing works
* [ ] Notifications work
* [ ] Search works
* [ ] Admin interfaces work
* [ ] External client portal works
* [ ] Visual regression tests pass
* [ ] E2E tests pass
* [ ] Accessibility tests pass
* [ ] Performance tests pass
* [ ] Security tests pass
* [ ] Responsive telemetry is operational

---

## 71. FAANG-Level Acceptance Criteria

SalesGenie responsive architecture SHALL satisfy the following principles:

## A. One Product

```text
One Product
   ↓
Multiple Viewports
   ↓
Adaptive Experiences
```

## B. One Backend Contract

```text
Desktop
Tablet
Mobile
   ↓
Same Domain APIs
```

## C. Backend Authority

```text
Backend
 ├── Identity
 ├── Authorization
 ├── Tenant
 ├── Subscription
 ├── Feature Entitlement
 ├── Data
 └── Business Rules
          ↓
Frontend
```

## D. Responsive Intelligence

The interface SHALL adapt based on:

```text
Viewport
+
Input Method
+
User Role
+
Permissions
+
Tenant
+
Subscription
+
Feature Flags
+
Data Density
+
Network Conditions
```

## E. No Functionality by Device Accident

A feature SHALL not become unavailable merely because the viewport is smaller unless:

1. The feature is genuinely unsuitable for the device.
2. A mobile alternative exists where appropriate.
3. The decision is explicitly documented.
4. Backend authorization remains unchanged.

---

## 72. Final Architecture

```text
                         SALESGENIE
                             │
                             ▼
                  ┌────────────────────┐
                  │ Responsive Web App │
                  └─────────┬──────────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          Desktop         Tablet         Mobile
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                 Responsive Design System
                            │
                 ┌──────────┼──────────┐
                 ▼          ▼          ▼
              Layout     Components   UX State
                 │          │          │
                 └──────────┼──────────┘
                            ▼
                     State Management
                            │
                            ▼
                       API Client
                            │
                            ▼
                       API Gateway
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
       Identity          Business           AI
       Services          Services         Services
          │                 │                 │
          ├─────────────────┼─────────────────┤
          ▼                 ▼                 ▼
       PostgreSQL         Redis          Vector DB
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                     Event / Message Bus
                            │
                            ▼
                     External Services
```

---

## 73. Core Requirement Summary

SalesGenie SHALL implement responsive design as an **adaptive enterprise application architecture**, not merely a collection of CSS media queries.

The responsive system SHALL preserve:

* Identity
* Authorization
* Tenant isolation
* Business workflows
* AI functionality
* Human operations
* Data integrity
* Security
* Accessibility
* Observability
* Performance
* Subscription enforcement
* Feature entitlements
* Real-time state
* Cross-device consistency

The final objective is:

```text
ANY DEVICE
    +
ANY AUTHORIZED USER
    +
ANY SUPPORTED WORKFLOW
    +
ANY SUPPORTED SALES / SUPPORT / AI OPERATION
    +
ANY ORGANIZATION
    +
ANY SUBSCRIPTION TIER
        ↓
CONSISTENT
SECURE
ACCESSIBLE
PERFORMANT
ADAPTIVE
ENTERPRISE-GRADE
SALESGENIE EXPERIENCE
```
