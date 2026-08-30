# SalesGenie iOS Requirements

## 1. Document Purpose

This document defines FAANG-level User Requirements (UR), System Requirements (SR), and Functional Requirements (FR) for the SalesGenie iOS application.

The iOS application is a first-class client of the SalesGenie platform rather than an isolated mobile frontend. Every capability that creates, reads, modifies, executes, or synchronizes business data MUST integrate with the SalesGenie backend APIs, authentication infrastructure, event system, real-time services, AI gateway, notification platform, analytics infrastructure, and security controls.

The application MUST support:

- Enterprise sales operations
- Lead generation and intelligence
- CRM
- Marketing operations
- SEO operations
- Customer support
- AI agents
- AI + human workflows
- Workflow automation
- Product launch intelligence
- Business intelligence
- Advertising intelligence
- Reporting
- Notifications
- Integrations
- Billing visibility
- Organization/workplace/team management
- Enterprise security
- Offline-aware operation
- Real-time synchronization
- Accessibility
- Internationalization and localization

---

## 2. Product Context

SalesGenie is an enterprise multi-tenant AI-powered customer support, sales, marketing, SEO, business intelligence, workflow automation, and AI-agent platform.

The iOS application MUST communicate with backend services through authenticated, versioned APIs and MUST NOT directly access internal databases, private service networks, message queues, or internal microservices.

High-level architecture:

```text
                         iOS APPLICATION
                               |
                    ┌──────────┴──────────┐
                    │                     │
              API CLIENT             REAL-TIME CLIENT
                    │                     │
                    ▼                     ▼
              API GATEWAY           WebSocket/SSE
                    │                     │
        ┌───────────┼─────────────────────┤
        │           │                     │
        ▼           ▼                     ▼
     AUTH       PLATFORM API        NOTIFICATION
        │           │                 SERVICE
        │           │
        │     ┌─────┼───────────────┐
        │     │     │               │
        ▼     ▼     ▼               ▼
      IAM    CRM   AI Gateway     Workflow Engine
              │       │               │
              ▼       ▼               ▼
           Sales    LLMs/RAG       Automation
              │
              ▼
          Analytics
```

---

## 3. Design Principles

The iOS application MUST follow these principles:

1. Backend-authoritative architecture
2. Zero-trust security
3. Multi-tenant isolation
4. Least-privilege access
5. Offline-aware UX
6. Event-driven synchronization
7. API-first integration
8. Secure local storage
9. Accessibility-first design
10. Localization-ready architecture
11. Observable client behavior
12. Graceful degradation
13. Idempotent mutation handling
14. Optimistic UI only where safe
15. Server-side authorization enforcement
16. Explicit AI confidence and approval states
17. Human-in-the-loop support
18. Consistent cross-platform behavior
19. Versioned APIs and backward compatibility
20. Privacy-by-design

---

## 4. Supported User Roles

The iOS application MUST support role-aware experiences for:

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

The frontend MUST NOT assume that every authenticated user has access to every module.

The backend remains the authoritative source for role and permission decisions.

---

## 5. User Requirements

## UR-001 — Secure User Authentication

Users SHALL be able to securely authenticate using supported SalesGenie authentication methods.

The application SHALL support:

* Email/password authentication
* Google OAuth
* MFA
* Biometric unlock where supported
* Session restoration
* Secure logout
* Password recovery
* Account verification
* Session expiration handling
* Token refresh
* Device/session management

---

## UR-002 — Organization Access

Users SHALL be able to access organizations they are authorized to use.

Users SHALL be able to:

* View organizations
* Switch organizations
* View organization status
* View organization metadata
* View their organization role
* View accessible workplaces
* View accessible teams

All organization data MUST be scoped by backend tenant authorization.

---

## UR-003 — Workplace Access

Authorized users SHALL be able to:

* View workplaces
* Switch workplaces
* View workplace members
* View workplace teams
* View workplace settings
* View workplace analytics

---

## UR-004 — Role-Based Experience

Users SHALL receive a personalized application experience based on their roles and permissions.

The application SHALL dynamically determine:

* Navigation visibility
* Screen access
* Action availability
* Data visibility
* Administrative capabilities
* AI capabilities
* Approval capabilities

---

## UR-005 — Sales Management

Sales users SHALL be able to manage sales activities from iOS.

Capabilities SHALL include:

* Leads
* Contacts
* Accounts
* Opportunities
* Deals
* Pipelines
* Tasks
* Activities
* Notes
* Follow-ups
* Sales sequences
* Outreach
* Lead scoring
* Lead qualification
* Lead routing
* Lead assignment
* Sales analytics

---

## UR-006 — Lead Intelligence

Users SHALL be able to discover and analyze leads using SalesGenie's AI-powered lead intelligence capabilities.

Users SHALL be able to:

* Search prospects
* Search companies
* View company intelligence
* View person intelligence
* View buying signals
* View intent signals
* View lead score
* View qualification status
* View enrichment data
* View verification status
* View recommended prospects

---

## UR-007 — AI Lead Generation

Authorized users SHALL be able to request AI-powered lead generation.

Users SHALL be able to specify:

* ICP
* Industry
* Geography
* Company size
* Revenue range
* Job title
* Technology stack
* Intent signals
* Buying signals
* Other qualification criteria

The backend SHALL execute the generation workflow.

The iOS client SHALL display:

* Job status
* Progress
* Generated leads
* Confidence
* Data sources
* Errors
* Completion status

---

## UR-008 — CRM Management

Users SHALL be able to manage CRM entities from iOS.

Supported entities SHALL include:

* Contacts
* Accounts
* Leads
* Opportunities
* Deals
* Activities
* Notes
* Tasks
* Pipelines

---

## UR-009 — Marketing Management

Authorized marketing users SHALL be able to:

* View campaigns
* Create campaigns
* Edit campaigns
* Schedule campaigns
* Monitor campaigns
* View audiences
* View campaign performance
* Review AI recommendations
* Approve AI-generated content
* Monitor marketing ROI

---

## UR-010 — SEO Management

Authorized SEO users SHALL be able to:

* View SEO projects
* View keyword research
* View rankings
* View SERP data
* View technical SEO issues
* View content gaps
* View competitor SEO analysis
* Review AI SEO recommendations
* Monitor SEO performance

---

## UR-011 — Customer Support

Support users SHALL be able to:

* View tickets
* Create tickets
* Assign tickets
* Update tickets
* Reply to customers
* Escalate conversations
* Transfer conversations
* View SLA status
* View customer history
* View sentiment
* View AI recommendations

---

## UR-012 — Omnichannel Communication

Users SHALL be able to access authorized communication channels including:

* Web chat
* Email
* WhatsApp
* Facebook Messenger
* Instagram messaging
* Telegram
* SMS
* Voice-related interactions where supported

The backend SHALL normalize communication events.

---

## UR-013 — AI Agent Management

