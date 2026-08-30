# SalesGenie — Lead Deduplication

## FAANG-Level User Requirements, System Requirements & Functional Requirements

**Module:** `lead_deduplication.md`  
**Platform:** SalesGenie Enterprise AI Sales & Revenue Intelligence Platform  
**Processing Modes:** AI-Based + Human-Assisted  
**Architecture:** Multi-Tenant, Event-Driven, Microservices, AI-Agentic  
**Requirement Level:** Enterprise / FAANG-Level  
**Version:** 1.0

---

## 1. Module Overview

The Lead Deduplication module shall identify, prevent, consolidate, and continuously manage duplicate lead records across SalesGenie and connected data sources.

The module shall support:

- Real-time duplicate prevention
- Batch duplicate detection
- Historical duplicate discovery
- AI-based duplicate detection
- Rule-based duplicate detection
- Fuzzy matching
- Exact matching
- Semantic matching
- Entity resolution
- Cross-source identity resolution
- Human review
- Human-approved merging
- AI-assisted merging
- Automatic merging under configurable policies
- Duplicate clustering
- Canonical record selection
- Field-level conflict resolution
- Data provenance
- Merge history
- Unmerge/recovery
- Duplicate analytics
- Duplicate prevention
- CRM synchronization
- Continuous deduplication

The system shall treat deduplication as an ongoing identity-resolution capability rather than a one-time cleanup operation.

---

## 2. Business Objectives

The Lead Deduplication module shall:

1. Prevent duplicate leads from entering the SalesGenie platform.
2. Detect duplicates created through different channels.
3. Detect duplicate leads across integrated CRM and external systems.
4. Consolidate fragmented lead information.
5. Preserve the most complete and trustworthy lead profile.
6. Prevent duplicate outreach.
7. Prevent duplicate sales ownership.
8. Improve lead scoring accuracy.
9. Improve segmentation accuracy.
10. Improve sales forecasting accuracy.
11. Improve CRM data quality.
12. Reduce operational data-cleaning costs.
13. Preserve original records and provenance.
14. Provide explainable AI duplicate decisions.
15. Allow humans to override AI decisions.
16. Support safe automated merging.
17. Prevent cross-tenant data contamination.
18. Maintain a complete audit trail.
19. Continuously learn from human review outcomes where permitted.
20. Provide measurable data-quality improvements.

---

## 3. Deduplication Lifecycle

```text
Lead Created / Imported
        ↓
Normalization
        ↓
Identity Feature Extraction
        ↓
Exact Match Detection
        ↓
Fuzzy Match Detection
        ↓
Semantic / AI Match Detection
        ↓
Candidate Generation
        ↓
Similarity Scoring
        ↓
Business Rule Validation
        ↓
Duplicate Classification
        ↓
 ┌───────────────────────────────┐
 │ High Confidence Duplicate     │
 │                               │
 │ Auto-Merge / Auto-Block       │
 └───────────────────────────────┘

 ┌───────────────────────────────┐
 │ Medium Confidence             │
 │                               │
 │ Human Review                  │
 └───────────────────────────────┘

 ┌───────────────────────────────┐
 │ Low Confidence                │
 │                               │
 │ Keep Separate                 │
 └───────────────────────────────┘

        ↓
Canonical Record
        ↓
Field-Level Consolidation
        ↓
Relationship Preservation
        ↓
Source Synchronization
        ↓
Audit & Analytics
```

---

## 4. User Roles

| Role                   | Responsibilities                             |
| ---------------------- | -------------------------------------------- |
| Super Admin            | Platform-wide deduplication governance       |
| Organization Admin     | Organization deduplication policies          |
| Workplace Admin        | Workplace-level configuration                |
| Sales Manager          | Review and approve duplicate decisions       |
| RevOps Manager         | Data-quality governance                      |
| Sales Agent            | Report suspected duplicates                  |
| SDR/BDR                | Review duplicate leads                       |
| Data Steward           | Perform data-quality operations              |
| Data Analyst           | Analyze deduplication performance            |
| AI Deduplication Agent | Detect and classify duplicates               |
| AI Sales Agent         | Consume canonical lead records               |
| End User               | Access authorized canonical lead information |

---

## 5. User Requirements

## UR-001 — Duplicate Prevention

The system shall prevent creation of duplicate leads when configured duplicate policies identify an existing matching lead.

## UR-002 — Duplicate Detection

Users shall be able to detect duplicate leads across existing records.

## UR-003 — Real-Time Detection

The system shall detect potential duplicates during lead creation or ingestion.

## UR-004 — Batch Detection

Authorized users shall be able to execute duplicate detection against large lead datasets.

## UR-005 — Historical Detection

The system shall identify duplicates among historical lead records.

## UR-006 — Exact Matching

Users shall be able to configure exact matching fields.

Supported examples:

* Email
* Phone
* External ID
* CRM ID
* Website/domain
* Social profile identifier

## UR-007 — Fuzzy Matching

The system shall support fuzzy matching for imperfect data.

Examples:

```text
john.smith@example.com
johnsmith@example.com

+1 202 555 0199
2025550199

Acme Corporation
ACME Corp.

Mohammad Rahman
Md. Rahman
```

## UR-008 — Semantic Matching

The system shall use AI to detect records that represent the same person or business despite significant textual differences.

## UR-009 — Duplicate Groups

The system shall group related duplicate records into duplicate clusters.

## UR-010 — Duplicate Confidence

Users shall be able to view duplicate confidence scores.

## UR-011 — Duplicate Explanation

Users shall be able to understand why two records were classified as duplicates.

## UR-012 — Review Queue

The system shall provide a human duplicate-review queue.

## UR-013 — Human Approval

Authorized users shall be able to approve duplicate decisions.

## UR-014 — Human Rejection

