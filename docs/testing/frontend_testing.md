# SalesGenie — Frontend Testing Requirements

**Document:** `frontend_testing.md`  
**Product:** SalesGenie — Enterprise AI Customer Support & Sales Agent Platform  
**Requirement Scope:** User Requirements, System Requirements, Functional Requirements  
**Testing Model:** Human + AI-Assisted + AI-Driven  
**Architecture:** Astro Frontend + Enterprise Microservices + Multi-Agent AI + Event-Driven Backend  
**Target Scale:** 10M+ users, 500K concurrent conversations  
**Priority:** Critical  
**Quality Target:** FAANG-Level Production Readiness

---

## 1. Purpose

The SalesGenie Frontend Testing subsystem shall validate the correctness, usability, accessibility, security, performance, reliability, compatibility, observability, and resilience of the complete frontend application.

The frontend testing platform shall validate both:

- Human-driven workflows.
- AI-assisted testing workflows.
- AI-generated test scenarios.
- AI-based visual analysis.
- AI-based failure diagnosis.
- Automated regression testing.

The system shall validate the complete frontend-to-backend lifecycle:

```text
User
  ↓
Browser
  ↓
Astro Frontend
  ↓
Frontend Components
  ↓
State Management
  ↓
API Client
  ↓
API Gateway
  ↓
Microservices
  ↓
AI / Database / Redis / Queue / Event Bus
  ↓
Response
  ↓
Frontend State
  ↓
UI Rendering
  ↓
User
```

---

## 2. Testing Objectives

SalesGenie frontend testing shall ensure:

1. Every critical user workflow functions correctly.
2. Every critical UI component behaves according to its contract.
3. API failures are handled gracefully.
4. Authentication state is correct.
5. Authorization boundaries are enforced.
6. Tenant isolation is reflected correctly in the UI.
7. AI-generated content is rendered safely.
8. Streaming AI responses render correctly.
9. Real-time updates work correctly.
10. Forms validate correctly.
11. Navigation works correctly.
12. Responsive layouts work across supported devices.
13. Accessibility requirements are satisfied.
14. Browser compatibility is maintained.
15. Frontend performance meets defined budgets.
16. Security controls are validated.
17. Client-side state remains consistent with backend state.
18. Error states are usable and actionable.
19. Loading states are correct.
20. Empty states are correct.
21. Permission-restricted UI elements behave correctly.
22. Regression testing protects existing functionality.
23. Visual regressions are detected automatically.
24. AI can generate and analyze tests.
25. Human engineers retain final ownership of critical test decisions.

---

## 3. Scope

## 3.1 In Scope

```text
Unit Testing
Component Testing
Integration Testing
End-to-End Testing
UI Testing
Visual Regression Testing
Accessibility Testing
Responsive Testing
Cross-Browser Testing
Cross-Device Testing
Form Testing
Navigation Testing
State Management Testing
API Integration Testing
Authentication Testing
Authorization Testing
AI UI Testing
Streaming UI Testing
Real-Time UI Testing
Error-State Testing
Loading-State Testing
Performance Testing
Security Testing
Regression Testing
Smoke Testing
Release Testing
Canary Testing
AI-Assisted Test Generation
AI-Assisted Failure Analysis
```

## 3.2 Out of Scope

Detailed infrastructure-only testing shall be covered by:

```text
infrastructure_testing.md
database_testing.md
load_testing.md
chaos_engineering.md
```

---

## 4. Frontend Actors

## 4.1 Human Actors

### HR-001 — End User

The end user shall be able to use the application without encountering broken critical workflows.

### HR-002 — Sales Agent

The sales agent shall be able to:

```text
View Leads
Search Leads
Manage Conversations
Interact With AI
Assign Conversations
Update Customer Information
Use Sales Workflows
```

### HR-003 — Customer Support Agent

The support agent shall be able to:

```text
View Conversations
Respond to Customers
Escalate Conversations
Use Knowledge Base
Interact With AI Agents
```

### HR-004 — Manager

The manager shall be able to:

```text
View Team Metrics
Monitor Agents
Review Conversations
Review Leads
Manage Workflows
```

### HR-005 — Administrator

The administrator shall be able to:

```text
Manage Users
Manage Roles
Manage Permissions
Manage Integrations
Manage API Keys
Manage Workflows
Manage AI Configuration
```

### HR-006 — Super Administrator

The super administrator shall be able to:

```text
View Platform Users
Manage Organizations
Manage Administrators
Manage Platform Configuration
Review Audit Logs
Monitor Platform Health
```

### HR-007 — Developer

Developers shall be able to:

```text
Use Developer Portal
Manage API Keys
Manage Service Accounts
Test APIs
Manage Webhooks
Use Sandbox
Review Usage
```

### HR-008 — QA Engineer

QA engineers shall be able to:

```text
Create Tests
Execute Tests
Review Failures
Analyze Regression
Review Visual Differences
```

### HR-009 — SDET

SDETs shall be able to:

```text
Build Automation
Maintain Test Suites
Manage Fixtures
Configure CI Gates
Maintain Test Infrastructure
```

---

## 5. AI Actors

## AI-001 — AI Test Generator

The AI system shall generate frontend tests from:

```text
User Requirements
System Requirements
Functional Requirements
UI Components
Routes
API Contracts
OpenAPI Specifications
Design Specifications
Existing Tests
Source Code
Production Incidents
Bug Reports
User Journeys
```

---

## AI-002 — AI Visual Testing Agent

The AI agent shall analyze screenshots and identify:

```text
Layout Regression
Missing Components
Alignment Issues
Typography Changes
Spacing Changes
Unexpected Elements
Broken Responsive Layout
Color/Contrast Problems
```

---

## AI-003 — AI Accessibility Agent

The AI system shall identify potential:

```text
Missing Labels
Keyboard Navigation Issues
Focus Issues
Poor Contrast
Improper Heading Hierarchy
Missing Alternative Text
ARIA Problems
```

