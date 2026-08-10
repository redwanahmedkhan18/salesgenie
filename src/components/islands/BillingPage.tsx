import React, { useState, useEffect } from 'react';
import { Calendar, CreditCard, Download, RefreshCw, AlertCircle, CheckCircle, Clock } from 'lucide-react';
import { apiClient, BILLING_SERVICE_URL } from '../../lib/api-client';
import { getToken, secureTokenStorage } from '../../lib/secure-storage';
import { format } from 'date-fns';

interface Plan {
  id: string;
  name: string;
  interval: 'monthly' | 'yearly';
  price_usd: number;
  max_seats: number;
  monthly_token_quota: number;
  features: Record<string, boolean>;
}

interface Subscription {
  subscription_id: string;
  plan_id: string;
  plan_name: string;
  status: 'active' | 'trial' | 'canceled' | 'past_due' | 'incomplete';
  current_period_start: string;
  current_period_end: string;
  cancel_at_period_end: boolean;
  trial_ends_at: string | null;
}

interface Invoice {
  invoice_id: string;
  amount_due_usd: number;
  status: 'paid' | 'unpaid' | 'pending';
  created_at: string;
  invoice_url: string;
}

interface Usage {
  current_tokens_used: number;
  monthly_token_quota: number;
  usage_percent: number;
  is_at_risk: boolean;
  estimated_cost_usd?: number;
  plan?: string;
}

