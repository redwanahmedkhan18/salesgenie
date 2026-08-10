import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { useAuth } from '../../auth/AuthProvider';
import { getToken } from '../../lib/secure-storage';
import { AI_GATEWAY_SERVICE_URL } from '../../lib/api-client';
import type { AIAgent } from '../../lib/types';

const DEFAULT_PROMPT = `You are SalesGenie's Senior AI Sales Representative.

Your goal is to:
1. Qualify leads using the BANT framework (Budget, Authority, Need, Timeline)
2. Recommend products and upsell opportunities
3. Apply relevant promotional coupons
4. Book demo calls for high-intent leads

Tone: {{tone}}
Company Name: {{company_name}}
Product Focus: {{product_focus}}

Context from Knowledge Base:
{{rag_context}}`;

const AGENT_TYPES: AIAgent['type'][] = ['sales', 'support', 'refund', 'booking', 'hr'];

const PROVIDERS = [
  { value: 'grok-beta', label: 'Grok Beta (Primary)' },
  { value: 'gemini-2.0-flash', label: 'Gemini 2.0 Flash' },
  { value: 'gpt-4o', label: 'GPT-4o' },
  { value: 'claude-3.5-sonnet', label: 'Claude 3.5 Sonnet' },
];

function PromptToolbar({ onInsert }: { onInsert: (variable: string) => void }) {
  return (
    <div className="flex gap-1 flex-wrap">
      {['tone', 'company_name', 'product_focus', 'rag_context'].map(v => (
        <button
          key={v}
          onClick={() => onInsert(v)}
          className="text-xs px-2 py-0.5 rounded border transition-colors hover:bg-amber-500/10"
          style={{ borderColor: 'rgba(247,165,1,0.3)', color: 'var(--color-primary)' }}
        >
          {`{{${v}}}`}
        </button>
      ))}
    </div>
  );
}

