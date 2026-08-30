# SalesGenie — Hybrid Search Requirements Specification

**Document Type:** User Requirements, System Requirements & Functional Requirements  
**Project:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Capability:** Hybrid Search  
**Requirement Level:** FAANG / Enterprise Production Grade  
**Search Paradigm:** Dense Semantic Retrieval + Sparse Lexical Retrieval + AI Reranking + Human Verification  
**Primary Consumers:** AI Agents, Human Agents, RAG Pipelines, Workflows, Administrators, End Customers  
**Version:** 1.0  
**Status:** Proposed  

---

## 1. Purpose

The Hybrid Search subsystem shall provide SalesGenie with an enterprise-grade information retrieval layer that combines:

- Dense vector retrieval
- Sparse lexical retrieval
- BM25-style keyword retrieval
- Semantic similarity
- Metadata filtering
- Query understanding
- Query expansion
- Reciprocal Rank Fusion
- Optional cross-encoder reranking
- Authorization-aware retrieval
- Result deduplication
- Source authority and freshness ranking
- Human verification
- AI-assisted retrieval
- RAG integration

Hybrid Search shall solve the limitations of using only semantic or only keyword search.

Dense retrieval shall capture semantic relationships even when query and document vocabulary differs, while lexical retrieval shall preserve exact matching for identifiers, product names, error codes, technical terms, and other high-value entities.

The architecture shall support configurable weighted fusion between retrieval strategies. A weighted Reciprocal Rank Fusion approach is recommended because hybrid retrieval can balance semantic relevance with exact lexical matching. :contentReference[oaicite:0]{index=0}

---

## 2. Scope

Hybrid Search shall support retrieval across:

1. Knowledge-base articles
2. Product documentation
3. FAQs
4. Support documentation
5. Troubleshooting guides
6. Policies
7. SOPs
8. Customer records
9. Support tickets
10. Conversations
11. Chat history
12. Email history
13. WhatsApp conversations
14. Telegram conversations
15. Facebook Messenger conversations
16. SMS conversations
17. Voice transcripts
18. Webchat conversations
19. Social inbox data
20. CRM records
21. Leads
22. Companies
23. Contacts
24. Opportunities
25. Sales activities
26. Agent memory
27. Agent-generated summaries
28. Uploaded documents
29. Workflow records
30. Integration data
31. Structured enterprise records
32. Unstructured enterprise content

---

## 3. Core Hybrid Search Model

The system shall combine multiple retrieval signals rather than relying on one retrieval mechanism.

```text
                         User Query
                             |
                             v
                  Query Understanding
                             |
              +--------------+--------------+
              |                             |
              v                             v
       Query Normalization            Entity Extraction
              |                             |
              +--------------+--------------+
                             |
                             v
                    Query Transformation
                             |
               +-------------+-------------+
               |                           |
               v                           v
        Dense Query Embedding        Lexical Query
               |                           |
               v                           v
       Vector Retrieval                 BM25
               |                           |
          Top-N Dense                 Top-N Sparse
               |                           |
               +-------------+-------------+
                             |
                             v
                    Candidate Generation
                             |
                             v
                    Result Fusion / RRF
                             |
                             v
                     Candidate Reranking
                             |
                             v
                   Authorization Filtering
                             |
                             v
                     Deduplication
                             |
                             v
                  Freshness / Authority
                             |
                             v
                    Relevance Threshold
                             |
                             v
                         Top-K
                             |
                +------------+------------+
                |                         |
                v                         v
          Human Agent UI              AI Agent / RAG
```

---

## 4. Retrieval Principles

## 4.1 Dense Retrieval

Dense retrieval shall identify semantically related content even when lexical overlap is limited.

Example:

```text
Query:
"How can I recover access to my account?"

Document:
"Procedure for restoring credentials after authentication lockout."
```

The system should identify the semantic relationship between these expressions.

Dense retrieval may use L2-normalized embeddings with cosine similarity or equivalent inner-product similarity. This architecture is consistent with retrieval systems where normalized embeddings and inner-product search approximate cosine similarity.

---

## 4.2 Sparse Retrieval

Sparse retrieval shall provide strong lexical matching for:

* Product names
* SKU
* Ticket IDs
* Order IDs
* Invoice IDs
* Error codes
* API identifiers
* Contract IDs
* Policy codes
* Technical terminology
* Customer names

BM25 shall be supported as the primary sparse retrieval strategy.

---

## 4.3 Hybrid Retrieval

Hybrid Search shall combine dense and sparse retrieval.

Conceptually:

```text
Hybrid Score
=
Dense Retrieval Signal
+
Lexical Retrieval Signal
+
Optional Reranking Signal
+
Business Ranking Signals
```

The exact score calculation shall be configurable.

---

## 5. User Requirements

## UR-HS-001 — Natural Language Search

Users shall be able to search SalesGenie using natural-language queries.

Example:

```text
"Why did the customer's subscription stop working?"
```

---

## UR-HS-002 — Semantic Understanding

The system shall retrieve conceptually relevant information even when the exact query vocabulary does not occur in the source.

---

## UR-HS-003 — Exact Matching

The system shall preserve exact matching capabilities for high-value terms.

Examples:

```text
ERR-4012
INV-2026-00152
SKU-PRO-ENTERPRISE
TICKET-82931
```

---

## UR-HS-004 — Hybrid Search

Users shall receive results generated from both semantic and lexical retrieval.

---

## UR-HS-005 — Contextual Search

Search shall consider authorized context from:

* Active conversation
* Customer
* Ticket
* Organization
* Product
* Subscription
* Lead
* Opportunity
* Workflow
* Agent state

---

## UR-HS-006 — Customer-Centric Search

Human and AI agents shall be able to search information related to a specific customer.

---

## UR-HS-007 — Conversation Search

Users shall be able to search previous conversations using semantic and lexical signals.

---

## UR-HS-008 — Cross-Channel Search

Users shall be able to search across authorized channels.

Supported channels shall include:

* Chat
* Email
* WhatsApp
* Telegram
* Facebook Messenger
* SMS
* Voice
* Webchat
* Social inbox

---

## UR-HS-009 — Knowledge Base Search

Users shall be able to retrieve relevant knowledge-base content using hybrid retrieval.

---

## UR-HS-010 — Support Search

Support agents shall be able to retrieve:

* Troubleshooting instructions
* FAQs
* Policies
* Product documentation
* Previous resolutions
* Related tickets
* Customer history

---

## UR-HS-011 — Sales Search

Sales representatives shall be able to retrieve:

* Leads
* Companies
* Contacts
* Opportunities
* Product information
* Previous interactions
* Sales notes
* Account intelligence

---

## UR-HS-012 — AI Agent Search

AI agents shall be able to invoke Hybrid Search as an authorized tool.

---

## UR-HS-013 — Human Agent Search

Human agents shall be able to invoke Hybrid Search from the SalesGenie dashboard.

---

## UR-HS-014 — RAG Search

Hybrid Search shall provide context to the RAG pipeline.

```text
Query
  ↓
Hybrid Retrieval
  ↓
Relevant Evidence
  ↓
RAG Context
  ↓
LLM
  ↓
Grounded Response
```

Hybrid retrieval is particularly appropriate for RAG because it combines exact term matching with semantic retrieval when lexical overlap is insufficient.

---

## UR-HS-015 — Search Filters

Users shall be able to filter results by:

* Customer
* Organization
* Tenant
* Channel
* Source
* Document type
* Product
* Date
* Language
* Department
* User
* Agent
* Ticket
* Lead
* Opportunity
* Access level

---

## UR-HS-016 — Search Scope

Users shall be able to define search scope.

Supported scopes shall include:

```text
Current Conversation
Customer
Ticket
Organization
Knowledge Base
CRM
Tenant
Global Authorized Data
```

---

## UR-HS-017 — Search Result Ranking

Users shall receive results ordered according to combined relevance.

---

## UR-HS-018 — Search Result Transparency

Human users shall be able to inspect:

* Result source
* Relevant snippet
* Document
* Timestamp
* Relevance
* Source type
* Citation
* Customer context

---

## UR-HS-019 — Search Citations

AI-facing retrieval results shall contain source provenance whenever available.

---

## UR-HS-020 — Search Confidence

The system shall indicate when retrieved information has insufficient relevance.

---

## UR-HS-021 — No-Answer Behavior

When no sufficiently relevant evidence exists, the system shall not fabricate a result.

---

## UR-HS-022 — Search Refinement

Users shall be able to refine searches through:

* Query modification
* Filters
* Search scope
* Top-K
* Date range
* Source
* Product
* Customer

---

## UR-HS-023 — Search Suggestions

The system should provide relevant search suggestions.

---

## UR-HS-024 — Search History

Authorized users shall be able to access recent searches according to tenant policy.

---

## UR-HS-025 — Saved Searches

Human agents and administrators should be able to save frequently used searches.

---

## UR-HS-026 — Multilingual Search

The system shall support multilingual retrieval when the configured embedding and lexical systems support the language.

---

## UR-HS-027 — Cross-Language Retrieval

The system should support semantic retrieval across supported languages.

---

## UR-HS-028 — Search Feedback

Human users shall be able to provide feedback such as:

```text
Relevant
Not Relevant
Outdated
Incorrect
Duplicate
Incomplete
Helpful
```

---

## 6. System Requirements

## SR-HS-001 — Dual Retrieval Architecture

The system shall maintain independent:

1. Dense retrieval pipeline
2. Sparse retrieval pipeline

These pipelines shall operate independently before candidate fusion.

---

## SR-HS-002 — Dense Retrieval Engine

The system shall support a vector retrieval engine capable of:

* Embedding lookup
* Similarity search
* Top-N retrieval
* Metadata filtering
* Tenant isolation
* Version-aware retrieval

---

## SR-HS-003 — Sparse Retrieval Engine

The system shall support a lexical retrieval engine capable of:

* BM25
* Exact matching
* Phrase matching
* Token matching
* Field weighting
* Metadata filtering

---

## SR-HS-004 — Query Embedding

The query shall be converted into an embedding using the configured embedding model.

---

## SR-HS-005 — Document Embedding

Indexed chunks shall have embeddings generated using the configured embedding pipeline.

---

## SR-HS-006 — Embedding Normalization

