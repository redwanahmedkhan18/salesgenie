import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';

interface Organization {
  id: string;
  name: string;
  slug: string;
  domain: string | null;
  subscription_tier: string;
  max_seats: number;
  max_monthly_tokens: number;
  is_active: boolean;
  created_at: string;
}

interface Branding {
  tenant_id: string;
  primary_color: string;
  secondary_color: string;
  logo_url: string | null;
  favicon_url: string | null;
  custom_domain: string | null;
  is_white_label_enabled: boolean;
}

interface Subscription {
  id: string;
  stripe_customer_id: string;
  stripe_subscription_id: string | null;
  plan_tier: string;
  status: string;
  current_period_start: string;
  current_period_end: string;
  cancel_at_period_end: boolean;
  created_at: string;
}

interface User {
  id: string;
  email: string;
  full_name: string;
  phone_number: string | null;
  job_title: string | null;
  department: string | null;
  is_active: boolean;
  created_at: string;
}

export default function SettingsAdmin() {
  const [activeRoute, setActiveRoute] = useState('settings');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [organization, setOrganization] = useState<Organization | null>(null);
  const [branding, setBranding] = useState<Branding | null>(null);
  const [subscription, setSubscription] = useState<Subscription | null>(null);
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'organization' | 'branding' | 'billing' | 'users'>('organization');

  const orgServiceUrl = import.meta.env.DEV ? 'http://localhost:8003' : '/api';
  const userServiceUrl = import.meta.env.DEV ? 'http://localhost:8002' : '/api';
  const billingServiceUrl = import.meta.env.DEV ? 'http://localhost:8004' : '/api';

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const [orgRes, brandingRes, billingRes, usersRes] = await Promise.all([
          fetch(`${orgServiceUrl}/organizations`, { headers: { 'Content-Type': 'application/json' } }),
          fetch(`${orgServiceUrl}/organizations/branding`, { headers: { 'Content-Type': 'application/json' } }),
          fetch(`${billingServiceUrl}/billing/subscriptions`, { headers: { 'Content-Type': 'application/json' } }),
          fetch(`${userServiceUrl}/users`, { headers: { 'Content-Type': 'application/json' } }),
        ]);

        if (orgRes.ok) {
          const orgData = await orgRes.json();
          setOrganization(orgData[0] || orgData);
        }
        if (brandingRes.ok) {
          const brandingData = await brandingRes.json();
          setBranding(brandingData[0] || brandingData);
        }
        if (billingRes.ok) {
          const billingData = await billingRes.json();
          setSubscription(billingData[0] || billingData);
        }
        if (usersRes.ok) {
          const usersData = await usersRes.json();
          setUsers(usersData);
        }
      } catch (error) {
        console.error('Error loading settings data:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
    });
  };

  const formatBytes = (bytes: number) => {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Settings & Administration
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Manage organization, branding, billing, and users
            </p>
          </div>
          <button
            id="open-command-palette-btn"
            onClick={() => setPaletteOpen(true)}
            className="flex items-center gap-2 px-3 py-2 rounded-lg text-sm transition-colors"
            style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)', border: '1px solid var(--color-border)' }}
          >
            <span>🔍</span>
            <span>Search</span>
            <kbd className="text-xs">⌘K</kbd>
          </button>
        </header>

        <div className="px-6 py-6 space-y-6">
          {/* Tabs */}
          <div className="flex gap-1 p-1 rounded-lg" style={{ background: 'var(--color-muted)' }}>
            <button
              onClick={() => setActiveTab('organization')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'organization' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'organization' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'organization' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Organization
            </button>
            <button
              onClick={() => setActiveTab('branding')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'branding' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'branding' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'branding' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Branding
            </button>
            <button
              onClick={() => setActiveTab('billing')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'billing' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'billing' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'billing' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Billing
            </button>
            <button
              onClick={() => setActiveTab('users')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'users' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'users' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'users' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Users ({users.length})
            </button>
          </div>

          {activeTab === 'organization' && organization && (
            <div className="space-y-6">
              <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h2 className="text-lg font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>Organization Details</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Name
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{organization.name}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Slug
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{organization.slug}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Domain
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{organization.domain || 'Not set'}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Subscription Tier
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{organization.subscription_tier}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Max Seats
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{organization.max_seats}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Max Monthly Tokens
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{formatBytes(organization.max_monthly_tokens)}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Status
                    </label>
                    <span className={`text-xs px-2 py-1 rounded-full ${
                      organization.is_active
                        ? 'bg-green-500/15 text-green-400'
                        : 'bg-red-500/15 text-red-400'
                    }`}>
                      {organization.is_active ? 'Active' : 'Inactive'}
                    </span>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Created
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{formatDate(organization.created_at)}</div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'branding' && branding && (
            <div className="space-y-6">
              <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h2 className="text-lg font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>Branding Settings</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Primary Color
                    </label>
                    <div className="flex items-center gap-2">
                      <div
                        className="w-6 h-6 rounded"
                        style={{ background: branding.primary_color }}
                      />
                      <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{branding.primary_color}</div>
                    </div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Secondary Color
                    </label>
                    <div className="flex items-center gap-2">
                      <div
                        className="w-6 h-6 rounded"
                        style={{ background: branding.secondary_color }}
                      />
                      <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{branding.secondary_color}</div>
                    </div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Logo URL
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{branding.logo_url || 'Not set'}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Favicon URL
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{branding.favicon_url || 'Not set'}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Custom Domain
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{branding.custom_domain || 'Not set'}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      White-label
                    </label>
                    <span className={`text-xs px-2 py-1 rounded-full ${
                      branding.is_white_label_enabled
                        ? 'bg-green-500/15 text-green-400'
                        : 'bg-gray-500/15 text-gray-400'
                    }`}>
                      {branding.is_white_label_enabled ? 'Enabled' : 'Disabled'}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'billing' && subscription && (
            <div className="space-y-6">
              <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h2 className="text-lg font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>Subscription Details</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Plan Tier
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{subscription.plan_tier}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Status
                    </label>
                    <span className={`text-xs px-2 py-1 rounded-full ${
                      subscription.status === 'active'
                        ? 'bg-green-500/15 text-green-400'
                        : 'bg-red-500/15 text-red-400'
                    }`}>
                      {subscription.status}
                    </span>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Current Period Start
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{formatDate(subscription.current_period_start)}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Current Period End
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{formatDate(subscription.current_period_end)}</div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Cancel at Period End
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>
                      {subscription.cancel_at_period_end ? 'Yes' : 'No'}
                    </div>
                  </div>
                  <div>
                    <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      Stripe Customer ID
                    </label>
                    <div className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>{subscription.stripe_customer_id}</div>
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'users' && (
            <div className="space-y-6">
              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="overflow-x-auto">
                  <table className="w-full">
                    <thead>
                      <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Name</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Email</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Phone</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Job Title</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Department</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Created</th>
                      </tr>
                    </thead>
                    <tbody>
                      {loading ? (
                        <tr>
                          <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            Loading users...
                          </td>
                        </tr>
                      ) : users.length === 0 ? (
                        <tr>
                          <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            No users found
                          </td>
                        </tr>
                      ) : (
                        users.map(user => (
                          <tr key={user.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                            <td className="px-4 py-3 text-sm font-medium" style={{ color: 'var(--color-foreground)' }}>{user.full_name}</td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>{user.email}</td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>{user.phone_number || '-'}</td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>{user.job_title || '-'}</td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>{user.department || '-'}</td>
                            <td className="px-4 py-3">
                              <span className={`text-xs px-2 py-1 rounded-full ${
                                user.is_active
                                  ? 'bg-green-500/15 text-green-400'
                                  : 'bg-red-500/15 text-red-400'
                              }`}>
                                {user.is_active ? 'Active' : 'Inactive'}
                              </span>
                            </td>
                            <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                              {formatDate(user.created_at)}
                            </td>
                          </tr>
                        ))
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}
