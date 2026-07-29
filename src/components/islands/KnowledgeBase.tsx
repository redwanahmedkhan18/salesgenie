import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { useAuth } from '../../auth/AuthProvider';
import { apiClient } from '../../lib/api-client';
import type { KnowledgeDocument, KnowledgeCategory, SearchHit } from '../../lib/types';

interface KnowledgeSearchResponse {
  total_hits: number;
  hits: KnowledgeDocument[];
  took_ms: number;
}

const documentTypeIcons: Record<string, string> = {
  article: '📄',
  faq: '❓',
  guide: '📚',
  policy: '📜',
  release_notes: '🚀',
  other: '📎',
};

const statusColors: Record<string, string> = {
  draft: 'bg-gray-500/15 text-gray-400',
  published: 'bg-green-500/15 text-green-400',
  archived: 'bg-orange-500/15 text-orange-400',
};

function toKnowledgeDocument(hit: SearchHit): KnowledgeDocument {
  return {
    id: hit.id,
    title: hit.title,
    slug: hit.document_id,
    content: hit.content || '',
    document_type: hit.metadata?.document_type as string || 'other',
    category: hit.metadata?.category as string || 'General',
    tags: hit.tags || null,
    status: hit.metadata?.status as string || 'draft',
    is_public: hit.metadata?.is_public as boolean ?? true,
    view_count: hit.metadata?.view_count as number || 0,
    word_count: hit.metadata?.word_count as number | null,
    language: hit.metadata?.language as string || 'en',
    source_url: hit.metadata?.source_url as string | null,
    created_at: hit.metadata?.created_at as string || new Date().toISOString(),
    updated_at: hit.metadata?.updated_at as string || new Date().toISOString(),
  };
}

