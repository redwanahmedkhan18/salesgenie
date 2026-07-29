import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { apiClient } from '../../lib/api-client';
import type { Customer, CustomerSegment, CustomerTag } from '../../lib/api-client';

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
    cold: 'bg-gray-500/15 text-gray-400',
    warm: 'bg-blue-500/15 text-blue-400',
    hot: 'bg-orange-500/15 text-orange-400',
    qualified: 'bg-purple-500/15 text-purple-400',
    converted: 'bg-green-500/15 text-green-400',
    churned: 'bg-red-500/15 text-red-400',
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Customer Management
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              {customers.length} customers · Segments: {segments.length} · Tags: {tags.length}
            </p>
          </div>
          <div className="flex items-center gap-3">
            <button
              onClick={() => setShowModal(true)}
              className="px-4 py-2 text-sm font-semibold rounded-lg transition-all"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              + Add Customer
            </button>
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
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            />
            
            <select
              value={filterStatus || ''}
              onChange={(e) => setFilterStatus(e.target.value || null)}
              className="px-3 py-2 rounded-lg text-sm outline-none"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
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
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            >
              <option value="">All Segments</option>
              {segments.map(seg => (
                <option key={seg.id} value={seg.name}>{seg.name}</option>
              ))}
            </select>
          </div>

          {/* Customer Table */}
          <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Customer</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Company</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Score</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>LTV</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Segments</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Last Interaction</th>
                  </tr>
                </thead>
                <tbody>
                  {loading ? (
                    <tr>
                      <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                        Loading customers...
                      </td>
                    </tr>
                  ) : filteredCustomers.length === 0 ? (
                    <tr>
                      <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                        No customers found
                      </td>
                    </tr>
                  ) : (
                    filteredCustomers.map(customer => (
                      <tr
                        key={customer.id}
                        onClick={() => setSelectedCustomer(customer)}
                        className="cursor-pointer transition-colors"
                        style={{ borderBottom: '1px solid var(--color-border)' }}
                      >
                        <td className="px-4 py-3">
                          <div className="flex items-center gap-3">
                            <div className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold"
                              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                              {customer.full_name.charAt(0)}
                            </div>
                            <div>
                              <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>
                                {customer.full_name}
                              </div>
                              <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                                {customer.email || customer.phone_number || 'No contact info'}
                              </div>
                            </div>
                          </div>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                          {customer.company_name || '-'}
                        </td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full ${leadStatusColors[customer.lead_status] || leadStatusColors.cold}`}>
                            {customer.lead_status}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                          {customer.lead_score}
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                          ${customer.lifetime_value.toLocaleString()}
                        </td>
                        <td className="px-4 py-3">
                          <div className="flex flex-wrap gap-1">
                            {customer.segments.slice(0, 2).map(seg => (
                              <span key={seg} className="text-xs px-2 py-0.5 rounded"
                                style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}>
                                {seg}
                              </span>
                            ))}
                            {customer.segments.length > 2 && (
                              <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                                +{customer.segments.length - 2}
                              </span>
                            )}
                          </div>
                        </td>
                        <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
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
          <div className="rounded-xl p-6 w-full max-w-md" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <h2 className="text-lg font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Add New Customer</h2>
            <form onSubmit={handleCreateCustomer} className="space-y-4">
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Full Name *
                </label>
                <input
                  name="full_name"
                  required
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Email
                </label>
                <input
                  name="email"
                  type="email"
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Phone Number
                </label>
                <input
                  name="phone_number"
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Company Name
                </label>
                <input
                  name="company_name"
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div className="flex justify-end gap-3 pt-4">
                <button
                  type="button"
                  onClick={() => setShowModal(false)}
                  className="px-4 py-2 text-sm rounded-lg transition-colors"
                  style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-sm font-semibold rounded-lg transition-all"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
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