# SalesGenie — TikTok Integration

## FAANG-Level User Requirements, System Requirements & Functional Requirements

> **Document:** `tiktok_integration.md`
>
> **Platform:** SalesGenie / FlowMind AI
>
> **Integration:** TikTok
>
> **Scope:** Enterprise TikTok integration for human-driven and AI-driven content, marketing, sales intelligence, workflow automation, analytics, lead generation, and controlled publishing.
>
> **Architecture:** Multi-Tenant SaaS + Microservices + Event-Driven Architecture + Multi-Agent AI + MCP + Workflow Engine + RAG + CRM
>
> **Primary Actors:** Super Admin, Organization Admin, Marketing Manager, Sales Manager, Sales Agent, Content Manager, Human Reviewer, AI Agent, Workflow Engine, MCP Server, Integration Service, TikTok APIs
>
> **Core Principle:** TikTok must be treated as a governed enterprise integration. AI agents and humans must use the same authentication, authorization, policy, quota, approval, audit, and tenant-isolation controls.
>
> **API Compatibility:** The implementation must dynamically reflect TikTok's currently approved products, scopes, endpoints, review requirements, and usage restrictions. TikTok currently provides products including Login Kit, Content Posting API, Research API, Display API, Data Portability API, and Commercial Content API. Not every capability is available to every application or commercial use case. :contentReference[oaicite:0]{index=0}

---

## 1. Product Objective

SalesGenie shall provide an enterprise-grade TikTok integration allowing organizations to connect authorized TikTok accounts and use humans, AI agents, and workflows to:

- Authenticate TikTok users securely.
- Manage authorized TikTok connections.
- Retrieve permitted TikTok account information.
- Retrieve permitted TikTok content.
- Analyze TikTok content.
- Analyze public content where the organization has approved access.
- Generate TikTok content ideas.
- Generate captions and hashtags.
- Generate scripts and creative briefs.
- Generate short-form video concepts.
- Upload content to TikTok where authorized.
- Direct-post supported content where authorized.
- Support TikTok publishing workflows.
- Monitor publishing status.
- Analyze engagement data where available through authorized products.
- Identify potential customers from permitted TikTok data.
- Score potential leads.
- Synchronize qualified leads with SalesGenie CRM.
- Trigger sales workflows.
- Trigger marketing workflows.
- Create AI-powered content workflows.
- Require human approval for high-risk operations.
- Monitor API limits and integration health.
- Provide enterprise auditability and governance.

The architecture shall support:

```text
HUMAN
  ↓
SalesGenie
  ↓
Policy Engine
  ↓
TikTok Integration
  ↓
TikTok
```

and:

```text
AI AGENT
  ↓
MCP
  ↓
Workflow Engine
  ↓
Policy Engine
  ↓
TikTok Integration
  ↓
TikTok
```

AI must never bypass controls that apply to human users.

---

## 2. TikTok Capability Model

SalesGenie shall not implement a generic assumption that "TikTok API" provides unlimited access.

Instead, capabilities shall be represented through a capability registry.

```text
TikTok
 ├── Login Kit
 ├── Content Posting API
 │     ├── Direct Post
 │     └── Upload
 ├── Display API
 ├── Research API
 ├── Commercial Content API
 ├── Data Portability API
 └── Other approved TikTok products
```

The official developer platform currently lists these products separately, and access requirements differ by product. ([TikTok for Developers][1])

Example capability registry:

```json
{
  "provider": "tiktok",
  "capability": "content.direct_publish",
  "api_product": "Content Posting API",
  "required_scopes": [
    "video.publish"
  ],
  "approval_required": true,
  "human_approval_default": true,
  "risk_level": "HIGH",
  "supports_ai_execution": true,
  "requires_creator_context": true
}
```

---

## 3. Actors

## 3.1 Super Admin

The Super Admin shall be able to:

* Enable or disable TikTok integration globally.
* Configure platform-wide integration policies.
* Configure global security policies.
* Configure supported TikTok products.
* Configure organization-level limits.
* Monitor aggregate API usage.
* Monitor integration failures.
* Inspect security events.
* Configure AI automation policies.
* Configure risk policies.
* Manage platform-level credentials where applicable.
* Review integration health.
* Disable compromised integrations.

The Super Admin shall not automatically receive access to customer-owned TikTok content.

---

## 4. Organization Admin

The Organization Admin shall be able to:

* Connect TikTok accounts.
* Disconnect TikTok accounts.
* View connected accounts.
* Configure integration permissions.
* Assign TikTok permissions to users.
* Configure AI permissions.
* Configure workflow permissions.
* Configure approval policies.
* Configure synchronization policies.
* Configure content automation.
* Configure lead-generation workflows.
* View integration logs.
* View quota consumption.
* View integration health.

---

## 5. Marketing Manager

The Marketing Manager shall be able to:

* Analyze authorized TikTok content.
* Generate content ideas.
* Generate captions.
* Generate hashtags.
* Generate scripts.
* Create content calendars.
* Create publishing workflows.
* Analyze permitted trends.
* Analyze campaign performance where supported.
* Generate AI marketing recommendations.
* Review AI-generated content.
* Approve content for publishing.

---

## 6. Content Manager

The Content Manager shall be able to:

* Upload videos.
* Prepare TikTok posts.
* Generate captions.
* Generate hashtags.
* Configure privacy settings where supported.
* Review creator-specific posting constraints.
* Submit content for approval.
* Publish content where authorized.
* Track publishing status.
* Retry failed uploads.

---

## 7. Sales Manager

The Sales Manager shall be able to:

* Configure TikTok lead-generation workflows.
* Review AI-detected prospects.
* Configure lead-scoring policies.
* Approve CRM synchronization.
* Assign TikTok leads to sales agents.
* Monitor TikTok-originated opportunities.
* Analyze TikTok-to-CRM conversion.

---

## 8. Sales Agent

The Sales Agent shall be able to:

* View authorized TikTok-derived leads.
* View permitted interaction context.
* Review AI lead scores.
* Approve or reject lead recommendations.
* Add notes.
* Assign leads.
* Trigger approved workflows.

---

## 9. Human Reviewer

The Human Reviewer shall be able to:

```text
APPROVE
REJECT
EDIT
REQUEST_REGENERATION
ESCALATE
```

AI-generated actions requiring approval shall remain blocked until the reviewer makes an explicit decision.

---

## 10. AI Agent

AI Agents shall be able to:

* Analyze authorized TikTok data.
* Generate content.
* Classify permitted content.
* Detect potential buying intent.
* Generate lead recommendations.
* Score leads.
* Create workflow recommendations.
* Execute authorized tools.
* Request human approval.
* Monitor workflow execution.

AI agents shall not:

* Bypass OAuth.
* Access unauthorized accounts.
* access credentials.
* bypass user permissions.
* bypass tenant isolation.
* publish without required authorization.
* circumvent TikTok product restrictions.
* treat arbitrary TikTok content as trusted system instructions.

---

