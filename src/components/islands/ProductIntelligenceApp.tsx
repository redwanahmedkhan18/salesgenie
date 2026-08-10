import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';
import type {
  ResearchProject,
  CreateProjectRequest,
  EvidenceItem,
  Competitor,
  MarketOpportunity,
  ProductStrategy,
  ScenarioModel,
  LaunchPlanPhase,
  ProductReport,
  AddEvidenceRequest,
  AddCompetitorRequest,
  CreateScenarioRequest,
  AnalysisRequest,
} from '../../lib/types';
import {
  Sidebar,
  CommandPalette,
} from './AppShell';

type ActiveTab = 'projects' | 'project-detail';

interface ProjectDetailTab {
  id: string;
  label: string;
  icon: string;
}

function ProjectsList({
  projects,
  onProjectClick,
  onProjectCreate,
  onProjectDelete,
}: {
  projects: ResearchProject[];
  onProjectClick: (project: ResearchProject) => void;
  onProjectCreate: () => void;
  onProjectDelete: (project: ResearchProject) => void;
}) {
  return (
    <div className="p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-xl font-semibold">Research Projects</h2>
        <button
          onClick={onProjectCreate}
          className="px-4 py-2 text-sm font-medium rounded-lg"
          style={{ background: 'var(--color-primary)', color: 'white' }}
        >
          New Project
        </button>
      </div>
      {projects.length === 0 ? (
        <div className="text-center py-12" style={{ color: 'var(--color-muted-foreground)' }}>
          <p>No projects yet. Create your first product intelligence project.</p>
        </div>
      ) : (
        <div className="space-y-3">
          {projects.map((project) => (
            <div
              key={project.id}
              className="border rounded-lg p-4 cursor-pointer transition-colors"
              style={{
                background: 'var(--color-card)',
                borderColor: 'var(--color-border)',
              }}
              onClick={() => onProjectClick(project)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') onProjectClick(project);
              }}
            >
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <h3 className="font-semibold">{project.name}</h3>
                  <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    {project.product_name} • {project.product_category}
                  </p>
                  <p className="text-xs mt-2" style={{ color: 'var(--color-muted-foreground)' }}>
                    Target: {project.target_market} • Geo: {project.geographic_market}
                  </p>
                </div>
                <span
                  className="text-xs px-2 py-1 rounded"
                  style={{
                    background:
                      project.status === 'completed'
                        ? 'var(--color-success-bg, #dcfce7)'
                        : project.status === 'research'
                        ? 'var(--color-info-bg, #dbeafe)'
                        : 'var(--color-warning-bg, #fef3c7)',
                    color:
                      project.status === 'completed'
                        ? 'var(--color-success, #166534)'
                        : project.status === 'research'
                        ? 'var(--color-info, #1e40af)'
                        : 'var(--color-warning, #92400e)',
                  }}
                >
                  {project.status}
                </span>
              </div>
              <div className="flex items-center justify-between mt-3 pt-3 border-t" style={{ borderColor: 'var(--color-border)' }}>
                <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                  Updated {new Date(project.updated_at).toLocaleDateString()}
                </span>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    onProjectDelete(project);
                  }}
                  className="text-xs px-2 py-1 rounded hover:underline"
                  style={{ color: 'var(--color-destructive, #dc2626)' }}
                >
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function ProjectForm({
  project,
  onSubmit,
  onCancel,
}: {
  project?: ResearchProject;
  onSubmit: (data: CreateProjectRequest) => Promise<void>;
  onCancel: () => void;
}) {
  const [formData, setFormData] = useState<CreateProjectRequest>({
    name: project?.name || '',
    description: project?.description || '',
    product_name: project?.product_name || '',
    product_description: project?.product_description || '',
    product_category: project?.product_category || '',
    target_market: project?.target_market || '',
    geographic_market: project?.geographic_market || '',
    business_model: project?.business_model || '',
    expected_price: project?.expected_price || '',
    product_stage: project?.product_stage || 'beta',
    competitive_advantages: project?.competitive_advantages || '',
  });

  const handleChange = (field: keyof CreateProjectRequest, value: string) => {
    setFormData({ ...formData, [field]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await onSubmit(formData);
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-semibold mb-4">
        {project ? 'Edit Project' : 'New Research Project'}
      </h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium mb-1">Project Name</label>
            <input
              type="text"
              value={formData.name}
              onChange={(e) => handleChange('name', e.target.value)}
              className="w-full px-3 py-2 border rounded-lg"
              style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Product Name</label>
            <input
              type="text"
              value={formData.product_name}
              onChange={(e) => handleChange('product_name', e.target.value)}
              className="w-full px-3 py-2 border rounded-lg"
              style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              required
            />
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">Product Description</label>
          <textarea
            value={formData.product_description}
            onChange={(e) => handleChange('product_description', e.target.value)}
            className="w-full px-3 py-2 border rounded-lg"
            style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
            rows={3}
            required
          />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium mb-1">Product Category</label>
            <input
              type="text"
              value={formData.product_category}
              onChange={(e) => handleChange('product_category', e.target.value)}
              className="w-full px-3 py-2 border rounded-lg"
              style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              placeholder="e.g., SaaS, Fintech, E-commerce"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Target Market (customers)</label>
            <input
              type="text"
              value={formData.target_market}
              onChange={(e) => handleChange('target_market', e.target.value)}
              className="w-full px-3 py-2 border rounded-lg"
              style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              placeholder="e.g., Mid-market e-commerce companies"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Geographic Market</label>
            <input
              type="text"
              value={formData.geographic_market}
              onChange={(e) => handleChange('geographic_market', e.target.value)}
              className="w-full px-3 py-2 border rounded-lg"
              style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              placeholder="e.g., United States, Southeast Asia"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Business Model</label>
            <input
              type="text"
              value={formData.business_model}
              onChange={(e) => handleChange('business_model', e.target.value)}
              className="w-full px-3 py-2 border rounded-lg"
              style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              placeholder="e.g., Subscription, Freemium"
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Expected Price</label>
            <input
              type="text"
              value={formData.expected_price}
              onChange={(e) => handleChange('expected_price', e.target.value)}
              className="w-full px-3 py-2 border rounded-lg"
              style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              placeholder="e.g., $49-$999"
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Product Stage</label>
            <select
              value={formData.product_stage}
              onChange={(e) => handleChange('product_stage', e.target.value)}
              className="w-full px-3 py-2 border rounded-lg"
              style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
            >
              <option value="concept">Concept</option>
              <option value="mvp">MVP</option>
              <option value="beta">Beta</option>
              <option value="launched">Launched</option>
            </select>
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">Competitive Advantages</label>
          <textarea
            value={formData.competitive_advantages}
            onChange={(e) => handleChange('competitive_advantages', e.target.value)}
            className="w-full px-3 py-2 border rounded-lg"
            style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
            rows={2}
            placeholder="e.g., AI-first, WhatsApp-native, integrated sales automation"
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">Description (internal)</label>
          <textarea
            value={formData.description || ''}
            onChange={(e) => handleChange('description', e.target.value)}
            className="w-full px-3 py-2 border rounded-lg"
            style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
            rows={2}
            placeholder="Internal notes about this project"
          />
        </div>

        <div className="flex gap-3">
          <button
            type="submit"
            className="px-4 py-2 text-sm font-medium rounded-lg"
            style={{ background: 'var(--color-primary)', color: 'white' }}
          >
            {project ? 'Update' : 'Create'} Project
          </button>
          <button
            type="button"
            onClick={onCancel}
            className="px-4 py-2 text-sm font-medium rounded-lg"
            style={{ background: 'var(--color-secondary-bg, #f1f5f9)', color: 'var(--color-secondary-foreground, #475569)' }}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}

function ProjectDetailView({
  project,
  onBack,
  onUpdate,
  onDelete,
}: {
  project: ResearchProject;
  onBack: () => void;
  onUpdate: (project: ResearchProject) => void;
  onDelete: (project: ResearchProject) => void;
}) {
  const detailTabs: ProjectDetailTab[] = [
    { id: 'evidence', label: 'Evidence', icon: '🔍' },
    { id: 'competitors', label: 'Competitors', icon: '🏢' },
    { id: 'opportunities', label: 'Opportunities', icon: '💡' },
    { id: 'strategy', label: 'Strategy', icon: '🎯' },
    { id: 'scenarios', label: 'Scenarios', icon: '📊' },
    { id: 'launch', label: 'Launch Plan', icon: '🚀' },
    { id: 'report', label: 'Report', icon: '📄' },
  ];

  const [activeTab, setActiveTab] = useState('evidence');
  const [evidence, setEvidence] = useState<EvidenceItem[]>([]);
  const [competitors, setCompetitors] = useState<Competitor[]>([]);
  const [opportunities, setOpportunities] = useState<MarketOpportunity[]>([]);
  const [strategy, setStrategy] = useState<ProductStrategy | null>(null);
  const [scenarios, setScenarios] = useState<ScenarioModel[]>([]);
  const [launchPlan, setLaunchPlan] = useState<LaunchPlanPhase[]>([]);
  const [report, setReport] = useState<ProductReport | null>(null);
  const [loading, setLoading] = useState<Record<string, boolean>>({});

  const loadTabData = async (tab: string) => {
    if (loading[tab]) return;
    setLoading({ ...loading, [tab]: true });

    try {
      if (tab === 'evidence') {
        const data = await apiClient.listProjectEvidence(project.id);
        setEvidence(data || []);
      } else if (tab === 'competitors') {
        const data = await apiClient.listCompetitors(project.id);
        setCompetitors(data || []);
      } else if (tab === 'opportunities') {
        const data = await apiClient.getMarketOpportunities(project.id);
        setOpportunities(data || []);
      } else if (tab === 'strategy') {
        const data = await apiClient.getProductStrategy(project.id);
        setStrategy(data || null);
      } else if (tab === 'scenarios') {
        const data = await apiClient.listScenarios(project.id);
        setScenarios(data || []);
      } else if (tab === 'launch') {
        const data = await apiClient.getLaunchPlan(project.id);
        setLaunchPlan(data || []);
      } else if (tab === 'report') {
        const data = await apiClient.getProductReport(project.id);
        setReport(data || null);
      }
    } catch (err) {
      console.error(`Failed to load ${tab}:`, err);
    } finally {
      setLoading({ ...loading, [tab]: false });
    }
  };

  useEffect(() => {
    loadTabData(activeTab);
  }, [activeTab]);

  const handleTriggerAnalysis = async (analysisType: string) => {
    setLoading({ ...loading, analyze: true });
    try {
      const req: AnalysisRequest = {
        project_id: project.id,
        analysis_type: analysisType,
        language: 'en',
      };
      const result = await apiClient.triggerAnalysis(project.id, req);
      if (result) {
        onUpdate({ ...project, status: 'research' });
      }
    } catch (err) {
      console.error('Failed to trigger analysis:', err);
    } finally {
      setLoading({ ...loading, analyze: false });
    }
  };

  return (
    <div className="p-6">
      <div className="flex items-center justify-between mb-4">
        <div>
          <button onClick={onBack} className="text-sm text-blue-600 hover:underline mb-2">
            ← Back to Projects
          </button>
          <h2 className="text-xl font-semibold">{project.name}</h2>
          <p className="text-sm mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
            Product: {project.product_name} • Category: {project.product_category}
          </p>
        </div>
        <div className="flex items-center gap-3">
          <button
            onClick={() => onUpdate({ ...project, status: project.status === 'completed' ? 'review' : 'completed' })}
            className="px-3 py-1 text-sm rounded border"
            style={{ borderColor: 'var(--color-border)' }}
          >
            {project.status === 'completed' ? 'Reopen' : 'Mark Complete'}
          </button>
          <button
            onClick={() => onDelete(project)}
            className="px-3 py-1 text-sm rounded"
            style={{ background: 'var(--color-destructive-bg, #fee2e2)', color: 'var(--color-destructive, #dc2626)' }}
          >
            Delete
          </button>
        </div>
      </div>

      <div className="flex gap-2 mb-4 overflow-x-auto">
        {detailTabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`px-4 py-2 text-sm font-medium rounded-lg whitespace-nowrap ${
              activeTab === tab.id ? 'border' : 'border border-transparent'
            }`}
            style={{
              background: activeTab === tab.id ? 'var(--color-primary)' : 'var(--color-secondary-bg, #f1f5f9)',
              color: activeTab === tab.id ? 'white' : 'var(--color-secondary-foreground, #475569)',
            }}
          >
            {tab.icon} {tab.label}
          </button>
        ))}
      </div>

      <div
        className="border rounded-lg p-4 min-h-[300px]"
        style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}
      >
        {activeTab === 'evidence' && (
          <EvidenceTab evidence={evidence} projectId={project.id} onEvidenceAdded={() => loadTabData('evidence')} />
        )}
        {activeTab === 'competitors' && (
          <CompetitorsTab competitors={competitors} projectId={project.id} onCompetitorAdded={() => loadTabData('competitors')} />
        )}
        {activeTab === 'opportunities' && (
          <OpportunitiesTab opportunities={opportunities} />
        )}
        {activeTab === 'strategy' && (
          <StrategyTab
            strategy={strategy}
            loading={loading.strategy}
            onAnalyze={() => handleTriggerAnalysis('strategy')}
          />
        )}
        {activeTab === 'scenarios' && (
          <ScenariosTab scenarios={scenarios} projectId={project.id} onScenarioAdded={() => loadTabData('scenarios')} />
        )}
        {activeTab === 'launch' && (
          <LaunchPlanTab launchPlan={launchPlan} />
        )}
        {activeTab === 'report' && (
          <ReportTab report={report} loading={loading.report} onGenerateFullReport={() => handleTriggerAnalysis('full')} />
        )}
      </div>
    </div>
  );
}

function EvidenceTab({
  evidence,
  projectId,
  onEvidenceAdded,
}: {
  evidence: EvidenceItem[];
  projectId: string;
  onEvidenceAdded: () => void;
}) {
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState<Partial<AddEvidenceRequest>>({
    evidence_type: 'web_search',
    source_name: '',
    title: '',
    content: '',
    confidence: 'medium',
    confidence_score: 0.7,
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await apiClient.addEvidence({ ...formData, project_id: projectId } as AddEvidenceRequest);
    setShowForm(false);
    setFormData({ evidence_type: 'web_search', source_name: '', title: '', content: '', confidence: 'medium', confidence_score: 0.7 });
    onEvidenceAdded();
  };

  return (
    <div>
      <div className="flex items-center justify-between mb-3">
        <h3 className="font-medium">Evidence Items ({evidence.length})</h3>
        <button
          onClick={() => setShowForm(!showForm)}
          className="text-xs px-3 py-1 rounded"
          style={{ background: 'var(--color-primary)', color: 'white' }}
        >
          + Add Evidence
        </button>
      </div>

      {showForm && (
        <form onSubmit={handleSubmit} className="border rounded-lg p-4 mb-3" style={{ borderColor: 'var(--color-border)' }}>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div>
              <label className="block text-xs font-medium mb-1">Type</label>
              <select
                value={formData.evidence_type}
                onChange={(e) => setFormData({ ...formData, evidence_type: e.target.value })}
                className="w-full px-3 py-2 text-sm border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
              >
                <option value="web_search">Web Search</option>
                <option value="news">News</option>
                <option value="report">Report</option>
                <option value="competitor_website">Competitor Website</option>
                <option value="customer_feedback">Customer Feedback</option>
                <option value="industry_analysis">Industry Analysis</option>
                <option value="mcp_tool">MCP Tool</option>
              </select>
            </div>
            <div>
              <label className="block text-xs font-medium mb-1">Source</label>
              <input
                type="text"
                value={formData.source_name}
                onChange={(e) => setFormData({ ...formData, source_name: e.target.value })}
                className="w-full px-3 py-2 text-sm border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                placeholder="e.g., TechCrunch, Google"
                required
              />
            </div>
            <div className="md:col-span-2">
              <label className="block text-xs font-medium mb-1">Title</label>
              <input
                type="text"
                value={formData.title}
                onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                className="w-full px-3 py-2 text-sm border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                required
              />
            </div>
            <div className="md:col-span-2">
              <label className="block text-xs font-medium mb-1">Content</label>
              <textarea
                value={formData.content}
                onChange={(e) => setFormData({ ...formData, content: e.target.value })}
                className="w-full px-3 py-2 text-sm border rounded"
                style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                rows={3}
                required
              />
            </div>
          </div>
          <div className="flex gap-2 mt-3">
            <button type="submit" className="text-xs px-3 py-1 rounded" style={{ background: 'var(--color-primary)', color: 'white' }}>Save</button>
            <button type="button" onClick={() => setShowForm(false)} className="text-xs px-3 py-1 rounded" style={{ background: 'var(--color-secondary-bg, #f1f5f9)' }}>Cancel</button>
          </div>
        </form>
      )}

      {evidence.length === 0 ? (
        <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No evidence added yet.</p>
      ) : (
        <div className="space-y-2">
          {evidence.map((e) => (
            <div key={e.id} className="border rounded p-3" style={{ borderColor: 'var(--color-border)' }}>
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <h4 className="font-medium text-sm">{e.title}</h4>
                  <p className="text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    {e.evidence_type} • {e.source_name} • Confidence: {e.confidence} ({Math.round(e.confidence_score * 100)}%)
                  </p>
                  <p className="text-xs mt-1 text-gray-600 dark:text-gray-400 line-clamp-2">{e.content}</p>
                </div>
                <span className="text-xs px-2 py-1 rounded" style={{
                  background: e.confidence === 'high' ? 'var(--color-success-bg, #dcfce7)' : 'var(--color-warning-bg, #fef3c7)',
                  color: e.confidence === 'high' ? 'var(--color-success, #166534)' : 'var(--color-warning, #92400e)',
                }}>{e.confidence}</span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function CompetitorsTab({
  competitors,
  projectId,
  onCompetitorAdded,
}: {
  competitors: Competitor[];
  projectId: string;
  onCompetitorAdded: () => void;
}) {
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState<Partial<AddCompetitorRequest>>({
    name: '',
    domain: '',
    industry: '',
    product_name: '',
  });

  const handleChange = (field: keyof AddCompetitorRequest, value: string | string[]) => {
    setFormData({ ...formData, [field]: value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await apiClient.addCompetitor({ ...formData, project_id: projectId } as AddCompetitorRequest);
    setShowForm(false);
    setFormData({ name: '', domain: '', industry: '', product_name: '' });
    onCompetitorAdded();
  };

  return (
    <div>
      <div className="flex items-center justify-between mb-3">
        <h3 className="font-medium">Competitors ({competitors.length})</h3>
        <button
          onClick={() => setShowForm(!showForm)}
          className="text-xs px-3 py-1 rounded"
          style={{ background: 'var(--color-primary)', color: 'white' }}
        >
          + Add Competitor
        </button>
      </div>

      {competitors.length === 0 ? (
        <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No competitors added yet. Add competitors to analyze gaps.</p>
      ) : (
        <div className="space-y-2">
          {competitors.map((c) => (
            <div key={c.id} className="border rounded p-3" style={{ borderColor: 'var(--color-border)' }}>
              <div className="flex items-start justify-between">
                <div>
                  <h4 className="font-medium text-sm">{c.name}</h4>
                  <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                    {c.domain} • {c.industry}
                  </p>
                  {c.product_name && (
                    <p className="text-xs mt-1">Product: {c.product_name}</p>
                  )}
                  {c.pricing_model && (
                    <p className="text-xs mt-1">Pricing: {c.pricing_model}</p>
                  )}
                </div>
                <div className="flex gap-2">
                  {c.strengths && c.strengths.length > 0 && (
                    <div className="text-right">
                      <span className="text-xs text-green-600">Strengths: {c.strengths.length}</span>
                    </div>
                  )}
                  {c.weaknesses && c.weaknesses.length > 0 && (
                    <div className="text-right">
                      <span className="text-xs text-orange-600">Weaknesses: {c.weaknesses.length}</span>
                    </div>
                  )}
                </div>
              </div>
              {c.strengths && c.strengths.length > 0 && (
                <div className="mt-2">
                  <p className="text-xs font-medium">Strengths:</p>
                  <ul className="text-xs list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
                    {c.strengths.map((s, i) => <li key={i}>{s}</li>)}
                  </ul>
                </div>
              )}
              {c.weaknesses && c.weaknesses.length > 0 && (
                <div className="mt-1">
                  <p className="text-xs font-medium">Weaknesses:</p>
                  <ul className="text-xs list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
                    {c.weaknesses.map((s, i) => <li key={i}>{s}</li>)}
                  </ul>
                </div>
              )}
            </div>
          ))}
        </div>
      )}

      {showForm && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="border rounded-lg p-6 w-full max-w-2xl" style={{ background: 'var(--color-card)' }}>
            <h3 className="text-lg font-semibold mb-4">Add Competitor</h3>
            <form onSubmit={handleSubmit} className="space-y-3">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-medium mb-1">Name *</label>
                  <input type="text" value={formData.name || ''} onChange={(e) => handleChange('name', e.target.value)}
                    className="w-full px-3 py-2 text-sm border rounded"
                    style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }} required />
                </div>
                <div>
                  <label className="block text-xs font-medium mb-1">Domain</label>
                  <input type="text" value={formData.domain || ''} onChange={(e) => handleChange('domain', e.target.value)}
                    className="w-full px-3 py-2 text-sm border rounded"
                    style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                    placeholder="e.g., compa.com" />
                </div>
                <div>
                  <label className="block text-xs font-medium mb-1">Industry</label>
                  <input type="text" value={formData.industry || ''} onChange={(e) => handleChange('industry', e.target.value)}
                    className="w-full px-3 py-2 text-sm border rounded"
                    style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }} />
                </div>
                <div>
                  <label className="block text-xs font-medium mb-1">Product Name</label>
                  <input type="text" value={formData.product_name || ''} onChange={(e) => handleChange('product_name', e.target.value)}
                    className="w-full px-3 py-2 text-sm border rounded"
                    style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }} />
                </div>
                <div>
                  <label className="block text-xs font-medium mb-1">Pricing Model</label>
                  <input type="text" value={formData.pricing_model || ''} onChange={(e) => handleChange('pricing_model', e.target.value)}
                    className="w-full px-3 py-2 text-sm border rounded"
                    style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                    placeholder="e.g., $49-999/mo" />
                </div>
                <div>
                  <label className="block text-xs font-medium mb-1">Market Position</label>
                  <input type="text" value={formData.market_position || ''} onChange={(e) => handleChange('market_position', e.target.value)}
                    className="w-full px-3 py-2 text-sm border rounded"
                    style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }} />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-xs font-medium mb-1">Strengths</label>
                  <input type="text" value={formData.strengths?.join(', ') || ''}
                    onChange={(e) => handleChange('strengths', e.target.value.split(',').map(s => s.trim()).filter(Boolean))}
                    className="w-full px-3 py-2 text-sm border rounded"
                    style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                    placeholder="Comma-separated" />
                </div>
                <div className="md:col-span-2">
                  <label className="block text-xs font-medium mb-1">Weaknesses</label>
                  <input type="text" value={formData.weaknesses?.join(', ') || ''}
                    onChange={(e) => handleChange('weaknesses', e.target.value.split(',').map(s => s.trim()).filter(Boolean))}
                    className="w-full px-3 py-2 text-sm border rounded"
                    style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                    placeholder="Comma-separated" />
                </div>
              </div>
              <div className="flex gap-2">
                <button type="submit" className="px-3 py-1 text-sm rounded" style={{ background: 'var(--color-primary)', color: 'white' }}>Add</button>
                <button type="button" onClick={() => setShowForm(false)} className="px-3 py-1 text-sm rounded" style={{ background: 'var(--color-secondary-bg, #f1f5f9)' }}>Cancel</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

function OpportunitiesTab({ opportunities }: { opportunities: MarketOpportunity[] }) {
  if (opportunities.length === 0) {
    return (
      <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
        <p>No market opportunities identified yet.</p>
        <p className="text-xs mt-1">Run competitor analysis to detect gaps.</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {opportunities.map((o) => (
        <div key={o.id} className="border rounded p-3" style={{ borderColor: 'var(--color-border)' }}>
          <div className="flex items-start justify-between">
            <div>
              <h4 className="font-medium text-sm">{o.title}</h4>
              <p className="text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>{o.category}</p>
            </div>
            <span className="text-xs px-2 py-1 rounded" style={{
              background: o.severity === 'high' ? 'var(--color-warning-bg, #fef3c7)' : 'var(--color-info-bg, #dbeafe)',
              color: o.severity === 'high' ? 'var(--color-warning, #92400e)' : 'var(--color-info, #1e40af)',
            }}>{o.severity}</span>
          </div>
          <p className="text-xs mt-2">{o.description}</p>
          {o.estimated_market_size_usd && (
            <p className="text-xs mt-2 font-medium">Est. Market Size: ${o.estimated_market_size_usd.toLocaleString()}</p>
          )}
          {o.supporting_evidence && o.supporting_evidence.length > 0 && (
            <div className="mt-2">
              <p className="text-xs font-medium">Supporting Evidence:</p>
              <ul className="text-xs list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
                {o.supporting_evidence.map((e: any, i: number) => <li key={i}>{e.title || e.source || 'Evidence item'}</li>)}
              </ul>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

function StrategyTab({
  strategy,
  loading,
  onAnalyze,
}: {
  strategy: ProductStrategy | null;
  loading: boolean;
  onAnalyze: () => void;
}) {
  if (loading) return <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>Loading strategy...</p>;
  if (!strategy)
    return (
      <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
        <p>No strategy has been generated yet.</p>
        <button
          onClick={onAnalyze}
          className="mt-3 px-4 py-2 text-sm font-medium rounded-lg"
          style={{ background: 'var(--color-primary)', color: 'white' }}
        >
          Generate Strategy with AI
        </button>
      </div>
    );

  return (
    <div className="space-y-4">
      <div>
        <h3 className="font-medium text-sm">Positioning Statement</h3>
        <p className="text-sm mt-1">{strategy.positioning_statement}</p>
      </div>
      {strategy.target_market_segments && (
        <div>
          <h3 className="font-medium text-sm">Target Segments</h3>
          <ul className="text-sm list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
            {strategy.target_market_segments.map((s, i) => <li key={i}>{s}</li>)}
          </ul>
        </div>
      )}
      {strategy.key_differentiators && (
        <div>
          <h3 className="font-medium text-sm">Key Differentiators</h3>
          <ul className="text-sm list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
            {strategy.key_differentiators.map((d, i) => <li key={i}>{d}</li>)}
          </ul>
        </div>
      )}
      {strategy.pricing_recommendation && (
        <div>
          <h3 className="font-medium text-sm">Pricing Recommendation</h3>
          <pre className="text-xs mt-1 p-2 border rounded" style={{ borderColor: 'var(--color-border)' }}>
            {JSON.stringify(strategy.pricing_recommendation, null, 2)}
          </pre>
        </div>
      )}
      {strategy.strategic_risks && (
        <div>
          <h3 className="font-medium text-sm">Strategic Risks</h3>
          <ul className="text-sm list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
            {strategy.strategic_risks.map((r, i) => <li key={i}>{r}</li>)}
          </ul>
        </div>
      )}
      <div className="flex items-center gap-2 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
        <span>Confidence: {Math.round(strategy.confidence_score * 100)}%</span>
        <span>•</span>
        <span>Model: {strategy.ai_model_version}</span>
      </div>
    </div>
  );
}

function ScenariosTab({
  scenarios,
  projectId,
  onScenarioAdded,
}: {
  scenarios: ScenarioModel[];
  projectId: string;
  onScenarioAdded: () => void;
}) {
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState<Partial<CreateScenarioRequest>>({
    name: 'Base',
    description: '',
    assumptions: {},
    probability: 0.33,
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await apiClient.createScenario({ ...formData, project_id: projectId } as CreateScenarioRequest);
    setShowForm(false);
    onScenarioAdded();
  };

  return (
    <div>
      <div className="flex items-center justify-between mb-3">
        <h3 className="font-medium">Scenario Models ({scenarios.length})</h3>
        <button
          onClick={() => setShowForm(!showForm)}
          className="text-xs px-3 py-1 rounded"
          style={{ background: 'var(--color-primary)', color: 'white' }}
        >
          + Add Scenario
        </button>
      </div>

      {showForm && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="border rounded-lg p-6 w-full max-w-lg" style={{ background: 'var(--color-card)' }}>
            <h3 className="font-medium mb-3">Add Scenario Model</h3>
            <form onSubmit={handleSubmit} className="space-y-3">
              <div>
                <label className="block text-xs font-medium mb-1">Name</label>
                <select
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="w-full px-3 py-2 text-sm border rounded"
                  style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                >
                  <option value="Conservative">Conservative</option>
                  <option value="Base">Base</option>
                  <option value="Aggressive">Aggressive</option>
                </select>
              </div>
              <div>
                <label className="block text-xs font-medium mb-1">Description</label>
                <textarea
                  value={formData.description || ''}
                  onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                  className="w-full px-3 py-2 text-sm border rounded"
                  style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                  rows={2}
                  placeholder="Low adoption, high CAC, slow growth..."
                />
              </div>
              <div>
                <label className="block text-xs font-medium mb-1">Probability</label>
                <input
                  type="number"
                  step="0.01"
                  min="0"
                  max="1"
                  value={formData.probability || 0.33}
                  onChange={(e) => setFormData({ ...formData, probability: parseFloat(e.target.value) })}
                  className="w-full px-3 py-2 text-sm border rounded"
                  style={{ background: 'var(--color-input)', borderColor: 'var(--color-border)' }}
                />
              </div>
              <div className="flex gap-2">
                <button type="submit" className="px-3 py-1 text-sm rounded" style={{ background: 'var(--color-primary)', color: 'white' }}>Add</button>
                <button type="button" onClick={() => setShowForm(false)} className="px-3 py-1 text-sm rounded" style={{ background: 'var(--color-secondary-bg, #f1f5f9)' }}>Cancel</button>
              </div>
            </form>
          </div>
        </div>
      )}

      {scenarios.length === 0 ? (
        <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No scenarios defined yet.</p>
      ) : (
        <div className="space-y-2">
          {scenarios.map((s) => (
            <div key={s.id} className="border rounded p-3" style={{ borderColor: 'var(--color-border)' }}>
              <div className="flex items-start justify-between">
                <div>
                  <h4 className="font-medium text-sm">{s.name}</h4>
                  {s.description && <p className="text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>{s.description}</p>}
                </div>
                <span className="text-xs px-2 py-1 rounded" style={{ background: 'var(--color-info-bg, #dbeafe)', color: 'var(--color-info, #1e40af)' }}>
                  {Math.round((s.probability || 0) * 100)}% prob
                </span>
              </div>
              {s.cac_estimate !== undefined && (
                <div className="grid grid-cols-3 gap-2 mt-2 text-center">
                  <div><p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>CAC</p><p className="font-medium">${s.cac_estimate}</p></div>
                  {s.ltv_estimate !== undefined && (
                    <div><p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>LTV</p><p className="font-medium">${s.ltv_estimate}</p></div>
                  )}
                  {s.break_even_months !== undefined && (
                    <div><p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Break-even</p><p className="font-medium">{s.break_even_months}mo</p></div>
                  )}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function LaunchPlanTab({ launchPlan }: { launchPlan: LaunchPlanPhase[] }) {
  if (launchPlan.length === 0)
    return (
      <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
        <p>No launch plan defined yet. Run full analysis to generate phases.</p>
      </div>
    );

  return (
    <div className="space-y-3">
      {launchPlan.map((phase, i) => (
        <div key={phase.id} className="border rounded p-3" style={{ borderColor: 'var(--color-border)' }}>
          <div className="flex items-center gap-3 mb-2">
            <span className="w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold" style={{ background: 'var(--color-primary)', color: 'white' }}>{i + 1}</span>
            <h4 className="font-medium">{phase.phase_name}</h4>
          </div>
          {phase.objectives && (
            <div className="mt-2">
              <p className="text-xs font-medium">Objectives:</p>
              <ul className="text-xs list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
                {phase.objectives.map((o, j) => <li key={j}>{o}</li>)}
              </ul>
            </div>
          )}
          {phase.kpis && (
            <div className="mt-1">
              <p className="text-xs font-medium">KPIs:</p>
              <ul className="text-xs list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
                {phase.kpis.map((k, j) => <li key={j}>{k}</li>)}
              </ul>
            </div>
          )}
          {phase.experiments && phase.experiments.length > 0 && (
            <div className="mt-2">
              <p className="text-xs font-medium">Experiments:</p>
              <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                {phase.experiments.map((exp, j) => (
                  <div key={j} className="mt-1">• {exp.name || exp.experiment_name || JSON.stringify(exp)}</div>
                ))}
              </div>
            </div>
          )}
          {phase.risks && phase.risks.length > 0 && (
            <div className="mt-2">
              <p className="text-xs font-medium" style={{ color: 'var(--color-destructive, #dc2626)' }}>Risks:</p>
              <ul className="text-xs list-disc list-inside">
                {phase.risks.map((r, j) => <li key={j}>{r}</li>)}
              </ul>
            </div>
          )}
          {phase.budget_estimate_usd && (
            <p className="text-xs mt-1 font-medium">Budget: ${phase.budget_estimate_usd.toLocaleString()}</p>
          )}
          {phase.exit_criteria && (
            <div className="mt-1">
              <p className="text-xs font-medium">Exit Criteria:</p>
              <ul className="text-xs list-disc list-inside" style={{ color: 'var(--color-muted-foreground)' }}>
                {phase.exit_criteria.map((c, j) => <li key={j}>{c}</li>)}
              </ul>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

function ReportTab({
  report,
  loading,
  onGenerateFullReport,
}: {
  report: ProductReport | null;
  loading: boolean;
  onGenerateFullReport: () => void;
}) {
  if (loading) return <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>Generating report...</p>;
  if (!report)
    return (
      <div className="text-center py-8" style={{ color: 'var(--color-muted-foreground)' }}>
        <p>No final report generated yet.</p>
        <button
          onClick={onGenerateFullReport}
          className="mt-3 px-4 py-2 text-sm font-medium rounded-lg"
          style={{ background: 'var(--color-primary)', color: 'white' }}
        >
          Generate Full Report with AI
        </button>
      </div>
    );

  return (
    <div className="prose max-w-none" style={{ color: 'var(--color-foreground)' }}>
      <div className="border-b pb-2 mb-4">
        <h3 className="text-lg font-semibold">{report.title}</h3>
        <div className="flex gap-4 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
          <span>Confidence: {report.confidence_level}</span>
          <span>Model: {report.ai_model_version}</span>
          <span>Generated: {new Date(report.created_at).toLocaleString()}</span>
        </div>
      </div>
      <div className="space-y-4 text-sm">
        <div>
          <h4 className="font-medium">Executive Summary</h4>
          <p className="mt-1">{report.executive_summary}</p>
        </div>
        <div>
          <h4 className="font-medium">Market Opportunity</h4>
          <p className="mt-1">{report.market_opportunity}</p>
        </div>
        <div>
          <h4 className="font-medium">Competitive Analysis</h4>
          <p className="mt-1">{report.competitive_analysis}</p>
        </div>
        <div>
          <h4 className="font-medium">Positioning</h4>
          <p className="mt-1">{report.positioning}</p>
        </div>
        <div>
          <h4 className="font-medium">Go-to-Market Strategy</h4>
          <p className="mt-1">{report.go_to_market}</p>
        </div>
        <div>
          <h4 className="font-medium">Risk Analysis</h4>
          <p className="mt-1">{report.risk_analysis}</p>
        </div>
        <div>
          <h4 className="font-medium">Recommendations</h4>
          <p className="mt-1">{report.recommendations}</p>
        </div>
      </div>
    </div>
  );
}

export default function ProductIntelligenceApp() {
  const [projects, setProjects] = useState<ResearchProject[]>([]);
  const [currentView, setCurrentView] = useState<ActiveTab>('projects');
  const [selectedProject, setSelectedProject] = useState<ResearchProject | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [loading, setLoading] = useState(true);

  const loadProjects = async () => {
    setLoading(true);
    const data = await apiClient.listResearchProjects();
    setProjects(data || []);
    setLoading(false);
  };

  useEffect(() => {
    loadProjects();
  }, []);

  const handleCreateProject = async (req: CreateProjectRequest) => {
    const created = await apiClient.createResearchProject(req);
    if (created) {
      setProjects([created as ResearchProject, ...projects]);
      setShowForm(false);
      setSelectedProject(created as ResearchProject);
      setCurrentView('project-detail');
    }
  };

  const handleDeleteProject = async (project: ResearchProject) => {
    if (!confirm(`Delete project "${project.name}"? This cannot be undone.`)) return;
    const success = await apiClient.deleteResearchProject(project.id);
    if (success) setProjects(projects.filter((p) => p.id !== project.id));
  };

  const handleProjectClick = (project: ResearchProject) => {
    setSelectedProject(project);
    setCurrentView('project-detail');
  };

  const handleUpdateProject = (updated: ResearchProject) => {
    setProjects(projects.map((p) => (p.id === updated.id ? updated : p)));
    if (selectedProject?.id === updated.id) setSelectedProject(updated);
  };

  const handleBack = () => {
    setCurrentView('projects');
    setSelectedProject(null);
  };

  return (
    <div>
      {currentView === 'projects' && !showForm && (
        <ProjectsList
          projects={projects}
          onProjectClick={handleProjectClick}
          onProjectCreate={() => setShowForm(true)}
          onProjectDelete={handleDeleteProject}
        />
      )}

      {currentView === 'projects' && showForm && (
        <ProjectForm
          onSubmit={handleCreateProject}
          onCancel={() => setShowForm(false)}
        />
      )}

      {currentView === 'project-detail' && selectedProject && (
        <ProjectDetailView
          project={selectedProject}
          onBack={handleBack}
          onUpdate={handleUpdateProject}
          onDelete={handleDeleteProject}
        />
      )}
    </div>
  );
}
