import React, { useState } from 'react';
import { Sidebar, CommandPalette } from './AppShell';

const HERO_FEATURES = [
  { icon: '🤖', title: 'Multi-Agent AI Orchestration', desc: 'LangGraph-powered Sales, Support, Memory, and Search agents working in concert.' },
  { icon: '📚', title: 'Advanced RAG Knowledge Base', desc: 'BAAI bge-m3 embeddings + pgvector search + cross-encoder re-ranking for sub-1s retrieval.' },
  { icon: '🌐', title: '9-Channel Omnichannel Support', desc: 'Website, WhatsApp, Telegram, Slack, Discord, Email, Voice — unified in one inbox.' },
  { icon: '⚡', title: 'n8n Workflow Automation', desc: 'Visual DAG workflow builder with 10 node types including LLM, CRM, and Database nodes.' },
  { icon: '🛡️', title: 'Enterprise Security & RBAC', desc: 'Keycloak SSO, OAuth2, MFA, 10-tier role-based access, and tenant isolation.' },
  { icon: '📊', title: 'Real-Time Analytics', desc: 'Prometheus/Grafana dashboards for AI accuracy, hallucination rate, and revenue metrics.' },
];

const PRICING_PLANS = [
  { key: 'starter', name: 'Starter', price: '$49', period: '/mo', seats: '5 seats', tokens: '1M tokens', features: ['5 AI Agents', 'Basic Analytics', 'Website Chat', 'Email Support'], cta: 'Start Free Trial', highlight: false },
  { key: 'growth', name: 'Growth', price: '$149', period: '/mo', seats: '25 seats', tokens: '10M tokens', features: ['Unlimited Agents', 'Advanced Analytics', 'All 9 Channels', 'n8n Workflows', 'API Access'], cta: 'Start Growth', highlight: true },
  { key: 'enterprise', name: 'Enterprise', price: '$499', period: '/mo', seats: 'Unlimited seats', tokens: '100M tokens', features: ['Custom AI Models', 'White-label Branding', 'SSO/SAML', 'Dedicated SLA', 'Custom Integrations'], cta: 'Contact Sales', highlight: false },
];