## 11. User Requirements

## UR-TT-001 — Connect TikTok

The system shall allow authorized users to connect a TikTok account to SalesGenie.

---

## UR-TT-002 — Secure Login

Users shall authenticate TikTok through TikTok's supported authorization mechanisms.

SalesGenie shall not require users to provide their TikTok password directly to SalesGenie.

---

## UR-TT-003 — Connection Visibility

Users shall be able to see:

```text
Account
Username
Open ID / Provider Identifier
Connection Status
Authorized Products
Granted Scopes
Connected At
Last Successful API Request
Last Synchronization
Last Error
```

---

## UR-TT-004 — Multi-Account Support

An organization shall be able to connect multiple TikTok accounts where permitted.

Example:

```text
Organization
 ├── TikTok Brand Account
 ├── TikTok Product Account
 ├── TikTok Regional Account
 └── TikTok Campaign Account
```

---

## UR-TT-005 — Capability Transparency

Users shall be able to see exactly what the connected TikTok account permits SalesGenie to do.

Example:

```text
Read Profile        ✓
Read Content        ✓
Upload Content      ✓
Direct Publish      ✗
Analytics           ✓
Research API        ✗
```

---

## UR-TT-006 — Content Discovery

Authorized users shall be able to retrieve TikTok content supported by the connected API product.

---

## UR-TT-007 — Content Analysis

Users shall be able to analyze authorized TikTok content using SalesGenie's AI.

---

## UR-TT-008 — AI Content Ideas

Users shall be able to generate:

* Video ideas.
* Hooks.
* Scripts.
* Captions.
* Hashtags.
* CTAs.
* Creative briefs.
* Content series.
* Short-form video concepts.

---

## UR-TT-009 — AI Caption Generation

Users shall be able to generate multiple caption variants.

Example:

```text
Professional
Educational
Conversational
Humorous
Sales-Oriented
Storytelling
Short
Long
CTA-Focused
```

---

## UR-TT-010 — AI Hashtag Generation

The system shall generate hashtag recommendations based on:

* Topic.
* Audience.
* Campaign.
* Product.
* Industry.
* Content intent.
* Organization configuration.

The AI shall not claim that a hashtag is currently trending unless supported by authorized and sufficiently fresh data.

---

## UR-TT-011 — Content Calendar

Users shall be able to create TikTok content calendars.

The calendar shall contain:

```text
Date
Time
Campaign
Content
Caption
Hashtags
Status
Approval
Publishing Method
Owner
```

---

## UR-TT-012 — Human Content Approval

Organizations shall be able to require human approval before TikTok publishing.

---

## UR-TT-013 — AI Content Generation

AI agents shall be able to generate content based on:

```text
Brand Guidelines
Product Catalog
RAG Knowledge Base
Campaign Objectives
Target Audience
Historical Content
Organization Policies
```

---

## UR-TT-014 — AI Content Review

Users shall be able to inspect:

* AI-generated text.
* AI-generated metadata.
* AI reasoning summary.
* Content policy results.
* Brand-policy results.
* Risk level.
* Recommended action.

---

## UR-TT-015 — Content Upload

Authorized users shall be able to upload supported content through the appropriate TikTok Content Posting API flow.

TikTok's current Content Posting API supports video and photo posting/upload workflows. ([TikTok for Developers][2])

---

## UR-TT-016 — Direct Publishing

Where approved and authorized, users shall be able to publish supported content directly to TikTok.

TikTok's current Direct Post flow requires creator information to be queried before posting and requires the appropriate publishing authorization, including `video.publish`. ([TikTok for Developers][3])

---

## UR-TT-017 — Upload-Then-Review

Users shall be able to use an upload workflow in which content is transferred to TikTok for the user to review and complete in TikTok.

TikTok documents this as a separate upload flow using `video.upload`; users must continue the editing/posting flow in TikTok. ([TikTok for Developers][2])

---

## UR-TT-018 — Creator Privacy Controls

Before direct publishing, SalesGenie shall retrieve and honor the creator's currently available privacy options.

TikTok's Direct Post documentation requires applications to query creator information and honor the returned privacy-level options. ([TikTok for Developers][3])

---

## UR-TT-019 — Publishing Status

Users shall be able to see:

```text
DRAFT
UPLOADING
UPLOADED
PROCESSING
PUBLISHED
FAILED
REQUIRES_REVIEW
REQUIRES_REAUTH
REJECTED
```

---

## UR-TT-020 — AI Lead Detection

Where permitted data is available, AI shall identify potential customer intent.

Possible classifications:

```text
HIGH_PURCHASE_INTENT
MEDIUM_PURCHASE_INTENT
LOW_PURCHASE_INTENT
SUPPORT_INTENT
PARTNERSHIP_INTENT
PRODUCT_INTEREST
GENERAL_INTEREST
UNKNOWN
```

---

## UR-TT-021 — Lead Scoring

AI shall calculate configurable lead scores.

Example:

```text
Intent
+
Content Relevance
+
Business Fit
+
Engagement Signal
+
Historical Interaction
=
Lead Score
```

---

## UR-TT-022 — CRM Synchronization

Approved TikTok leads shall be synchronizable with:

* SalesGenie CRM.
* HubSpot.
* Salesforce.
* Other authorized CRM integrations.

---

## UR-TT-023 — Lead Attribution

SalesGenie shall retain TikTok as a source attribution.

Example:

```text
Lead Source:
TikTok

Campaign:
Summer Product Campaign

Content:
Video ID

Interaction:
Authorized TikTok Data Source

Conversion:
CRM Opportunity
```

---

## UR-TT-024 — Workflow Automation

Users shall be able to create TikTok-triggered workflows.

---

## UR-TT-025 — Scheduled Analysis

Users shall be able to schedule:

* Content analysis.
* Campaign reports.
* Lead analysis.
* Content recommendations.
* Synchronization.
* Performance monitoring.

---

## UR-TT-026 — AI Workflow Automation

AI agents shall be able to trigger approved TikTok workflows.

---

## UR-TT-027 — Human Override

Users shall be able to stop:

* AI workflows.
* Scheduled publishing.
* Content pipelines.
* Lead-generation automation.
* Synchronization.

---

## UR-TT-028 — Disconnect

Authorized users shall be able to disconnect TikTok.

Disconnecting shall:

* Stop protected API operations.
* Invalidate local authorization state.
* Pause dependent workflows.
* Preserve audit records.
* Mark the integration as disconnected.

---

## 12. System Requirements

## SR-TT-001 — Multi-Tenant Isolation

Every TikTok resource shall contain:

```text
tenant_id
organization_id
connection_id
provider
provider_user_id
resource_type
resource_id
```

No tenant may access another tenant's TikTok data.

---

## SR-TT-002 — Integration Service

TikTok shall be implemented behind a dedicated Integration Service.

```text
API Gateway
    ↓
Integration Service
    ↓
TikTok Adapter
    ↓
TikTok APIs
```

---

## SR-TT-003 — Capability Registry

