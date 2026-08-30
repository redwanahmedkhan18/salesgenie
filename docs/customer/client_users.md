# SalesGenie — Client Users Requirements Specification

**Document:** `client_users.md`  
**Product:** SalesGenie — Enterprise AI Customer Support, Sales, Marketing & Business Intelligence Platform  
**Scope:** Client/External Client User Management  
**Requirement Level:** FAANG / Enterprise Production  
**Actors:** External Clients, Client Administrators, Organization Owners, Organization Admins, Workplace Admins, Team Managers, Sales/Marketing/Support Users, AI Agents, Platform Admins, Security Admins, Billing Admins  
**Architecture:** Multi-Tenant SaaS + Microservices + Event-Driven + Multi-Agent AI + Human-in-the-Loop  
**Frontend:** Web Application + Future iOS/Android Applications  
**Backend:** API Gateway + Identity Service + Organization Service + User Service + RBAC/ABAC + Audit Service + Notification Service + AI Gateway + Event Bus

---

## 1. Purpose

The Client Users module provides secure, tenant-isolated management of users belonging to an external client's organization.

The module must allow authorized client administrators to:

- View users
- Invite users
- Create users
- Update user profiles
- Assign roles
- Assign permissions
- Assign workplaces
- Assign teams
- Activate/deactivate users
- Suspend users
- Remove users
- Manage user access
- Manage AI-agent access
- Manage integrations access
- Manage project access
- Manage reporting access
- Manage workspace access
- Manage security settings
- Monitor user activity
- Review user sessions
- Review audit history
- Manage user lifecycle
- Approve sensitive access changes
- Manage human and AI-assisted operations

The system must enforce strict tenant isolation so that a client can never access another organization's users or data.

---

## 2. Actors

## 2.1 Human Actors

### External Client

Can access resources explicitly authorized by the client's organization.

### Organization Owner

Full organization-level user management authority.

### Organization Admin

Manages users, teams, workplaces, permissions and organizational configuration according to assigned permissions.

### Workplace Admin

Manages users within assigned workplaces.

### Team Manager

Manages members of assigned teams.

### Sales Manager

Manages sales users within authorized teams/workspaces.

### Marketing Manager

Manages marketing users.

### SEO Manager

Manages SEO users.

### Finance Manager

Manages finance users.

### Support Manager

Manages support users.

### Security Admin

Manages security-sensitive user operations.

### Platform Admin

Manages users across the platform when explicitly authorized.

### Super Admin

Global platform administrator with controlled cross-tenant administrative capabilities.

---

## 2.2 AI Actors

### AI User Administration Agent

Assists administrators with user-management operations.

### AI Security Agent

Detects suspicious account activity and recommends or executes approved protective actions.

### AI Compliance Agent

Checks user access against organizational policies and compliance requirements.

### AI Access Review Agent

Analyzes excessive, unused or anomalous permissions.

### AI Support Agent

Assists users with account and access issues.

### AI Workflow Agent

Executes user-management workflows when explicitly authorized.

### AI Analytics Agent

Analyzes user activity, adoption, engagement and access patterns.

---

## 3. User Requirements

## UR-001 — User Directory

The client administrator shall be able to view all users belonging to the authorized organization.

The directory shall display:

- User ID
- Name
- Email
- Profile image
- Job title
- Designation
- Department
- Role
- Workplace
- Team
- Account status
- Verification status
- MFA status
- Last login
- Last activity
- Created date
- Invitation status
- AI access status
- Risk status
- Account suspension status

---

## UR-002 — User Search

Users shall be searchable by:

- Name
- Email
- User ID
- Employee ID
- Role
- Department
- Team
- Workplace
- Status
- Job title
- Account state

---

## UR-003 — Advanced Filtering

Authorized administrators shall be able to filter users by:

- Active
- Inactive
- Suspended
- Pending invitation
- Disabled
- Locked
- MFA enabled
- MFA disabled
- High-risk
- Recently active
- Never logged in
- Role
- Team
- Workplace
- Department
- Permission group

---

## UR-004 — User Invitation

Authorized administrators shall be able to invite users by email.

The invitation system shall support:

- Individual invitations
- Bulk invitations
- Role assignment
- Workplace assignment
- Team assignment
- Permission assignment
- Project assignment
- Invitation expiration
- Invitation cancellation
- Invitation resending

---

## UR-005 — User Registration

Invited users shall be able to create their account through a secure onboarding flow.

The system shall support:

- Email verification
- Password creation
- OAuth registration
- MFA enrollment
- Terms acceptance
- Privacy consent
- Organization association
- Workplace association
- Role initialization

