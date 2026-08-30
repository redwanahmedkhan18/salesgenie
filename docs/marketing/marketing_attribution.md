# SalesGenie — Marketing Attribution & Touchpoint Analytics Engine

## FAANG-Level User Requirements, System Requirements & Functional Requirements

> **Document:** `marketing_attribution.md`  
> **Product:** SalesGenie  
> **Module:** Multi-Touch Marketing Attribution Platform  
> **Architecture:** Real-Time Stream Processing / Event-Driven / ML Analytics

---

## 1. Document Purpose

This document outlines the requirements for SalesGenie's Marketing Attribution module. The system tracks prospect touchpoints across organic, paid, social, email, and sales outreach to accurately measure ROI and credit revenue contribution.

---

## 2. Touchpoint Attribution Pipeline

```text
Customer Interaction Events (Web, Ads, Email, Sales Call)
                           ↓
              Identity Resolution Engine
                           ↓
             Attribution Model Calculation
     +---------------------+---------------------+
     |                     |                     |
     v                     v                     v
First-Touch            Last-Touch           Multi-Touch (W-Shaped / AI)
     |                     |                     |
     +---------------------+---------------------+
                           v
           Revenue & Campaign ROI Reporting
```

---

## 3. Core Functional Requirements

### 3.1 Multi-Touch Model Support (FR-MA-001)

- System SHALL support First-Touch, Last-Touch, Linear, Time-Decay, U-Shaped, W-Shaped, and Data-Driven ML attribution models.

### 3.2 Omnichannel Identity Stitching (FR-MA-002)

- Anonymous web sessions SHALL retroactively stitch to identified CRM contacts upon form submission or email click.

### 3.3 Campaign ROI Calculation (FR-MA-003)

- Real-time spend from ad platforms (Google, Meta, LinkedIn) SHALL combine with closed-won CRM deal revenue to present accurate Customer Acquisition Cost (CAC) and Return on Ad Spend (ROAS).