Every TikTok capability shall be represented by a versioned capability definition.

```json
{
  "provider": "tiktok",
  "product": "content_posting",
  "operation": "direct_publish_video",
  "required_scopes": [
    "video.publish"
  ],
  "approval_required": true,
  "risk_level": "HIGH",
  "enabled": true
}
```

---

## SR-TT-004 — OAuth Security

OAuth credentials shall:

* Be encrypted at rest.
* Be transmitted only over TLS.
* Never appear in application logs.
* Never be exposed to AI agents.
* Never be sent to the frontend unnecessarily.
* Be stored in a secure secret/token system.

---

## SR-TT-005 — Least Privilege

SalesGenie shall request only scopes required by the selected functionality.

---

## SR-TT-006 — Scope Mapping

The integration shall maintain a scope-to-capability mapping.

Example:

```text
video.upload
    ↓
Upload Content

video.publish
    ↓
Direct Publish

user.info.basic
    ↓
Basic User Information

user.info.profile
    ↓
Authorized Profile Information
```

Actual scopes shall always be validated against the current TikTok documentation before implementation.

---

## SR-TT-007 — RBAC

SalesGenie shall support permissions including:

```text
tiktok.integration.read
tiktok.integration.manage

tiktok.account.read

tiktok.content.read
tiktok.content.analyze

tiktok.content.create
tiktok.content.upload
tiktok.content.publish
tiktok.content.update
tiktok.content.delete

tiktok.analytics.read

tiktok.lead.read
tiktok.lead.create
tiktok.lead.assign

tiktok.workflow.read
tiktok.workflow.execute
tiktok.workflow.manage

tiktok.ai.analyze
tiktok.ai.generate
tiktok.ai.execute

tiktok.approval.review
```

---

## SR-TT-008 — ABAC

Authorization shall consider:

```text
tenant_id
organization_id
user_id
role
connection_id
account_id
workflow_id
agent_id
resource_id
risk_level
approval_status
environment
```

---

## SR-TT-009 — AI Agent Context

Every AI agent execution shall receive:

```text
tenant_id
organization_id
agent_id
workflow_id
user_id
connection_id
allowed_tools
allowed_scopes
allowed_actions
risk_policy
approval_policy
budget
quota
```

---

## SR-TT-010 — MCP Integration

The TikTok integration shall expose controlled MCP capabilities.

Example:

```text
tiktok.get_profile
tiktok.get_content
tiktok.search_content
tiktok.analyze_content

tiktok.generate_caption
tiktok.generate_hashtags
tiktok.generate_script

tiktok.prepare_upload
tiktok.upload_content
tiktok.publish_content
tiktok.get_publish_status

tiktok.detect_lead
tiktok.score_lead

tiktok.sync
```

Only capabilities actually supported by the connected TikTok product and authorization shall be exposed.

---

## SR-TT-011 — MCP Tool Metadata

Every MCP tool shall declare:

```text
tool_name
description
input_schema
output_schema
required_scopes
required_permissions
risk_level
approval_requirement
quota_policy
idempotency_policy
api_product
api_version
```

---

## SR-TT-012 — Tool Authorization

Every MCP invocation shall pass:

```text
Authentication
↓
Tenant Validation
↓
RBAC
↓
ABAC
↓
Scope Validation
↓
Capability Validation
↓
Policy Evaluation
↓
Approval Validation
↓
Quota Validation
↓
Execution
```

---

## 13. TikTok Content Posting Architecture

## SR-TT-013 — Creator Information Preflight

Before a direct post, SalesGenie shall retrieve current creator information where required.

The response may determine:

* Creator identity.
* Available privacy levels.
* Comment settings.
* Duet settings.
* Stitch settings.
* Maximum supported duration.
* Other creator-specific posting constraints.

TikTok explicitly requires creator information to be queried before Direct Post. ([TikTok for Developers][3])

---

## SR-TT-014 — Direct Post State Machine

The direct publishing state machine shall be:

```text
DRAFT
  ↓
CONTENT_VALIDATION
  ↓
AI_POLICY_CHECK
  ↓
HUMAN_APPROVAL
  ↓
AUTHORIZATION_CHECK
  ↓
CREATOR_INFO_PREFLIGHT
  ↓
QUOTA_CHECK
  ↓
POST_INITIALIZATION
  ↓
MEDIA_TRANSFER
  ↓
PROCESSING
  ↓
PUBLISH_VERIFICATION
  ↓
PUBLISHED
```

Failure states shall transition to:

```text
FAILED
REQUIRES_REAUTH
REQUIRES_REVIEW
QUOTA_BLOCKED
POLICY_BLOCKED
```

---

## SR-TT-015 — User Consent

Direct posting shall require explicit user consent for sending the content to TikTok.

TikTok's current Direct Post documentation requires users to provide necessary metadata and explicit consent before the application sends the video to TikTok. ([TikTok for Developers][4])

---

## SR-TT-016 — Publishing Restrictions

The system shall honor:

* Creator privacy options.
* TikTok posting restrictions.
* Client review requirements.
* API scope restrictions.
* Rate limits.
* Daily posting limits.
* Application approval restrictions.

TikTok documents errors including invalid scopes, posting limits, rate limits, privacy-option mismatches, and restrictions affecting unaudited clients. ([TikTok for Developers][4])

---

## 14. Upload Architecture

## SR-TT-017

The upload service shall support supported transfer modes.

```text
FILE_UPLOAD
PULL_FROM_URL
```

TikTok's current upload API documents both mechanisms for video uploads. ([TikTok for Developers][5])

---

## SR-TT-018

The media service shall validate:

```text
File Type
File Size
Codec
Duration
Resolution
Aspect Ratio
Content Policy
Malware
Integrity
```

---

## SR-TT-019

The media pipeline shall support chunked upload where required.

---

## SR-TT-020

Upload failures shall be resumable when technically supported.

---

## 15. API Rate Limiting

## SR-TT-021

The system shall maintain rate limits per:

```text
tenant
connection
TikTok user
workflow
AI agent
API operation
```

TikTok's current Direct Post API documentation states that each user access token is limited to six requests per minute for the relevant initialization endpoint. SalesGenie shall therefore model provider-specific rate limits rather than assuming a universal limit. ([TikTok for Developers][4])

---

## SR-TT-022

The system shall use:

```text
Token Bucket
+
Exponential Backoff
+
Circuit Breaker
+
Queue-Based Execution
```

---

## 16. Research API Requirements

## SR-TT-023

The Research API shall be treated as a separate capability from normal commercial TikTok account integration.

---

## SR-TT-024

SalesGenie shall not automatically grant Research API functionality merely because a tenant has connected TikTok.

---

## SR-TT-025

Research API access shall require an approved research project/credential where TikTok requires it.

TikTok currently restricts Research Tools to qualifying researchers and approved projects; its documentation explicitly states that commercial users are not eligible for Research Tools. ([TikTok for Developers][6])

---

## SR-TT-026