---

## UR-006 — User Profile Management

Authorized users shall be able to manage profile information.

Supported fields shall include:

- First name
- Last name
- Display name
- Profile picture
- Email
- Phone
- Job title
- Designation
- Department
- Time zone
- Locale
- Language
- Date format
- Notification preferences
- Accessibility preferences

Sensitive fields shall require appropriate authorization.

---

## UR-007 — User Role Management

Authorized administrators shall be able to assign roles.

Supported roles shall include:

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

Role assignment shall be governed by RBAC and ABAC policies.

---

## UR-008 — Permission Management

Administrators shall be able to assign granular permissions.

Permissions may include:

- User management
- Role management
- Permission management
- Sales access
- Lead access
- CRM access
- Marketing access
- SEO access
- Finance access
- Support access
- Analytics access
- Reporting access
- AI-agent access
- Workflow access
- Integration access
- Billing access
- API access
- Developer access
- Export access
- Administrative access

---

## UR-009 — Workplace Assignment

Authorized administrators shall be able to assign users to one or more workplaces according to organization policy.

The system shall support:

- Primary workplace
- Multiple workplaces
- Workplace-specific roles
- Workplace-specific permissions
- Workplace-specific projects
- Workplace-specific AI agents

---

## UR-010 — Team Assignment

Administrators and authorized managers shall be able to assign users to teams.

The system shall support:

- Primary team
- Multiple teams
- Team manager
- Team-specific permissions
- Team-specific workflows
- Team-specific AI agents

---

## UR-011 — Project Access

Administrators shall be able to control user access to client projects.

Project access shall support:

- View
- Create
- Edit
- Delete
- Manage
- Approve
- Export
- Execute workflows
- Use AI agents

---

## UR-012 — AI Agent Access

Administrators shall be able to control which AI agents a user can access.

Controls shall include:

- View AI agent
- Chat with AI agent
- Execute AI agent
- Approve AI actions
- Configure AI agent
- Deploy AI agent
- Monitor AI agent
- Access AI logs
- Access AI analytics

---

## UR-013 — User Activation

Authorized administrators shall be able to activate users.

Activation shall:

- Restore authorized access
- Re-enable sessions
- Re-enable permitted services
- Generate audit events
- Notify relevant administrators when configured

---

## UR-014 — User Deactivation

Authorized administrators shall be able to deactivate users.

Deactivation shall:

- Prevent new authentication
- Revoke active sessions
- Revoke access tokens
- Disable API credentials where applicable
- Stop user-triggered workflows where required
- Preserve required audit records
- Preserve organization ownership relationships

---

## UR-015 — User Suspension

The system shall support temporary account suspension.

Suspension shall support:

- Manual suspension
- Security-triggered suspension
- AI-recommended suspension
- Automated policy suspension
- Temporary suspension duration
- Suspension reason
- Review date
- Administrator approval

---

## UR-016 — User Removal

Authorized administrators shall be able to remove users from an organization.

Removal must distinguish between:

- Organization membership removal
- Account deactivation
- Account deletion
- Data deletion
- Legal retention requirements

---

## UR-017 — Ownership Transfer

The system shall prevent deletion of the sole organization owner.

Ownership transfer shall require:

- Authorized administrator
- Target user
- Explicit confirmation
- Optional MFA verification
- Audit record

---

## UR-018 — User Sessions

Authorized security administrators shall be able to view user sessions.

Information shall include:

- Session ID
- Device
- Browser
- Operating system
- Approximate location
- IP metadata where permitted
- Login timestamp
- Last activity
- Session expiration
- Authentication method

---

## UR-019 — Session Revocation

Authorized administrators shall be able to:

- Revoke individual sessions
- Revoke all sessions
- Revoke suspicious sessions
- Force reauthentication

---

## UR-020 — MFA Management

Authorized users shall be able to configure MFA.

Supported mechanisms may include:

- Authenticator application
- WebAuthn/passkeys
- Security keys
- Recovery codes
- Organization-enforced MFA

Administrators shall be able to reset MFA only under controlled authorization.

---

## UR-021 — Password Management

Users shall be able to:

- Change password
- Recover password
- Reset password
- View password security requirements

Administrators shall not be able to view user passwords.

---

## UR-022 — User Risk Management

The system shall display user risk indicators based on authorized security analytics.

Risk factors may include:

- Unusual login behavior
- Impossible travel
- Credential abuse
- Excessive failed authentication
- Suspicious API activity
- Abnormal data exports
- Unusual privilege escalation
- Suspicious AI-agent activity

---

## UR-023 — User Audit History

Authorized administrators shall be able to view user-related audit events.

