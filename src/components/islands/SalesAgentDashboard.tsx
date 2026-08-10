import React, { useState, useEffect } from 'react';
import { apiClient, type SalesLead, type ProductRecommendation, type SalesBooking } from '../../lib/api-client';

export default function SalesAgentDashboard() {
  const [activeTab, setActiveTab] = useState<'recommendations' | 'leads' | 'bookings'>('recommendations');
  const [leads, setLeads] = useState<SalesLead[]>([]);
  const [recommendations, setRecommendations] = useState<ProductRecommendation[]>([]);
  const [bookings, setBookings] = useState<SalesBooking[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState('Enterprise AI');
  const [showNewLeadModal, setShowNewLeadModal] = useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    setLoading(true);
    const [leadsData, recData, bookingsData] = await Promise.all([
      apiClient.getSalesLeads(),
      apiClient.getSalesRecommendations(selectedCategory),
      apiClient.getSalesBookings(),
    ]);
    setLeads(leadsData);
    setRecommendations(recData);
    setBookings(bookingsData);
    setLoading(false);
  };

  const handleCategoryChange = async (category: string) => {
    setSelectedCategory(category);
    const recData = await apiClient.getSalesRecommendations(category);
    setRecommendations(recData);
  };

  const handleCreateLead = async (req: {
    email: string;
    full_name: string;
    company?: string;
    phone?: string;
    budget_usd?: number;
    timeline?: string;
  }) => {
    const result = await apiClient.createSalesLead(req);
    if (result) {
      setLeads([result, ...leads]);
      setShowNewLeadModal(false);
    }
  };

  const scoreColor = (s: number) => s >= 80 ? '#2c8c66' : s >= 60 ? '#f7a501' : '#cd4239';

  const qualifiedLeads = leads.filter(l => l.status === 'qualified' || l.lead_score >= 70);
  const totalBookings = bookings.length;
  const upcomingBookings = bookings.filter(b => new Date(b.start_time) > new Date()).length;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Sales Agent Dashboard</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Lead qualification, AI recommendations & calendar bookings</p>
        </div>
        <button
          onClick={() => setShowNewLeadModal(true)}
          className="px-4 py-2 text-xs font-semibold rounded-lg"
          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
        >
          + New Lead
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Leads</div>
          <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-primary)' }}>{leads.length}</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Qualified Leads</div>
          <div className="text-2xl font-bold mt-1" style={{ color: '#2c8c66' }}>{qualifiedLeads.length}</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Product Recommendations</div>
          <div className="text-2xl font-bold mt-1" style={{ color: 'var(--color-primary)' }}>{recommendations.length}</div>
        </div>
        <div className="p-4 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Upcoming Bookings</div>
          <div className="text-2xl font-bold mt-1" style={{ color: '#7c44a6' }}>{upcomingBookings}</div>
        </div>
      </div>

      <div className="border-b" style={{ borderColor: 'var(--color-border)' }}>
        <div className="flex gap-6">
          <button
            onClick={() => setActiveTab('recommendations')}
            className={`pb-3 px-1 text-sm font-medium transition-colors ${
              activeTab === 'recommendations' ? 'border-b-2' : ''
            }`}
            style={{
              borderColor: activeTab === 'recommendations' ? 'var(--color-primary)' : 'transparent',
              color: activeTab === 'recommendations' ? 'var(--color-primary)' : 'var(--color-muted-foreground)',
            }}
          >
            AI Recommendations
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
            My Leads
          </button>
          <button
            onClick={() => setActiveTab('bookings')}
            className={`pb-3 px-1 text-sm font-medium transition-colors ${
              activeTab === 'bookings' ? 'border-b-2' : ''
            }`}
            style={{
              borderColor: activeTab === 'bookings' ? 'var(--color-primary)' : 'transparent',
              color: activeTab === 'bookings' ? 'var(--color-primary)' : 'var(--color-muted-foreground)',
            }}
          >
            Bookings
          </button>
        </div>
      </div>

      {loading ? (
        <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>Loading...</div>
      ) : null}

      {activeTab === 'recommendations' && !loading && (
        <div className="space-y-4">
          <div className="flex gap-3">
            {['Enterprise AI', 'Support AI', 'Analytics'].map(cat => (
              <button
                key={cat}
                onClick={() => handleCategoryChange(cat)}
                className="px-3 py-1.5 text-xs rounded"
                style={{
                  background: selectedCategory === cat ? 'var(--color-primary)' : 'rgba(247,165,1,0.1)',
                  color: selectedCategory === cat ? 'var(--color-on-primary)' : '#f7a501',
                }}
              >
                {cat}
              </button>
            ))}
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {recommendations.map(rec => (
              <div key={rec.product_id} className="p-4 rounded-xl"
                style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
                <div className="flex items-start justify-between mb-2">
                  <div>
                    <div className="text-sm font-bold" style={{ color: 'var(--color-foreground)' }}>{rec.name}</div>
                    <div className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>{rec.sku}</div>
                  </div>
                  <div className="text-sm font-bold" style={{ color: 'var(--color-primary)' }}>
                    ${rec.price_usd.toLocaleString()}
                  </div>
                </div>
                <p className="text-xs mb-2" style={{ color: 'var(--color-muted-foreground)' }}>{rec.recommendation_reason}</p>
                {rec.upsell_discount_offer && (
                  <div className="text-xs px-2 py-1 rounded"
                    style={{ background: 'rgba(44,140,102,0.15)', color: '#2c8c66' }}>
                    {rec.upsell_discount_offer}
                  </div>
                )}
              </div>
            ))}
          </div>
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

      {activeTab === 'bookings' && !loading && (
        <div className="space-y-3">
          {bookings.map(b => (
            <div key={b.id} className="flex items-center justify-between p-4 rounded-xl"
              style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
              <div>
                <div className="text-sm font-semibold" style={{ color: 'var(--color-foreground)' }}>{b.meeting_title}</div>
                <div className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                  Lead #{b.lead_id.slice(0, 8)} · {new Date(b.start_time).toLocaleString()}
                </div>
              </div>
              <a
                href={b.meeting_link}
                className="text-xs px-3 py-1.5 rounded"
                style={{ background: 'rgba(44,140,102,0.15)', color: '#2c8c66' }}
              >
                Join Meeting
              </a>
            </div>
          ))}
          {bookings.length === 0 && (
            <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
              No bookings yet
            </div>
          )}
        </div>
      )}

      {showNewLeadModal && (
        <NewLeadModal
          onClose={() => setShowNewLeadModal(false)}
          onSubmit={handleCreateLead}
        />
      )}
    </div>
  );
}

