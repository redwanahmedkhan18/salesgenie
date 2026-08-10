import React, { useState, useEffect } from 'react';
import { apiClient, type SalesLead, type SalesDeal, type SalesCoupon, type CreateDealRequest, type CreateCouponRequest } from '../../lib/api-client';
import type { DealStage } from '../../lib/types';

const PIPELINE_STAGES: { key: string; label: string; color: string }[] = [
  { key: 'discovery', label: 'Discovery', color: '#9b9c92' },
  { key: 'demo', label: 'Demo', color: '#2c84e0' },
  { key: 'proposal', label: 'Proposal', color: '#f7a501' },
  { key: 'negotiation', label: 'Negotiation', color: '#7c44a6' },
  { key: 'won', label: 'Won', color: '#2c8c66' },
  { key: 'lost', label: 'Lost', color: '#cd4239' },
];

export default function SalesManagerDashboard() {
  const [activeTab, setActiveTab] = useState<'pipeline' | 'leads' | 'coupons'>('pipeline');
  const [deals, setDeals] = useState<SalesDeal[]>([]);
  const [leads, setLeads] = useState<SalesLead[]>([]);
  const [coupons, setCoupons] = useState<SalesCoupon[]>([]);
  const [loading, setLoading] = useState(true);
  const [showDealModal, setShowDealModal] = useState(false);
  const [showCouponModal, setShowCouponModal] = useState(false);
  const [editingDeal, setEditingDeal] = useState<SalesDeal | null>(null);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    setLoading(true);
    const [dealsData, leadsData, couponsData] = await Promise.all([
      apiClient.getSalesDeals(),
      apiClient.getSalesLeads(),
      apiClient.getSalesCoupons(),
    ]);
    setDeals(dealsData);
    setLeads(leadsData);
    setCoupons(couponsData);
    setLoading(false);
  };

  const handleCreateDeal = async (req: CreateDealRequest) => {
    const result = await apiClient.createSalesDeal(req);
    if (result) {
      setDeals([...deals, result]);
      setShowDealModal(false);
    }
  };

  const handleUpdateDeal = async (id: string, req: CreateDealRequest) => {
    const result = await apiClient.updateSalesDeal(id, req);
    if (result) {
      setDeals(deals.map(d => d.id === id ? result : d));
      setEditingDeal(null);
    }
  };

  const handleDeleteDeal = async (id: string) => {
    const ok = await apiClient.deleteSalesDeal(id);
      if (ok) setDeals(deals.filter(d => d.id !== id));
  };

  const handleCreateCoupon = async (req: CreateCouponRequest) => {
    const result = await apiClient.createSalesCoupon(req);
    if (result) {
      setCoupons([...coupons, result]);
      setShowCouponModal(false);
    }
  };

  const dealsByStage = (stage: string) => deals.filter(d => d.pipeline_stage === stage);
  const stageValue = (stage: string) => dealsByStage(stage).reduce((s, d) => s + d.value_usd, 0);

  const stageColor = (stage: string) => {
    const found = PIPELINE_STAGES.find(s => s.key === stage);
    return found ? found.color : '#9b9c92';
  };

  const scoreColor = (s: number) => s >= 80 ? '#2c8c66' : s >= 60 ? '#f7a501' : '#cd4239';

  const totalPipelineValue = deals.filter(d => d.pipeline_stage !== 'won' && d.pipeline_stage !== 'lost').reduce((s, d) => s + d.value_usd, 0);
  const wonValue = deals.filter(d => d.pipeline_stage === 'won').reduce((s, d) => s + d.value_usd, 0);
  const activeDeals = deals.filter(d => d.pipeline_stage !== 'won' && d.pipeline_stage !== 'lost').length;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Sales Manager Dashboard</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Pipeline management, deal tracking, and team oversight</p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={() => setShowDealModal(true)}
            className="px-4 py-2 text-xs font-semibold rounded-lg"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
          >
            + New Deal
          </button>
          <button
            onClick={() => setShowCouponModal(true)}
            className="px-4 py-2 text-xs font-semibold rounded border"
            style={{ borderColor: 'var(--color-primary)', color: 'var(--color-primary)' }}
          >
            + New Coupon
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Pipeline Value</div>
          <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-primary)' }}>
            ${totalPipelineValue.toLocaleString()}
          </div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Active Deals</div>
          <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-primary)' }}>{activeDeals}</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Won This Period</div>
          <div className="text-2xl font-bold mt-1" style={{ color: '#2c8c66' }}>
            ${wonValue.toLocaleString()}
          </div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Qualified Leads</div>
          <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-primary)' }}>
            {leads.filter(l => l.status === 'qualified').length}
          </div>
        </div>
      </div>

      <div className="border-b" style={{ borderColor: 'var(--color-border)' }}>
        <div className="flex gap-6">
          <button
            onClick={() => setActiveTab('pipeline')}
            className={`pb-3 px-1 text-sm font-medium transition-colors ${
              activeTab === 'pipeline' ? 'border-b-2' : ''
            }`}
            style={{
              borderColor: activeTab === 'pipeline' ? 'var(--color-primary)' : 'transparent',
              color: activeTab === 'pipeline' ? 'var(--color-primary)' : 'var(--color-muted-foreground)',
            }}
          >
            Pipeline (Kanban)
          </button>
          <button
            onClick={() => setActiveTab('leads')}
            className={`pb-3 px-1 text-sm font-medium transition-colors ${
              activeTab === 'leads' ? 'border-b-2' : ''
            }`}
            style={{
              borderColor: activeTab === 'leads' ? 'var(--color-primary)' : 'transparent',
              color: activeTab === 'leads' ? 'var(--color-primary)' : 'var(--color-muted-foreground)',
            }}
          >
            Leads
          </button>
          <button
            onClick={() => setActiveTab('coupons')}
            className={`pb-3 px-1 text-sm font-medium transition-colors ${
              activeTab === 'coupons' ? 'border-b-2' : ''
            }`}
            style={{
              borderColor: activeTab === 'coupons' ? 'var(--color-primary)' : 'transparent',
              color: activeTab === 'coupons' ? 'var(--color-primary)' : 'var(--color-muted-foreground)',
            }}
          >
            Coupons
          </button>
        </div>
      </div>

      {loading ? (
        <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>Loading...</div>
      ) : null}

      {activeTab === 'pipeline' && !loading && (
        <div className="flex gap-4 overflow-x-auto pb-4">
          {PIPELINE_STAGES.map(stage => (
            <div key={stage.key} className="flex flex-col w-64 flex-shrink-0">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-bold uppercase tracking-wider" style={{ color: stageColor(stage.key) }}>
                  {stage.label}
                </span>
                <span className="text-xs font-bold px-2 py-0.5 rounded"
                  style={{ background: `${stageColor(stage.key)}20`, color: stageColor(stage.key) }}>
                  {dealsByStage(stage.key).length}
                </span>
              </div>
              <div className="space-y-3 flex-1">
                {dealsByStage(stage.key).map(deal => (
                  <div
                    key={deal.id}
                    onClick={() => setEditingDeal(deal)}
                    className="p-3 rounded-lg cursor-pointer transition-all duration-200"
                    style={{
                      background: 'var(--color-background)',
                      border: '1px solid var(--color-border)',
                    }}
                  >
                    <div className="text-sm font-semibold" style={{ color: 'var(--color-foreground)' }}>{deal.title}</div>
                    <div className="text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      ${deal.value_usd.toLocaleString()} · {(deal.probability * 100).toFixed(0)}%
                    </div>
                    <button
                      onClick={e => { e.stopPropagation(); handleDeleteDeal(deal.id); }}
                      className="text-xs mt-2 px-2 py-1 rounded"
                      style={{ background: 'rgba(205,66,59,0.15)', color: '#cd4239' }}
                    >
                      Delete
                    </button>
                  </div>
                ))}
                {dealsByStage(stage.key).length === 0 && (
                  <div className="text-center py-6 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                    No deals in {stage.label}
                  </div>
                )}
              </div>
              <div className="text-right mt-2">
                <div className="text-xs font-bold" style={{ color: 'var(--color-primary)' }}>
                  ${(stageValue(stage.key) / 1000).toFixed(0)}k
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {activeTab === 'leads' && !loading && (
        <table className="w-full text-sm">
          <thead>
            <tr className="text-xs uppercase tracking-wider" style={{ color: '#94a3b8' }}>
              <th className="text-left px-4 py-2">Lead</th>
              <th className="text-left px-4 py-2">Company</th>
              <th className="text-left px-4 py-2">BANT Score</th>
              <th className="text-left px-4 py-2">Status</th>
              <th className="text-left px-4 py-2">Budget</th>
              <th className="text-left px-4 py-2">Created</th>
            </tr>
          </thead>
          <tbody>
            {leads.map(l => (
              <tr key={l.id} style={{ background: '#1e293b', borderRadius: 8 }}>
                <td className="px-4 py-3 rounded-l-lg">
                  <div className="font-semibold text-xs" style={{ color: 'var(--color-foreground)' }}>{l.full_name}</div>
                  <div className="text-xs" style={{ color: '#94a3b8' }}>{l.email}</div>
                </td>
                <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-foreground)' }}>{l.company || '—'}</td>
                <td className="px-4 py-3">
                  <span className="text-xs font-bold px-2 py-0.5 rounded"
                    style={{ background: `${scoreColor(l.lead_score)}20`, color: scoreColor(l.lead_score) }}>
                    {l.lead_score}/100
                  </span>
                </td>
                <td className="px-4 py-3 text-xs capitalize" style={{ color: '#94a3b8' }}>{l.status}</td>
                <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-foreground)' }}>{l.budget_usd ? `$${l.budget_usd.toLocaleString()}` : '—'}</td>
                <td className="px-4 py-3 text-xs" style={{ color: '#94a3b8' }}>{new Date(l.created_at).toLocaleDateString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {activeTab === 'coupons' && !loading && (
        <div className="space-y-4">
          {coupons.map(c => (
            <div key={c.id} className="flex items-center justify-between p-4 rounded-xl"
              style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
              <div>
                <div className="text-sm font-bold" style={{ color: 'var(--color-foreground)' }}>{c.code}</div>
                <div className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                  {c.discount_percent}% off · {c.current_uses}/{c.max_uses} used · Expires {new Date(c.expires_at).toLocaleDateString()}
                </div>
              </div>
              <span className="text-xs px-2 py-1 rounded"
                style={{
                  background: new Date(c.expires_at) > new Date() ? 'rgba(44,140,102,0.15)' : 'rgba(205,66,59,0.15)',
                  color: new Date(c.expires_at) > new Date() ? '#2c8c66' : '#cd4239',
                }}>
                {new Date(c.expires_at) > new Date() ? 'Active' : 'Expired'}
              </span>
            </div>
          ))}
        </div>
      )}

      {showDealModal && (
        <DealModal
          onClose={() => setShowDealModal(false)}
          onSubmit={handleCreateDeal}
          leads={leads}
        />
      )}

      {editingDeal && (
        <DealModal
          deal={editingDeal}
          onClose={() => setEditingDeal(null)}
          onSubmit={(req) => handleUpdateDeal(editingDeal.id, req)}
          leads={leads}
        />
      )}

      {showCouponModal && (
        <CouponModal
          onClose={() => setShowCouponModal(false)}
          onSubmit={handleCreateCoupon}
        />
      )}
    </div>
  );
}

interface DealModalProps {
  deal?: SalesDeal;
  onClose: () => void;
  onSubmit: (req: CreateDealRequest) => void;
  leads: SalesLead[];
}

function DealModal({ deal, onClose, onSubmit, leads }: DealModalProps) {
  const [title, setTitle] = useState(deal?.title || '');
  const [leadId, setLeadId] = useState(deal?.lead_id || '');
  const [value, setValue] = useState(deal?.value_usd || 0);
  const [stage, setStage] = useState(deal?.pipeline_stage || 'discovery');
  const [probability, setProbability] = useState(deal?.probability || 0.2);

  const handleSubmit = () => {
    onSubmit({ title, lead_id: leadId, value_usd: value, pipeline_stage: stage, probability });
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
      <div className="bg-card rounded-xl max-w-md w-full p-6 border" style={{ borderColor: 'var(--color-border)' }}>
        <h2 className="text-lg font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>
          {deal ? 'Edit Deal' : 'New Deal'}
        </h2>
        <div className="space-y-4">
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Title</label>
            <input value={title} onChange={e => setTitle(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Lead</label>
            <select value={leadId} onChange={e => setLeadId(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}>
              <option value="">Select a lead</option>
              {leads.map(l => <option key={l.id} value={l.id}>{l.full_name}</option>)}
            </select>
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Value (USD)</label>
            <input type="number" value={value} onChange={e => setValue(parseFloat(e.target.value) || 0)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Stage</label>
            <select value={stage} onChange={e => setStage(e.target.value as DealStage)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}>
              {PIPELINE_STAGES.map(s => <option key={s.key} value={s.key}>{s.label}</option>)}
            </select>
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Probability (%)</label>
            <input type="number" value={probability * 100} onChange={e => setProbability(parseFloat(e.target.value) / 100 || 0)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
        </div>
        <div className="flex gap-2 mt-6">
          <button onClick={onClose} className="flex-1 px-4 py-2 rounded border text-sm"
            style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)', background: '#1e293b' }}>Cancel</button>
          <button onClick={handleSubmit} className="flex-1 px-4 py-2 rounded font-bold text-sm"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>Save</button>
        </div>
      </div>
    </div>
  );
}

interface CouponModalProps {
  onClose: () => void;
  onSubmit: (req: CreateCouponRequest) => void;
}

function CouponModal({ onClose, onSubmit }: CouponModalProps) {
  const [code, setCode] = useState('');
  const [discount, setDiscount] = useState(15);
  const [maxUses, setMaxUses] = useState(500);
  const [expiresAt, setExpiresAt] = useState('');

  const handleSubmit = () => {
    onSubmit({ code, discount_percent: discount, max_uses: maxUses, expires_at: expiresAt });
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
      <div className="bg-card rounded-xl max-w-md w-full p-6 border" style={{ borderColor: 'var(--color-border)' }}>
        <h2 className="text-lg font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>New Coupon</h2>
        <div className="space-y-4">
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Code</label>
            <input value={code} onChange={e => setCode(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Discount (%)</label>
            <input type="number" value={discount} onChange={e => setDiscount(parseFloat(e.target.value) || 0)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Max Uses</label>
            <input type="number" value={maxUses} onChange={e => setMaxUses(parseInt(e.target.value) || 0)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Expires At</label>
            <input type="datetime-local" value={expiresAt} onChange={e => setExpiresAt(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
        </div>
        <div className="flex gap-2 mt-6">
          <button onClick={onClose} className="flex-1 px-4 py-2 rounded border text-sm"
            style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)', background: '#1e293b' }}>Cancel</button>
          <button onClick={handleSubmit} className="flex-1 px-4 py-2 rounded font-bold text-sm"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>Create</button>
        </div>
      </div>
    </div>
  );
}