Authorized users SHALL be able to:

* View AI agents
* Create agents
* Configure agents
* Activate agents
* Deactivate agents
* Monitor agents
* View agent executions
* Review agent decisions
* Review agent errors
* Approve agent actions
* Perform human handoff

---

## UR-014 — AI + Human Collaboration

Users SHALL be able to participate in human-in-the-loop workflows.

The application SHALL support:

```text
AI Decision
     |
     ▼
Confidence Evaluation
     |
 ┌───┼────────┐
 ▼   ▼        ▼
High Medium   Low
 │     │       │
AI    Review  Human
 │     │       │
 └─────┼───────┘
       ▼
    Outcome
```

Users SHALL be able to:

* Approve AI decisions
* Reject AI decisions
* Modify AI output
* Escalate AI actions
* Assign work to humans
* Return work to AI
* Add review notes

---

## UR-015 — Workflow Automation

Authorized users SHALL be able to:

* View workflows
* Create workflows
* Trigger workflows
* Pause workflows
* Resume workflows
* Inspect execution history
* Retry failed executions
* View workflow logs
* Approve workflow actions

---

## UR-016 — Product Launch Intelligence

Product and business users SHALL be able to:

* Create product analysis requests
* View market analysis
* View competitor analysis
* View market trends
* View market gaps
* View opportunities
* View launch risks
* View AI recommendations
* View go-to-market recommendations

---

## UR-017 — Business Intelligence

Authorized users SHALL be able to view:

* Revenue
* Expenses
* Profit
* Loss
* Growth
* Product profitability
* Customer metrics
* Sales metrics
* Marketing metrics
* Advertising metrics
* Business health score
* AI business recommendations

---

## UR-018 — Advertising Intelligence

Authorized users SHALL be able to view advertising data from supported platforms.

The application SHALL support backend-integrated views for:

* Google Ads
* Facebook Ads
* Instagram Ads
* WhatsApp Ads
* YouTube Ads
* TikTok Ads
* LinkedIn Ads

Metrics SHALL include:

* Spend
* Revenue
* ROAS
* ROI
* CTR
* CPC
* CPM
* Conversions
* Conversion rate
* Reach
* Impressions
* Audience demographics

---

## UR-019 — Reports

Users SHALL be able to:

* View reports
* Generate reports
* Schedule reports
* Export reports
* Download reports
* Share authorized reports

Supported formats:

* XLSX
* CSV
* PDF
* JSON

---

## UR-020 — Notifications

Users SHALL receive relevant:

* Push notifications
* In-app notifications
* Security alerts
* Workflow alerts
* AI approval requests
* Support notifications
* Sales notifications
* Billing notifications
* Incident notifications

Users SHALL be able to configure notification preferences.

---

## UR-021 — Real-Time Updates

Users SHALL receive real-time updates for:

* Conversations
* Tickets
* AI agent execution
* Workflow execution
* Lead generation
* Notifications
* Assignment changes
* Collaboration events
* System incidents where authorized

---

## UR-022 — Offline Awareness

Users SHALL be able to continue using safe read-oriented functionality during temporary network loss.

The application SHALL:

* Cache permitted data
* Display offline state
* Queue safe mutations
* Retry operations
* Detect conflicts
* Synchronize when connectivity returns

---

## UR-023 — Search

Users SHALL be able to search authorized SalesGenie data globally.

Search SHALL support:

* Leads
* Contacts
* Companies
* Tickets
* Conversations
* Opportunities
* Deals
* Agents
* Workflows
* Reports
* Documents
* Knowledge resources

---

## UR-024 — Accessibility

Users SHALL be able to use SalesGenie through iOS accessibility technologies including:

* VoiceOver
* Dynamic Type
* Reduce Motion
* Switch Control
* Voice Control
* High-contrast configurations where applicable

---

## UR-025 — Localization

Users SHALL be able to select supported languages.

The application SHALL support:

* Localized UI strings
* Date formatting
* Number formatting
* Currency formatting
* Time zones
* Right-to-left layouts where required
* Localized notifications
* Localized AI content where supported

---

## 6. System Requirements

## SR-001 — iOS Platform

The application SHALL be implemented as a native iOS application using Apple's supported development ecosystem.

The architecture SHOULD use:

* Swift
* SwiftUI
* Swift Concurrency
* URLSession
* Keychain Services
* UserNotifications
* LocalAuthentication
* Network framework
* BackgroundTasks
* App Intents where applicable

---

## SR-002 — Backend-First Architecture

The iOS application MUST NOT directly access:

* PostgreSQL
* Redis
* Object storage internals
* Message queues
* Event buses
* Internal microservices
* Internal service databases

All business operations MUST pass through authorized backend interfaces.

---

## SR-003 — API Gateway

All external API communication SHOULD use the SalesGenie API Gateway.

```text
iOS
 |
 ▼
API Gateway
 |
 ├── Authentication
 ├── Authorization
 ├── Rate Limiting
 ├── Request Validation
 ├── Tenant Isolation
 ├── Routing
 ├── Observability
 └── Security
```

---

## SR-004 — API Versioning

The client SHALL support versioned APIs.

Example:

```text
/api/v1/*
/api/v2/*
```

The application SHALL avoid hard-coding assumptions about unversioned APIs.

---

## SR-005 — Authentication Tokens

Authentication tokens SHALL be handled securely.

Requirements:

* Access tokens MUST NOT be stored in insecure plaintext storage.
* Refresh tokens MUST be protected.
* Tokens SHOULD be stored in Keychain.
* Tokens MUST NOT be logged.
* Tokens MUST NOT appear in analytics.
* Tokens MUST NOT appear in crash reports.
* Expired credentials MUST trigger controlled refresh or reauthentication.

---

## SR-006 — Authorization

The backend MUST enforce authorization.

The frontend SHALL use permissions to optimize UX but MUST NOT treat frontend permission checks as security controls.

---

## SR-007 — Multi-Tenant Isolation

Every backend request MUST carry sufficient tenant context.

The application SHALL support:

* Organization ID
* Workplace ID
* User ID
* Role context
* Permission context
* Session/device context

The backend MUST validate all tenant boundaries.

---

## SR-008 — Network Layer

The network layer SHALL provide:

* Request construction
* Authentication
* Token refresh
* Retry
* Timeout
* Cancellation
* Error decoding
* Request correlation IDs
* API versioning
* Network monitoring
* Response validation

---

## SR-009 — API Error Model

The application SHALL normalize backend errors.

Minimum categories:

```text
AuthenticationError
AuthorizationError
ValidationError
NotFoundError
ConflictError
RateLimitError
NetworkError
TimeoutError
ServerError
ServiceUnavailableError
UnknownError
```

---

## SR-010 — Idempotency

Mutation requests that may be retried SHALL support idempotency.

Examples:

* Creating leads
* Sending messages
* Creating tickets
* Starting workflows
* Generating reports
* Executing AI actions
* Triggering campaigns

