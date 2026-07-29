import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';

interface AuditLog {
  id: string;
  event_type: string;
  severity: string;
  actor_id: string | null;
  actor_type: string;
  resource_type: string | null;
  resource_id: string | null;
  action: string;
  description: string;
  ip_address: string | null;
  request_id: string | null;
  metadata: Record<string, unknown> | null;
  is_compliance: boolean;
  tenant_id: string;
  created_at: string;
}

interface AuditOverview {
  total_events: number;
  events_today: number;
  events_by_severity: Record<string, number>;
  events_by_type: Record<string, number>;
  top_actors: Array<{ actor_id: string; count: number }>;
  compliance_events: number;
  security_alerts: number;
  retention_summary: Record<string, number>;
}

interface AuditSearchResponse {
  total_hits: number;
  hits: AuditLog[];
  took_ms: number;
}

const severityColors: Record<string, string> = {
  info: 'bg-blue-500/15 text-blue-400',
  warning: 'bg-yellow-500/15 text-yellow-400',
  error: 'bg-orange-500/15 text-orange-400',
  critical: 'bg-red-500/15 text-red-400',
};

const eventTypeLabels: Record<string, string> = {
  user_login: 'User Login',
  user_logout: 'User Logout',
  user_created: 'User Created',
  user_updated: 'User Updated',
  user_deleted: 'User Deleted',
  customer_created: 'Customer Created',
  customer_updated: 'Customer Updated',
  customer_deleted: 'Customer Deleted',
  ticket_created: 'Ticket Created',
  ticket_updated: 'Ticket Updated',
  ticket_assigned: 'Ticket Assigned',
  ticket_resolved: 'Ticket Resolved',
  document_indexed: 'Document Indexed',
  document_deleted: 'Document Deleted',
  api_call: 'API Call',
  system_event: 'System Event',
  data_export: 'Data Export',
  permission_granted: 'Permission Granted',
  permission_revoked: 'Permission Revoked',
  config_changed: 'Config Changed',
  security_alert: 'Security Alert',
  compliance_violation: 'Compliance Violation',
};