Authorized users shall be able to reject duplicate recommendations.

## UR-015 — Human Override

Authorized users shall be able to override AI duplicate classifications.

## UR-016 — Merge Records

Authorized users shall be able to merge duplicate leads.

## UR-017 — Keep Separate

Users shall be able to explicitly mark records as distinct.

## UR-018 — False-Positive Protection

The system shall prevent uncertain records from being automatically merged.

## UR-019 — Canonical Record

The system shall identify a canonical lead record for each duplicate cluster.

## UR-020 — Field-Level Selection

Users shall be able to choose which field value survives a merge.

## UR-021 — Data Provenance

Users shall be able to identify the source of every merged field.

## UR-022 — Merge Preview

Users shall be able to preview the result of a merge before execution.

## UR-023 — Merge Recovery

Authorized users shall be able to recover or unmerge records where supported.

## UR-024 — Duplicate Reporting

Users shall be able to generate duplicate reports.

## UR-025 — Duplicate Search

Users shall be able to search for suspected duplicates.

## UR-026 — Duplicate Filtering

Users shall be able to filter duplicates by:

* Confidence
* Source
* Organization
* Date
* Status
* Duplicate type
* Match method
* Review status

## UR-027 — Duplicate Statistics

Users shall be able to view duplicate rates and data-quality metrics.

## UR-028 — Duplicate Reporting

Users shall be able to identify the highest sources of duplicate creation.

## UR-029 — Source Comparison

Users shall be able to compare duplicate records across external systems.

## UR-030 — Duplicate Prevention Rules

Authorized administrators shall be able to configure duplicate-prevention policies.

## UR-031 — Exclusion Rules

Authorized users shall be able to define records or sources that must not be automatically merged.

## UR-032 — Protected Records

Authorized users shall be able to protect specific records from automated merging.

## UR-033 — Bulk Merge

Authorized users shall be able to merge duplicate groups in bulk.

## UR-034 — Bulk Review

Users shall be able to approve or reject multiple duplicate recommendations.

## UR-035 — Duplicate Notifications

The system shall notify relevant users about important duplicate conflicts.

---

## 6. AI-Based User Requirements

## AI-UR-001 — AI Duplicate Detection

AI shall identify potential duplicate leads using multiple identity signals.

## AI-UR-002 — Entity Resolution

AI shall determine whether multiple records represent the same real-world entity.

## AI-UR-003 — Identity Similarity

AI shall calculate similarity between lead records.

## AI-UR-004 — Multi-Field Reasoning

AI shall evaluate multiple fields jointly rather than relying exclusively on a single identifier.

## AI-UR-005 — Contextual Matching

AI shall consider contextual information including:

* Name
* Email
* Phone
* Company
* Job title
* Website
* Domain
* Location
* Industry
* Social profiles
* CRM identifiers
* Lead source
* Existing account relationships
* Engagement history

## AI-UR-006 — Typo Detection

AI shall detect typographical variations.

## AI-UR-007 — Name Variation Detection

AI shall detect variations such as:

```text
Mohammad Rahman
Md Rahman
Muhammad Rahman
M. Rahman
```

## AI-UR-008 — Company Resolution

AI shall recognize company naming variations.

```text
Microsoft Corporation
Microsoft Corp.
Microsoft
Microsoft Inc.
```

## AI-UR-009 — Domain Intelligence

AI shall use domain information to strengthen company-level identity resolution.

## AI-UR-010 — Contact Identity Resolution

AI shall identify whether different contact records represent the same person.

## AI-UR-011 — Confidence Scoring

AI shall produce a duplicate confidence score.

## AI-UR-012 — Explainability

AI shall provide evidence supporting duplicate classification.

## AI-UR-013 — Alternative Interpretation

AI shall identify cases where records may represent different people with similar attributes.

## AI-UR-014 — Duplicate Cluster Detection

AI shall identify groups containing multiple records belonging to the same entity.

## AI-UR-015 — Canonical Record Recommendation

AI shall recommend the best canonical record.

## AI-UR-016 — Field Value Recommendation

AI shall recommend the best value for conflicting fields.

## AI-UR-017 — Data Quality Assessment

AI shall evaluate completeness and reliability of candidate records.

## AI-UR-018 — Source Reliability

AI shall consider source reliability when selecting canonical field values.

## AI-UR-019 — Temporal Reasoning

AI shall consider the freshness of information.

## AI-UR-020 — Conflict Detection

AI shall identify contradictory information between records.

## AI-UR-021 — Merge Risk Prediction

AI shall estimate the risk of an incorrect merge.

## AI-UR-022 — Human Review Prioritization

AI shall prioritize ambiguous duplicates for human review.

## AI-UR-023 — Learning From Review

AI shall use approved human decisions as feedback where organizational policy permits.

## AI-UR-024 — Duplicate Pattern Discovery

AI shall identify recurring duplicate-generation patterns.

## AI-UR-025 — Duplicate Source Prediction

AI shall identify systems or workflows producing excessive duplicates.

## AI-UR-026 — Continuous Improvement

The AI system shall continuously improve duplicate detection based on validated outcomes.

---

## 7. Human-Based User Requirements

## HUMAN-UR-001 — Manual Duplicate Detection

Users shall be able to manually mark records as suspected duplicates.

## HUMAN-UR-002 — Manual Merge

Authorized users shall be able to merge records without AI assistance.

## HUMAN-UR-003 — Manual Canonical Selection

Users shall be able to select the canonical record.

## HUMAN-UR-004 — Field-Level Conflict Resolution

Users shall be able to choose individual field values during merging.

## HUMAN-UR-005 — Duplicate Rejection

Users shall be able to explicitly classify records as non-duplicates.

## HUMAN-UR-006 — Protected Records

Humans shall be able to protect strategic records from automated merging.

