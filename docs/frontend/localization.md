# SalesGenie Localization Requirements

## 1. Document Purpose

This document defines the FAANG-level user requirements, system requirements, and functional requirements for the **SalesGenie Localization Platform**.

The localization architecture shall enable SalesGenie to adapt its product experience to different:

* Languages
* Countries
* Regions
* Locales
* Time zones
* Currencies
* Number formats
* Date/time formats
* Calendars
* Measurement systems
* Address formats
* Phone-number formats
* Tax conventions
* Business conventions
* Cultural conventions
* Writing systems
* Text directions
* Regulatory requirements

Localization shall be implemented as a cross-platform capability affecting the frontend, backend, APIs, databases, AI systems, analytics, reporting, billing, notifications, integrations, workflows, customer portal, administration, and developer platform.

---

## 2. Localization Goals

SalesGenie localization shall provide:

1. Complete multilingual user experiences.
2. Locale-aware formatting.
3. Country-aware business behavior.
4. Regional configuration.
5. RTL and bidirectional language support.
6. Translation management.
7. Human translation workflows.
8. AI-assisted translation workflows.
9. Human review of AI-generated translations.
10. Translation versioning.
11. Translation approval workflows.
12. Locale-specific content management.
13. Backend-driven localization.
14. Tenant-level localization.
15. Organization-level localization.
16. Workplace-level localization.
17. User-level localization.
18. API localization.
19. AI-agent localization.
20. Localized reports and exports.
21. Localized notifications.
22. Localized billing.
23. Localized analytics.
24. Localized customer support.
25. Localized documentation.
26. Locale-aware search and sorting.
27. Locale-aware validation.
28. Localization observability.
29. Localization testing.
30. Safe fallback behavior.

---

## 3. Supported Localization Dimensions

SalesGenie shall support localization across:

```text
Language
   │
   ├── Language Code
   ├── Script
   ├── Dialect
   └── Translation

Locale
   │
   ├── Language
   ├── Country
   ├── Region
   └── Cultural Convention

Regional Configuration
   │
   ├── Currency
   ├── Time Zone
   ├── Calendar
   ├── Number Format
   ├── Date Format
   ├── Address Format
   ├── Phone Format
   ├── Measurement System
   └── Tax Rules

Presentation
   │
   ├── Text Direction
   ├── Fonts
   ├── Layout
   ├── Images
   ├── Icons
   └── Content

Business Logic
   │
   ├── Billing
   ├── Tax
   ├── Payments
   ├── Compliance
   ├── Notifications
   └── Reporting
```

---

## 4. Localization Actors

## 4.1 End User

The end user shall be able to:

* Select a preferred language.
* Select a preferred locale.
* Select a preferred time zone.
* Select a preferred currency where permitted.
* Select regional formatting preferences.
* Switch languages without losing application state.
* Use localized dashboards.
* Use localized reports.
* Receive localized notifications.
* Use localized AI agents.
* Enter localized customer data.

---

## 4.2 External Client

The external client shall be able to:

* Configure organization localization.
* Configure workspace localization.
* Configure supported languages.
* Configure regional preferences.
* Configure client-facing terminology.
* Configure localized customer portals.
* Configure localized reports.
* Configure localized notifications.
* Review AI-generated translations.
* Approve translations.
* Configure market-specific content.

---

## 4.3 Organization Owner

The Organization Owner shall be able to:

* Set organization default language.
* Set organization default locale.
* Set organization default time zone.
* Set organization default currency.
* Configure allowed languages.
* Configure regional policies.
* Override defaults for individual workplaces.
* View localization usage.
* Manage localization permissions.

---

## 4.4 Workplace Administrator

The Workplace Administrator shall be able to:

* Configure workplace language.
* Configure workplace locale.
* Configure workplace time zone.
* Configure workplace currency.
* Configure regional formatting.
* Configure localized workflows.
* Configure localized notifications.
* Configure localized dashboards.

---

## 4.5 Administrator

Administrators shall be able to:

* Add languages.
* Disable languages.
* Configure locales.
* Manage translation catalogs.
* Manage translation versions.
* Approve translations.
* Reject translations.
* Monitor missing translations.
* Monitor translation failures.
* Configure fallback policies.
* Manage localization providers.

---

## 4.6 Localization Manager

The Localization Manager shall be able to:

* Manage translation projects.
* Assign translators.
* Assign reviewers.
* Manage terminology.
* Manage translation memory.
* Approve translations.
* Reject translations.
* Track translation completeness.
* Track translation quality.
* Manage localization releases.

---

## 4.7 Translator

The Translator shall be able to:

* View translation tasks.
* Translate strings.
* View source context.
* View screenshots.
* View variable definitions.
* View terminology guidance.
* Submit translations.
* Request clarification.
* Save drafts.
* Submit translations for review.

---

## 4.8 Localization Reviewer

The Reviewer shall be able to:

* Review translations.
* Compare source and target text.
* Approve translations.
* Reject translations.
* Request modifications.
* Report linguistic issues.
* Report cultural issues.
* Report formatting issues.

---

## 4.9 AI Agent

AI agents shall be able to:

* Detect user language.
* Detect locale.
* Generate localized responses.
* Translate content.
* Localize content.
* Preserve structured variables.
* Respect terminology.
* Respect organization-specific terminology.
* Escalate uncertain translations to humans.

---

## 4.10 AI Localization Agent

The AI Localization Agent shall be able to:

* Translate source strings.
* Generate translation suggestions.
* Detect missing translations.
* Detect inconsistent terminology.
* Detect untranslated strings.
* Detect placeholder mismatches.
* Detect potentially harmful translations.
* Detect cultural inconsistencies.
* Recommend translation improvements.
* Generate translation-quality reports.

---

## 5. User Requirements

## UR-LOC-001 — Language Selection

The system shall allow users to select their preferred application language.

---

## UR-LOC-002 — Automatic Language Detection

The system shall optionally detect the user's preferred language from:

* Browser language.
* Operating-system language.
* Existing account preference.
* Organization preference.
* Workspace preference.
* URL locale.
* Authentication context.

---

## UR-LOC-003 — Explicit User Preference

Explicit user language preferences shall take precedence over automatically detected language preferences.

---

## UR-LOC-004 — Locale Selection

Users shall be able to select a locale independently from language when required.

