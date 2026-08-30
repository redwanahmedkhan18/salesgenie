# Internationalization Requirements — SalesGenie

**Document:** `internationalization.md`  
**Product:** SalesGenie — Enterprise AI Customer Support, Sales, Marketing, SEO, Analytics & Automation Platform  
**Document Type:** User Requirements, System Requirements & Functional Requirements  
**Architecture:** Multi-Tenant, Multi-Region, Multi-Language, Multi-Currency, AI + Human Hybrid  
**Priority:** P0 — Critical Platform Capability  
**Status:** Production Specification  
**Target Scale:** 10M+ users, 500K+ concurrent conversations

---

## 1. Purpose

SalesGenie shall provide enterprise-grade internationalization (i18n) and localization (l10n) capabilities so that users, organizations, AI agents, workflows, customer-facing interfaces, reports, notifications, billing systems, analytics, and integrations can operate across multiple languages, locales, currencies, time zones, date formats, number formats, regional conventions, and regulatory requirements.

Internationalization shall be implemented as a platform-level capability rather than as a frontend-only translation feature.

The system shall support:

- Multiple UI languages
- Organization-level language configuration
- User-level language preferences
- Workspace-level localization
- Customer/end-user language detection
- AI multilingual conversations
- Human-agent multilingual support
- Translation workflows
- Locale-aware formatting
- Multi-currency operations
- Time-zone management
- Regional business rules
- Localized notifications
- Localized reports
- Localized invoices
- Localized dashboards
- Localized AI responses
- Translation memory
- Terminology management
- Right-to-left languages
- Unicode
- Locale-aware search
- Multilingual RAG
- Multilingual embeddings
- Multilingual AI agents
- Multilingual workflows
- Regional compliance
- Localization administration
- Translation auditing
- Translation versioning
- Fallback language handling

---

## 2. Internationalization Goals

## 2.1 Primary Goals

1. Provide a consistent multilingual experience across the entire SalesGenie platform.
2. Allow users to independently configure their preferred language and locale.
3. Allow organizations to define supported languages.
4. Allow workspaces to override organization-level localization settings.
5. Automatically detect customer language where appropriate.
6. Enable AI agents to communicate naturally in supported languages.
7. Preserve business meaning during translation.
8. Support human-agent workflows across multiple languages.
9. Support regional currencies and financial formatting.
10. Support time-zone-aware scheduling and analytics.
11. Prevent locale-specific formatting from corrupting backend data.
12. Ensure all APIs remain locale-aware without coupling business logic to presentation language.
13. Provide centralized translation management.
14. Provide enterprise-grade translation governance.
15. Support future expansion to additional countries and languages without architectural redesign.

---

## 3. Non-Goals

The initial implementation shall not require:

- Separate application deployments for each language.
- Separate databases for each locale.
- Hard-coded language-specific business logic.
- Duplicate frontend applications per language.
- Translation of immutable technical identifiers.
- Translation of internal database IDs.
- Translation of source code.
- Translation of cryptographic values.
- Translation of API field names.

---

## 4. Supported Localization Dimensions

SalesGenie shall support the following independent dimensions:

```text
Language
   +
Locale
   +
Region
   +
Currency
   +
Time Zone
   +
Date Format
   +
Number Format
   +
Measurement System
   +
Writing Direction
   +
Business Rules
   +
Translation Preferences
```

These dimensions shall not be treated as a single hard-coded configuration value.

---

## 5. User Types

Internationalization shall support:

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
* AI Agents
* System Services

---

## 6. User Requirements

## UR-001 — Language Selection

Users shall be able to select their preferred interface language.

The selected language shall apply to:

* Navigation
* Buttons
* Forms
* Dashboards
* Tables
* Notifications
* Error messages
* Help text
* System messages
* Settings
* Reports
* AI interface controls

---

## UR-002 — Automatic Language Detection

The system shall be able to detect the user's preferred language using:

1. Explicit user preference
2. Organization preference
3. Browser language
4. Operating-system locale
5. Geographic locale where permitted
6. Customer conversation language
7. AI language detection

Explicit user configuration shall take precedence over automatic detection.

---

## UR-003 — Language Preference Persistence

Users shall be able to save language preferences.

Preferences shall persist across:

* Browser sessions
* Devices
* Login sessions
* Workspace changes

Preferences shall be stored server-side when the user is authenticated.

---

## UR-004 — Organization Language Configuration

Organization administrators shall be able to:

* Select default language
* Enable supported languages
* Disable unsupported languages
* Define default locale
* Define default currency
* Define default time zone
* Define regional formats

---

## UR-005 — Workspace Language Configuration

Workplace administrators shall be able to configure:

* Default language
* Supported languages
* Locale
* Currency
* Time zone
* Regional formatting
* AI language behavior

Workspace settings shall inherit from organization settings unless explicitly overridden.

---

## UR-006 — User-Level Overrides

Users shall be able to override organization/workspace defaults when permitted by policy.

Example:

```text
Organization:
English

Workspace:
English

User:
Spanish
```

The user's UI shall display Spanish without modifying organization configuration.

---

## UR-007 — Customer Language Detection

Support and sales systems shall detect the language used by customers.

Detection shall support:

* Email
* Webchat
* WhatsApp
* Facebook Messenger
* Instagram Messaging
* Telegram
* SMS
* Voice transcription
* Social inbox
* API conversations

---

## UR-008 — Multilingual AI Conversations

