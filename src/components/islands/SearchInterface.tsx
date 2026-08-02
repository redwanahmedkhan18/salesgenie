import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { apiClient } from '../../lib/api-client';

interface SearchHit {
  id: string;
  index_type: string;
  document_id: string;
  title: string;
  content: string;
  tags?: string[];
  score: number;
  highlights?: Record<string, string[]>;
}

interface SearchResponse {
  query: string;
  total_hits: number;
  hits: SearchHit[];
  took_ms: number;
}

export default function SearchInterface() {
  const [activeRoute, setActiveRoute] = useState('search');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchHit[]>([]);
  const [loading, setLoading] = useState(false);
  const [totalHits, setTotalHits] = useState(0);
  const [tookMs, setTookMs] = useState(0);
  const [selectedTypes, setSelectedTypes] = useState<string[]>([]);
  const [searchHistory, setSearchHistory] = useState<string[]>([]);

  const searchTypes = [
    { value: 'document', label: 'Documents', icon: '📄' },
    { value: 'customer', label: 'Customers', icon: '👥' },
    { value: 'ticket', label: 'Tickets', icon: '🎫' },
    { value: 'conversation', label: 'Conversations', icon: '💬' },
    { value: 'knowledge_base', label: 'Knowledge Base', icon: '📚' },
  ];

  const handleSearch = async (searchQuery: string) => {
    if (!searchQuery.trim()) return;
    
    setLoading(true);
    try {
      const response = await fetch(
        `${import.meta.env.DEV ? 'http://localhost:8013/api/v1' : '/api/v1'}/search/search?q=${encodeURIComponent(searchQuery)}&size=20`,
        {
          headers: { 'Content-Type': 'application/json' },
        }
      );
      
      if (response.ok) {
        const data: SearchResponse = await response.json();
        setResults(data.hits);
        setTotalHits(data.total_hits);
        setTookMs(data.took_ms);
        
        if (!searchHistory.includes(searchQuery)) {
          setSearchHistory([searchQuery, ...searchHistory.slice(0, 4)]);
        }
      }
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    handleSearch(query);
  };

  const toggleType = (type: string) => {
    if (selectedTypes.includes(type)) {
      setSelectedTypes(selectedTypes.filter(t => t !== type));
    } else {
      setSelectedTypes([...selectedTypes, type]);
    }
  };

  const clearFilters = () => {
    setSelectedTypes([]);
  };

  const getTypeName = (type: string) => {
    return searchTypes.find(t => t.value === type)?.label || type;
  };

  const getTypeIcon = (type: string) => {
    return searchTypes.find(t => t.value === type)?.icon || '📄';
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              Search
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Full-text search across knowledge base, customers, tickets, and conversations
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
          {/* Search Form */}
          <form onSubmit={handleSearchSubmit} className="flex gap-3">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search across all content..."
              className="flex-1 px-4 py-3 rounded-xl text-sm outline-none"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
            />
            <button
              type="submit"
              disabled={loading || !query.trim()}
              className="px-6 py-3 text-sm font-semibold rounded-xl transition-all disabled:opacity-60"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              {loading ? 'Searching...' : 'Search'}
            </button>
          </form>

          {/* Search Type Filters */}
          <div className="flex flex-wrap gap-2">
            {searchTypes.map(type => (
              <button
                key={type.value}
                onClick={() => toggleType(type.value)}
                className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs transition-all ${
                  selectedTypes.includes(type.value)
                    ? 'ring-2 ring-amber-500'
                    : 'hover:bg-white/5'
                }`}
                style={{
                  background: selectedTypes.includes(type.value) 
                    ? 'rgba(247,165,1,0.15)' 
                    : 'var(--color-muted)',
                  color: selectedTypes.includes(type.value) 
                    ? 'var(--color-primary)' 
                    : 'var(--color-muted-foreground)',
                }}
              >
                <span>{type.icon}</span>
                {type.label}
              </button>
            ))}
            {selectedTypes.length > 0 && (
              <button
                onClick={clearFilters}
                className="text-xs px-3 py-1.5 rounded-lg hover:bg-white/5"
                style={{ color: 'var(--color-muted-foreground)' }}
              >
                Clear Filters
              </button>
            )}
          </div>

          {/* Search History */}
          {searchHistory.length > 0 && !loading && results.length === 0 && (
            <div className="space-y-2">
              <div className="text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>
                Recent Searches
              </div>
              {searchHistory.map((term, i) => (
                <button
                  key={i}
                  onClick={() => handleSearch(term)}
                  className="flex items-center gap-2 text-sm hover:underline"
                  style={{ color: 'var(--color-foreground)' }}
                >
                  <span>🔍</span>
                  {term}
                </button>
              ))}
            </div>
          )}

          {/* Search Results */}
          {loading ? (
            <div className="space-y-4">
              {Array.from({ length: 5 }).map((_, i) => (
                <div key={i} className="rounded-xl p-4 border skeleton"
                  style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <div className="h-5 w-3/4 rounded mb-2" style={{ background: 'var(--color-muted)' }} />
                  <div className="h-3 w-1/2 rounded mb-3" style={{ background: 'var(--color-muted)' }} />
                  <div className="h-3 w-full rounded mb-2" style={{ background: 'var(--color-muted)' }} />
                  <div className="h-3 w-2/3 rounded" style={{ background: 'var(--color-muted)' }} />
                </div>
              ))}
            </div>
          ) : results.length > 0 ? (
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                  {totalHits} results in {tookMs}ms
                </div>
                {selectedTypes.length > 0 && (
                  <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                    Filtered by: {selectedTypes.map(t => getTypeName(t)).join(', ')}
                  </div>
                )}
              </div>
              
              {results.map(hit => (
                <div key={hit.id} className="rounded-xl p-4 border transition-colors hover:bg-white/3"
                  style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <div className="flex items-start gap-3">
                    <span className="text-xl">{getTypeIcon(hit.index_type)}</span>
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-1">
                        <span className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>
                          {hit.title}
                        </span>
                        <span className="text-xs px-2 py-0.5 rounded"
                          style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}>
                          {getTypeName(hit.index_type)}
                        </span>
                        <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          Score: {hit.score.toFixed(2)}
                        </span>
                      </div>
                      <div className="text-sm text-justify" style={{ color: 'var(--color-muted-foreground)' }}>
                        {hit.content.substring(0, 200)}...
                      </div>
                      {hit.tags && hit.tags.length > 0 && (
                        <div className="flex flex-wrap gap-1 mt-2">
                          {hit.tags.map(tag => (
                            <span key={tag} className="text-xs px-2 py-0.5 rounded"
                              style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)' }}>
                              {tag}
                            </span>
                          ))}
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : query && !loading ? (
            <div className="text-center py-12" style={{ color: 'var(--color-muted-foreground)' }}>
              <div className="text-4xl mb-4">🔍</div>
              <h3 className="text-lg font-semibold mb-2" style={{ color: 'var(--color-foreground)' }}>
                No results found
              </h3>
              <p>No results for "{query}"</p>
            </div>
          ) : (
            <div className="text-center py-12" style={{ color: 'var(--color-muted-foreground)' }}>
              <div className="text-4xl mb-4">🔍</div>
              <h3 className="text-lg font-semibold mb-2" style={{ color: 'var(--color-foreground)' }}>
                Search the Knowledge Base
              </h3>
              <p>Enter a search query to find documents, customers, tickets, and conversations.</p>
            </div>
          )}
        </div>
      </main>

      <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={setActiveRoute} />
    </div>
  );
}