Events shall include:

- User creation
- Invitation
- Invitation acceptance
- Role change
- Permission change
- Team change
- Workplace change
- Project assignment
- AI-agent assignment
- Login
- Logout
- MFA change
- Password reset
- Suspension
- Activation
- Deactivation
- Deletion
- Session revocation
- API-key changes

---

## UR-024 — Bulk User Management

Authorized administrators shall be able to perform bulk operations.

Supported operations:

- Invite users
- Assign roles
- Assign teams
- Assign workplaces
- Activate
- Deactivate
- Suspend
- Export
- Update permissions

Bulk operations shall require appropriate authorization.

---

## UR-025 — User Import

The system shall support importing users from structured files and integrations.

Supported formats may include:

- CSV
- XLSX
- JSON

Import validation shall detect:

- Duplicate emails
- Invalid emails
- Invalid roles
- Invalid teams
- Invalid workplaces
- Missing mandatory fields
- Unauthorized assignments

---

## UR-026 — User Export

Authorized administrators shall be able to export user information.

Supported formats:

- CSV
- XLSX
- JSON
- PDF where applicable

Sensitive data shall be governed by data-export permissions.

---

## UR-027 — User Notifications

Users shall receive appropriate notifications for:

- Invitation
- Role change
- Permission change
- Workplace assignment
- Team assignment
- Security event
- Account suspension
- Account activation
- Password reset
- MFA changes
- Organization changes

---

## UR-028 — AI-Assisted Administration

Administrators shall be able to ask AI administrative assistants questions such as:

- "Show inactive users."
- "Which users have excessive permissions?"
- "Who has not logged in for 90 days?"
- "Find users without MFA."
- "Recommend users for this sales team."

AI must not perform high-risk operations without explicit authorization.

---

## UR-029 — Human Approval

Sensitive AI-generated user-management actions shall support human approval.

Examples:

- Role escalation
- Organization ownership transfer
- Security suspension
- Permission expansion
- Bulk deactivation
- User deletion

---

## UR-030 — Access Review

Administrators shall be able to periodically review user access.

The system shall identify:

- Unused permissions
- Excessive permissions
- Conflicting roles
- Dormant accounts
- Orphaned accounts
- Unused AI-agent access
- Unused integration access

---

## 4. System Requirements

## SR-001 — Multi-Tenant Isolation

The system shall enforce strict tenant isolation.

Every user-management operation shall be scoped by:

```text
tenant_id
organization_id
workplace_id
team_id
user_id
```

Cross-tenant access shall be denied by default.

---

## SR-002 — Identity Service Integration

The Client Users module shall integrate with the centralized Identity/Auth Service.

The Identity Service shall manage:

* Authentication
* Passwords
* OAuth
* MFA
* Sessions
* Tokens
* Account state
* Credential lifecycle

---

## SR-003 — Organization Service Integration

User membership shall be managed through the Organization Service.

The system shall maintain:

```text
Organization
    └── Workplace
          └── Team
                └── User
```

---

## SR-004 — RBAC Integration

The module shall integrate with centralized RBAC.

Authorization must be evaluated before every protected operation.

---

## SR-005 — ABAC Integration

Fine-grained authorization shall support attributes including:

* Organization
* Workplace
* Team
* User role
* Resource ownership
* Resource classification
* Environment
* Risk level
* Request origin

---

## SR-006 — API Gateway Integration

Frontend requests shall pass through the API Gateway unless an explicitly approved service-to-service route exists.

---

## SR-007 — Service-to-Service Authorization

Internal services shall authenticate using:

* Service identities
* Short-lived credentials
* mTLS where applicable
* Signed service tokens

---

## SR-008 — Event-Driven Architecture

User lifecycle events shall be published to the event bus.

Example events:

```text
user.created
user.invited
user.invitation.accepted
user.updated
user.role.changed
user.permission.changed
user.team.assigned
user.workplace.assigned
user.project.assigned
user.ai_agent.assigned
user.activated
user.deactivated
user.suspended
user.deleted
user.session.revoked
user.mfa.changed
```

---

## SR-009 — Auditability

Every security-sensitive user operation shall generate an immutable audit event.

Audit records shall contain:

* Event ID
* Actor ID
* Actor type
* Target user ID
* Organization ID
* Action
* Resource
* Timestamp
* Request ID
* Correlation ID
* Result
* Reason
* Risk metadata

---

## SR-010 — Idempotency

User-management mutation APIs shall support idempotency for operations where duplicate execution could create inconsistent state.

---

## SR-011 — Concurrency Control

The system shall protect against conflicting simultaneous updates.

Examples:

* Two administrators changing the same user's role
* Simultaneous suspension and activation
* Concurrent team assignment
* Concurrent ownership transfer

---

## SR-012 — Transactional Integrity

User membership, roles and critical access changes shall use transactional guarantees where required.

---

## SR-013 — Eventual Consistency

Non-critical projections may use eventual consistency.

The UI shall clearly represent:

* Pending
* Processing
* Completed
* Failed
* Partially completed

---

## SR-014 — Data Encryption

Sensitive user data shall be encrypted:

* In transit
* At rest
* In backups

---

## SR-015 — Secrets Protection

Passwords, tokens, recovery codes and credentials shall never be stored in plaintext.

---

## SR-016 — Privacy

The system shall support:

* Data minimization
* Data retention
* Data deletion
* Consent management
* Data subject requests
* Privacy-aware exports

---

## SR-017 — Rate Limiting

User-management APIs shall be protected against abuse.

Limits shall exist for:

* Invitations
* Login-related operations
* Password resets
* Bulk operations
* User searches
* Exports
* API requests

---

## SR-018 — API Pagination

Large user directories shall use cursor-based pagination where appropriate.

---

## SR-019 — Search Architecture

User search shall support indexed retrieval for:

* Name
* Email
* User ID
* Role
* Team
* Workplace
* Status

---

## SR-020 — Caching

Read-heavy non-sensitive user metadata may be cached.

Authorization decisions must never rely on stale permissions beyond the defined security consistency window.

---

## SR-021 — Notification Integration

The module shall integrate with the Notification Platform.

Supported channels:

* Email
* SMS
* Push
* In-app notifications

---

## SR-022 — Reporting Integration

User analytics shall be available to authorized dashboards and reporting services.

---

## SR-023 — Analytics Integration

The system shall emit analytics events for:

* User creation
* Invitation
* Activation
* Login
* Feature adoption
* AI usage
* Workflow usage
* User churn
* Deactivation

---

## SR-024 — AI Gateway Integration

AI-powered user administration shall use the centralized AI/LLM Gateway.

The AI layer shall not directly access production databases unless explicitly authorized through controlled tools.

---

## SR-025 — AI Tool Authorization

AI agents shall access user-management functions through explicit tools.

Example:

```text
search_users
get_user
get_user_permissions
get_user_activity
invite_user
update_user
assign_role
assign_team
assign_workplace
suspend_user
activate_user
revoke_sessions
```

Each tool shall have independent authorization.

---

## SR-026 — AI Action Safety

AI agents shall classify operations into:

### Read Operations

Can execute automatically when authorized.

### Low-Risk Mutations

May execute under predefined policies.

### High-Risk Mutations

Require human confirmation.

### Critical Operations

Require privileged authorization and potentially MFA.

---

## SR-027 — Frontend API Integration

The frontend shall connect to backend services for:

* User directory
* Search
* Filters
* User details
* Invitations
* Profile management
* Roles
* Permissions
* Teams
* Workplaces
* Projects
* AI agents
* Sessions
* Security
* Audit history
* Notifications
* Analytics

No authoritative user state shall be maintained only in frontend state.

---

## 5. Functional Requirements

## FR-001 — User Directory API

```http
GET /api/v1/client/users
```

The API shall return authorized users only.

Supported parameters:

```text
organization_id
workplace_id
team_id
role
status
search
sort
cursor
limit
```

---

## FR-002 — Get User

```http
GET /api/v1/client/users/{user_id}
```

The API shall return the user's authorized profile and membership information.

---

## FR-003 — Create User

```http
POST /api/v1/client/users
```

The endpoint shall:

1. Authenticate caller.
2. Authorize caller.
3. Validate tenant scope.
4. Validate user data.
5. Validate role.
6. Validate workplace.
7. Validate team.
8. Create membership.
9. Publish event.
10. Create audit record.
11. Trigger notification.

---

## FR-004 — Invite User

```http
POST /api/v1/client/users/invitations
```

The system shall generate a secure invitation.

Invitation properties shall include:

```text
invitation_id
organization_id
email
role
workplace
team
expires_at
created_by
status
```

---

## FR-005 — Resend Invitation

```http
POST /api/v1/client/users/invitations/{invitation_id}/resend
```

The system shall enforce invitation rate limits.

---

## FR-006 — Cancel Invitation

```http
DELETE /api/v1/client/users/invitations/{invitation_id}
```

---

## FR-007 — Update User

```http
PATCH /api/v1/client/users/{user_id}
```

The system shall validate every mutable field individually.

---

## FR-008 — Role Assignment

```http
PUT /api/v1/client/users/{user_id}/roles
```

