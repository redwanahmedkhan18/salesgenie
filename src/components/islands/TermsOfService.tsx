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

export default function TermsOfService() {
  const effectiveDate = 'August 8, 2026';

  return (
    <div className="max-w-4xl mx-auto px-6 py-12">
      <div className="mb-12 text-center">
        <h1 className="text-4xl font-bold mb-3" style={{ color: 'var(--color-foreground)' }}>Terms of Service</h1>
        <p className="text-sm" style={{ color: 'var(--color-mute)' }}>Last updated: {effectiveDate}</p>
      </div>

      <div className="prose prose-sm max-w-none mb-12" style={{ color: 'var(--color-body)' }}>
        <p>
          These Terms of Service ("Terms") constitute a legally binding agreement between you
          ("you", "your", or "User") and SalesGenie, Inc. ("SalesGenie", "we", "us", or "our")
          governing your access to and use of the SalesGenie platform, including all associated
          websites, applications, APIs, and services (collectively, the "Platform").
        </p>
        <p>
          By accessing or using the Platform, you acknowledge that you have read, understood, and
          agreed to be bound by these Terms. If you do not agree with all the terms and conditions,
          you are expressly prohibited from using the Platform.
        </p>
      </div>

      <Section title="1. Eligibility">
        <p>
          The Platform is offered and available to individuals who are at least 18 years of age
          and are capable of forming a binding contract under applicable law. By using the Platform,
          you represent and warrant that you are of legal age to form a binding contract and that
          all registration information you submit is accurate, complete, and current. If you are
          using the Platform on behalf of a legal entity, you represent that you are authorized to
          bind that entity to these Terms.
        </p>
      </Section>

      <Section title="2. Account Registration & Security">
        <p>
          To access certain features of the Platform, you must register for an account. You agree
          to provide accurate, current, and complete information during registration and to
          promptly update such information as needed. You are responsible for maintaining the
          confidentiality of your account credentials and for all activities that occur under your
          account. You must notify us immediately of any unauthorized use of your account.
        </p>
        <p>
          You agree not to:
        </p>
        <ul className="list-disc list-inside mt-3 space-y-1">
          <li>Share your account credentials with any third party;</li>
          <li>Use any false or inaccurate information to create an account;</li>
          <li>Create an account if you have been previously removed or suspended by us;</li>
          <li>Engage in any data scraping or automated data collection without our express written consent.</li>
        </ul>
      </Section>

      <Section title="3. License Grant">
        <p>
          Subject to these Terms, SalesGenie grants you a limited, non-exclusive,
          non-transferable, non-sublicensable right to access and use the Platform for your
          internal business purposes. This license does not include the right to resell,
          redistribute, or create derivative works based on the Platform, except as expressly
          authorized in writing by SalesGenie.
        </p>
      </Section>

      <Section title="4. Acceptable Use">
        <p>You agree not to use the Platform to:</p>
        <ul className="list-disc list-inside mt-3 space-y-1">
          <li>Violate any applicable law, regulation, or third-party right;</li>
          <li>Transmit any content that is defamatory, obscene, or infringing;</li>
          <li>Interfere with or disrupt the Platform's functionality or security;</li>
          <li>Attempt to gain unauthorized access to any portion of the Platform;</li>
          <li>Use any automated system (including bots or scrapers) to access the Platform;</li>
          <li>Misrepresent your identity or affiliation with any person or entity;</li>
          <li>Collect or harvest personal information from other users without their consent.</li>
        </ul>
      </Section>

      <Section title="5. Subscription & Billing">
        <p>
          Certain features of the Platform may require a paid subscription. By subscribing, you
          authorize SalesGenie to charge the payment method provided. Fees are non-refundable
          except as required by law or as explicitly stated in our refund policy. We may change
          pricing upon 30 days' notice.
        </p>
      </Section>

      <Section title="6. Intellectual Property">
        <p>
          The Platform, including all content, logos, trademarks, and intellectual property, are
          owned by SalesGenie or its licensors and are protected by copyright, trademark, and
          other intellectual property laws. These Terms do not grant you any right, title, or
          interest in or to the Platform or any content, except for the limited license
          described in Section 3.
        </p>
      </Section>

      <Section title="7. User Content">
        <p>
          You retain ownership of any content you upload or submit through the Platform. By
          submitting content, you grant SalesGenie a worldwide, non-exclusive, royalty-free,
          sublicensable, and transferable license to use, reproduce, distribute, and display such
          content solely in connection with providing and improving the Platform. You represent
          that you have all necessary rights to submit such content and that it does not violate
          these Terms or any third-party rights.
        </p>
      </Section>

      <Section title="8. Disclaimer of Warranties">
        <p>
          THE PLATFORM IS PROVIDED ON AN "AS IS" AND "AS AVAILABLE" BASIS WITHOUT WARRANTIES OF
          ANY KIND, EITHER EXPRESS OR IMPLIED. SALESGENIE DISCLAIMS ALL WARRANTIES, INCLUDING
          IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
          NON-INFRINGEMENT. WE DO NOT WARRANT THAT THE PLATFORM WILL BE UNINTERRUPTED OR ERROR-FREE,
          THAT DEFECTS WILL BE CORRECTED, OR THAT THE PLATFORM IS FREE OF VIRUSES OR OTHER
          HARMFUL COMPONENTS.
        </p>
      </Section>

      <Section title="9. Limitation of Liability">
        <p>
          TO THE FULLEST EXTENT PERMITTED BY LAW, IN NO EVENT SHALL SALESGENIE BE LIABLE FOR ANY
          INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES, OR ANY LOSS OF
          PROFITS, DATA, USE, OR OTHER INTANGIBLE LOSSES, ARISING OUT OF OR IN CONNECTION WITH
          YOUR USE OF THE PLATFORM. OUR TOTAL LIABILITY TO YOU FOR ALL CLAIMS SHALL NOT EXCEED THE
          GREATER OF THE AMOUNT PAID BY YOU TO SALESGENIE IN THE 12 MONTHS PRECEDING THE CLAIM OR
          $100 USD.
        </p>
      </Section>

      <Section title="10. Indemnification">
        <p>
          You agree to defend, indemnify, and hold harmless SalesGenie, its affiliates, and their
          respective directors, officers, employees, and agents from and against any and all
          claims, liabilities, damages, losses, or expenses arising out of or in connection with
          your access to or use of the Platform, your violation of these Terms, or your
          infringement of any third-party right.
        </p>
      </Section>

      <Section title="11. Termination">
        <p>
          We may suspend or terminate your access to all or any part of the Platform at any time,
          with or without cause, with or without notice. Upon termination, all licenses granted
          under these Terms shall immediately cease. We shall not be liable to you or any third
          party for any termination of your access to or use of the Platform.
        </p>
      </Section>

      <Section title="12. Governing Law & Dispute Resolution">
        <p>
          These Terms shall be governed by and construed in accordance with the laws of the State
          of Delaware, United States, without regard to its conflict of law principles. Any
          dispute, controversy, or claim arising out of or relating to these Terms or the
          Platform shall be resolved exclusively by the state or federal courts located in Delaware,
          and you consent to the jurisdiction and venue of those courts.
        </p>
        <p>
          Any dispute between the parties that cannot be resolved through direct negotiation shall
          first be submitted to non-binding mediation before proceeding to litigation. If mediation
          fails, either party may pursue resolution through the courts.
        </p>
      </Section>

      <Section title="13. Changes to These Terms">
        <p>
          We may update these Terms from time to time. If we make material changes, we will
          provide notice through the Platform and, where appropriate, via email. Your continued
          use of the Platform after such changes constitutes your acceptance of the revised Terms.
          The "Last updated" date at the top of these Terms will reflect the effective date of the
          most recent revision.
        </p>
      </Section>

      <Section title="14. Miscellaneous">
        <p>
          These Terms, together with our Privacy Policy and any other legal notices published by
          SalesGenie, constitute the entire agreement between you and SalesGenie regarding the
          Platform. If any provision of these Terms is held to be invalid or unenforceable, the
          remaining provisions will remain in full force. Our failure to enforce any right or
          provision of these Terms shall not constitute a waiver of such right or provision.
        </p>
        <p>
          You may not assign or transfer these Terms without our prior written consent. SalesGenie
          may assign these Terms without restriction. Nothing in these Terms creates a
          partnership, joint venture, or agency relationship between you and SalesGenie.
        </p>
      </Section>

      <Section title="15. Contact Information">
        <p>
          If you have any questions about these Terms, please contact us:
        </p>
        <ul className="list-none">
          <li>Email: <a href="mailto:legal@salesgenie.ai" className="text-[var(--color-link-blue)] hover:underline">legal@salesgenie.ai</a></li>
          <li>Address: 123 AI Plaza, San Francisco, CA 94105, United States</li>
        </ul>
      </Section>
    </div>
  );
}