## HUMAN-UR-007 — Review Queue

Humans shall be able to review AI-generated duplicate recommendations.

## HUMAN-UR-008 — Merge Approval

Organizations shall be able to require approval before merging sensitive or high-value leads.

## HUMAN-UR-009 — Merge Reason

Organizations shall be able to require a reason for manual merging.

## HUMAN-UR-010 — Emergency Data Repair

Authorized administrators shall be able to correct incorrect merges.

## HUMAN-UR-011 — Audit Review

Authorized users shall be able to inspect who merged, separated, or protected records.

## HUMAN-UR-012 — Data Steward Workflow

Data stewards shall be able to process large duplicate-review queues.

---

## 8. System Requirements

## SR-001 — Multi-Tenant Isolation

Duplicate detection shall never compare or merge records across unauthorized tenants.

## SR-002 — Organization Isolation

Organization boundaries shall be enforced during duplicate detection.

## SR-003 — Workplace Isolation

Workplace-level ownership boundaries shall be respected.

## SR-004 — RBAC

Deduplication operations shall integrate with SalesGenie's centralized RBAC system.

## SR-005 — Fine-Grained Permissions

The system shall support permissions such as:

```text
lead.deduplication.view
lead.deduplication.detect
lead.deduplication.review
lead.deduplication.approve
lead.deduplication.reject
lead.deduplication.merge
lead.deduplication.unmerge
lead.deduplication.bulk
lead.deduplication.configure
lead.deduplication.audit
```

## SR-006 — Duplicate State Management

The system shall maintain canonical duplicate states.

```text
NEW
SUSPECTED
CANDIDATE
UNDER_REVIEW
CONFIRMED
REJECTED
MERGED
PROTECTED
UNMERGED
FAILED
```

## SR-007 — Immutable Original Data

The system shall preserve original record information before destructive or consolidating operations.

## SR-008 — Merge Versioning

Every merge operation shall create a versioned record of the transformation.

## SR-009 — Data Provenance

The system shall retain the origin of merged fields.

## SR-010 — Idempotency

Repeated duplicate-detection and merge requests shall not produce inconsistent results.

## SR-011 — Concurrency Control

Concurrent merge operations shall be protected against race conditions.

## SR-012 — Transactional Merge

Record merges shall be transactional.

## SR-013 — Referential Integrity

Merging shall preserve valid relationships with:

* Activities
* Conversations
* Opportunities
* Deals
* Accounts
* Tasks
* Notes
* Campaigns
* Sales sequences
* Outreach history
* Assignments

## SR-014 — Assignment Preservation

Lead ownership shall be preserved or explicitly resolved during merging.

## SR-015 — Outreach Protection

Deduplication shall prevent duplicate outreach after consolidation.

## SR-016 — CRM Synchronization

Merged identities shall synchronize with supported external systems.

## SR-017 — Event-Driven Architecture

Deduplication operations shall publish relevant domain events.

## SR-018 — Audit Logging

All consequential deduplication actions shall generate audit events.

## SR-019 — AI Model Versioning

AI duplicate decisions shall record model version information.

## SR-020 — Policy Versioning

Duplicate decisions shall record the applicable deduplication policy version.

---

## 9. Functional Requirements

## FR-001 — Normalize Lead Data

The system shall normalize data before duplicate comparison.

Normalization shall support:

```text
Whitespace normalization
Case normalization
Unicode normalization
Phone normalization
Email normalization
URL normalization
Domain normalization
Company-name normalization
Name normalization
Address normalization
```

## FR-002 — Exact Duplicate Detection

The system shall identify exact duplicates using configured unique identifiers.

## FR-003 — Fuzzy Duplicate Detection

The system shall identify approximate duplicates using configurable similarity algorithms.

## FR-004 — AI Duplicate Detection

The system shall use AI-based entity resolution for ambiguous records.

## FR-005 — Candidate Generation

The system shall efficiently generate likely duplicate candidates before expensive comparison.

Candidate blocking may use:

```text
Email domain
Phone prefix
Company domain
Company name
Name tokens
Location
External identifiers
```

## FR-006 — Similarity Scoring

The system shall calculate field-level and overall similarity.

Example:

```text
Name Similarity       = 0.94
Email Similarity      = 1.00
Phone Similarity      = 0.97
Company Similarity    = 0.91
Domain Similarity     = 1.00
Location Similarity   = 0.86

Overall Score         = 0.96
```

## FR-007 — Confidence Classification

The system shall classify duplicate candidates using configurable thresholds.

Example:

```text
0.95 - 1.00 → High Confidence
0.80 - 0.94 → Review Required
0.00 - 0.79 → Likely Distinct
```

Thresholds shall be configurable.

## FR-008 — Duplicate Candidate

The system shall create a duplicate candidate record containing:

```text
Candidate ID
Lead A
Lead B
Similarity Score
Confidence
Match Method
Evidence
Model Version
Policy Version
Status
Created At
```

## FR-009 — Duplicate Cluster

The system shall group related duplicate candidates into clusters.

Example:

```text
Duplicate Cluster #D-1024

Lead A
Lead B
Lead C
Lead D

Canonical Candidate:
Lead A
```

## FR-010 — Duplicate Classification

The system shall support:

```text
DUPLICATE
NOT_DUPLICATE
POSSIBLE_DUPLICATE
UNKNOWN
```

## FR-011 — AI Explanation

AI recommendations shall include explainable evidence.

Example:

```text
Reason:
- Same normalized email
- Same company domain
- Similar person name
- Same phone number
- Matching company
```

## FR-012 — Human Review

Medium-confidence records shall enter a configurable human-review queue.

## FR-013 — Review Actions

Reviewers shall be able to:

```text
Confirm Duplicate
Reject Duplicate
Merge
Keep Separate
Protect
Escalate
```