Where required by the selected embedding model and similarity strategy, embeddings shall be normalized consistently between indexing and query time.

---

## SR-HS-007 — Stable Vector Mapping

Vector identifiers shall maintain stable mappings to:

* Document IDs
* Chunk IDs
* Tenant IDs
* Source IDs

A stable mapping between vector IDs and chunk identifiers is required to reconstruct retrieved evidence correctly.

---

## SR-HS-008 — Candidate Retrieval

The system shall retrieve independent candidate sets from dense and sparse search.

Recommended production configuration:

```text
Dense Candidate Count: 30
Sparse Candidate Count: 30
```

The exact values shall be configurable.

A hybrid retrieval design can retrieve top candidates independently from dense and lexical search before fusion.

---

## SR-HS-009 — Candidate Pool

The system shall merge candidates from:

```text
Dense Retrieval
+
Sparse Retrieval
+
Optional Additional Retrieval Sources
```

---

## SR-HS-010 — Reciprocal Rank Fusion

The system shall support Reciprocal Rank Fusion.

Recommended formulation:

```text
RRF(d) =
Σ [ weight_i / (k + rank_i(d)) ]
```

Where:

```text
d       = candidate document
k       = configurable RRF constant
rank_i  = rank from retrieval strategy i
weight_i = strategy weight
```

---

## SR-HS-011 — Configurable RRF Weights

The system shall allow independent weights for:

```text
Dense Retrieval
Sparse Retrieval
Reranker
Freshness
Source Authority
Business Priority
```

A configuration such as:

```text
RRF k = 60
BM25 Weight = 2.0
Dense Weight = 1.0
```

shall be supported as one possible tenant configuration.

---

## SR-HS-012 — Dynamic Retrieval Weighting

The system should support dynamically adjusting retrieval weights based on query characteristics.

Example:

```text
Query contains error code
        ↓
Increase lexical weight

Conceptual customer question
        ↓
Increase dense weight
```

---

## SR-HS-013 — Query Classification

The system should classify queries into retrieval categories such as:

```text
Exact Lookup
Semantic Question
Entity Search
Troubleshooting
Policy Search
Product Search
Customer Search
Sales Research
Conversation Search
Mixed Query
```

---

## SR-HS-014 — Query Rewriting

The system shall support retrieval-oriented query rewriting.

---

## SR-HS-015 — Entity Extraction

The system shall extract entities such as:

```text
Customer
Company
Product
Ticket
Order
Invoice
Subscription
SKU
Error Code
Lead
Opportunity
```

---

## SR-HS-016 — Lexical Query Expansion

The system should support query expansion for:

* Synonyms
* Aliases
* Product names
* Acronyms
* Entity names
* Technical terms

---

## SR-HS-017 — Dense Query Expansion

The system may generate additional semantic representations for complex queries.

---

## SR-HS-018 — HyDE Compatibility

The architecture shall support optional HyDE retrieval for queries where semantic mismatch is likely.

HyDE can generate a hypothetical passage representing the query intent and then embed that passage for retrieval.

HyDE shall remain optional because it introduces additional LLM computation and latency.

---

## SR-HS-019 — Cross-Encoder Compatibility

The architecture shall support optional cross-encoder reranking.

Cross-encoder reranking can score the query and candidate passage jointly and generally provide a more precise relevance signal than independent bi-encoder similarity.

---

## SR-HS-020 — Reranking Candidate Count

The reranker shall support a configurable candidate pool.

Recommended default:

```text
Initial Candidates: Up to 50
Final Results: Top 5
```

The exact values shall be configurable based on latency and infrastructure constraints.

---

## SR-HS-021 — Relevance Threshold

The system shall support configurable minimum relevance thresholds.

---

## SR-HS-022 — Result Ranking

Final ranking shall consider:

```text
Dense Relevance
Sparse Relevance
RRF Score
Reranker Score
Source Authority
Freshness
Customer Context
Product Context
Business Priority
Access Scope
```

---

## SR-HS-023 — Metadata Filtering

Metadata filtering shall occur as early as possible in the retrieval pipeline to reduce unnecessary candidate processing.

---

## SR-HS-024 — Authorization-Aware Retrieval

The system shall enforce:

```text
Authentication
RBAC
Tenant Isolation
Organization Isolation
Resource Permissions
Agent Permissions
```

---

## SR-HS-025 — Authorization Invariant

The system shall enforce:

```text
Authorization > Relevance
```

A highly relevant document shall never be returned to an unauthorized requester.

---

## SR-HS-026 — Tenant Isolation

Hybrid Search shall ensure strict isolation between tenants.

No retrieval operation shall expose:

* Embeddings
* Documents
* Chunks
* Metadata
* Search results
* Cached results
* Search history

belonging to another tenant.

---

## SR-HS-027 — Document Versioning

The search index shall support document versions.

---

## SR-HS-028 — Freshness

Newer authoritative content shall be preferred over obsolete content where business rules require it.

---

## SR-HS-029 — Deleted Content

Deleted or revoked documents shall be removed or invalidated from:

```text
Vector Index
Lexical Index
Cache
Search Metadata
RAG Retrieval
```

within the configured deletion SLA.

---

