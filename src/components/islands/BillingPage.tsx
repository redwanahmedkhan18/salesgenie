import React, { useState, useEffect } from 'react';
import { Calendar, CreditCard, Download, RefreshCw, AlertCircle, CheckCircle, Clock } from 'lucide-react';
import { apiClient } from '../../lib/api-client';
import { useAuth } from '../../auth/AuthProvider';
import { format, addDays, isAfter, isBefore } from 'date-fns';

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
  amount_usd: number;
  status: 'paid' | 'unpaid' | 'pending';
  period_start: string;
  period_end: string;
  pdf_url?: string;
}

interface Usage {
  current_tokens_used: number;
  monthly_token_quota: number;
  usage_percent: number;
  is_at_risk: boolean;
}

export default function BillingPage() {
  const { hasRole } = useAuth();
  const [activeTab, setActiveTab] = useState<'plans' | 'subscription' | 'history' | 'usage'>('plans');
  const [plans, setPlans] = useState<Plan[]>([]);
  const [subscription, setSubscription] = useState<Subscription | null>(null);
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [usage, setUsage] = useState<Usage | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showUpgradeModal, setShowUpgradeModal] = useState(false);

  useEffect(() => {
    loadPlans();
    loadSubscription();
    loadInvoices();
    loadUsage();
    setInterval(checkSubscriptionStatus, 60000);
  }, []);

  const loadPlans = async () => {
    try {
      const data = await apiClient.listBillingPlans();
      setPlans(data || []);
    } catch (err) {
      setError('Failed to load plans');
    }
  };

  const loadSubscription = async () => {
    try {
      const response = await fetch('/api/v1/billing/subscriptions', {
        headers: { 'Authorization': `Bearer ${localStorage.getItem('auth_token')}` }
      });
      if (response.ok) {
        const data = await response.json();
        setSubscription(data);
      }
    } catch (err) {
      console.error('Failed to load subscription:', err);
    }
  };

  const loadInvoices = async () => {
    try {
      const data = await apiClient.listInvoices();
      setInvoices(data || []);
    } catch (err) {
      console.error('Failed to load invoices:', err);
    }
  };

  const loadUsage = async () => {
    try {
      const plan = subscription?.plan_id || 'growth';
      const data = await apiClient.getBillingUsage(2480000, plan);
      setUsage(data);
    } catch (err) {
      console.error('Failed to load usage:', err);
    }
  };

  const checkSubscriptionStatus = async () => {
    if (!subscription) return;
    
    const now = new Date();
    const periodEnd = new Date(subscription.current_period_end);
    const daysRemaining = Math.ceil((periodEnd.getTime() - now.getTime()) / (1000 * 60 * 60 * 24));
    
    if (subscription.status === 'trial' && subscription.trial_ends_at) {
      const trialEnd = new Date(subscription.trial_ends_at);
      if (isAfter(now, trialEnd)) {
        await handleTrialExpired();
      } else if (isBefore(now, addDays(trialEnd, -3))) {
        sendTrialWarning();
      }
    }
    
    if (daysRemaining <= 7 && daysRemaining > 0 && subscription.status === 'active') {
      sendRenewalWarning(daysRemaining);
    }
  };

  const handleTrialExpired = async () => {
    const result = await apiClient.downgradeToFree(subscription.subscription_id);
    setSubscription({ ...subscription, status: 'downgraded', plan_id: 'free' });
    localStorage.removeItem('auth_token');
    localStorage.removeItem('user_data');
  };

  const sendRenewalWarning = (days: number) => {
    // Send notification
  };

  const sendTrialWarning = () => {
    // Send trial ending soon notification
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
    try {
      const result = await apiClient.upgradeSubscription(subscription?.subscription_id, newPlanId);
      if (result?.client_secret) {
        const stripe = await import('@stripe/stripe-js');
        const stripeInstance = await stripe.loadStripe(import.meta.env.VITE_STRIPE_PUBLISHABLE_KEY);
        await stripeInstance?.redirectToCheckout({ sessionId: result.client_secret });
      }
    } catch (err) {
      setError('Failed to upgrade plan');
    }
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
            {plans.map(plan => (
              <div key={plan.id} className="rounded-lg border border-border bg-card p-6">
                <h3 className="text-lg font-semibold text-foreground">{plan.name}</h3>
                <p className="text-2xl font-bold text-foreground my-2">${plan.price_usd}{plan.interval === 'yearly' ? '/yr' : '/mo'}</p>
                <p className="text-sm text-muted-foreground my-2">{plan.max_seats === -1 ? 'Unlimited' : `${plan.max_seats} seats`}</p>
                <p className="text-sm text-muted-foreground my-2">{formatTokens(plan.monthly_token_quota)} tokens/month</p>
                <ul className="text-sm text-muted-foreground mb-4 space-y-1">
                  {Object.entries(plan.features).map(([key, value]) => (
                    <li key={key} className="flex items-center">
                      {value ? <CheckCircle className="h-4 w-4 text-green-500 mr-2" /> : <Clock className="h-4 w-4 text-gray-400 mr-2" />}
                      {key.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}
                    </li>
                  ))}
                </ul>
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
            ))}
          </div>
        )}

        {activeTab === 'subscription' && subscription && (
          <div className="rounded-lg border border-border bg-card p-6">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-foreground">Current Subscription</h2>
              {subscription.status === 'trial' && (
                <span className="px-3 py-1 text-xs font-semibold rounded-full bg-amber-500/15 text-amber-600">
                  Trial Active
                </span>
              )}
            </div>
            
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
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
                <label className="text-xs font-semibold text-muted-foreground">Next Billing</label>
                <p className="text-foreground">{format(new Date(subscription.current_period_end), 'MMM d, yyyy')}</p>
              </div>
              <div>
                <label className="text-xs font-semibold text-muted-foreground">Tokens Remaining</label>
                <p className="text-foreground">{formatTokens(getTokensRemaining())}</p>
              </div>
              {subscription.trial_ends_at && subscription.status === 'trial' && (
                <div className="md:col-span-2">
                  <label className="text-xs font-semibold text-muted-foreground">Trial Ends</label>
                  <p className="text-foreground">
                    <Clock className="h-4 w-4 inline mr-1" />
                    {format(new Date(subscription.trial_ends_at), 'MMM d, yyyy')}
                  </p>
                </div>
              )}
            </div>

            <div className="mt-6 flex gap-3">
              <button
                onClick={() => setShowUpgradeModal(true)}
                className="px-4 py-2 rounded-lg font-semibold text-sm transition-colors"
                style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
              >
                Change Plan
              </button>
              <button
                onClick={() => apiClient.cancelSubscription(subscription.subscription_id)}
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
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="border-b border-border">
                    <th className="px-4 py-3 text-left text-xs font-semibold text-muted-foreground">Invoice</th>
                    <th className="px-4 py-3 text-right text-xs font-semibold text-muted-foreground">Amount</th>
                    <th className="px-4 py-3 text-center text-xs font-semibold text-muted-foreground">Status</th>
                    <th className="px-4 py-3 text-right text-xs font-semibold text-muted-foreground">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {invoices.map(invoice => (
                    <tr key={invoice.invoice_id} className="border-b border-border">
                      <td className="px-4 py-3">
                        <div>
                          <span className="font-semibold text-foreground">{invoice.invoice_id}</span>
                          <div className="text-xs text-muted-foreground">
                            {format(new Date(invoice.period_start), 'MMM d')} - {format(new Date(invoice.period_end), 'MMM d')}
                          </div>
                        </div>
                      </td>
                      <td className="px-4 py-3 text-right font-semibold text-foreground">
                        ${invoice.amount_usd.toFixed(2)}
                      </td>
                      <td className="px-4 py-3 text-center">
                        <span className={`px-2 py-1 text-xs font-semibold rounded-full ${
                          invoice.status === 'paid' ? 'bg-green-500/15 text-green-600' : 'bg-red-500/15 text-red-600'
                        }`}>
                          {invoice.status}
                        </span>
                      </td>
                      <td className="px-4 py-3 text-right">
                        <button
                          onClick={() => downloadInvoice(invoice.invoice_id)}
                          className="px-3 py-1 text-sm rounded font-semibold"
                          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                        >
                          Download PDF
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {activeTab === 'usage' && usage && (
          <div className="space-y-6">
            <div className="rounded-lg border border-border bg-card p-6">
              <h2 className="text-xl font-semibold text-foreground mb-4">Token Usage</h2>
              
              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-muted-foreground">
                    {usage.current_tokens_used.toLocaleString()} / {usage.monthly_token_quota.toLocaleString()} tokens
                  </span>
                  <span className="font-semibold text-foreground">{usage.usage_percent.toFixed(1)}%</span>
                </div>
                
                <div className="h-3 rounded-full overflow-hidden" style={{ background: 'var(--color-border)' }}>
                  <div
                    className={`h-full rounded-full transition-all ${
                      usage.is_at_risk ? 'bg-red-500' : usage.usage_percent > 70 ? 'bg-amber-500' : 'bg-green-500'
                    }`}
                    style={{ width: `${Math.min(usage.usage_percent, 100)}%` }}
                  />
                </div>
                
                {usage.is_at_risk && (
                  <div className="flex items-center gap-2 text-amber-600 text-sm">
                    <AlertCircle className="h-4 w-4" />
                    <span>Usage limit is approaching. Consider upgrading your plan.</span>
                  </div>
                )}
              </div>
            </div>

            <div className="grid gap-6 md:grid-cols-2">
              <div className="rounded-lg border border-border bg-card p-6">
                <h3 className="text-lg font-semibold text-foreground mb-4">Estimated Cost</h3>
                <div className="flex items-center gap-2">
                  <span className="text-3xl font-bold text-foreground">${usage.estimated_cost_usd.toFixed(2)}</span>
                </div>
                <p className="text-xs text-muted-foreground mt-1">
                  Based on current usage at $0.60 per 1M tokens
                </p>
              </div>

              <div className="rounded-lg border border-border bg-card p-6">
                <h3 className="text-lg font-semibold text-foreground mb-4">Reset Status</h3>
                <div className="flex items-center gap-2">
                  <RefreshCw className="h-4 w-4" />
                  <span className="text-muted-foreground">
                    Tokens will reset at the start of the next billing cycle
                  </span>
                </div>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

function formatTokens(tokens: number): string {
  if (tokens >= 1_000_000) {
    return `${(tokens / 1_000_000).toFixed(1)}M tokens`;
  }
  if (tokens >= 1_000) {
    return `${(tokens / 1_000).toFixed(0)}K tokens`;
  }
  return `${tokens} tokens`;
}

function getTokensRemaining(): number {
  if (!usage) return 0;
  return usage.monthly_token_quota - usage.current_tokens_used;
}