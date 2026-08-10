import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';
import type { MCPTool, MCPToolRegistration, MCPExecutionLog, MCPToolStats } from '../../lib/types';
import { Plug, Settings, Play, BarChart3, History, RefreshCw, Trash2, Check, X } from 'lucide-react';

function MCPToolsList({
  tools,
  onToolClick,
  onToolDelete,
  onRefresh,
  loading,
}: {
  tools: MCPTool[];
  onToolClick: (tool: MCPTool) => void;
  onToolDelete: (tool: MCPTool) => void;
  onRefresh: () => void;
  loading: boolean;
}) {
  if (loading) {
    return (
      <div className="p-6">
        <div className="space-y-3">
          {[...Array(5)].map((_, i) => (
            <div key={i} className="border rounded-lg p-4" style={{ borderColor: 'var(--color-border)' }}>
              <div className="h-5 w-3/4 bg-gray-200 dark:bg-gray-700 rounded animate-pulse mb-2"></div>
              <div className="h-4 w-1/2 bg-gray-200 dark:bg-gray-700 rounded animate-pulse"></div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-semibold">MCP Tools</h2>
        <div className="flex gap-2">
          <button
            onClick={onRefresh}
            className="px-3 py-1 text-sm rounded border"
            style={{ borderColor: 'var(--color-border)' }}
          >
            <RefreshCw className="w-4 h-4 inline mr-1" />
            Refresh
          </button>
          <button
            onClick={() => {}}
            className="px-3 py-1 text-sm rounded"
            style={{ background: 'var(--color-primary)', color: 'white' }}
          >
            <Settings className="w-4 h-4 inline mr-1" />
            Register Tool
          </button>
        </div>
      </div>

      {tools.length === 0 ? (
        <div className="text-center py-12" style={{ color: 'var(--color-muted-foreground)' }}>
          <Plug className="w-12 h-12 mx-auto mb-3 opacity-30" />
          <p>No MCP tools registered yet.</p>
          <p className="text-sm">Register tools to extend SalesGenie's capabilities.</p>
        </div>
      ) : (
        <div className="space-y-3">
          {tools.map((tool) => (
            <MCPToolCard key={tool.id} tool={tool} onClick={() => onToolClick(tool)} onDelete={onToolDelete} />
          ))}
        </div>
      )}
    </div>
  );
}

function MCPToolCard({
  tool,
  onClick,
  onDelete,
}: {
  tool: MCPTool;
  onClick: () => void;
  onDelete: (tool: MCPTool) => void;
}) {
  const categoryColors: Record<string, { bg: string; color: string }> = {
    search: { bg: '#dbeafe', color: '#1e40af' },
    research: { bg: '#dcfce7', color: '#166534' },
    crm: { bg: '#ddd6fe', color: '#5b21b6' },
    communication: { bg: '#fed7aa', color: '#9a3412' },
    data_enrichment: { bg: '#d1fae5', color: '#065f44' },
    analytics: { bg: '#fbbf24', color: '#92400e' },
    database: { bg: '#a5b4fc', color: '#312e81' },
    file: { bg: '#fecaca', color: '#991b2b' },
    webhook: { bg: '#e5e7eb', color: '#374151' },
    custom: { bg: '#f3e8ff', color: '#7b2cbf' },
  };

  const color = categoryColors[tool.category] || { bg: '#f1f5f9', color: '#475569' };

  return (
    <div
      className="border rounded-lg p-4 cursor-pointer transition-all hover:shadow-sm"
      style={{
        background: 'var(--color-card)',
        borderColor: 'var(--color-border)',
      }}
      onClick={onClick}
    >
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <div className="flex items-center gap-2">
            <h3 className="font-semibold">{tool.name}</h3>
            <span
              className="text-xs px-2 py-0.5 rounded"
              style={{ background: color.bg, color: color.color }}
            >
              {tool.category}
            </span>
            {!tool.enabled && (
              <span className="text-xs px-2 py-0.5 rounded" style={{ background: '#fee2e2', color: '#991b2b' }}>
                Disabled
              </span>
            )}
          </div>
          <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>{tool.description}</p>
          <div className="flex items-center gap-4 mt-2 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
            <span>Server: {tool.server_name}</span>
            <span>•</span>
            <span>Runs: {tool.execution_count}</span>
            <span>•</span>
            <span>Errors: {tool.total_errors}</span>
            {tool.avg_latency_ms > 0 && (
              <>
                <span>•</span>
                <span>Avg: {tool.avg_latency_ms}ms</span>
              </>
            )}
          </div>
        </div>
        <button
          onClick={(e) => {
            e.stopPropagation();
            onDelete(tool);
          }}
          className="text-xs px-2 py-1 rounded hover:opacity-80"
          style={{ color: 'var(--color-destructive, #dc2626)' }}
        >
          <Trash2 className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}

function MCPToolForm({
  tool,
  onSubmit,
  onCancel,
}: {
  tool?: MCPTool;
  onSubmit: (data: MCPToolRegistration) => Promise<void>;
  onCancel: () => void;
}) {
  const [formData, setFormData] = useState<MCPToolRegistration>({
    name: tool?.name || '',
    description: tool?.description || '',
    category: tool?.category || 'custom',
    server_url: tool?.server_url || '',
    server_name: tool?.server_name || '',
    visibility: tool?.visibility || 'tenant',
    required_roles: tool?.required_roles || [],
    required_permissions: tool?.required_permissions || [],
    timeout_seconds: tool?.timeout_seconds || 30,
    enabled: tool?.enabled !== false,
  });

  const handleChange = (field: keyof MCPToolRegistration, value: any) => {
    setFormData({ ...formData, [field]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await onSubmit(formData);
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="border rounded-lg p-6 w-full max-w-3xl" style={{ background: 'var(--color-card)' }}>
        <h2 className="text-xl font-semibold mb-4">{tool ? 'Edit MCP Tool' : 'Register MCP Tool'}</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium mb-1">Tool Name *</label>
              <input
                type="text"
                value={formData.name}
                onChange={(e) => handleChange('name', e.target.value)}
                className="w-full px-3 py-2 border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                placeholder="e.g., web_search"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Server Name *</label>
              <input
                type="text"
                value={formData.server_name}
                onChange={(e) => handleChange('server_name', e.target.value)}
                className="w-full px-3 py-2 border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                placeholder="e.g., web-search-server"
                required
              />
            </div>
            <div className="md:col-span-2">
              <label className="block text-sm font-medium mb-1">Server URL *</label>
              <input
                type="url"
                value={formData.server_url}
                onChange={(e) => handleChange('server_url', e.target.value)}
                className="w-full px-3 py-2 border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                placeholder="http://localhost:9000/sse"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Category</label>
              <select
                value={formData.category}
                onChange={(e) => handleChange('category', e.target.value)}
                className="w-full px-3 py-2 border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              >
                <option value="search">Search</option>
                <option value="research">Research</option>
                <option value="crm">CRM</option>
                <option value="communication">Communication</option>
                <option value="data_enrichment">Data Enrichment</option>
                <option value="analytics">Analytics</option>
                <option value="database">Database</option>
                <option value="file">File</option>
                <option value="webhook">Webhook</option>
                <option value="custom">Custom</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Visibility</label>
              <select
                value={formData.visibility}
                onChange={(e) => handleChange('visibility', e.target.value)}
                className="w-full px-3 py-2 border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              >
                <option value="public">Public</option>
                <option value="tenant">Tenant</option>
                <option value="role">Role-based</option>
                <option value="private">Private</option>
              </select>
            </div>
            <div className="md:col-span-2">
              <label className="block text-sm font-medium mb-1">Description</label>
              <textarea
                value={formData.description}
                onChange={(e) => handleChange('description', e.target.value)}
                className="w-full px-3 py-2 border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                rows={2}
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">API Key</label>
              <input
                type="password"
                value={formData.api_key || ''}
                onChange={(e) => handleChange('api_key', e.target.value || undefined)}
                className="w-full px-3 py-2 border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Timeout (seconds)</label>
              <input
                type="number"
                min="1"
                max="300"
                value={formData.timeout_seconds}
                onChange={(e) => handleChange('timeout_seconds', parseInt(e.target.value))}
                className="w-full px-3 py-2 border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              />
            </div>
            <div className="flex items-center gap-2">
              <input
                type="checkbox"
                id="enabled"
                checked={formData.enabled}
                onChange={(e) => handleChange('enabled', e.target.checked)}
              />
              <label htmlFor="enabled" className="text-sm font-medium">Enable this tool</label>
            </div>
          </div>
          <div className="flex gap-3">
            <button type="submit" className="px-4 py-2 text-sm font-medium rounded" style={{ background: 'var(--color-primary)', color: 'white' }}>
              {tool ? 'Update' : 'Register'}
            </button>
            <button type="button" onClick={onCancel} className="px-4 py-2 text-sm font-medium rounded" style={{ background: 'var(--color-secondary-bg, #f1f5f9)' }}>
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

function MCPToolDetail({
  tool,
  onClose,
  onEdit,
  logs,
  stats,
}: {
  tool: MCPTool;
  onClose: () => void;
  onEdit: () => void;
  logs: MCPExecutionLog[];
  stats: MCPToolStats | null;
}) {
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="border rounded-lg w-full max-w-4xl" style={{ background: 'var(--color-card)' }}>
        <div className="p-6 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-xl font-semibold">{tool.name}</h2>
              <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>{tool.description}</p>
            </div>
            <div className="flex gap-2">
              <button onClick={onEdit} className="px-3 py-1 text-sm rounded border" style={{ borderColor: 'var(--color-border)' }}>
                Edit
              </button>
              <button onClick={onClose} className="px-3 py-1 text-sm rounded border" style={{ borderColor: 'var(--color-border)' }}>
                <X className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
        <div className="p-6 overflow-y-auto max-h-[70vh]">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
              <h3 className="font-medium text-sm mb-2">Tool Info</h3>
              <div className="space-y-2 text-sm">
                <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Category:</span> {tool.category}</div>
                <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Server:</span> {tool.server_name}</div>
                <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>URL:</span> {tool.server_url}</div>
                <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Visibility:</span> {tool.visibility}</div>
                <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Timeout:</span> {tool.timeout_seconds}s</div>
                <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Status:</span> {tool.status}</div>
                <div className="flex items-center gap-2">
                  <span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Enabled:</span>
                  {tool.enabled ? <Check className="w-4 h-4 text-green-500" /> : <X className="w-4 h-4 text-red-500" />}
                </div>
              </div>
            </div>
            <div>
              <h3 className="font-medium text-sm mb-2">Execution Stats</h3>
              {stats ? (
                <div className="space-y-2 text-sm">
                  <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Executions:</span> {stats.execution_count}</div>
                  <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Success Rate:</span> {stats.success_rate}%</div>
                  <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Avg Latency:</span> {stats.avg_latency_ms}ms</div>
                  <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>P99 Latency:</span> {stats.p99_latency_ms}ms</div>
                  <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Errors:</span> {stats.error_count}</div>
                  {stats.last_used_at && (
                    <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Last Used:</span> {new Date(stats.last_used_at).toLocaleString()}</div>
                  )}
                  {stats.most_common_error && (
                    <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Common Error:</span> {stats.most_common_error}</div>
                  )}
                </div>
              ) : (
                <p style={{ color: 'var(--color-muted-foreground)' }}>No stats available</p>
              )}
            </div>
            <div>
              <h3 className="font-medium text-sm mb-2">Permissions</h3>
              <div className="space-y-2 text-sm">
                {tool.required_roles && tool.required_roles.length > 0 && (
                  <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Roles:</span> {tool.required_roles.join(', ')}</div>
                )}
                {tool.required_permissions && tool.required_permissions.length > 0 && (
                  <div><span className="font-medium" style={{ color: 'var(--color-muted-foreground)' }}>Permissions:</span> {tool.required_permissions.join(', ')}</div>
                )}
                {!tool.required_roles?.length && !tool.required_permissions?.length && (
                  <p style={{ color: 'var(--color-muted-foreground)' }}>No restrictions</p>
                )}
              </div>
            </div>
          </div>

          <div className="mt-6">
            <h3 className="font-medium text-sm mb-2">Recent Executions ({logs.length})</h3>
            {logs.length === 0 ? (
              <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No executions yet</p>
            ) : (
              <div className="space-y-2">
                {logs.slice(0, 10).map((log) => (
                  <div key={log.id} className="text-xs border rounded p-2" style={{ borderColor: 'var(--color-border)' }}>
                    <div className="flex items-center gap-2">
                      {log.success ? <Check className="w-3 h-3 text-green-500" /> : <X className="w-3 h-3 text-red-500" />}
                      <span>{new Date(log.created_at).toLocaleString()}</span>
                      <span>• {log.latency_ms}ms</span>
                      {!log.success && log.error_message && (
                        <span style={{ color: 'var(--color-destructive, #dc2626)' }}>{log.error_message.slice(0, 60)}...</span>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default function MCPToolsApp() {
  const [tools, setTools] = useState<MCPTool[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [editingTool, setEditingTool] = useState<MCPTool | null>(null);
  const [selectedTool, setSelectedTool] = useState<MCPTool | null>(null);
  const [selectedToolLogs, setSelectedToolLogs] = useState<MCPExecutionLog[]>([]);
  const [selectedToolStats, setSelectedToolStats] = useState<MCPToolStats | null>(null);

  const loadTools = async () => {
    setLoading(true);
    const data = await apiClient.listMCPTools();
    setTools(data || []);
    setLoading(false);
  };

  useEffect(() => {
    loadTools();
  }, []);

  const handleRegister = async (req: MCPToolRegistration) => {
    const result = await apiClient.registerMCPTool(req);
    if (result) {
      await loadTools();
      setShowForm(false);
    }
  };

  const handleDelete = async (tool: MCPTool) => {
    if (!confirm(`Delete MCP tool "${tool.name}"?`)) return;
    const success = await apiClient.deleteMCPTool(tool.id);
    if (success) setTools(tools.filter((t) => t.id !== tool.id));
  };

  const handleEdit = (tool: MCPTool) => {
    setEditingTool(tool);
    setShowForm(true);
    setSelectedTool(null);
  };

  const handleUpdate = async (req: MCPToolRegistration) => {
    if (editingTool) {
      const result = await apiClient.updateMCPTool(editingTool.id, req);
      if (result) {
        await loadTools();
        setShowForm(false);
        setEditingTool(null);
        if (selectedTool) setSelectedTool(result);
      }
    }
  };

  const handleToolClick = async (tool: MCPTool) => {
    setSelectedTool(tool);
    const logs = await apiClient.getMCPExecutionLogs(tool.id);
    setSelectedToolLogs(logs || []);
    const stats = await apiClient.getMCPToolStats();
    const toolStats = stats?.find((s) => s.tool_id === tool.id) || null;
    setSelectedToolStats(toolStats);
  };

  return (
    <div>
      {!showForm && !selectedTool && (
        <MCPToolsList
          tools={tools}
          onToolClick={handleToolClick}
          onToolDelete={handleDelete}
          onRefresh={loadTools}
          loading={loading}
        />
      )}

      {showForm && (
        <MCPToolForm
          tool={editingTool || undefined}
          onSubmit={editingTool ? handleUpdate : handleRegister}
          onCancel={() => {
            setShowForm(false);
            setEditingTool(null);
          }}
        />
      )}

      {selectedTool && (
        <MCPToolDetail
          tool={selectedTool}
          onClose={() => setSelectedTool(null)}
          onEdit={() => handleEdit(selectedTool)}
          logs={selectedToolLogs}
          stats={selectedToolStats}
        />
      )}
    </div>
  );
}