---

## SR-011 — Request Correlation

Every API request SHOULD support:

* Request ID
* Correlation ID
* Trace ID
* Client version
* Device/session metadata

Sensitive information MUST NOT be included unnecessarily.

---

## SR-012 — Real-Time Transport

The application SHALL support backend-provided real-time communication.

Supported mechanisms MAY include:

* WebSocket
* Server-Sent Events
* Push notifications
* Polling fallback

The client SHALL automatically recover from interrupted real-time connections.

---

## SR-013 — Push Notification Infrastructure

Push notifications SHALL use Apple's notification infrastructure and SalesGenie's notification backend.

The backend SHALL determine:

* Recipient
* Notification type
* Priority
* Payload
* Localization
* Authorization
* Delivery policy

---

## SR-014 — Background Processing

Background execution SHALL be used only for supported iOS use cases.

Potential operations:

* Data refresh
* Synchronization
* Upload completion
* Notification processing
* Offline queue processing
* Report downloads

The application MUST respect iOS background execution constraints.

---

## SR-015 — Local Data Storage

The application MAY use local persistence for:

* Cached API responses
* User preferences
* Offline queues
* Drafts
* Search history
* UI state

Sensitive data MUST be encrypted/protected appropriately.

---

## SR-016 — Offline Synchronization

The synchronization system SHALL support:

```text
Local State
    |
    ▼
Mutation Queue
    |
    ▼
Connectivity Detection
    |
    ▼
Backend Sync
    |
    ├── Success
    ├── Conflict
    ├── Retry
    └── Failure
```

---

## SR-017 — Conflict Resolution

The client SHALL handle server-side conflicts.

Conflict strategies MAY include:

* Server wins
* Client wins where explicitly allowed
* Last-write-wins
* Version-based conflict detection
* Manual resolution

Business-critical entities SHOULD use server-authoritative conflict resolution.

---

## SR-018 — Secure Networking

The application SHALL enforce:

* HTTPS
* TLS
* Certificate validation
* Secure redirects
* Secure cookies where applicable
* No plaintext production API traffic

Certificate pinning MAY be considered for high-risk environments but MUST include operational rotation planning.

---

## SR-019 — Privacy

The application SHALL minimize collection of personal information.

Sensitive data SHALL NOT be unnecessarily:

* Logged
* Cached
* Sent to analytics
* Included in crash reports
* Included in notification payloads

---

## SR-020 — Analytics

The client SHALL emit product analytics events through the backend-approved analytics architecture.

Events SHALL include controlled metadata such as:

* Screen viewed
* Feature used
* Workflow action
* AI interaction
* Error occurrence
* Performance metric

PII and secrets MUST be excluded unless explicitly approved.

---

## SR-021 — Crash Monitoring

The application SHALL integrate with an approved crash monitoring system.

Crash reports SHOULD contain:

* App version
* OS version
* Device class
* Screen/module
* Non-sensitive request context
* Correlation ID where safe

---

## SR-022 — Performance Monitoring

The application SHALL measure:

* App startup
* Screen rendering
* API latency
* Network failure rate
* Real-time connection health
* Memory pressure
* Battery-impacting operations
* AI response latency

---

## SR-023 — Feature Flags

Backend-controlled feature flags SHALL support:

* Feature rollout
* Role-based rollout
* Organization rollout
* Workplace rollout
* Percentage rollout
* Emergency disablement
* Experimental AI features

---

## SR-024 — Remote Configuration

The application SHALL support controlled backend configuration for:

* API endpoints
* Feature availability
* UI behavior
* Experiment configuration
* Minimum supported version
* Maintenance mode
* Notification behavior

Secrets MUST NOT be delivered through remote configuration.

---

## SR-025 — App Version Enforcement

The backend SHALL be able to communicate:

* Current minimum version
* Recommended version
* Mandatory upgrade requirement
* Deprecated version status

The application SHALL provide controlled upgrade experiences.

---

## 7. Functional Requirements

## 7.1 Authentication

## FR-AUTH-001 — Login

The system SHALL allow users to authenticate through the SalesGenie authentication API.

## FR-AUTH-002 — OAuth

The system SHALL support Google OAuth where enabled for the tenant.

## FR-AUTH-003 — MFA

The system SHALL support MFA challenges.

## FR-AUTH-004 — Biometric Authentication

The application SHALL support Face ID/Touch ID as a local unlock mechanism where available.

Biometrics SHALL NOT replace backend authorization.

## FR-AUTH-005 — Token Refresh

The application SHALL refresh expired access tokens using the authorized refresh mechanism.

## FR-AUTH-006 — Logout

Logout SHALL invalidate or revoke the appropriate backend session/token where supported.

## FR-AUTH-007 — Session Revocation

The application SHALL detect backend session revocation and force appropriate reauthentication.

---

## 7.2 Organization

## FR-ORG-001 — Organization List

The application SHALL retrieve authorized organizations from the backend.

## FR-ORG-002 — Organization Switching

Users SHALL be able to switch between authorized organizations.

## FR-ORG-003 — Organization Context

Every organization-scoped API request SHALL use the currently selected organization context.

## FR-ORG-004 — Organization Settings

Authorized administrators SHALL be able to view and modify supported organization settings.

---

## 7.3 Workplace

## FR-WORK-001 — Workplace List

The application SHALL retrieve authorized workplaces.

## FR-WORK-002 — Workplace Switching

Users SHALL be able to switch workplaces.

## FR-WORK-003 — Workplace Membership

Authorized administrators SHALL be able to manage workplace membership.

---

## 7.4 User Management

## FR-USER-001 — User List

Authorized administrators SHALL be able to retrieve users.

## FR-USER-002 — User Profile

Users SHALL be able to retrieve and update permitted profile fields.

## FR-USER-003 — Role Display

The application SHALL display backend-authorized roles.

## FR-USER-004 — User Status

Administrators SHALL be able to view user status where authorized.

---

## 7.5 Lead Management

## FR-LEAD-001 — Lead List

The application SHALL retrieve paginated leads.

## FR-LEAD-002 — Lead Search

Users SHALL be able to search leads.

## FR-LEAD-003 — Lead Filtering

The application SHALL support server-side filtering.

Filters MAY include:

* Score
* Status
* Industry
* Geography
* Source
* Owner
* Intent
* Buying signal
* Company size
* Revenue

## FR-LEAD-004 — Lead Creation

Authorized users SHALL be able to create leads.

## FR-LEAD-005 — Lead Update

Authorized users SHALL be able to update leads.

## FR-LEAD-006 — Lead Assignment

Authorized users SHALL be able to assign leads.

## FR-LEAD-007 — Lead Scoring

The application SHALL retrieve AI-generated lead scores from the backend.

## FR-LEAD-008 — Lead Enrichment

Users SHALL be able to request lead enrichment where authorized.