---

## AI-004 — AI Failure Diagnosis Agent

The AI system shall analyze:

```text
Browser Console
Network Requests
Screenshots
DOM State
Frontend Logs
API Responses
Trace IDs
Application Metrics
Recent Git Changes
```

to identify probable root causes.

---

## AI-005 — AI Regression Agent

The AI system shall identify workflows affected by code changes.

---

## 6. User Requirements

## UR-001 — Application Launch

Users shall be able to launch the SalesGenie frontend successfully.

---

## UR-002 — Authentication

Users shall be able to:

```text
Login
Logout
Refresh Session
Handle Expired Session
Recover From Authentication Failure
```

---

## UR-003 — Authorization

Users shall see only the UI functionality allowed by their permissions.

---

## UR-004 — Dashboard

Users shall be able to access the appropriate dashboard according to their role.

---

## UR-005 — Navigation

Users shall be able to navigate between authorized application routes.

---

## UR-006 — Responsive UI

Users shall be able to use SalesGenie on supported:

```text
Desktop
Laptop
Tablet
Mobile
```

devices.

---

## UR-007 — Conversation Interface

Users shall be able to:

```text
Create Conversation
Open Conversation
Send Message
Receive Message
View History
Search Conversation
Assign Conversation
Escalate Conversation
```

where authorized.

---

## UR-008 — AI Interaction

Users shall be able to interact with AI agents through the supported UI.

---

## UR-009 — Streaming Responses

Users shall be able to see AI-generated streaming responses without UI corruption.

---

## UR-010 — Lead Management

Authorized users shall be able to:

```text
Search Leads
View Lead
Create Lead
Update Lead
Filter Leads
Sort Leads
Paginate Leads
```

---

## UR-011 — Knowledge Base

Authorized users shall be able to:

```text
Upload Documents
View Documents
Search Documents
Delete Documents
Manage Knowledge Bases
```

---

## UR-012 — Workflow Management

Authorized users shall be able to:

```text
Create Workflow
Edit Workflow
Run Workflow
Disable Workflow
View Workflow Status
```

---

## UR-013 — AI Agent Management

Authorized users shall be able to:

```text
Create Agent
Configure Agent
Assign Tools
Configure Permissions
Run Agent
Monitor Agent
Disable Agent
```

---

## UR-014 — Billing

Authorized users shall be able to:

```text
View Plan
View Usage
Upgrade
Downgrade
Cancel
View Invoices
```

according to permissions.

---

## UR-015 — Developer Portal

Developers shall be able to:

```text
View API Documentation
Create API Keys
Revoke API Keys
Manage Service Accounts
Configure Webhooks
Use Sandbox
View API Usage
```

---

## UR-016 — Administrative UI

Administrators shall be able to access administrative functionality according to RBAC policies.

---

## UR-017 — Localization

Users shall be able to select supported languages and see the selected language consistently across the application.

---

## UR-018 — Theme

Users shall be able to switch supported themes without breaking UI state.

---

## UR-019 — Error Recovery

Users shall receive actionable feedback when operations fail.

---

## UR-020 — Empty States

Users shall receive useful empty-state information when no data exists.

---

## 7. System Requirements

## SR-001 — Test Framework

The frontend testing platform shall support:

```text
Unit Tests
Component Tests
Integration Tests
End-to-End Tests
Visual Tests
Accessibility Tests
Performance Tests
```

---

## SR-002 — Browser Automation

The system shall support automated browser testing.

Supported browser categories shall include:

```text
Chromium-Based
Firefox
WebKit-Based
```

where applicable.

---

## SR-003 — Test Isolation

Each automated test shall execute in an isolated state.

---

## SR-004 — Deterministic Tests

Tests shall minimize dependence on:

```text
Real Time
External APIs
Random Data
Shared State
Uncontrolled Network Conditions
```

---

## SR-005 — Test Environment

Dedicated frontend test environments shall exist for:

```text
Local
Development
CI
Staging
Pre-Production
Production Synthetic
```

where applicable.

---

## 8. Test Pyramid

SalesGenie shall implement:

```text
                    E2E
                   /   \
                Visual  A11y
               /         \
          Integration    Browser
             /              \
       Component          Contract
          /                  \
                 Unit
```

The majority of tests should remain fast lower-level tests.

---

## 9. Unit Testing

## FR-001

Unit tests shall validate isolated frontend logic.

Examples:

```text
Utility Functions
Data Transformers
Validators
Formatters
State Reducers
Permission Functions
Authentication Helpers
API Response Parsers
```

---

## 10. Component Testing

## FR-002

Reusable components shall have automated tests.

Examples:

```text
Button
Input
Modal
Dropdown
Table
Card
Sidebar
Navigation
Toast
Dialog
Tabs
Pagination
DataGrid
ChatMessage
AgentCard
LeadCard
```

---

## 11. Component State Testing

Components shall be tested under:

```text
Default
Loading
Success
Error
Empty
Disabled
Readonly
Selected
Focused
Hovered
Expanded
Collapsed
Unauthorized
```

states where applicable.

---

## 12. Form Testing

Forms shall validate:

```text
Required Fields
Optional Fields
Invalid Values
Boundary Values
Empty Values
Submission
Loading
Success
Failure
Server Validation
```

---

## 13. Authentication UI Testing

The frontend shall test:

```text
Login Success
Login Failure
Expired JWT
Invalid JWT
Missing Token
Logout
Session Restoration
Session Timeout
Unauthorized Redirect
```

---

## 14. JWT State Testing

The frontend shall correctly interpret JWT expiration timestamps.

Tests shall verify:

```text
Valid Token
Expired Token
Near-Expiry Token
Malformed Token
Missing Token
```

---

## 15. Authorization UI Testing

Tests shall verify that restricted functionality is not exposed to unauthorized users.

Example:

```text
Admin
  → Admin Controls Visible

Sales Agent
  → Admin Controls Hidden

End User
  → Admin Controls Hidden
```

UI restrictions shall complement, not replace, backend authorization.

---

## 16. Tenant-Aware UI Testing

Tests shall verify:

```text
Tenant A
  ↓
Tenant A Data
```

and:

```text
Tenant A
  ↓
Tenant B Data
  ↓
Not Visible
```

---

## 17. Route Testing

Every application route shall be tested for:

```text
Valid Navigation
Invalid Navigation
Unauthorized Navigation
Missing Resource
Deep Linking
Refresh
Browser Back
Browser Forward
```

---

## 18. Protected Route Testing

Protected routes shall redirect unauthorized users correctly.

---

## 19. Navigation Testing

The system shall test:

```text
Sidebar
Header
Breadcrumbs
Tabs
Links
Buttons
Back
Forward
Redirects
```

---

## 20. Browser Refresh Testing

Critical pages shall preserve or correctly reconstruct application state after browser refresh.

---

## 21. Deep-Link Testing

Users shall be able to directly navigate to supported application routes.

---

## 22. API Integration Testing

Frontend API clients shall be tested against:

```text
200
201
202
204
400
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
```

where applicable.

---

## 23. API Client Testing

The frontend API client shall correctly handle:

```text
Authentication Headers
Token Refresh
Request Serialization
Response Parsing
Error Parsing
Timeout
Retry
Cancellation
```

---

## 24. Network Failure Testing

Frontend tests shall simulate:

```text
Offline
Slow Network
Request Timeout
Connection Reset
DNS Failure
5xx Response
Malformed Response
```

---

## 25. Loading-State Testing

Every asynchronous critical operation shall have a validated loading state.

---

## 26. Error-State Testing

Every critical asynchronous operation shall have a validated error state.

---

## 27. Empty-State Testing

The UI shall correctly render empty data sets.

Examples:

```text
No Leads
No Conversations
No Documents
No Agents
No Workflows
No API Keys
No Notifications
```

---

## 28. Optimistic UI Testing

Where optimistic updates are used, tests shall verify:

```text
Optimistic Success
Optimistic Failure
Rollback
Duplicate Action
Concurrent Action
```

---

## 29. State Management Testing

Frontend state shall be tested for:

```text
Initialization
Update
Reset
Persistence
Synchronization
Invalidation
Race Conditions
```

---

## 30. Local Storage Testing

Where local storage is used, tests shall validate:

```text
Missing Key
Valid Value
Invalid Value
Corrupted Value
Reset
Migration
```

---

## 31. Session Storage Testing

Session storage behavior shall be tested similarly.

---

## 32. Theme Testing

Tests shall verify:

```text
Default Theme
Light Theme
Dark Theme
Theme Persistence
Theme Switching
Refresh
```

---

## 33. Localization Testing

Localization tests shall validate:

```text
Language Selection
Persistence
Fallback Language
Missing Translation
Dynamic Text
Date Formatting
Number Formatting
RTL Where Supported
```

---

## 34. Language Regression

Changing language shall not silently revert after navigation or refresh.

---

## 35. Accessibility Testing

The frontend shall target WCAG 2.2 AA-level accessibility where applicable.

Tests shall cover:

```text
Keyboard Navigation
Focus Management
Screen Reader Semantics
ARIA
Labels
Contrast
Headings
Landmarks
Alternative Text
Form Errors
Modal Focus
```

---

## 36. Keyboard Testing

Critical workflows shall be executable without a mouse.

---

## 37. Focus Testing

Tests shall verify correct focus behavior after:

```text
Modal Open
Modal Close
Form Error
Navigation
Dynamic Content
Toast
```

---

## 38. Screen Reader Testing

Critical UI workflows shall expose meaningful semantic information to assistive technologies.

---

## 39. Visual Regression Testing

Automated screenshots shall be compared against approved baselines.

Visual testing shall detect:

```text
Layout Shift
Component Removal
Component Addition
Spacing Changes
Typography Changes
Overflow
Broken Alignment
Responsive Regression
```

---

## 40. AI Visual Regression

AI shall assist in distinguishing meaningful visual changes from harmless rendering differences.

AI classification:

```yaml
change_type:
severity:
affected_component:
likely_intentional:
confidence:
```

Human approval shall be required for ambiguous critical visual changes.

---

## 41. Responsive Testing

The application shall be tested across defined viewport classes.

Example:

```text
Mobile
  320px
  375px
  390px
  414px

Tablet
  768px
  820px
  1024px

Desktop
  1280px
  1440px
  1920px
```

Exact supported breakpoints shall be maintained as project configuration.

---

## 42. Responsive Layout Testing

Tests shall detect:

```text
Horizontal Overflow
Clipped Text
Overlapping Elements
Broken Navigation
Broken Tables
Broken Modals
Broken Charts
Unreadable Content
```

---

## 43. Mobile Navigation Testing

Mobile navigation shall validate:

```text
Open
Close
Route Change
Back Navigation
Overlay
Focus
Scroll Lock
```

---

## 44. Table Testing

Data tables shall validate:

```text
Loading
Empty
Error
Pagination
Sorting
Filtering
Selection
Column Visibility
Responsive Behavior
```

---

## 45. Dashboard Testing

Dashboard tests shall validate:

```text
Metrics
Charts
Cards
Filters
Date Ranges
Refresh
Loading
Empty State
Error State
```

---

## 46. Real-Time UI Testing

Real-time interfaces shall validate:

```text
Message Received
Status Update
Agent Status
Notification
Assignment
Presence
Connection Loss
Reconnection
```

where applicable.

---

## 47. WebSocket/SSE Testing

Streaming connections shall validate:

```text
Connection
Data Event
Heartbeat
Disconnect
Reconnect
Malformed Event
Server Error
Client Cancellation
```

---

## 48. AI Chat UI Testing