The system shall prevent privilege escalation by unauthorized administrators.

---

## FR-009 — Permission Assignment

```http
PUT /api/v1/client/users/{user_id}/permissions
```

The system shall support granular permission changes.

---

## FR-010 — Team Assignment

```http
PUT /api/v1/client/users/{user_id}/teams
```

---

## FR-011 — Workplace Assignment

```http
PUT /api/v1/client/users/{user_id}/workplaces
```

---

## FR-012 — Project Assignment

```http
PUT /api/v1/client/users/{user_id}/projects
```

---

## FR-013 — AI Agent Assignment

```http
PUT /api/v1/client/users/{user_id}/ai-agents
```

---

## FR-014 — Activate User

```http
POST /api/v1/client/users/{user_id}/activate
```

---

## FR-015 — Deactivate User

```http
POST /api/v1/client/users/{user_id}/deactivate
```

---

## FR-016 — Suspend User

```http
POST /api/v1/client/users/{user_id}/suspend
```

Request shall include:

```json
{
  "reason": "security_review",
  "duration": 86400
}
```

---

## FR-017 — Revoke User Sessions

```http
POST /api/v1/client/users/{user_id}/sessions/revoke
```

---

## FR-018 — List User Sessions

```http
GET /api/v1/client/users/{user_id}/sessions
```

---

## FR-019 — User Audit History

```http
GET /api/v1/client/users/{user_id}/audit
```

---

## FR-020 — User Activity

```http
GET /api/v1/client/users/{user_id}/activity
```

The endpoint shall return authorized activity data.

---

## FR-021 — Bulk User Operations

```http
POST /api/v1/client/users/bulk
```

Bulk requests shall produce an operation ID.

Example:

```json
{
  "operation": "assign_role",
  "user_ids": ["u1", "u2"],
  "role": "sales_agent"
}
```

---

## FR-022 — Bulk Operation Status

```http
GET /api/v1/client/users/bulk/{operation_id}
```

The system shall provide:

```text
total
processed
successful
failed
skipped
status
errors
```

---

## FR-023 — Import Users

```http
POST /api/v1/client/users/import
```

The import engine shall:

1. Parse input.
2. Validate schema.
3. Validate tenant context.
4. Validate duplicate users.
5. Validate roles.
6. Validate teams.
7. Validate workplaces.
8. Preview changes.
9. Require confirmation.
10. Execute import.
11. Publish events.
12. Generate audit records.

---

## FR-024 — Export Users

```http
POST /api/v1/client/users/export
```

Exports shall be asynchronous for large datasets.

---

## FR-025 — User Access Review

```http
GET /api/v1/client/users/access-review
```

The system shall identify:

* Excessive privileges
* Dormant accounts
* Unused permissions
* Conflicting permissions
* Unused AI access
* Unused integration access

---

## 6. Frontend Functional Requirements

## FR-FE-001 — Client Users Page

The frontend shall provide:

```text
Client Portal
 └── Users
      ├── All Users
      ├── Invitations
      ├── Teams
      ├── Workplaces
      ├── Roles
      ├── Permissions
      ├── Access Reviews
      └── User Activity
```

---

## FR-FE-002 — User Table

The user table shall support:

* Pagination
* Sorting
* Filtering
* Search
* Column customization
* Bulk selection
* Bulk actions
* Status indicators
* Role indicators
* Risk indicators
* Last activity

---

## FR-FE-003 — User Details

The user details screen shall contain:

```text
Overview
Profile
Roles
Permissions
Teams
Workplaces
Projects
AI Agents
Integrations
Sessions
Activity
Audit
Security
Notifications
```

---

## FR-FE-004 — Create User UI

The frontend shall provide a multi-step user creation workflow:

```text
Profile
   ↓
Organization Membership
   ↓
Workplace
   ↓
Team
   ↓
Role
   ↓
Permissions
   ↓
Projects
   ↓
AI Agents
   ↓
Review
   ↓
Create
```

---

## FR-FE-005 — Invite User UI

The invitation interface shall support:

* Email entry
* Role selection
* Workplace selection
* Team selection
* Permission preview
* Project access
* AI-agent access
* Invitation expiration
* Confirmation

---

## FR-FE-006 — Permission UI

Permissions shall be grouped by domain:

```text
Administration
Sales
Marketing
SEO
Finance
Support
AI
RAG
Workflows
Integrations
Analytics
Reporting
Developer
Billing
Security
```

---

## FR-FE-007 — Role Preview

Before assigning a role, the UI shall display:

* Included permissions
* Restricted resources
* Accessible modules
* AI capabilities
* Project access
* Risk level

