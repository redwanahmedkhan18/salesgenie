import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';
import type { ChannelIntegration, WhatsAppAccount } from '../../lib/types';

interface ChannelIntegratorProps {
  tenantId: string;
}

export default function ChannelIntegrator({ tenantId }: ChannelIntegratorProps) {
  const [channels, setChannels] = useState<ChannelIntegration[]>([]);
  const [whatsappAccounts, setWhatsAppAccounts] = useState<WhatsAppAccount[]>([]);
  const [loading, setLoading] = useState(true);
  const [showConnect, setShowConnect] = useState('');
  const [connectConfig, setConnectConfig] = useState({
    name: '',
    phone_number_id: '',
    access_token: '',
    webhook_url: '',
  });

  useEffect(() => {
    loadData();
  }, [tenantId]);

  const loadData = async () => {
    setLoading(true);
    try {
      const [channelsRes, waRes] = await Promise.all([
        apiClient.listChannelIntegrations(),
        apiClient.getWhatsAppAccounts(),
      ]);
      setChannels(channelsRes || []);
      setWhatsAppAccounts(waRes ? [waRes] : []);
    } catch (error) {
      console.error('Failed to load channel data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleConnectWhatsApp = async () => {
    if (!connectConfig.phone_number_id || !connectConfig.access_token) return;
    
    try {
      await apiClient.createWhatsAppAccount(connectConfig);
      setConnectConfig({ name: '', phone_number_id: '', access_token: '', webhook_url: '' });
      setShowConnect('');
      loadData();
    } catch (error) {
      console.error('Failed to connect WhatsApp:', error);
    }
  };

  const sendWhatsAppMessage = async (to: string, message: string) => {
    try {
      await apiClient.sendWhatsAppMessage({ to, message });
    } catch (error) {
      console.error('Failed to send WhatsApp message:', error);
    }
  };

  if (loading) {
    return <div className="text-center py-8">Loading channel integrations...</div>;
  }

  const channelTypes = [
    { id: 'whatsapp', label: 'WhatsApp', icon: '💬', description: 'Facebook Messenger Integration' },
    { id: 'telegram', label: 'Telegram', icon: '✈️', description: 'Telegram Bot Integration' },
    { id: 'facebook', label: 'Facebook', icon: '📘', description: 'Facebook Messenger' },
    { id: 'email', label: 'Email', icon: '📧', description: 'SMTP/IMAP Integration' },
    { id: 'sms', label: 'SMS', icon: '📱', description: 'Twilio SMS Gateway' },
    { id: 'website', label: 'Website', icon: '🌐', description: 'Live Chat Widget' },
  ];

  return (
    <div className="space-y-4">
      <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Omnichannel Setup</h3>

      <div className="grid gap-4">
        {channelTypes.map(channel => (
          <div key={channel.id} className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <span className="text-2xl">{channel.icon}</span>
                <div>
                  <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{channel.label}</div>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{channel.description}</div>
                </div>
              </div>
              <button
                onClick={() => setShowConnect(channel.id)}
                className="text-xs px-3 py-1 rounded border"
                style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
              >
                Connect
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* WhatsApp Configuration Modal */}
      {showConnect === 'whatsapp' && (
        <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <h4 className="font-semibold mb-3">Connect WhatsApp</h4>
          <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>
            Configure your Facebook Business WhatsApp account. You'll need a Facebook Business account with WhatsApp Business API.
          </p>
          <div className="space-y-3">
            <input
              type="text"
              placeholder="Account Name"
              value={connectConfig.name}
              onChange={e => setConnectConfig({ ...connectConfig, name: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="text"
              placeholder="Phone Number ID"
              value={connectConfig.phone_number_id}
              onChange={e => setConnectConfig({ ...connectConfig, phone_number_id: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="password"
              placeholder="Access Token"
              value={connectConfig.access_token}
              onChange={e => setConnectConfig({ ...connectConfig, access_token: e.target.value })}
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
              onClick={handleConnectWhatsApp}
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

      {/* Configured Channels */}
      <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="p-4 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <h4 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Connected Channels</h4>
        </div>
        <div className="p-4 space-y-3">
          {whatsappAccounts.length > 0 ? (
            whatsappAccounts.map(account => (
              <div key={account.id} className="p-3 rounded" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <span className="text-2xl">💬</span>
                    <div>
                      <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{account.name}</div>
                      <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                        Phone ID: {account.phone_number_id} • {account.is_active ? 'Active' : 'Inactive'}
                      </div>
                    </div>
                  </div>
                  <button
                    onClick={() => console.log('Send WhatsApp test message')}
                    className="text-xs px-2 py-1 rounded border"
                    style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
                  >
                    Send Test
                  </button>
                </div>
              </div>
            ))
          ) : (
            <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No channels connected yet.</p>
          )}
        </div>
      </div>
    </div>
  );
}