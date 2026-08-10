import { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { apiClient, SALES_SERVICE_URL } from '../../lib/api-client';
import { getToken } from '../../lib/secure-storage';
import type { Lead } from '../../lib/types';

const MOCK_LEADS: Lead[] = [
  { id: 'l1', name: 'Sarah Chen',   company: 'TechCorp Inc.',  email: 'sarah@techcorp.com',  score: 92, stage: 'proposal',    value: 48000, status: 'qualified' },
  { id: 'l2', name: 'Marcus Webb',  company: 'Apex Solutions', email: 'marcus@apex.io',       score: 78, stage: 'demo',        value: 24000, status: 'contacted' },
  { id: 'l3', name: 'Priya Nair',   company: 'FinFlow Ltd.',   email: 'priya@finflow.co',   score: 65, stage: 'discovery',   value: 18000, status: 'new' },
  { id: 'l4', name: 'Jake Torres',  company: 'CloudBase',      email: 'jake@cloudbase.dev',  score: 88, stage: 'negotiation', value: 72000, status: 'qualified' },
  { id: 'l5', name: 'Amira Hassan', company: 'DataSphere',     email: 'amira@datasphere.ai',  score: 55, stage: 'discovery',   value: 9600,  status: 'new' },
];

const PIPELINE_STAGES = ['discovery', 'demo', 'proposal', 'negotiation', 'won', 'lost'];

const STAGE_COLORS: Record<string, string> = {
  discovery: 'var(--color-ash)',
  demo: 'var(--color-accent-blue)',
  proposal: 'var(--color-primary)',
  negotiation: 'var(--color-accent-purple)',
  won: 'var(--color-accent-green)',
  lost: 'var(--color-accent-red)',
};

interface LeadDetailModalProps {
  lead: Lead | null;
  onClose: () => void;
  onUpdate: (lead: Lead) => void;
}

function LeadDetailModal({ lead, onClose, onUpdate }: LeadDetailModalProps) {
  const [formData, setFormData] = useState<Partial<Lead>>({});

  useEffect(() => {
    if (lead) setFormData(lead);
  }, [lead]);

  if (!lead) return null;

  const handleSave = () => {
    if (formData) {
      onUpdate({ ...lead, ...formData } as Lead);
      onClose();
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm"
      style={{ background: 'rgba(0,0,0,0.5)' }}>
      <div className="bg-card rounded-xl max-w-md w-full p-6 border"
        style={{ borderColor: 'var(--color-border)' }}>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-lg font-bold" style={{ color: 'var(--color-foreground)' }}>Lead Details</h2>
          <button onClick={onClose} className="text-muted"
            style={{ color: 'var(--color-muted-foreground)' }}>&times;</button>
        </div>
        <div className="space-y-4">
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Name</label>
            <input value={formData.name || ''} onChange={e => setFormData({...formData, name: e.target.value})}
              className="mt-1 w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Company</label>
            <input value={formData.company || ''} onChange={e => setFormData({...formData, company: e.target.value})}
              className="mt-1 w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Email</label>
            <input value={formData.email || ''} onChange={e => setFormData({...formData, email: e.target.value})}
              className="mt-1 w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>BANT Score</label>
            <input type="number" value={formData.score || 0} onChange={e => setFormData({...formData, score: parseInt(e.target.value)})}
              className="mt-1 w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Stage</label>
            <select value={formData.stage || ''} onChange={e => setFormData({...formData, stage: e.target.value})}
              className="mt-1 w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-muted)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}>
              {PIPELINE_STAGES.map(s => <option key={s} value={s}>{s}</option>)}
            </select>
          </div>
        </div>
        <div className="flex gap-2 mt-6">
          <button onClick={onClose} className="flex-1 px-4 py-2 rounded border"
            style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)', background: 'var(--color-muted)' }}>Cancel</button>
          <button onClick={handleSave} className="flex-1 px-4 py-2 rounded font-bold"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>Save</button>
        </div>
      </div>
    </div>
  );
}

export default function SalesCRM() {
  const [activeRoute, setActiveRoute] = useState('sales');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [leads, setLeads] = useState<Lead[]>(MOCK_LEADS);
  const [selectedLead, setSelectedLead] = useState<Lead | null>(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [stageFilter, setStageFilter] = useState<string>('all');
  const [loading, setLoading] = useState(false);

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

  const filteredLeads = leads.filter(l =>
    (searchTerm === '' || l.name.toLowerCase().includes(searchTerm.toLowerCase()) || l.company.toLowerCase().includes(searchTerm.toLowerCase())) &&
    (stageFilter === 'all' || l.stage === stageFilter)
  );

  const leadsByStage = (stage: string) => filteredLeads.filter(l => l.stage === stage);
  const stageValue = (stage: string) => leadsByStage(stage).reduce((s, l) => s + l.value, 0);

  const getScoreColor = (s: number) => s >= 80 ? 'var(--color-accent-green)' : s >= 60 ? 'var(--color-primary)' : 'var(--color-accent-red)';
  const getScoreBg = (s: number) => s >= 80 ? 'rgba(44,140,102,0.12)' : s >= 60 ? 'rgba(247,165,1,0.12)' : 'rgba(205,66,57,0.12)';

  const handleUpdateLead = (updatedLead: Lead) => {
    setLeads(leads.map(l => l.id === updatedLead.id ? updatedLead : l));
  };

  const handleExport = () => {
    const csvContent = 'data:text/csv;charset=utf-8,' +
      ['Name,Company,Email,Score,Stage,Value,Status'].join(',') + '\n' +
      leads.map(l => [l.name, l.company, l.email, l.score, l.stage || '', l.value, l.status].join(',')).join('\n');
    const link = document.createElement('a');
    link.setAttribute('href', encodeURI(csvContent));
    link.setAttribute('download', `leads-export-${new Date().toISOString().slice(0,10)}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const handleAIAssist = async () => {
    setLoading(true);
    try {
       const token = getToken();
      const headers: Record<string, string> = { 'Content-Type': 'application/json' };
      if (token) {
        headers['Authorization'] = `Bearer ${token}`;
      }
      const res = await fetch(`${SALES_SERVICE_URL}/api/v1/sales/assist`, {
        method: 'POST',
        headers,
        body: JSON.stringify({ leads: filteredLeads }),
      });
      if (res.ok) {
        const data = await res.json();
        console.log('AI Assist completed');
      }
    } catch (error) {
      console.error('AI Assist error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 flex flex-col overflow-hidden">
        <header className="flex items-center justify-between px-6 py-4 border-b flex-shrink-0"
          style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="font-bold text-lg" style={{ color: 'var(--color-foreground)' }}>Sales CRM & Pipeline</h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>AI-qualified leads · BANT scoring · Kanban pipeline</p>
          </div>
          <div className="flex items-center gap-3">
            <input type="text" placeholder="Search leads..." value={searchTerm} onChange={e => setSearchTerm(e.target.value)}
              className="px-3 py-1.5 rounded border text-sm"
              style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
            <select value={stageFilter} onChange={e => setStageFilter(e.target.value)}
              className="px-3 py-1.5 rounded border text-sm"
              style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}>
              <option value="all">All Stages</option>
              {PIPELINE_STAGES.map(s => <option key={s} value={s}>{s}</option>)}
            </select>
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
              onClick={handleAIAssist}
              disabled={loading}
              className="px-3 py-1.5 text-xs rounded font-semibold transition-all disabled:opacity-60"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              {loading ? '⏳' : 'AI Assist'}
            </button>
            <button onClick={handleExport} className="px-3 py-1.5 text-xs rounded border"
              style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)', background: 'var(--color-muted)' }}>
              Export CSV
            </button>
            <button
              onClick={() => setSelectedLead(null)}
              className="px-4 py-2 text-xs font-semibold rounded-lg"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              + New Lead
            </button>
          </div>
        </header>

        <div className="flex border-b px-6 py-3 gap-6 flex-shrink-0" style={{ borderColor: 'var(--color-border)', background: 'var(--color-card)' }}>
          {[
            { label: 'Total Pipeline', value: `$${leads.reduce((s, l) => s + l.value, 0).toLocaleString()}` },
            { label: 'Qualified Leads', value: leads.filter(l => l.status === 'qualified').length },
            { label: 'Avg BANT Score', value: `${Math.round(leads.reduce((s, l) => s + l.score, 0) / leads.length)}` },
            { label: 'Conversion Rate', value: '18.6%' },
          ].map(m => (
            <div key={m.label} className="text-center">
              <div className="text-base font-bold" style={{ color: 'var(--color-primary)' }}>{m.value}</div>
              <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{m.label}</div>
            </div>
          ))}
        </div>

        <div className="flex-1 overflow-x-auto overflow-y-hidden p-5">
          <div className="flex gap-4 h-full min-w-max">
            {PIPELINE_STAGES.map(stage => (
              <div key={stage} className="flex flex-col w-64 flex-shrink-0 rounded-xl overflow-hidden"
                style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="flex items-center justify-between px-4 py-3 border-b flex-shrink-0"
                  style={{ borderColor: 'var(--color-border)' }}>
                  <div className="flex items-center gap-2">
                    <div className="w-2 h-2 rounded-full" style={{ background: STAGE_COLORS[stage] }} />
                    <span className="text-xs font-bold uppercase tracking-wider capitalize"
                      style={{ color: 'var(--color-foreground)' }}>{stage}</span>
                  </div>
                  <div className="text-right">
                    <div className="text-xs font-bold" style={{ color: 'var(--color-primary)' }}>
                      ${(stageValue(stage) / 1000).toFixed(0)}k
                    </div>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                      {leadsByStage(stage).length} leads
                    </div>
                  </div>
                </div>

                <div className="flex-1 overflow-y-auto p-3 space-y-3">
                  {leadsByStage(stage).map(lead => (
                    <div key={lead.id}
                      onClick={() => setSelectedLead(lead)}
                      className="p-3 rounded-lg cursor-pointer hover:shadow-lg transition-all duration-200"
                      style={{ background: 'var(--color-background)', border: '1px solid var(--color-border)' }}>
                      <div className="flex items-start justify-between mb-2">
                        <div>
                          <div className="text-xs font-semibold" style={{ color: 'var(--color-foreground)' }}>{lead.name}</div>
                          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{lead.company}</div>
                        </div>
                        <div className="text-xs font-bold px-1.5 py-0.5 rounded"
                          style={{ background: getScoreBg(lead.score), color: getScoreColor(lead.score) }}>
                          {lead.score}
                        </div>
                      </div>
                      <div className="text-xs font-semibold" style={{ color: 'var(--color-primary)' }}>
                        ${lead.value.toLocaleString()}
                      </div>
                      <div className="mt-2 h-1 rounded-full" style={{ background: 'var(--color-border)' }}>
                        <div className="h-full rounded-full" style={{ width: `${lead.score}%`, background: getScoreColor(lead.score) }} />
                      </div>
                    </div>
                  ))}
                  {leadsByStage(stage).length === 0 && (
                    <div className="flex-1 flex items-center justify-center text-center py-8"
                      style={{ color: 'var(--color-muted-foreground)' }}>
                      No leads in {stage}
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>

        {selectedLead && (
          <LeadDetailModal
            lead={selectedLead}
            onClose={() => setSelectedLead(null)}
            onUpdate={handleUpdateLead}
          />
        )}
      </main>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}