---

## FR-FE-008 — Security UI

The security section shall display:

* MFA status
* Active sessions
* Recent login activity
* Security events
* Risk indicators
* Session revocation controls

---

## FR-FE-009 — User Activity Timeline

The UI shall visualize:

```text
Login
Logout
Permission change
Role change
Team assignment
Workplace assignment
Project activity
AI activity
Workflow execution
Export
Security events
```

---

## FR-FE-010 — AI Assistant UI

Administrators shall be able to interact with an AI user-management assistant.

Example:

```text
Admin:
"Show users who haven't logged in for 60 days."

AI:
"I found 14 inactive users."

[View Users]
[Review Accounts]
```

---

## FR-FE-011 — AI Action Confirmation

For mutations:

```text
AI Recommendation
       ↓
Action Preview
       ↓
Impact Analysis
       ↓
Human Confirmation
       ↓
Backend Authorization
       ↓
Execution
       ↓
Audit
```

---

## FR-FE-012 — Real-Time Updates

The UI shall receive relevant user-management events through:

* WebSocket
* Server-Sent Events
* Push notifications

where appropriate.

Examples:

```text
User invited
User accepted invitation
User suspended
Role changed
Bulk operation completed
Security event detected
```

---

## 7. AI Functional Requirements

## FR-AI-001 — AI User Search

AI shall answer natural-language user queries.

Examples:

```text
"Find all inactive sales agents."

"Who has administrator privileges?"

"Show users without MFA."

"Which users haven't logged in this month?"
```

---

## FR-AI-002 — AI Access Analysis

AI shall analyze:

* Permission usage
* Role assignments
* Login frequency
* Resource usage
* AI-agent usage
* Integration usage

---

## FR-AI-003 — AI Permission Recommendation

AI may recommend:

* Permission removal
* Role changes
* Team assignments
* Workplace assignments
* Access reviews

AI recommendations shall include explanations.

---

## FR-AI-004 — AI Risk Detection

AI shall identify anomalous patterns such as:

```text
Unusual login time
Unusual device
Unusual geographic pattern
Sudden privilege escalation
Abnormal export volume
Abnormal API usage
Suspicious AI-agent activity
```

---

## FR-AI-005 — AI User Lifecycle Automation

AI workflows may recommend lifecycle actions:

```text
Dormant user
     ↓
AI identifies inactivity
     ↓
Risk assessment
     ↓
Recommendation
     ↓
Human approval
     ↓
Deactivate
```

---

## FR-AI-006 — AI Explainability

AI recommendations shall provide:

* Reason
* Evidence
* Confidence
* Impact
* Recommended action
* Potential risks

---

## FR-AI-007 — AI Guardrails

AI shall not bypass:

* RBAC
* ABAC
* Tenant isolation
* Security policy
* Approval requirements
* Audit requirements

---

## 8. Human-in-the-Loop Requirements

## HITL-001

Sensitive user operations shall support mandatory human approval.

## HITL-002

Approval requests shall contain:

```text
Requested action
Requester
Target users
Current state
Proposed state
Reason
AI recommendation
AI confidence
Security impact
Business impact
```

## HITL-003

Approvers shall be able to:

* Approve
* Reject
* Request changes
* Delegate where permitted

## HITL-004

Every approval shall be audited.

---

## 9. Backend Data Model

## User

```text
User
----
id
organization_id
primary_workplace_id
primary_team_id
employee_id
first_name
last_name
display_name
email
phone
avatar_url
job_title
designation
department
locale
timezone
status
risk_level
email_verified
mfa_enabled
created_at
updated_at
last_login_at
last_activity_at
deleted_at
```

## Organization Membership

```text
OrganizationMembership
----------------------
id
organization_id
user_id
membership_status
joined_at
invited_by
created_at
updated_at
```

## User Role

```text
UserRole
--------
id
user_id
organization_id
role_id
scope
assigned_by
created_at
expires_at
```

## User Permission

```text
UserPermission
--------------
id
user_id
permission_id
scope
source
assigned_by
created_at
expires_at
```

## User Team Membership

```text
UserTeam
--------
id
user_id
team_id
organization_id
is_primary
created_at
```

## User Workplace Membership

```text
UserWorkplace
-------------
id
user_id
workplace_id
organization_id
is_primary
created_at
```

## User Project Access

```text
UserProjectAccess
-----------------
id
user_id
project_id
access_level
assigned_by
created_at
expires_at
```

## User AI Agent Access

```text
UserAIAgentAccess
-----------------
id
user_id
agent_id
access_level
assigned_by
created_at
expires_at
```