The Research API service shall maintain separate:

```text
research_client_id
research_project_id
research_access_token
research_policy
research_quota
```

---

## SR-TT-027

Research data shall never be mixed with customer-owned TikTok account data without explicit data-governance rules.

---

## SR-TT-028

Research API queries shall support:

```text
Keyword
Username
Region
Video ID
Hashtag
Music
Effect
Video Length
Date Range
```

TikTok's current Research API documentation supports these query condition fields and cursor-based pagination. ([TikTok for Developers][7])

---

## SR-TT-029

Research API results shall be marked:

```text
DATA_CLASS = RESEARCH
SOURCE = TIKTOK_RESEARCH_API
```

---

## 17. Research API Pagination

The research service shall support:

```text
cursor
search_id
has_more
max_count
```

The system shall continue pagination until:

```text
has_more == false
```

or until:

```text
tenant_budget_exceeded
workflow_limit_reached
user_cancelled
```

TikTok currently documents a maximum `max_count` of 100 for Research API video queries. ([TikTok for Developers][7])

---

## 18. Data Freshness

SalesGenie shall track data freshness.

```text
source_timestamp
retrieved_at
last_updated_at
data_age
freshness_status
```

Research data shall not automatically be treated as real-time analytics.

TikTok currently documents that Research API video datasets can be archived and that new videos/statistics may have substantial indexing/update delays. ([TikTok for Developers][8])

---

## 19. Event-Driven Architecture

The integration shall publish events including:

```text
tiktok.connection.created
tiktok.connection.updated
tiktok.connection.revoked

tiktok.account.synced
tiktok.content.discovered
tiktok.content.updated

tiktok.content.generated
tiktok.content.approved
tiktok.content.rejected

tiktok.upload.started
tiktok.upload.completed
tiktok.upload.failed

tiktok.publish.started
tiktok.publish.processing
tiktok.publish.completed
tiktok.publish.failed

tiktok.lead.detected
tiktok.lead.scored
tiktok.lead.created

tiktok.workflow.started
tiktok.workflow.completed
tiktok.workflow.failed

tiktok.quota.warning
tiktok.rate_limit.warning

tiktok.integration.degraded
tiktok.integration.failed
```

---

## 20. Event Schema

```json
{
  "event_id": "uuid",
  "event_type": "tiktok.publish.completed",
  "event_version": "1.0",
  "tenant_id": "uuid",
  "organization_id": "uuid",
  "connection_id": "uuid",
  "tiktok_user_id": "string",
  "resource_type": "video",
  "resource_id": "string",
  "workflow_id": "uuid",
  "agent_id": "uuid",
  "actor_type": "human|ai|system",
  "timestamp": "ISO-8601",
  "trace_id": "uuid",
  "idempotency_key": "string"
}
```

---

## 21. Functional Requirements

## 21.1 Authentication

## FR-TT-AUTH-001

The system shall provide a **Connect TikTok** operation.

---

## FR-TT-AUTH-002

The system shall initiate TikTok's supported authorization flow.

---

## FR-TT-AUTH-003

The system shall validate OAuth state.

---

## FR-TT-AUTH-004

The system shall securely process the authorization callback.

---

## FR-TT-AUTH-005

The system shall securely store authorization credentials.

---

## FR-TT-AUTH-006

The system shall record granted scopes.

---

## FR-TT-AUTH-007

The system shall associate the connection with the correct SalesGenie tenant.

---

## FR-TT-AUTH-008

The system shall detect expired or invalid tokens.

---

## FR-TT-AUTH-009

The system shall support reauthorization.

---

## 21.2 Account Management

## FR-TT-ACCOUNT-001

The system shall retrieve authorized account information where permitted.

---

## FR-TT-ACCOUNT-002

The system shall store canonical account metadata.

---

## FR-TT-ACCOUNT-003

The system shall display connection health.

---

## FR-TT-ACCOUNT-004

The system shall allow authorized users to disconnect accounts.

---

## 21.3 Content Retrieval

## FR-TT-CONTENT-001

The system shall retrieve content using the appropriate approved TikTok API.

---

## FR-TT-CONTENT-002

The system shall normalize TikTok content.

---

## FR-TT-CONTENT-003

The system shall associate content with:

```text
tenant
connection
account
campaign
workflow
```

---

## FR-TT-CONTENT-004

The system shall preserve source metadata.

---

## 21.4 AI Content Analysis

## FR-TT-AI-001

AI shall analyze authorized TikTok content.

---

## FR-TT-AI-002

AI shall classify content by:

```text
Topic
Intent
Sentiment
Industry
Audience
Product
Campaign
Content Type
```

---

## FR-TT-AI-003

AI shall identify potential content opportunities.

---

## FR-TT-AI-004

AI shall generate recommendations.

---

## 21.5 AI Content Generation

## FR-TT-AI-005

The system shall generate TikTok scripts.

---

## FR-TT-AI-006

The system shall generate hooks.

---

## FR-TT-AI-007

The system shall generate captions.

---

## FR-TT-AI-008

The system shall generate hashtag recommendations.

---

## FR-TT-AI-009

The system shall generate CTAs.

---

## FR-TT-AI-010

The system shall generate content variants.

---

## FR-TT-AI-011

The system shall store generation metadata:

```text
model_provider
model_name
model_version
prompt_version
generation_id
timestamp
tenant_id
agent_id
workflow_id
```

---

## 21.6 Publishing

## FR-TT-PUBLISH-001

The system shall validate content before upload.

---

## FR-TT-PUBLISH-002

The system shall validate authorization.

---

## FR-TT-PUBLISH-003

The system shall validate creator-specific options.

---

## FR-TT-PUBLISH-004

The system shall require human approval when configured.

---

## FR-TT-PUBLISH-005

The system shall validate quota/rate-limit availability.

---

## FR-TT-PUBLISH-006

The system shall initialize the TikTok publishing request.

---

## FR-TT-PUBLISH-007

The system shall transfer media.

---

## FR-TT-PUBLISH-008

The system shall track publishing state.

---

## FR-TT-PUBLISH-009

The system shall verify final publishing status.

---

## FR-TT-PUBLISH-010

The system shall record the resulting TikTok publish identifier.

---

## 22. AI-Powered Publishing

## FR-TT-AI-PUBLISH-001

AI shall be allowed to prepare publishing operations.

---

## FR-TT-AI-PUBLISH-002

AI shall not automatically publish unless:

```text
Required Scope
+
Required Permission
+
Organization Policy
+
Workflow Policy
+
Content Policy
+
Approval Policy
+
Quota
```

all pass.

---

## FR-TT-AI-PUBLISH-003

Default enterprise behavior shall be:

```text
AI Generate
    ↓
AI Safety
    ↓
Brand Policy
    ↓
Human Approval
    ↓
TikTok Preflight
    ↓
Publish
```

---

## 23. Human Workflow Examples

## HWF-TT-001 — Manual Content Publishing