## SR-HS-030 — Incremental Indexing

The system shall support incremental indexing.

Only changed content should require reprocessing.

---

## SR-HS-031 — Bulk Indexing

The system shall support bulk indexing for:

* Tenant onboarding
* Knowledge-base migration
* Reindexing
* Embedding migration
* Search engine migration

---

## SR-HS-032 — Index Consistency

The following shall remain synchronized:

```text
Source Data
   ↕
Document
   ↕
Chunk
   ↕
Embedding
   ↕
Vector Index
   ↕
Lexical Index
   ↕
Metadata
```

---

## SR-HS-033 — Duplicate Detection

The system shall detect duplicate and near-duplicate content.

---

## SR-HS-034 — Result Deduplication

The final result set shall prevent redundant chunks from dominating retrieval.

---

## SR-HS-035 — Source Diversity

The ranking layer should support source diversity.

Example:

```text
5 results from one document
```

should be avoided when:

```text
2 knowledge articles
1 support ticket
1 product document
1 previous resolution
```

would provide stronger evidence.

---

## SR-HS-036 — Search API

The system shall expose a dedicated Hybrid Search API.

Example:

```http
POST /api/v1/search/hybrid
```

---

## SR-HS-037 — Search Request

Example request:

```json
{
  "query": "Why did the customer's enterprise subscription stop working?",
  "top_k": 5,
  "dense_top_k": 30,
  "sparse_top_k": 30,
  "rerank": true,
  "filters": {
    "customer_id": "customer_123",
    "product": "enterprise"
  },
  "search_scope": "customer"
}
```

---

## SR-HS-038 — Search Response

Example:

```json
{
  "query": "Why did the customer's enterprise subscription stop working?",
  "results": [
    {
      "document_id": "doc_123",
      "chunk_id": "chunk_456",
      "content": "Enterprise subscription troubleshooting...",
      "dense_score": 0.91,
      "sparse_score": 14.8,
      "rrf_score": 0.043,
      "rerank_score": 0.96,
      "source_type": "knowledge_base",
      "metadata": {},
      "citation": {}
    }
  ]
}
```

Internal scores may be hidden from end customers while remaining available to authorized debugging and evaluation systems.

---

## SR-HS-039 — Search Trace ID

Every search request shall receive a unique correlation ID.

---

## SR-HS-040 — Retrieval Traceability

The platform shall be able to trace:

```text
Search Request
    ↓
Query Processing
    ↓
Dense Retrieval
    ↓
Sparse Retrieval
    ↓
Candidate Fusion
    ↓
Reranking
    ↓
Authorization
    ↓
Deduplication
    ↓
Final Results
    ↓
RAG / Human Agent
```

---

## SR-HS-041 — Search Caching

The system should support secure caching of repeated searches.

---

## SR-HS-042 — Cache Key Isolation

Cache keys shall incorporate relevant security boundaries.

Example:

```text
tenant_id
user_id
authorization_scope
query_hash
filter_hash
index_version
embedding_version
search_configuration_version
```

---

## SR-HS-043 — Cache Security

Unauthorized users shall never receive cached results generated for another authorization context.

---

## SR-HS-044 — Rate Limiting

Hybrid Search shall support rate limiting at:

```text
Platform
Tenant
User
AI Agent
API Key
Workflow
Integration
```

---

## SR-HS-045 — Cost Controls

The system shall monitor costs associated with:

* Embeddings
* Reranking
* HyDE
* Vector search
* Lexical search
* Compute
* Storage
* Network
* External providers

---

## 7. Functional Requirements

## FR-HS-001 — Execute Hybrid Search

The system shall execute both dense and sparse retrieval for a hybrid-enabled query.

---

## FR-HS-002 — Generate Dense Representation

The system shall generate a dense vector representation of the query.

---

## FR-HS-003 — Execute Dense Retrieval

The system shall retrieve semantically similar candidates.

---

## FR-HS-004 — Generate Sparse Representation

The system shall tokenize and prepare the query for lexical retrieval.

---

## FR-HS-005 — Execute BM25 Retrieval

The system shall retrieve lexically relevant candidates using BM25 or an equivalent sparse ranking algorithm.

---

## FR-HS-006 — Preserve Exact Terms

Important query entities shall be preserved during lexical retrieval.

---

## FR-HS-007 — Entity Boosting

The system shall support boosting exact entity matches.

Example:

```text
Customer asks:
"What does ERR-4012 mean?"

ERR-4012
```

shall receive stronger lexical relevance than a generic semantically similar document.

---

## FR-HS-008 — Candidate Fusion

The system shall combine dense and sparse candidate lists.

---

## FR-HS-009 — RRF Ranking

The system shall calculate an aggregated RRF ranking.

---

## FR-HS-010 — Weighted Retrieval

The system shall support independent dense and sparse weights.

---

## FR-HS-011 — Dynamic Weight Selection

The system should select retrieval weights based on query characteristics when enabled.

---

## FR-HS-012 — Reranking

The system shall optionally rerank the fused candidate pool.

---

## FR-HS-013 — Cross-Encoder Reranking

The system shall support cross-encoder scoring for high-precision retrieval.

---

## FR-HS-014 — Top-K Selection