---

## 10. Frontend ↔ Backend Contract

The frontend shall never assume that a user has permission based solely on UI state.

The backend remains authoritative.

```text
Frontend
   │
   ▼
API Gateway
   │
   ▼
Authentication
   │
   ▼
Authorization
   │
   ├── RBAC
   ├── ABAC
   ├── Tenant Isolation
   └── Resource Ownership
   │
   ▼
Client User Service
   │
   ├── PostgreSQL
   ├── Redis
   ├── Event Bus
   ├── Audit Service
   ├── Notification Service
   └── AI Gateway
```

---

## 11. Error Handling Requirements

The frontend shall handle:

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 User Not Found
409 Conflict
422 Validation Error
429 Rate Limited
500 Internal Server Error
503 Service Unavailable
```

Errors shall return machine-readable error codes.

Example:

```json
{
  "error": {
    "code": "USER_ROLE_ASSIGNMENT_FORBIDDEN",
    "message": "You are not authorized to assign this role.",
    "request_id": "req_123"
  }
}
```

---

## 12. Security Requirements

## SEC-001

Users shall never access another organization's user directory.

## SEC-002

Administrative APIs shall enforce authorization server-side.

## SEC-003

Privilege escalation shall be prevented.

## SEC-004

Deleted users shall lose authentication access immediately.

## SEC-005

Suspended users shall have active sessions revoked.

## SEC-006

Bulk operations shall require appropriate authorization.

## SEC-007

Exports shall be permission-controlled and audited.

## SEC-008

Sensitive operations shall optionally require MFA step-up authentication.

## SEC-009

AI agents shall use scoped credentials and tools.

## SEC-010

All security-sensitive mutations shall be auditable.

---

## 13. Observability Requirements

The module shall expose:

## Metrics

```text
active_users
inactive_users
pending_invitations
suspended_users
user_creation_rate
user_deactivation_rate
invitation_acceptance_rate
login_success_rate
login_failure_rate
mfa_adoption_rate
role_change_rate
permission_change_rate
bulk_operation_failure_rate
```

## Logs

Structured logs shall include:

```text
timestamp
service
user_id
organization_id
request_id
correlation_id
action
result
latency
error_code
```

## Tracing

Distributed traces shall cover:

```text
Frontend
 → API Gateway
 → Auth Service
 → Authorization Service
 → User Service
 → Database
 → Event Bus
 → Notification Service
 → Audit Service
```

---

## 14. Reliability Requirements

The Client Users module shall:

* Avoid duplicate user creation
* Prevent lost membership updates
* Support retry-safe operations
* Support idempotency
* Maintain audit consistency
* Recover from partial failures
* Handle event replay
* Support database failover
* Support graceful degradation

---

## 15. Acceptance Criteria

## AC-001

An authorized Organization Admin can view users belonging to their organization.

## AC-002

An unauthorized user cannot retrieve another organization's users.

## AC-003

An authorized administrator can invite a user.

## AC-004

An invited user can securely complete onboarding.

## AC-005

An administrator can assign an allowed role.

## AC-006

An administrator cannot assign a role above their authorization level.

## AC-007

An administrator can assign teams and workplaces.

## AC-008

An administrator can manage project access.

## AC-009

An administrator can manage AI-agent access.

## AC-010

Suspending a user revokes active sessions according to policy.

## AC-011

All sensitive user mutations create audit events.

## AC-012

Bulk operations are tracked using an operation ID.

## AC-013

Failed bulk operations expose actionable failure information.

## AC-014

User exports require explicit authorization.

## AC-015

AI can search and analyze users without bypassing authorization.

## AC-016

AI cannot perform restricted mutations without required approval.

## AC-017

The frontend reflects backend authorization decisions.

## AC-018

User state changes propagate to dependent services through events.

## AC-019

A removed user cannot authenticate after access revocation.

## AC-020

The system maintains tenant isolation under concurrent, malformed and unauthorized requests.

---

## 16. End-to-End User Lifecycle

```text
Administrator
      │
      ▼
Open Client Users
      │
      ▼
Create / Invite User
      │
      ▼
Validate Authorization
      │
      ▼
Validate Tenant
      │
      ▼
Create Invitation
      │
      ▼
Send Notification
      │
      ▼
User Accepts Invitation
      │
      ▼
Identity Verification
      │
      ▼
Account Creation
      │
      ▼
Organization Membership
      │
      ▼
Workplace Assignment
      │
      ▼
Team Assignment
      │
      ▼
Role Assignment
      │
      ▼
Permission Evaluation
      │
      ▼
Project Access
      │
      ▼
