import React, { useState, useEffect } from 'react';
import { useAuth } from '../../auth/AuthProvider';
import { apiClient } from '../../lib/api-client';
import type { SuperAdminUser, AuditEvent, SystemHealth, AIProviderStatus, PlatformSettings, SystemInfo } from '../../lib/types';

export default function SuperAdminRoutesPage() {
  const { user } = useAuth();
  const [users, setUsers] = useState<SuperAdminUser[]>([]);
  const [auditEvents, setAuditEvents] = useState<AuditEvent[]>([]);
  const [health, setHealth] = useState<SystemHealth[]>([]);
  const [aiProviders, setAiProviders] = useState<AIProviderStatus[]>([]);
  const [settings, setSettings] = useState<PlatformSettings | null>(null);
  const [systemInfo, setSystemInfo] = useState<SystemInfo | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'users' | 'audit' | 'health' | 'ai' | 'settings'>('users');
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    loadSuperAdminData();
  }, [activeTab, searchQuery]);

  const loadSuperAdminData = async () => {
    setLoading(true);
    try {
      const promises: Promise<any>[] = [];

      if (activeTab === 'users' || activeTab === 'audit') {
        promises.push(apiClient.fetchSuperAdminUsers(searchQuery));
      }

      if (activeTab === 'audit') {
        promises.push(apiClient.fetchAuditEvents());
      }

      if (activeTab === 'health') {
        promises.push(apiClient.fetchSystemHealth());
      }

      if (activeTab === 'ai') {
        promises.push(apiClient.fetchAIProviderStatus());
      }

      if (activeTab === 'settings') {
        promises.push(apiClient.fetchPlatformSettings());
        promises.push(apiClient.fetchSystemInfo());
      }

      const results = await Promise.all(promises);

      if (results[0]) setUsers(results[0]);
      if (results[1]) setAuditEvents(results[1]);
      if (results[2]) setHealth(results[2]);
      if (results[3]) setAiProviders(results[3]);
      if (results[4]) setSettings(results[4]);
      if (results[5]) setSystemInfo(results[5]);
    } catch (error) {
      console.error('Failed to load data:', error);
    } finally {
      setLoading(false);
    }
  };

  const getSeverityColor = (severity: string) => {
    switch (severity) {
      case 'low': return 'text-blue-400 bg-blue-500/10';
      case 'medium': return 'text-yellow-400 bg-yellow-500/10';
      case 'high': return 'text-orange-400 bg-orange-500/10';
      case 'critical': return 'text-red-400 bg-red-500/10';
      default: return 'text-gray-400 bg-gray-500/10';
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'healthy': return 'text-green-400';
      case 'degraded': return 'text-yellow-400';
      case 'down': return 'text-red-400';
      default: return 'text-gray-400';
    }
  };

  if (!settings && !health && !users && !auditEvents) {
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
          <h2 className="font-bold text-sm" style={{ color: 'var(--color-foreground)' }}>Super Admin</h2>
        </div>
        <nav className="flex-1 overflow-y-auto p-3 space-y-1">
          {[
            { id: 'users', label: 'Users' },
            { id: 'audit', label: 'Audit Logs' },
            { id: 'health', label: 'System Health' },
            { id: 'ai', label: 'AI Providers' },
            { id: 'settings', label: 'Platform Settings' },
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
              Super Admin Control Center
            </h1>
            <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
              Manage platform users, audit logs, and system configuration
            </p>
          </div>

          {/* Users Tab */}
          {activeTab === 'users' && (
            <div className="space-y-4">
              <div className="flex items-center gap-3">
                <input
                  type="text"
                  placeholder="Search users..."
                  value={searchQuery}
                  onChange={e => setSearchQuery(e.target.value)}
                  className="px-3 py-2 rounded border text-sm"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
                />
              </div>

              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <table className="w-full">
                  <thead>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Email</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Role</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Created</th>
                    </tr>
                  </thead>
                  <tbody>
                    {users.map(user => (
                      <tr key={user.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td className="px-4 py-3">
                          <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{user.email}</div>
                          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{user.full_name || '-'}</div>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>{user.role}</td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full ${user.is_active ? 'bg-green-500/15 text-green-400' : 'bg-red-500/15 text-red-400'}`}>
                            {user.is_active ? 'Active' : 'Inactive'}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          {new Date(user.created_at).toLocaleDateString()}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Audit Logs Tab */}
          {activeTab === 'audit' && (
            <div className="space-y-4">
              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <table className="w-full">
                  <thead>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Action</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Resource</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>User</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Severity</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Created</th>
                    </tr>
                  </thead>
                  <tbody>
                    {auditEvents.slice(0, 50).map(event => (
                      <tr key={event.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>{event.action}</td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                          {event.resource_type}#{event.resource_id || '-'}
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>{event.user_email || 'System'}</td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full ${getSeverityColor(event.severity)}`}>
                            {event.severity}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          {new Date(event.created_at).toLocaleString()}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* System Health Tab */}
          {activeTab === 'health' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {health.map(service => (
                <div key={service.service} className="p-4 rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <div className="flex items-center justify-between">
                    <div>
                      <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{service.service}</h3>
                      <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                        Response: {service.response_time_ms}ms
                      </div>
                    </div>
                    <span className={`text-sm font-bold ${getStatusColor(service.status)}`}>
                      {service.status.toUpperCase()}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* AI Providers Tab */}
          {activeTab === 'ai' && (
            <div className="space-y-4">
              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <table className="w-full">
                  <thead>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Provider</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Models</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Daily Usage</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Rate Limit</th>
                    </tr>
                  </thead>
                  <tbody>
                    {aiProviders.map(provider => (
                      <tr key={provider.name} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>{provider.name}</td>
                        <td className="px-4 py-3">
                          <span className={`text-xs font-bold ${getStatusColor(provider.status)}`}>
                            {provider.status.toUpperCase()}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>{provider.models.join(', ')}</td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                          ${provider.daily_used} / ${provider.daily_limit}
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                          {provider.rate_limit_remaining} remaining
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Settings Tab */}
          {activeTab === 'settings' && (
            <div className="space-y-4">
              <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h3 className="font-semibold text-sm mb-3" style={{ color: 'var(--color-foreground)' }}>System Information</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Version:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{systemInfo?.version || 'Loading...'}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Environment:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{systemInfo?.environment || 'Loading...'}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Python:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{systemInfo?.python_version || 'Loading...'}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Database:</span>
                    <span className="block" style={{ color: 'var(--color-foreground)' }}>{systemInfo?.database || 'Loading...'}</span>
                  </div>
                </div>
              </div>

              <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h3 className="font-semibold text-sm mb-3" style={{ color: 'var(--color-foreground)' }}>Platform Settings</h3>
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-sm" style={{ color: 'var(--color-foreground)' }}>Maintenance Mode</span>
                    <span className="text-xs px-2 py-1 rounded" style={{ background: (settings?.maintenance_mode ? 'var(--color-secondary)' : 'var(--color-green)'), color: 'var(--color-on-secondary)' }}>
                      {settings?.maintenance_mode ? 'ON' : 'OFF'}
                    </span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>AI Token Budget: ${settings?.ai_token_budget_usd || 0}</span>
                  </div>
                  <div>
                    <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                      Max API Requests/minute: {settings?.max_api_requests_per_minute || 100000}
                    </span>
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