The system shall return the configured number of final results.

---

## FR-HS-015 — Result Thresholding

Results below the configured relevance threshold shall be excluded or marked low-confidence.

---

## FR-HS-016 — Result Deduplication

The system shall remove duplicate and near-duplicate results.

---

## FR-HS-017 — Source Diversity

The system shall optionally diversify final results across sources.

---

## FR-HS-018 — Metadata Filtering

The system shall apply metadata filters before final result delivery.

---

## FR-HS-019 — Authorization Filtering

The system shall remove unauthorized results.

---

## FR-HS-020 — Tenant Filtering

The system shall restrict all retrieval to the current tenant unless a higher-level authorized search scope explicitly exists.

---

## FR-HS-021 — Customer Filtering

The system shall support restricting results to a customer.

---

## FR-HS-022 — Organization Filtering

The system shall support organization-level retrieval.

---

## FR-HS-023 — Product Filtering

The system shall support product-specific retrieval.

---

## FR-HS-024 — Channel Filtering

The system shall support channel-specific retrieval.

---

## FR-HS-025 — Date Filtering

The system shall support:

```text
created_after
created_before
updated_after
updated_before
```

---

## FR-HS-026 — Language Filtering

The system shall support language-aware retrieval.

---

## FR-HS-027 — Search Scope

The system shall support:

```text
conversation
customer
ticket
organization
knowledge_base
crm
tenant
global_authorized
```

---

## FR-HS-028 — Query Rewriting

The system shall optionally transform the original query into a retrieval-optimized query.

---

## FR-HS-029 — Context Enrichment

The system shall optionally enrich the query using authorized conversation and customer context.

---

## FR-HS-030 — HyDE Retrieval

The system shall optionally generate a hypothetical answer/passsage for semantic retrieval.

---

## FR-HS-031 — Fallback Retrieval

If dense retrieval fails:

```text
Dense Retrieval
      ↓ failure
Sparse Retrieval
```

If sparse retrieval fails:

```text
Sparse Retrieval
      ↓ failure
Dense Retrieval
```

If both fail:

```text
No Evidence / Human Escalation
```

Fallback behavior shall never bypass authorization.

---

## FR-HS-032 — No-Result State

The system shall return an explicit no-result state.

Example:

```json
{
  "status": "no_relevant_results",
  "results": []
}
```

---

## FR-HS-033 — Low-Confidence State

The system shall return a low-confidence state when candidates exist but do not satisfy the configured threshold.

---

## FR-HS-034 — Clarification

The AI agent may request clarification when the query is ambiguous.

Example:

```text
"Which subscription plan are you referring to?"
```

---

## FR-HS-035 — RAG Integration

The system shall provide retrieved evidence to the RAG generation layer.

---

## FR-HS-036 — Context Compression

The system should optimize retrieved context before sending it to an LLM.

---

## FR-HS-037 — Citation Preservation

The retrieval system shall preserve source references through the RAG pipeline.

---

## FR-HS-038 — Human Verification

Human agents shall be able to inspect the sources used by AI.

---

## FR-HS-039 — Human Search Override

Human agents shall be able to manually execute broader or narrower searches where permitted.

---

## FR-HS-040 — AI Search Tool

AI agents shall invoke:

```text
semantic_search()
hybrid_search()
```

through the authorized agent tool framework.

---

## FR-HS-041 — Workflow Search

Workflows shall be able to invoke Hybrid Search as an automation action.

Example:

```text
Trigger
  ↓
Extract Query
  ↓
Hybrid Search
  ↓
Evaluate Results
  ↓
AI Agent
  ↓
Human Escalation
```

---

## FR-HS-042 — Search Feedback

Human agents shall be able to mark retrieved results as:

```text
Relevant
Irrelevant
Outdated
Incorrect
Duplicate
Incomplete
```

---

## FR-HS-043 — Feedback Storage

Search feedback shall be stored for retrieval-quality analysis.

---

## FR-HS-044 — Search Analytics

The system shall expose:

```text
Total Searches
Searches / Tenant
Searches / User
Searches / Agent
Dense Retrieval Count
Sparse Retrieval Count
Hybrid Retrieval Count
Reranking Count
No-Result Rate
Low-Confidence Rate
Average Latency
Cache Hit Rate
Error Rate
```

---

## FR-HS-045 — Retrieval Quality Evaluation

The platform shall support:

```text
Precision@K
Recall@K
MRR
NDCG
Hit Rate
Zero Result Rate
Reranking Gain
Grounded Answer Rate
Citation Accuracy
```

---

## FR-HS-046 — Human Evaluation

Human evaluators shall be able to judge:

* Relevance
* Completeness
* Correctness
* Authority
* Freshness
* Usefulness

---

## FR-HS-047 — AI Evaluation

The platform shall support automated evaluation of retrieval quality.

---

## FR-HS-048 — Retrieval Experiments

The system shall support experimentation with:

* Embedding models
* BM25 parameters
* Dense weights
* Sparse weights
* RRF parameters
* Rerankers
* Top-K
* Candidate count
* Thresholds
* Query rewriting
* HyDE

---

## FR-HS-049 — A/B Testing

Search configurations shall support controlled A/B testing.

---

