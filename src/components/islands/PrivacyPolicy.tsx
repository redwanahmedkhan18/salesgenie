import React from 'react';
import type { ReactNode } from 'react';

interface ProseProps {
  children: ReactNode;
}

function Prose({ children }: ProseProps) {
  return <div className="prose prose-sm max-w-none text-[var(--color-body)] prose-headings:text-[var(--color-foreground)] prose-a:text-[var(--color-link-blue)] prose-a:hover:underline prose-strong:text-[var(--color-foreground)]">{children}</div>;
}

function Section({ title, children }: { title: string; children: ReactNode }) {
  return (
    <section className="mb-10">
      <h2 className="text-xl font-semibold mb-4 pb-2 border-b" style={{ color: 'var(--color-foreground)', borderColor: 'var(--color-hairline)' }}>{title}</h2>
      <Prose>{children}</Prose>
    </section>
  );
}

function InfoCard({ title, children }: { title: string; children: ReactNode }) {
  return (
    <div className="rounded-xl p-6 mb-6" style={{ background: 'var(--color-surface-soft)', border: '1px solid var(--color-hairline)' }}>
      <h3 className="font-semibold mb-2" style={{ color: 'var(--color-foreground)' }}>{title}</h3>
      <div className="text-sm" style={{ color: 'var(--color-body)' }}>{children}</div>
    </div>
  );
}