## FR-LEAD-009 — Lead Verification

Users SHALL be able to request verification where supported.

## FR-LEAD-010 — Lead Deduplication

The application SHALL display backend-generated duplicate warnings.

---

## 7.6 Lead Generation

## FR-LGEN-001 — Lead Generation Request

Users SHALL be able to submit AI lead generation requests.

## FR-LGEN-002 — Generation Job Tracking

The application SHALL track asynchronous generation jobs.

## FR-LGEN-003 — Generation Progress

The application SHALL display progress when supported by backend events.

## FR-LGEN-004 — Generated Lead Review

Users SHALL be able to review generated leads before committing them to CRM.

## FR-LGEN-005 — Human Approval

The application SHALL support human approval before high-impact lead operations.

---

## 7.7 CRM

## FR-CRM-001 — Contact Management

Users SHALL be able to retrieve, create, update, and search contacts where authorized.

## FR-CRM-002 — Account Management

Users SHALL be able to manage accounts.

## FR-CRM-003 — Opportunity Management

Users SHALL be able to manage opportunities.

## FR-CRM-004 — Deal Management

Users SHALL be able to manage deals.

## FR-CRM-005 — Pipeline Management

Authorized users SHALL be able to view pipelines and stages.

## FR-CRM-006 — Activity Management

Users SHALL be able to manage activities.

---

## 7.8 Sales Automation

## FR-SALES-001 — Sales Sequences

Users SHALL be able to view and manage authorized sequences.

## FR-SALES-002 — Outreach

Users SHALL be able to initiate authorized outreach workflows.

## FR-SALES-003 — Follow-Up

The application SHALL display and manage follow-up tasks.

## FR-SALES-004 — Sales Recommendations

The application SHALL retrieve AI sales recommendations.

---

## 7.9 Marketing

## FR-MKT-001 — Campaign List

The application SHALL retrieve marketing campaigns.

## FR-MKT-002 — Campaign Creation

Authorized users SHALL be able to create campaigns.

## FR-MKT-003 — Campaign Scheduling

Authorized users SHALL be able to schedule campaigns.

## FR-MKT-004 — Campaign Analytics

The application SHALL retrieve campaign performance metrics.

## FR-MKT-005 — AI Content Approval

Users SHALL be able to approve, reject, or modify AI-generated marketing content.

---

## 7.10 SEO

## FR-SEO-001 — SEO Projects

Users SHALL be able to retrieve SEO projects.

## FR-SEO-002 — Keyword Data

The application SHALL retrieve keyword intelligence.

## FR-SEO-003 — Ranking Data

Users SHALL be able to view ranking data.

## FR-SEO-004 — SEO Audit

Authorized users SHALL be able to initiate SEO audits.

## FR-SEO-005 — AI SEO Recommendations

The application SHALL retrieve AI recommendations.

---

## 7.11 Support

## FR-SUP-001 — Ticket List

Support users SHALL be able to retrieve tickets.

## FR-SUP-002 — Ticket Creation

Authorized users SHALL be able to create tickets.

## FR-SUP-003 — Ticket Assignment

Authorized users SHALL be able to assign tickets.

## FR-SUP-004 — Ticket Update

Users SHALL be able to update authorized ticket fields.

## FR-SUP-005 — Conversation Reply

Authorized users SHALL be able to respond to conversations.

## FR-SUP-006 — Escalation

Users SHALL be able to escalate conversations.

## FR-SUP-007 — AI Support Recommendation

The application SHALL display AI-generated support recommendations.

---

## 7.12 Omnichannel

## FR-OMNI-001 — Unified Inbox

The application SHALL display authorized conversations in a unified inbox.

## FR-OMNI-002 — Channel Identification

Every conversation SHALL display its originating channel.

## FR-OMNI-003 — Message Sending

Messages SHALL be submitted through the backend communication API.

## FR-OMNI-004 — Delivery State

The application SHALL display:

* Sending
* Sent
* Delivered
* Failed
* Read

where supported.

## FR-OMNI-005 — Real-Time Messages

New messages SHALL be received through the real-time communication layer.

---

## 7.13 AI Agents

## FR-AGENT-001 — Agent List

Authorized users SHALL be able to retrieve agents.

## FR-AGENT-002 — Agent Details

The application SHALL display:

* Agent status
* Version
* Capabilities
* Tools
* Permissions
* Model
* Knowledge sources
* Recent executions

## FR-AGENT-003 — Agent Execution

Authorized users SHALL be able to trigger supported agent executions.

## FR-AGENT-004 — Execution Status

The application SHALL display:

* Queued
* Running
* Waiting
* Completed
* Failed
* Cancelled

## FR-AGENT-005 — Agent Approval

Users SHALL be able to approve agent actions requiring human approval.

## FR-AGENT-006 — Human Handoff

Users SHALL be able to take over AI-managed interactions.

---

## 7.14 AI Model Infrastructure

## FR-LLM-001 — Model Visibility

Authorized users SHALL be able to view permitted model information.

## FR-LLM-002 — Provider Visibility

The application MAY display configured providers such as:

* Grok
* Gemini
* Mistral
* Other configured providers

## FR-LLM-003 — AI Usage

Authorized users SHALL be able to view AI usage.

## FR-LLM-004 — AI Cost

Authorized users SHALL be able to view AI cost information.

## FR-LLM-005 — Model Errors

The application SHALL display model/service errors without exposing provider secrets.

---

## 7.15 RAG / Knowledge

## FR-RAG-001 — Knowledge Bases

Users SHALL be able to view authorized knowledge bases.

## FR-RAG-002 — Documents

Users SHALL be able to browse authorized documents.

## FR-RAG-003 — Search

Users SHALL be able to perform semantic/hybrid knowledge searches.

## FR-RAG-004 — Retrieval Results

The application SHALL display AI retrieval results and citations where available.

## FR-RAG-005 — Knowledge Permissions

The frontend SHALL respect backend-provided document permissions.

---

## 7.16 Workflow Automation

## FR-WF-001 — Workflow List

Users SHALL be able to retrieve workflows.

## FR-WF-002 — Workflow Execution

Authorized users SHALL be able to start workflows.

## FR-WF-003 — Workflow Monitoring

Users SHALL be able to monitor executions.

## FR-WF-004 — Workflow Retry

Authorized users SHALL be able to retry failed executions.

## FR-WF-005 — Workflow Cancellation

Authorized users SHALL be able to cancel supported executions.

---

## 7.17 Product Launch Intelligence

## FR-PLI-001 — Product Creation

Authorized users SHALL be able to create product intelligence projects.

## FR-PLI-002 — Market Analysis

Users SHALL be able to retrieve market analysis.

## FR-PLI-003 — Competitor Analysis

Users SHALL be able to retrieve competitor intelligence.

## FR-PLI-004 — Risk Analysis

Users SHALL be able to retrieve launch risks.