## FR-HS-050 — Configuration Management

Authorized administrators shall configure:

```text
dense_model
sparse_engine
bm25_parameters
dense_weight
sparse_weight
rrf_k
dense_top_k
sparse_top_k
reranker
reranker_top_k
final_top_k
relevance_threshold
freshness_weight
authority_weight
source_priority
```

---

## FR-HS-051 — Tenant Configuration

Tenants shall be able to configure supported search behavior subject to platform-level constraints.

---

## FR-HS-052 — Platform Configuration

Super administrators shall be able to enforce:

* Maximum candidate count
* Maximum top-K
* Allowed models
* Allowed search engines
* Maximum reranking limits
* Rate limits
* Cost limits
* Security policies

---

## FR-HS-053 — Index Monitoring

Administrators shall be able to monitor:

```text
Document Count
Chunk Count
Vector Count
Lexical Document Count
Index Version
Failed Indexing
Stale Documents
Pending Index Jobs
Last Synchronization
```

---

## FR-HS-054 — Search Monitoring

Administrators shall be able to monitor:

```text
Dense Search Latency
Sparse Search Latency
Fusion Latency
Reranking Latency
Authorization Latency
Total Search Latency
```

---

## FR-HS-055 — Search Auditing

The system shall log security-relevant search operations.

Example:

```text
search_id
tenant_id
actor_id
actor_type
search_scope
query_hash
result_count
timestamp
configuration_version
index_version
```

---

## FR-HS-056 — Security Monitoring

The system shall detect abnormal retrieval behavior.

---

## FR-HS-057 — Data Leakage Prevention

The system shall prevent retrieval-based leakage of:

* Customer data
* Tenant data
* Internal documents
* Private conversations
* CRM information
* Agent memory

---

## FR-HS-058 — Index Rebuilding

Administrators shall be able to rebuild:

```text
Document Index
Tenant Index
Vector Index
Lexical Index
Hybrid Index
```

---

## FR-HS-059 — Embedding Migration

The system shall support migration to a new embedding model without unnecessary service interruption.

---

## FR-HS-060 — Search Configuration Versioning

Search configurations shall be versioned.

Each search result should be traceable to the configuration that generated it.

---

## 8. AI-Specific Requirements

## AI-HS-001 — Retrieval Planning

AI agents shall determine whether a query requires:

```text
Dense Search
Sparse Search
Hybrid Search
Hybrid + Reranking
Hybrid + HyDE
```

---

## AI-HS-002 — Query Classification

The AI retrieval planner should identify whether the query is:

```text
Exact
Semantic
Mixed
Entity-Centric
Contextual
Multi-Step
```

---

## AI-HS-003 — Exact Query Optimization

For exact identifiers, the system should increase sparse retrieval importance.

---

## AI-HS-004 — Semantic Query Optimization

For conceptual questions, the system should increase dense retrieval importance.

---

## AI-HS-005 — Mixed Query Optimization

For queries containing both conceptual and exact information, the system shall use hybrid retrieval.

Example:

```text
"Why does ERR-4012 occur when enterprise customers upgrade?"
```

The search should combine:

```text
ERR-4012 → lexical signal

"enterprise customers upgrade" → semantic signal
```

---

## AI-HS-006 — Multi-Step Retrieval

AI agents shall be able to perform multiple searches for complex tasks.

Example:

```text
Search Customer
      ↓
Search Related Tickets
      ↓
Search Product Documentation
      ↓
Search Policy
      ↓
Combine Evidence
```

---

## AI-HS-007 — Evidence Selection

AI agents shall prefer high-quality, authoritative retrieved evidence.

---

## AI-HS-008 — Evidence Grounding

AI-generated responses shall preferentially rely on retrieved evidence for knowledge-dependent claims.

---

## AI-HS-009 — Retrieval Abstention

When retrieval evidence is insufficient, the AI agent shall abstain instead of inventing information.

---

## AI-HS-010 — Human Handoff

When search confidence is insufficient for a configured task, the AI agent shall be capable of escalating to a human agent with the retrieved evidence and search context.

---

## 9. Human-Agent Requirements

## HUMAN-HS-001 — Unified Search Interface

Human agents shall have a single interface for hybrid retrieval.

---

## HUMAN-HS-002 — Search by Customer

Agents shall be able to search within a customer's authorized data.

---

## HUMAN-HS-003 — Search by Ticket

Agents shall be able to search within a ticket and related records.

---

## HUMAN-HS-004 — Search by Product

Agents shall be able to search product-specific information.

---

## HUMAN-HS-005 — Search by Conversation

Agents shall be able to search previous customer conversations.

---

## HUMAN-HS-006 — Search by Knowledge Base

Agents shall be able to search approved knowledge content.

---

## HUMAN-HS-007 — Search Result Inspection

Agents shall be able to inspect source documents.

---

## HUMAN-HS-008 — AI Evidence Inspection

Agents shall be able to inspect evidence retrieved by AI agents.

---

## HUMAN-HS-009 — Human Override

Agents shall be able to override AI retrieval recommendations when authorized.

---

## HUMAN-HS-010 — Feedback

Agents shall be able to submit retrieval feedback.

---

## 10. AI + Human Collaboration