interface NewLeadModalProps {
  onClose: () => void;
  onSubmit: (req: { email: string; full_name: string; company?: string; phone?: string; budget_usd?: number; timeline?: string }) => void;
}

function NewLeadModal({ onClose, onSubmit }: NewLeadModalProps) {
  const [email, setEmail] = useState('');
  const [fullName, setFullName] = useState('');
  const [company, setCompany] = useState('');
  const [phone, setPhone] = useState('');
  const [budget, setBudget] = useState('');
  const [timeline, setTimeline] = useState('exploring');

  const handleSubmit = () => {
    if (!email || !fullName) return;
    onSubmit({
      email,
      full_name: fullName,
      company: company || undefined,
      phone: phone || undefined,
      budget_usd: budget ? parseFloat(budget) : undefined,
      timeline,
    });
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
      <div className="bg-card rounded-xl max-w-md w-full p-6 border" style={{ borderColor: 'var(--color-border)' }}>
        <h2 className="text-lg font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>New Lead</h2>
        <div className="space-y-4">
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Email *</label>
            <input type="email" value={email} onChange={e => setEmail(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Full Name *</label>
            <input value={fullName} onChange={e => setFullName(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Company</label>
            <input value={company} onChange={e => setCompany(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Phone</label>
            <input value={phone} onChange={e => setPhone(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Budget (USD)</label>
            <input type="number" value={budget} onChange={e => setBudget(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }} />
          </div>
          <div>
            <label className="text-xs uppercase" style={{ color: 'var(--color-muted-foreground)' }}>Timeline</label>
            <select value={timeline} onChange={e => setTimeline(e.target.value)}
              className="mt-1 w-full px-3 py-2 rounded border text-sm"
              style={{ background: '#1e293b', borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}>
              <option value="immediate">Immediate</option>
              <option value="this_quarter">This Quarter</option>
              <option value="exploring">Exploring</option>
            </select>
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