AI agents shall be able to:

* Detect customer language
* Respond in customer language
* Maintain language consistency
* Switch language dynamically
* Preserve conversation context
* Translate when necessary
* Escalate to human agents when confidence is insufficient

---

## UR-009 — Human-Agent Translation

Human support agents shall be able to communicate with customers who speak another language.

The platform shall support:

```text
Customer Language
       ↓
Translation
       ↓
Human Agent
       ↓
Translation
       ↓
Customer Language
```

---

## UR-010 — Translation Visibility

Agents shall be able to view:

* Original customer message
* Translated message
* Agent response
* Customer-language response
* Translation confidence where available

---

## UR-011 — Currency Localization

Users shall be able to view monetary values using appropriate currencies.

Examples:

* USD
* EUR
* GBP
* BDT
* CAD
* AUD
* JPY
* INR
* SGD
* AED
* SAR

The system shall support extensible ISO 4217 currency definitions.

---

## UR-012 — Time Zone Localization

Users shall be able to configure their preferred time zone.

Time-zone settings shall affect:

* Meetings
* Campaign scheduling
* Workflow scheduling
* Reports
* Notifications
* Billing periods
* Analytics
* Audit logs
* AI scheduling
* Sales sequences

---

## UR-013 — Local Date and Time Formatting

Dates and times shall be rendered according to the user's locale.

The system shall support:

* 12-hour format
* 24-hour format
* Local date formats
* Relative time
* Calendar conventions
* Daylight-saving transitions

---

## UR-014 — Number Formatting

The UI shall format:

* Currency
* Percentages
* Large numbers
* Decimal numbers
* Metrics
* Statistical values
* Financial values

according to locale.

---

## UR-015 — Right-to-Left Support

The platform shall support RTL languages such as:

* Arabic
* Hebrew
* Persian
* Urdu

RTL mode shall apply to:

* Navigation
* Dashboards
* Forms
* Tables
* Chat
* AI interfaces
* Reports
* Modals
* Notifications

---

## UR-016 — Multilingual Reports

Users shall be able to generate reports in their selected language.

Supported report formats shall include:

* XLSX
* CSV
* PDF
* JSON

---

## UR-017 — Localized Notifications

Users shall receive notifications in their configured language.

Supported notifications include:

* Email
* SMS
* Push
* In-app
* System alerts
* Security alerts
* Billing notifications
* Workflow notifications
* AI notifications

---

## UR-018 — Localized Billing

Billing interfaces shall support:

* Currency
* Regional tax presentation
* Invoice language
* Payment descriptions
* Subscription terminology
* Localized billing dates

---

## UR-019 — Multilingual Search

Users shall be able to search across multilingual content.

Search shall support:

* Language-aware tokenization
* Unicode
* Stemming where applicable
* Synonyms
* Transliteration
* Cross-language search
* Semantic search

---

## UR-020 — Multilingual Knowledge Base

Organizations shall be able to maintain knowledge-base content in multiple languages.

The system shall support:

* Original documents
* Translated documents
* Language metadata
* Translation versions
* Source-document relationships
* Language-specific access control

---

## UR-021 — Multilingual RAG

RAG systems shall support:

```text
Question in Language A
        ↓
Language Detection
        ↓
Multilingual Retrieval
        ↓
Relevant Documents
        ↓
Context Assembly
        ↓
LLM
        ↓
Answer in Language A
```

---

## UR-022 — Multilingual AI Agents

AI agents shall support:

* System prompts per language
* Language-specific instructions
* Multilingual tools
* Multilingual knowledge bases
* Language-specific guardrails
* Language-specific fallback behavior

---

## UR-023 — Translation Quality Feedback

Users shall be able to report:

* Incorrect translation
* Missing translation
* Poor terminology
* Wrong context
* Formatting errors
* Offensive translation
* Business terminology errors

---

## UR-024 — Language Availability

Users shall only see languages enabled by their organization/workspace policy unless the platform exposes globally available languages.

---

## UR-025 — Graceful Fallback

If a translation is unavailable, the system shall use the configured fallback language.

Example:

```text
Requested:
French

French translation unavailable

Fallback:
English
```

---

## 7. System Requirements

## SR-001 — Unicode

The entire platform shall use Unicode-compatible encoding.

UTF-8 shall be the default character encoding.

---

## SR-002 — Locale Model

The system shall represent locale independently from language.

Example:

```text
language = en
region   = US
locale   = en-US
currency = USD
timezone = America/New_York
```

---

## SR-003 — BCP 47 Language Tags

Language identifiers shall follow BCP 47 conventions where applicable.

Examples:

```text
en
en-US
en-GB
bn
bn-BD
es
es-MX
fr
fr-FR
de
de-DE
ar
ar-SA
ja
ja-JP
zh-CN
zh-TW
```

---

## SR-004 — ISO Standards

The platform shall use appropriate international standards including:

* ISO 639 for languages
* ISO 3166 for countries/regions
* ISO 4217 for currencies
* IANA Time Zone Database for time zones
* Unicode CLDR for locale formatting
* BCP 47 for language tags

---

## SR-005 — Centralized Locale Service

SalesGenie shall provide a centralized localization service.

Responsibilities:

* Locale resolution
* Translation lookup
* Currency formatting
* Number formatting
* Date formatting
* Time formatting
* Language fallback
* Translation version management

---

## SR-006 — Translation Service

A centralized translation service shall expose APIs for:

* Translation retrieval
* Translation creation
* Translation update
* Translation deletion
* Translation versioning
* Translation validation
* Translation publishing

---

## SR-007 — Translation Storage

Translations shall be stored independently from application source code.

Example conceptual model:

```text
translation_key
language
locale
value
version
status
namespace
metadata
created_at
updated_at
```

---

## SR-008 — Translation Namespaces

Translations shall support namespaces.

Examples:

```text
auth.*
navigation.*
dashboard.*
sales.*
marketing.*
seo.*
support.*
billing.*
settings.*
notifications.*
errors.*
ai.*
workflow.*
admin.*
```

---

## SR-009 — Translation Versioning

Translation changes shall be versioned.

The system shall support:

* Draft
* Review
* Approved
* Published
* Deprecated

---

## SR-010 — Translation Auditability

Translation modifications shall be auditable.

Audit information shall include:

* User
* Role
* Timestamp
* Previous value
* New value
* Language
* Locale
* Translation key
* Change reason

---

## SR-011 — Translation Cache

Frequently used translations shall be cached.

Caching shall support:

```text
tenant
+
workspace
+
language
+
locale
+
namespace
+
version
```

---

## SR-012 — Cache Invalidation

Translation cache shall be invalidated when:

* Translation changes
* Translation version changes
* Translation is unpublished
* Language is disabled
* Organization configuration changes

---

## SR-013 — Locale Resolution Priority

The system shall resolve locale using a deterministic hierarchy:

```text
Explicit Request Locale
        ↓
Authenticated User Locale
        ↓
Workspace Locale
        ↓
Organization Locale
        ↓
Browser Locale
        ↓
Platform Default Locale
```

---

## SR-014 — Tenant Isolation

Localization configuration shall be tenant-isolated.

One organization shall never access another organization's:

* Translation overrides
* Language policies
* Terminology
* Custom locale configuration
* Translation memory
* Localization analytics

---

## SR-015 — API Locale Support

APIs shall support locale metadata through standardized request mechanisms.

Examples:

```http
Accept-Language
Content-Language
```

API contracts shall not require localized field names.

---

## SR-016 — Backend Canonical Data

Backend systems shall store canonical values independent of presentation locale.

Examples:

```text
Database:
2026-08-30T10:30:00Z

UI:
August 30, 2026 4:30 PM
```

---

## SR-017 — UTC Storage

Timestamps shall be stored in UTC whenever technically appropriate.

Conversion shall occur at presentation or scheduling boundaries.

---

## SR-018 — Currency Storage

Financial values shall not rely exclusively on localized strings.

The backend shall preserve:

```text
amount
currency_code
precision
exchange_rate
effective_at
```

where applicable.

---

## SR-019 — Locale-Aware Formatting

Formatting shall use locale-aware libraries rather than manually implemented formatting rules.

---

## SR-020 — RTL Architecture

The frontend shall support logical CSS properties and bidirectional text.

Examples:

```css
margin-inline-start
margin-inline-end
padding-inline-start
padding-inline-end
inset-inline-start
```

---

## 8. Functional Requirements

## FR-001 — Language Management

The system shall allow authorized administrators to:

* Add language
* Enable language
* Disable language
* Set default language
* Configure language metadata
* Define fallback language
* View translation coverage

---

## FR-002 — User Locale Management

The system shall expose:

```http
GET    /api/v1/users/me/locale
PUT    /api/v1/users/me/locale
```

The locale profile shall include:

```json
{
  "language": "en",
  "locale": "en-US",
  "timezone": "America/New_York",
  "currency": "USD",
  "date_format": "auto",
  "time_format": "12h"
}
```

---

## FR-003 — Organization Localization Configuration

The system shall expose organization localization settings.

Conceptual endpoint:

```http
GET /api/v1/organizations/{organization_id}/localization
PUT /api/v1/organizations/{organization_id}/localization
```

---

## FR-004 — Workspace Localization

Workspace localization shall support inheritance.

```text
Platform
   ↓
Organization
   ↓
Workspace
   ↓
User
```

---

## FR-005 — Translation Retrieval

The frontend shall retrieve translation bundles based on:

```text
language
locale
namespace
version
tenant
```

---

## FR-006 — Translation Bundle Loading

The frontend shall support:

* Lazy loading
* Namespace loading
* Route-based loading
* Language switching
* Cache reuse
* Offline-safe fallback for previously loaded translations

---

## FR-007 — Dynamic Language Switching

Users shall be able to switch language without requiring a complete account reconfiguration.

The application shall update:

* UI labels
* Navigation
* Messages
* Formatting
* Directionality
* Date/time presentation

---

## FR-008 — Translation Interpolation

Translations shall support variables.

Example:

```text
"Welcome, {name}"
```

The system shall safely interpolate:

```text
Welcome, Redwan
```

---

## FR-009 — Pluralization

The localization engine shall support locale-specific pluralization rules.

Examples:

```text
0 items
1 item
2 items
```

Pluralization shall not be hard-coded using English-only rules.

---

## FR-010 — Gender-Aware Localization

Where required, translation systems shall support grammatical gender.

---

## FR-011 — Context-Aware Translation

Translation keys shall provide semantic context.

Example:

```text
sales.close
calendar.close
window.close
```

shall not necessarily share a single translation key.

---

## FR-012 — Translation Variables

User-generated values shall not be treated as translation keys.

The system shall prevent translation-key injection.

---

## FR-013 — Custom Terminology