## COLLAB-HS-001

AI shall perform initial retrieval for routine support and sales tasks.

## COLLAB-HS-002

Human agents shall be able to verify AI-retrieved evidence.

## COLLAB-HS-003

Human agents shall be able to perform additional searches during escalation.

## COLLAB-HS-004

Human feedback shall contribute to retrieval-quality improvement.

## COLLAB-HS-005

AI shall provide retrieved evidence when transferring cases to humans.

## COLLAB-HS-006

Human verification shall be distinguishable from AI retrieval.

The system shall distinguish:

```text
AI Retrieved
Human Verified
Authoritative Source
Unverified
Low Confidence
```

---

## 11. RAG Integration Requirements

Hybrid Search shall operate as a core retrieval layer for SalesGenie's RAG architecture.

```text
                    User Question
                          |
                          v
                Query Understanding
                          |
                          v
                   Hybrid Search
                    /          \
                   /            \
                  v              v
              Dense             BM25
               Search           Search
                  \              /
                   \            /
                    v          v
                  RRF Fusion
                       |
                       v
                   Reranking
                       |
                       v
                Authorization
                       |
                       v
                 Top-K Evidence
                       |
                       v
                Context Assembly
                       |
                       v
                     LLM
                       |
                       v
               Grounded Response
```

RAG architectures retrieve external evidence and condition generation on the retrieved context, providing a non-parametric knowledge layer that can be updated independently from model weights.

---

## 12. Performance Requirements

## NFR-HS-001 — Cached Search

Target:

```text
< 100 ms
```

---

## NFR-HS-002 — Dense Search

Target:

```text
< 300 ms
```

---

## NFR-HS-003 — Sparse Search

Target:

```text
< 200 ms
```

---

## NFR-HS-004 — Hybrid Fusion

Target:

```text
< 100 ms additional processing
```

---

## NFR-HS-005 — Hybrid Search

Target:

```text
< 500 ms
```

excluding optional expensive AI reranking.

---

## NFR-HS-006 — Reranked Search

Target:

```text
< 1 second
```

where infrastructure permits.

---

## NFR-HS-007 — Scalability

The system shall horizontally scale:

```text
Search API
Vector Retrieval
Sparse Retrieval
Reranking
Embedding
Caching
Indexing
```

---

## NFR-HS-008 — Availability

Hybrid Search shall support production-grade availability and shall not become a single point of failure for customer-support operations.

---

## NFR-HS-009 — Graceful Degradation

The system shall remain operational if one retrieval strategy becomes unavailable.

---

## 13. Quality Requirements

## QR-HS-001 — Retrieval Recall

Hybrid Search shall improve recall compared with an isolated retrieval strategy where evaluation demonstrates a measurable benefit.

Hybrid retrieval can improve recall by combining complementary sparse and dense retrieval signals, although the additional computation and latency must be evaluated against deployment constraints.

---

## QR-HS-002 — Retrieval Precision

The system shall optimize precision through:

```text
RRF
Reranking
Authority Ranking
Freshness
Deduplication
Query Classification
```

---

## QR-HS-003 — Exact Match Quality

The system shall maintain strong retrieval performance for exact entities.

---

## QR-HS-004 — Semantic Match Quality

The system shall maintain strong retrieval performance for paraphrased and semantically equivalent queries.

---

## QR-HS-005 — Ranking Quality

The system shall continuously evaluate ranking quality using:

```text
MRR
NDCG
Precision@K
Recall@K
Hit Rate
```

---

## 14. Security Requirements

## SEC-HS-001

All search requests shall require authentication unless explicitly configured as public.

## SEC-HS-002

All retrieval shall enforce authorization.

## SEC-HS-003

Tenant isolation shall be mandatory.

## SEC-HS-004

Search caches shall preserve authorization boundaries.

## SEC-HS-005

Search logs shall minimize sensitive information.

## SEC-HS-006

AI agents shall not use Hybrid Search to bypass permissions.

## SEC-HS-007

Human agents shall only retrieve data within their authorized scope.

## SEC-HS-008

Deleted or revoked information shall become unavailable to retrieval according to the configured deletion SLA.

---

## 15. Observability Requirements

The system shall expose metrics for:

```text
Search Requests
Dense Requests
Sparse Requests
Hybrid Requests
Reranker Requests
HyDE Requests

Dense Latency
Sparse Latency
Fusion Latency
Reranker Latency
Total Latency

Candidate Count
Final Result Count

No Result Rate
Low Confidence Rate

Precision@K
Recall@K
MRR
NDCG
Hit Rate

Cache Hit Rate
Error Rate
Timeout Rate

Embedding Cost
Reranking Cost
Search Infrastructure Cost
```

---

## 16. Recommended Adaptive Retrieval Strategy

SalesGenie should support query-dependent retrieval behavior.

```text
                     Query
                       |
                       v
                Query Classifier
                       |
        +--------------+--------------+
        |              |              |
        v              v              v
      Exact         Semantic         Mixed
        |              |              |
        v              v              v
      BM25          Dense          Hybrid
                       |              |
                       |              v
                       |          RRF Fusion
                       |              |
                       +------+-------+
                              |
                              v
                         Reranking
                              |
                              v
                         Top-K
```

