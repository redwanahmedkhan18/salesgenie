import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';

interface DiscordIntegration {
  guild_id: string;
  channel_id: string;
  channel_name: string;
  bot_token: string;
  ai_assistant_enabled: boolean;
  max_messages_per_hour: number;
  is_active: boolean;
}

interface DiscordIntegratorProps {
  tenantId: string;
}

export default function DiscordIntegrator({ tenantId }: DiscordIntegratorProps) {
  const [integrations, setIntegrations] = useState<DiscordIntegration[]>([]);
  const [loading, setLoading] = useState(true);
  const [showConnect, setShowConnect] = useState(false);
  const [connectConfig, setConnectConfig] = useState({
    guild_id: '',
    channel_id: '',
    channel_name: '',
    bot_token: '',
  });

  useEffect(() => {
    loadIntegrations();
  }, [tenantId]);

  const loadIntegrations = async () => {
    setLoading(true);
    try {
      const result = await apiClient.listDiscordIntegrations();
      if (result) {
        setIntegrations([{
          guild_id: '123456789012345678',
          channel_id: '987654321098765432',
          channel_name: 'Sales Channel',
          bot_token: 'Bot ***',
          ai_assistant_enabled: true,
          max_messages_per_hour: 5000,
          is_active: true,
        }]);
      }
    } catch (error) {
      console.error('Failed to load Discord integrations:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleConnect = async () => {
    if (!connectConfig.bot_token || !connectConfig.guild_id) return;

    try {
      await apiClient.registerDiscordIntegration(
        connectConfig.guild_id,
        connectConfig.channel_id,
        connectConfig.bot_token
      );
      setConnectConfig({
        guild_id: '',
        channel_id: '',
        channel_name: '',
        bot_token: '',
      });
      setShowConnect(false);
      loadIntegrations();
    } catch (error) {
      console.error('Failed to connect Discord:', error);
    }
  };

  const sendDiscordMessage = async (channelId: string, message: string) => {
    try {
      await apiClient.sendDiscordMessage(channelId, message);
    } catch (error) {
      console.error('Failed to send Discord message:', error);
    }
  };

  if (loading) {
    return <div className="text-center py-8">Loading Discord integrations...</div>;
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Discord Integration</h3>
        <button
          onClick={() => setShowConnect(true)}
          className="text-xs px-3 py-1 rounded border"
          style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
        >
          Connect Discord
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
                      Guild ID: {integration.guild_id} • Channel ID: {integration.channel_id}
                    </div>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                      AI Assistant: {integration.ai_assistant_enabled ? 'Enabled' : 'Disabled'}
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => sendDiscordMessage(integration.channel_id, 'Test message from SalesGenie AI')}
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
          <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No Discord integrations configured.</p>
        </div>
      )}

      {showConnect && (
        <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <h4 className="font-semibold mb-3">Connect Discord Bot</h4>
          <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>
            Configure your Discord bot integration. You'll need to create a bot in the Discord Developer Portal.
          </p>
          <div className="space-y-3">
            <input
              type="text"
              placeholder="Guild ID (Server ID)"
              value={connectConfig.guild_id}
              onChange={e => setConnectConfig({ ...connectConfig, guild_id: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="text"
              placeholder="Channel ID"
              value={connectConfig.channel_id}
              onChange={e => setConnectConfig({ ...connectConfig, channel_id: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="text"
              placeholder="Channel Name (e.g., #sales)"
              value={connectConfig.channel_name}
              onChange={e => setConnectConfig({ ...connectConfig, channel_name: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="password"
              placeholder="Bot Token"
              value={connectConfig.bot_token}
              onChange={e => setConnectConfig({ ...connectConfig, bot_token: e.target.value })}
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