AI chat interfaces shall validate:

```text
Prompt Submission
Loading
Streaming
Completion
Cancellation
Retry
Error
Conversation History
Context
Token/Usage Display
```

---

## 49. AI Streaming Test

Example:

```text
User Prompt
   ↓
Request
   ↓
Connection
   ↓
Token 1
   ↓
Token 2
   ↓
Token N
   ↓
Final Event
   ↓
Completed Message
```

The UI shall not duplicate, reorder, or lose content.

---

## 50. AI Tool-Call UI Testing

When AI invokes tools, the UI shall correctly represent:

```text
Tool Started
Tool Running
Tool Success
Tool Failure
Tool Authorization Failure
```

where exposed to users.

---

## 51. AI Agent UI Testing

Agent interfaces shall validate:

```text
Agent Selection
Agent Status
Agent Execution
Agent Output
Tool Usage
Errors
Permissions
Termination
```

---

## 52. AI Safety UI Testing

The frontend shall not accidentally expose:

```text
System Prompts
Internal Tool Credentials
Hidden Instructions
Private Tenant Data
Internal Debug Information
```

---

## 53. Rich AI Content Testing

AI-generated content shall be safely rendered when supporting:

```text
Markdown
Code
Tables
Links
Lists
Structured Content
```

---

## 54. XSS Testing

User-controlled and AI-generated content shall be tested for unsafe HTML/script injection.

---

## 55. Clipboard Testing

Clipboard interactions shall be validated where implemented:

```text
Copy
Paste
Copy Success
Copy Failure
Permission Denied
```

---

## 56. File Upload Testing

Upload interfaces shall validate:

```text
Valid File
Invalid File
Unsupported Type
Oversized File
Empty File
Duplicate File
Upload Failure
Upload Retry
Upload Cancellation
```

---

## 57. File Download Testing

Downloads shall validate:

```text
Correct File
Correct Filename
Correct Content-Type
Authorization
Failure
Expired URL
```

---

## 58. Drag-and-Drop Testing

Where supported:

```text
Drag Start
Drag Over
Drop
Invalid Drop
Cancel
```

shall be tested.

---

## 59. Notification Testing

Notifications shall validate:

```text
Success
Error
Warning
Info
Dismiss
Auto-Dismiss
Persistence
Navigation
```

---

## 60. Modal Testing

Modals shall validate:

```text
Open
Close
Escape
Outside Click
Focus Trap
Submit
Cancel
Error
```

---

## 61. Search UI Testing

Search interfaces shall validate:

```text
Exact Search
Partial Search
No Result
Empty Search
Special Characters
Unicode
Loading
Error
Pagination
```

---

## 62. Filter UI Testing

Filters shall validate:

```text
Single Filter
Multiple Filters
Clear Filter
Reset
Persistence
URL Synchronization
```

where applicable.

---

## 63. Sorting UI Testing

Sorting shall validate:

```text
Ascending
Descending
Reset
Multiple Fields
```

where supported.

---

## 64. Pagination UI Testing

Pagination shall validate:

```text
First
Previous
Next
Last
Disabled State
Page Count
Page Size
```

---

## 65. URL State Testing

Where UI state is encoded in URLs, tests shall validate:

```text
Query Parameters
Filters
Sorting
Pagination
Tabs
Deep Links
Refresh
```

---

## 66. Browser History Testing

The application shall correctly handle:

```text
Back
Forward
Refresh
Direct URL
```

navigation.

---

## 67. Browser Compatibility

Critical workflows shall be validated across supported browsers.

---

## 68. Browser Feature Detection

The frontend shall gracefully handle unsupported browser capabilities where applicable.

---

## 69. Performance Testing

Frontend performance tests shall measure:

```text
Page Load
First Contentful Paint
Largest Contentful Paint
Interaction to Next Paint
Cumulative Layout Shift
Time to Interactive
JavaScript Execution
Network Transfer
```

where applicable.

---

## 70. Performance Budgets

Critical routes shall have defined budgets for:

```text
JavaScript
CSS
Images
Fonts
Network Requests
Rendering
```

---

## 71. Bundle Testing

The CI pipeline shall detect unexpected bundle growth.

---

## 72. Code Splitting Testing

Large features shall be validated for appropriate lazy loading where applicable.

---

## 73. Image Optimization Testing

Images shall be tested for:

```text
Correct Dimensions
Lazy Loading
Responsive Loading
Broken Source
Alt Text
```

---

## 74. Memory Leak Testing

Long-running application sessions shall be tested for:

```text
Increasing Memory
Unreleased Event Listeners
Unreleased Timers
Detached DOM
Persistent Subscriptions
```

---

## 75. Long Session Testing

Critical dashboards and chat interfaces shall remain functional during prolonged usage.

---

## 76. Security Testing

Frontend security tests shall cover:

```text
XSS
CSRF Where Applicable
Clickjacking Protections
CSP
Secure Cookies
Token Handling
Sensitive Data Exposure
Open Redirect
Unsafe URL Handling
```

---

## 77. CSP Testing

The frontend shall validate that Content Security Policy does not unintentionally block legitimate:

```text
API Requests
Workers
Images
Fonts
Scripts
WebSockets
SSE
```

---

## 78. Authentication Storage Testing

Tests shall validate secure handling of authentication state according to the application's security architecture.

---

## 79. Sensitive Data Testing

Frontend tests shall ensure sensitive information is not accidentally rendered into:

```text
DOM
HTML
Console
Local Storage
Session Storage
URLs
Analytics Events
Error Messages
```

---

## 80. Permission UI Testing

Every permission-controlled UI feature shall have positive and negative tests.

---

## 81. Error Boundary Testing

Frontend error boundaries shall correctly handle unexpected component failures.

Expected behavior:

```text
Component Failure
      ↓
Error Boundary
      ↓
User-Friendly UI
      ↓
Error Telemetry
```

---

## 82. Crash Recovery