export default function AuditLogs() {
  const [activeRoute, setActiveRoute] = useState('audit');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [logs, setLogs] = useState<AuditLog[]>([]);
  const [overview, setOverview] = useState<AuditOverview | null>(null);
  const [loading, setLoading] = useState(true);
  const [totalHits, setTotalHits] = useState(0);
  const [tookMs, setTookMs] = useState(0);
  const [query, setQuery] = useState('');
  const [filterSeverity, setFilterSeverity] = useState<string | null>(null);
  const [filterEventType, setFilterEventType] = useState<string | null>(null);
  const [filterCompliance, setFilterCompliance] = useState<boolean | null>(null);
  const [activeTab, setActiveTab] = useState<'logs' | 'overview'>('logs');

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const [logsRes, overviewRes] = await Promise.all([
          fetch(`${import.meta.env.DEV ? 'http://localhost:8013' : '/api'}/audit/logs?size=50`, {
            headers: { 'Content-Type': 'application/json' },
          }),
          fetch(`${import.meta.env.DEV ? 'http://localhost:8013' : '/api'}/audit/overview`, {
            headers: { 'Content-Type': 'application/json' },
          }),
        ]);

        if (logsRes.ok) {
          const logsData: AuditSearchResponse = await logsRes.json();
          setLogs(logsData.hits);
          setTotalHits(logsData.total_hits);
          setTookMs(logsData.took_ms);
        }

        if (overviewRes.ok) {
          const overviewData: AuditOverview = await overviewRes.json();
          setOverview(overviewData);
        }
      } catch (error) {
        console.error('Error loading audit data:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    try {
      const params = new URLSearchParams();
      params.set('q', query);
      params.set('size', '50');
      if (filterSeverity) params.set('severities', filterSeverity);
      if (filterEventType) params.set('event_types', filterEventType);
      if (filterCompliance !== null) params.set('is_compliance', String(filterCompliance));

      const response = await fetch(
        `${import.meta.env.DEV ? 'http://localhost:8013' : '/api'}/audit/logs?${params.toString()}`,
        { headers: { 'Content-Type': 'application/json' } }
      );

      if (response.ok) {
        const data: AuditSearchResponse = await response.json();
        setLogs(data.hits);
        setTotalHits(data.total_hits);
        setTookMs(data.took_ms);
      }
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setLoading(false);
    }
  };

  const clearFilters = () => {
    setQuery('');
    setFilterSeverity(null);
    setFilterEventType(null);
    setFilterCompliance(null);
  };

  const getSeverityClass = (severity: string) => {
    return severityColors[severity] || severityColors.info;
  };

  const getEventTypeLabel = (type: string) => {
    return eventTypeLabels[type] || type.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Audit Logs
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Track user actions, system events, and compliance logs
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
              onClick={() => setActiveTab('logs')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'logs'
                  ? 'shadow'
                  : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'logs' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'logs' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Audit Logs
            </button>
            <button
              onClick={() => setActiveTab('overview')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'overview'
                  ? 'shadow'
                  : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'overview' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'overview' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Overview
            </button>
          </div>

          {activeTab === 'logs' ? (
            <>
              {/* Search & Filters */}
              <div className="flex flex-col sm:flex-row gap-3">
                <input
                  type="text"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Search audit logs..."
                  onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
                  className="flex-1 px-4 py-2.5 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
                <select
                  value={filterSeverity || ''}
                  onChange={(e) => setFilterSeverity(e.target.value || null)}
                  className="px-3 py-2 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                >
                  <option value="">All Severities</option>
                  <option value="info">Info</option>
                  <option value="warning">Warning</option>
                  <option value="error">Error</option>
                  <option value="critical">Critical</option>
                </select>
                <select
                  value={filterCompliance?.toString() || ''}
                  onChange={(e) => {
                    const val = e.target.value;
                    setFilterCompliance(val === '' ? null : val === 'true');
                  }}
                  className="px-3 py-2 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                >
                  <option value="">All Events</option>
                  <option value="true">Compliance Only</option>
                  <option value="false">Non-Compliance</option>
                </select>
                <button
                  onClick={handleSearch}
                  className="px-4 py-2 text-sm font-semibold rounded-xl transition-all"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                >
                  Search
                </button>
                <button
                  onClick={clearFilters}
                  className="px-4 py-2 text-sm rounded-xl transition-colors"
                  style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}
                >
                  Clear
                </button>
              </div>

              {/* Results Summary */}
              <div className="flex items-center justify-between text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                <span>{totalHits} results in {tookMs}ms</span>
              </div>

              {/* Logs Table */}
              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="overflow-x-auto">
                  <table className="w-full">
                    <thead>
                      <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Event</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Severity</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Actor</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Action</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Description</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Compliance</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Timestamp</th>
                      </tr>
                    </thead>
                    <tbody>
                      {loading ? (
                        <tr>
                          <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            Loading audit logs...
                          </td>
                        </tr>
                      ) : logs.length === 0 ? (
                        <tr>
                          <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            No audit logs found
                          </td>
                        </tr>
                      ) : (
                        logs.map(log => (
                          <tr key={log.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                            <td className="px-4 py-3">
                              <span className="text-sm font-medium" style={{ color: 'var(--color-foreground)' }}>
                                {getEventTypeLabel(log.event_type)}
                              </span>
                            </td>
                            <td className="px-4 py-3">
                              <span className={`text-xs px-2 py-1 rounded-full ${getSeverityClass(log.severity)}`}>
                                {log.severity}
                              </span>
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                              {log.actor_id || 'System'}
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                              {log.action}
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                              {log.description.substring(0, 60)}...
                            </td>
                            <td className="px-4 py-3">
                              {log.is_compliance && (
                                <span className="text-xs px-2 py-1 rounded-full bg-purple-500/15 text-purple-400">
                                  Compliance
                                </span>
                              )}
                            </td>
                            <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                              {new Date(log.created_at).toLocaleString()}
                            </td>
                          </tr>
                        ))
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </>
          ) : (
            /* Overview Tab */
            overview && (
              <div className="space-y-6">
                {/* Summary Cards */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                  <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Events</div>
                    <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>{overview.total_events.toLocaleString()}</div>
                  </div>
                  <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Today</div>
                    <div className="text-2xl font-bold" style={{ color: '#2c84e0' }}>{overview.events_today}</div>
                  </div>
                  <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Compliance Events</div>
                    <div className="text-2xl font-bold" style={{ color: '#7c44a6' }}>{overview.compliance_events}</div>
                  </div>
                  <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Security Alerts</div>
                    <div className="text-2xl font-bold" style={{ color: '#cd4239' }}>{overview.security_alerts}</div>
                  </div>
                </div>

                {/* Events by Severity */}
                <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Events by Severity</h3>
                  <div className="space-y-2">
                    {Object.entries(overview.events_by_severity).map(([severity, count]) => (
                      <div key={severity} className="flex items-center gap-3">
                        <span className="w-20 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{severity}</span>
                        <div className="flex-1 h-2 rounded" style={{ background: 'var(--color-muted)' }}>
                          <div
                            className="h-2 rounded"
                            style={{
                              width: `${(count / overview.total_events) * 100}%`,
                              background: severity === 'info' ? '#2c84e0' :
                                         severity === 'warning' ? '#f7a501' :
                                         severity === 'error' ? '#cd4239' :
                                         severity === 'critical' ? '#dc2626' : '#2c84e0',
                            }}
                          />
                        </div>
                        <span className="text-sm" style={{ color: 'var(--color-foreground)' }}>{count}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Events by Type */}
                <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Events by Type</h3>
                  <div className="space-y-2">
                    {Object.entries(overview.events_by_type)
                      .sort((a, b) => b[1] - a[1])
                      .slice(0, 10)
                      .map(([type, count]) => (
                        <div key={type} className="flex items-center gap-3">
                          <span className="w-48 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                            {getEventTypeLabel(type)}
                          </span>
                          <div className="flex-1 h-2 rounded" style={{ background: 'var(--color-muted)' }}>
                            <div
                              className="h-2 rounded"
                              style={{
                                width: `${(count / overview.total_events) * 100}%`,
                                background: 'var(--color-primary)',
                              }}
                            />
                          </div>
                          <span className="text-sm" style={{ color: 'var(--color-foreground)' }}>{count}</span>
                        </div>
                      ))}
                  </div>
                </div>

                {/* Top Actors */}
                <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Top Actors</h3>
                  <div className="space-y-2">
                    {overview.top_actors.map((actor, i) => (
                      <div key={actor.actor_id || `actor-${i}`} className="flex items-center justify-between">
                        <span className="text-sm" style={{ color: 'var(--color-foreground)' }}>
                          {actor.actor_id || 'System'}
                        </span>
                        <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          {actor.count} actions
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )
          )}
        </div>
      </main>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}