Example:

```text
Language: English
Locale: Bangladesh
```

or:

```text
Language: English
Locale: United States
```

---

## UR-LOC-005 — Time Zone

Users shall be able to configure their preferred time zone.

---

## UR-LOC-006 — Currency

Users shall be able to view monetary values using the applicable currency based on organization, billing, transaction, or display context.

---

## UR-LOC-007 — Number Formatting

Users shall receive locale-aware number formatting.

---

## UR-LOC-008 — Date Formatting

Users shall receive locale-aware date formatting.

---

## UR-LOC-009 — Time Formatting

Users shall receive locale-aware time formatting.

---

## UR-LOC-010 — Calendar Support

The platform shall support locale-specific calendar presentation where required.

---

## UR-LOC-011 — RTL Support

The platform shall support right-to-left languages.

Examples include:

* Arabic
* Hebrew
* Persian
* Urdu

---

## UR-LOC-012 — Mixed-Direction Content

Users shall be able to work with mixed-language content containing:

* Names
* URLs
* Email addresses
* Phone numbers
* IDs
* Product codes
* Technical terms
* Numbers

---

## UR-LOC-013 — Localized Dashboard

Users shall receive localized:

* Navigation
* Dashboards
* Widgets
* Charts
* Tables
* Filters
* Buttons
* Tooltips
* Forms
* Errors
* Notifications

---

## UR-LOC-014 — Localized AI

Users shall be able to communicate with SalesGenie AI agents in supported languages.

---

## UR-LOC-015 — AI Language Continuity

AI agents shall preserve the user's preferred language throughout a conversation unless explicitly requested otherwise.

---

## UR-LOC-016 — Human Handoff Localization

When an AI agent escalates to a human agent, the system shall preserve:

* Conversation language.
* Locale.
* Translation context.
* User language.
* Conversation history.
* Translation metadata.

---

## UR-LOC-017 — Localized Support

Customer support workflows shall support localized:

* Tickets
* Messages
* Templates
* Knowledge-base articles
* Notifications
* SLA communications

---

## UR-LOC-018 — Localized Sales

Sales workflows shall support localized:

* Lead information
* Contact information
* Outreach templates
* Email content
* Sales sequences
* Pipeline labels
* CRM fields
* Customer communications

---

## UR-LOC-019 — Localized Marketing

Marketing workflows shall support:

* Localized campaigns.
* Localized content.
* Localized email.
* Localized social media content.
* Localized advertisements.
* Localized audience segmentation.
* Localized customer messaging.

---

## UR-LOC-020 — Localized SEO

SEO workflows shall support:

* Language-specific keywords.
* Locale-specific keywords.
* Local SERPs.
* Local search intent.
* Localized metadata.
* Localized content.
* Localized URLs.
* Regional ranking data.

---

## UR-LOC-021 — Localized Reports

Users shall be able to generate localized:

* Sales reports.
* Marketing reports.
* Financial reports.
* SEO reports.
* Advertising reports.
* Executive reports.
* AI reports.

---

## UR-LOC-022 — Localized Excel Exports

Excel exports shall support:

* Localized column names.
* Locale-aware numbers.
* Locale-aware dates.
* Locale-aware currencies.
* Localized report titles.

---

## UR-LOC-023 — Localized Notifications

The platform shall send localized:

* Email notifications.
* SMS notifications.
* Push notifications.
* In-app notifications.
* System alerts.
* Security alerts.
* Billing notifications.

---

## UR-LOC-024 — Localized Billing

Billing interfaces shall support:

* Localized currency display.
* Localized invoices.
* Localized tax information.
* Localized payment descriptions.
* Localized billing notifications.

---

## UR-LOC-025 — Localized Customer Portal

External clients shall receive a localized customer portal.

---

## UR-LOC-026 — Translation Context

Translators shall receive contextual information for each translatable string.

---

## UR-LOC-027 — Translation Preview

Translators and reviewers shall be able to preview translations in their actual UI context.

---

## UR-LOC-028 — Translation Quality

Users shall receive translations that meet configured quality thresholds.

---

## UR-LOC-029 — Human Review

AI-generated translations shall be reviewable by authorized humans before production publication when configured as mandatory.

---

## UR-LOC-030 — Localization Fallback

If a translation is unavailable, the system shall use a configured fallback language.

---

## 6. System Requirements

## SR-LOC-001 — Unicode

All localization-sensitive systems shall support Unicode end-to-end.

This includes:

* Database
* APIs
* Queues
* Event bus
* Object storage
* Search
* Logging
* Analytics
* AI systems
* Frontend

---

## SR-LOC-002 — Canonical Data

The system shall store canonical business data independently from presentation localization.

Example:

```text
Canonical:
amount = 1250.50
currency = USD

Presentation:
$1,250.50
```

The localized representation shall never replace the canonical business value.

---

## SR-LOC-003 — Locale Model

The backend shall maintain a first-class locale model.

Example:

```text
Locale
├── id
├── language_code
├── country_code
├── script_code
├── locale_code
├── direction
├── currency
├── timezone
├── calendar
├── number_system
├── date_format
├── time_format
├── enabled
└── metadata
```

---

## SR-LOC-004 — Language Registry

The system shall maintain a centralized language registry.

---

## SR-LOC-005 — Locale Registry

The system shall maintain a centralized locale registry.

---

## SR-LOC-006 — Translation Catalog

All user-facing strings shall be stored in translation catalogs or equivalent localization resources.

---

## SR-LOC-007 — Stable Translation Keys

Translation keys shall be semantic and stable.

Example:

```text
dashboard.sales.revenue.title
```

The English sentence shall not be used as the translation key.

---

## SR-LOC-008 — Translation Variables

Translation resources shall support structured variables.

Example:

```text
sales.leads.count =
"You have {count, plural,
  =0 {no leads}
  one {# lead}
  other {# leads}
}"
```

---

## SR-LOC-009 — Placeholder Validation

The platform shall validate:

* Missing variables.
* Extra variables.
* Invalid variable names.
* Invalid plural branches.
* Invalid select branches.

---

## SR-LOC-010 — Translation Versioning

Every translation shall support:

* Version.
* Author.
* Reviewer.
* Timestamp.
* Status.
* Source version.
* Target locale.
* Change history.

---

## SR-LOC-011 — Translation Status

