import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';

interface PromptTemplate {
  id: string;
  name: string;
  description: string | null;
  content: string;
  category: string;
  is_active: boolean;
  version: number;
  created_by: string | null;
  created_at: string;
  updated_at: string;
}

interface PromptCategory {
  name: string;
  count: number;
}

export default function PromptManagement() {
  const [activeRoute, setActiveRoute] = useState('prompts');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [prompts, setPrompts] = useState<PromptTemplate[]>([]);
  const [loading, setLoading] = useState(true);
  const [query, setQuery] = useState('');
  const [filterCategory, setFilterCategory] = useState<string | null>(null);
  const [selectedPrompt, setSelectedPrompt] = useState<PromptTemplate | null>(null);
  const [showModal, setShowModal] = useState(false);

  const aiGatewayUrl = import.meta.env.DEV ? 'http://localhost:8000' : '/api';

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const response = await fetch(`${aiGatewayUrl}/prompts`, {
          headers: { 'Content-Type': 'application/json' },
        });

        if (response.ok) {
          const data = await response.json();
          setPrompts(data.prompts || data);
        }
      } catch (error) {
        console.error('Error loading prompts:', error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const getCategories = (): PromptCategory[] => {
    const catMap: Record<string, number> = {};
    prompts.forEach(p => {
      catMap[p.category] = (catMap[p.category] || 0) + 1;
    });
    return Object.entries(catMap).map(([name, count]) => ({ name, count }));
  };

  const categories = getCategories();

  const filteredPrompts = prompts.filter(p => {
    if (query && !p.name.toLowerCase().includes(query.toLowerCase()) &&
        !p.content.toLowerCase().includes(query.toLowerCase())) {
      return false;
    }
    if (filterCategory && p.category !== filterCategory) {
      return false;
    }
    return true;
  });

  const clearFilters = () => {
    setQuery('');
    setFilterCategory(null);
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Prompt Management
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Manage AI agent system prompts and templates
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
          {/* Search & Filters */}
          <div className="flex flex-col sm:flex-row gap-3">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search prompts..."
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
                <option key={cat.name} value={cat.name}>{cat.name} ({cat.count})</option>
              ))}
            </select>
            <button
              onClick={() => setShowModal(true)}
              className="px-4 py-2 text-sm font-semibold rounded-xl transition-all"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              + New Prompt
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
          <div className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
            {filteredPrompts.length} prompts found
          </div>

          {/* Prompts Table */}
          <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Name</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Category</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Status</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Version</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Content Preview</th>
                    <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Updated</th>
                  </tr>
                </thead>
                <tbody>
                  {loading ? (
                    <tr>
                      <td colSpan={6} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                        Loading prompts...
                      </td>
                    </tr>
                  ) : filteredPrompts.length === 0 ? (
                    <tr>
                      <td colSpan={6} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                        No prompts found
                      </td>
                    </tr>
                  ) : (
                    filteredPrompts.map(prompt => (
                      <tr key={prompt.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td className="px-4 py-3">
                          <div
                            className="font-semibold text-sm cursor-pointer hover:underline"
                            style={{ color: 'var(--color-foreground)' }}
                            onClick={() => setSelectedPrompt(prompt)}
                          >
                            {prompt.name}
                          </div>
                          {prompt.description && (
                            <div className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                              {prompt.description}
                            </div>
                          )}
                        </td>
                        <td className="px-4 py-3">
                          <span className="text-xs px-2 py-1 rounded"
                            style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}>
                            {prompt.category}
                          </span>
                        </td>
                        <td className="px-4 py-3">
                          <span className={`text-xs px-2 py-1 rounded-full ${
                            prompt.is_active
                              ? 'bg-green-500/15 text-green-400'
                              : 'bg-gray-500/15 text-gray-400'
                          }`}>
                            {prompt.is_active ? 'Active' : 'Inactive'}
                          </span>
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                          v{prompt.version}
                        </td>
                        <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                          {prompt.content.substring(0, 60)}...
                        </td>
                        <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          {new Date(prompt.updated_at).toLocaleDateString()}
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

      {/* Prompt Detail Modal */}
      {selectedPrompt && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div className="rounded-xl w-full max-w-4xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <div className="p-6 border-b" style={{ borderColor: 'var(--color-border)' }}>
              <div className="flex items-center justify-between">
                <h2 className="text-lg font-bold" style={{ color: 'var(--color-foreground)' }}>{selectedPrompt.name}</h2>
                <button
                  onClick={() => setSelectedPrompt(null)}
                  className="text-sm"
                  style={{ color: 'var(--color-muted-foreground)' }}
                >
                  ✕
                </button>
              </div>
              <div className="text-xs mt-1" style={{ color: 'var(--color-muted-foreground)' }}>
                {selectedPrompt.description || 'No description'}
              </div>
            </div>
            <div className="p-6">
              <div className="mb-4">
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Category
                </label>
                <div className="text-sm" style={{ color: 'var(--color-foreground)' }}>{selectedPrompt.category}</div>
              </div>
              <div className="mb-4">
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Status
                </label>
                <span className={`text-xs px-2 py-1 rounded-full ${
                  selectedPrompt.is_active
                    ? 'bg-green-500/15 text-green-400'
                    : 'bg-gray-500/15 text-gray-400'
                }`}>
                  {selectedPrompt.is_active ? 'Active' : 'Inactive'}
                </span>
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Prompt Content
                </label>
                <textarea
                  readOnly
                  value={selectedPrompt.content}
                  className="w-full h-64 px-3 py-2 rounded-lg text-sm outline-none resize-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
            </div>
          </div>
        </div>
      )}

      {/* New Prompt Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div className="rounded-xl w-full max-w-3xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <div className="p-6 border-b" style={{ borderColor: 'var(--color-border)' }}>
              <h2 className="text-lg font-bold" style={{ color: 'var(--color-foreground)' }}>Create New Prompt</h2>
            </div>
            <div className="p-6">
              <form className="space-y-4">
                <div>
                  <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    Name *
                  </label>
                  <input
                    type="text"
                    required
                    className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                    style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                  />
                </div>
                <div>
                  <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    Description
                  </label>
                  <input
                    type="text"
                    className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                    style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                  />
                </div>
                <div>
                  <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    Category
                  </label>
                  <select
                    className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                    style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                  >
                    <option value="system">System</option>
                    <option value="sales">Sales</option>
                    <option value="support">Support</option>
                    <option value="knowledge">Knowledge</option>
                    <option value="workflow">Workflow</option>
                    <option value="custom">Custom</option>
                  </select>
                </div>
                <div>
                  <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                    Prompt Content *
                  </label>
                  <textarea
                    required
                    rows={8}
                    className="w-full px-3 py-2 rounded-lg text-sm outline-none resize-none"
                    style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                    placeholder="Enter prompt template content..."
                  />
                </div>
              </form>
            </div>
            <div className="p-6 border-t flex justify-end gap-3" style={{ borderColor: 'var(--color-border)' }}>
              <button
                onClick={() => setShowModal(false)}
                className="px-4 py-2 text-sm rounded-lg transition-colors"
                style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}
              >
                Cancel
              </button>
              <button
                className="px-4 py-2 text-sm font-semibold rounded-lg transition-all"
                style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
              >
                Create
              </button>
            </div>
          </div>
        </div>
      )}

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}