export default function PrivacyPolicy() {
  const effectiveDate = 'August 8, 2026';

  return (
    <div className="max-w-4xl mx-auto px-6 py-12">
      <div className="mb-12 text-center">
        <h1 className="text-4xl font-bold mb-3" style={{ color: 'var(--color-foreground)' }}>Privacy Policy</h1>
        <p className="text-sm" style={{ color: 'var(--color-mute)' }}>Last updated: {effectiveDate}</p>
      </div>

      <InfoCard title="In short">
        <p>
          We collect personal data that you provide directly to us, such as when you register for
          an account, and certain automatically-collected information like your IP address and
          device information. We use this data to provide, personalize, and improve the SalesGenie
          platform, to communicate with you, and for security and compliance purposes. We retain
          data for as long as necessary to provide our services and fulfill our legal obligations.
          You have rights to access, correct, and delete your personal data.
        </p>
      </InfoCard>

      <div className="prose prose-sm max-w-none mb-12" style={{ color: 'var(--color-body)' }}>
        <p>
          SalesGenie, Inc. ("SalesGenie", "we", "us", or "our") is committed to protecting your
          privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your
          personal information when you use our platform, websites, applications, and services
          (collectively, the "Platform"). Please read this Privacy Policy carefully. If you do not
          agree with the terms of this Privacy Policy, you are expressly prohibited from using the
          Platform.
        </p>
      </div>

      <Section title="1. Information We Collect">
        <p><strong className="font-semibold">Information You Provide Directly</strong></p>
        <p>We collect personal data that you voluntarily provide to us directly, including:</p>
        <ul className="list-disc list-inside mt-2 space-y-1">
          <li><strong>Account Information</strong> — name, email address, company name, job title, and phone number when you register or update your profile.</li>
          <li><strong>Communication Data</strong> — content of messages, support tickets, feedback, and any files you upload.</li>
          <li><strong>Payment Information</strong> — payment card details processed by our third-party payment providers (we do not store full card numbers).</li>
          <li><strong>Consent Records</strong> — your preferences regarding marketing communications and cookie settings.</li>
        </ul>

        <p className="mt-4"><strong className="font-semibold">Information Collected Automatically</strong></p>
        <p>We automatically collect certain information about your device and usage of the Platform:</p>
        <ul className="list-disc list-inside mt-2 space-y-1">
          <li><strong>Usage Data</strong> — pages visited, features used, time spent, clicks, scroll events, and error reports.</li>
          <li><strong>Device Information</strong> — IP address, browser type, operating system, device identifiers, and browser language.</li>
          <li><strong>Network Data</strong> — network connection type, carrier, and standard web log information.</li>
          <li><strong>Location Data</strong> — approximate location derived from your IP address.</li>
          <li><strong>Cookies & Tracking</strong> — we use cookies and similar tracking technologies as described in our Cookie Policy.</li>
        </ul>
      </Section>

      <Section title="2. How We Use Your Information">
        <p>We use the information we collect for the following purposes:</p>
        <ul className="list-disc list-inside mt-3 space-y-1">
          <li><strong>Provide & Maintain the Platform</strong> — to create and manage your account, authenticate your access, and deliver the services you request.</li>
          <li><strong>Improve & Personalize</strong> — to understand how you use the Platform, personalize your experience, and recommend relevant features or content.</li>
          <li><strong>Communicate</strong> — to send you service-related notifications, respond to your inquiries, and (if opted in) marketing communications.</li>
          <li><strong>Security & Fraud Prevention</strong> — to detect fraudulent activity, enforce our terms, protect our systems, and comply with security requirements.</li>
          <li><strong>Analytics & Performance</strong> — to monitor platform usage, measure performance, and conduct internal analytics.</li>
          <li><strong>Legal Compliance</strong> — to comply with applicable laws, regulations, subpoenas, and lawful requests.</li>
        </ul>
      </Section>

      <Section title="3. Legal Basis for Processing">
        <p>
          Our legal basis for collecting and using personal data depends on the information
          concerned and the context in which we collect it. We rely on the following legal bases:
        </p>
        <ul className="list-disc list-inside mt-3 space-y-1">
          <li><strong>Contractual Necessity</strong> — processing is necessary to perform our agreement with you (e.g., providing the Platform).</li>
          <li><strong>Legitimate Interests</strong> — processing is necessary for our legitimate interests, including platform security, analytics, and fraud prevention.</li>
          <li><strong>Consent</strong> — we may ask for your consent to process certain data for specific purposes (e.g., marketing emails).</li>
          <li><strong>Legal Obligation</strong> — processing is necessary to comply with applicable laws (e.g., tax, audit, or law enforcement requests).</li>
        </ul>
        <p className="mt-3">
          Under the GDPR, CCPA, and similar laws, you may have rights including access, rectification,
          erasure, restriction, data portability, and objection. See Section 7 for details.
        </p>
      </Section>

      <Section title="4. How We Share Your Information">
        <p>
          We do not sell your personal data. We share your information with third parties only in
          the following circumstances:
        </p>
        <ul className="list-disc list-inside mt-3 space-y-1">
          <li><strong>Service Providers</strong> — trusted third parties who perform services on our behalf (e.g., hosting, analytics, payment processing, email delivery, customer support).</li>
          <li><strong>Business Transfers</strong> — in connection with a merger, acquisition, financing, or sale of assets, we may transfer your data to the acquiring entity.</li>
          <li><strong>Legal Compliance</strong> — to comply with applicable law, respond to lawful requests, or protect our rights, privacy, safety, or property.</li>
          <li><strong>Vital Interests</strong> — to protect the vital interests of our users or the public where required by law.</li>
          <li><strong>With Your Consent</strong> — to perform other activities that require your consent.</li>
        </ul>
      </Section>

      <Section title="5. Cookies & Tracking Technologies">
        <p>
          We use cookies and similar tracking technologies to enhance your experience, analyze
          usage, and secure the Platform. You can control cookies through your browser settings.
          For more details, please review our separate <a href="/cookies">Cookie Policy</a>.
          We use:
        </p>
        <ul className="list-disc list-inside mt-3 space-y-1">
          <li><strong>Essential Cookies</strong> — required for authentication and core functionality.</li>
          <li><strong>Performance Cookies</strong> — to understand how visitors interact with our services.</li>
          <li><strong>Functional Cookies</strong> — to remember your preferences.</li>
        </ul>
      </Section>

      <Section title="6. Data Security">
        <Prose>
          <p>
            We implement commercially reasonable technical and organizational measures to protect
            your personal data from unauthorized access, alteration, disclosure, or destruction.
            These measures include encryption in transit (TLS/SSL) and at rest, access controls,
            regular security assessments, and personnel training.
          </p>
          <p>
            However, no method of transmission over the internet or electronic storage is 100%
            secure. We strive to use commercially acceptable means to protect your data but
            cannot guarantee absolute security. In the event of a data breach, we will notify
            affected users and relevant authorities as required by law.
          </p>
        </Prose>
      </Section>

      <Section title="7. Your Privacy Rights & Choices">
        <p>
          Depending on your location and applicable law, you may have the following rights
          regarding your personal data:
        </p>
        <ul className="list-disc list-inside mt-3 space-y-1">
          <li><strong>Access</strong> — request details about the personal data we hold about you.</li>
          <li><strong>Rectification</strong> — request correction of inaccurate or incomplete data.</li>
          <li><strong>Erasure</strong> — request deletion of your personal data (subject to legal obligations).</li>
          <li><strong>Restriction</strong> — request limitation of processing under certain conditions.</li>
          <li><strong>Data Portability</strong> — request a copy of your data in a structured, machine-readable format.</li>
          <li><strong>Objection</strong> — object to processing based on legitimate interests or direct marketing.</li>
          <li><strong>Withdraw Consent</strong> — withdraw previously given consent at any time.</li>
        </ul>
        <InfoCard title="How to exercise your rights">
          You may submit a request to exercise your privacy rights by emailing
          <a href="mailto:privacy@salesgenie.ai" className="text-[var(--color-link-blue)] hover:underline"> privacy@salesgenie.ai</a>.
          We will respond within 30 days of receiving your request. For data portability and
          certain other requests, we may need to verify your identity before fulfilling your request.
        </InfoCard>
      </Section>

      <Section title="8. Data Retention">
        <Prose>
          <p>
            We retain personal data for as long as necessary to provide the Platform and fulfill
            the purposes described in this Privacy Policy, unless a longer retention period is
            required by law. Our retention schedule considers:
          </p>
          <ul>
            <li><strong>Account Data</strong> — retained while your account is active or as needed to provide services.</li>
            <li><strong>Usage Data</strong> — retained for up to 24 months for analytics and performance optimization.</li>
            <li><strong>Support Records</strong> — retained for up to 24 months for quality assurance.</li>
            <li><strong>Audit & Compliance</strong> — retained as required by applicable regulations (e.g., 7 years for tax records).</li>
          </ul>
          <p>
            When data is no longer necessary or upon your request, we will securely delete or
            anonymize it.
          </p>
        </Prose>
      </Section>

      <Section title="9. International Data Transfers">
        <Prose>
          <p>
            The Platform is hosted in the United States. If you are accessing the Platform from
            outside the United States, please note that your information may be transferred to,
            stored, and processed in the United States and other countries where our service
            providers operate. By using the Platform, you consent to such transfers.
          </p>
          <p>
            When transferring personal data outside the European Economic Area (EEA), UK, or
            Switzerland, we rely on appropriate safeguards, including Standard Contractual Clauses
            (SCCs), to ensure your data remains protected.
          </p>
        </Prose>
      </Section>

      <Section title="10. Third-Party Services & Links">
        <Prose>
          <p>
            The Platform may contain links to third-party websites, services, or integrations
            (e.g., Google, Microsoft, payment processors). This Privacy Policy does not apply to
            those third-party services. We are not responsible for the content, privacy practices,
            or data collection of third-party services. We encourage you to read their privacy
            policies before providing any personal information.
          </p>
        </Prose>
      </Section>

      <Section title="11. Children's Privacy">
        <Prose>
          <p>
            The Platform is not intended for children under the age of 13 (or 16 where applicable
            under local law such as the GDPR). We do not knowingly collect personal data from
            children. If we become aware that we have collected data from a child, we will take
            steps to delete such information. If you believe a child has provided us with personal
            data, please contact us immediately.
          </p>
        </Prose>
      </Section>

      <Section title="12. Changes to This Privacy Policy">
        <Prose>
          <p>
            We may update this Privacy Policy from time to time. We will notify you of any
            material changes by posting the new Privacy Policy on the Platform and updating the
            "Last updated" date. Where required by law, we will provide notice via email or
            through the Platform before the change takes effect.
          </p>
        </Prose>
      </Section>

      <Section title="13. Contact Us">
        <Prose>
          <p>
            If you have any questions about this Privacy Policy, the data we hold about you, or
            wish to exercise your rights, please contact our Data Protection Officer / Privacy
            Team:
          </p>
          <ul>
            <li>Email: <a href="mailto:privacy@salesgenie.ai" className="text-[var(--color-link-blue)] hover:underline">privacy@salesgenie.ai</a></li>
            <li>Mailing Address: SalesGenie, Inc., Attn: DPO, 123 AI Plaza, San Francisco, CA 94105, United States</li>
            <li>DPO (EEA/UK): <a href="mailto:dpo@salesgenie.ai" className="text-[var(--color-link-blue)] hover:underline">dpo@salesgenie.ai</a></li>
          </ul>
        </Prose>
      </Section>
    </div>
  );
}