Recoverable UI failures shall allow users to continue using unaffected parts of the application.

---

## 83. Offline Testing

Where offline behavior is supported:

```text
Offline
 ↓
User Action
 ↓
Queue / Reject / Inform
 ↓
Online
 ↓
Recovery
```

shall be tested.

---

## 84. Retry UX Testing

Retryable failures shall provide appropriate retry controls.

---

## 85. Duplicate Action Testing

Double-clicking or repeatedly submitting critical actions shall not create unintended duplicate operations.

---

## 86. Race Condition Testing

The frontend shall test concurrent state changes such as:

```text
Two Saves
Two Searches
Rapid Navigation
Rapid Filter Changes
Message Send + Conversation Change
Token Refresh + API Request
```

---

## 87. Abort/Cancellation Testing

Cancelled requests shall not update stale UI state.

---

## 88. Stale Response Testing

The frontend shall prevent older asynchronous responses from overwriting newer state.

---

## 89. API Response Contract Testing

Frontend consumers shall validate API response structures against the expected contracts.

---

## 90. Mock Service Testing

Tests shall use controlled mock services for:

```text
Success
Failure
Latency
Malformed Response
Timeout
Rate Limit
```

where appropriate.

---

## 91. Integration Environment Testing

Critical workflows shall also be tested against real service integrations in dedicated environments.

---

## 92. Test Fixtures

Reusable fixtures shall exist for:

```text
User
Admin
Manager
Sales Agent
Tenant
Conversation
Lead
Document
Agent
Workflow
Subscription
API Key
Service Account
```

---

## 93. Role Fixtures

At minimum:

```text
SUPER_ADMIN
ADMIN
MANAGER
SALES_AGENT
SUPPORT_AGENT
DEVELOPER
END_USER
```

shall be represented where applicable.

---

## 94. Test Data Isolation

Tests shall never depend on shared mutable production data.

---

## 95. Test Cleanup

Automated tests shall clean up resources they create.

---

## 96. Screenshot Testing

Critical pages shall have baseline screenshots for supported viewport classes.

---

## 97. Visual Diff Thresholds

Visual regression shall distinguish:

```text
Expected Change
Minor Rendering Noise
Meaningful UI Change
Critical UI Regression
```

---

## 98. AI Visual Review

AI shall analyze visual differences and provide:

```yaml
component:
difference:
severity:
likely_cause:
confidence:
recommendation:
```

---

## 99. AI Test Generation

AI shall generate frontend tests from user journeys.

Example:

```text
User Requirement:
User can create a conversation.

AI Generates:

1. Open dashboard
2. Click New Conversation
3. Select customer
4. Enter message
5. Submit
6. Verify loading
7. Verify API request
8. Verify conversation appears
9. Verify success state
10. Verify failure state
```

---

## 100. AI Test Mutation

AI shall generate mutations such as:

```text
Remove Required Field
Double Submit
Slow API
Failed API
Expired Token
Unauthorized User
Empty Data
Large Data
Malformed Data
Rapid Navigation
```

---

## 101. AI User Journey Generation

AI shall generate journeys from:

```text
User Role
Feature
Business Goal
Permissions
API Contract
```

---

## 102. AI Accessibility Analysis

AI shall inspect:

```text
DOM
ARIA
Labels
Focus Order
Keyboard Paths
Screenshots
```

for accessibility defects.

---

## 103. AI Failure Analysis

For a failed test, AI shall correlate:

```text
Test Step
DOM
Screenshot
Network
Console
API Response
Logs
Trace
Commit
```

and produce a probable root cause.

---

## 104. AI Failure Output

Example:

```yaml
test_id:
failure:
affected_route:
affected_component:
api_dependency:
probable_root_cause:
evidence:
severity:
confidence:
recommended_fix:
regression_test_required:
```

---

## 105. AI Test Prioritization

AI shall prioritize tests based on:

```text
Business Criticality
Traffic
Recent Code Changes
Historical Failure Rate
User Impact
Security Sensitivity
Dependency Count
```

---

## 106. Change-Aware Testing

When frontend code changes, the system shall identify affected:

```text
Routes
Components
API Clients
State Modules
User Journeys
Visual Baselines
Accessibility Tests
```

and execute the relevant tests.

---

## 107. Dependency-Aware Testing

Example:

```text
Changed:
Conversation Component

Automatically Run:
Conversation Unit Tests
Conversation Component Tests
Conversation API Tests
Conversation E2E Tests
AI Chat Tests
Streaming Tests
Visual Tests
Accessibility Tests
```

---

## 108. Smoke Test Suite

The frontend smoke suite shall validate:

```text
Application Launch
Login
Logout
Dashboard
Navigation
Conversation
AI Interaction
Lead Search
Admin Access
Developer Portal
```

where applicable.

---

## 109. Critical E2E Workflows

Mandatory critical journeys shall include:

```text
User Login
User Logout
Session Restoration
Role-Based Access
Organization Access
Conversation Creation
Message Sending
AI Response
AI Streaming
Human Handoff
Lead Search
Lead Management
Document Upload
RAG Search
Agent Execution
Workflow Execution
Subscription Management
API Key Management
Webhook Configuration
Admin Management
```

---

## 110. Super Admin UI Testing

Super Admin workflows shall validate:

```text
Platform Dashboard
User Management
Organization Management
Role Management
Admin Management
Security
Audit Logs
Sessions
Platform Metrics
```

---

## 111. Developer Portal Testing

Developer portal workflows shall validate:

```text
API Documentation
API Key Creation
API Key Revocation
Service Accounts
Webhooks
Sandbox
Usage
API Testing
```

---

## 112. SalesGenie Dashboard Testing

Dashboard testing shall validate:

```text
Metrics
Charts
Navigation
Filters
Date Range
Refresh
Role Permissions
Loading
Errors
Empty States
```

---

## 113. Chat Interface Testing

