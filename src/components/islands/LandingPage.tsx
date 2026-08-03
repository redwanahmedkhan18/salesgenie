import React, { useState, useEffect } from 'react';
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

const NAV_LINKS = ['Features', 'Pricing', 'Integrations', 'Docs', 'Customers'];

export default function LandingPage() {
  const [activeNav, setActiveNav] = useState('home');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    if (window.location.hash) {
      const section = document.querySelector(window.location.hash);
      if (section) {
        setTimeout(() => {
          section.scrollIntoView({ behavior: 'smooth' });
        }, 100);
      }
    }
  }, []);

  const handleNavClick = (link: string) => {
    setMobileMenuOpen(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-neutral-950 to-slate-900 text-white">
      {/* Navbar */}
      <nav className="sticky top-0 z-40 flex items-center justify-between px-4 py-3 border-b backdrop-blur-md bg-black/40 lg:px-8"
        style={{ borderColor: 'var(--color-border)' }}>
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm flex-shrink-0 text-white">SG</div>
          <span className="font-bold text-base tracking-tight hidden sm:inline">SalesGenie</span>
          <span className="text-xs px-2 py-0.5 rounded-full hidden sm:inline"
            style={{ background: 'rgba(247,165,1,0.15)', color: 'var(--color-primary)' }}>AI</span>
        </div>

        {/* Mobile Menu Button */}
        <button
          className="lg:hidden p-2 rounded-lg hover:bg-white/10 transition-colors"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label="Toggle menu">
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="filled 0 0 24 24">
            {mobileMenuOpen ? (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            ) : (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            )}
          </svg>
        </button>

        {/* Desktop Navigation */}
        <div className="hidden lg:flex items-center gap-1 xl gap-6 text-sm">
          {NAV_LINKS.map(link => (
            <a key={link} href={`#${link.toLowerCase()}`}
              className="hover:text-white transition-colors"
              onClick={() => setActiveNav(link.toLowerCase())}>{link}</a>
          ))}
        </div>

        {/* Desktop CTA */}
        <div className="hidden lg:flex items-center gap-3">
          <a href="/login" className="text-sm font-medium px-4 py-2 rounded-lg transition-colors hover:bg-white/6 text-white">Log in</a>
          <a href="/login" className="text-sm font-bold px-4 py-2 rounded-lg transition-all hover:brightness-110"
            style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
            Start Free Trial →
          </a>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="absolute top-16 left-0 right-0 bg-black/95 border-b border-white/10 lg:hidden p-4">
            <div className="flex flex-col gap-2">
              {NAV_LINKS.map(link => (
                <a key={link} href={`#${link.toLowerCase()}`}
                  className="block py-2 text-base hover:text-orange-400 transition-colors"
                  onClick={handleNavClick}>{link}</a>
              ))}
              <div className="flex flex-col gap-2 pt-2 border-t border-white/10">
                <a href="/login" className="text-sm font-medium py-2 rounded-lg text-center hover:bg-white/10">Log in</a>
                <a href="/login" className="text-sm font-bold py-2 rounded-lg text-center"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                  Start Free Trial →
                </a>
              </div>
            </div>
          </div>
        )}
      </nav>

      {/* Hero */}
      <section className="relative overflow-hidden px-4 py-12 md:py-24 lg:py-20 text-center">
        <div className="absolute inset-0 gradient-dark-mesh pointer-events-none" />
        <div className="relative z-10 max-w-5xl mx-auto px-2">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs mb-6 sm:mb-8"
            style={{ background: 'rgba(247,165,1,0.12)', border: '1px solid rgba(247,165,1,0.25)', color: 'var(--color-primary)' }}>
            Now serving 10M+ enterprise users · 99.99% uptime SLA
          </div>
          <h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-bold leading-tight tracking-tight mb-4 sm:mb-6 px-2">
            <span>Enterprise AI</span>
            <br className="hidden sm:block" />
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-orange-400 to-amber-500">
              Sales & Support
            </span>
            <br />
            <span>That Never Sleeps</span>
          </h1>
          <p className="text-base sm:text-lg max-w-2xl mx-auto mb-6 sm:mb-10 leading-relaxed">
            Multi-agent AI platform with LangGraph orchestration, BAAI RAG pipeline, and omnichannel inbox.
            Built for <strong>500k concurrent connections</strong> and FAANG-grade reliability.
          </p>
          <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 justify-center items-center">
            <a href="/login"
              className="w-full sm:w-auto px-6 sm:px-8 py-3 sm:py-4 rounded-xl font-bold text-base transition-all hover:brightness-110 hover:scale-105 text-center"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
              🚀 Launch Dashboard
            </a>
            <a href="#features"
              className="w-full sm:w-auto px-6 sm:px-8 py-3 sm:py-4 rounded-xl font-semibold text-base border transition-all hover:bg-white/5 text-center"
              style={{ borderColor: 'var(--color-border)', color: 'var(--color-foreground)' }}>
              View Features →
            </a>
          </div>
          <div className="flex items-center justify-center gap-4 sm:gap-6 mt-8 sm:mt-12 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
            {['10M+ Users', '500k Concurrent', '99.99% Uptime', '< 2s Response'].map(stat => (
              <div key={stat} className="text-center min-w-max">
                <div className="font-bold text-sm" style={{ color: 'var(--color-foreground)' }}>{stat.split(' ')[0]}</div>
                <div className="text-xs">{stat.split(' ').slice(1).join(' ')}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="px-4 py-12 md:py-20 lg:px-8">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-10 lg:mb-14 px-2">
            <h2 className="text-2xl sm:text-3xl font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Enterprise-Grade AI, Out of the Box</h2>
            <p className="text-base" style={{ color: 'var(--color-muted-foreground)' }}>Everything you need to automate customer support and accelerate sales at scale.</p>
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {HERO_FEATURES.map((f, i) => (
              <div key={i} className="p-4 rounded-xl border hover:shadow-lg transition-shadow"
                style={{ borderColor: 'var(--color-border)' }}>
                <div className="text-3xl mb-3">{f.icon}</div>
                <h3 className="font-bold text-sm mb-2" style={{ color: 'var(--color-foreground)' }}>{f.title}</h3>
                <p className="text-xs leading-relaxed" style={{ color: 'var(--color-muted-foreground)' }}>{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing */}
      <section id="pricing" className="px-4 py-12 md:py-20 border-t" style={{ borderColor: 'var(--color-border)' }}>
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-10 lg:mb-14 px-2">
            <h2 className="text-2xl sm:text-3xl font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Transparent Pricing</h2>
            <p style={{ color: 'var(--color-muted-foreground)' }}>Usage-based billing. No surprise charges. Start free.</p>
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
            {PRICING_PLANS.map(plan => (
              <div key={plan.key}
                className={`rounded-2xl p-4 sm:p-6 flex flex-col transition-all hover:-translate-y-1 duration-200 ${plan.highlight ? 'ring-2' : 'border'}`}
                style={{
                  background: plan.highlight ? 'rgba(247,165,1,0.06)' : 'var(--color-card)',
                  borderColor: plan.highlight ? 'var(--color-primary)' : 'var(--color-border)',
                  boxShadow: plan.highlight ? '0 0 40px rgba(247,165,1,0.15)' : undefined,
                }}>
                {plan.highlight && (
                  <div className="text-xs font-bold px-3 py-1 rounded-full mb-3 self-start"
                    style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                    Most Popular
                  </div>
                )}
                <div className="text-sm font-bold mb-1" style={{ color: 'var(--color-foreground)' }}>{plan.name}</div>
                <div className="mb-1">
                  <span className="text-2xl sm:text-3xl font-bold" style={{ color: plan.highlight ? 'var(--color-primary)' : 'var(--color-foreground)' }}>{plan.price}</span>
                  <span className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>{plan.period}</span>
                </div>
                <div className="text-xs mb-4" style={{ color: 'var(--color-muted-foreground)' }}>{plan.seats} · {plan.tokens}</div>
                <ul className="space-y-1.5 mb-6 flex-1">
                  {plan.features.map(f => (
                    <li key={f} className="flex items-center gap-2 text-xs" style={{ color: 'var(--color-foreground)' }}>
                      <span style={{ color: '#2c8c66' }}>✓</span> {f}
                    </li>
                  ))}
                </ul>
                <a href="/login"
                  className="block text-center py-2.5 sm:py-3 rounded-xl font-bold text-sm transition-all hover:brightness-110"
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

      {/* Integrations */}
      <section id="integrations" className="px-4 py-12 md:py-20">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-10 lg:mb-14 px-2">
            <h2 className="text-2xl sm:text-3xl font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>9-Channel Omnichannel Platform</h2>
            <p className="text-base" style={{ color: 'var(--color-muted-foreground)' }}>Connect all your customer touchpoints in one unified workspace.</p>
          </div>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {[
              { name: 'Website Chat', icon: '💬', desc: 'Real-time website widgets' },
              { name: 'WhatsApp', icon: '💚', desc: 'Business messaging' },
              { name: 'Slack', icon: '🟦', desc: 'Workspace integration' },
              { name: 'Discord', icon: '🎮', desc: 'Community servers' },
              { name: 'Telegram', icon: '⚪', desc: 'Messaging platform' },
              { name: 'Email', icon: '✉️', desc: 'SMTP/IMAP integration' },
            ].map((i, idx) => (
              <div key={idx} className="border rounded-xl p-4" style={{ borderColor: 'var(--color-border)' }}>
                <div className="text-2xl mb-2">{i.icon}</div>
                <h3 className="font-bold text-sm mb-2" style={{ color: 'var(--color-foreground)' }}>{i.name}</h3>
                <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{i.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Docs */}
      <section id="docs" className="px-4 py-12 md:py-20 border-t" style={{ borderColor: 'var(--color-border)' }}>
        <div className="max-w-4xl mx-auto text-center px-2">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full text-xs mb-6"
            style={{ background: 'rgba(247,165,1,0.12)', border: '1px solid rgba(247,165,1,0.25)', color: 'var(--color-primary)' }}>
            Documentation & Guides
          </div>
          <h2 className="text-2xl sm:text-3xl font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Developer Resources</h2>
          <p className="text-base mb-6" style={{ color: 'var(--color-muted-foreground)' }}>All API docs, tutorials, and reference guides in one place.</p>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3">
            <a href="/docs" className="border rounded-lg p-4 hover:bg-white/5 transition-colors" style={{ borderColor: 'var(--color-border)' }}>
              <h3 className="font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>API Reference</h3>
              <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>REST & GraphQL endpoints</p>
            </a>
            <a href="/docs" className="border rounded-lg p-4 hover:bg-white/5 transition-colors" style={{ borderColor: 'var(--color-border)' }}>
              <h3 className="font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>Tutorials</h3>
              <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Step-by-step guides</p>
            </a>
            <a href="/docs" className="border rounded-lg p-4 hover:bg-white/5 transition-colors" style={{ borderColor: 'var(--color-border)' }}>
              <h3 className="font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>SDKs</h3>
              <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>JavaScript, Python, Go</p>
            </a>
          </div>
        </div>
      </section>

      {/* Customers */}
      <section id="customers" className="px-4 py-12 md:py-20">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-10 lg:mb-14 px-2">
            <h2 className="text-2xl sm:text-3xl font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Trusted by Enterprises</h2>
            <p className="text-base" style={{ color: 'var(--color-muted-foreground)' }}>Global brands rely on SalesGenie for AI-powered sales and support.</p>
          </div>
          <div className="flex flex-col md:flex-row items-center justify-center gap-6 md:gap-8">
            <div className="text-center">
              <div className="text-3xl lg:text-4xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>10M+</div>
              <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>Active Users</p>
            </div>
            <div className="text-center">
              <div className="text-3xl lg:text-4xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>500k+</div>
              <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>Concurrent Connections</p>
            </div>
            <div className="text-center">
              <div className="text-3xl lg:text-4xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>99.99%</div>
              <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>Uptime SLA</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="px-4 py-6 md:py-10 border-t" style={{ borderColor: 'var(--color-border)' }}>
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 rounded flex items-center justify-center text-xs font-bold"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>SG</div>
            <span className="font-bold text-sm">SalesGenie</span>
            <span className="text-xs hidden sm:inline" style={{ color: 'var(--color-muted-foreground)' }}>Enterprise AI Platform · © 2026</span>
          </div>
          <div className="flex gap-4 sm:gap-6 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
            {['Privacy', 'Terms', 'Security', 'Status', 'Docs'].map(l => (
              <a key={l} href="#" className="hover:text-white transition-colors text-sm">{l}</a>
            ))}
          </div>
        </div>
      </footer>
    </div>
  );
}