Translation resources shall support statuses such as:

```text
DRAFT
IN_TRANSLATION
TRANSLATED
IN_REVIEW
APPROVED
REJECTED
PUBLISHED
DEPRECATED
```

---

## SR-LOC-012 — Translation Fallback

The backend shall provide deterministic fallback resolution.

Example:

```text
User Locale
    ↓
Requested Locale
    ↓
Language + Region
    ↓
Language
    ↓
Organization Default
    ↓
System Default
```

---

## SR-LOC-013 — Locale Negotiation

The system shall implement deterministic locale negotiation.

---

## SR-LOC-014 — Locale Persistence

The selected locale shall be persisted according to the applicable scope:

```text
User
   ↓
Workplace
   ↓
Organization
   ↓
Platform
```

---

## SR-LOC-015 — Locale Precedence

The system shall support configurable precedence rules.

Default:

```text
Explicit User Preference
        >
Workspace Preference
        >
Organization Preference
        >
Browser Preference
        >
Platform Default
```

---

## SR-LOC-016 — Backend Localization API

The backend shall expose localization APIs.

Example:

```http
GET /api/v1/localization/languages
GET /api/v1/localization/locales
GET /api/v1/localization/preferences
PUT /api/v1/localization/preferences
GET /api/v1/localization/messages
GET /api/v1/localization/catalogs
POST /api/v1/localization/translations
PUT /api/v1/localization/translations/{id}
POST /api/v1/localization/translations/{id}/approve
POST /api/v1/localization/translations/{id}/publish
```

---

## SR-LOC-017 — Tenant Isolation

Localization configuration shall be tenant-aware.

Tenant-specific configuration shall never leak between organizations.

---

## SR-LOC-018 — Organization Localization

Organizations shall have localization configuration independent of other organizations.

---

## SR-LOC-019 — Workplace Localization

Workplaces shall be able to inherit or override organization localization configuration.

---

## SR-LOC-020 — User Localization

Users shall be able to inherit or override workplace localization configuration.

---

## SR-LOC-021 — Locale-Aware API

API responses shall support locale-aware presentation where explicitly requested.

Canonical machine-readable values shall remain stable.

---

## SR-LOC-022 — Locale Headers

The platform shall support standardized locale negotiation through mechanisms such as:

```text
Accept-Language
Content-Language
```

---

## SR-LOC-023 — Locale-Aware Error Messages

API and application errors shall support localized human-readable messages while retaining stable machine-readable error codes.

Example:

```json
{
  "code": "LEAD_NOT_FOUND",
  "message": "Lead not found",
  "locale": "en-US"
}
```

---

## SR-LOC-024 — Stable Error Codes

Business logic shall never depend on localized error messages.

---

## SR-LOC-025 — Localization Cache

Frequently accessed translation resources shall be cached.

---

## SR-LOC-026 — Cache Invalidation

Published translation changes shall invalidate relevant caches.

---

## SR-LOC-027 — CDN Localization

Static localization resources shall support CDN delivery where appropriate.

---

## SR-LOC-028 — Locale-Aware Search

Search shall support:

* Unicode.
* Locale-aware tokenization.
* Locale-aware sorting.
* Diacritics.
* Language-specific normalization.
* Language-specific analyzers where required.

---

## SR-LOC-029 — Locale-Aware Sorting

The system shall use locale-aware collation rather than assuming ASCII ordering.

---

## SR-LOC-030 — Locale-Aware Case Handling

Case conversion shall use locale-aware mechanisms where required.

---

## SR-LOC-031 — Text Normalization

The system shall define an explicit Unicode normalization policy.

---

## SR-LOC-032 — Font Support

The frontend shall provide appropriate font coverage for supported scripts.

---

## SR-LOC-033 — RTL Architecture

The frontend shall support:

```text
LTR
RTL
Mixed Direction
```

---

## SR-LOC-034 — CSS Logical Properties

The frontend shall use logical layout properties where possible.

Examples:

```css
margin-inline-start
margin-inline-end
padding-inline
inset-inline-start
inset-inline-end
border-inline-start
border-inline-end
```

---

## SR-LOC-035 — Responsive Localization

The UI shall support:

* Text expansion.
* Text contraction.
* Long words.
* Long labels.
* Multi-line labels.
* Different writing systems.
* RTL layouts.

---

## 7. Functional Requirements

## FR-LOC-001 — Language Management

The system shall allow authorized administrators to:

* Create languages.
* Enable languages.
* Disable languages.
* Configure language metadata.
* Configure language display names.
* Configure fallback languages.

---

## FR-LOC-002 — Locale Management

The system shall allow authorized administrators to:

* Create locales.
* Enable locales.
* Disable locales.
* Configure locale metadata.
* Configure locale fallback.
* Configure regional formatting.

---

## FR-LOC-003 — Translation Catalog Management

The system shall allow authorized users to:

* Create catalogs.
* Import catalogs.
* Export catalogs.
* Edit catalogs.
* Version catalogs.
* Publish catalogs.
* Roll back catalogs.

---

## FR-LOC-004 — Translation Management

The system shall provide CRUD functionality for translations.

---

## FR-LOC-005 — Translation Workflow

The translation workflow shall support:

```text
SOURCE STRING
     ↓
EXTRACTION
     ↓
TRANSLATION
     ↓
AI ASSISTANCE
     ↓
HUMAN REVIEW
     ↓
APPROVAL
     ↓
QA
     ↓
PUBLISH
     ↓
CACHE INVALIDATION
     ↓
PRODUCTION
```

---

## FR-LOC-006 — AI Translation

The AI localization engine shall generate translation suggestions.

---

## FR-LOC-007 — AI Translation Confidence

Each AI-generated translation shall optionally receive a confidence score.

---

## FR-LOC-008 — Human Translation Override

Humans shall be able to override AI-generated translations.

---

## FR-LOC-009 — AI Translation Review

The system shall support:

```text
AI Generated
      ↓
Confidence Evaluation
      ↓
 ┌────┴────┐
High      Low
 ↓         ↓
Auto      Human
Review    Review
```

---

## FR-LOC-010 — Terminology Management

The system shall maintain a terminology database containing:

* Preferred terms.
* Forbidden terms.
* Acronyms.
* Product names.
* Brand terms.
* Technical terminology.
* Industry terminology.
* Tenant-specific terminology.