export default function KnowledgeBase() {
  const { hasRole } = useAuth();
  const [activeRoute, setActiveRoute] = useState('knowledge');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [documents, setDocuments] = useState<KnowledgeDocument[]>([]);
  const [categories, setCategories] = useState<KnowledgeCategory[]>([]);
  const [loading, setLoading] = useState(true);
  const [totalHits, setTotalHits] = useState(0);
  const [tookMs, setTookMs] = useState(0);
  const [query, setQuery] = useState('');
  const [filterCategory, setFilterCategory] = useState<string | null>(null);
  const [filterType, setFilterType] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'documents' | 'categories'>('documents');
  const [selectedDoc, setSelectedDoc] = useState<KnowledgeDocument | null>(null);

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const [docsRes, catsRes] = await Promise.all([
          apiClient.searchDocuments({ query: '', index_types: ['knowledge'], size: 50 }),
          apiClient.fetchKnowledgeCategories(),
        ]);

        if (docsRes) {
          setDocuments(docsRes.hits.map(toKnowledgeDocument));
          setTotalHits(docsRes.total_hits);
          setTookMs(docsRes.took_ms);
        }

        if (catsRes) {
          setCategories(catsRes);
        }
      } catch (error) {
        console.error('Error loading knowledge data:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    try {
      const response = await apiClient.searchDocuments({ 
        query, 
        index_types: ['knowledge'],
        size: 50,
        tags: filterCategory ? [filterCategory] : undefined,
      });
      if (response) {
        setDocuments(response.hits.map(toKnowledgeDocument));
        setTotalHits(response.total_hits);
        setTookMs(response.took_ms);
      }
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setLoading(false);
    }
  };

  const clearFilters = () => {
    setQuery('');
    setFilterCategory(null);
    setFilterType(null);
  };

  const formatWordCount = (count: number | null) => {
    if (!count) return '-';
    if (count < 1000) return `${count} words`;
    return `${(count / 1000).toFixed(1)}k words`;
  };

  const getDocTypeIcon = (type: string) => {
    return documentTypeIcons[type] || documentTypeIcons.other;
  };

  const getStatusClass = (status: string) => {
    return statusColors[status] || statusColors.draft;
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Knowledge Base
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Manage documents, articles, and FAQs
            </p>
          </div>
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
        </header>

        <div className="px-6 py-6 space-y-6">
          {/* Tabs */}
          <div className="flex gap-1 p-1 rounded-lg" style={{ background: 'var(--color-muted)' }}>
            <button
              onClick={() => setActiveTab('documents')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'documents' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'documents' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'documents' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Documents
            </button>
            <button
              onClick={() => setActiveTab('categories')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'categories' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'categories' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'categories' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Categories
            </button>
          </div>

          {activeTab === 'documents' ? (
            <>
              {/* Search & Filters */}
              <div className="flex flex-col sm:flex-row gap-3">
                <input
                  type="text"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Search knowledge base..."
                  onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
                  className="flex-1 px-4 py-2.5 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
                <select
                  value={filterCategory || ''}
                  onChange={(e) => setFilterCategory(e.target.value || null)}
                  className="px-3 py-2 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                >
                  <option value="">All Categories</option>
                  {categories.map(cat => (
                    <option key={cat.id} value={cat.slug}>{cat.name}</option>
                  ))}
                </select>
                <select
                  value={filterType || ''}
                  onChange={(e) => setFilterType(e.target.value || null)}
                  className="px-3 py-2 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                >
                  <option value="">All Types</option>
                  <option value="article">Article</option>
                  <option value="faq">FAQ</option>
                  <option value="guide">Guide</option>
                  <option value="policy">Policy</option>
                  <option value="release_notes">Release Notes</option>
                </select>
                <button
                  onClick={handleSearch}
                  className="px-4 py-2 text-sm font-semibold rounded-xl transition-all"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                >
                  Search
                </button>
                <button
                  onClick={clearFilters}
                  className="px-4 py-2 text-sm rounded-xl transition-colors"
                  style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}
                >
                  Clear
                </button>
              </div>

              {/* Results Summary */}
              <div className="flex items-center justify-between text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                <span>{totalHits} documents in {tookMs}ms</span>
              </div>

              {/* Documents Table */}
              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="overflow-x-auto">
                  <table className="w-full">
                    <thead>
                      <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Title</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Type</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Category</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Views</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Updated</th>
                      </tr>
                    </thead>
                    <tbody>
                      {loading ? (
                        <tr>
                          <td colSpan={6} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            Loading documents...
                          </td>
                        </tr>
                      ) : documents.length === 0 ? (
                        <tr>
                          <td colSpan={6} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            No documents found
                          </td>
                        </tr>
                      ) : (
                        documents.map(doc => (
                          <tr key={doc.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                            <td className="px-4 py-3">
                              <div className="flex items-center gap-2">
                                <span className="text-xl">{getDocTypeIcon(doc.document_type)}</span>
                                <div>
                                  <div
                                    className="font-semibold text-sm cursor-pointer hover:underline"
                                    style={{ color: 'var(--color-foreground)' }}
                                    onClick={() => setSelectedDoc(doc)}
                                  >
                                    {doc.title}
                                  </div>
                                  {doc.tags && doc.tags.length > 0 && (
                                    <div className="flex flex-wrap gap-1 mt-1">
                                      {doc.tags.slice(0, 3).map(tag => (
                                        <span key={tag} className="text-xs px-1.5 py-0.5 rounded"
                                          style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}>
                                          {tag}
                                        </span>
                                      ))}
                                    </div>
                                  )}
                                </div>
                              </div>
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                              {doc.document_type}
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                              {doc.category}
                            </td>
                            <td className="px-4 py-3">
                              <span className={`text-xs px-2 py-1 rounded-full ${getStatusClass(doc.status)}`}>
                                {doc.status}
                              </span>
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                              {doc.view_count}
                            </td>
                            <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                              {new Date(doc.updated_at).toLocaleDateString()}
                            </td>
                          </tr>
                        ))
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </>
          ) : (
            /* Categories Tab */
            <div className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {categories.map(cat => (
                  <div key={cat.id} className="rounded-xl p-4 border"
                    style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="flex items-center gap-3 mb-3">
                      <div
                        className="w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold"
                        style={{ background: cat.color || 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                      >
                        📁
                      </div>
                      <div>
                        <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{cat.name}</h3>
                        <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{cat.slug}</p>
                      </div>
                    </div>
                    <p className="text-xs mb-3" style={{ color: 'var(--color-muted-foreground)' }}>
                      {cat.description || 'No description'}
                    </p>
                    <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>
                      {cat.document_count} documents
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </main>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}