export default function LandingPage() {
  const [activeNav, setActiveNav] = useState('home');

  return (
    <div className="min-h-screen" style={{ background: 'var(--color-background)', color: 'var(--color-foreground)' }}>
      {/* Navbar */}
      <nav className="sticky top-0 z-40 flex items-center justify-between px-8 py-4 border-b"
        style={{ background: 'rgba(24,25,29,0.92)', backdropFilter: 'blur(12px)', borderColor: 'var(--color-border)' }}>
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm flex-shrink-0"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>SG</div>
          <span className="font-bold text-base tracking-tight" style={{ color: 'var(--color-foreground)' }}>SalesGenie</span>
          <span className="text-xs px-2 py-0.5 rounded-full" style={{ background: 'rgba(247,165,1,0.15)', color: 'var(--color-primary)' }}>Enterprise AI</span>
        </div>
        <div className="hidden md:flex items-center gap-6 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
          {['Features', 'Pricing', 'Integrations', 'Docs', 'Customers'].map(link => (
            <a key={link} href={`#${link.toLowerCase()}`} className="hover:text-white transition-colors">{link}</a>
          ))}
        </div>
        <div className="flex items-center gap-3">
          <a href="/login" className="text-sm font-medium px-4 py-2 rounded-lg transition-colors hover:bg-white/6"
            style={{ color: 'var(--color-foreground)' }}>Log in</a>
          <a href="/login" className="text-sm font-bold px-4 py-2 rounded-lg transition-all hover:brightness-110"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
            Start Free Trial →
          </a>
        </div>
      </nav>

      {/* Hero */}
      <section className="relative overflow-hidden px-8 pt-24 pb-20 text-center">
        {/* Mesh gradient background */}
        <div className="absolute inset-0 gradient-dark-mesh pointer-events-none" />
        <div className="relative z-10 max-w-5xl mx-auto">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-sm mb-8"
            style={{ background: 'rgba(247,165,1,0.12)', border: '1px solid rgba(247,165,1,0.25)', color: 'var(--color-primary)' }}>
            Now serving 10M+ enterprise users · 99.99% uptime SLA
          </div>
          <h1 className="text-5xl md:text-7xl font-bold leading-tight tracking-tight mb-6">
            <span style={{ color: 'var(--color-foreground)' }}>Enterprise AI</span>
            <br />
            <span className="gradient-brand bg-clip-text text-transparent" style={{ WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
              Sales & Support
            </span>
            <br />
            <span style={{ color: 'var(--color-foreground)' }}>That Never Sleeps</span>
          </h1>
          <p className="text-lg max-w-2xl mx-auto mb-10 leading-relaxed" style={{ color: 'var(--color-muted-foreground)' }}>
            Multi-agent AI platform with LangGraph orchestration, BAAI RAG pipeline, and omnichannel inbox.
            Built for <strong style={{ color: 'var(--color-foreground)' }}>500k concurrent connections</strong> and FAANG-grade reliability.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="/login"
              className="px-8 py-4 rounded-xl font-bold text-base transition-all hover:brightness-110 hover:scale-105"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
              🚀 Launch Dashboard
            </a>
            <a href="#features"
              className="px-8 py-4 rounded-xl font-semibold text-base border transition-all hover:bg-white/5"
              style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}>
              View Features →
            </a>
          </div>
          {/* Social proof */}
          <div className="flex items-center justify-center gap-8 mt-12 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
            {['10M+ Users', '500k Concurrent', '99.99% Uptime', '< 2s Response'].map(stat => (
              <div key={stat} className="text-center">
                <div className="font-bold text-sm" style={{ color: 'var(--color-foreground)' }}>{stat.split(' ')[0]}</div>
                <div className="text-xs">{stat.split(' ').slice(1).join(' ')}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="px-8 py-20">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-14">
            <h2 className="text-3xl font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Enterprise-Grade AI, Out of the Box</h2>
            <p className="text-base" style={{ color: 'var(--color-muted-foreground)' }}>Everything you need to automate customer support and accelerate sales at scale.</p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
            {HERO_FEATURES.map((f, i) => (
              <div key={i} className="kpi-card group cursor-default">
                <div className="text-3xl mb-4">{f.icon}</div>
                <h3 className="font-bold text-sm mb-2" style={{ color: 'var(--color-foreground)' }}>{f.title}</h3>
                <p className="text-xs leading-relaxed" style={{ color: 'var(--color-muted-foreground)' }}>{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing */}
      <section id="pricing" className="px-8 py-20 border-t" style={{ borderColor: 'var(--color-border)' }}>
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-14">
            <h2 className="text-3xl font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Transparent Pricing</h2>
            <p style={{ color: 'var(--color-muted-foreground)' }}>Usage-based billing. No surprise charges. Start free.</p>
          </div>
          <div className="grid md:grid-cols-3 gap-6">
            {PRICING_PLANS.map(plan => (
              <div key={plan.key}
                className={`rounded-2xl p-6 flex flex-col transition-all hover:-translate-y-1 duration-200 ${plan.highlight ? 'ring-2' : 'border'}`}
                style={{
                  background: plan.highlight ? 'rgba(247,165,1,0.06)' : 'var(--color-card)',
                  borderColor: plan.highlight ? 'var(--color-primary)' : 'var(--color-border)',
                  boxShadow: plan.highlight ? '0 0 40px rgba(247,165,1,0.15)' : undefined,
                }}>
                {plan.highlight && (
                  <div className="text-xs font-bold px-3 py-1 rounded-full mb-4 self-start"
                    style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                    Most Popular
                  </div>
                )}
                <div className="text-sm font-bold mb-1" style={{ color: 'var(--color-foreground)' }}>{plan.name}</div>
                <div className="mb-1">
                  <span className="text-4xl font-bold" style={{ color: plan.highlight ? 'var(--color-primary)' : 'var(--color-foreground)' }}>{plan.price}</span>
                  <span className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>{plan.period}</span>
                </div>
                <div className="text-xs mb-6" style={{ color: 'var(--color-muted-foreground)' }}>{plan.seats} · {plan.tokens}</div>
                <ul className="space-y-2 mb-8 flex-1">
                  {plan.features.map(f => (
                    <li key={f} className="flex items-center gap-2 text-xs" style={{ color: 'var(--color-foreground)' }}>
                      <span style={{ color: '#2c8c66' }}>✓</span> {f}
                    </li>
                  ))}
                </ul>
                <a href="/login"
                  className="block text-center py-3 rounded-xl font-bold text-sm transition-all hover:brightness-110"
                  style={{
                    background: plan.highlight ? 'var(--color-primary)' : 'var(--color-muted)',
                    color: plan.highlight ? 'var(--color-on-primary)' : 'var(--color-foreground)',
                  }}>
                  {plan.cta}
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="px-8 py-10 border-t" style={{ borderColor: 'var(--color-border)' }}>
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 rounded flex items-center justify-center text-xs font-bold"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>SG</div>
            <span className="font-bold text-sm" style={{ color: 'var(--color-foreground)' }}>SalesGenie</span>
            <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Enterprise AI Platform · © 2026</span>
          </div>
          <div className="flex gap-6 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
            {['Privacy', 'Terms', 'Security', 'Status', 'Docs'].map(l => (
              <a key={l} href="#" className="hover:text-white transition-colors">{l}</a>
            ))}
          </div>
        </div>
      </footer>
    </div>
  );
}
