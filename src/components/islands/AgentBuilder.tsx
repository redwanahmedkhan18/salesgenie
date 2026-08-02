import React, { useState } from 'react';
import { Sidebar, CommandPalette } from './AppShell';

const AGENTS = [
  { id: 'sales', name: 'Sales AI Agent', status: 'active', type: 'sales_agent', icon: '💼', convos: 284, accuracy: 98.4 },
  { id: 'support', name: 'Support AI Agent', status: 'active', type: 'support_agent', icon: '🎧', convos: 891, accuracy: 99.1 },
  { id: 'knowledge', name: 'Knowledge Search Agent', status: 'active', type: 'search_agent', icon: '📚', convos: 1204, accuracy: 99.8 },
];

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

export default function AgentBuilder() {
  const [activeRoute, setActiveRoute] = useState('agents');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [selectedAgent, setSelectedAgent] = useState(AGENTS[0]);
  const [promptText, setPromptText] = useState(DEFAULT_PROMPT);
  const [temperature, setTemperature] = useState(0.7);
  const [maxTokens, setMaxTokens] = useState(1000);
  const [provider, setProvider] = useState('grok-beta');
  const [saving, setSaving] = useState(false);

  const handleSave = () => {
    setSaving(true);
    setTimeout(() => setSaving(false), 1200);
  };

  const insertVariable = (variable: string) => {
    setPromptText(prev => prev + `{{${variable}}}`);
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <header className="flex items-center justify-between px-6 py-4 border-b flex-shrink-0"
          style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="font-bold text-lg" style={{ color: 'var(--color-foreground)' }}>AI Agent Builder & Prompt Studio</h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Configure multi-agent personalities, prompts, and tool calling</p>
          </div>
          <div className="flex gap-2">
            <button onClick={handleSave} disabled={saving}
              className="px-4 py-2 text-sm font-semibold rounded-lg transition-all disabled:opacity-60"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
              {saving ? '⏳ Saving...' : '💾 Save Configuration'}
            </button>
          </div>
        </header>

        <div className="flex flex-1 overflow-hidden">
          {/* Agent selector panel */}
          <div className="w-64 border-r flex-shrink-0 flex flex-col" style={{ borderColor: 'var(--color-border)', background: 'var(--color-card)' }}>
            <div className="px-4 py-3 border-b text-xs font-semibold uppercase tracking-wider" style={{ borderColor: 'var(--color-border)', color: 'var(--color-muted-foreground)' }}>
              Platform Agents
            </div>
            <div className="flex-1 overflow-y-auto py-2">
              {AGENTS.map(agent => (
                <button
                  key={agent.id}
                  onClick={() => setSelectedAgent(agent)}
                  className={`w-full text-left px-4 py-3 transition-colors border-l-2 ${selectedAgent.id === agent.id ? 'border-amber-500 bg-amber-500/8' : 'border-transparent hover:bg-white/3'}`}
                >
                  <div className="flex items-center gap-3">
                    <span className="text-xl">{agent.icon}</span>
                    <div>
                      <div className="text-xs font-semibold" style={{ color: 'var(--color-foreground)' }}>{agent.name}</div>
                      <div className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>{agent.convos} conversations</div>
                    </div>
                  </div>
                </button>
              ))}
            </div>

            {/* Version History */}
            <div className="p-4 border-t" style={{ borderColor: 'var(--color-border)' }}>
              <div className="text-xs font-semibold mb-2 uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>Version History</div>
              {['v3 · Current', 'v2 · Jul 25', 'v1 · Jul 18'].map(v => (
                <button key={v} onClick={() => alert(`Version: ${v}`)} className="w-full text-left text-xs py-1.5 transition-colors hover:text-amber-400"
                  style={{ color: 'var(--color-muted-foreground)' }}>
                  📋 {v}
                </button>
              ))}
            </div>
          </div>

          {/* Prompt Editor */}
          <div className="flex-1 flex flex-col overflow-hidden">
            {/* Agent stats bar */}
            <div className="flex items-center gap-6 px-6 py-3 border-b" style={{ borderColor: 'var(--color-border)', background: 'var(--color-background)' }}>
              <div className="flex items-center gap-2">
                <span className="text-xl">{selectedAgent.icon}</span>
                <span className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{selectedAgent.name}</span>
                <span className="text-xs px-2 py-0.5 rounded-full" style={{ background: 'rgba(44,140,102,0.15)', color: '#2c8c66' }}>● Active</span>
              </div>
              <div className="text-xs px-3 py-1 rounded-lg" style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}>
                Accuracy: <strong style={{ color: '#2c8c66' }}>{selectedAgent.accuracy}%</strong>
              </div>
              <div className="text-xs px-3 py-1 rounded-lg" style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}>
                {selectedAgent.convos.toLocaleString()} conversations handled
              </div>
            </div>

            <div className="flex flex-1 overflow-hidden">
              {/* Prompt textarea */}
              <div className="flex-1 flex flex-col p-5 overflow-hidden">
                <div className="flex items-center justify-between mb-2">
                  <label className="text-xs font-semibold uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>
                    System Prompt
                  </label>
                  <div className="flex gap-2">
                    {['tone', 'company_name', 'product_focus', 'rag_context'].map(v => (
                      <button key={v} onClick={() => insertVariable(v)}
                        className="text-xs px-2 py-0.5 rounded border transition-colors hover:bg-amber-500/10"
                        style={{ borderColor: 'rgba(247,165,1,0.3)', color: 'var(--color-primary)' }}>
                        +{`{${v}}`}
                      </button>
                    ))}
                  </div>
                </div>
                <textarea
                  id="agent-prompt-editor"
                  className="flex-1 w-full p-4 rounded-xl text-sm font-mono resize-none outline-none border leading-relaxed"
                  style={{
                    background: 'var(--color-card)',
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

              {/* Config Panel */}
              <div className="w-64 border-l flex-shrink-0 p-5 space-y-5 overflow-y-auto" style={{ borderColor: 'var(--color-border)' }}>
                <div>
                  <label className="text-xs font-semibold uppercase tracking-wider block mb-2" style={{ color: 'var(--color-muted-foreground)' }}>LLM Provider</label>
                  <select
                    id="llm-provider-select"
                    value={provider}
                    onChange={e => setProvider(e.target.value)}
                    className="w-full px-3 py-2 rounded-lg text-sm border outline-none"
                    style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
                  >
                    <option value="grok-beta">Grok Beta (Primary)</option>
                    <option value="gemini-2.0-flash">Gemini 2.0 Flash</option>
                    <option value="gpt-4o">GPT-4o</option>
                    <option value="claude-3.5-sonnet">Claude 3.5 Sonnet</option>
                  </select>
                </div>

                <div>
                  <label className="text-xs font-semibold uppercase tracking-wider block mb-2" style={{ color: 'var(--color-muted-foreground)' }}>
                    Temperature <span style={{ color: 'var(--color-primary)' }}>{temperature}</span>
                  </label>
                  <input type="range" min={0} max={1} step={0.05} value={temperature}
                    onChange={e => setTemperature(parseFloat(e.target.value))}
                    className="w-full accent-amber-500" />
                  <div className="flex justify-between text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    <span>Precise</span><span>Creative</span>
                  </div>
                </div>

                <div>
                  <label className="text-xs font-semibold uppercase tracking-wider block mb-2" style={{ color: 'var(--color-muted-foreground)' }}>
                    Max Tokens <span style={{ color: 'var(--color-primary)' }}>{maxTokens}</span>
                  </label>
                  <input type="range" min={100} max={4000} step={50} value={maxTokens}
                    onChange={e => setMaxTokens(parseInt(e.target.value))}
                    className="w-full accent-amber-500" />
                </div>

                <div>
                  <label className="text-xs font-semibold uppercase tracking-wider block mb-3" style={{ color: 'var(--color-muted-foreground)' }}>Active Tools</label>
                  <div className="space-y-2">
                    {['CRM Lookup', 'Knowledge Search', 'Ticket Creator', 'Calendar Booking', 'Coupon Distributor'].map(tool => (
                      <label key={tool} className="flex items-center gap-2 cursor-pointer">
                        <input type="checkbox" defaultChecked className="accent-amber-500" />
                        <span className="text-xs" style={{ color: 'var(--color-foreground)' }}>{tool}</span>
                      </label>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}