## FR-014 — Merge Preview

Before merging, the system shall display:

```text
Canonical Record
Duplicate Record
Field Differences
Selected Values
Relationships
Activities
Ownership
Source Systems
Potential Conflicts
Merge Impact
```

## FR-015 — Canonical Record Selection

The system shall recommend or allow selection of the canonical lead.

Canonical selection may consider:

```text
Completeness
Freshness
Source reliability
Verification status
Engagement history
Ownership
Conversion history
Account relationships
```

## FR-016 — Field-Level Resolution

The system shall support:

```text
Canonical value
Duplicate value
Most recent value
Most trusted source
AI recommended value
Human selected value
```

## FR-017 — Merge Execution

The system shall merge duplicate records while preserving valid relationships.

## FR-018 — Merge Audit

The system shall record:

```text
Merge ID
Canonical Lead
Merged Lead
Actor
Actor Type
Reason
Field Changes
Relationships Changed
AI Recommendation
AI Confidence
Policy Version
Timestamp
```

## FR-019 — Soft Merge

The system shall support soft merging where the original record remains recoverable.

## FR-020 — Hard Merge

Hard deletion or irreversible consolidation shall require elevated permissions and explicit policy configuration.

## FR-021 — Unmerge

Authorized users shall be able to reverse supported merges.

## FR-022 — Merge Recovery

The system shall provide recovery mechanisms for failed or incorrect merges.

## FR-023 — Protected Records

Protected records shall be excluded from automated merging unless explicitly overridden.

## FR-024 — Duplicate Prevention

The system shall perform duplicate checks before creating a new lead.

## FR-025 — Import Deduplication

The system shall deduplicate leads during bulk imports.

## FR-026 — API Deduplication

API-created leads shall pass through duplicate detection according to tenant policy.

## FR-027 — Integration Deduplication

Leads synchronized from external platforms shall pass through deduplication.

## FR-028 — Continuous Deduplication

The system shall periodically detect newly created duplicate records.

## FR-029 — Duplicate Alerts

The system shall notify users when high-risk duplicates are detected.

## FR-030 — Duplicate Assignment Protection

The system shall prevent duplicate leads from being independently assigned when the duplicate relationship is confirmed.

## FR-031 — Duplicate Outreach Protection

The system shall prevent multiple sales sequences from contacting the same resolved person when organizational policy requires identity-level suppression.

## FR-032 — Account Relationship Preservation

Lead-to-account relationships shall be preserved during merging.

## FR-033 — Opportunity Preservation

Associated opportunities shall remain correctly connected after merging.

## FR-034 — Deal Preservation

Associated deals shall remain correctly associated with the canonical entity.

## FR-035 — Conversation Preservation

Conversation history shall remain accessible after merging.

## FR-036 — Activity Preservation

Tasks, notes, meetings, calls, and activities shall be preserved.

## FR-037 — Sequence Preservation

Sales sequence participation shall be consolidated safely.

## FR-038 — Campaign Preservation

Campaign membership and attribution shall be preserved.

## FR-039 — Source Attribution

Original lead sources shall remain available after merging.

## FR-040 — Provenance Tracking

Each canonical field shall optionally retain:

```text
Source
Source Record ID
Original Value
Selected Value
Selection Method
Selection Timestamp
```

## FR-041 — Bulk Detection

Authorized users shall be able to scan large datasets.

## FR-042 — Bulk Review

Reviewers shall be able to process duplicate candidates in batches.

## FR-043 — Bulk Merge

Authorized users shall be able to merge approved duplicate clusters in bulk.

## FR-044 — Bulk Safety

Bulk operations shall support:

```text
Dry Run
Preview
Validation
Partial Failure Handling
Rollback
Audit
```

## FR-045 — Duplicate Search

Users shall be able to search by:

```text
Name
Email
Phone
Company
Domain
Lead ID
External ID
```

## FR-046 — Duplicate Filters

Users shall be able to filter by:

```text
Confidence
Status
Source
Date
Owner
Organization
Workplace
Review Status
Match Method
```

## FR-047 — Duplicate Dashboard

The system shall provide:

```text
Total Leads
Duplicate Candidates
Confirmed Duplicates
Merged Records
Rejected Candidates
Pending Reviews
Duplicate Rate
Merge Rate
False Positive Rate
```

## FR-048 — Source Quality Analytics

The system shall identify which sources generate the most duplicates.

## FR-049 — Duplicate Trend Analytics

The system shall track duplicate rates over time.

## FR-050 — Data Quality Score

The system shall calculate lead data-quality scores.

## FR-051 — AI Performance Analytics

The system shall measure:

```text
AI Detection Precision
AI Detection Recall
AI False Positive Rate
AI False Negative Rate
Human Override Rate
Auto-Merge Accuracy
Review Acceptance Rate
```

## FR-052 — Human Performance Analytics

The system shall measure:

```text
Reviews Completed
Merge Decisions
Rejection Decisions
Average Review Time
Human Override Rate
Post-Merge Correction Rate
```

## FR-053 — AI vs Human Comparison

The platform shall compare AI and human duplicate decisions.

## FR-054 — Feedback Loop

Human decisions shall be stored as labeled outcomes for future model improvement where permitted.

## FR-055 — Duplicate Pattern Detection

AI shall identify recurring patterns that cause duplicate creation.

Example:

```text
Source:
Website Lead Form

Detected Pattern:
Users submit multiple forms using different email aliases.

Recommendation:
Enable identity-level duplicate prevention.
```

## FR-056 — Policy Recommendations

AI shall recommend improvements to duplicate-prevention policies.

## FR-057 — Simulation

Users shall be able to simulate a deduplication policy before activating it.

## FR-058 — Historical Replay

Users shall be able to replay historical records against a new deduplication policy.

## FR-059 — Conflict Detection

