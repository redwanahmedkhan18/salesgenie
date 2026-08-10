import React, { useState, useEffect } from 'react';
import { useAuth } from '../../auth/AuthProvider';
import { apiClient } from '../../lib/api-client';
import type {
  WorkspaceMember,
  WorkspaceUsageMetrics,
  Branding,
  WorkspaceUser,
  Organization,
} from '../../lib/types';

const ROLES: { value: string; label: string }[] = [
  { value: 'end_user', label: 'End User' },
  { value: 'sales_agent', label: 'Sales Agent' },
  { value: 'sales_manager', label: 'Sales Manager' },
  { value: 'support_agent', label: 'Support Agent' },
  { value: 'support_manager', label: 'Support Manager' },
  { value: 'knowledge_manager', label: 'Knowledge Manager' },
  { value: 'org_admin', label: 'Org Admin' },
];

export default function OrgAdminDashboard() {
  const { user } = useAuth();
  const [workspace, setWorkspace] = useState<Organization | null>(null);
  const [members, setMembers] = useState<WorkspaceMember[]>([]);
  const [workspaceUsers, setWorkspaceUsers] = useState<WorkspaceUser[]>([]);
  const [usage, setUsage] = useState<WorkspaceUsageMetrics | null>(null);
  const [branding, setBranding] = useState<Branding | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<
    'overview' | 'users' | 'members' | 'branding' | 'billing'
  >('overview');

  useEffect(() => {
    loadData();
  }, [activeTab]);

  const loadData = async () => {
    setLoading(true);
    try {
      const promises: Promise<any>[] = [];
      let wsResult, membersResult, usersResult, usageResult, brandingResult;

      promises.push(apiClient.getOrgAdminWorkspace());
      promises.push(apiClient.getOrgAdminMembers());
      promises.push(apiClient.getWorkspaceUsers());
      promises.push(apiClient.getOrgAdminWorkspaceUsage());
      promises.push(apiClient.getOrgAdminBranding());

      [wsResult, membersResult, usersResult, usageResult, brandingResult] =
        await Promise.all(promises);

      if (wsResult) setWorkspace(wsResult);
      if (membersResult) setMembers(membersResult);
      if (usersResult) setWorkspaceUsers((usersResult as any).users || []);
      if (usageResult) setUsage(usageResult);
      if (brandingResult) setBranding(brandingResult);
    } catch (error) {
      console.error('Failed to load org admin data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSuspendMember = async (memberId: string) => {
    if (!window.confirm('Suspend this member?')) return;
    await apiClient.suspendOrgAdminMember(memberId);
    loadData();
  };

  const handleRoleChange = async (userId: string, newRole: string) => {
    const member = members.find(m => m.user_id === userId);
    if (!member) return;
    const result = await apiClient.updateOrgAdminMemberRole(member.id, newRole);
    if (result) {
      setWorkspaceUsers(workspaceUsers.map(u =>
        u.id === userId ? { ...u, role: result.role } : u
      ));
    }
  };

  const handleUpdateBranding = async (updates: any) => {
    await apiClient.updateOrgAdminBranding(updates);
    loadData();
  };

  const formatTokens = (value: number) => {
    if (value >= 1000000) return `${(value / 1000000).toFixed(1)}M`;
    if (value >= 1000) return `${(value / 1000).toFixed(1)}K`;
    return value.toString();
  };

  if (loading && !workspace) {
    return (
      <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
        <div className="flex-1 overflow-y-auto p-6">
          <div className="text-center py-8">Loading organization admin panel...</div>
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
          <h2 className="font-bold text-sm" style={{ color: 'var(--color-foreground)' }}>Organization Admin</h2>
        </div>
        <nav className="flex-1 overflow-y-auto p-3 space-y-1">
          {[
            { id: 'overview', label: 'Overview', icon: '📊' },
            { id: 'users', label: 'Workspace Users', icon: '👥' },
            { id: 'members', label: 'Member Access', icon: '🔑' },
            { id: 'branding', label: 'Branding', icon: '🎨' },
            { id: 'billing', label: 'Billing', icon: '💳' },
          ].map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              className={`w-full text-left flex items-center gap-3 px-3 py-2 text-sm rounded-lg transition-colors ${
                activeTab === tab.id ? 'bg-secondary/10' : 'hover:bg-secondary/5'
              }`}
              style={{ color: 'var(--color-foreground)' }}
            >
              <span>{tab.icon}</span>
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
              Organization Administration
            </h1>
            <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Hello, {user?.email || 'Admin'} — Manage workspace settings, members, and branding
            </p>
          </div>

          {/* Overview Tab */}
          {activeTab === 'overview' && usage && (
            <div className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Conversations</div>
                  <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-foreground)' }}>{usage.total_conversations.toLocaleString()}</div>
                </div>
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Cost (Today)</div>
                  <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-foreground)' }}>${usage.ai_cost_usd.toFixed(2)}</div>
                </div>
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Accuracy</div>
                  <div className="text-2xl font-bold text-green-400 mt-1">{usage.ai_accuracy_rate.toFixed(1)}%</div>
                </div>
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active Conversations</div>
                  <div className="text-2xl font-bold text-blue-400 mt-1">{usage.active_conversations}</div>
                </div>
              </div>

              <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h3 className="font-semibold text-sm mb-3" style={{ color: 'var(--color-foreground)' }}>Workspace: {workspace?.name}</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Subscription Tier:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{workspace?.subscription_tier}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Max Seats:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{workspace?.max_seats}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Max Monthly Tokens:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{formatTokens(workspace?.max_monthly_tokens || 0)}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Token Utilization:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{usage.token_utilization_pct?.toFixed(1)}%</span>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Users Tab */}
          {activeTab === 'users' && (
            <div className="space-y-4">
              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <table className="w-full">
                  <thead>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Name</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Email</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Role</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Joined</th>
                    </tr>
                  </thead>
                  <tbody>
                    {workspaceUsers.map(u => (
                      <tr key={u.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td className="px-4 py-3">
                          <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{u.full_name || '-'}</div>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>{u.email}</td>
                        <td className="px-4 py-3">
                          <select
                            value={u.role}
                            onChange={(e) => handleRoleChange(u.id, e.target.value)}
                            className="text-xs px-2 py-1 rounded border"
                            style={{ background: 'var(--color-input)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
                          >
                            {ROLES.map(r => (
                              <option key={r.value} value={r.value}>{r.label}</option>
                            ))}
                          </select>
                        </td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full ${u.is_active ? 'bg-green-500/15 text-green-400' : 'bg-red-500/15 text-red-400'}`}>
                            {u.is_active ? 'Active' : 'Inactive'}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{new Date(u.created_at).toLocaleDateString()}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Members Tab */}
          {activeTab === 'members' && (
            <div className="space-y-4">
              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <table className="w-full">
                  <thead>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>User ID</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Role</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Created</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {members.map(m => (
                      <tr key={m.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>{m.user_id}</td>
                        <td className="px-4 py-3">
                          <span className="text-xs px-2 py-1 rounded" style={{ background: 'rgba(247,165,1,0.15)', color: '#f7a501' }}>{m.role}</span>
                        </td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full ${m.status === 'active' ? 'bg-green-500/15 text-green-400' : 'bg-red-500/15 text-red-400'}`}>
                            {m.status}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{new Date(m.created_at).toLocaleDateString()}</td>
                        <td className="px-4 py-3">
                          {m.status === 'active' && (
                            <button
                              onClick={() => handleSuspendMember(m.id)}
                              className="text-xs px-3 py-1 rounded border"
                              style={{ borderColor: '#ef4444', color: '#ef4444' }}
                            >
                              Suspend
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

          {/* Branding Tab */}
          {activeTab === 'branding' && branding && (
            <div className="space-y-4">
              <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h3 className="font-semibold text-sm mb-4" style={{ color: 'var(--color-foreground)' }}>Workspace Branding</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Primary Color</label>
                    <div className="flex items-center gap-2 mt-1">
                      <input
                        type="text"
                        defaultValue={branding.primary_color}
                        onChange={e => handleUpdateBranding({ primary_color: e.target.value })}
                        className="flex-1 px-3 py-2 rounded text-sm"
                        style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                      />
                      <div className="w-8 h-8 rounded border" style={{ background: branding.primary_color }} />
                    </div>
                  </div>
                  <div>
                    <label className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Secondary Color</label>
                    <div className="flex items-center gap-2 mt-1">
                      <input
                        type="text"
                        defaultValue={branding.secondary_color}
                        onChange={e => handleUpdateBranding({ secondary_color: e.target.value })}
                        className="flex-1 px-3 py-2 rounded text-sm"
                        style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                      />
                      <div className="w-8 h-8 rounded border" style={{ background: branding.secondary_color }} />
                    </div>
                  </div>
                  <div>
                    <label className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Logo URL</label>
                    <input
                      type="text"
                      defaultValue={branding.logo_url || ''}
                      onChange={e => handleUpdateBranding({ logo_url: e.target.value || null })}
                      className="w-full px-3 py-2 rounded text-sm mt-1"
                      style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                    />
                  </div>
                  <div>
                    <label className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Custom Domain</label>
                    <input
                      type="text"
                      defaultValue={branding.custom_domain || ''}
                      onChange={e => handleUpdateBranding({ custom_domain: e.target.value || null })}
                      className="w-full px-3 py-2 rounded text-sm mt-1"
                      style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                    />
                  </div>
                </div>
                <button
                  onClick={() => handleUpdateBranding({ is_white_label_enabled: !branding.is_white_label_enabled })}
                  className={`mt-4 text-xs px-3 py-1 rounded border ${
                    branding.is_white_label_enabled ? 'bg-green-500/15 text-green-400 border-green-500/30' : 'text-muted'
                  }`}
                  style={{ color: 'var(--color-foreground)' }}
                >
                  White-label: {branding.is_white_label_enabled ? 'ON' : 'OFF'}
                </button>
              </div>
            </div>
          )}

          {/* Billing Tab */}
          {activeTab === 'billing' && (
            <div className="space-y-4">
              <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h3 className="font-semibold text-sm mb-3" style={{ color: 'var(--color-foreground)' }}>Subscription & Usage</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Plan:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{workspace?.subscription_tier}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Billing Period:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{new Date().toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active Users:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{workspaceUsers.length}/{workspace?.max_seats}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Tokens Used:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{formatTokens(usage?.total_tokens_used || 0)} / {formatTokens(workspace?.max_monthly_tokens || 0)}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Cost:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>${usage?.ai_cost_usd.toFixed(2)}</span>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
