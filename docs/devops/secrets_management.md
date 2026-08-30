# SalesGenie — Secrets Management Infrastructure Requirements

## FAANG-Level User Requirements, System Requirements & Functional Requirements

> **Document:** `secrets_management.md`  
> **Product:** SalesGenie  
> **Module:** Secrets Management & Key Protection Infrastructure  
> **Architecture:** Zero Trust / Multi-Tenant SaaS / Event-Driven Microservices / Cloud-Native  
> **Security Standard:** SOC2 Type II / ISO 27001 / FIPS 140-3 / FAANG-Level Security

---

## 1. Document Purpose

This document defines the **User Requirements (UR)**, **System Requirements (SR)**, and **Functional Requirements (FR)** for the centralized Secrets Management infrastructure of SalesGenie.

The secrets management architecture SHALL securely manage, rotate, audit, and inject credentials, API keys, certificates, cryptographic tokens, database strings, and third-party integration secrets across all microservices, multi-agent AI environments, and tenant workspaces.

---

## 2. Secrets Management Architecture Overview

```text
       +-------------------------------------------------------+
       |               HashiCorp Vault / AWS KMS               |
       +-------------------------------------------------------+
                                   |
           +-----------------------+-----------------------+
           |                                               |
           v                                               v
+-----------------------+                       +-----------------------+
|  Control Plane Secrets |                       | Tenant Integration    |
|  (DB, Redis, Kafka)   |                       | Secrets (OAuth, Keys) |
+-----------------------+                       +-----------------------+
           |                                               |
           +-----------------------+-----------------------+
                                   v
       +-------------------------------------------------------+
       |   Dynamic Rotation & Zero-Trust Secrets Injection     |
       +-------------------------------------------------------+
```

---

## 3. Core Requirements

### 3.1 Zero-Trust Secrets Injection (SR-SEC-001)

- Secrets SHALL NOT be written to source repositories, build images, or hardcoded in configuration files.
- Secrets SHALL be injected dynamically into application memory at runtime using identity-based Kubernetes init-containers or Vault Agent injectors.

### 3.2 Dynamic Rotation & Short-Lived Credentials (SR-SEC-002)

- Database credentials, cloud IAM tokens, and service-to-service keys SHALL support automated dynamic rotation with maximum TTL of 24 hours.
- Automated secret rotation SHALL cause zero downtime or service interruption.

### 3.3 Tenant Secret Isolation & Envelope Encryption (SR-SEC-003)

- Customer integration keys (e.g., Salesforce OAuth, OpenAI API keys, WhatsApp tokens) SHALL be encrypted using per-tenant encryption keys (Envelope Encryption).
- Key Encryption Keys (KEK) SHALL be managed inside HSM/KMS modules.

### 3.4 Immutable Audit Logging (SR-SEC-004)

- Every secret access, injection, rotation, or revocation event SHALL be logged immutably with timestamp, service identity, tenant ID, and IP address.
- Logs SHALL be shipped in real-time to SIEM and anomaly detection pipelines.

---

## 4. Operational Controls & Failure Modes

- **HSM / KMS Outage:** In-memory caching with encrypted cache fallback and graceful retry policies.
- **Compromised Secret:** Instant automated single-click or programmatic secret revocation and re-issuance across all running pods.