The system shall detect conflicts such as:

```text
Different owners
Different companies
Different phones
Different emails
Different countries
Different account relationships
Different lifecycle stages
Different consent states
```

## FR-060 — Consent Preservation

The merge engine shall preserve the strictest applicable consent and communication-preference constraints.

## FR-061 — Suppression Preservation

Do-not-contact and suppression states shall not be accidentally removed through merging.

## FR-062 — Compliance Preservation

The system shall preserve applicable privacy, retention, and deletion requirements.

---

## 10. AI Deduplication Decision Architecture

```text
Incoming Lead
      ↓
Data Normalization
      ↓
Feature Extraction
      ↓
Candidate Blocking
      ↓
Exact Matching
      ↓
Fuzzy Matching
      ↓
Semantic Matching
      ↓
Entity Resolution Model
      ↓
Similarity Scoring
      ↓
Business Constraint Validation
      ↓
Duplicate Confidence
      ↓
Risk Assessment
      ↓
 ┌────────────────────────────┐
 │ High Confidence            │
 │                            │
 │ Automatic Decision         │
 └────────────────────────────┘

 ┌────────────────────────────┐
 │ Medium Confidence          │
 │                            │
 │ Human Review               │
 └────────────────────────────┘

 ┌────────────────────────────┐
 │ Low Confidence             │
 │                            │
 │ Keep Separate              │
 └────────────────────────────┘
```

---

## 11. Hybrid AI + Human Workflow

```text
Lead
 ↓
AI Detection
 ↓
AI Confidence
 ↓
Risk Evaluation
 ↓
Policy Evaluation
 ↓
 ┌──────────────────────────┐
 │ Low Risk + High Confidence
 │                          │
 │ Auto-Resolve             │
 └──────────────────────────┘

 ┌──────────────────────────┐
 │ Medium Risk              │
 │                          │
 │ Human Review             │
 └──────────────────────────┘

 ┌──────────────────────────┐
 │ High Risk                │
 │                          │
 │ Mandatory Human Approval │
 └──────────────────────────┘
```

AI shall never bypass mandatory human approval rules.

---

## 12. Canonical Record Selection

The canonical record scoring system may consider:

```text
Canonical Score =
    Data Completeness
  + Data Freshness
  + Source Reliability
  + Verification Level
  + Historical Engagement
  + Existing Ownership
  + Account Relationship
  + Conversion History
  + Revenue Relationship
```

The system shall distinguish between:

```text
Identity Resolution
```

and:

```text
Canonical Data Selection
```

A record may be correctly identified as a duplicate without automatically being selected as the canonical record.

---

## 13. Field-Level Merge Strategy

For every conflicting field, the system shall support strategies such as:

```text
PREFER_CANONICAL
PREFER_NEWEST
PREFER_TRUSTED_SOURCE
PREFER_VERIFIED
PREFER_NON_EMPTY
AI_RECOMMENDED
HUMAN_SELECTED
CUSTOM_RULE
```

Example:

```text
Field: Phone

Lead A:
+1-202-555-0101

Lead B:
+1-202-555-0199

AI Recommendation:
+1-202-555-0199

Reason:
Most recently verified source.
```

---

## 14. Duplicate Types

The system shall classify duplicates including:

```text
EXACT_DUPLICATE
NEAR_DUPLICATE
FUZZY_DUPLICATE
SEMANTIC_DUPLICATE
CONTACT_DUPLICATE
COMPANY_DUPLICATE
CROSS_SOURCE_DUPLICATE
IMPORT_DUPLICATE
CRM_DUPLICATE
FORM_DUPLICATE
API_DUPLICATE
HISTORICAL_DUPLICATE
```

---

## 15. Duplicate Data Model

## LeadDuplicateCandidate

```text
LeadDuplicateCandidate
├── id
├── tenant_id
├── organization_id
├── workplace_id
├── lead_a_id
├── lead_b_id
├── duplicate_type
├── match_method
├── similarity_score
├── confidence_score
├── risk_score
├── evidence
├── ai_model_id
├── ai_model_version
├── policy_id
├── policy_version
├── status
├── reviewed_by
├── reviewed_at
├── created_at
└── updated_at
```

## DuplicateCluster

```text
DuplicateCluster
├── id
├── tenant_id
├── organization_id
├── workplace_id
├── member_count
├── canonical_lead_id
├── confidence_score
├── risk_score
├── status
├── created_at
└── updated_at
```

## MergeOperation

```text
MergeOperation
├── id
├── tenant_id
├── cluster_id
├── canonical_lead_id
├── merged_lead_ids
├── actor_id
├── actor_type
├── merge_strategy
├── field_changes
├── relationship_changes
├── source_provenance
├── ai_model_version
├── policy_version
├── status
├── rollback_available
├── created_at
└── completed_at
```

---

## 16. API Requirements

The module should expose APIs conceptually equivalent to:

```http
POST   /api/v1/leads/deduplication/check
POST   /api/v1/leads/deduplication/detect
POST   /api/v1/leads/deduplication/scan

GET    /api/v1/leads/{lead_id}/duplicates
GET    /api/v1/duplicates
GET    /api/v1/duplicates/{duplicate_id}

POST   /api/v1/duplicates/{duplicate_id}/confirm
POST   /api/v1/duplicates/{duplicate_id}/reject
POST   /api/v1/duplicates/{duplicate_id}/protect

POST   /api/v1/duplicates/{duplicate_id}/merge
POST   /api/v1/duplicates/{duplicate_id}/unmerge
POST   /api/v1/duplicates/{duplicate_id}/preview

POST   /api/v1/duplicates/bulk-detect
POST   /api/v1/duplicates/bulk-review
POST   /api/v1/duplicates/bulk-merge

POST   /api/v1/deduplication/ai/match
POST   /api/v1/deduplication/ai/explain
POST   /api/v1/deduplication/ai/recommend

POST   /api/v1/deduplication/simulate
POST   /api/v1/deduplication/replay

GET    /api/v1/deduplication/analytics
GET    /api/v1/deduplication/quality
GET    /api/v1/deduplication/audit
```