The chat interface shall validate:

```text
Message Composer
Send
Cancel
Retry
Streaming
Attachments
History
Search
Typing Indicator
AI Status
Human Handoff
```

---

## 114. Lead Intelligence UI Testing

Lead intelligence pages shall validate:

```text
Company Search
Lead Search
Filters
Sorting
Pagination
Lead Detail
Scoring
Export
```

where supported.

---

## 115. Knowledge Base UI Testing

Knowledge base interfaces shall validate:

```text
Upload
Processing State
Ready State
Failure State
Search
Filtering
Permissions
Delete
```

---

## 116. Workflow Builder Testing

Workflow builder tests shall validate:

```text
Create Node
Delete Node
Connect Nodes
Edit Node
Validate Workflow
Save
Run
Disable
```

---

## 117. Agent Builder Testing

Agent builder tests shall validate:

```text
Create Agent
Configure Instructions
Select Model
Assign Tools
Set Permissions
Save
Run
Observe
Disable
```

---

## 118. Billing UI Testing

Billing UI shall validate:

```text
Current Plan
Usage
Upgrade
Downgrade
Cancellation
Invoice
Payment State
Entitlements
```

---

## 119. Integration UI Testing

Integration configuration shall validate:

```text
Connect
Authenticate
Configure
Test Connection
Disconnect
Reconnect
Failure
```

for supported integrations.

---

## 120. Accessibility Release Gate

Critical accessibility violations shall block release where configured.

---

## 121. Visual Release Gate

Critical visual regressions shall block release.

---

## 122. E2E Release Gate

Critical E2E workflows shall pass before production deployment.

---

## 123. Performance Release Gate

Critical frontend performance budgets shall not regress beyond approved thresholds.

---

## 124. Security Release Gate

Critical frontend security failures shall block production release.

---

## 125. CI/CD Integration

Frontend tests shall run at appropriate pipeline stages:

```text
Pull Request
 ↓
Unit
 ↓
Component
 ↓
Integration
 ↓
E2E
 ↓
Accessibility
 ↓
Visual
 ↓
Performance
 ↓
Release
```

---

## 126. Pull Request Quality Gate

Every pull request shall execute relevant fast tests.

Critical failures shall block merging.

---

## 127. Merge Testing

Merged code shall execute broader integration and regression suites.

---

## 128. Nightly Testing

Nightly testing shall execute:

```text
Full E2E
Cross-Browser
Visual
Accessibility
Performance
Regression
```

suites.

---

## 129. Pre-Production Testing

Pre-production shall execute:

```text
Critical E2E
API Integration
Visual
Accessibility
Security
Performance
```

tests.

---

## 130. Canary Testing

Frontend canary deployment shall validate:

```text
Application Launch
Authentication
Critical Routes
Critical API Calls
JavaScript Errors
Core Web Vitals
```

before full rollout.

---

## 131. Rollback Testing

After rollback, the system shall validate critical workflows.

---

## 132. Flaky Test Detection

The platform shall monitor:

```text
Pass Rate
Retry Rate
Failure Pattern
Browser
Environment
Timing
Network
Dependency
```

to identify flaky tests.

---

## 133. Flaky Test Governance

A flaky test shall not be silently disabled.

Quarantine requires:

```yaml
reason:
owner:
issue:
created_at:
expiration:
approval:
```

---

## 134. Frontend Error Taxonomy

Failures shall be classified as:

```text
UI_RENDER_ERROR
COMPONENT_ERROR
STATE_ERROR
ROUTING_ERROR
AUTH_ERROR
AUTHORIZATION_ERROR
API_ERROR
NETWORK_ERROR
VALIDATION_ERROR
STREAMING_ERROR
WEBSOCKET_ERROR
SSE_ERROR
VISUAL_REGRESSION
ACCESSIBILITY_ERROR
PERFORMANCE_REGRESSION
SECURITY_ERROR
BROWSER_COMPATIBILITY_ERROR
DATA_ERROR
TEST_DEFECT
ENVIRONMENT_ERROR
UNKNOWN
```

---

## 135. Observability Testing

Critical frontend workflows shall generate appropriate:

```text
Error Events
Performance Metrics
Correlation IDs
Trace IDs
User Journey Context
```

where supported.

---

## 136. Browser Console Testing

Critical E2E tests shall detect unexpected:

```text
JavaScript Errors
Unhandled Promise Rejections
Critical Warnings
Network Errors
```

---

## 137. Network Request Testing

Tests shall validate:

```text
Request URL
Method
Headers
Payload
Response
Status
Timing
Retry
```

where relevant.

---

## 138. Trace Correlation

Frontend failures shall be correlatable with backend traces when tracing is enabled.

Example:

```text
Browser
   ↓
Request ID
   ↓
API Gateway
   ↓
Microservice
   ↓
Database
```

---

## 139. Production Synthetic Testing

Safe synthetic browser workflows may validate:

```text
Login
Dashboard
Conversation
AI Interaction
Logout
```

without interacting with real customer data.

---

## 140. Production Data Protection

Frontend tests shall never use uncontrolled real customer information.

---

## 141. Test Secrets

Test secrets shall be injected securely and never committed to source control.

---

## 142. Test Reports

Every test execution shall report:

```text
Test ID
Test Name
Suite
Browser
Viewport
Environment
Commit SHA
Duration
Status
Failure
Screenshot
Trace
Console
Network
```

where applicable.

---

## 143. Test Artifacts

Failed tests shall preserve appropriate:

```text
Screenshot
Video
DOM Snapshot
Console Logs
Network Logs
Trace
API Response
```

subject to security and privacy controls.

---

## 144. Frontend Test Dashboard

The dashboard shall expose:

```text
Test Pass Rate
E2E Pass Rate
Unit Coverage
Component Coverage
Visual Regression Rate
Accessibility Score
Performance Score
Flaky Test Rate
Browser Failures
Route Coverage
Critical Workflow Coverage
```

