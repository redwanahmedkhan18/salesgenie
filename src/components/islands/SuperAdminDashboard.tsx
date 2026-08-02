import React, { useState, useEffect } from 'react';
import { useAuth } from '../../auth/AuthProvider';
import { apiClient } from '../../lib/api-client';
import type { PlatformMetrics as PlatformMetricsType, OrganizationListItem as OrganizationListItemType, OrganizationDetail as OrganizationDetailType } from '../../lib/types';

interface PlatformMetricsLocal {
  total_organizations: number;
  active_organizations: number;
  suspended_organizations: number;
  total_users: number;
  total_tokens_used: number;
  ai_cost_usd: number;
  platform_uptime_percent: number;
}

export default function SuperAdminDashboard() {
  const { user } = useAuth();
  const [metrics, setMetrics] = useState<PlatformMetricsLocal | null>(null);
  const [organizations, setOrganizations] = useState<OrganizationListItemType[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'overview' | 'organizations' | 'billing' | 'ai'>('overview');
  const [statusFilter, setStatusFilter] = useState<'all' | 'active' | 'suspended'>('all');

  useEffect(() => {
    loadData();
  }, [statusFilter]);

  const loadData = async () => {
    setLoading(true);
    try {
      const [metricsRes, orgsRes] = await Promise.all([
        apiClient.fetchPlatformMetrics(),
        apiClient.fetchOrganizations(statusFilter === 'all' ? undefined : statusFilter),
      ]);
      
      if (metricsRes) setMetrics(metricsRes);
      if (orgsRes) setOrganizations(orgsRes);
    } catch (error) {
      console.error('Failed to load data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSuspendOrg = async (orgId: string) => {
    if (window.confirm('Are you sure you want to suspend this organization?')) {
      await apiClient.suspendOrganization(orgId);
      loadData();
    }
  };

  const handleResumeOrg = async (orgId: string) => {
    if (window.confirm('Are you sure you want to resume this organization?')) {
      await apiClient.resumeOrganization(orgId);
      loadData();
    }
  };

  const formatCurrency = (value: number) => {
    return `$${value.toLocaleString(undefined, { maximumFractionDigits: 0 })}`;
  };

  const formatTokens = (value: number) => {
    if (value >= 1000000) return `${(value / 1000000).toFixed(1)}M`;
    if (value >= 1000) return `${(value / 1000).toFixed(1)}K`;
    return value.toString();
  };

  if (!metrics) {
    return (
      <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
        <div className="flex-1 overflow-y-auto p-6">
          <div className="text-center py-8">Loading platform data...</div>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      {/* Sidebar */}
      <div className="w-64 flex-shrink-0 border-r flex flex-col" 
        style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="px-4 py-3 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <h2 className="font-bold text-sm" style={{ color: 'var(--color-foreground)' }}>Platform Admin</h2>
        </div>
        <nav className="flex-1 overflow-y-auto p-3 space-y-1">
          {[
            { id: 'overview', label: 'Overview' },
            { id: 'organizations', label: 'Organizations' },
            { id: 'billing', label: 'Billing' },
            { id: 'ai', label: 'AI Providers' },
          ].map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              className={`w-full text-left px-3 py-2 text-sm rounded-lg transition-colors ${
                activeTab === tab.id ? 'bg-secondary/10' : 'hover:bg-secondary/5'
              }`}
              style={{ color: 'var(--color-foreground)' }}
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </div>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto">
        <div className="p-6 space-y-6">
          <div>
            <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Platform Administration
            </h1>
            <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
              Hello, {user?.email || 'Admin'} - Managing global platform settings
            </p>
          </div>

          {activeTab === 'overview' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Organizations</div>
                <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>{metrics.total_organizations}</div>
              </div>
              <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active</div>
                <div className="text-2xl font-bold text-green-500">{metrics.active_organizations}</div>
              </div>
              <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Users</div>
                <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>{metrics.total_users.toLocaleString()}</div>
              </div>
              <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Cost</div>
                <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>{formatCurrency(metrics.ai_cost_usd)}</div>
              </div>
            </div>
          )}

          {activeTab === 'organizations' && (
            <div className="space-y-4">
              <div className="flex items-center gap-3">
                <select
                  value={statusFilter}
                  onChange={e => setStatusFilter(e.target.value as any)}
                  className="px-3 py-2 rounded border text-sm"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
                >
                  <option value="all">All Organizations</option>
                  <option value="active">Active</option>
                  <option value="suspended">Suspended</option>
                </select>
              </div>

              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <table className="w-full">
                  <thead>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Name</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Plan</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Created</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {organizations.map(org => (
                      <tr key={org.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td className="px-4 py-3">
                          <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{org.name}</div>
                          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{org.slug}</div>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>{org.subscription_tier}</td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full ${org.is_active ? 'bg-green-500/15 text-green-400' : 'bg-red-500/15 text-red-400'}`}>
                            {org.is_active ? 'Active' : 'Suspended'}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          {new Date(org.created_at).toLocaleDateString()}
                        </td>
                        <td className="px-4 py-3">
                          {org.is_active ? (
                            <button
                              onClick={() => handleSuspendOrg(org.id)}
                              className="text-xs px-3 py-1 rounded border"
                              style={{ borderColor: '#f59e0b', color: '#f59e0b' }}
                            >
                              Suspend
                            </button>
                          ) : (
                            <button
                              onClick={() => handleResumeOrg(org.id)}
                              className="text-xs px-3 py-1 rounded border"
                              style={{ borderColor: '#10b981', color: '#10b981' }}
                            >
                              Resume
                            </button>
                          )}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {activeTab === 'ai' && (
            <div className="space-y-4">
              <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h3 className="font-semibold text-sm mb-3" style={{ color: 'var(--color-foreground)' }}>AI Providers</h3>
                <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                  Configure global AI model access for all organizations.
                </p>
                <div className="mt-4 grid grid-cols-1 md:grid-cols-3 gap-4">
                  {['Groq', 'Google AI', 'Mistral'].map(provider => (
                    <div key={provider} className="p-3 rounded border" style={{ borderColor: 'var(--color-border)' }}>
                      <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{provider}</div>
                      <button className="mt-2 text-xs px-2 py-1 rounded"
                        style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                        Configure
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}