---

## 17. Event Requirements

The service shall publish and consume events such as:

```text
LeadCreated
LeadImported
LeadUpdated
LeadNormalized

DuplicateCheckRequested
DuplicateCheckCompleted

DuplicateCandidateCreated
DuplicateCandidateUpdated
DuplicateConfirmed
DuplicateRejected

DuplicateClusterCreated
DuplicateClusterUpdated

MergeRequested
MergeApproved
MergeRejected
MergeStarted
MergeCompleted
MergeFailed
MergeRolledBack

LeadMerged
LeadUnmerged

DuplicateReviewRequested
DuplicateReviewCompleted

DuplicatePolicyChanged
DuplicateModelChanged

DuplicateSLAExceeded

DataQualityIssueDetected
DataQualityIssueResolved
```

---

## 18. SalesGenie Integration

The Lead Deduplication module shall integrate with:

```text
Lead Discovery
        ↓
Lead Enrichment
        ↓
Lead Qualification
        ↓
Lead Segmentation
        ↓
Lead Deduplication
        ↓
Lead Scoring
        ↓
Lead Routing
        ↓
Lead Assignment
        ↓
Sales Sequence
        ↓
Outreach Automation
        ↓
Opportunity Management
        ↓
Deal Management
        ↓
Sales Forecasting
        ↓
Sales Analytics
```

Deduplication should occur both:

```text
Before Lead Qualification
```

and:

```text
Continuously throughout the lead lifecycle
```

when appropriate.

---

## 19. SalesGenie AI Agent Integration

The module shall integrate with the multi-agent architecture.

Potential agents:

```text
Lead Discovery Agent
Lead Enrichment Agent
Lead Qualification Agent
Lead Deduplication Agent
Lead Segmentation Agent
Lead Scoring Agent
Lead Routing Agent
Lead Assignment Agent
Sales Research Agent
Outreach Agent
Revenue Intelligence Agent
Data Quality Agent
Human Escalation Agent
```

The AI Deduplication Agent shall:

1. Receive duplicate-detection requests.
2. Normalize identity information.
3. Generate candidate records.
4. Compare candidate entities.
5. Calculate similarity.
6. Determine confidence.
7. Estimate merge risk.
8. Explain the decision.
9. Recommend a canonical record.
10. Recommend field-level values.
11. Escalate ambiguous cases.
12. Execute authorized automatic actions.
13. Monitor post-merge outcomes.
14. Learn from validated human decisions.

---

## 20. Duplicate Prevention During Lead Creation

```text
New Lead
   ↓
Normalize
   ↓
Check Existing Identity
   ↓
 ┌──────────────────────┐
 │ Exact Match          │
 │                      │
 │ Block / Update       │
 └──────────────────────┘

 ┌──────────────────────┐
 │ High AI Confidence   │
 │                      │
 │ Existing Lead Match  │
 └──────────────────────┘

 ┌──────────────────────┐
 │ Ambiguous            │
 │                      │
 │ Create + Review      │
 └──────────────────────┘

 ┌──────────────────────┐
 │ No Match             │
 │                      │
 │ Create Lead          │
 └──────────────────────┘
```

The exact behavior shall be configurable per organization.

---

## 21. Duplicate Outreach Prevention

Once two records are confirmed to represent the same person, SalesGenie shall be able to consolidate outreach eligibility.

The system shall prevent configured scenarios such as:

```text
Lead A → Email Sequence #1
Lead B → Email Sequence #2

Same Person
       ↓
Potential Duplicate Outreach
       ↓
Prevent / Consolidate
```

The system shall preserve the most restrictive applicable communication state.

---

## 22. CRM Synchronization

The module shall support synchronization with supported systems including:

```text
Salesforce
HubSpot
Zendesk
Gmail
Microsoft Teams
Slack
Google Workspace
Other configured CRM/Data Sources
```

Synchronization shall support:

* Duplicate detection
* External ID mapping
* Merge propagation
* Conflict detection
* Retry
* Reconciliation
* Failure handling
* Source attribution

---

## 23. Data Provenance

The system shall preserve:

```text
Original Lead ID
Original Source
Source System
Source Timestamp
Original Field Value
Canonical Field Value
Selection Method
Selection Actor
Selection Timestamp
```

Example:

```text
Canonical Email:
john@example.com

Source:
CRM

Selected By:
AI

Reason:
Verified CRM record

Confidence:
0.98
```

---

## 24. Security Requirements

The deduplication engine shall enforce:

* Authentication
* Authorization
* RBAC
* Fine-grained permissions
* Tenant isolation
* Organization isolation
* Workplace isolation
* Encryption in transit
* Encryption at rest
* Audit logging
* Rate limiting
* API validation
* Input sanitization
* AI output validation
* Secure secret management
* Data access policies
* Privacy controls
* Data retention controls

AI agents shall operate under the same tenant and permission boundaries as human users.

---

## 25. AI Security Requirements

The AI deduplication system shall:

1. Prevent cross-tenant candidate matching.
2. Prevent cross-organization matching unless explicitly authorized.
3. Treat lead data as untrusted input.
4. Protect against prompt injection.
5. Validate structured AI outputs.
6. Prevent unauthorized merge actions.
7. Require deterministic policy validation before merge execution.
8. Preserve model-version information.
9. Preserve decision evidence.
10. Support human review for high-risk decisions.

AI confidence shall never replace authorization.

---

## 26. Privacy Requirements

The system shall support configurable privacy policies for:

```text
Personal Data
Contact Information
Phone Numbers
Email Addresses
Social Profiles
Location Data
Communication Preferences
Consent
Suppression
Deletion Requests
Retention Policies
```

Deduplication shall not cause deleted or restricted personal data to be unintentionally restored.

---

## 27. Performance Requirements

Target production objectives:

```text
Exact duplicate check:
P95 < 100 ms

Cached duplicate lookup:
P95 < 150 ms

Fuzzy duplicate check:
P95 < 500 ms

AI duplicate analysis:
P95 < 3 seconds

Merge preview:
P95 < 1 second

Simple merge:
P95 < 500 ms
```

Large batch operations shall be asynchronous.

---

## 28. Scalability Requirements

The platform shall be designed to support:

```text
10M+ leads
Millions of duplicate candidates
Millions of duplicate clusters
Large historical datasets
Thousands of organizations
High-volume imports
High-frequency API ingestion
Large CRM synchronization workloads
Concurrent duplicate checks
```

The deduplication service shall support horizontal scaling.

---

## 29. Reliability Requirements

The system shall support:

* Idempotent operations
* Transactional merges
* Distributed locking where necessary
* Retry policies
* Dead-letter queues
* Circuit breakers
* Timeouts
* Reconciliation
* Recovery
* Rollback
* Graceful degradation

---

## 30. Graceful Degradation

The system shall use the following fallback hierarchy:

```text
AI Entity Resolution
       ↓ failure
Fuzzy Matching
       ↓ failure
Exact Matching
       ↓ failure
Deterministic Business Rules
       ↓ failure
Human Review
```

AI infrastructure failure shall not cause the entire lead-ingestion pipeline to fail.

---

## 31. Observability Requirements

The system shall monitor:

```text
Duplicate Detection Latency
Duplicate Detection Throughput
Candidate Generation Rate
Duplicate Precision
Duplicate Recall
False Positive Rate
False Negative Rate
Auto-Merge Rate
Human Review Rate
Merge Failure Rate
Rollback Rate
Duplicate Creation Rate
Duplicate Resolution Rate
AI Confidence
AI Override Rate
CRM Sync Failure Rate
```

Every deduplication transaction shall support distributed tracing.

---

## 32. Data Quality Metrics

The platform shall provide:

```text
Duplicate Rate
Unique Lead Rate
Duplicate Resolution Rate
Unresolved Duplicate Rate
False Positive Rate
False Negative Rate
Average Duplicate Cluster Size
Merge Success Rate
Merge Correction Rate
Source Duplicate Rate
Data Completeness
Data Freshness
Identity Confidence
```

---

## 33. AI Performance Evaluation

The system shall measure:

```text
Precision
Recall
F1 Score
ROC-AUC where applicable
False Positive Rate
False Negative Rate
Human Agreement Rate
Human Override Rate
Auto-Merge Accuracy
Post-Merge Correction Rate
```

Evaluation shall distinguish between:

```text
Detection Accuracy
```

and:

```text
Merge Decision Accuracy
```

---

## 34. Human Review Prioritization

AI shall prioritize duplicate candidates according to:

```text
Confidence
Merge Risk
Lead Value
Revenue Potential
Existing Opportunity
Existing Deal
Strategic Account
Customer Relationship
Data Conflict Severity
```

Example:

```text
High-value enterprise lead
+
Medium-confidence duplicate
+
Existing active opportunity
        ↓
Priority: CRITICAL
Human Review Required
```

---

## 35. Duplicate Risk Model

The system shall calculate merge risk using factors such as:

```text
Identity Ambiguity
Field Conflict
Ownership Conflict
Account Conflict
Opportunity Conflict
Consent Conflict
Source Reliability
Record Freshness
Historical Activity
Revenue Impact
```

Example:

```text
Duplicate Confidence = 0.97
Merge Risk            = 0.21

Result:
Potential Auto-Merge
```

versus:

```text
Duplicate Confidence = 0.91
Merge Risk            = 0.82

Result:
Mandatory Human Review
```

---

## 36. Merge Governance

Organizations shall be able to configure:

```text
Auto-Merge Threshold
Human Review Threshold
Protected Lead Rules
Protected Account Rules
Required Approval Roles
Maximum Bulk Merge Size
Rollback Availability
Merge Retention Period
Source Reliability
Field Precedence
```

---

## 37. Assignment and Ownership Preservation

When merging duplicate leads, SalesGenie shall resolve ownership according to configured policies.

Example:

```text
Lead A
Owner: Agent A

Lead B
Owner: Agent B

Confirmed Duplicate
        ↓
Ownership Resolution Policy
        ↓
Canonical Owner
```

The system shall not silently transfer ownership.

---

## 38. Opportunity and Deal Protection

If duplicate leads have active commercial relationships:

```text
Lead A → Opportunity A
Lead B → Opportunity B
```

the merge engine shall detect the conflict before merging.

The system shall require appropriate policy or human review.

---

## 39. Historical Replay

The platform shall allow administrators to evaluate a deduplication policy against historical records.

Example:

```text
Current Policy:
Email Exact Match

New Policy:
Email + Phone + Company Domain + AI Entity Resolution

Historical Dataset:
1,000,000 leads

Simulation Result:
Potential Duplicates: 84,230
High Confidence: 61,420
Human Review: 17,800
Low Confidence: 5,010
```

Historical replay shall not mutate production data.

---

## 40. Deduplication Experimentation

The system shall support controlled comparison of strategies.

Example:

```text
Control:
Rule-Based Matching

Experiment:
AI Entity Resolution
```

Metrics shall include:

```text
Precision
Recall
False Positives
False Negatives
Human Review Volume
Merge Accuracy
Processing Cost
Processing Latency
```

---

## 41. Duplicate Source Analytics

The platform shall identify high-risk sources.