---

## FR-LOC-011 — Translation Memory

The system shall support translation memory.

---

## FR-LOC-012 — Translation Reuse

Previously approved translations shall be reusable when source content matches or closely corresponds.

---

## FR-LOC-013 — Translation Similarity

The AI system may recommend similar existing translations.

---

## FR-LOC-014 — Translation Quality Checks

The system shall automatically detect:

* Placeholder changes.
* Missing placeholders.
* HTML changes.
* Markdown changes.
* Broken links.
* Unexpected terminology.
* Missing translations.
* Excessive length.
* Suspicious characters.
* Unsupported scripts.

---

## FR-LOC-015 — Missing Translation Detection

The system shall detect missing translation keys across all enabled locales.

---

## FR-LOC-016 — Translation Completeness

The platform shall calculate:

```text
Translation Completeness =
Translated Required Strings
/
Total Required Strings
× 100
```

---

## FR-LOC-017 — Localization Dashboard

Administrators shall receive localization dashboards containing:

* Translation completion.
* Translation backlog.
* Missing keys.
* Failed translations.
* Pending reviews.
* Translation quality.
* Locale adoption.
* Locale usage.
* Translation errors.

---

## FR-LOC-018 — Locale Analytics

The analytics platform shall track:

* Users by language.
* Users by locale.
* Sessions by language.
* Conversion by locale.
* Retention by locale.
* Feature usage by locale.
* AI usage by locale.
* Support volume by locale.

---

## FR-LOC-019 — Locale-Based Product Analytics

SalesGenie shall allow product teams to compare product performance across locales.

---

## FR-LOC-020 — Localized AI Agents

AI agents shall consume:

```text
User Locale
+
Organization Locale
+
Conversation Locale
+
Knowledge Base Locale
+
Agent Language Policy
```

when generating responses.

---

## FR-LOC-021 — AI Language Detection

AI systems shall detect the language of incoming user messages.

---

## FR-LOC-022 — AI Language Switching

AI agents shall support user-requested language switching during a conversation.

---

## FR-LOC-023 — Multilingual RAG

RAG shall support multilingual:

* Documents.
* Embeddings.
* Queries.
* Retrieval.
* Ranking.
* Answers.

---

## FR-LOC-024 — Multilingual Knowledge Base

Knowledge-base documents shall support language metadata.

Example:

```text
Document
├── id
├── organization_id
├── language
├── locale
├── title
├── content
└── version
```

---

## FR-LOC-025 — Localized RAG Retrieval

The retrieval engine shall prioritize content matching the user's language and locale where configured.

---

## FR-LOC-026 — Multilingual Lead Generation

Lead-generation workflows shall support multilingual:

* Company names.
* Person names.
* Job titles.
* Company descriptions.
* Search queries.
* Lead enrichment.
* Lead summaries.
* Outreach content.

---

## FR-LOC-027 — Multilingual Sales Outreach

SalesGenie shall generate localized:

* Emails.
* Messages.
* Follow-ups.
* Sales sequences.
* Proposals.
* Outreach templates.

---

## FR-LOC-028 — Multilingual Marketing

Marketing agents shall generate localized:

* Campaigns.
* Ads.
* Social posts.
* Blog content.
* Email campaigns.
* Landing-page content.

---

## FR-LOC-029 — Localized SEO

SEO agents shall generate:

* Localized keywords.
* Localized titles.
* Localized descriptions.
* Localized content.
* Localized schema.
* Localized URLs.

---

## FR-LOC-030 — Localized Product Launch Intelligence

Product launch intelligence shall support market-specific:

* Market research.
* Competitor analysis.
* Buyer analysis.
* Pricing analysis.
* Positioning.
* GTM recommendations.

---

## FR-LOC-031 — Localized Advertising Intelligence

Advertising analytics shall support locale and market segmentation across:

* Google Ads.
* Facebook Ads.
* Instagram Ads.
* LinkedIn Ads.
* TikTok Ads.
* YouTube Ads.
* WhatsApp campaigns.

---

## FR-LOC-032 — Localized Financial Analytics

Financial analytics shall preserve canonical financial values while displaying:

* Local currency.
* Local number formatting.
* Local dates.
* Local tax representations.

---

## FR-LOC-033 — Currency Conversion

If currency conversion is enabled, the system shall maintain:

* Source currency.
* Target currency.
* Exchange rate.
* Exchange-rate timestamp.
* Conversion source.
* Conversion methodology.

---

## FR-LOC-034 — Currency Integrity

The system shall never overwrite original transaction currency solely because a user changes their display locale.

---

## FR-LOC-035 — Localized Reports

Report generation shall support locale-specific presentation.

---

## FR-LOC-036 — Localized Charts

Charts shall support:

* Localized labels.
* Localized legends.
* Locale-aware numbers.
* Locale-aware dates.
* Locale-aware currencies.
* RTL rendering where applicable.

---

## FR-LOC-037 — Localized Exports

Exports shall support:

```text
XLSX
CSV
PDF
JSON
```

with locale-aware presentation.

---

## FR-LOC-038 — Localized Notifications

Notification templates shall be selected using:

```text
Notification Type
+
User Locale
+
Organization Locale
+
Channel
```

---

## FR-LOC-039 — Notification Fallback

If the target translation is unavailable, notification delivery shall use the configured fallback locale.

---

## FR-LOC-040 — Localized Email Templates

Email templates shall support localized variants.

---

## FR-LOC-041 — Localized SMS Templates

SMS templates shall support localized variants.

---

## FR-LOC-042 — Localized Push Notifications

Push notifications shall support localized titles, bodies, and actions.

---

## FR-LOC-043 — Localized Workflow Automation

Workflow nodes shall support localized:

* Messages.
* Emails.
* Notifications.
* AI prompts.
* Customer-facing content.

---

## FR-LOC-044 — Localization-Aware Workflow Execution

Workflow execution shall resolve locale at runtime based on the target user, customer, organization, or workflow configuration.

---

## FR-LOC-045 — Localized CRM

CRM fields shall support:

* Localized labels.
* Localized descriptions.
* Locale-aware values.
* Localized templates.

---

## FR-LOC-046 — Localized Customer Support

Support agents shall be able to:

* View customer language.
* View customer locale.
* Translate conversations.
* Respond in the customer's language.
* Request AI translation.
* Compare original and translated messages.