```text
Content Manager
    ↓
Create TikTok Content
    ↓
Upload Video
    ↓
Generate Caption
    ↓
Generate Hashtags
    ↓
Review
    ↓
Select Privacy
    ↓
Approve
    ↓
TikTok Creator Preflight
    ↓
Publish
    ↓
Monitor Status
```

---

## HWF-TT-002 — AI-Assisted Publishing

```text
Marketing Manager
    ↓
Enter Campaign Objective
    ↓
AI Generates:
    ├── Hook
    ├── Script
    ├── Caption
    ├── Hashtags
    └── CTA
    ↓
Human Review
    ↓
Edit
    ↓
Approve
    ↓
Upload
    ↓
Publish
```

---

## HWF-TT-003 — Lead Qualification

```text
Sales Agent
    ↓
Open TikTok Lead
    ↓
View AI Analysis
    ↓
Review Evidence
    ↓
Approve Lead
    ↓
Create CRM Lead
    ↓
Assign Sales Owner
```

---

## 24. AI Workflow Examples

## AIWF-TT-001 — Automated Content Generation

```text
Campaign Created
        ↓
AI Agent
        ↓
Retrieve Brand Knowledge
        ↓
Retrieve Product Knowledge
        ↓
Analyze Previous Content
        ↓
Generate TikTok Concept
        ↓
Generate Script
        ↓
Generate Caption
        ↓
Generate Hashtags
        ↓
Policy Check
        ↓
Human Approval
```

---

## AIWF-TT-002 — AI Content Optimization

```text
Existing TikTok Content
        ↓
AI Analysis
        ↓
Identify Weaknesses
        ↓
Generate Alternative Hooks
        ↓
Generate Alternative Captions
        ↓
Generate CTA
        ↓
Human Review
```

---

## AIWF-TT-003 — AI Lead Detection

```text
Authorized TikTok Data
        ↓
Content Classification
        ↓
Intent Detection
        ↓
Business Relevance
        ↓
Lead Scoring
        ↓
Policy Check
        ↓
CRM Lead Recommendation
        ↓
Human Approval
        ↓
CRM
```

---

## 25. MCP Requirements

## FR-TT-MCP-001

The MCP server shall expose only authorized TikTok tools.

---

## FR-TT-MCP-002

Every tool shall validate:

```text
tenant
user
role
connection
scope
capability
workflow
agent
resource
policy
```

---

## FR-TT-MCP-003

The MCP layer shall reject unauthorized tool invocations.

---

## FR-TT-MCP-004

The MCP layer shall prevent AI agents from directly accessing OAuth secrets.

---

## FR-TT-MCP-005

The MCP layer shall generate trace IDs for all tool invocations.

---

## 26. Tool Catalog

Recommended tools:

```text
tiktok.get_account
tiktok.get_profile

tiktok.list_content
tiktok.get_content
tiktok.search_content

tiktok.analyze_content

tiktok.generate_hook
tiktok.generate_script
tiktok.generate_caption
tiktok.generate_hashtags
tiktok.generate_cta

tiktok.query_creator_info

tiktok.initialize_upload
tiktok.upload_media
tiktok.get_upload_status

tiktok.initialize_publish
tiktok.publish_content
tiktok.get_publish_status

tiktok.detect_lead
tiktok.score_lead
tiktok.create_lead

tiktok.sync
tiktok.health_check
```

Tool availability shall be dynamic and capability-driven.

---

## 27. Workflow Conditions

Examples:

```text
IF tiktok.content.type == "VIDEO"
THEN analyze_content
```

```text
IF tiktok.lead.intent_score >= 0.85
THEN create_crm_lead
```

```text
IF tiktok.content.policy_status != "APPROVED"
THEN require_human_review
```

```text
IF tiktok.connection.status != "AUTHORIZED"
THEN pause_workflow
```

```text
IF tiktok.publish.risk_level == "HIGH"
THEN require_human_approval
```

```text
IF tiktok.rate_limit.remaining < threshold
THEN queue_publish
```

```text
IF tiktok.creator.privacy_options
DO NOT select unsupported privacy_level
```

---

## 28. Workflow Actions

Recommended actions:

```text
tiktok.connect
tiktok.disconnect

tiktok.get_account
tiktok.get_profile
tiktok.get_content
tiktok.search_content

tiktok.analyze_content

tiktok.generate_hook
tiktok.generate_script
tiktok.generate_caption
tiktok.generate_hashtags
tiktok.generate_cta

tiktok.query_creator_info

tiktok.prepare_upload
tiktok.upload_content

tiktok.prepare_publish
tiktok.publish_content
tiktok.get_publish_status

tiktok.detect_lead
tiktok.score_lead
tiktok.create_lead
tiktok.sync_lead

tiktok.sync
tiktok.health_check
```

---

## 29. Synchronization Engine

## FR-TT-SYNC-001

The system shall support initial synchronization.

---

## FR-TT-SYNC-002

The system shall support incremental synchronization where the underlying API supports appropriate retrieval semantics.

---

## FR-TT-SYNC-003

The system shall support scheduled synchronization.

---

## FR-TT-SYNC-004

The system shall support manual synchronization.

---

## FR-TT-SYNC-005

The system shall detect duplicates.

---

## FR-TT-SYNC-006

The system shall maintain synchronization checkpoints.

---

## FR-TT-SYNC-007

The system shall recover from interrupted synchronization.

---

## FR-TT-SYNC-008

The system shall record:

```text
sync_started_at
sync_completed_at
records_discovered
records_created
records_updated
records_skipped
records_failed
last_cursor
error
```

---

## 30. Error Handling

## FR-TT-ERR-001

The system shall classify errors:

```text
AUTHENTICATION_ERROR
AUTHORIZATION_ERROR
INVALID_SCOPE
INVALID_REQUEST
RESOURCE_NOT_FOUND
RATE_LIMIT_EXCEEDED
POSTING_LIMIT_EXCEEDED
QUOTA_EXCEEDED
TOKEN_EXPIRED
TOKEN_REVOKED
PRIVACY_OPTION_MISMATCH
CONTENT_VALIDATION_ERROR
MEDIA_UPLOAD_ERROR
PROCESSING_ERROR
NETWORK_ERROR
TIMEOUT
POLICY_BLOCKED
APPROVAL_REQUIRED
API_ERROR
UNKNOWN_ERROR
```

TikTok's current Content Posting API documentation explicitly describes errors including invalid parameters, invalid/expired access tokens, unauthorized scopes, rate limiting, posting restrictions, privacy-option mismatches, and server/network failures. ([TikTok for Developers][4])

---

## FR-TT-ERR-002

Transient failures shall be retried.

---

## FR-TT-ERR-003

Authorization failures shall not be blindly retried.

---

## FR-TT-ERR-004

Policy failures shall not be retried automatically.

---

## FR-TT-ERR-005

The system shall use exponential backoff.

---

## FR-TT-ERR-006

The system shall support dead-letter queues.

---

## 31. Token Lifecycle