AI Agent Access
      │
      ▼
Audit Event
      │
      ▼
Analytics Event
      │
      ▼
Active User
```

---

## 17. AI + Human User Management Architecture

```text
                         CLIENT ADMIN
                              │
                              ▼
                       CLIENT USERS UI
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
          HUMAN OPERATIONS           AI ASSISTANT
                 │                         │
                 │                  AI ANALYSIS
                 │                         │
                 │                  RECOMMENDATION
                 │                         │
                 │                         ▼
                 │                  POLICY ENGINE
                 │                         │
                 └────────────┬────────────┘
                              ▼
                       API GATEWAY
                              │
                              ▼
                     AUTHENTICATION
                              │
                              ▼
                      AUTHORIZATION
                    ┌─────────┼─────────┐
                    ▼         ▼         ▼
                  RBAC      ABAC     TENANT
                                      ISOLATION
                              │
                              ▼
                       USER SERVICE
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
        PostgreSQL        Redis Cache       Event Bus
             │                                 │
             │             ┌───────────────────┼───────────────┐
             │             ▼                   ▼               ▼
             │       Audit Service      Notification       Analytics
             │
             ▼
      Organization Service
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
    Teams  Workplaces Projects
                              │
                              ▼
                         AI Gateway
                              │
                    ┌─────────┼─────────┐
                    ▼         ▼         ▼
                 LLMs      AI Agents   Guardrails
```

---

## 18. Required Frontend Screens

```text
/client/users
/client/users/new
/client/users/invitations
/client/users/{id}
/client/users/{id}/profile
/client/users/{id}/roles
/client/users/{id}/permissions
/client/users/{id}/teams
/client/users/{id}/workplaces
/client/users/{id}/projects
/client/users/{id}/ai-agents
/client/users/{id}/sessions
/client/users/{id}/activity
/client/users/{id}/audit
/client/users/{id}/security
/client/users/access-review
/client/users/import
/client/users/export
```

---

## 19. Required Backend Services

```text
API Gateway
Identity Service
User Service
Organization Service
Workplace Service
Team Service
Authorization Service
RBAC Service
ABAC Policy Engine
Project Service
AI Agent Service
Audit Service
Notification Service
Analytics Service
Search Service
Event Bus
AI Gateway
Security Service
```

---

## 20. Non-Functional Quality Targets

The implementation should target:

```text
Availability:
≥ 99.9%

Authorization:
100% server-side enforcement

Tenant Isolation:
100%

Audit Coverage:
100% for security-sensitive mutations

API Reliability:
≥ 99.9% successful requests excluding client errors

Search:
Low-latency indexed retrieval

Bulk Operations:
Asynchronous for large workloads

Observability:
Distributed tracing + structured logging + metrics

Security:
Zero-trust authorization model

AI Safety:
Policy-controlled tool execution

Data Integrity:
No unauthorized privilege escalation

Consistency:
Strong consistency for security-critical mutations
```

---

## 21. Definition of Done

The Client Users module is considered production-ready only when:

* [ ] User directory is implemented
* [ ] User search is implemented
* [ ] Filtering and pagination are implemented
* [ ] User invitation is implemented
* [ ] User onboarding is implemented
* [ ] Profile management is implemented
* [ ] Role management is implemented
* [ ] Permission management is implemented
* [ ] Team assignment is implemented
* [ ] Workplace assignment is implemented
* [ ] Project access management is implemented
* [ ] AI-agent access management is implemented
* [ ] Activation/deactivation is implemented
* [ ] Suspension is implemented
* [ ] Session management is implemented
* [ ] MFA management is integrated
* [ ] Audit logging is integrated
* [ ] Notifications are integrated
* [ ] Analytics events are integrated
* [ ] Bulk operations are implemented
* [ ] Import/export is implemented
* [ ] Access reviews are implemented
* [ ] RBAC is enforced
* [ ] ABAC is enforced
* [ ] Tenant isolation is enforced
* [ ] AI user-management tools are implemented
* [ ] AI guardrails are implemented
* [ ] Human approval workflows are implemented
* [ ] Security-sensitive AI actions require authorization
* [ ] Frontend is fully connected to backend APIs
* [ ] Backend remains the authoritative source of user state
* [ ] Distributed tracing is implemented
* [ ] Metrics are implemented
* [ ] Structured logging is implemented
* [ ] Automated tests cover critical workflows
* [ ] Security testing is completed
* [ ] Performance testing is completed
* [ ] Accessibility requirements are satisfied
* [ ] Internationalization/localization is supported
* [ ] Disaster-recovery behavior is validated
* [ ] Production monitoring and alerting are enabled
