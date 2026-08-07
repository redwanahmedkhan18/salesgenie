import React from 'react';
import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";

export default function IntegrationsApp() {
  return (
    <AuthProvider>
      <ProtectedRoute
        requiredRoles={[
          "org_admin",
          "super_admin",
          "workspace_admin",
          "knowledge_manager",
          "support_manager"
        ]}
      >
        <IntegrationsContent />
      </ProtectedRoute>
    </AuthProvider>
  );
}

function IntegrationsContent() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>Integrations</h1>
        <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
          Connect your existing tools and services to SalesGenie AI
        </p>
      </div>

      <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <h2 className="text-lg font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>Communication Channels</h2>
        <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>
          Configure your customer communication channels.
        </p>
        <ul className="list-disc list-inside space-y-2 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
          <li>WhatsApp - Facebook Business API integration</li>
          <li>SMS - Twilio gateway support</li>
          <li>Email - SMTP/IMAP configuration</li>
          <li>Website - Live chat widget</li>
          <li>Discord - Community server integration</li>
          <li>Slack - Workplace messaging</li>
        </ul>
      </div>

      <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <h2 className="text-lg font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>Enterprise Systems</h2>
        <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>
          Connect your business systems for seamless data flow.
        </p>
        <div className="grid gap-4 md:grid-cols-2">
          <div className="rounded-lg p-4" style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)' }}>
            <h3 className="font-semibold text-sm mb-2" style={{ color: 'var(--color-foreground)' }}>CRM Systems</h3>
            <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>HubSpot, Salesforce, Pipedrive</p>
          </div>
          <div className="rounded-lg p-4" style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)' }}>
            <h3 className="font-semibold text-sm mb-2" style={{ color: 'var(--color-foreground)' }}>Help Desk</h3>
            <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Zendesk, Freshdesk, Intercom</p>
          </div>
          <div className="rounded-lg p-4" style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)' }}>
            <h3 className="font-semibold text-sm mb-2" style={{ color: 'var(--color-foreground)' }}>Analytics</h3>
            <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Mixpanel, Amplitude, GA</p>
          </div>
          <div className="rounded-lg p-4" style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)' }}>
            <h3 className="font-semibold text-sm mb-2" style={{ color: 'var(--color-foreground)' }}>E-commerce</h3>
            <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Shopify, WooCommerce, Stripe</p>
          </div>
        </div>
      </div>

      <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <h2 className="text-lg font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>API Access</h2>
        <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>
          Manage API keys and webhook configurations.
        </p>
        <div className="flex gap-3">
          <button
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)', padding: '8px 16px', borderRadius: '6px', border: 'none', cursor: 'pointer' }}
          >
            Generate API Key
          </button>
          <button
            style={{ background: 'var(--color-secondary)', color: 'var(--color-on-secondary)', padding: '8px 16px', borderRadius: '6px', border: 'none', cursor: 'pointer' }}
          >
            View Webhooks
          </button>
        </div>
      </div>
    </div>
  );
}