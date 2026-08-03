import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';

interface SlackIntegration {
  channel_id: string;
  channel_name: string;
  bot_token: string;
  signing_secret: string;
  ai_assistant_enabled: boolean;
  max_messages_per_hour: number;
  is_active: boolean;
}

interface SlackIntegratorProps {
  tenantId: string;
}

export default function SlackIntegrator({ tenantId }: SlackIntegratorProps) {
  const [integrations, setIntegrations] = useState<SlackIntegration[]>([]);
  const [loading, setLoading] = useState(true);
  const [showConnect, setShowConnect] = useState(false);
  const [connectConfig, setConnectConfig] = useState({
    channel_id: '',
    channel_name: '',
    bot_token: '',
    signing_secret: '',
  });

  useEffect(() => {
    loadIntegrations();
  }, [tenantId]);

  const loadIntegrations = async () => {
    setLoading(true);
    try {
      const result = await apiClient.listSlackIntegrations();
      if (result) {
        setIntegrations([{
          channel_id: 'C1234567890',
          channel_name: '#sales-notifications',
          bot_token: 'xoxb-***',
          signing_secret: '***',
          ai_assistant_enabled: true,
          max_messages_per_hour: 1000,
          is_active: true,
        }]);
      }
    } catch (error) {
      console.error('Failed to load Slack integrations:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleConnect = async () => {
    if (!connectConfig.bot_token || !connectConfig.signing_secret) return;

    try {
      await apiClient.registerSlackIntegration(
        connectConfig.channel_id,
        connectConfig.bot_token,
        connectConfig.signing_secret
      );
      setConnectConfig({
        channel_id: '',
        channel_name: '',
        bot_token: '',
        signing_secret: '',
      });
      setShowConnect(false);
      loadIntegrations();
    } catch (error) {
      console.error('Failed to connect Slack:', error);
    }
  };

  const sendSlackMessage = async (channelId: string, message: string) => {
    try {
      await apiClient.sendSlackMessage(channelId, message);
    } catch (error) {
      console.error('Failed to send Slack message:', error);
    }
  };

  if (loading) {
    return <div className="text-center py-8">Loading Slack integrations...</div>;
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Slack Integration</h3>
        <button
          onClick={() => setShowConnect(true)}
          className="text-xs px-3 py-1 rounded border"
          style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
        >
          Connect Slack
        </button>
      </div>

      {integrations.length > 0 ? (
        <div className="space-y-3">
          {integrations.map(integration => (
            <div key={integration.channel_id} className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <span className="text-2xl">💬</span>
                  <div>
                    <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{integration.channel_name}</div>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                      Channel ID: {integration.channel_id} • {integration.is_active ? 'Active' : 'Inactive'}
                    </div>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                      AI Assistant: {integration.ai_assistant_enabled ? 'Enabled' : 'Disabled'}
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => sendSlackMessage(integration.channel_id, 'Test message from SalesGenie')}
                  className="text-xs px-2 py-1 rounded"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                >
                  Send Test
                </button>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No Slack integrations configured.</p>
        </div>
      )}

      {showConnect && (
        <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <h4 className="font-semibold mb-3">Connect Slack Workspace</h4>
          <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>
            Configure your Slack bot integration. You'll need to create a Slack App with appropriate permissions.
          </p>
          <div className="space-y-3">
            <input
              type="text"
              placeholder="Channel ID (e.g., C1234567890)"
              value={connectConfig.channel_id}
              onChange={e => setConnectConfig({ ...connectConfig, channel_id: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="text"
              placeholder="Channel Name (e.g., #sales-notifications)"
              value={connectConfig.channel_name}
              onChange={e => setConnectConfig({ ...connectConfig, channel_name: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="password"
              placeholder="Bot Token (xoxb-...)"
              value={connectConfig.bot_token}
              onChange={e => setConnectConfig({ ...connectConfig, bot_token: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="password"
              placeholder="Signing Secret"
              value={connectConfig.signing_secret}
              onChange={e => setConnectConfig({ ...connectConfig, signing_secret: e.target.value })}
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
              onClick={() => setShowConnect(false)}
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