## FR-TT-TOKEN-001

The system shall monitor token validity.

---

## FR-TT-TOKEN-002

The system shall securely refresh tokens when supported.

---

## FR-TT-TOKEN-003

The system shall detect revoked authorization.

---

## FR-TT-TOKEN-004

The system shall mark connections requiring reauthorization.

---

## FR-TT-TOKEN-005

Dependent workflows shall automatically pause when authorization is invalid.

---

## 32. AI Safety Requirements

## SR-TT-AI-001

TikTok content shall be considered untrusted external input.

---

## SR-TT-AI-002

The system shall protect against prompt injection.

Example:

```text
TikTok Caption
     ↓
Untrusted Input
     ↓
Sanitization
     ↓
Content Classifier
     ↓
AI Context Isolation
     ↓
Agent
```

---

## SR-TT-AI-003

AI agents shall never treat TikTok captions, comments, descriptions, or metadata as system instructions.

---

## SR-TT-AI-004

AI-generated publishing operations shall pass through the policy engine.

---

## SR-TT-AI-005

AI shall not bypass human approval.

---

## SR-TT-AI-006

AI shall not modify authorization state.

---

## SR-TT-AI-007

AI shall not retrieve OAuth tokens.

---

## 33. Content Safety

The AI content gateway shall evaluate:

```text
Hate
Harassment
Violence
Sexual Content
Dangerous Content
Illegal Activity
Spam
Scams
Impersonation
Misinformation Risk
Copyright Risk
Privacy Risk
Personal Data
Brand Safety
Regulatory Risk
```

The exact policy implementation shall be configurable by organization and jurisdiction.

---

## 34. Brand Safety

Organizations shall be able to define:

```text
Forbidden Words
Required Phrases
Tone
Brand Voice
Competitor Restrictions
Industry Restrictions
Legal Disclaimers
CTA Rules
Hashtag Rules
Audience Rules
```

AI-generated TikTok content shall be validated against the configured policy.

---

## 35. RAG Integration

The TikTok AI subsystem shall support retrieval from SalesGenie's RAG knowledge base.

Example:

```text
TikTok Content Request
        ↓
Retrieve Brand Guidelines
        ↓
Retrieve Product Knowledge
        ↓
Retrieve Campaign Knowledge
        ↓
Retrieve Legal Guidelines
        ↓
AI Generation
        ↓
Policy Validation
```

---

## 36. CRM Integration

TikTok-derived leads shall support:

```text
Lead
Contact
Account
Opportunity
Campaign
Activity
Interaction
Owner
Source
```

Example:

```json
{
  "source": "tiktok",
  "source_type": "social",
  "campaign_id": "campaign-123",
  "intent_score": 0.92,
  "qualification_status": "AI_RECOMMENDED",
  "requires_human_review": true
}
```

---

## 37. Lead Scoring

The AI lead score shall be configurable.

Example:

```text
Lead Score =
    Intent × 0.35
  + Product Relevance × 0.20
  + Business Fit × 0.20
  + Engagement × 0.15
  + Historical Signals × 0.10
```

The organization shall be able to modify weights.

---

## 38. Audit Requirements

The system shall audit:

```text
Connection Created
Connection Removed
Scope Granted
Scope Changed
Authentication Failure
Token Failure
Content Retrieved
Content Generated
Content Uploaded
Content Published
Content Rejected
AI Decision
AI Tool Call
Human Approval
Human Rejection
Workflow Started
Workflow Completed
Workflow Failed
CRM Lead Created
Quota Warning
Rate Limit Event
Policy Violation
```

---

## 39. Audit Event Schema

```json
{
  "event_id": "uuid",
  "tenant_id": "uuid",
  "organization_id": "uuid",
  "connection_id": "uuid",
  "actor_type": "human|ai|system",
  "actor_id": "uuid",
  "action": "tiktok.publish_content",
  "resource_type": "video",
  "resource_id": "provider-resource-id",
  "authorization_result": "allowed",
  "policy_result": "approved",
  "approval_result": "approved",
  "execution_result": "success",
  "trace_id": "uuid",
  "timestamp": "ISO-8601"
}
```

---

## 40. Monitoring Requirements

## FR-TT-MON-001

The system shall monitor connection health.

---

## FR-TT-MON-002

The system shall monitor API latency.

---

## FR-TT-MON-003

The system shall monitor API errors.

---

## FR-TT-MON-004

The system shall monitor rate limits.

---

## FR-TT-MON-005

The system shall monitor publishing failures.

---

## FR-TT-MON-006

The system shall monitor upload failures.

---

## FR-TT-MON-007

The system shall monitor AI workflow failures.

---

## FR-TT-MON-008

The system shall monitor human approval latency.

---

## FR-TT-MON-009

The system shall monitor synchronization lag.

---

## 41. Metrics

Recommended metrics:

```text
tiktok_connected_accounts
tiktok_active_connections
tiktok_api_requests_total
tiktok_api_errors_total
tiktok_api_latency_ms
tiktok_rate_limit_events
tiktok_uploads_total
tiktok_upload_failures
tiktok_publishes_total
tiktok_publish_failures
tiktok_ai_generations_total
tiktok_ai_tool_calls_total
tiktok_human_approvals_total
tiktok_human_rejections_total
tiktok_leads_detected_total
tiktok_leads_created_total
tiktok_crm_conversions_total
tiktok_workflows_total
tiktok_workflow_failures
```

---

## 42. Data Models

## TikTokConnection

```text
id
tenant_id
organization_id
provider
provider_user_id
username
display_name
encrypted_access_token
encrypted_refresh_token
token_expires_at
granted_scopes
enabled_products
status
created_at
updated_at
last_sync_at
last_error
```

---

## TikTokContent

```text
id
tenant_id
connection_id
provider_content_id
content_type
title
caption
hashtags
media_reference
published_at
status
metadata
source
created_at
updated_at
```

---

## TikTokPublishJob

```text
id
tenant_id
connection_id
workflow_id
content_id
publish_method
status
privacy_level
publish_id
upload_id
approval_status
policy_status
created_at
started_at
completed_at
error_code
error_message
```

---

## TikTokLead

```text
id
tenant_id
connection_id
source_content_id
source_interaction_id
crm_contact_id
crm_lead_id
intent_score
relevance_score
qualification_score
confidence
status
assigned_to
created_at
updated_at
```

---

## TikTokWorkflowExecution

```text
id
tenant_id
workflow_id
connection_id
trigger
actor_type
agent_id
status
started_at
completed_at
actions_executed
actions_failed
api_calls
trace_id
error_code
```

---

## 43. AI Decision Record

Every important AI decision shall have:

```text
decision_id
tenant_id
agent_id
workflow_id
model_provider
model_name
model_version
input_reference
decision
confidence
policy_result
recommended_action
approval_required
human_decision
timestamp
```

---

## 44. Human-in-the-Loop Architecture

