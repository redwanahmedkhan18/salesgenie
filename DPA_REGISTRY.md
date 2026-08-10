# Data Processing Addendum (DPA) Registry

**Document Version:** 1.0  
**Effective Date:** 2026-08-09  
**Data Controller:** SalesGenie, Inc.  
**DPO Contact:** dpo@salesgenie.ai

---

## Subprocessor List

| Subprocessor | Service | Data Categories | Legal Basis | DPA Status | SCCs | Location |
|-------------|---------|----------------|-------------|------------|------|----------|
| **Stripe, Inc.** | Payment processing | payment_method, amount, invoice, customer_stripe_id | Contractual necessity | Signed | Yes (EU) | USA |
| **Google Cloud Platform** | LLM inference (Gemini), Cloud Run, Cloud SQL | messages[], system_prompt, conversation_history | Contractual necessity + Legitimate interest | Signed | Yes (EU) | USA |
| **Groq Inc.** | LLM inference (LLaMA) | messages[], system_prompt | Contractual necessity + Legitimate interest | **Signed** | Yes (EU) | USA |
| **Mistral AI** | LLM inference | messages[], system_prompt | Contractual necessity + Legitimate interest | **Signed** | Yes (EU) | France |
| **SendGrid (Twilio SendGrid)** | Email delivery | email_address, email_content, name | Contractual necessity | Signed | Yes (EU) | USA |
| **Meta Platforms, Inc.** | WhatsApp Business API | phone_number, message_content, conversation_history | Contractual necessity | **Sign pending** | Yes (EU) | USA |
| **Telegram FZ LLC** | Telegram Bot API | message_content, bot_token | Contractual necessity | **Not executed** | No | UAE |
| **Discord Inc.** | Discord Bot API | message_content, channel_id | Contractual necessity | **Not executed** | No | USA |
| **Twilio Inc.** | SMS messaging | phone_number, sms_content | Contractual necessity | Signed | Yes (EU) | USA |
| **Slack Technologies LLC** | Slack Bot API | channel_id, message_content, email | Contractual necessity | Signed | Yes (EU) | USA |
| **Amazon Web Services** | S3, RDS, ECS, CloudFront | file_attachments, database, logs | Contractual necessity | Signed (AWS DPA) | Yes (EU) | USA |
| **Cloudflare, Inc.** | CDN, DDoS, WAF | request_logs, ip_address | Legitimate interest | Signed | Yes (EU) | USA |
| **Vercel Inc.** | Frontend hosting | page_views, user_agent | Contractual necessity | Signed | Yes (EU) | USA |
| **Sentry (Functional Software)** | Error monitoring | error_tracebacks, request_metadata | Legitimate interest | **Not executed** | No | USA |
| **New Relic** | Infrastructure monitoring | host_metrics, container_logs | Legitimate interest | **Not executed** | No | USA |

---

## Data Minimization Per Subprocessor

### LLM Providers (Groq, Google, Mistral)
**What is sent:**
- `messages[]` — conversation content (may contain PII in user messages)
- `system_prompt` — agent instructions (no PII)
- `temperature`, `max_tokens`, `top_p` — inference parameters (no PII)

**What is NOT sent:**
- `tenant_id` — not included in API payloads
- `user_id` — not included in API payloads
- `auth_token` / JWT — never sent
- User email/phone — only included as message content (user-provided context)
- Conversation metadata (timestamps, IDs, statuses) — not sent

**Retention:** Per provider ToS, data used for training is retained for 30 days for abuse monitoring, then deleted.

### Communication Providers (Meta, Telegram, Discord, Slack, Twilio, SendGrid)
**What is sent:**
- `phone_number` / `email_address` — required for message routing
- `message_content` — the actual message text

**What is NOT sent:**
- `auth_token` / JWT — never shared
- `tenant_id` — not included in channel integration payloads
- Internal user IDs — mapped to channel-specific user IDs
- Billing/payment data — not shared with communication providers

**Retention:** Per provider ToS, message content retained for 90 days for delivery status tracking.

### Payment Provider (Stripe)
**What is sent:**
- `payment_method` token (created client-side via Stripe.js)
- `amount`, `currency` — transaction details
- `customer_stripe_id` — Stripe's internal customer ID

**What is NOT sent:**
- Raw card numbers — tokenized by Stripe.js, never touch our servers
- User email — only used for receipt delivery via Stripe, no access to us
- Tenant ID — mapped to internal Stripe customer object

---

## International Data Transfer Mechanisms

| Subprocessor | Transfer Basis | SCC Version | Date Executed |
|-------------|---------------|-------------|---------------|
| Stripe | SCCs (Controller-to-Processor) | EU SCCs 2021 | 2025-01-15 |
| Google Cloud | SCCs (Processor) | EU SCCs 2021 | 2024-06-01 |
| Groq | SCCs (Processor) | EU SCCs 2021 | 2025-03-22 |
| Mistral AI | SCCs (Processor) | EU SCCs 2021 | 2025-02-10 |
| SendGrid | SCCs (Processor) | EU SCCs 2021 | 2024-11-03 |
| Twilio | SCCs (Processor) | EU SCCs 2021 | 2025-01-15 |
| AWS | SCCs (Processor) + BCIA certification | EU SCCs 2021 | 2024-03-01 |
| Cloudflare | SCCs (Processor) | EU SCCs 2021 | 2024-05-20 |
| Vercel | SCCs (Processor) | EU SCCs 2021 | 2025-04-01 |

**Note:** The platform is hosted in the United States (us-east-1). Transfers from the EEA/UK/Switzerland rely on Standard Contractual Clauses (SCCs) as the transfer mechanism.

---

## Actions Required

### Legal Team
1. **Execute DPAs** with Meta (WhatsApp), Telegram, Discord, Sentry, and New Relic
2. **Review and sign** SCCs with all subprocessors listed as "Sign pending" or "Not executed"
3. **Verify data localization** options for EU customers requiring EU-only data processing

### Engineering Team
1. **Implement subprocessor allowlist** — `PII_ENCRYPTION_KEY` in `config.py`
2. **Add per-request consent check** before sending data to LLM providers in `llm_provider.py`
3. **Implement audit trail** for all subprocessor data transfers
4. **Add data transfer logging** to compliance audit log

---

## DPA Registry Schema

Each DPA must include:
- **Parties**: Controller (SalesGenie, Inc.) and Processor (subprocessor)
- **Data Processing Description**: Purpose, duration, nature, and scope of processing
- **Categories of Personal Data**: PII, sensitive data, pseudonymized data
- **Obligations**: Security measures, subprocessor restrictions, assistance with rights requests, data deletion
- **Transfer Mechanism**: SCCs for international transfers
- **Liability**: Financial liability cap, indemnification terms
- **Termination**: Automatic on service termination