Organizations shall be able to define custom terminology.

Example:

```text
Lead
Prospect
Customer
Opportunity
Workspace
Agent
Campaign
```

Custom terminology shall be respected by:

* AI agents
* Translation
* Reports
* Search
* RAG
* Notifications

---

## FR-014 — Translation Memory

The platform shall maintain reusable translation memory where enabled.

Translation memory shall support:

* Source phrase
* Target phrase
* Language pair
* Organization
* Context
* Confidence
* Approval state

---

## FR-015 — Machine Translation Integration

The platform may integrate with external machine translation providers.

Translation provider abstraction shall support:

```text
Provider A
Provider B
Provider C
Self-hosted model
```

The application shall not be tightly coupled to a single provider.

---

## FR-016 — AI Translation

AI-powered translation shall support:

* Context-aware translation
* Business terminology
* Conversation context
* Formality
* Tone preservation
* Brand voice
* Technical vocabulary

---

## FR-017 — Translation Confidence

AI translation may expose:

```text
translation_confidence
quality_score
detected_language
target_language
```

Low-confidence translations shall be eligible for human review.

---

## FR-018 — Human Translation Review

Authorized users shall be able to:

* Review translations
* Edit translations
* Approve translations
* Reject translations
* Request retranslation

---

## FR-019 — Translation Workflow

The translation lifecycle shall support:

```text
Machine Translation
        ↓
AI Quality Check
        ↓
Human Review
        ↓
Approval
        ↓
Publication
```

---

## FR-020 — Translation Coverage

The administration interface shall show:

```text
Language
Total Keys
Translated
Missing
Outdated
Reviewed
Approved
Coverage %
```

---

## FR-021 — Missing Translation Detection

The system shall identify untranslated keys automatically.

---

## FR-022 — Stale Translation Detection

When the source translation changes, dependent translations shall be marked stale.

---

## FR-023 — Translation Deployment

Translation updates shall be deployable independently of application code where architecture permits.

---

## FR-024 — Translation Rollback

Administrators shall be able to restore previous translation versions.

---

## FR-025 — Locale-Aware Currency

Currency display shall respect user and organization configuration.

---

## FR-026 — Currency Conversion

Where financial analytics require cross-currency aggregation, the system shall support:

* Exchange-rate ingestion
* Historical rates
* Conversion timestamps
* Base currency
* Reporting currency
* Original currency

---

## FR-027 — Currency Precision

The system shall respect currency-specific decimal precision.

---

## FR-028 — Financial Integrity

Localized currency formatting shall never alter the underlying financial value.

Example:

```text
$1,000.50
```

shall not be parsed back into an ambiguous floating-point representation for financial persistence.

---

## FR-029 — Time Zone Conversion

The system shall convert UTC timestamps into user-local time zones for presentation.

---

## FR-030 — Scheduling Across Time Zones

Workflow and campaign scheduling shall support:

```text
User Time Zone
Workspace Time Zone
Organization Time Zone
Recipient Time Zone
```

---

## FR-031 — Recipient Time Zone Optimization

Sales and marketing automation may use recipient-local time for:

* Email sequences
* Calls
* Notifications
* Campaigns
* Follow-ups

---

## FR-032 — Daylight-Saving Handling

The scheduling system shall correctly handle DST transitions.

Ambiguous or invalid local times shall trigger deterministic resolution policies.

---

## FR-033 — Locale-Aware Analytics

Analytics shall distinguish between:

```text
event_time_utc
user_timezone
report_timezone
```

to avoid incorrect aggregation.

---

## FR-034 — Localized Dashboards

Dashboard labels, metrics, filters, and date ranges shall be localized.

Metric identifiers shall remain language-independent internally.

---

## FR-035 — Localized AI Insights

AI-generated business insights shall be returned in the user's selected language.

---

## FR-036 — Localized AI Recommendations

AI recommendations shall respect:

* User language
* Organization language
* Locale
* Currency
* Time zone
* Business terminology

---

## FR-037 — AI Language Detection

AI agents shall detect language with confidence scoring.

Example:

```json
{
  "language": "es",
  "confidence": 0.98
}
```

---

## FR-038 — AI Language Policy

Organizations shall be able to configure:

```text
Auto Detect
Fixed Language
Customer Language
Agent Language
User Language
```

---

## FR-039 — Multilingual Conversation State

Conversation state shall preserve:

```text
detected_language
preferred_language
conversation_language
agent_language
translation_required
```

---

## FR-040 — Language Switching During Conversation

If a customer changes language, the system shall detect the change and adapt where policy permits.

---

## FR-041 — Human Handoff Translation

During AI-to-human escalation, the system shall provide:

* Original conversation
* Translated conversation
* Detected language
* Translation metadata
* Customer language preference

---

## FR-042 — Multilingual RAG Retrieval

The RAG system shall support:

* Same-language retrieval
* Cross-language retrieval
* Multilingual embeddings
* Language filters
* Translation-assisted retrieval

---

## FR-043 — Language-Aware Vector Search

Vector search metadata shall support:

```text
language
locale
region
tenant_id
workspace_id
document_id
```

---

## FR-044 — Multilingual Knowledge Base Permissions

Language variants shall inherit or explicitly define access-control policies.

---

## FR-045 — Localized Workflow Builder

Workflow UI shall be localized.

Workflow business logic shall remain language-neutral.

---

## FR-046 — Localized Workflow Content

Workflow-generated content shall support:

* Email templates
* SMS
* Notifications
* AI prompts
* Customer responses

in multiple languages.

---

## FR-047 — Language-Aware Email Templates

Templates shall support:

```text
template_id
language
locale
version
status
```

---

## FR-048 — Language-Aware Notification Templates

Notification templates shall support localization.

---

## FR-049 — Localized Error Messages

User-facing errors shall use localization keys.

Example:

```text
auth.invalid_credentials
billing.payment_failed
workflow.execution_failed
integration.connection_expired
```

Backend error codes shall remain stable regardless of language.

---

## FR-050 — API Error Localization

APIs shall return stable machine-readable error codes.

Example:

```json
{
  "error_code": "AUTH_INVALID_CREDENTIALS",
  "message": "Localized human-readable message"
}
```

Clients shall be able to localize messages independently where appropriate.

---

## 9. Frontend Requirements

## FE-001 — Internationalized UI

No user-facing string shall be hard-coded directly into UI components unless explicitly marked as non-localizable.

---

## FE-002 — Translation Hooks

Frontend components shall use a centralized localization abstraction.

Example:

```text
t("dashboard.revenue")
```

---

## FE-003 — Locale Provider

The application shall expose locale state globally.

Conceptual architecture:

```text
Application
    │
    ▼
Locale Provider
    │
    ├── Language
    ├── Locale
    ├── Currency
    ├── Time Zone
    └── Direction
```

---

## FE-004 — RTL Layout

Frontend components shall dynamically support LTR and RTL.

---

## FE-005 — Dynamic Direction

The document direction shall switch based on locale:

```html
<html dir="ltr">
```

or

```html
<html dir="rtl">
```

---

## FE-006 — Localized Forms

Forms shall support locale-aware:

* Dates
* Numbers
* Currency
* Addresses
* Phone numbers
* Names

---

## FE-007 — Phone Number Localization

Phone-number fields shall support international formats and country codes.

---

## FE-008 — Address Localization

Address forms shall support country-specific field ordering and requirements.

---

## FE-009 — Locale-Aware Validation

Validation shall support localized:

* Dates
* Numbers
* Postal codes
* Phone numbers
* Addresses

---

## FE-010 — Browser Locale

The frontend shall detect browser locale as a fallback.

---

## 10. Backend Requirements

## BE-001 — Locale Context

Backend requests shall carry locale context.

Conceptual context:

```json
{
  "language": "en",
  "locale": "en-US",
  "timezone": "Asia/Dhaka",
  "currency": "USD"
}
```

---

## BE-002 — Locale Middleware

API services shall provide centralized locale resolution middleware.

---

## BE-003 — Microservice Consistency

All SalesGenie microservices shall use a consistent localization contract.

Services include:

* Auth Service
* AI Gateway
* Lead Intelligence Service
* Billing Service
* WhatsApp Service
* Support Service
* Sales Service
* Marketing Service
* SEO Service
* Workflow Service
* Notification Service
* Reporting Service
* Analytics Service

---

## BE-004 — Service-to-Service Locale Propagation

Locale context shall propagate across asynchronous and synchronous service calls where required.

---

## BE-005 — Event Locale Metadata

Events may include:

```json
{
  "locale": {
    "language": "en",
    "locale": "en-US",
    "timezone": "Asia/Dhaka",
    "currency": "USD"
  }
}
```

Locale metadata shall not replace canonical event data.

---

## 11. Database Requirements

## DB-001 — Unicode Database

PostgreSQL shall use Unicode-compatible encoding.

---

## DB-002 — Language Metadata

Relevant entities shall support language metadata.

Examples:

* Documents
* Leads
* Contacts
* Campaigns
* Templates
* Conversations
* Knowledge articles
* AI agents

---

## DB-003 — Locale Configuration Tables

The system shall maintain structured localization configuration.

Conceptual entities:

```text
languages
locales
countries
currencies
time_zones
translation_keys
translations
translation_versions
translation_memory
terminology
locale_preferences
```

---

## DB-004 — Tenant Localization

Localization configuration shall include tenant/workspace boundaries.

---

## DB-005 — Translation Audit

Translation history shall be retained according to organizational retention policies.

---

## 12. API Requirements

## API-001 — Locale APIs

The platform shall provide APIs for:

```text
GET    /localization
GET    /localization/languages
GET    /localization/locales
GET    /localization/currencies
GET    /localization/timezones
GET    /localization/translations
PUT    /users/me/locale
PUT    /organizations/{id}/localization
PUT    /workspaces/{id}/localization
```

---

## API-002 — Translation APIs

Administrative APIs shall support:

```text
GET
POST
PUT
PATCH
DELETE
```

for translation management according to authorization policy.

---

## API-003 — Locale Validation

APIs shall validate:

* Language code
* Locale code
* Currency code
* Time-zone identifier
* Supported combinations

---

## API-004 — Locale Negotiation

API gateway shall support locale negotiation.

---

## API-005 — API Compatibility

Changing a user's locale shall never break API contracts.

---

## 13. AI Requirements

## AI-001 — Multilingual Model Routing

The LLM Gateway shall be able to select models based on:

* Language
* Quality requirements
* Latency
* Cost
* Provider availability

---

## AI-002 — Language-Aware Model Selection

Example:

```text
Language
   ↓
Model Capability
   ↓
Quality Score
   ↓
Cost
   ↓
Latency
   ↓
Selected Model
```

---