## FR-PLI-005 — AI Recommendations

Users SHALL be able to retrieve AI-generated launch recommendations.

---

## 7.18 Business Intelligence

## FR-BI-001 — Executive Dashboard

Authorized users SHALL be able to view executive metrics.

## FR-BI-002 — Revenue

The application SHALL retrieve revenue metrics.

## FR-BI-003 — Profit/Loss

The application SHALL retrieve profit/loss analytics.

## FR-BI-004 — Product Profitability

The application SHALL display profitable and loss-making products.

## FR-BI-005 — Growth

The application SHALL display:

* Monthly growth
* Yearly growth
* Revenue growth
* Customer growth
* Sales growth

## FR-BI-006 — AI Business Advisor

Authorized users SHALL be able to retrieve AI business recommendations.

---

## 7.19 Advertising

## FR-ADS-001 — Advertising Accounts

Users SHALL be able to view connected advertising accounts where authorized.

## FR-ADS-002 — Campaign Metrics

The application SHALL retrieve campaign metrics.

## FR-ADS-003 — Spend

The application SHALL display advertising spend.

## FR-ADS-004 — ROI/ROAS

The application SHALL display ROI and ROAS.

## FR-ADS-005 — Audience Analytics

The application SHALL display authorized audience and demographic analytics.

## FR-ADS-006 — AI Optimization

Authorized users SHALL be able to retrieve AI advertising recommendations.

---

## 7.20 Reporting

## FR-REPORT-001 — Report List

Users SHALL be able to retrieve reports.

## FR-REPORT-002 — Report Generation

Authorized users SHALL be able to generate reports.

## FR-REPORT-003 — Report Status

The application SHALL display asynchronous report generation status.

## FR-REPORT-004 — Report Download

The application SHALL securely download completed reports.

## FR-REPORT-005 — Report Scheduling

Authorized users SHALL be able to manage scheduled reports.

---

## 7.21 Notifications

## FR-NOTIF-001 — Notification Registration

The application SHALL register the device push token with the backend.

## FR-NOTIF-002 — Notification List

Users SHALL be able to view in-app notifications.

## FR-NOTIF-003 — Read State

Users SHALL be able to mark notifications as read.

## FR-NOTIF-004 — Notification Preferences

Users SHALL be able to configure notification preferences.

## FR-NOTIF-005 — Deep Linking

Supported notifications SHALL deep-link to the relevant application resource.

---

## 7.22 Search

## FR-SEARCH-001 — Global Search

Users SHALL be able to search across authorized resources.

## FR-SEARCH-002 — Search Suggestions

The application SHALL retrieve backend-generated suggestions.

## FR-SEARCH-003 — Search Filtering

Users SHALL be able to filter results by entity type.

## FR-SEARCH-004 — Permission-Aware Results

The backend SHALL return only authorized results.

---

## 7.23 Integrations

## FR-INT-001 — Integration List

Authorized users SHALL be able to view configured integrations.

## FR-INT-002 — OAuth Integration

The application SHALL initiate supported OAuth flows.

## FR-INT-003 — Integration Status

The application SHALL display:

* Connected
* Disconnected
* Expired
* Error
* Reauthorization required

## FR-INT-004 — Integration Synchronization

Users SHALL be able to view synchronization status.

## FR-INT-005 — Integration Errors

Users SHALL be able to inspect authorized integration errors.

---

## 7.24 Billing

## FR-BILL-001 — Subscription

Authorized users SHALL be able to view subscription information.

## FR-BILL-002 — Usage

Users SHALL be able to view usage against plan limits.

## FR-BILL-003 — Billing Status

Authorized users SHALL be able to view billing status.

## FR-BILL-004 — Invoice Access

Authorized users SHALL be able to view and download invoices.

Sensitive payment information SHALL NOT be stored directly in the iOS application.

---

## 7.25 Administrative Functions

Administrative capabilities SHALL be dynamically enabled according to permissions.

Potential administrative functions:

* User management
* Role management
* Permission management
* Organization management
* Workplace management
* Feature flags
* Audit logs
* Platform monitoring
* Incident management
* Security monitoring
* Billing administration

High-risk administrative mutations SHOULD require additional confirmation.

---

## 7.26 Audit Logging

## FR-AUDIT-001 — Audit Events

Security-sensitive operations SHALL generate backend audit events.

Examples:

* Login
* Logout
* Role changes
* Permission changes
* User suspension
* API key creation
* Integration changes
* AI approval
* Data export
* Billing changes
* Administrative changes

The client SHALL never be the sole authority for audit logging.

---

## 7.27 AI Safety

## FR-AI-SAFE-001 — AI Confidence

Where provided by backend services, the application SHALL display AI confidence.

## FR-AI-SAFE-002 — AI Approval

High-impact AI operations SHALL support approval workflows.

## FR-AI-SAFE-003 — AI Explainability

Where supported, the application SHALL expose:

* Reasoning summary
* Evidence
* Sources
* Confidence
* Recommended action

The application MUST NOT fabricate explanations when backend evidence is unavailable.

## FR-AI-SAFE-004 — AI Failure

AI failures SHALL produce actionable error states.

---

## 7.28 Security

## FR-SEC-001 — Secure Storage

Sensitive credentials SHALL use iOS Keychain or equivalent secure storage.

## FR-SEC-002 — Screen Privacy

Sensitive screens SHOULD support appropriate privacy behavior.

## FR-SEC-003 — Screenshot Protection

The application SHOULD evaluate platform-appropriate protection for highly sensitive information.

## FR-SEC-004 — Jailbreak/Risk Signals

The application MAY detect security-risk signals and communicate them to backend security systems where legally and technically appropriate.

## FR-SEC-005 — Session Security

The application SHALL respond to backend security events such as:

* Session revocation
* Account suspension
* MFA requirement
* Password reset requirement
* Security incident

---

## 7.29 Accessibility

## FR-ACCESS-001 — VoiceOver

All interactive controls SHALL expose meaningful accessibility labels.

## FR-ACCESS-002 — Dynamic Type

Text SHALL support Dynamic Type where practical.

## FR-ACCESS-003 — Focus Order

VoiceOver navigation SHALL follow logical information hierarchy.

## FR-ACCESS-004 — Accessible Charts

Charts SHALL expose meaningful textual summaries.

## FR-ACCESS-005 — Accessible Errors

Errors SHALL be announced accessibly.

---

## 7.30 Localization

## FR-I18N-001 — Localized Strings

All user-facing strings SHALL be externalized.

## FR-I18N-002 — Backend Language Preference

The application SHALL synchronize language preference with the user's backend profile where supported.

## FR-I18N-003 — Date/Time

Dates and times SHALL use the user's configured locale and time zone.

## FR-I18N-004 — Currency

Financial metrics SHALL use backend-provided currency metadata.

## FR-I18N-005 — RTL

The application SHALL support RTL layout where required.

---

