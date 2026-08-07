import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { apiClient } from '../../lib/api-client';
import type { Customer, CustomerSegment, CustomerTag } from '../../lib/api-client';

const CARD_BG = '#1e293b';
const CARD_BORDER = '#334155';
const TEXT_COLOR = '#f8fafc';
const MUTED_COLOR = '#94a3b8';
const PRIMARY_COLOR = '#f7a501';
const ON_PRIMARY_COLOR = '#23251d';

export default function CustomerManagement() {
  const [activeRoute, setActiveRoute] = useState('customers');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [customers, setCustomers] = useState<Customer[]>([]);
  const [segments, setSegments] = useState<CustomerSegment[]>([]);
  const [tags, setTags] = useState<CustomerTag[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [filterStatus, setFilterStatus] = useState<string | null>(null);
  const [filterSegment, setFilterSegment] = useState<string | null>(null);
  const [selectedCustomer, setSelectedCustomer] = useState<Customer | null>(null);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const [custData, segData, tagData] = await Promise.all([
          apiClient.fetchCustomers(),
          apiClient.fetchSegments(),
          apiClient.fetchTags(),
        ]);
        setCustomers(custData);
        setSegments(segData);
        setTags(tagData);
      } catch (error) {
        console.error('Error loading customer data:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const filteredCustomers = customers.filter(c => {
    if (search && !c.full_name.toLowerCase().includes(search.toLowerCase()) &&
        !(c.email && c.email.toLowerCase().includes(search.toLowerCase()))) {
      return false;
    }
    if (filterStatus && c.lead_status !== filterStatus) {
      return false;
    }
    if (filterSegment && !c.segments.includes(filterSegment)) {
      return false;
    }
    return true;
  });

  const handleCreateCustomer = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const customer = await apiClient.createCustomer({
      full_name: formData.get('full_name') as string,
      email: formData.get('email') as string,
      phone_number: formData.get('phone_number') as string,
      company_name: formData.get('company_name') as string,
      lead_status: 'cold',
    });
    if (customer) {
      setCustomers([customer, ...customers]);
      setShowModal(false);
    }
  };

  const leadStatusColors: Record<string, string> = {
    cold: '#9b9c92', warm: '#2c84e0', hot: '#f7a501',
    qualified: '#7c44a6', converted: '#2c8c66', churned: '#cd4239',
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: '#0f1117' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: CARD_BG, borderColor: CARD_BORDER }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: TEXT_COLOR }}>
              Customer Management
            </h1>
            <p className="text-xs mt-0.5" style={{ color: MUTED_COLOR }}>
              {customers.length} customers · Segments: {segments.length} · Tags: {tags.length}
            </p>
          </div>
          <div className="flex items-center gap-3">
            <button
              onClick={() => setShowModal(true)}
              className="px-4 py-2 text-sm font-semibold rounded-lg transition-all"
              style={{ background: PRIMARY_COLOR, color: ON_PRIMARY_COLOR }}
            >
              + Add Customer
            </button>
            <button
              id="open-command-palette-btn"
              onClick={() => setPaletteOpen(true)}
              className="flex items-center gap-2 px-3 py-2 rounded-lg text-sm transition-colors"
              style={{ background: '#64748b', color: TEXT_COLOR, border: '1px solid #334155' }}
            >
              <span>🔍</span>
              <span>Search</span>
              <kbd className="text-xs">⌘K</kbd>
            </button>
          </div>
        </header>

        <div className="px-6 py-6 space-y-6">
          {/* Filters */}
          <div className="flex gap-4 items-center">
            <input
              type="text"
              placeholder="Search customers..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="px-3 py-2 rounded-lg text-sm outline-none"
              style={{ background: CARD_BG, color: TEXT_COLOR, border: '1px solid ' + CARD_BORDER }}
            />
            
            <select
              value={filterStatus || ''}
              onChange={(e) => setFilterStatus(e.target.value || null)}
              className="px-3 py-2 rounded-lg text-sm outline-none"
              style={{ background: CARD_BG, color: TEXT_COLOR, border: '1px solid ' + CARD_BORDER }}
            >
              <option value="">All Statuses</option>
              <option value="cold">Cold</option>
              <option value="warm">Warm</option>
              <option value="hot">Hot</option>
              <option value="qualified">Qualified</option>
              <option value="converted">Converted</option>
              <option value="churned">Churned</option>
            </select>

            <select
              value={filterSegment || ''}
              onChange={(e) => setFilterSegment(e.target.value || null)}
              className="px-3 py-2 rounded-lg text-sm outline-none"
              style={{ background: CARD_BG, color: TEXT_COLOR, border: '1px solid ' + CARD_BORDER }}
            >
              <option value="">All Segments</option>
              {segments.map(seg => (
                <option key={seg.id} value={seg.name}>{seg.name}</option>
              ))}
            </select>
          </div>

          {/* Customer Table */}
          <div className="rounded-xl border" style={{ background: CARD_BG, borderColor: CARD_BORDER }}>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr style={{ borderBottom: '1px solid ' + CARD_BORDER }}>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: MUTED_COLOR }}>Customer</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: MUTED_COLOR }}>Company</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: MUTED_COLOR }}>Status</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: MUTED_COLOR }}>Score</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: MUTED_COLOR }}>LTV</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: MUTED_COLOR }}>Segments</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: MUTED_COLOR }}>Last Interaction</th>
                  </tr>
                </thead>
                <tbody>
                  {loading ? (
                    <tr>
                      <td colSpan={7} className="px-4 py-8 text-center" style={{ color: MUTED_COLOR }}>
                        Loading customers...
                      </td>
                    </tr>
                  ) : filteredCustomers.length === 0 ? (
                    <tr>
                      <td colSpan={7} className="px-4 py-8 text-center" style={{ color: MUTED_COLOR }}>
                        No customers found
                      </td>
                    </tr>
                  ) : (
                    filteredCustomers.map(customer => (
                      <tr
                        key={customer.id}
                        onClick={() => setSelectedCustomer(customer)}
                        className="cursor-pointer transition-colors"
                        style={{ borderBottom: '1px solid ' + CARD_BORDER }}
                      >
                        <td className="px-4 py-3">
                          <div className="flex items-center gap-3">
                            <div className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold"
                              style={{ background: PRIMARY_COLOR, color: ON_PRIMARY_COLOR }}>
                              {customer.full_name.charAt(0)}
                            </div>
                            <div>
                              <div className="font-semibold text-sm" style={{ color: TEXT_COLOR }}>
                                {customer.full_name}
                              </div>
                              <div className="text-xs" style={{ color: MUTED_COLOR }}>
                                {customer.email || customer.phone_number || 'No contact info'}
                              </div>
                            </div>
                          </div>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: TEXT_COLOR }}>
                          {customer.company_name || '-'}
                        </td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full`}>
                            {customer.lead_status}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: TEXT_COLOR }}>
                          {customer.lead_score}
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: TEXT_COLOR }}>
                          ${customer.lifetime_value.toLocaleString()}
                        </td>
                        <td className="px-4 py-3">
                          <div className="flex flex-wrap gap-1">
                            {customer.segments.slice(0, 2).map(seg => (
                              <span key={seg} className="text-xs px-2 py-0.5 rounded"
                                style={{ background: '#64748b', color: TEXT_COLOR }}>
                                {seg}
                              </span>
                            ))}
                            {customer.segments.length > 2 && (
                              <span className="text-xs" style={{ color: MUTED_COLOR }}>
                                +{customer.segments.length - 2}
                              </span>
                            )}
                          </div>
                        </td>
                        <td className="px-4 py-3 text-xs" style={{ color: MUTED_COLOR }}>
                          {customer.last_interaction_at 
                            ? new Date(customer.last_interaction_at).toLocaleDateString()
                            : 'Never'}
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </main>

      {/* Create Customer Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="rounded-xl p-6 w-full max-w-md" style={{ background: CARD_BG, border: '1px solid ' + CARD_BORDER }}>
            <h2 className="text-lg font-bold mb-4" style={{ color: TEXT_COLOR }}>Add New Customer</h2>
            <form onSubmit={handleCreateCustomer} className="space-y-4">
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: MUTED_COLOR }}>
                  Full Name *
                </label>
                <input
                  name="full_name"
                  required
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: CARD_BG, color: TEXT_COLOR, border: '1px solid ' + CARD_BORDER }}
                />
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: MUTED_COLOR }}>
                  Email
                </label>
                <input
                  name="email"
                  type="email"
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: CARD_BG, color: TEXT_COLOR, border: '1px solid ' + CARD_BORDER }}
                />
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: MUTED_COLOR }}>
                  Phone Number
                </label>
                <input
                  name="phone_number"
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: CARD_BG, color: TEXT_COLOR, border: '1px solid ' + CARD_BORDER }}
                />
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: MUTED_COLOR }}>
                  Company Name
                </label>
                <input
                  name="company_name"
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: CARD_BG, color: TEXT_COLOR, border: '1px solid ' + CARD_BORDER }}
                />
              </div>
              <div className="flex justify-end gap-3 pt-4">
                <button
                  type="button"
                  onClick={() => setShowModal(false)}
                  className="px-4 py-2 text-sm rounded-lg transition-colors"
                  style={{ background: PRIMARY_COLOR, color: ON_PRIMARY_COLOR }}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-sm font-semibold rounded-lg transition-all"
                  style={{ background: PRIMARY_COLOR, color: ON_PRIMARY_COLOR }}
                >
                  Create Customer
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}