export default function AgentBuilder() {
  const { user } = useAuth();
  const tenantId = user?.tenant_id || 'default_tenant';
  const [activeRoute, setActiveRoute] = useState('agents');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [selectedAgent, setSelectedAgent] = useState<AIAgent | null>(null);
  const [agents, setAgents] = useState<AIAgent[]>([]);
  const [promptText, setPromptText] = useState(DEFAULT_PROMPT);
  const [temperature, setTemperature] = useState(0.7);
  const [maxTokens, setMaxTokens] = useState(1000);
  const [provider, setProvider] = useState('grok-beta');
  const [saving, setSaving] = useState(false);
  const [loading, setLoading] = useState(true);
  const [agentName, setAgentName] = useState('');
  const [agentType, setAgentType] = useState<AIAgent['type']>('sales');
  const [isCreating, setIsCreating] = useState(false);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setPaletteOpen(p => !p);
      }
      if (e.key === 'Escape') setPaletteOpen(false);
    };
    document.addEventListener('open-command-palette', () => setPaletteOpen(true));
    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  useEffect(() => {
    const loadAgents = async () => {
      setLoading(true);
      try {
         const token = getToken();
        if (!token) {
          window.location.href = '/login';
          return;
        }
        const res = await fetch(`${AI_GATEWAY_SERVICE_URL}/api/v1/agents?tenant_id=${encodeURIComponent(tenantId)}`, {
          headers: token ? { 'Authorization': `Bearer ${token}` } : {},
        });
        if (res.ok) {
          const data: AIAgent[] = await res.json();
          setAgents(data);
          if (data.length > 0) setSelectedAgent(data[0]);
        } else {
          const fallback: AIAgent[] = [
            { id: 'sales', name: 'Sales AI Agent', type: 'sales', model: 'groq', temperature: 0.7, is_active: true, created_at: new Date().toISOString(), tenant_id: tenantId },
            { id: 'support', name: 'Support AI Agent', type: 'support', model: 'groq', temperature: 0.7, is_active: true, created_at: new Date().toISOString(), tenant_id: tenantId },
            { id: 'knowledge', name: 'Knowledge Search Agent', type: 'search' as AIAgent['type'], model: 'groq', temperature: 0.5, is_active: true, created_at: new Date().toISOString(), tenant_id: tenantId },
          ];
          setAgents(fallback);
          setSelectedAgent(fallback[0]);
        }
      } catch (error) {
        console.error('Failed to load agents:', error);
        const fallback: AIAgent[] = [
          { id: 'sales', name: 'Sales AI Agent', type: 'sales', model: 'groq', temperature: 0.7, is_active: true, created_at: new Date().toISOString(), tenant_id: 'default' },
          { id: 'support', name: 'Support AI Agent', type: 'support', model: 'groq', temperature: 0.7, is_active: true, created_at: new Date().toISOString(), tenant_id: 'default' },
          { id: 'knowledge', name: 'Knowledge Search Agent', type: 'search' as AIAgent['type'], model: 'groq', temperature: 0.5, is_active: true, created_at: new Date().toISOString(), tenant_id: 'default' },
        ];
        setAgents(fallback);
        setSelectedAgent(fallback[0]);
      } finally {
        setLoading(false);
      }
    };
    loadAgents();
  }, []);

  const handleSave = async () => {
    if (!selectedAgent) return;
    setSaving(true);
    try {
      const token = getToken();
      const res = await fetch(`${AI_GATEWAY_SERVICE_URL}/api/v1/agents/${selectedAgent.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
        },
        body: JSON.stringify({
          name: selectedAgent.name,
          type: selectedAgent.type,
          model: provider,
          temperature,
        }),
      });
      if (res.ok) {
        setAgents(agents.map(a => a.id === selectedAgent.id ? selectedAgent : a));
      }
    } catch (error) {
      console.error('Failed to save agent:', error);
    } finally {
      setTimeout(() => setSaving(false), 1200);
    }
  };

  const handleCreateAgent = async () => {
    if (!agentName.trim()) return;
    setIsCreating(true);
    try {
      const token = getToken();
      const res = await fetch(`${AI_GATEWAY_SERVICE_URL}/api/v1/agents`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
        },
        body: JSON.stringify({
          name: agentName,
          type: agentType,
          model: provider,
          temperature,
          tenant_id: tenantId,
        }),
      });
      if (res.ok) {
        const newAgent: AIAgent = await res.json();
        setAgents([...agents, newAgent]);
        setSelectedAgent(newAgent);
        setAgentName('');
        setAgentType('sales');
      }
    } catch (error) {
      console.error('Failed to create agent:', error);
    } finally {
      setIsCreating(false);
    }
  };

  const insertVariable = (variable: string) => {
    setPromptText(prev => prev + `{{${variable}}}`);
  };

  const handleProviderChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const newProvider = e.target.value;
    setProvider(newProvider);
    if (selectedAgent) {
      setSelectedAgent({ ...selectedAgent, model: newProvider as AIAgent['model'] });
    }
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 flex flex-col overflow-hidden">
        <header className="flex items-center justify-between px-6 py-4 border-b flex-shrink-0"
          style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="font-bold text-lg" style={{ color: 'var(--color-foreground)' }}>AI Agent Builder & Prompt Studio</h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Configure multi-agent personalities, prompts, and tool calling</p>
          </div>
          <div className="flex items-center gap-3">
            <button
              id="open-command-palette-btn"
              onClick={() => setPaletteOpen(true)}
              className="flex items-center gap-2 px-3 py-1.5 rounded text-xs transition-colors"
              style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)', border: '1px solid var(--color-border)' }}
            >
              <span>🔍</span>
              <span>Search</span>
              <kbd className="text-xs">⌘K</kbd>
            </button>
            <button
              onClick={handleSave}
              disabled={saving || !selectedAgent}
              className="px-4 py-2 text-sm font-semibold rounded-lg transition-all disabled:opacity-60"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              {saving ? '⏳ Saving...' : '💾 Save Configuration'}
            </button>
          </div>
        </header>

        <div className="flex flex-1 overflow-hidden">
          <div className="w-64 border-r flex-shrink-0 flex flex-col overflow-y-auto"
            style={{ background: 'var(--color-surface-dark)', borderColor: 'var(--color-border)' }}>
            <div className="px-4 py-3 border-b text-xs font-semibold uppercase tracking-wider"
              style={{ borderColor: 'var(--color-border)', color: 'var(--color-muted-foreground)' }}>
              Platform Agents
            </div>

            {loading ? (
              <div className="p-4 space-y-3">
                {Array.from({ length: 3 }).map((_, i) => (
                  <div key={i} className="skeleton h-12 rounded-lg" />
                ))}
              </div>
            ) : (
              <div className="py-2">
                {agents.map(agent => (
                  <button
                    key={agent.id}
                    onClick={() => setSelectedAgent(agent)}
                    className={`w-full text-left px-4 py-3 transition-colors border-l-2 flex items-center gap-3 ${selectedAgent?.id === agent.id ? 'border-amber-500 bg-amber-500/8' : 'border-transparent hover:bg-white/3'}`}
                  >
                    <div className="w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold flex-shrink-0"
                      style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                      {agent.type === 'sales' ? '💼' : agent.type === 'support' ? '🎧' : '📚'}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="text-xs font-semibold" style={{ color: 'var(--color-foreground)' }}>{agent.name}</div>
                      <div className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                        {agent.model} · {Math.round(agent.temperature * 100)}% creativity
                      </div>
                    </div>
                    <span className={`text-xs px-1.5 py-0.5 rounded ${agent.is_active ? 'bg-green-500/15 text-green-400' : 'bg-red-500/15 text-red-400'}`}>
                      {agent.is_active ? '●' : '○'}
                    </span>
                  </button>
                ))}
              </div>
            )}

            <div className="p-4 border-t" style={{ borderColor: 'var(--color-border)' }}>
              <div className="text-xs font-semibold mb-3 uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>
                Create New Agent
              </div>
              <div className="space-y-3">
                <input
                  type="text"
                  placeholder="Agent name..."
                  value={agentName}
                  onChange={e => setAgentName(e.target.value)}
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
                />
                <select
                  value={agentType}
                  onChange={e => setAgentType(e.target.value as any)}
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
                >
                  {AGENT_TYPES.map(t => (
                    <option key={t} value={t}>{t.charAt(0).toUpperCase() + t.slice(1)}</option>
                  ))}
                </select>
                <button
                  onClick={handleCreateAgent}
                  disabled={!agentName.trim() || isCreating}
                  className="w-full px-3 py-2 text-xs font-semibold rounded-lg transition-all disabled:opacity-60"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                >
                  {isCreating ? '⏳ Creating...' : '+ Create Agent'}
                </button>
              </div>

              <div className="text-xs font-semibold mb-2 mt-4 uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>
                Version History
              </div>
              {['v3 · Current', 'v2 · Jul 25', 'v1 · Jul 18'].map(v => (
                <button
                  key={v}
                   onClick={() => {}}
                  className="w-full text-left text-xs py-1.5 transition-colors"
                  style={{ color: 'var(--color-muted-foreground)' }}
                >
                  📋 {v}
                </button>
              ))}
            </div>
          </div>

          <div className="flex-1 flex flex-col overflow-hidden">
            {selectedAgent ? (
              <>
                <div className="flex items-center gap-6 px-6 py-3 border-b"
                  style={{ borderColor: 'var(--color-border)', background: 'var(--color-surface-dark)' }}>
                  <div className="flex items-center gap-2">
                    <span className="text-xl">
                      {selectedAgent.type === 'sales' ? '💼' : selectedAgent.type === 'support' ? '🎧' : '📚'}
                    </span>
                    <span className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{selectedAgent.name}</span>
                    <span className="text-xs px-2 py-0.5 rounded-full"
                      style={{ background: 'rgba(44,140,102,0.15)', color: 'var(--color-accent-green)' }}>● Active</span>
                  </div>
                  <div className="text-xs px-3 py-1 rounded-lg"
                    style={{ background: 'var(--color-muted)', color: 'var(--color-foreground)' }}>
                    Accuracy: <strong style={{ color: 'var(--color-primary)' }}>99.1%</strong>
                  </div>
                  <div className="text-xs px-3 py-1 rounded-lg"
                    style={{ background: 'var(--color-muted)', color: 'var(--color-foreground)' }}>
                    284 conversations handled
                  </div>
                </div>

                <div className="flex flex-1 overflow-hidden">
                  <div className="flex-1 flex flex-col p-5 overflow-hidden">
                    <div className="flex items-center justify-between mb-2">
                      <label className="text-xs font-semibold uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>
                        System Prompt
                      </label>
                      <PromptToolbar onInsert={insertVariable} />
                    </div>
                    <textarea
                      id="agent-prompt-editor"
                      className="flex-1 w-full p-4 rounded-xl text-sm font-mono resize-none outline-none border"
                      style={{
                        background: 'var(--color-muted)',
                        color: 'var(--color-foreground)',
                        borderColor: 'var(--color-border)',
                        fontFamily: 'Source Code Pro, ui-monospace, monospace',
                      }}
                      value={promptText}
                      onChange={e => setPromptText(e.target.value)}
                    />
                    <div className="flex items-center justify-between mt-2">
                      <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                        {promptText.length} chars · {promptText.split(/\s+/).length} tokens est.
                      </span>
                    </div>
                  </div>

                  <div className="w-64 border-l flex-shrink-0 p-5 space-y-5 overflow-y-auto" style={{ borderColor: 'var(--color-border)' }}>
                    <div>
                      <label className="text-xs font-semibold uppercase tracking-wider block mb-2" style={{ color: 'var(--color-muted-foreground)' }}>
                        LLM Provider
                      </label>
                      <select
                        id="llm-provider-select"
                        value={provider}
                        onChange={handleProviderChange}
                        className="w-full px-3 py-2 rounded-lg text-sm outline-none border"
                        style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}
                      >
                        {PROVIDERS.map(p => (
                          <option key={p.value} value={p.value}>{p.label}</option>
                        ))}
                      </select>
                    </div>

                    <div>
                      <label className="text-xs font-semibold uppercase tracking-wider block mb-2" style={{ color: 'var(--color-muted-foreground)' }}>
                        Temperature <span style={{ color: 'var(--color-primary)' }}>{temperature.toFixed(2)}</span>
                      </label>
                      <input
                        type="range"
                        min={0}
                        max={1}
                        step={0.05}
                        value={temperature}
                        onChange={e => {
                          const newTemp = parseFloat(e.target.value);
                          setTemperature(newTemp);
                          if (selectedAgent) {
                            setSelectedAgent({ ...selectedAgent, temperature: newTemp });
                          }
                        }}
                        className="w-full"
                      />
                      <div className="flex justify-between text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
                        <span>Precise</span><span>Creative</span>
                      </div>
                    </div>

                    <div>
                      <label className="text-xs font-semibold uppercase tracking-wider block mb-2" style={{ color: 'var(--color-muted-foreground)' }}>
                        Max Tokens <span style={{ color: 'var(--color-primary)' }}>{maxTokens}</span>
                      </label>
                      <input
                        type="range"
                        min={100}
                        max={4000}
                        step={50}
                        value={maxTokens}
                        onChange={e => setMaxTokens(parseInt(e.target.value))}
                        className="w-full"
                      />
                    </div>

                    <div>
                      <label className="text-xs font-semibold uppercase tracking-wider block mb-3" style={{ color: 'var(--color-muted-foreground)' }}>
                        Active Tools
                      </label>
                      <div className="space-y-2">
                        {['CRM Lookup', 'Knowledge Search', 'Ticket Creator', 'Calendar Booking', 'Coupon Distributor'].map(tool => (
                          <label key={tool} className="flex items-center gap-2 cursor-pointer">
                            <input type="checkbox" defaultChecked className="border rounded"
                              style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)' }} />
                            <span className="text-xs" style={{ color: 'var(--color-foreground)' }}>{tool}</span>
                          </label>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </>
            ) : (
              <div className="flex-1 flex items-center justify-center" style={{ color: 'var(--color-muted-foreground)' }}>
                Select an agent to configure
              </div>
            )}
          </div>
        </div>
      </main>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}
