import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';

interface CRMApiManagerProps {
  tenantId: string;
}

interface CRMIntegration {
  id: string;
  name: string;
  provider: 'hubspot' | 'salesforce' | 'pipedrive' | 'zoho';
  is_connected: boolean;
  created_at: string;
}

const CRM_PROVIDERS = [
  { id: 'hubspot', name: 'HubSpot', icon: '🔗', description: 'Full CRM integration' },
  { id: 'salesforce', name: 'Salesforce', icon: '⚡', description: 'Enterprise CRM' },
  { id: 'pipedrive', name: 'Pipedrive', icon: '📈', description: 'Sales pipeline focused' },
  { id: 'zoho', name: 'Zoho CRM', icon: '📝', description: 'SMB friendly CRM' },
];

export default function CRMApiManager({ tenantId }: CRMApiManagerProps) {
  const [integrations, setIntegrations] = useState<CRMIntegration[]>([]);
  const [loading, setLoading] = useState(true);
  const [showConnect, setShowConnect] = useState('');
  const [connectConfig, setConnectConfig] = useState({
    name: '',
    provider: 'hubspot' as const,
    api_key: '',
    webhook_url: '',
  });

  useEffect(() => {
    loadData();
  }, [tenantId]);

  const loadData = async () => {
    setLoading(true);
    try {
      // TODO: Implement API method for CRM integrations
      const integrationsRes: CRMIntegration[] = [];
      setIntegrations(integrationsRes || []);
    } catch (error) {
      console.error('Failed to load CRM integrations:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleConnect = async () => {
    if (!connectConfig.api_key) return;
    // TODO: Implement CRM connection logic
    setShowConnect('');
    loadData();
  };

  if (loading) {
    return <div className="text-center py-8">Loading CRM integrations...</div>;
  }

  return (
    <div className="space-y-4">
      <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>CRM Integrations</h3>
      
      <div className="grid gap-4">
        {CRM_PROVIDERS.map(provider => (
          <div key={provider.id} className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <span className="text-2xl">{provider.icon}</span>
                <div>
                  <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{provider.name}</div>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{provider.description}</div>
                </div>
              </div>
              <button
                onClick={() => setShowConnect(provider.id)}
                className="text-xs px-3 py-1 rounded border"
                style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
              >
                Connect
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Connect Modal */}
      {showConnect && (
        <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <h4 className="font-semibold mb-3">Connect {showConnect.toUpperCase()}</h4>
          <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>
            Enter your API credentials to establish the integration.
          </p>
          <div className="space-y-3">
            <input
              type="text"
              placeholder="Integration Name"
              value={connectConfig.name}
              onChange={e => setConnectConfig({ ...connectConfig, name: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="password"
              placeholder="API Key / Access Token"
              value={connectConfig.api_key}
              onChange={e => setConnectConfig({ ...connectConfig, api_key: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="url"
              placeholder="Webhook URL (optional)"
              value={connectConfig.webhook_url}
              onChange={e => setConnectConfig({ ...connectConfig, webhook_url: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
          </div>
          <div className="mt-4 flex gap-2">
            <button 
              onClick={handleConnect}
              className="text-xs px-3 py-1 rounded"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              Connect
            </button>
            <button 
              onClick={() => setShowConnect('')}
              style={{ color: 'var(--color-muted-foreground)' }}
            >
              Cancel
            </button>
          </div>
        </div>
      )}
    </div>
  );
}