---

## FR-LOC-047 — Real-Time Translation

The platform shall optionally support real-time translation for:

* Chat.
* Support.
* Sales.
* Collaboration.
* Omnichannel communication.

---

## FR-LOC-048 — Translation Audit Trail

All translation changes shall be auditable.

Audit records shall contain:

```text
actor_id
organization_id
locale
translation_key
old_value
new_value
action
timestamp
source
approval_status
```

---

## FR-LOC-049 — Localization Permissions

Localization functionality shall integrate with RBAC and ABAC.

Example permissions:

```text
localization.read
localization.create
localization.update
localization.delete
localization.translate
localization.review
localization.approve
localization.publish
localization.configure
```

---

## FR-LOC-050 — Localization API Authorization

Localization APIs shall enforce tenant and role permissions.

---

## 8. Backend Integration Requirements

## Backend Integration Architecture

```text
                    FRONTEND
                       │
                       ▼
              LOCALE CONTEXT
                       │
                       ▼
                API GATEWAY
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 Localization      User Service    Organization
   Service                          Service
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                 LOCALE ENGINE
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Translation   Formatting    Regional
       Service       Service       Rules
          │            │            │
          └────────────┼────────────┘
                       ▼
                 CACHE / REDIS
                       │
                       ▼
             LOCALIZATION DATABASE
```

---

## 9. Backend Services

The architecture should provide dedicated localization capabilities through services such as:

```text
Localization Service
Translation Service
Locale Service
Language Service
Formatting Service
Translation Memory Service
Terminology Service
Localization QA Service
Localization Analytics Service
AI Translation Service
```

These services may be implemented as independent microservices or modular components depending on deployment architecture.

---

## 10. Localization Service Requirements

The Localization Service shall manage:

* Languages.
* Locales.
* Translation catalogs.
* Translation keys.
* Translation versions.
* Locale configuration.
* Fallback rules.
* Publishing.
* Localization metadata.

---

## 11. Translation Service Requirements

The Translation Service shall manage:

* Translation creation.
* Translation updates.
* Translation review.
* Translation approval.
* Translation publication.
* Translation rollback.
* Translation history.

---

## 12. Formatting Service Requirements

The Formatting Service shall provide standardized formatting for:

```text
Numbers
Currencies
Dates
Times
Durations
Percentages
Units
Lists
Relative times
Addresses
Phone numbers
```

---

## 13. Locale Resolution Engine

The locale resolution engine shall resolve locale using:

```text
Request Locale
      ↓
Authenticated User Locale
      ↓
Workspace Locale
      ↓
Organization Locale
      ↓
Browser Locale
      ↓
Platform Default
```

---

## 14. Database Requirements

The database shall support tables/entities such as:

```text
languages
locales
locale_preferences
translation_namespaces
translation_keys
translations
translation_versions
translation_reviews
translation_terminology
translation_memory
localization_projects
localization_tasks
localization_releases
localization_audit_logs
```

---

## 15. Suggested Translation Schema

```text
translation_key
----------------
id
namespace
key
description
source_text
source_locale
context
variables
status
created_at
updated_at
```

```text
translation
------------
id
translation_key_id
locale_id
translated_text
version
status
translator_id
reviewer_id
created_at
updated_at
published_at
```

---

## 16. API Requirements

Localization APIs shall support:

```text
Language APIs
Locale APIs
Preference APIs
Translation APIs
Catalog APIs
Terminology APIs
Translation Memory APIs
Review APIs
Approval APIs
Publishing APIs
Analytics APIs
```

---

## 17. Frontend Integration Requirements

The frontend shall obtain localization configuration from backend services where configuration is dynamic.

The frontend shall integrate localization with:

* Authentication.
* User profile.
* Organization settings.
* Workplace settings.
* Dashboard.
* Navigation.
* Forms.
* Tables.
* Charts.
* Search.
* Notifications.
* Billing.
* Reports.
* AI interfaces.
* Agent interfaces.
* Workflow builder.
* CRM.
* Support.
* Customer portal.

---

## 18. Frontend Locale Context

The frontend shall maintain a centralized locale context:

```text
LocaleContext
├── language
├── locale
├── timezone
├── currency
├── direction
├── calendar
├── numberSystem
├── messages
└── formattingRules
```

---

## 19. Dynamic Locale Switching

Changing language shall:

1. Update user preference.
2. Update frontend locale state.
3. Fetch required translation resources.
4. Update text.
5. Update direction.
6. Update formatting.
7. Update date/time display.
8. Update currency presentation where applicable.
9. Preserve navigation state.
10. Avoid unnecessary page reloads.

---

## 20. RTL Requirements

RTL support shall include:

* Layout mirroring.
* Navigation mirroring.
* Sidebar behavior.
* Dialog alignment.
* Form alignment.
* Table alignment.
* Text alignment.
* Icon handling.
* Tooltip placement.
* Chart rendering.
* Keyboard navigation.
* Focus order.
* Mixed-direction content.

---

## 21. Localization of AI Prompts

AI prompts shall support locale variables.

Example:

```text
SYSTEM:
Respond using the user's preferred language.

USER_LOCALE:
{{user.locale}}

LANGUAGE:
{{user.language}}

TIMEZONE:
{{user.timezone}}

CURRENCY:
{{user.currency}}
```

---

## 22. AI Localization Requirements

AI localization shall support:

```text
Language Detection
Translation
Transcreation
Terminology Enforcement
Cultural Adaptation
Tone Adaptation
Locale Formatting
Translation Quality Evaluation
Translation Confidence
Human Escalation
```

---

## 23. AI + Human Localization Workflow

```text
SOURCE CONTENT
      │
      ▼
AI TRANSLATION
      │
      ▼
QUALITY CHECK
      │
      ├── HIGH CONFIDENCE
      │        │
      │        ▼
      │     AUTO APPROVAL
      │
      └── LOW/MEDIUM CONFIDENCE
               │
               ▼
          HUMAN REVIEW
               │
         ┌─────┴─────┐
         ▼           ▼
      APPROVE       REJECT
         │           │
         │           ▼
         │       AI/HUMAN
         │       REVISION
         │           │
         └───────────┘
               │
               ▼
           QA CHECK
               │
               ▼
            PUBLISH
```