```text
AI Agent
   ↓
Generate
   ↓
Risk Classifier
   ↓
Policy Engine
   ↓
 ┌──────────────────────┐
 │ Low Risk             │
 │ Auto Continue        │
 └──────────┬───────────┘
            │
            ▼
      Execute Action

 ┌──────────────────────┐
 │ High Risk            │
 │ Human Approval       │
 └──────────┬───────────┘
            │
            ▼
     Human Reviewer
       ↓        ↓
    Approve    Reject
       ↓
   Execute
```

---

## 45. Default Risk Classification

```text
LOW
Read authorized content
Basic content analysis
AI content ideation

MEDIUM
CRM lead recommendation
Automated campaign analysis
AI-generated marketing copy

HIGH
Content upload
Content publishing
External-facing action
Lead creation
Automated customer-facing communication

CRITICAL
Bulk publishing
High-volume automation
Security-sensitive operations
Cross-tenant operations
Authorization changes
```

---

## 46. Bulk Automation Protection

The system shall implement bulk-operation safeguards.

```text
AI Request
    ↓
Bulk Operation Detector
    ↓
Estimate Impact
    ↓
Quota Check
    ↓
Policy Check
    ↓
Approval Threshold
    ↓
Execute in Batches
```

---

## 47. Idempotency

Publishing and workflow actions shall use idempotency keys.

```text
idempotency_key =
tenant_id
+
connection_id
+
workflow_execution_id
+
action_id
```

Repeated execution of the same workflow action shall not unintentionally create duplicate external operations.

---

## 48. Circuit Breaker

The TikTok adapter shall implement:

```text
CLOSED
   ↓
Repeated Failures
   ↓
OPEN
   ↓
Cooldown
   ↓
HALF_OPEN
   ↓
Success → CLOSED
Failure → OPEN
```

---

## 49. Quota Management

SalesGenie shall maintain provider-specific quota/rate-limit policies.

```text
Provider Limit
     ↓
Tenant Allocation
     ↓
Workflow Allocation
     ↓
Agent Allocation
     ↓
Execution
```

---

## 50. Quota-Aware AI

Before executing expensive operations, AI agents shall be able to query:

```text
Current Rate Limit
Remaining Capacity
Workflow Budget
Tenant Budget
Operation Cost
Priority
```

Example:

```text
IF rate_limit.remaining < threshold
THEN defer_noncritical_workflow
```

---

## 51. Priority Queue

TikTok workflows shall support:

```text
P0 — Security / Compliance
P1 — Customer-Critical
P2 — Sales
P3 — Marketing
P4 — Analytics
P5 — Background Enrichment
```

---

## 52. Security Requirements

The system shall protect against:

```text
OAuth Token Theft
OAuth CSRF
Credential Leakage
Cross-Tenant Data Access
Privilege Escalation
Prompt Injection
Tool Injection
Malicious Content
Unauthorized Publishing
Spam Automation
Rate-Limit Abuse
Quota Exhaustion
Data Exfiltration
Replay Attacks
Workflow Abuse
```

---

## 53. Zero-Trust Execution

Every external TikTok action shall independently validate authorization.

```text
Never Trust Previous Authorization
        ↓
Validate Current Context
        ↓
Validate Current Scope
        ↓
Validate Current Policy
        ↓
Validate Current Connection
        ↓
Execute
```

---

## 54. Integration Health States

```text
CONNECTED
AUTHORIZED
SYNCING
HEALTHY
DEGRADED
RATE_LIMITED
TOKEN_EXPIRING
REAUTH_REQUIRED
UPLOAD_FAILED
PUBLISH_FAILED
POLICY_BLOCKED
DISCONNECTED
REVOKED
ERROR
```

---

## 55. Non-Functional Requirements

## NFR-TT-001 — Availability

The TikTok integration shall target enterprise-grade availability consistent with the SalesGenie platform SLA.

---

## NFR-TT-002 — Scalability

The system shall horizontally scale:

```text
API Workers
Integration Workers
Upload Workers
Workflow Workers
AI Workers
MCP Servers
Queue Consumers
Synchronization Workers
```

---

## NFR-TT-003 — Reliability

The system shall support:

```text
Retries
Exponential Backoff
Circuit Breakers
Dead Letter Queues
Checkpointing
Idempotency
Replay
```

---

## NFR-TT-004 — Observability

All TikTok operations shall support distributed tracing.

Required fields:

```text
trace_id
span_id
tenant_id
connection_id
workflow_id
agent_id
provider_request_id
```

---

## NFR-TT-005 — Performance

The system shall minimize unnecessary TikTok API requests using:

```text
Caching
Pagination
Deduplication
Batching where supported
Asynchronous processing
Request coalescing
```

---

## NFR-TT-006 — Privacy

The system shall minimize collection and retention of personal data.

---

## NFR-TT-007 — Data Retention

Organizations shall be able to configure:

```text
Content Retention
Interaction Retention
AI Analysis Retention
Lead Retention
Audit Retention
Media Retention
```

---

## 56. TikTok Data Classification

All stored TikTok information shall have a data classification.

```text
PUBLIC
AUTHORIZED_ACCOUNT_DATA
CUSTOMER_DATA
AI_DERIVED_DATA
LEAD_DATA
RESEARCH_DATA
CREDENTIAL_DATA
AUDIT_DATA
```

Credential data must receive the highest security classification.

---

## 57. Research Data Governance

Research API data shall be logically isolated from normal commercial integrations.

```text
Commercial TikTok Data
          │
          ├── Customer Tenant
          │
          └── CRM / Workflow

Research API Data
          │
          ├── Research Project
          │
          ├── Approved Research Organization
          │
          └── Research Workspace
```

The system shall not expose Research API data to normal customer workflows unless such use is explicitly authorized and permitted by the applicable TikTok terms and product access.

TikTok currently describes Research Tools as a separately governed product with eligibility, approval, research-use requirements, and specific access controls. ([TikTok for Developers][6])

---

## 58. AI Research Workflow

For eligible approved research environments:

```text
Research Request
       ↓
Research Project Validation
       ↓
Research Credentials
       ↓
Query Validation
       ↓
Quota Validation
       ↓
TikTok Research API
       ↓
Pagination
       ↓
Normalization
       ↓
Research Dataset
       ↓
AI Analysis
       ↓
Research Report
```

---

## 59. Enterprise Workflow Template — TikTok Content Factory

```text
Campaign Created
       ↓
AI Market Analysis
       ↓
RAG Product Retrieval
       ↓
Generate 10 Concepts
       ↓
Score Concepts
       ↓
Select Top 3
       ↓
Generate Scripts
       ↓
Generate Captions
       ↓
Generate Hashtags
       ↓
Brand Safety
       ↓
Legal Safety
       ↓
Human Review
       ↓
Create Publishing Jobs
       ↓
Creator Preflight
       ↓
Upload / Direct Post
       ↓
Monitor Status
       ↓
Analytics
       ↓
AI Optimization
```

---

## 60. Enterprise Workflow Template — TikTok Lead Generation