## 7.31 Offline

## FR-OFF-001 — Connectivity Detection

The application SHALL detect network availability.

## FR-OFF-002 — Offline Banner

The application SHALL clearly indicate offline status.

## FR-OFF-003 — Cached Data

Authorized cached data SHALL remain available where safe.

## FR-OFF-004 — Mutation Queue

Supported mutations SHALL be queued when offline.

## FR-OFF-005 — Retry

Queued operations SHALL retry when connectivity returns.

## FR-OFF-006 — Conflict

The application SHALL display conflicts requiring user intervention.

---

## 7.32 Deep Linking

## FR-DEEP-001 — Resource Deep Links

The application SHALL support links to resources such as:

```text
salesgenie://lead/{id}
salesgenie://contact/{id}
salesgenie://ticket/{id}
salesgenie://conversation/{id}
salesgenie://agent/{id}
salesgenie://workflow/{id}
salesgenie://report/{id}
```

Universal Links SHOULD be supported for production web-to-app navigation.

---

## 7.33 Navigation

The application SHALL provide role-aware navigation.

Example:

```text
Home
├── Sales
│   ├── Leads
│   ├── Contacts
│   ├── Accounts
│   ├── Opportunities
│   └── Pipeline
│
├── Marketing
│   ├── Campaigns
│   ├── Audiences
│   └── Analytics
│
├── SEO
│   ├── Projects
│   ├── Keywords
│   └── Rankings
│
├── Support
│   ├── Inbox
│   ├── Tickets
│   └── Customers
│
├── AI
│   ├── Agents
│   ├── Executions
│   └── Approvals
│
├── Automation
│   ├── Workflows
│   └── Executions
│
├── Analytics
│   ├── Business
│   ├── Sales
│   ├── Marketing
│   └── Advertising
│
└── Settings
    ├── Account
    ├── Organization
    ├── Integrations
    ├── Notifications
    └── Security
```

Navigation visibility SHALL be permission-driven.

---

## 8. Backend Integration Matrix

| iOS Capability        | Backend Dependency        | Real-Time | Auth Required | Tenant Scoped |
| --------------------- | ------------------------- | --------: | ------------: | ------------: |
| Login                 | Auth Service              |        No |            No |           Yes |
| MFA                   | Auth Service              |  Optional |           Yes |           Yes |
| Organizations         | Organization Service      |  Optional |           Yes |           Yes |
| Users                 | Identity Service          |  Optional |           Yes |           Yes |
| Leads                 | Lead Intelligence Service |       Yes |           Yes |           Yes |
| Lead Generation       | AI/Lead Generation Engine |       Yes |           Yes |           Yes |
| CRM                   | CRM Service               |  Optional |           Yes |           Yes |
| Marketing             | Marketing Service         |       Yes |           Yes |           Yes |
| SEO                   | SEO Service               |       Yes |           Yes |           Yes |
| Support               | Support Service           |       Yes |           Yes |           Yes |
| Omnichannel           | Communication Service     |       Yes |           Yes |           Yes |
| AI Agents             | Agent Platform            |       Yes |           Yes |           Yes |
| RAG                   | Knowledge/RAG Service     |  Optional |           Yes |           Yes |
| Workflows             | Workflow Engine           |       Yes |           Yes |           Yes |
| Product Launch        | Intelligence Service      |       Yes |           Yes |           Yes |
| Business Intelligence | Analytics Service         |  Optional |           Yes |           Yes |
| Advertising           | Advertising Services      |  Optional |           Yes |           Yes |
| Reports               | Reporting Service         |       Yes |           Yes |           Yes |
| Notifications         | Notification Service      |       Yes |           Yes |           Yes |
| Search                | Search Service            |  Optional |           Yes |           Yes |
| Integrations          | Integration Service       |       Yes |           Yes |           Yes |
| Billing               | Billing Service           |  Optional |           Yes |           Yes |
| Audit                 | Audit Service             |       Yes |           Yes |           Yes |
| Feature Flags         | Configuration Service     |  Optional |           Yes |           Yes |

---

## 9. API Requirements

The API client SHALL support:

```text
GET
POST
PUT
PATCH
DELETE
```

where applicable.

Every API response SHOULD follow a normalized structure.

Example:

```json
{
  "success": true,
  "data": {},
  "meta": {
    "request_id": "..."
  },
  "errors": []
}
```

Pagination SHOULD support cursor-based pagination for large datasets.

Example:

```json
{
  "data": [],
  "pagination": {
    "next_cursor": "...",
    "has_more": true
  }
}
```

---

## 10. Real-Time Event Requirements

The iOS client SHOULD subscribe to backend events such as:

```text
lead.created
lead.updated
lead.scored

conversation.created
conversation.message.created
conversation.updated

ticket.created
ticket.updated
ticket.assigned

agent.execution.started
agent.execution.completed
agent.execution.failed
agent.approval.required

workflow.execution.started
workflow.execution.completed
workflow.execution.failed

notification.created

report.generated

integration.sync.started
integration.sync.completed
integration.sync.failed

security.session.revoked
security.account.suspended
```

Events MUST be tenant-authorized before reaching the client.

---

## 11. State Management Requirements

The iOS application SHALL maintain distinct state categories:

```text
App State
├── Authentication State
├── User State
├── Organization State
├── Workplace State
├── Permission State
├── Feature Flag State
├── Network State
├── Notification State
├── Navigation State
├── Domain State
├── AI State
├── Workflow State
└── Offline Sync State
```

Server state SHALL remain server-authoritative.

---

## 12. Caching Requirements

The application SHALL implement controlled caching.

Cache categories:

```text
Public/Low Risk
    └── Standard cache

User Preferences
    └── Local persistence

Business Data
    └── Secure cache

Sensitive Data
    └── Minimal/no persistence

Credentials
    └── Keychain only
```

Cache invalidation SHALL be driven by:

* TTL
* Backend events
* Explicit refresh
* Version changes
* Authentication changes
* Organization switching

---

## 13. Pagination Requirements

Large collections SHALL use pagination.

Required for:

* Leads
* Contacts
* Accounts
* Opportunities
* Tickets
* Conversations
* Messages
* Notifications
* Users
* Audit logs
* Reports
* Agent executions
* Workflow executions

The application SHALL avoid loading unbounded datasets into memory.

---

## 14. Search Requirements

Search SHALL preferably execute server-side.

The client SHALL support:

* Debouncing
* Pagination
* Filters
* Sorting
* Search history
* Empty states
* Loading states
* Error states
* Permission-aware results

---

## 15. File and Media Requirements

The application SHALL support backend-authorized:

* File upload
* File download
* Document preview
* Image upload
* Image preview
* Report download
* Attachment upload

Large files SHOULD use pre-signed upload/download mechanisms where appropriate.

The iOS application MUST NOT expose object-storage credentials.

---

## 16. Security Requirements

The application SHALL protect:

* Authentication credentials
* Access tokens
* Refresh tokens
* User data
* Organization data
* Customer information
* Business analytics
* AI prompts
* AI outputs
* Documents
* Integration credentials
* Billing data

The application SHALL implement:

* Secure storage
* TLS
* Authorization
* Session management
* Secure logging
* Privacy controls
* Data minimization
* Secure networking
* Dependency security

---

## 17. Performance Requirements

The application SHOULD target:

* Fast cold launch
* Fast warm launch
* Smooth scrolling
* Efficient image loading
* Efficient pagination
* Low memory usage
* Minimal unnecessary network requests
* Efficient background work
* Responsive interaction during AI processing

Long-running operations SHALL be asynchronous.

---

## 18. Reliability Requirements

The application SHALL gracefully handle:

* No network
* Slow network
* Backend timeout
* Authentication expiration
* API errors
* Service degradation
* Partial failures
* Real-time disconnection
* Push notification failure
* Background execution interruption

The UI SHALL never become permanently blocked because of a failed backend request.

---

## 19. Error Handling Requirements

Every backend operation SHALL support:

```text
Idle
Loading
Success
Empty
Error
Retrying
Offline
Unauthorized
Forbidden
Conflict
```

Errors SHALL provide actionable user feedback without exposing:

* Stack traces
* Internal service names
* Database errors
* Secrets
* Internal infrastructure details

---

## 20. AI UX Requirements

AI-powered interfaces SHALL clearly distinguish:

```text
AI Generated
AI Suggested
Human Approved
Human Modified
System Generated
```

AI outputs SHALL display backend-provided:

* Confidence
* Sources
* Evidence
* Timestamp
* Model information where appropriate
* Approval status

---

## 21. Human Approval Requirements

High-impact AI actions SHALL support:

```text
Pending Approval
      |
      ├── Approve
      ├── Reject
      ├── Edit
      └── Escalate
```

Examples:

* Sending customer messages
* Sending marketing campaigns
* Assigning high-value leads
* Executing external actions
* Changing business configuration
* AI-generated financial recommendations
* Product launch decisions

---

## 22. Notification Deep-Link Architecture

Notification flow:

```text
Backend Event
     |
     ▼
Notification Service
     |
     ▼
APNs
     |
     ▼
iOS
     |
     ▼
Deep Link
     |
     ▼
Authenticated Screen
     |
     ▼
Backend Resource
```

The application MUST revalidate authorization after a deep link is opened.

---

## 23. Background Synchronization

Background synchronization SHALL prioritize:

1. Security events
2. Critical notifications
3. User-generated pending mutations
4. Support conversations
5. Sales activities
6. AI approvals
7. Workflow status
8. Analytics refresh

The application SHALL not perform unnecessary background synchronization.

---

## 24. Accessibility Requirements

The application SHALL conform to appropriate WCAG-aligned accessibility principles and Apple's accessibility APIs.

Requirements include:

* VoiceOver support
* Dynamic Type
* Sufficient contrast
* Accessible controls
* Logical focus order
* Accessible forms
* Accessible errors
* Accessible charts
* Motion reduction
* Semantic UI hierarchy

---

## 25. Localization Requirements

The system SHALL support:

```text
Language
Locale
Currency
Timezone
Date Format
Time Format
Number Format
Calendar Format
RTL Direction
```

The backend SHALL remain authoritative for organization-level localization policies where configured.

---

## 26. Testing Requirements

The iOS application SHALL include:

## Unit Testing

* API clients
* State management
* View models
* Business logic
* Validation
* Permission logic
* Offline synchronization

## Integration Testing

* Authentication
* API integration
* Push notifications
* Real-time transport
* Backend synchronization
* File upload/download
* OAuth

## UI Testing

* Login
* Organization switching
* Lead workflows
* CRM workflows
* Support workflows
* AI approval
* Workflow execution
* Reporting
* Notifications

## E2E Testing

Critical workflows SHALL be validated against staging backend environments.

---

## 27. CI/CD Requirements

The iOS project SHALL use automated CI/CD.

Pipeline:

```text
Commit
  |
  ▼
Lint
  |
  ▼
Static Analysis
  |
  ▼
Unit Tests
  |
  ▼
UI Tests
  |
  ▼
Security Checks
  |
  ▼
Build
  |
  ▼
TestFlight
  |
  ▼
Release Approval
  |
  ▼
App Store
```

---

## 28. Release Management

The application SHALL support:

* Development
* Testing
* Staging
* Production

Build configuration SHALL prevent accidental production credentials in development builds.

Release metadata SHALL include:

* App version
* Build number
* API compatibility
* Feature flags
* Release notes

---

## 29. Minimum Backend Contracts

Before an iOS module is considered production-ready, the backend SHOULD provide:

* Authentication API
* Authorization API
* Tenant context
* Stable API contracts
* Error schema
* Pagination
* Idempotency
* Request IDs
* Rate-limit metadata
* Real-time events where required
* Audit events where required
* Feature flags
* Versioning
* API documentation

---

## 30. Critical User Journeys

## Journey 1 — Login

```text
Open App
  ↓
Authenticate
  ↓
MFA if required
  ↓
Load User
  ↓
Load Organizations
  ↓
Load Permissions
  ↓
Load Feature Flags
  ↓
Load Dashboard
```

---

## Journey 2 — Lead Generation

```text
User
 ↓
Define ICP
 ↓
Submit Lead Generation Request
 ↓
Backend Job
 ↓
AI/Data Processing
 ↓
Real-Time Progress
 ↓
Generated Leads
 ↓
AI Scoring
 ↓
Human Review
 ↓
Approve
 ↓
CRM Import
```

---

## Journey 3 — AI Support

```text
Customer Message
       ↓
Backend
       ↓
AI Support Agent
       ↓
RAG Retrieval
       ↓
AI Response
       ↓
Confidence Evaluation
       ↓
 ┌─────┴─────┐
High        Low
 ↓           ↓
AI Reply    Human Review
             ↓
          Approval
             ↓
          Response
```

---

## Journey 4 — AI Sales Agent

```text
Lead
 ↓
Lead Intelligence
 ↓
Lead Score
 ↓
AI Sales Agent
 ↓
Recommended Action
 ↓
Human Approval
 ↓
Outreach
 ↓
CRM Update
 ↓
Analytics
```

---

## Journey 5 — Workflow

```text
User
 ↓
Select Workflow
 ↓
Configure Parameters
 ↓
Execute
 ↓
Backend Workflow Engine
 ↓
Real-Time Status
 ↓
Execution Result
 ↓
Analytics
```

---

## Journey 6 — Business Intelligence

```text
Sales Data
Marketing Data
Advertising Data
Expense Data
Product Data
Customer Data
       ↓
Analytics Backend
       ↓
Business Intelligence
       ↓
Revenue
Profit
Loss
Growth
Product Profitability
       ↓
AI Business Advisor
       ↓
Recommendations
```

