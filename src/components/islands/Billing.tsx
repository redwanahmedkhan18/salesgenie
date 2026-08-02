import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { apiClient } from '../../lib/api-client';
import type { PlatformRole } from '../../lib/types';

interface BillingPlan {
  plan_key: string;
  name: string;
  price_usd: number;
  max_seats: number;
  monthly_token_quota: number;
}

interface Subscription {
  subscription_id: string;
  tenant_id: string;
  plan: string;
  price_usd: number;
  max_seats: number;
  current_period_end: string;
  status: string;
}

interface Invoice {
  invoice_id: string;
  amount_due_usd: number;
  status: string;
  created_at: string;
  invoice_url: string;
}

interface Usage {
  current_tokens_used: number;
  monthly_token_quota: number;
  usage_percent: number;
  estimated_cost_usd: number;
}

interface PaymentReceipt {
  invoice_id: string;
  amount_usd: number;
  plan_name: string;
  status: string;
  pdf_url: string;
}

export default function Billing() {
  const [activeTab, setActiveTab] = useState<'plans' | 'subscription' | 'invoices' | 'usage'>('plans');
  const [plans, setPlans] = useState<BillingPlan[]>([]);
  const [subscription, setSubscription] = useState<Subscription | null>(null);
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [usage, setUsage] = useState<Usage | null>(null);
  const [selectedPlan, setSelectedPlan] = useState<string>('growth');
  const [loading, setLoading] = useState(true);
  const [generatingReceipt, setGeneratingReceipt] = useState(false);
  const [authError, setAuthError] = useState(false);

  useEffect(() => {
    loadPlans();
    loadSubscription();
    loadInvoices();
    loadUsage();
  }, []);

  const loadPlans = async () => {
    try {
      const data = await apiClient.listBillingPlans();
      setPlans(data || []);
    } catch (error) {
      console.error('Failed to load plans:', error);
    }
  };

  const loadSubscription = async () => {
    try {
      const response = await fetch('/billing/subscriptions', {
        headers: { 'Content-Type': 'application/json' }
      });
      if (response.ok) {
        const data = await response.json();
        setSubscription(data);
      }
    } catch (error) {
      console.error('Failed to load subscription:', error);
      if ((error as any).message?.includes('401') || (error as any).message?.includes('403')) {
        setAuthError(true);
      }
    }
  };

  const loadInvoices = async () => {
    try {
      const data = await apiClient.listInvoices();
      setInvoices(data || []);
    } catch (error) {
      console.error('Failed to load invoices:', error);
    }
  };

  const loadUsage = async () => {
    try {
      const data = await apiClient.getBillingUsage(2480000, 'growth');
      setUsage(data);
    } catch (error) {
      console.error('Failed to load usage:', error);
    }
  };

  const handleSubscribe = async (plan: string) => {
    setLoading(true);
    try {
      const response = await apiClient.createSubscription(plan);
      if (response) {
        setSubscription({
          subscription_id: response.subscription_id,
          tenant_id: response.tenant_id,
          plan: response.plan,
          price_usd: response.price_usd,
          max_seats: response.max_seats,
          current_period_end: response.current_period_end,
          status: response.status,
        });
        await loadInvoices();
        await generatePaymentReceipt(response.subscription_id);
      }
    } catch (error) {
      console.error('Failed to subscribe:', error);
    } finally {
      setLoading(false);
    }
  };

  const generatePaymentReceipt = async (subscriptionId: string) => {
    setGeneratingReceipt(true);
    try {
      const response = await fetch('/billing/payments/receipt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          amount_usd: subscription?.price_usd || 149,
          description: `${subscription?.plan || 'Growth'} Plan Payment`,
        })
      });
      
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `receipt-${subscriptionId}.pdf`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
      }
    } catch (error) {
      console.error('Failed to generate receipt:', error);
    } finally {
      setGeneratingReceipt(false);
    }
  };

  const downloadInvoice = async (invoiceId: string) => {
    try {
      const response = await fetch(`/billing/invoices/${invoiceId}/pdf`, {
        headers: { 'Accept': 'application/pdf' }
      });
      
      if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `invoice-${invoiceId}.pdf`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
      }
    } catch (error) {
      console.error('Failed to download invoice:', error);
    }
  };

  if (authError) {
    return (
      <div className="flex h-screen items-center justify-center" style={{ background: 'var(--color-background)' }}>
        <div className="text-center p-8" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-4xl mb-4">🔐</div>
          <h2 className="text-xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>Authentication Required</h2>
          <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
            Please log in to access billing features.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute="billing" onRouteChange={() => {}} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-10 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>Billing & Subscription</h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Manage your plan, invoices, and usage</p>
          </div>
        </header>

        <div className="px-6 py-6">
          <nav className="flex space-x-2 mb-6" role="tablist">
            {(['plans', 'subscription', 'invoices', 'usage'] as any[]).map(tab => (
              <button
                key={tab}
                onClick={() => setActiveTab(tab as any)}
                className={`px-4 py-2 text-sm font-medium rounded-lg transition-colors ${
                  activeTab === tab
                    ? 'bg-primary/10 text-primary'
                    : 'bg-white/5 text-muted-foreground hover:bg-white/10'
                }`}
                style={{ color: 'var(--color-foreground)' }}
              >
                {tab.charAt(0).toUpperCase() + tab.slice(1)}
              </button>
            ))}
          </nav>

          {activeTab === 'plans' && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {plans.length === 0 ? (
                <div className="col-span-3 text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
                  Loading plans...
                </div>
              ) : (
                plans.map(plan => (
                  <div key={plan.plan_key} className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="text-2xl mb-2">{plan.icon || '💼'}</div>
                    <h3 className="font-bold text-lg mb-2" style={{ color: 'var(--color-foreground)' }}>{plan.name}</h3>
                    <p className="text-sm mb-4" style={{ color: 'var(--color-muted-foreground)' }}>${plan.price_usd}/mo</p>
                    <ul className="text-xs mb-4 space-y-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      <li>✓ {plan.max_seats === -1 ? 'Unlimited' : `${plan.max_seats} seats`}</li>
                      <li>✓ {plan.monthly_token_quota.toLocaleString()} AI tokens</li>
                    </ul>
                    <button
                      onClick={() => handleSubscribe(plan.plan_key)}
                      disabled={loading}
                      className="w-full px-4 py-2 rounded-lg font-semibold text-sm transition-colors"
                      style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                    >
                      {loading ? 'Processing...' : 'Select Plan'}
                    </button>
                  </div>
                ))
              )}
            </div>
          )}

          {activeTab === 'subscription' && subscription && (
            <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <h2 className="text-lg font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>Current Subscription</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label className="text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Plan</label>
                  <div className="text-lg font-bold" style={{ color: 'var(--color-foreground)' }}>{subscription.plan}</div>
                </div>
                <div>
                  <label className="text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</label>
                  <span className={`px-2 py-1 rounded-full text-xs ${
                    subscription.status === 'active' ? 'bg-green-500/15 text-green-400' : 'bg-red-500/15 text-red-400'
                  }`}>
                    {subscription.status}
                  </span>
                </div>
                <div>
                  <label className="text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Price</label>
                  <div className="text-lg font-bold" style={{ color: 'var(--color-foreground)' }}>
                    ${subscription.price_usd}/mo
                  </div>
                </div>
                <div>
                  <label className="text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Period End</label>
                  <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>
                    {new Date(subscription.current_period_end).toLocaleDateString()}
                  </div>
                </div>
              </div>
              
              <div className="mt-6">
                <button
                  onClick={() => generatePaymentReceipt(subscription.subscription_id)}
                  disabled={generatingReceipt}
                  className="px-4 py-2 rounded-lg font-semibold text-sm transition-colors mr-2"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                >
                  {generatingReceipt ? 'Generating...' : 'Generate PDF Receipt'}
                </button>
                <button
                  onClick={() => handleSubscribe(selectedPlan)}
                  disabled={loading}
                  className="px-4 py-2 rounded-lg font-semibold text-sm transition-colors"
                  style={{ background: 'var(--color-secondary)', color: 'var(--color-on-secondary)' }}
                >
                  Change Plan
                </button>
              </div>
            </div>
          )}

          {activeTab === 'invoices' && (
            <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="p-4 border-b" style={{ borderColor: 'var(--color-border)' }}>
                <h2 className="font-semibold" style={{ color: 'var(--color-foreground)' }}>Invoices</h2>
              </div>
              <div className="p-4">
                {invoices.length === 0 ? (
                  <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
                    No invoices found
                  </div>
                ) : (
                  <table className="w-full">
                    <thead>
                      <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <th className="text-left px-3 py-2 text-sm font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Invoice ID</th>
                        <th className="text-left px-3 py-2 text-sm font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Amount</th>
                        <th className="text-left px-3 py-2 text-sm font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                        <th className="text-left px-3 py-2 text-sm font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Date</th>
                        <th className="text-left px-3 py-2 text-sm font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {invoices.map(invoice => (
                        <tr key={invoice.invoice_id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                          <td className="px-3 py-2 text-sm" style={{ color: 'var(--color-foreground)' }}>{invoice.invoice_id}</td>
                          <td className="px-3 py-2 text-sm font-semibold" style={{ color: 'var(--color-foreground)' }}>${invoice.amount_due_usd}</td>
                          <td className="px-3 py-2 text-sm">
                            <span className={`px-2 py-1 rounded-full text-xs ${
                              invoice.status === 'paid' ? 'bg-green-500/15 text-green-400' : 'bg-amber-500/15 text-amber-400'
                            }`}>
                              {invoice.status}
                            </span>
                          </td>
                          <td className="px-3 py-2 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                            {new Date(invoice.created_at).toLocaleDateString()}
                          </td>
                          <td className="px-3 py-2 text-sm">
                            <button
                              onClick={() => downloadInvoice(invoice.invoice_id)}
                              className="px-2 py-1 text-xs rounded"
                              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                            >
                              PDF
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                )}
              </div>
            </div>
          )}

          {activeTab === 'usage' && usage && (
            <div className="space-y-6">
              <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h2 className="text-lg font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>Token Usage</h2>
                <div className="space-y-4">
                  <div>
                    <div className="flex justify-between text-sm mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      <span>{usage.current_tokens_used.toLocaleString()} / {usage.monthly_token_quota.toLocaleString()} tokens</span>
                      <span>{usage.usage_percent.toFixed(1)}%</span>
                    </div>
                    <div className="h-2 rounded-full" style={{ background: 'var(--color-border)' }}>
                      <div 
                        className="h-full rounded-full transition-all"
                        style={{ 
                          width: `${Math.min(usage.usage_percent, 100)}%`, 
                          background: usage.usage_percent > 90 ? '#cd4239' : usage.usage_percent > 70 ? '#f7a501' : '#2c8c66'
                        }}
                      />
                    </div>
                  </div>
                </div>
              </div>

              <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <h2 className="text-lg font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>Estimated Cost</h2>
                <div className="text-3xl font-bold" style={{ color: 'var(--color-foreground)' }}>
                  ${usage.estimated_cost_usd.toFixed(2)}
                </div>
                <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Based on current usage at $0.60 per 1M tokens
                </p>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

function formatDate(date: string) {
  return new Date(date).toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'short', 
    day: 'numeric' 
  });
}