## AI-003 — Language Quality Monitoring

AI observability shall measure:

* Language detection accuracy
* Translation quality
* Response language correctness
* Language switching accuracy
* Hallucination rate by language
* RAG quality by language
* Agent success rate by language

---

## AI-004 — Prompt Localization

Prompts shall support:

* Language-specific system instructions
* Locale-specific examples
* Cultural context
* Terminology
* Brand voice

---

## AI-005 — Prompt Versioning

Localized prompts shall be versioned independently.

---

## AI-006 — AI Safety Across Languages

Safety and policy controls shall operate across supported languages.

The system shall not assume English-only safety evaluation.

---

## AI-007 — Prompt Injection Detection

Multilingual prompt-injection detection shall be supported.

---

## 14. Agent Requirements

## AG-001 — Agent Language Configuration

Each AI agent shall support:

```text
Supported Languages
Primary Language
Fallback Language
Auto Detection
Language Switching
```

---

## AG-002 — Agent Language Policy

Agent builders shall configure:

```text
Customer Language
Fixed Language
User Language
Organization Language
```

---

## AG-003 — Multilingual Agent Tools

Agent tools shall remain language-neutral internally while exposing localized descriptions to users/agents where required.

---

## AG-004 — Agent Handoff

Agent handoff shall preserve language state.

---

## 15. Sales Requirements

## SALES-I18N-001

Lead records shall support language preference.

---

## SALES-I18N-002

Sales agents shall be able to filter prospects by language.

---

## SALES-I18N-003

Sales sequences shall support language variants.

---

## SALES-I18N-004

AI sales agents shall generate outreach in prospect language.

---

## SALES-I18N-005

Lead intelligence shall support regional signals.

---

## SALES-I18N-006

Sales analytics shall allow localization-aware segmentation.

---

## 16. Marketing Requirements

## MKT-I18N-001

Marketing campaigns shall support language variants.

---

## MKT-I18N-002

Audience segmentation shall support language.

---

## MKT-I18N-003

AI marketing agents shall generate multilingual content.

---

## MKT-I18N-004

Campaign analytics shall allow comparison by:

```text
Language
Region
Country
Locale
```

---

## 17. SEO Requirements

## SEO-I18N-001

SEO tools shall support language-specific keyword research.

---

## SEO-I18N-002

SERP analysis shall support country/language combinations.

---

## SEO-I18N-003

Keyword clustering shall support multilingual datasets.

---

## SEO-I18N-004

AI SEO content generation shall support language and locale.

---

## 18. Support Requirements

## SUPPORT-I18N-001

Support tickets shall store customer language preference.

---

## SUPPORT-I18N-002

Support routing may route conversations based on agent language capability.

---

## SUPPORT-I18N-003

Support managers shall be able to filter agents by supported languages.

---

## SUPPORT-I18N-004

AI support agents shall support multilingual conversations.

---

## SUPPORT-I18N-005

SLA timers shall operate independently of display language and correctly account for configured time zones.

---

## 19. Billing Requirements

## BILL-I18N-001

Invoices shall contain:

* Customer locale
* Currency
* Billing date
* Tax information
* Localized descriptions

---

## BILL-I18N-002

Billing shall preserve original transaction currency.

---

## BILL-I18N-003

Reports shall support organization reporting currency.

---

## BILL-I18N-004

Currency conversion shall retain exchange-rate provenance.

---

## 20. Reporting Requirements

## REPORT-I18N-001

Reports shall support language selection.

---

## REPORT-I18N-002

Exports shall preserve locale-aware formatting where appropriate.

---

## REPORT-I18N-003

Machine-readable exports shall prioritize canonical values over localized display strings.

---

## REPORT-I18N-004

PDF reports shall support RTL and Unicode fonts.

---

## 21. Notification Requirements

## NOTIFY-I18N-001

Notification services shall select language based on recipient preference.

---

## NOTIFY-I18N-002

Notifications shall support language fallback.

---

## NOTIFY-I18N-003

Templates shall support locale variants.

---

## NOTIFY-I18N-004

Notification scheduling shall respect recipient time zones.

---

## 22. Search Requirements

## SEARCH-I18N-001

Search shall support Unicode.

---

## SEARCH-I18N-002

Search indexing shall retain document language metadata.

---

## SEARCH-I18N-003

Search ranking may consider language preference.

---

## SEARCH-I18N-004

Enterprise search shall enforce permissions independently of language.

---

## SEARCH-I18N-005

Semantic search shall support multilingual queries.

---

## 23. Accessibility Requirements

Internationalization shall work together with accessibility.

The system shall support:

* Screen readers
* RTL screen-reader navigation
* Localized ARIA labels
* Localized error messages
* Keyboard navigation
* Unicode characters
* Dynamic text expansion
* High zoom
* Long translated labels

Translations shall not cause interactive components to become inaccessible.

---

## 24. Security Requirements

## SEC-I18N-001

Translation systems shall not expose tenant-isolated content across organizations.

---

## SEC-I18N-002

User-provided translation content shall be sanitized.

---

## SEC-I18N-003

Translation APIs shall enforce RBAC/ABAC.

---

## SEC-I18N-004

Sensitive content shall not be sent to third-party translation providers unless explicitly permitted by policy.

---

## SEC-I18N-005

Organizations shall be able to disable external translation providers.

---

## SEC-I18N-006

Translation requests shall be auditable where they involve sensitive business data.

---

## 25. Privacy Requirements