Example:

```text
Lead Source Analysis

Website Forms       → 32% duplicate rate
CSV Import          → 21% duplicate rate
CRM Sync            → 17% duplicate rate
API                 → 11% duplicate rate
Manual Entry        → 8% duplicate rate
```

The system shall recommend preventive actions.

---

## 42. Duplicate Prevention Recommendations

AI may recommend:

```text
Enable email normalization
Enable phone normalization
Require company domain
Add external ID
Enable identity-level suppression
Enable pre-import duplicate checks
Require human approval for high-value merges
Improve CRM synchronization
```

Recommendations shall require authorization before changing production policies.

---

## 43. Audit Trail

Every important operation shall record:

```text
Actor
Actor Type
Action
Lead IDs
Duplicate IDs
Previous State
New State
Reason
AI Model
AI Confidence
Policy Version
Timestamp
Correlation ID
Source System
```

Audit logs shall be immutable according to platform governance policies.

---

## 44. Failure Recovery

The system shall support:

```text
Merge Failure
      ↓
Transaction Rollback
      ↓
Retry
      ↓
Dead Letter Queue
      ↓
Human Investigation
```

CRM synchronization failures shall not corrupt the canonical SalesGenie record.

---

## 45. Reconciliation

The system shall periodically compare:

```text
SalesGenie Canonical Identity
        vs
External CRM Identity
        vs
Source Records
```

and identify:

```text
Missing Merge
Incorrect Merge
Stale Mapping
Conflicting External ID
Duplicate External Record
Synchronization Failure
```

---

## 46. Acceptance Criteria

* [ ] Exact duplicate detection works.
* [ ] Fuzzy duplicate detection works.
* [ ] AI entity resolution works.
* [ ] Duplicate confidence is calculated.
* [ ] Duplicate explanations are available.
* [ ] Duplicate candidates are generated.
* [ ] Duplicate clusters are supported.
* [ ] Human review queue works.
* [ ] Human duplicate approval works.
* [ ] Human duplicate rejection works.
* [ ] Human override works.
* [ ] Manual merge works.
* [ ] AI-assisted merge works.
* [ ] Automatic merge works under configured policies.
* [ ] Merge preview works.
* [ ] Canonical record selection works.
* [ ] Field-level conflict resolution works.
* [ ] Data provenance is preserved.
* [ ] Merge history is preserved.
* [ ] Unmerge/recovery works where supported.
* [ ] Protected records are respected.
* [ ] Bulk detection works.
* [ ] Bulk review works.
* [ ] Bulk merge works.
* [ ] Dry-run mode works.
* [ ] Historical replay works.
* [ ] Duplicate simulation works.
* [ ] Duplicate prevention works during lead creation.
* [ ] Import deduplication works.
* [ ] API deduplication works.
* [ ] CRM deduplication works.
* [ ] Duplicate outreach protection works.
* [ ] Assignment relationships are preserved.
* [ ] Opportunity relationships are preserved.
* [ ] Deal relationships are preserved.
* [ ] Conversation history is preserved.
* [ ] Campaign attribution is preserved.
* [ ] Consent restrictions are preserved.
* [ ] Suppression states are preserved.
* [ ] Tenant isolation is enforced.
* [ ] Organization isolation is enforced.
* [ ] Workplace isolation is enforced.
* [ ] RBAC is enforced.
* [ ] Fine-grained permissions are enforced.
* [ ] Merge operations are transactional.
* [ ] Concurrent merges are safely handled.
* [ ] Failed merges can recover.
* [ ] CRM synchronization works.
* [ ] Reconciliation works.
* [ ] Audit logging works.
* [ ] AI model versioning works.
* [ ] Policy versioning works.
* [ ] AI explanations work.
* [ ] AI confidence thresholds work.
* [ ] Human approval thresholds work.
* [ ] AI performance analytics work.
* [ ] Human review analytics work.
* [ ] Duplicate source analytics work.
* [ ] Data-quality metrics work.
* [ ] Distributed tracing works.
* [ ] Duplicate detection scales horizontally.
* [ ] AI failure has deterministic fallbacks.
* [ ] High-risk merges require appropriate human governance.

---

## 47. FAANG-Level Product Outcome

SalesGenie's Lead Deduplication module should evolve beyond simple duplicate checking into an:

**AI-Powered Identity Resolution, Data Quality, and Revenue Integrity Engine**

For every potentially duplicated lead, SalesGenie should be able to answer:

```text
ARE these records the same entity?

WHY does the system believe they are duplicates?

HOW confident is the decision?

WHAT evidence supports the decision?

WHICH record should become canonical?

WHICH field values should survive?

WHAT relationships will be affected?

WHAT is the risk of merging?

SHOULD AI merge automatically?

SHOULD a human review it?

WHO approved the merge?

WHAT changed after merging?

CAN the operation be recovered?

DID the merge improve data quality?
```

The complete intelligence loop should be:

```text
Lead Ingestion
      ↓
Normalization
      ↓
Identity Resolution
      ↓
Duplicate Detection
      ↓
AI Similarity Analysis
      ↓
Risk Evaluation
      ↓
Human / AI Decision
      ↓
Canonical Record Selection
      ↓
Field-Level Consolidation
      ↓
Relationship Preservation
      ↓
CRM Synchronization
      ↓
Outreach Protection
      ↓
Audit
      ↓
Data Quality Analytics
      ↓
Human Feedback
      ↓
AI Improvement
      ↓
Continuous Duplicate Prevention
```

The ultimate goal is not simply to remove duplicate records.

The goal is to create a **trusted, continuously maintained, explainable, tenant-isolated customer identity layer for SalesGenie that improves lead quality, prevents duplicate sales activity, protects revenue attribution, preserves customer relationships, and continuously learns from AI and human decisions.**
