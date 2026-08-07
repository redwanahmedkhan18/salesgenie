import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { WORKFLOW_SERVICE_URL } from '../../lib/api-client';

interface WorkflowDefinition {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  definition_json: Record<string, unknown>;
  trigger_type: string;
  is_active: boolean;
  version: number;
  created_at: string;
}

interface ExecutionLog {
  id: string;
  workflow_id: string;
  tenant_id: string;
  trigger_event: string;
  status: string;
  current_step: string | null;
  execution_time_ms: number | null;
  error_details: string | null;
  created_at: string;
}

export default function WorkflowBuilder() {
  const [activeRoute, setActiveRoute] = useState('workflows');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [workflows, setWorkflows] = useState<WorkflowDefinition[]>([]);
  const [executions, setExecutions] = useState<ExecutionLog[]>([]);
  const [loading, setLoading] = useState(true);
  const [query, setQuery] = useState('');
  const [selectedWorkflow, setSelectedWorkflow] = useState<WorkflowDefinition | null>(null);
  const [activeTab, setActiveTab] = useState<'workflows' | 'executions'>('workflows');

  interface WorkflowDefinitionExtended extends WorkflowDefinition {
    updated_at?: string;
  }
  
  interface ExecutionLogExtended extends ExecutionLog {
    duration_ms?: number;
    started_at?: string;
    error_message?: string | null;
  }

  const wfData = workflows as WorkflowDefinitionExtended[];
  const execData = executions as ExecutionLogExtended[];

  const workflowServiceUrl = WORKFLOW_SERVICE_URL;

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const [wfRes, execRes] = await Promise.all([
          fetch(`${workflowServiceUrl}/api/v1/workflows`, {
            headers: { 'Content-Type': 'application/json' },
          }),
          fetch(`${workflowServiceUrl}/api/v1/workflows/executions?size=50`, {
            headers: { 'Content-Type': 'application/json' },
          }),
        ]);

        if (wfRes.ok) {
          const data = await wfRes.json();
          setWorkflows(data.workflows || data);
        }
        if (execRes.ok) {
          const data = await execRes.json();
          setExecutions(data.executions || data);
        }
      } catch (error) {
        console.error('Error loading workflow data:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const filteredWorkflows = workflows.filter(wf => {
    if (query && !wf.name.toLowerCase().includes(query.toLowerCase()) &&
        !wf.description?.toLowerCase().includes(query.toLowerCase())) {
      return false;
    }
    return true;
  });

  const getStatusColor = (status: string) => {
    const colors: Record<string, string> = {
      pending: 'bg-gray-500/15 text-gray-400',
      running: 'bg-blue-500/15 text-blue-400',
      completed: 'bg-green-500/15 text-green-400',
      failed: 'bg-red-500/15 text-red-400',
      cancelled: 'bg-orange-500/15 text-orange-400',
    };
    return colors[status] || colors.pending;
  };

  const getTriggerTypeLabel = (type: string) => {
    const labels: Record<string, string> = {
      webhook: 'Webhook',
      schedule: 'Scheduled',
      event: 'Event',
      manual: 'Manual',
    };
    return labels[type] || type;
  };

  const formatDuration = (ms: number | null) => {
    if (!ms) return '-';
    if (ms < 1000) return `${ms}ms`;
    return `${(ms / 1000).toFixed(2)}s`;
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Workflow Builder
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Build and manage automated AI workflows
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
              onClick={() => setActiveTab('workflows')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'workflows' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'workflows' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'workflows' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Workflows ({workflows.length})
            </button>
            <button
              onClick={() => setActiveTab('executions')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'executions' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'executions' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'executions' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Executions ({executions.length})
            </button>
          </div>

          {activeTab === 'workflows' ? (
            <>
              {/* Search */}
              <div className="flex gap-3">
                <input
                  type="text"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Search workflows..."
                  className="flex-1 px-4 py-2.5 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
                <button
                  onClick={() => alert('New Workflow form would open here')}
                  className="px-4 py-2 text-sm font-semibold rounded-xl transition-all"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                >
                  + New Workflow
                </button>
              </div>

              {/* Workflows Table */}
              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="overflow-x-auto">
                  <table className="w-full">
                    <thead>
                      <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Name</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Slug</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Trigger</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Updated</th>
                      </tr>
                    </thead>
                    <tbody>
                      {loading ? (
                        <tr>
                          <td colSpan={5} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            Loading workflows...
                          </td>
                        </tr>
                      ) : filteredWorkflows.length === 0 ? (
                        <tr>
                          <td colSpan={5} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            No workflows found
                          </td>
                        </tr>
                      ) : (
                        filteredWorkflows.map((wf: WorkflowDefinitionExtended) => (
                          <tr key={wf.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                            <td className="px-4 py-3">
                              <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{wf.name}</div>
                              {wf.description && (
                                <div className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                                  {wf.description}
                                </div>
                              )}
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>{wf.slug}</td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                              {getTriggerTypeLabel(wf.trigger_type)}
                            </td>
                            <td className="px-4 py-3">
                              <span className={`text-xs px-2 py-1 rounded-full ${
                                wf.is_active
                                  ? 'bg-green-500/15 text-green-400'
                                  : 'bg-gray-500/15 text-gray-400'
                              }`}>
                                {wf.is_active ? 'Active' : 'Inactive'}
                              </span>
                            </td>
                            <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                              {wf.updated_at ? new Date(wf.updated_at).toLocaleDateString() : '-'}
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
            /* Executions Tab */
            <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Workflow</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Duration</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Started</th>
                      <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Error</th>
                    </tr>
                  </thead>
                  <tbody>
                    {loading ? (
                      <tr>
                        <td colSpan={5} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                          Loading executions...
                        </td>
                      </tr>
                    ) : executions.length === 0 ? (
                      <tr>
                        <td colSpan={5} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                          No executions found
                        </td>
                      </tr>
                    ) : (
                      executions.map(exec => {
                        const wf = workflows.find(w => w.id === exec.workflow_id);
                        return (
                          <tr key={exec.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                            <td className="px-4 py-3 text-sm font-medium" style={{ color: 'var(--color-foreground)' }}>
                              {wf?.name || exec.workflow_id.substring(0, 8)}
                            </td>
                            <td className="px-4 py-3">
                              <span className={`text-xs px-2 py-1 rounded-full ${getStatusColor(exec.status)}`}>
                                {exec.status}
                              </span>
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                              {formatDuration((exec as any).duration_ms ?? exec.execution_time_ms)}
                            </td>
                            <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                              {((exec as any).started_at ?? exec.created_at) ? new Date((exec as any).started_at ?? exec.created_at).toLocaleString() : '-'}
                            </td>
                            <td className="px-4 py-3 text-xs" style={{ color: '#cd4239' }}>
                              {((exec as any).error_message ?? exec.error_details) ? ((exec as any).error_message ?? exec.error_details)?.substring(0, 50) + '...' : '-'}
                            </td>
                          </tr>
                        );
                      })
                    )}
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </div>
      </main>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}