export default function BillingPage() {
  const [activeTab, setActiveTab] = useState<'plans' | 'subscription' | 'history' | 'usage'>('plans');
  const [plans, setPlans] = useState<Plan[]>([]);
  const [subscription, setSubscription] = useState<Subscription | null>(null);
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [usage, setUsage] = useState<Usage | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadPlans();
    loadSubscription();
    loadInvoices();
    loadUsage();
  }, []);

  const loadPlans = async () => {
    try {
      const controller = new AbortController();
      setTimeout(() => controller.abort(), 10000);
      const response = await fetch(`${BILLING_SERVICE_URL}/api/v1/billing/plans`, {
        signal: controller.signal
      });
      if (response.ok) {
        const data = await response.json();
        const mappedPlans: Plan[] = data.map((p: any) => ({
          id: p.plan_key,
          name: p.name,
          interval: 'monthly' as const,
          price_usd: p.price_usd,
          max_seats: p.max_seats,
          monthly_token_quota: p.monthly_token_quota,
          features: {},
        }));
        setPlans(mappedPlans);
      }
    } catch (err) {
      console.error('Failed to load plans:', err);
      setError('Failed to load plans. Backend service unavailable.');
    } finally {
      setLoading(false);
    }
  };

  const loadSubscription = async () => {
    try {
      const token = getToken();
      if (!token) {
        setLoading(false);
        return;
      }
      const controller = new AbortController();
      setTimeout(() => controller.abort(), 10000);
      const response = await fetch(`${BILLING_SERVICE_URL}/api/v1/billing/subscriptions`, {
        headers: { 'Authorization': `Bearer ${token}` },
        signal: controller.signal
      });
      if (response.ok) {
        const data = await response.json();
        setSubscription(data);
      }
    } catch (err) {
      console.error('Failed to load subscription:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadInvoices = async () => {
    try {
      const token = getToken();
      if (!token) {
        setLoading(false);
        return;
      }
      const controller = new AbortController();
      setTimeout(() => controller.abort(), 10000);
      const response = await fetch(`${BILLING_SERVICE_URL}/api/v1/billing/invoices`, {
        headers: { 'Authorization': `Bearer ${token}` },
        signal: controller.signal
      });
      if (response.ok) {
        const data = await response.json();
        const mappedInvoices: Invoice[] = data.map((i: any) => ({
          invoice_id: i.invoice_id || i.subscription_id + '-' + Date.now(),
          amount_due_usd: i.amount_usd || 0,
          status: (i.status || 'paid') as 'paid' | 'unpaid' | 'pending',
          created_at: i.created_at || new Date().toISOString(),
          invoice_url: i.invoice_url || '',
        }));
        setInvoices(mappedInvoices);
      }
    } catch (err) {
      console.error('Failed to load invoices:', err);
      setError('Failed to load invoices. Backend service unavailable.');
    } finally {
      setLoading(false);
    }
  };

  const loadUsage = async () => {
    try {
      const token = getToken();
      if (!token) {
        setLoading(false);
        return;
      }
      const controller = new AbortController();
      setTimeout(() => controller.abort(), 10000);
      const response = await fetch(`${BILLING_SERVICE_URL}/api/v1/billing/usage?plan=${subscription?.plan_id || 'growth'}`, {
        headers: { 'Authorization': `Bearer ${token}` },
        signal: controller.signal
      });
      if (response.ok) {
        const data = await response.json();
        if (data) {
          setUsage({
            current_tokens_used: data.current_tokens_used,
            monthly_token_quota: data.quota,
            usage_percent: data.percentage_used,
            is_at_risk: data.percentage_used > 80,
            estimated_cost_usd: data.estimated_cost_usd,
            plan: data.plan,
          });
        }
      }
    } catch (err) {
      console.error('Failed to load usage:', err);
      setError('Billing backend unavailable. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  const handleTrialExpired = async () => {
    if (!subscription) return;
    try {
      setSubscription({ ...subscription, status: 'canceled', plan_id: 'free' } as Subscription);
      secureTokenStorage.removeItem('auth_token');
      secureTokenStorage.removeItem('user_data');
    } catch (err) {
      console.error('Trial expired handling failed:', err);
    }
  };

  const downloadInvoice = async (invoiceId: string) => {
    const blob = await apiClient.downloadInvoicePdf(invoiceId);
    if (blob) {
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `invoice-${invoiceId}.pdf`;
      a.click();
      URL.revokeObjectURL(url);
    }
  };

  const upgradePlan = async (newPlanId: string) => {
    if (!subscription) return;
    try {
      const result = await apiClient.createSubscription(newPlanId);
      if (result) {
        setSubscription({ ...subscription, plan_id: newPlanId, status: 'active' });
      }
    } catch (err) {
      setError('Failed to upgrade plan');
    }
  };

  const cancelSubscription = async (subscriptionId: string) => {
    if (!subscriptionId) return;
    try {
      setSubscription(prev => prev ? { ...prev, status: 'canceled' } : null);
    } catch (err) {
      console.error('Cancel subscription failed:', err);
      setError('Failed to cancel subscription');
    }
  };

  const formatTokens = (tokens: number): string => {
    if (tokens >= 1_000_000) return `${(tokens / 1_000_000).toFixed(1)}M tokens`;
    if (tokens >= 1_000) return `${(tokens / 1_000).toFixed(0)}K tokens`;
    return `${tokens} tokens`;
  };

  const getTokensRemaining = (): number => {
    if (!usage) return 0;
    return usage.monthly_token_quota - usage.current_tokens_used;
  };

  if (loading) {
    return <div className="flex items-center justify-center min-h-screen">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b border-border bg-card px-6 py-4">
        <h1 className="text-2xl font-bold text-foreground">Billing & Subscription</h1>
        <p className="text-sm text-muted-foreground">Manage your plan, invoices, and usage</p>
      </header>

      <nav className="flex overflow-x-auto border-b border-border bg-card px-6 py-2">
        {(['plans', 'subscription', 'history', 'usage'] as const).map(tab => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`flex-1 min-w-[120px] px-4 py-2 text-sm font-medium rounded-t-lg transition-colors ${
              activeTab === tab
                ? 'bg-primary/10 text-primary border-b-2 border-primary'
                : 'text-muted-foreground hover:text-foreground hover:bg-secondary'
            }`}
          >
            {tab.charAt(0).toUpperCase() + tab.slice(1)}
          </button>
        ))}
      </nav>

      <main className="p-6">
        {activeTab === 'plans' && (
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {plans.length === 0 ? (
              <div className="col-span-3 text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
                Loading plans...
              </div>
            ) : (
              plans.map(plan => (
                <div key={plan.id} className="rounded-lg border border-border bg-card p-6">
                  <h3 className="text-lg font-semibold text-foreground">{plan.name}</h3>
                  <p className="text-2xl font-bold text-foreground my-2">${plan.price_usd}{plan.interval === 'yearly' ? '/yr' : '/mo'}</p>
                  <p className="text-sm text-muted-foreground my-2">{plan.max_seats === -1 ? 'Unlimited' : `${plan.max_seats} seats`}</p>
                  <p className="text-sm text-muted-foreground my-2">{formatTokens(plan.monthly_token_quota)} tokens/month</p>
                  {subscription?.plan_id !== plan.id && (
                    <button
                      onClick={() => upgradePlan(plan.id)}
                      className="w-full px-4 py-2 rounded-lg font-semibold text-sm transition-colors"
                      style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                    >
                      Select Plan
                    </button>
                  )}
                </div>
              ))
            )}
          </div>
        )}

        {activeTab === 'subscription' && subscription && (
          <div className="rounded-lg border border-border bg-card p-6">
            <h2 className="text-xl font-semibold text-foreground mb-4">Current Subscription</h2>
            <div className="grid gap-6 md:grid-cols-2">
              <div>
                <label className="text-xs font-semibold text-muted-foreground">Plan</label>
                <p className="text-lg font-semibold text-foreground">{subscription.plan_name}</p>
              </div>
              <div>
                <label className="text-xs font-semibold text-muted-foreground">Status</label>
                <span className={`px-2 py-1 text-xs font-semibold rounded-full ${
                  subscription.status === 'active' ? 'bg-green-500/15 text-green-600' :
                  subscription.status === 'trial' ? 'bg-amber-500/15 text-amber-600' :
                  'bg-red-500/15 text-red-600'
                }`}>
                  {subscription.status}
                </span>
              </div>
              <div>
                <label className="text-xs font-semibold text-muted-foreground">Price</label>
                <p className="text-lg font-semibold text-foreground">${subscription.plan_name ? '149' : 0}/mo</p>
              </div>
              <div>
                <label className="text-xs font-semibold text-muted-foreground">Period End</label>
                <p className="text-foreground">
                  {subscription.current_period_end ? format(new Date(subscription.current_period_end), 'MMM d, yyyy') : 'N/A'}
                </p>
              </div>
            </div>
            <div className="mt-6 flex gap-3">
              <button
                onClick={() => subscription && cancelSubscription(subscription.subscription_id)}
                className="px-4 py-2 rounded-lg font-semibold text-sm transition-colors"
                style={{ background: 'var(--color-secondary)', color: 'var(--color-on-secondary)' }}
              >
                Cancel Subscription
              </button>
            </div>
          </div>
        )}

        {activeTab === 'history' && (
          <div className="rounded-lg border border-border bg-card">
            <div className="p-4 border-b border-border">
              <h2 className="text-lg font-semibold text-foreground">Billing History</h2>
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
                      <th className="text-right px-3 py-2 text-sm font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Amount</th>
                      <th className="text-left px-3 py-2 text-sm font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {invoices.map(invoice => (
                      <tr key={invoice.invoice_id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td className="px-3 py-2 text-sm" style={{ color: 'var(--color-foreground)' }}>{invoice.invoice_id}</td>
                        <td className="px-3 py-2 text-sm font-semibold" style={{ color: 'var(--color-foreground)' }}>${invoice.amount_due_usd.toFixed(2)}</td>
                        <td className="px-3 py-2 text-sm">
                          <span className={`px-2 py-1 rounded-full text-xs ${
                            invoice.status === 'paid' ? 'bg-green-500/15 text-green-400' : 'bg-amber-500/15 text-amber-400'
                          }`}>
                            {invoice.status}
                          </span>
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
                ${usage.estimated_cost_usd ? usage.estimated_cost_usd.toFixed(2) : '0.00'}
              </div>
              <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
                Based on current usage at $0.60 per 1M tokens
              </p>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}