---

## 17. Recommended Search Profiles

## PROFILE-HS-001 — Exact Lookup

```text
Sparse Weight: High
Dense Weight: Low
Reranking: Optional
```

Use for:

* Ticket IDs
* Invoice IDs
* Order IDs
* Error codes
* SKU
* Customer IDs

---

## PROFILE-HS-002 — Semantic Question

```text
Dense Weight: High
Sparse Weight: Medium
Reranking: Optional
```

Use for:

* General support questions
* Product questions
* Conceptual questions

---

## PROFILE-HS-003 — Enterprise Hybrid

```text
Dense Retrieval: Enabled
BM25: Enabled
RRF: Enabled
Reranking: Enabled
Metadata Filtering: Enabled
Authorization: Enabled
```

Use for:

* Complex support
* Sales research
* RAG
* Account intelligence

---

## PROFILE-HS-004 — High-Precision Retrieval

```text
Dense Retrieval
+
Sparse Retrieval
+
RRF
+
Cross-Encoder
+
Authority Ranking
+
Freshness Ranking
```

Use for:

* Critical support
* Enterprise policy
* Compliance-sensitive retrieval
* High-value sales decisions

---

## 18. Failure and Fallback Architecture

```text
                  Hybrid Search
                       |
          +------------+------------+
          |                         |
          v                         v
       Dense                    Sparse
          |                         |
          v                         v
       Success?                  Success?
       /     \                   /     \
     Yes      No               Yes      No
      |        |                |        |
      |        v                |        v
      |      Sparse             |      Dense
      |                         |
      +-----------+-------------+
                  |
                  v
             Fusion / RRF
                  |
                  v
             Reranking
                  |
                  v
             Authorization
                  |
                  v
            Relevance Check
                  |
          +-------+-------+
          |               |
       Relevant       Not Relevant
          |               |
          v               v
        Return       Clarification /
                     Human Handoff
```

---

## 19. Business Invariants

The following invariants shall always hold:

```text
Authorization > Relevance

Tenant Isolation > Search Convenience

Exact Entity Matching > Semantic Approximation

Authoritative Source > Unverified Source

Current Version > Obsolete Version

Human Verification > AI Confidence

No Evidence ≠ Evidence

Semantic Similarity ≠ Authorization

Hybrid Retrieval ≠ Guaranteed Correctness

More Candidates ≠ Better Results
```

---

## 20. Acceptance Criteria

The Hybrid Search subsystem shall be considered production-ready when:

* [ ] Dense retrieval is operational.
* [ ] Sparse retrieval is operational.
* [ ] BM25 retrieval is operational.
* [ ] Hybrid retrieval is operational.
* [ ] Candidate fusion is operational.
* [ ] Weighted RRF is operational.
* [ ] Dense and sparse weights are configurable.
* [ ] Query classification is operational.
* [ ] Query rewriting is supported.
* [ ] Entity extraction is supported.
* [ ] Exact identifiers receive appropriate lexical treatment.
* [ ] Semantic queries receive appropriate dense treatment.
* [ ] Mixed queries use hybrid retrieval.
* [ ] Optional cross-encoder reranking is operational.
* [ ] Optional HyDE retrieval is supported.
* [ ] Metadata filtering works.
* [ ] RBAC filtering works.
* [ ] Tenant isolation is enforced.
* [ ] Customer-scoped search works.
* [ ] Ticket-scoped search works.
* [ ] Organization-scoped search works.
* [ ] Knowledge-base search works.
* [ ] CRM search works.
* [ ] Conversation search works.
* [ ] Cross-channel search works.
* [ ] Multilingual retrieval works where configured.
* [ ] Result deduplication works.
* [ ] Source diversity is supported.
* [ ] Source authority ranking works.
* [ ] Freshness ranking works.
* [ ] Search thresholds work.
* [ ] No-result detection works.
* [ ] Low-confidence detection works.
* [ ] Search fallback works.
* [ ] AI agents can invoke Hybrid Search.
* [ ] Human agents can invoke Hybrid Search.
* [ ] Workflows can invoke Hybrid Search.
* [ ] RAG can consume Hybrid Search results.
* [ ] Citations are preserved.
* [ ] Human agents can verify AI evidence.
* [ ] Search feedback can be collected.
* [ ] Retrieval analytics are available.
* [ ] Retrieval quality metrics are available.
* [ ] Search tracing is available.
* [ ] Search audit logging is available.
* [ ] Search costs are measurable.
* [ ] Rate limiting works.
* [ ] Search caching is authorization-aware.
* [ ] Deleted content is removed from retrieval.
* [ ] Document versioning works.
* [ ] Incremental indexing works.
* [ ] Bulk indexing works.
* [ ] Embedding migration is supported.
* [ ] Index health is observable.
* [ ] Search services support horizontal scaling.
* [ ] Hybrid Search supports graceful degradation.
* [ ] Production latency targets are measurable.
* [ ] Security tests demonstrate zero unauthorized retrieval.
* [ ] Retrieval evaluation demonstrates measurable quality.
* [ ] AI agents abstain when evidence is insufficient.
* [ ] Human escalation preserves retrieval evidence and search context.