---

## 145. Test Coverage Model

Coverage shall be measured across:

```text
Code
Components
Routes
User Journeys
Roles
Browsers
Viewports
API Contracts
Permissions
States
```

---

## 146. Role × Feature Coverage

The testing system shall support a matrix:

| Role          | Dashboard | Conversations | Leads    | AI      | Billing | Admin | Developer |
| ------------- | --------- | ------------- | -------- | ------- | ------- | ----- | --------- |
| Super Admin   | Yes       | Policy        | Policy   | Yes     | Yes     | Yes   | Yes       |
| Admin         | Yes       | Yes           | Yes      | Yes     | Yes     | Yes   | Optional  |
| Manager       | Yes       | Yes           | Yes      | Yes     | Policy  | No    | No        |
| Sales Agent   | Yes       | Yes           | Yes      | Yes     | No      | No    | No        |
| Support Agent | Yes       | Yes           | Limited  | Yes     | No      | No    | No        |
| Developer     | Yes       | Optional      | Optional | Yes     | Usage   | No    | Yes       |
| End User      | Limited   | Allowed       | No       | Allowed | Plan    | No    | No        |

Exact permissions shall be determined by SalesGenie's RBAC policy.

---

## 147. Browser × Workflow Matrix

Critical workflows shall be validated across supported browsers.

```text
                    Chromium   Firefox   WebKit
Login                  ✓          ✓        ✓
Dashboard              ✓          ✓        ✓
Chat                   ✓          ✓        ✓
AI Streaming           ✓          ✓        ✓
Lead Search            ✓          ✓        ✓
Admin                   ✓          ✓        ✓
Developer Portal        ✓          ✓        ✓
```

---

## 148. Viewport × Workflow Matrix

Critical workflows shall be tested across supported viewport classes.

---

## 149. Requirements Traceability

Every critical frontend test shall map to one or more:

```text
User Requirement
System Requirement
Functional Requirement
API Contract
Security Requirement
Accessibility Requirement
Performance Requirement
Production Incident
```

---

## 150. Production Incident → Frontend Regression

```text
Production Bug
      ↓
Incident
      ↓
Screenshot / Logs / Trace
      ↓
Root Cause
      ↓
Affected Component
      ↓
Regression Test
      ↓
Human Review
      ↓
Permanent Test Suite
      ↓
CI/CD Gate
```

---

## 151. AI + Human Frontend Testing Workflow

```text
Requirements
      ↓
User Journey Modeling
      ↓
AI Test Generation
      ↓
Human Review
      ↓
Test Environment
      ↓
Automated Execution
      ↓
Browser
      ↓
Frontend
      ↓
API
      ↓
Backend
      ↓
Assertions
      ↓
Screenshots + Logs + Network + Trace
      ↓
AI Failure Analysis
      ↓
Human Diagnosis
      ↓
Regression Test
      ↓
CI/CD Quality Gate
      ↓
Release
```

---

## 152. AI Governance

AI-generated tests shall:

1. Be reviewable.
2. Be traceable to requirements.
3. Have deterministic assertions where possible.
4. Not automatically weaken existing tests.
5. Not automatically approve security-sensitive changes.
6. Not expose secrets.
7. Not access unauthorized production data.
8. Require human approval for critical release gates.

---

## 153. Critical Frontend Invariants

The following invariants shall always hold:

```text
Unauthorized users cannot access protected functionality.

Users cannot see data outside their tenant.

Expired authentication cannot silently remain authorized.

Critical user actions provide visible feedback.

Critical API failures cannot leave the UI in a misleading state.

AI-generated content cannot execute arbitrary client-side code.

Stale API responses cannot overwrite newer application state.

Duplicate user actions cannot create unintended duplicate operations.

Critical navigation paths cannot dead-end.

Production credentials cannot appear in frontend artifacts.

Sensitive information cannot be unintentionally rendered or logged.
```

---

## 154. Minimum Test Coverage

Critical features shall include:

```text
Unit Test
Component Test
Integration Test
E2E Test
Negative Test
Error Test
Permission Test
Accessibility Test
Responsive Test
Visual Test
Regression Test
```

where applicable.

---

## 155. Frontend Quality Gates

A release shall fail when:

```text
Critical E2E Test Fails
OR
Critical Authentication Test Fails
OR
Critical Authorization Test Fails
OR
Tenant Isolation UI Test Fails
OR
Critical Accessibility Test Fails
OR
Critical Visual Regression Detected
OR
Critical Security Test Fails
OR
Critical Performance Budget Violated
OR
Production-Critical JavaScript Error Detected
```

---

## 156. Test Execution Modes

The platform shall support:

```text
UNIT
COMPONENT
INTEGRATION
SMOKE
TARGETED
AFFECTED
REGRESSION
E2E
VISUAL
ACCESSIBILITY
SECURITY
PERFORMANCE
RELEASE
CANARY
PRODUCTION-SYNTHETIC
```

---

## 157. Frontend Testing Maturity Model

## Level 1 — Manual Testing

```text
Manual UI Validation
Manual Browser Testing
```

## Level 2 — Automated Testing

```text
Unit
Component
E2E
```

## Level 3 — Continuous Quality

```text
CI/CD
Regression
Cross-Browser
Accessibility
Visual
```

## Level 4 — Production Engineering

```text
Performance
Observability
Synthetic Monitoring
Canary Validation
Incident Regression
```

## Level 5 — Intelligent Frontend Engineering

```text
AI Test Generation
AI Visual Analysis
AI Accessibility Analysis
AI Failure Diagnosis
Change-Aware Test Selection
User-Journey Mining
Production Regression Learning
Automated Risk Prioritization
Human Governance
```

SalesGenie shall target **Level 5**.

---

## 158. Ultimate Frontend Testing Architecture