---

## 31. Backend Connectivity Rules

Every iOS feature that modifies persistent business state MUST have a backend integration.

Examples:

```text
Create Lead
    → POST API

Update Lead
    → PATCH API

Assign Lead
    → POST/PATCH API

Send Message
    → Messaging API

Approve AI Action
    → Approval API

Execute Workflow
    → Workflow API

Generate Report
    → Reporting API

Update Profile
    → Identity API

Change Organization Setting
    → Organization API

Update Notification Preference
    → Notification Preference API
```

The frontend MUST NOT simulate successful backend operations without server confirmation except for explicitly defined optimistic UI behavior.

---

## 32. Backend Event Synchronization

When another client modifies data, the iOS application SHOULD receive the update through backend events.

Example:

```text
Web App
   |
   ▼
Backend
   |
   ├──────────────► Database
   |
   └──────────────► Event Bus
                       |
                       ▼
                  Real-Time Gateway
                       |
                       ▼
                      iOS
```

The iOS application SHALL reconcile event updates with local state.

---

## 33. Security-Critical Operations

The following operations SHOULD require elevated authentication or confirmation:

* Changing password
* Changing MFA
* Changing security settings
* Managing roles
* Managing permissions
* Suspending users
* Exporting sensitive data
* Connecting integrations
* Disconnecting integrations
* Executing high-impact AI actions
* Changing billing configuration
* Changing organization security configuration

---

## 34. Data Governance

The iOS application SHALL comply with backend policies for:

* Data retention
* Data deletion
* Consent
* Data export
* Privacy requests
* Tenant isolation
* Access control
* Audit logging
* Data classification

The application SHALL never bypass backend governance controls.

---

## 35. Observability

The iOS client SHALL expose safe telemetry for:

```text
Application
├── Crash Rate
├── Startup Time
├── Screen Performance
├── API Latency
├── API Errors
├── Network Failures
├── Real-Time Connection Failures
├── Offline Duration
├── Sync Failures
├── AI Interaction Latency
└── User Experience Metrics
```

Telemetry MUST exclude secrets and unauthorized PII.

---

## 36. Enterprise Scale Requirements

The iOS application SHALL be architected to support SalesGenie's target enterprise scale without assuming that all data is downloaded to the device.

The application SHALL use:

* Server-side pagination
* Incremental synchronization
* Efficient caching
* Lazy loading
* Background synchronization
* Event-driven updates
* Request deduplication
* Image optimization
* Resource lifecycle management

---

## 37. Disaster and Service Degradation Behavior

If a backend service becomes unavailable:

```text
Service Available
      ↓
Normal Operation

Service Degraded
      ↓
Cached/Read-Only Experience

Service Unavailable
      ↓
Graceful Error
      ↓
Retry
      ↓
Recovery
```

The application SHALL distinguish between:

* Client failure
* Network failure
* Authentication failure
* Authorization failure
* Backend failure
* Third-party integration failure
* AI provider failure

---

## 38. Feature Flag Architecture

Feature flags SHALL support:

```text
Global
Organization
Workplace
Role
User
Percentage
Environment
```

Example:

```text
AI_LEAD_GENERATION_IOS
AI_AGENT_APPROVAL_IOS
ADVANCED_ANALYTICS_IOS
PRODUCT_LAUNCH_IOS
AI_BUSINESS_ADVISOR_IOS
```

Feature flags SHALL be evaluated securely and consistently.

---

## 39. API Rate Limiting

The application SHALL gracefully handle backend rate limits.

When rate limited:

1. Detect HTTP 429.
2. Read retry metadata.
3. Delay retry.
4. Prevent request storms.
5. Display appropriate UI feedback.
6. Preserve user input where safe.

---

## 40. Data Synchronization Guarantees

The client SHALL distinguish:

```text
Local Draft
Pending Sync
Synced
Sync Failed
Conflict
Deleted Remotely
```

The UI SHALL not represent pending local mutations as permanently committed until backend confirmation is received.

---

## 41. Security and Privacy for AI

AI-related client data SHALL be handled carefully.

The application MUST NOT expose:

* API provider keys
* LLM credentials
* Internal prompts unless authorized
* Internal system instructions
* Internal tool credentials
* Internal infrastructure secrets

AI requests SHALL be sent through the SalesGenie backend AI gateway.

```text
iOS
 ↓
SalesGenie AI Gateway
 ↓
Policy / Security
 ↓
Model Routing
 ↓
LLM Provider
```

The iOS client SHALL never directly embed production LLM provider secrets.

---

## 42. Definition of Done

An iOS feature SHALL NOT be considered production-ready until:

* User requirements are implemented.
* System requirements are satisfied.
* Backend APIs are integrated.
* Authorization is enforced server-side.
* Tenant isolation is verified.
* Loading states exist.
* Empty states exist.
* Error states exist.
* Offline behavior is defined.
* Retry behavior is defined.
* Analytics are implemented where appropriate.
* Audit logging exists for sensitive operations.
* Accessibility is implemented.
* Localization is supported.
* Unit tests exist.
* Integration tests exist.
* UI tests exist for critical flows.
* Security testing is completed.
* Performance testing is completed.
* Crash monitoring is enabled.
* API observability is enabled.
* Feature flags are configured where required.
* Documentation is complete.

---

## 43. Final iOS Architecture Requirement

The SalesGenie iOS application SHALL function as a secure, enterprise-grade client of the SalesGenie platform:

```text
                         SALESGENIE iOS
                              |
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
        Presentation      Application       Local Data
        Layer             Layer             Layer
              |               |                |
              └───────────────┼────────────────┘
                              ▼
                         API CLIENT
                              |
                  ┌───────────┴───────────┐
                  ▼                       ▼
             API GATEWAY             REAL-TIME
                  |                       |
                  ▼                       ▼
        ┌─────────┼───────────────────────┐
        │         │                       │
        ▼         ▼                       ▼
       IAM       DOMAIN SERVICES       EVENT SYSTEM
        │         │                       │
        │    ┌────┼────┬────┬────┐        │
        │    ▼    ▼    ▼    ▼    ▼        │
        │   CRM  AI  RAG  BI  Workflow    │
        │                                 │
        └─────────────────────────────────┘
                              |
                              ▼
                       DATA PLATFORM
                              |
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
          PostgreSQL        Redis        Object Storage
```

The architecture MUST preserve:

* Backend authority
* Enterprise security
* Multi-tenant isolation
* Role-based access
* AI governance
* Human oversight
* Real-time synchronization
* Offline resilience
* Observability
* Accessibility
* Localization
* Scalability
* Reliability
* Privacy
* API compatibility

The iOS application SHALL be treated as a first-class enterprise client of SalesGenie's distributed platform, with the same security, authorization, reliability, observability, AI governance, and data-integrity guarantees expected from the web application.
