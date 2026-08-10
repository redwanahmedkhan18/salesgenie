import { useState, useEffect } from 'react';
import { useAuth } from '../../auth/AuthProvider';
import { apiClient } from '../../lib/api-client';
import type {
  WorkspaceMember,
  WorkspaceUsageMetrics,
  Branding,
  BillingOverview,
} from '../../lib/types';

export default function WorkspaceAdminDashboard() {
  const { user } = useAuth();
  const [workspace, setWorkspace] = useState<any>(null);
  const [members, setMembers] = useState<WorkspaceMember[]>([]);
  const [usage, setUsage] = useState<WorkspaceUsageMetrics | null>(null);
  const [branding, setBranding] = useState<Branding | null>(null);
  const [billing, setBilling] = useState<BillingOverview | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<
    'overview' | 'usage' | 'members' | 'branding' | 'billing'
  >('overview');

  useEffect(() => {
    loadData();
  }, [activeTab]);

  const loadData = async () => {
    setLoading(true);
    try {
      const promises: Promise<any>[] = [];
      let wsResult, membersResult, usageResult, brandingResult, billingResult;

      promises.push(apiClient.getWorkspaceAdminWorkspace());
      promises.push(apiClient.getWorkspaceAdminMembers());
      promises.push(apiClient.getWorkspaceAdminUsage());
      promises.push(apiClient.getWorkspaceAdminBranding());
      promises.push(apiClient.getWorkspaceAdminBilling());

      [wsResult, membersResult, usageResult, brandingResult, billingResult] =
        await Promise.all(promises);

      if (wsResult) setWorkspace(wsResult);
      if (membersResult) setMembers(membersResult);
      if (usageResult) setUsage(usageResult);
      if (brandingResult) setBranding(brandingResult);
      if (billingResult) setBilling(billingResult);
    } catch (error) {
      console.error('Failed to load workspace admin data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSuspendMember = async (memberId: string) => {
    if (!window.confirm('Suspend this member?')) return;
    await apiClient.suspendWorkspaceAdminMember(memberId);
    loadData();
  };

  const handleUpdateBranding = async (updates: any) => {
    await apiClient.updateWorkspaceAdminBranding(updates);
    loadData();
  };

  const formatTokens = (value: number) => {
    if (value >= 1000000) return `${(value / 1000000).toFixed(1)}M`;
    if (value >= 1000) return `${(value / 1000).toFixed(1)}K`;
    return value.toString();
  };

  const getRoleColor = (role: string) => {
    const roleColors: Record<string, string> = {
      workspace_admin: 'rgba(132,204,255,0.15)',
      org_admin: 'rgba(251,146,60,0.15)',
      sales_manager: 'rgba(132,204,255,0.15)',
      sales_agent: 'rgba(74,222,128,0.15)',
      support_manager: 'rgba(132,204,255,0.15)',
      support_agent: 'rgba(74,222,128,0.15)',
      knowledge_manager: 'rgba(168,85,247,0.15)',
      auditor: 'rgba(251,146,60,0.15)',
      end_user: 'rgba(149,151,167,0.15)',
      super_admin: 'rgba(252,211,30,0.15)',
    };
    const colors = {
      text: {
        workspace_admin: '#87ceeb',
        org_admin: '#fb923c',
        sales_manager: '#87ceeb',
        sales_agent: '#4ade80',
        support_manager: '#87ceeb',
        support_agent: '#4ade80',
        knowledge_manager: '#a855f7',
        auditor: '#fb923c',
        end_user: '#9593eb',
        super_admin: '#fcd34d',
      }
    };
    return {
      bg: roleColors[role] || roleColors.end_user,
      text: colors.text[role as keyof typeof colors.text] || '#9593eb',
    };
  };

  if (loading && !workspace) {
    return (
      <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
        <div className="flex-1 overflow-y-auto p-6">
          <div className="text-center py-8">Loading workspace admin panel...</div>
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
          <h2 className="font-bold text-sm" style={{ color: 'var(--color-foreground)' }}>Workspace Admin</h2>
        </div>
        <nav className="flex-1 overflow-y-auto p-3 space-y-1">
          {[
            { id: 'overview', label: 'Overview', icon: '📊' },
            { id: 'usage', label: 'Usage Stats', icon: '📈' },
            { id: 'members', label: 'Team Members', icon: '👥' },
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
              Workspace Administration
            </h1>
            <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Hello, {user?.email || 'Admin'} — Manage your workspace, team, and billing
            </p>
          </div>

          {/* Overview Tab */}
          {activeTab === 'overview' && workspace && usage && (
            <div className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Subscription</div>
                  <div className="text-xl font-bold mt-1" style={{ color: 'var(--color-foreground)' }}>{workspace.subscription_tier}</div>
                </div>
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Team Members</div>
                  <div className="text-xl font-bold text-blue-400 mt-1">{members.length}/{workspace.max_seats}</div>
                </div>
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Cost (Today)</div>
                  <div className="text-xl font-bold text-green-400 mt-1">${usage.ai_cost_usd.toFixed(2)}</div>
                </div>
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active Conversations</div>
                  <div className="text-xl font-bold text-orange-400 mt-1">{usage.active_conversations}</div>
                </div>
              </div>

              <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h3 className="font-semibold text-sm mb-3" style={{ color: 'var(--color-foreground)' }}>Workspace: {workspace.name}</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Domain:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{workspace.domain || 'Not set'}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Created:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{new Date(workspace.created_at).toLocaleDateString()}</span>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Usage Tab */}
          {activeTab === 'usage' && usage && (
            <div className="space-y-4">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Tokens Used</div>
                  <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-foreground)' }}>{formatTokens(usage.total_tokens_used)}</div>
                </div>
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Cost</div>
                  <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-foreground)' }}>${usage.ai_cost_usd.toFixed(2)}</div>
                </div>
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Accuracy</div>
                  <div className="text-2xl font-bold text-green-400 mt-1">{usage.ai_accuracy_rate.toFixed(1)}%</div>
                </div>
                <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Hallucination Rate</div>
                  <div className="text-2xl font-bold text-red-400 mt-1">{usage.hallucination_rate.toFixed(1)}%</div>
                </div>
              </div>

              {usage.token_utilization_pct !== undefined && (
                <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm" style={{ color: 'var(--color-foreground)' }}>Token Utilization</span>
                    <span className="text-sm font-bold" style={{ color: 'var(--color-foreground)' }}>{usage.token_utilization_pct.toFixed(1)}%</span>
                  </div>
                  <div className="w-full bg-gray-700/30 rounded-full h-2">
                    <div
                      className="h-2 rounded-full"
                      style={{
                        background: 'var(--color-primary)',
                        width: `${Math.min(usage.token_utilization_pct, 100)}%`,
                      }}
                    />
                  </div>
                </div>
              )}

              {usage.seat_utilization_pct !== undefined && (
                <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm" style={{ color: 'var(--color-foreground)' }}>Seat Utilization</span>
                    <span className="text-sm font-bold" style={{ color: 'var(--color-foreground)' }}>{usage.seat_utilization_pct.toFixed(1)}%</span>
                  </div>
                  <div className="w-full bg-gray-700/30 rounded-full h-2">
                    <div
                      className="h-2 rounded-full"
                      style={{
                        background: 'var(--color-primary)',
                        width: `${Math.min(usage.seat_utilization_pct, 100)}%`,
                      }}
                    />
                  </div>
                </div>
              )}
            </div>
          )}

          {/* Members Tab */}
          {activeTab === 'members' && (
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Team Members ({members.length})</h3>
              </div>
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
                    {members.map(m => {
                      const roleStyle = getRoleColor(m.role);
                      return (
                        <tr key={m.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                          <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>{m.user_id}</td>
                          <td className="px-4 py-3">
                            <span className="text-xs px-2 py-1 rounded-full" style={{ background: roleStyle.bg, color: roleStyle.text }}>{m.role}</span>
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
                      );
                    })}
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
              </div>
            </div>
          )}

          {/* Billing Tab */}
          {activeTab === 'billing' && billing && (
            <div className="space-y-4">
              <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h3 className="font-semibold text-sm mb-3" style={{ color: 'var(--color-foreground)' }}>Subscription & Billing</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Workspace:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{billing.workspace_name}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Plan:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{billing.subscription_tier}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Billing Period:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{billing.current_billing_period}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active Seats:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{billing.tokens_used ? 'In use' : 'Ready'}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Tokens Used:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{formatTokens(billing.tokens_used)} / {formatTokens(billing.max_monthly_tokens)}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Cost:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>${billing.ai_cost_usd.toFixed(2)}</span>
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