---

## 24. Localization Security Requirements

Localization resources shall be protected against:

* Tenant data leakage.
* Unauthorized translation access.
* Unauthorized publishing.
* Prompt injection through translation content.
* Malicious translation payloads.
* XSS through translated HTML.
* Template injection.
* Variable injection.
* Unauthorized locale configuration.
* Cross-tenant catalog access.

---

## 25. Translation Content Security

User-provided translated content shall be treated as untrusted input.

The system shall sanitize:

* HTML.
* Markdown.
* Links.
* Embedded content.
* Dynamic variables.
* Rich-text content.

---

## 26. Localization Observability

The observability platform shall track:

```text
missing_translation
fallback_translation
translation_error
locale_resolution_failure
formatter_error
unsupported_locale
translation_latency
catalog_load_latency
translation_cache_hit
translation_cache_miss
ai_translation_failure
human_review_latency
translation_publish_failure
```

---

## 27. Localization Metrics

The platform shall provide:

```text
Translation Coverage
Translation Completion Rate
Translation Error Rate
Fallback Rate
Locale Adoption
Locale Retention
Translation Review Time
AI Translation Acceptance Rate
AI Translation Rejection Rate
Translation Cache Hit Rate
Localization API Latency
Locale Resolution Latency
```

---

## 28. Localization Alerts

The alerting system shall trigger alerts for:

* Sudden fallback spikes.
* Missing critical translations.
* Translation service failures.
* Locale API failures.
* Translation cache failures.
* Catalog corruption.
* Invalid translation deployments.
* Large translation-quality degradation.

---

## 29. Localization Testing

The system shall support:

## Unit Tests

Test:

* Locale resolution.
* Translation lookup.
* Formatting.
* Pluralization.
* Variable interpolation.
* Fallback logic.

## Integration Tests

Test:

* Frontend/backend localization.
* Translation APIs.
* Locale persistence.
* Translation publishing.
* Cache invalidation.

## E2E Tests

Test:

* Language switching.
* RTL workflows.
* Localized authentication.
* Localized billing.
* Localized AI.
* Localized support.
* Localized reports.

## Pseudolocalization

The system shall support pseudo-locales for detecting:

* Text expansion.
* Text contraction.
* Unicode issues.
* Layout overflow.
* RTL issues.
* Hardcoded strings.

---

## 30. Localization Release Management

Localization releases shall support:

```text
Draft
   ↓
Validation
   ↓
QA
   ↓
Approval
   ↓
Staging
   ↓
Canary
   ↓
Production
```

---

## 31. Localization Rollback

Administrators shall be able to roll back a localization release without rolling back unrelated application functionality.

---

## 32. Feature Flags

Localization features shall support feature flags for:

* New languages.
* New locales.
* Experimental translations.
* AI translation.
* Automatic translation.
* RTL support.
* Regional features.

---

## 33. Localization Data Governance

The platform shall maintain:

* Translation ownership.
* Translation provenance.
* Translation history.
* Translation retention.
* Translation approval history.
* Translation deletion policies.

---

## 34. Internationalized Business Data

The system shall distinguish between:

```text
Canonical Business Data
        +
Localized Presentation
        +
Regional Business Rules
```

Example:

```text
Canonical Transaction
---------------------
amount = 1000.00
currency = USD
timestamp = UTC

Localized Presentation
----------------------
$1,000.00
Aug 30, 2026
09:30 AM

Regional Business Rules
-----------------------
Tax
Payment Method
Invoice Format
Legal Requirements
```

---

## 35. Address Localization

The platform shall support country-specific:

* Address field ordering.
* Postal-code formats.
* Administrative regions.
* City formats.
* State/province formats.
* Country names.

---

## 36. Phone Localization

The platform shall support:

* International phone numbers.
* Country codes.
* Regional display formats.
* Phone validation.
* E.164-compatible canonical storage.
* Localized presentation.

---

## 37. Measurement Localization

The system shall support:

* Metric.
* Imperial.
* Locale-specific measurement conventions.

Canonical values shall remain independent from presentation units.

---

## 38. Date and Time Requirements

The system shall store timestamps in a canonical representation and convert them for presentation according to the relevant time zone.

The system shall support:

* Time zones.
* Daylight-saving transitions.
* Locale-specific dates.
* Relative time.
* Date ranges.
* Recurring schedules.

---

## 39. Billing Localization

Billing shall integrate localization with:

```text
Subscription
      ↓
Pricing
      ↓
Currency
      ↓
Tax
      ↓
Invoice
      ↓
Payment
      ↓
Receipt
      ↓
Notification
```

Canonical financial records shall remain independent of display localization.

---

## 40. Localization and RBAC

Localization permissions shall integrate with SalesGenie's existing roles, including:

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

Role permissions shall determine whether the user can:

* View localization configuration.
* Modify localization configuration.
* Translate.
* Review.
* Approve.
* Publish.
* Configure locale defaults.

---

## 41. Localization and Multi-Tenancy

The system shall enforce:

```text
Platform Localization
        │
        ├── Organization A
        │      ├── Workplace A1
        │      └── Workplace A2
        │
        ├── Organization B
        │      ├── Workplace B1
        │      └── Workplace B2
        │
        └── Organization C
```

Localization data belonging to one organization shall never be accessible to another organization unless explicitly shared through an authorized global resource.

---

## 42. Localization and Search

Search shall support:

* Unicode.
* Multilingual queries.
* Locale-aware ranking.
* Locale-aware sorting.
* Transliteration where explicitly configured.
* Diacritics.
* Language-specific tokenization.

---

## 43. Localization and Analytics

Analytics events shall retain canonical event semantics.

Example:

```json
{
  "event": "lead_created",
  "user_id": "...",
  "organization_id": "...",
  "locale": "en-BD",
  "language": "en",
  "timezone": "Asia/Dhaka"
}
```

Localized display labels shall not replace stable event names.

---

## 44. Localization and Data Warehouse

The data warehouse shall store canonical analytical dimensions separately from localized presentation dimensions.

---

## 45. Localization and Notifications

Notification delivery shall resolve:

```text
Recipient
   ↓
Preferred Language
   ↓
Locale
   ↓
Notification Template
   ↓
Channel
   ↓
Localized Message
   ↓
Delivery
```

---

## 46. Localization and Omnichannel