The platform shall support:

* Data minimization
* Consent-aware translation
* Data residency policies
* Provider restrictions
* PII masking
* Sensitive-data detection
* Translation retention policies
* Deletion of translation artifacts

---

## 26. Performance Requirements

## PERF-I18N-001

Localization lookup shall not become a major contributor to frontend latency.

---

## PERF-I18N-002

Translation bundles shall support caching.

---

## PERF-I18N-003

Large translation bundles shall support lazy loading.

---

## PERF-I18N-004

Locale switching shall not require full application restart where technically avoidable.

---

## PERF-I18N-005

AI translation latency shall be observable separately from base AI inference latency.

---

## 27. Reliability Requirements

## REL-I18N-001

If the localization service becomes unavailable, previously cached translations shall remain usable where possible.

---

## REL-I18N-002

Missing translations shall fall back automatically.

---

## REL-I18N-003

Translation provider failures shall not break core customer conversations.

---

## REL-I18N-004

AI translation provider failures shall trigger fallback behavior.

---

## 28. Observability Requirements

The platform shall monitor:

```text
translation_requests
translation_failures
translation_latency
translation_cache_hit_rate
translation_coverage
missing_translation_count
stale_translation_count
language_detection_accuracy
translation_quality
ai_language_accuracy
language_switch_events
fallback_events
locale_resolution_failures
```

---

## 29. Analytics Requirements

Localization analytics shall measure:

* Users by language
* Organizations by language
* Active languages
* Language adoption
* Translation coverage
* Translation quality
* AI usage by language
* Support conversations by language
* Sales conversions by language
* Marketing conversions by language
* Revenue by region
* Revenue by currency
* Support SLA by language
* AI performance by language

---

## 30. Administration Requirements

Authorized administrators shall have access to:

```text
Localization Dashboard
        │
        ├── Languages
        ├── Locales
        ├── Translation Keys
        ├── Translation Coverage
        ├── Translation Memory
        ├── Terminology
        ├── Translation Providers
        ├── Translation Quality
        ├── Regional Settings
        ├── Currency
        ├── Time Zones
        ├── RTL Configuration
        └── Audit Logs
```

---

## 31. Localization Dashboard Requirements

The dashboard shall display:

* Supported languages
* Active languages
* Translation coverage
* Missing translations
* Stale translations
* Translation errors
* Translation latency
* AI translation quality
* Most-used languages
* Language adoption trend
* Translation provider health

---

## 32. Role-Based Permissions

Example permissions:

```text
localization.view
localization.manage
localization.language.create
localization.language.update
localization.language.disable
localization.translation.view
localization.translation.create
localization.translation.update
localization.translation.delete
localization.translation.publish
localization.translation.rollback
localization.terminology.manage
localization.provider.manage
localization.audit.view
```

---

## 33. AI + Human Localization Workflow

```text
CONTENT
   │
   ▼
LANGUAGE DETECTION
   │
   ▼
TRANSLATION REQUIRED?
   │
   ├── NO ───────────────► ORIGINAL CONTENT
   │
   └── YES
          │
          ▼
   AI/MACHINE TRANSLATION
          │
          ▼
   QUALITY EVALUATION
          │
       ┌──┴──┐
       │     │
    HIGH    LOW
       │     │
       ▼     ▼
   PUBLISH  HUMAN REVIEW
             │
             ▼
          APPROVAL
             │
             ▼
          PUBLISH
             │
             ▼
          CACHE
             │
             ▼
           USERS
```

---

## 34. Locale Resolution Architecture

```text
REQUEST
   │
   ▼
Explicit Locale?
   │
   ├── YES ──► USE IT
   │
   ▼
User Locale?
   │
   ├── YES ──► USE IT
   │
   ▼
Workspace Locale?
   │
   ├── YES ──► USE IT
   │
   ▼
Organization Locale?
   │
   ├── YES ──► USE IT
   │
   ▼
Browser Locale?
   │
   ├── YES ──► USE IT
   │
   ▼
PLATFORM DEFAULT
```

---

## 35. Multilingual AI Architecture

```text
CUSTOMER MESSAGE
       │
       ▼
LANGUAGE DETECTION
       │
       ▼
LANGUAGE + LOCALE CONTEXT
       │
       ▼
AI ORCHESTRATOR
       │
       ├───────────────┐
       ▼               ▼
RAG RETRIEVAL     MODEL ROUTING
       │               │
       └───────┬───────┘
               ▼
          LLM INFERENCE
               │
               ▼
       LANGUAGE VALIDATION
               │
               ▼
        SAFETY VALIDATION
               │
               ▼
        RESPONSE GENERATION
               │
               ▼
        CUSTOMER LANGUAGE
```

---

## 36. Multilingual RAG Architecture

```text
DOCUMENTS
   │
   ▼
DOCUMENT LANGUAGE DETECTION
   │
   ▼
NORMALIZATION
   │
   ▼
CHUNKING
   │
   ▼
MULTILINGUAL EMBEDDINGS
   │
   ▼
VECTOR DATABASE
   │
   ▼
USER QUERY
   │
   ▼
QUERY LANGUAGE DETECTION
   │
   ▼
MULTILINGUAL RETRIEVAL
   │
   ▼
RANKING
   │
   ▼
LANGUAGE-AWARE CONTEXT
   │
   ▼
LLM
   │
   ▼
USER LANGUAGE
```

---

## 37. Translation Data Model

Conceptual model:

```text
TranslationKey
├── id
├── namespace
├── key
├── description
├── context
├── source_language
├── source_value
├── created_at
└── updated_at

Translation
├── id
├── translation_key_id
├── language
├── locale
├── value
├── status
├── version
├── translator_type
├── quality_score
├── approved_by
├── created_at
└── updated_at

TranslationMemory
├── source_language
├── target_language
├── source_text
├── target_text
├── context
├── confidence
├── tenant_id
└── created_at
```

---

## 38. Locale Preference Data Model

```text
UserLocalePreference
├── user_id
├── language
├── locale
├── timezone
├── currency
├── date_format
├── time_format
├── number_format
└── updated_at

OrganizationLocalePreference
├── organization_id
├── default_language
├── default_locale
├── default_timezone
├── default_currency
└── supported_languages

WorkspaceLocalePreference
├── workspace_id
├── default_language
├── locale
├── timezone
├── currency
└── inheritance_policy
```

---

## 39. Language Detection Requirements

Language detection shall:

* Detect supported languages
* Return confidence
* Handle mixed-language content
* Handle short messages
* Handle spelling errors where possible
* Handle transliteration where possible
* Handle code-switching
* Avoid incorrectly switching languages based on a single ambiguous token

---

## 40. Mixed-Language Requirements

The platform shall support messages such as:

```text
"Can you send me the invoiceটা আজকে?"
```

where multiple languages appear in one message.

The system shall avoid unnecessary translation of already understandable segments.

---

## 41. Regionalization Requirements

Regional settings shall support:

* Country
* Region/state
* Currency
* Time zone
* Date format
* Number format
* Address format
* Phone format
* Tax conventions
* Business-day rules
* Holiday calendars
* Measurement systems

---

## 42. Business Calendar Requirements

The workflow scheduler shall optionally support regional:

* Weekends
* Public holidays
* Working hours
* Business days
* Office hours

These settings shall be configurable by organization/workspace.

---

## 43. Localization of AI Business Logic

Localization shall never alter internal identifiers.

Example:

```text
Internal:
lead_status = qualified

English:
Qualified

Spanish:
Calificado

Bangla:
যোগ্য
```

The backend shall continue using:

```text
qualified
```

as the canonical value.

---

## 44. Localization of Enumerations

Backend enumerations shall remain language-independent.

The frontend shall map enum values to localized labels.

Example:

```json
{
  "status": "qualified"
}
```

UI:

```text
Qualified
Calificado
যোগ্য
```

---

## 45. Internationalization Testing

The test strategy shall include:

## Language Testing

* Translation completeness
* Translation correctness
* Missing keys
* Duplicate keys
* Stale translations

## Locale Testing

* Date formatting
* Time formatting
* Currency formatting
* Number formatting
* Time zones

## RTL Testing

* Arabic
* Hebrew
* Urdu
* Persian

## AI Testing

* Language detection
* Translation quality
* Multilingual RAG
* Multilingual agents
* Prompt injection in multiple languages
* Safety policy enforcement

---

## 46. Internationalization Acceptance Criteria

The implementation shall be considered production-ready only when:

* [ ] Users can select language.
* [ ] User language persists.
* [ ] Organization defaults work.
* [ ] Workspace overrides work.
* [ ] Locale resolution is deterministic.
* [ ] Translation fallback works.
* [ ] Missing translations are detectable.
* [ ] Translation versions are auditable.
* [ ] RTL languages render correctly.
* [ ] Currency formatting is locale-aware.
* [ ] Time-zone conversion works correctly.
* [ ] DST transitions are handled.
* [ ] AI can detect supported languages.
* [ ] AI can respond in customer language.
* [ ] AI language switching works.
* [ ] Human translation workflow works.
* [ ] Multilingual RAG works.
* [ ] Multilingual search works.
* [ ] Reports support localization.
* [ ] Notifications support localization.
* [ ] Billing supports localized presentation.
* [ ] Translation cache works.
* [ ] Translation cache invalidation works.
* [ ] Tenant isolation is enforced.
* [ ] Localization permissions are enforced.
* [ ] Localization activity is audited.
* [ ] Translation provider failures have fallback behavior.
* [ ] Localization metrics are observable.
* [ ] Internationalization does not degrade core platform reliability.

---

## 47. Definition of Done

Internationalization shall be considered complete when SalesGenie can operate as a single global SaaS platform in which:

```text
USER
 │
 ├── Language
 ├── Locale
 ├── Currency
 ├── Time Zone
 └── Regional Preferences
        │
        ▼
ORGANIZATION
 │
 ├── Supported Languages
 ├── Localization Policy
 ├── Terminology
 ├── Translation Memory
 └── Regional Configuration
        │
        ▼
WORKSPACE
 │
 ├── Language
 ├── Locale
 ├── Currency
 └── Time Zone
        │
        ▼
SALES / MARKETING / SEO / SUPPORT
        │
        ▼
AI ORCHESTRATION
        │
 ├── Language Detection
 ├── Multilingual Models
 ├── Translation
 ├── Multilingual RAG
 └── Language-Aware Agents
        │
        ▼
HUMAN OPERATIONS
        │
 ├── Human Review
 ├── Translation Review
 └── Human Handoff
        │
        ▼
CUSTOMER
```

The complete system shall maintain **language independence at the data and business-logic layers while providing localized experiences at the presentation, communication, AI, reporting, billing, analytics, and customer-interaction layers.**