```text
Authorized TikTok Data
       ↓
Content Retrieval
       ↓
AI Classification
       ↓
Intent Detection
       ↓
Business Relevance
       ↓
Lead Score
       ↓
Deduplication
       ↓
CRM Lookup
       ↓
 ┌─────────────────────┐
 │ Existing Lead?      │
 └─────────┬───────────┘
       YES │ NO
           │
           ▼
      Update Lead
           │
           ▼
      Create Lead
           │
           ▼
      Assign Owner
           │
           ▼
      Sales Workflow
```

---

## 61. Enterprise Workflow Template — AI Publishing Agent

```text
AI Agent
   ↓
Campaign Objective
   ↓
RAG Retrieval
   ↓
Content Generation
   ↓
Content Validation
   ↓
Brand Policy
   ↓
Safety Policy
   ↓
Human Approval
   ↓
TikTok Capability Discovery
   ↓
Creator Info Preflight
   ↓
Authorization Check
   ↓
Rate Limit Check
   ↓
Initialize Publish
   ↓
Upload
   ↓
Verify
   ↓
Audit
   ↓
Analytics
```

---

## 62. Acceptance Criteria

## AC-TT-001

An authorized user can connect a TikTok account securely.

---

## AC-TT-002

SalesGenie never exposes TikTok credentials to AI agents.

---

## AC-TT-003

The system records granted scopes and capabilities.

---

## AC-TT-004

Unauthorized API operations are rejected.

---

## AC-TT-005

Users can generate TikTok content using SalesGenie's AI.

---

## AC-TT-006

AI-generated content can be reviewed and edited by humans.

---

## AC-TT-007

Publishing cannot occur when required authorization is missing.

---

## AC-TT-008

Direct publishing retrieves and honors creator-specific options before publishing.

---

## AC-TT-009

Upload and publishing failures are recoverable.

---

## AC-TT-010

Rate limits are enforced before external API calls.

---

## AC-TT-011

AI agents cannot bypass human approval policies.

---

## AC-TT-012

TikTok-originated leads can be synchronized with SalesGenie CRM.

---

## AC-TT-013

Every AI and human action is auditable.

---

## AC-TT-014

Multiple tenants can use TikTok integrations concurrently without cross-tenant data leakage.

---

## AC-TT-015

Disconnecting TikTok stops protected API operations and dependent workflows.

---

## AC-TT-016

Research API capabilities remain isolated behind the appropriate eligibility and approval controls.

---

## 63. Reference Architecture

```text
                         ┌─────────────────────┐
                         │       TikTok        │
                         │  Developer Platform │
                         └──────────┬──────────┘
                                    │
                 ┌──────────────────┼───────────────────┐
                 │                  │                   │
                 ▼                  ▼                   ▼
            Login Kit        Content Posting       Research API
                                  API
                 │                  │                   │
                 └──────────────────┼───────────────────┘
                                    ▼
                       ┌────────────────────────┐
                       │ TikTok Integration     │
                       │ Service                │
                       └────────────┬───────────┘
                                    │
                  ┌─────────────────┼──────────────────┐
                  │                 │                  │
                  ▼                 ▼                  ▼
             Auth Layer       Capability        API Adapter
                               Registry
                  │                 │                  │
                  └─────────────────┼──────────────────┘
                                    ▼
                              Event Bus
                                    │
              ┌─────────────────────┼────────────────────┐
              │                     │                    │
              ▼                     ▼                    ▼
        Workflow Engine        AI Agent Runtime       MCP
              │                     │                    │
              │                     ▼                    │
              │               AI Safety Gateway          │
              │                     │                    │
              └─────────────────────┼────────────────────┘
                                    ▼
                          Policy / RBAC / ABAC
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
                  CRM              RAG           Analytics
                   │                │                │
                   └────────────────┼────────────────┘
                                    ▼
                             Human Approval
                                    │
                                    ▼
                              Action Executor
                                    │
                                    ▼
                                  TikTok
```

---

## 64. Core Design Principle

SalesGenie's TikTok integration shall follow:

```text
TikTok
   ↓
Integration Platform
   ↓
Authentication
   ↓
Tenant Isolation
   ↓
Capability Discovery
   ↓
Authorization
   ↓
RBAC / ABAC
   ↓
Policy Engine
   ↓
AI Safety
   ↓
Human Approval
   ↓
Quota / Rate Limit
   ↓
MCP / Workflow
   ↓
Execution
   ↓
Verification
   ↓
Audit
   ↓
Analytics
```

The platform shall support both:

```text
HUMAN → SALESGENIE → TIKTOK
```

and:

```text
AI AGENT → MCP → WORKFLOW → POLICY → TIKTOK
```

with identical enterprise security and governance boundaries.

---

## 65. Critical Implementation Constraint

SalesGenie shall implement TikTok capabilities as **provider-backed capabilities**, not assumptions.

For example:

```text
Capability Requested
        ↓
Is TikTok Product Available?
        ↓
Is SalesGenie App Approved?
        ↓
Is Required Scope Granted?
        ↓
Does User Have Permission?
        ↓
Does Organization Permit It?
        ↓
Does Workflow Permit It?
        ↓
Does AI Policy Permit It?
        ↓
Does Human Approval Apply?
        ↓
Is Rate Limit Available?
        ↓
Execute
```

This prevents SalesGenie from exposing UI buttons or AI tools for TikTok operations that the connected account, application approval, API product, OAuth scope, or current TikTok platform rules do not actually permit.

TikTok's current documentation demonstrates why this capability-gating model is necessary: Direct Post requires the `video.publish` scope and creator preflight; upload uses `video.upload`; provider limits and account/posting restrictions can block requests; and Research API access has separate eligibility requirements. ([TikTok for Developers][4])

---

## 66. Final Enterprise Requirement

The TikTok integration shall be considered production-ready only when it provides:

```text
✓ Multi-Tenant Isolation
✓ Secure OAuth
✓ Least-Privilege Scopes
✓ RBAC
✓ ABAC
✓ Capability Registry
✓ MCP Integration
✓ AI Agent Integration
✓ Human-in-the-Loop
✓ AI Safety Gateway
✓ Content Generation
✓ Content Analysis
✓ Upload Pipeline
✓ Direct Publishing
✓ Creator Preflight
✓ Publishing State Machine
✓ Lead Generation
✓ CRM Synchronization
✓ Workflow Automation
✓ Scheduling
✓ Quota / Rate-Limit Management
✓ Idempotency
✓ Retry / Backoff
✓ Circuit Breaker
✓ Dead-Letter Queue
✓ Synchronization Engine
✓ Observability
✓ Distributed Tracing
✓ Audit Logging
✓ Data Classification
✓ Data Retention
✓ Research Data Isolation
✓ Policy Enforcement
✓ Human Override
✓ Disaster Recovery
✓ Provider Capability Validation
```

The resulting integration must function as a first-class component of the SalesGenie multi-agent enterprise automation platform rather than as a thin TikTok API wrapper.