```text
                         SALESGENIE
                             │
                             ▼
                    Frontend Test Registry
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
          Human Test Design        AI Test Generator
                 │                       │
                 └───────────┬───────────┘
                             ▼
                       Test Orchestrator
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
        Unit             Component             E2E
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
                      Browser Automation
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
       Chromium           Firefox             WebKit
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
                       Astro Frontend
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
   Components           State Layer          API Client
        │                    │                    │
        └────────────────────┼────────────────────┘
                             ▼
                       API Gateway
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
           Microservices   AI Gateway   Integrations
                │            │            │
                ▼            ▼            ▼
            PostgreSQL     LLMs         External APIs
                │
                ▼
          Redis / Queue / Event Bus
                             │
                             ▼
                Logs + Metrics + Traces
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
      AI Failure        AI Visual        AI Accessibility
       Analyzer           Analyzer           Analyzer
            │                │                │
            └────────────────┼────────────────┘
                             ▼
                       Test Dashboard
                             │
                             ▼
                       CI/CD Quality Gate
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
                  Deploy            Rollback
```

---

## 159. Ultimate Frontend Test Lifecycle

```text
Requirement
    ↓
User Journey
    ↓
Risk Analysis
    ↓
AI Test Generation
    ↓
Human Review
    ↓
Test Implementation
    ↓
Local Execution
    ↓
CI Execution
    ↓
Browser Matrix
    ↓
Assertions
    ↓
Visual Validation
    ↓
Accessibility Validation
    ↓
Performance Validation
    ↓
Security Validation
    ↓
Observability Validation
    ↓
AI Failure Diagnosis
    ↓
Human Root Cause Analysis
    ↓
Regression Protection
    ↓
Release Gate
    ↓
Production Canary
    ↓
Synthetic Monitoring
    ↓
Continuous Feedback
```

---

## 160. Engineering Principles

1. **Test user journeys, not merely individual buttons.**
2. **Keep most tests fast and deterministic.**
3. **Use E2E tests only for high-value workflows.**
4. **Treat authentication and authorization as critical frontend contracts.**
5. **Never rely on frontend authorization alone; backend authorization remains authoritative.**
6. **Treat tenant isolation as a release-blocking invariant.**
7. **Test every meaningful UI state: loading, success, empty, error, disabled, and unauthorized.**
8. **Validate API failures as aggressively as API successes.**
9. **Test asynchronous behavior for race conditions and stale responses.**
10. **Treat AI-generated UI as untrusted content and render it safely.**
11. **Validate AI streaming and tool execution states.**
12. **Use visual regression testing for high-value interfaces.**
13. **Use accessibility testing as a continuous engineering requirement.**
14. **Measure frontend performance with explicit budgets.**
15. **Use AI to increase test coverage and diagnose failures, not to bypass quality gates.**
16. **Convert every significant production frontend incident into a regression test.**
17. **Correlate browser failures with API, logs, metrics, and traces.**
18. **Protect test credentials and customer data.**
19. **Detect flaky tests rather than hiding them.**
20. **Make critical frontend tests mandatory release gates.**
21. **Use change-aware testing to reduce unnecessary CI execution.**
22. **Validate critical workflows across supported browsers and viewport classes.**
23. **Maintain requirements-to-test traceability.**
24. **Human engineers retain accountability for production quality.**

---

## 161. Final Acceptance Criteria

SalesGenie frontend testing shall be considered production-ready when:

* All critical routes have automated coverage.
* All critical user journeys have E2E coverage.
* Authentication workflows are tested.
* Authorization workflows are tested.
* Tenant-aware UI behavior is tested.
* API integration failures are tested.
* Loading states are tested.
* Error states are tested.
* Empty states are tested.
* Critical forms are tested.
* Critical components are tested.
* AI chat workflows are tested.
* AI streaming is tested.
* AI tool-call UI is tested where applicable.
* RAG workflows are tested.
* Agent workflows are tested.
* Lead workflows are tested.
* Billing workflows are tested.
* Developer portal workflows are tested.
* Super Admin workflows are tested.
* Localization is tested.
* Theme switching is tested.
* Responsive behavior is tested.
* Supported browsers are tested.
* Accessibility is continuously tested.
* Visual regressions are automatically detected.
* Performance budgets are continuously validated.
* Frontend security controls are tested.
* JavaScript errors are detected during E2E execution.
* API/network failures are observable.
* Critical failures are correlated with backend traces.
* Production incidents can generate regression tests.
* AI can generate and prioritize tests.
* AI can analyze visual regressions.
* AI can analyze accessibility issues.
* AI can diagnose test failures.
* Human review controls critical AI-generated changes.
* Flaky tests are tracked and governed.
* Critical tests block releases.
* Test artifacts are securely retained.
* Test results are auditable.
* CI/CD automatically executes appropriate test suites.
* Canary deployments validate critical frontend workflows.
* Rollbacks are validated.
* No production customer data is unintentionally exposed.
* No secrets are leaked into frontend builds, browser logs, screenshots, or test artifacts.

---

## 162. Ultimate Goal

```text
                    FUNCTIONAL CORRECTNESS
                             +
                     USER JOURNEY SAFETY
                             +
                     API INTEGRATION
                             +
                    AUTHORIZATION SAFETY
                             +
                     TENANT ISOLATION
                             +
                    VISUAL CONSISTENCY
                             +
                      ACCESSIBILITY
                             +
                       PERFORMANCE
                             +
                        SECURITY
                             +
                    CROSS-BROWSER
                             +
                     RESPONSIVENESS
                             +
                    AI INTERACTION
                             +
                      REAL-TIME UX
                             +
                     OBSERVABILITY
                             +
                    AI TEST GENERATION
                             +
                    AI FAILURE ANALYSIS
                             +
                    HUMAN GOVERNANCE
                             +
                   CONTINUOUS REGRESSION
                             =
               ENTERPRISE-GRADE SALESGENIE
                  FRONTEND QUALITY SYSTEM
```