Every communication channel shall support localization:

```text
Web Chat
Email
WhatsApp
Facebook Messenger
Instagram
Telegram
SMS
Voice
Social Inbox
```

---

## 47. Localization and Voice AI

Voice systems shall support, where available:

* Language selection.
* Locale-specific speech recognition.
* Locale-specific text-to-speech.
* Voice selection.
* Pronunciation metadata.
* Regional accents.
* Language-aware fallback.

---

## 48. Localization and Voice Routing

Voice calls shall preserve:

```text
Caller Locale
Caller Language
Preferred Language
Agent Language
Translation Requirement
```

---

## 49. Localization and Workflow Automation

Workflow automation shall support locale-aware:

* Trigger conditions.
* Message templates.
* AI prompts.
* Customer communication.
* Scheduling.
* Date calculations.
* Notifications.

---

## 50. Localization and Scheduling

Schedulers shall interpret recurring workflows according to configured time zones.

Example:

```text
Organization Timezone
        ↓
Workflow Schedule
        ↓
Timezone-aware Execution
```

---

## 51. Localization and Integrations

Integrations shall preserve locale metadata when supported.

Examples:

```text
Google
Gmail
Google Drive
LinkedIn
Facebook
Instagram
WhatsApp
YouTube
TikTok
Slack
HubSpot
Salesforce
Zendesk
Jira
Notion
Microsoft Teams
```

---

## 52. Localization and API Clients

Developer APIs shall support locale metadata.

Example:

```http
Accept-Language: en-BD
```

APIs shall return stable machine-readable identifiers regardless of language.

---

## 53. Localization and Webhooks

Webhook payloads shall prioritize canonical data.

Localized display fields may be included separately.

Example:

```json
{
  "event": "invoice.created",
  "invoice": {
    "amount": 1000,
    "currency": "USD"
  },
  "localized": {
    "display_amount": "$1,000.00",
    "locale": "en-US"
  }
}
```

---

## 54. Localization and Object Storage

Localized assets may be stored independently.

Example:

```text
/localization/
    /en-US/
    /en-BD/
    /bn-BD/
    /ar-SA/
```

Assets shall support versioning and tenant isolation.

---

## 55. Localization and CDN

Static translation resources and localized assets shall support:

* CDN caching.
* Versioned URLs.
* Cache invalidation.
* Regional delivery.
* Compression.

---

## 56. Localization Performance Requirements

The localization system shall:

* Avoid blocking critical rendering unnecessarily.
* Cache frequently used translations.
* Support lazy loading of locale resources.
* Avoid loading unused languages.
* Support CDN delivery.
* Minimize locale-switch latency.
* Avoid repeated translation API requests.

---

## 57. Localization Reliability Requirements

The localization layer shall degrade gracefully.

If localization infrastructure fails:

```text
Localization Service Failure
          ↓
Cached Translation
          ↓
Fallback Locale
          ↓
Default Language
```

Core business functionality shall remain operational wherever possible.

---

## 58. Localization Availability

Localization services shall support:

* Horizontal scaling.
* Redundant instances.
* Health checks.
* Automatic failover.
* Cache redundancy.
* Database backups.
* Deployment rollback.

---

## 59. Localization Cache Architecture

```text
Frontend
   │
   ▼
CDN
   │
   ▼
Redis
   │
   ▼
Localization Service
   │
   ▼
PostgreSQL
```

Cache keys should include relevant dimensions:

```text
locale
namespace
catalog_version
tenant_id
```

---

## 60. Localization Observability

Distributed tracing shall propagate:

```text
trace_id
request_id
organization_id
user_id
locale
language
translation_key
catalog_version
```

Sensitive user content shall not be unnecessarily logged.

---

## 61. Localization Disaster Recovery

Localization data shall be included in disaster-recovery processes.

Backups shall include:

* Translation catalogs.
* Translation versions.
* Locale configuration.
* Language configuration.
* Terminology.
* Translation memory.
* Localization workflows.

---

## 62. Localization Deployment

Localization resources shall be deployable independently from application binaries where practical.

The deployment system shall support:

* Versioned catalogs.
* Canary releases.
* Locale-specific rollout.
* Rollback.
* Validation before production.

---

## 63. Localization CI/CD Gates

CI/CD shall fail when:

* Required translations are missing.
* Placeholders mismatch.
* Invalid locale resources exist.
* Translation keys are duplicated.
* Translation schemas are invalid.
* Critical localized UI fails automated checks.

---

## 64. Localization Quality Gates

Production publication shall optionally require:

```text
Translation Completeness
+
Placeholder Validation
+
Automated QA
+
AI Quality Evaluation
+
Human Review
+
Accessibility Validation
+
Visual Validation
```

---

## 65. Accessibility Localization

Localized interfaces shall remain accessible.

Requirements include:

* Screen-reader support.
* Correct language metadata.
* Correct direction metadata.
* Keyboard navigation.
* Accessible labels.
* Localized ARIA labels.
* Localized error messages.
* Localized announcements.

---

## 66. SEO Localization

Public-facing SalesGenie pages shall support:

* Locale-specific URLs.
* Localized metadata.
* Language metadata.
* Alternate locale references.
* Localized titles.
* Localized descriptions.
* Localized structured data where applicable.

---

## 67. Localization Content Governance

Every production translation shall have:

```text
Owner
Translator
Reviewer
Version
Status
Timestamp
Source
Approval
```

---

## 68. Localization Auditability

The system shall maintain immutable audit records for critical localization actions.

Audited actions include:

* Language added.
* Language disabled.
* Locale modified.
* Translation created.
* Translation modified.
* Translation approved.
* Translation rejected.
* Translation published.
* Translation rolled back.
* Fallback changed.

---

## 69. Localization API Security

Localization APIs shall implement:

* Authentication.
* Authorization.
* RBAC.
* ABAC.
* Rate limiting.
* Input validation.
* Tenant isolation.
* Audit logging.
* Abuse prevention.

---

## 70. Localization Rate Limiting

AI translation and localization APIs shall support quotas at:

```text
Platform
Organization
Workplace
User
API Key
AI Agent
```

---

## 71. Localization Cost Management

AI translation usage shall be tracked.

Metrics shall include:

```text
Translation Tokens
Translation Requests
Translation Cost
Cost by Organization
Cost by Locale
Cost by Agent
Cost by Provider
```

