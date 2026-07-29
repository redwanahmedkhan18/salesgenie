import React, { useState, useEffect } from 'react';
import { useAuth } from '../../../auth/AuthProvider';
import { apiClient } from '../../../lib/api-client';

interface WhatsAppAccountLocal {
  id: string;
  name: string;
  phone_number_id: string;
  display_name?: string;
  is_active: boolean;
  verified: boolean;
  webhook_url?: string;
  last_sync?: string;
}

const CHANNEL_ICONS: Record<string, string> = {
  whatsapp: '💬',
  email: '✉️',
  telegram: '✈️',
  messenger: '💬',
  instagram: '📸',
  slack: '💜',
  teams: '🟦',
  discord: '🎮',
  sms: '📱',
  website: '🌐',
};

const CHANNEL_COLORS: Record<string, string> = {
  whatsapp: '#25D369',
  email: '#34A853',
  telegram: '#0088CC',
  messenger: '#1877F2',
  instagram: '#E4405F',
  slack: '#611F69',
  teams: '#6264A7',
  discord: '#5865F2',
  sms: '#25D369',
  website: '#4285F4',
};

export function ChannelManagement() {
  const { hasRole, hasAnyRole } = useAuth();
  const [accounts, setAccounts] = useState<WhatsAppAccountLocal[]>([]);
  const [loading, setLoading] = useState(true);
  const [showConnectModal, setShowConnectModal] = useState(false);
  const [newAccount, setNewAccount] = useState({
    name: '',
    phone_number_id: '',
    access_token: '',
    webhook_url: '',
  });

  useEffect(() => {
    loadAccounts();
  }, []);

  const loadAccounts = async () => {
    setLoading(true);
    try {
      const response = await apiClient.getWhatsAppAccounts();
      if (response) {
        setAccounts([response]);
      }
    } catch (error) {
      console.error('Failed to load accounts:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleConnect = async () => {
    if (!newAccount.name || !newAccount.phone_number_id || !newAccount.access_token) return;
    
    try {
      await apiClient.createWhatsAppAccount({
        name: newAccount.name,
        phone_number_id: newAccount.phone_number_id,
        access_token: newAccount.access_token,
        webhook_url: newAccount.webhook_url || undefined,
      });
      setShowConnectModal(false);
      setNewAccount({ name: '', phone_number_id: '', access_token: '', webhook_url: '' });
      await loadAccounts();
    } catch (error) {
      console.error('Failed to connect account:', error);
    }
  };

  const handleVerifyWebhook = async (accountId: string) => {
    // In a real implementation, this would trigger webhook verification
    alert(`Webhook verification initiated for account ${accountId}`);
  };

  if (!hasAnyRole(['org_admin', 'super_admin', 'workspace_admin', 'knowledge_manager'])) {
    return (
      <div className="flex items-center justify-center min-h-screen" style={{ background: 'var(--color-background)' }}>
        <div className="text-center p-8 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-4xl mb-4">🔒</div>
          <h2 className="text-xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>Access Denied</h2>
          <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
            You don't have permission to access channel settings.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Channel Management</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
            Configure and manage communication channels
          </p>
        </div>
        <button
          onClick={() => setShowConnectModal(true)}
          className="px-4 py-2 rounded-xl font-semibold text-sm transition-all"
          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
        >
          + Connect Channel
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {loading ? (
          Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="skeleton h-4 w-full rounded mb-2" />
              <div className="skeleton h-3 w-3/4 rounded mb-2" />
              <div className="skeleton h-3 w-1/2 rounded" />
            </div>
          ))
        ) : accounts.length === 0 ? (
          <div className="col-span-full text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
            <div className="text-3xl mb-4">📡</div>
            <p>No channels connected yet</p>
          </div>
        ) : (
          accounts.map(account => (
            <div key={account.id} className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="flex items-start justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center text-2xl"
                    style={{ background: `${CHANNEL_COLORS.whatsapp}20`, color: CHANNEL_COLORS.whatsapp }}>
                    {CHANNEL_ICONS.whatsapp}
                  </div>
                  <div>
                    <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{account.name}</h3>
                    <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                      {account.display_name || account.phone_number_id}
                    </p>
                    <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                      Last sync: {account.last_sync ? new Date(account.last_sync).toLocaleString() : 'Never'}
                    </p>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <span className={`text-xs px-2 py-0.5 rounded-full ${account.verified ? 'bg-green-500/15 text-green-400' : 'bg-yellow-500/15 text-yellow-400'}`}>
                    {account.verified ? '✓ Verified' : '⚠ Unverified'}
                  </span>
                  <span className={`text-xs px-2 py-0.5 rounded-full ${account.is_active ? 'bg-green-500/15 text-green-400' : 'bg-gray-500/15 text-gray-400'}`}>
                    {account.is_active ? '● Active' : '● Inactive'}
                  </span>
                </div>
              </div>
              <div className="flex gap-2 mt-4">
                <button
                  onClick={() => handleVerifyWebhook(account.id)}
                  className="flex-1 text-xs px-3 py-1.5 rounded border transition-colors"
                  style={{ borderColor: 'var(--color-border)', color: 'var(--color-muted-foreground)' }}
                >
                  Verify Webhook
                </button>
                <button
                  className="flex-1 text-xs px-3 py-1.5 rounded border transition-colors"
                  style={{ borderColor: 'var(--color-border)', color: 'var(--color-muted-foreground)' }}
                >
                  View Stats
                </button>
              </div>
            </div>
          ))
        )}
      </div>

      {/* Connect Modal */}
      {showConnectModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="rounded-2xl p-6 w-full max-w-md" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <h2 className="text-xl font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Connect WhatsApp Business</h2>
            <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>
              Enter your WhatsApp Business API credentials to connect this channel.
            </p>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  Account Name
                </label>
                <input
                  type="text"
                  value={newAccount.name}
                  onChange={e => setNewAccount({ ...newAccount, name: e.target.value })}
                  placeholder="My Support Line"
                  className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  Phone Number ID
                </label>
                <input
                  type="text"
                  value={newAccount.phone_number_id}
                  onChange={e => setNewAccount({ ...newAccount, phone_number_id: e.target.value })}
                  placeholder="123456789012345"
                  className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  Access Token
                </label>
                <input
                  type="password"
                  value={newAccount.access_token}
                  onChange={e => setNewAccount({ ...newAccount, access_token: e.target.value })}
                  placeholder="EAA...Z"
                  className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  Webhook URL (optional)
                </label>
                <input
                  type="url"
                  value={newAccount.webhook_url}
                  onChange={e => setNewAccount({ ...newAccount, webhook_url: e.target.value })}
                  placeholder="https://yourapp.com/api/whatsapp/webhook"
                  className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
            </div>
            <div className="flex gap-3 mt-6">
              <button
                onClick={() => setShowConnectModal(false)}
                className="flex-1 px-4 py-2.5 rounded-xl font-semibold text-sm transition-colors"
                style={{ background: 'var(--color-muted)', color: 'var(--color-foreground)' }}
              >
                Cancel
              </button>
              <button
                onClick={handleConnect}
                disabled={!newAccount.name || !newAccount.phone_number_id || !newAccount.access_token}
                className="flex-1 px-4 py-2.5 rounded-xl font-semibold text-sm transition-all disabled:opacity-60"
                style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
              >
                Connect
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}