---

## 72. Multi-Provider Translation

The AI localization system shall support multiple AI providers through the existing LLM gateway.

Example:

```text
Localization Request
       ↓
LLM Gateway
       ↓
Model Router
       ↓
Provider
       │
       ├── Primary
       ├── Secondary
       └── Fallback
```

---

## 73. AI Translation Safety

AI translation shall be evaluated for:

* Hallucination.
* Meaning distortion.
* Unsafe content transformation.
* Prompt injection.
* Terminology violations.
* Personally identifiable information exposure.
* Sensitive-data leakage.

---

## 74. Localization Prompt Management

Translation prompts shall be:

* Versioned.
* Tested.
* Evaluated.
* Audited.
* Environment-specific.
* Model-specific where required.

---

## 75. Localization Model Evaluation

The platform shall evaluate AI translation using:

```text
Semantic Accuracy
Terminology Accuracy
Fluency
Grammar
Cultural Appropriateness
Consistency
Placeholder Integrity
Formatting Integrity
Human Acceptance
```

---

## 76. Localization Human-in-the-Loop

The localization platform shall support:

```text
AI
 ↓
Confidence
 ↓
Human Review
 ↓
Approval
 ↓
Production
```

Humans shall remain authoritative for critical translations.

---

## 77. Critical Localization Content

Human approval shall be configurable as mandatory for:

* Legal documents.
* Privacy policies.
* Terms of service.
* Billing documents.
* Security notices.
* Compliance documents.
* Financial reports.
* Regulatory communications.
* High-risk customer communications.

---

## 78. Localization Feature Flags

Administrators shall be able to enable localization features progressively.

Example:

```text
feature.localization.arabic
feature.localization.bengali
feature.localization.ai_translation
feature.localization.rtl
feature.localization.localized_billing
feature.localization.localized_ai_agents
```

---

## 79. Localization Rollout Strategy

```text
Internal Users
      ↓
Beta Organizations
      ↓
Selected Regions
      ↓
10% Production
      ↓
25% Production
      ↓
50% Production
      ↓
100% Production
```

---

## 80. Definition of Done

Localization shall be considered production-ready when:

* All supported locales are registered.
* Locale resolution works.
* Translation catalogs are versioned.
* Missing translations are detected.
* Fallback logic works.
* RTL is supported where required.
* Unicode is supported end-to-end.
* Date/time formatting is correct.
* Currency formatting is correct.
* Number formatting is correct.
* Search works with localized content.
* AI agents support configured languages.
* RAG supports multilingual content.
* Reports support localization.
* Notifications support localization.
* Billing supports localization.
* Customer portal supports localization.
* Localization permissions are enforced.
* Tenant isolation is verified.
* Translation audit logging works.
* Localization metrics are available.
* Localization alerts are configured.
* Automated localization tests pass.
* Accessibility tests pass.
* Performance tests pass.
* Security tests pass.
* Human review workflows are operational.
* Rollback procedures are tested.

---

## 81. End-to-End Localization Architecture

```text
                         SALESGENIE
                             │
                             ▼
                    USER / CLIENT / AI
                             │
                             ▼
                    LOCALE RESOLUTION
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
          LANGUAGE         REGION        TIMEZONE
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                    LOCALIZATION ENGINE
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
   TRANSLATION           FORMATTING          REGIONAL
     SERVICE              SERVICE             SERVICE
        │                    │                    │
        ▼                    ▼                    ▼
   TRANSLATIONS           NUMBERS              TAX
   TERMINOLOGY            DATES                ADDRESS
   MEMORY                 CURRENCY             PHONE
        │                    │                    │
        └────────────────────┼────────────────────┘
                             ▼
                        CACHE LAYER
                             │
                             ▼
                         DATABASE
                             │
                             ▼
                    APPLICATION SERVICES
                             │
      ┌──────────────┬──────┼──────┬──────────────┐
      ▼              ▼      ▼      ▼              ▼
    SALES         MARKETING  SEO   SUPPORT       BILLING
      │              │      │      │              │
      └──────────────┴──────┼──────┴──────────────┘
                             ▼
                         AI PLATFORM
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
             AI Agents      RAG        Workflows
                │            │            │
                └────────────┼────────────┘
                             ▼
                     HUMAN REVIEW
                             │
                             ▼
                         PUBLISHING
                             │
                             ▼
                      LOCALIZED USER
```

---

## 82. Core Localization Principles

SalesGenie localization shall follow these principles:

1. **Never hardcode user-facing text.**
2. **Never use translated text as business logic.**
3. **Never overwrite canonical business data with localized presentation values.**
4. **Never assume English word order.**
5. **Never assume a single date format.**
6. **Never assume a single currency.**
7. **Never assume a single measurement system.**
8. **Never assume left-to-right layout.**
9. **Never concatenate translated message fragments.**
10. **Never expose tenant-specific translation data across tenants.**
11. **Never allow unauthorized translation publication.**
12. **Never allow localized errors to replace stable machine-readable error codes.**
13. **Never rely exclusively on AI translation for critical content.**
14. **Always preserve translation context.**
15. **Always version translations.**
16. **Always validate placeholders.**
17. **Always provide deterministic fallback behavior.**
18. **Always test localization independently from core business logic.**
19. **Always preserve canonical values.**
20. **Always treat localization as a platform capability rather than a frontend-only feature.**

---

## 83. Final Requirement

Localization shall be implemented as a **platform-wide cross-cutting architecture** rather than merely a frontend language switch.

The localization layer shall integrate with:

```text
Authentication
Authorization
RBAC
ABAC
Organizations
Workplaces
Users
CRM
Sales
Lead Generation
Lead Intelligence
Marketing
SEO
Advertising
Finance
Billing
Analytics
Reporting
Customer Support
Omnichannel
AI Agents
LLM Gateway
RAG
Knowledge Management
Workflow Automation
MCP
Integrations
Notifications
Search
Developer APIs
Data Platform
Observability
Security
Compliance
Testing
Customer Portal
Human-in-the-Loop
```

The final architecture shall ensure that **language, locale, region, timezone, currency, formatting, cultural conventions, AI behavior, business presentation, and localized content remain consistent across the entire SalesGenie ecosystem while canonical business data and business logic remain language-independent.**
