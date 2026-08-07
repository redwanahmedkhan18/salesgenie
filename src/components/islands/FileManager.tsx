import React, { useState, useEffect } from 'react';
import { Sidebar, CommandPalette } from './AppShell';
import { FILE_SERVICE_URL } from '../../lib/api-client';

interface FileMetadata {
  id: string;
  filename: string;
  file_size: number;
  content_type: string;
  file_category: string;
  visibility: string;
  version: number;
  is_deleted: boolean;
  uploaded_by: string | null;
  download_count: number;
  tags: string[] | null;
  download_url: string;
  tenant_id: string;
  created_at: string;
  updated_at: string;
}

interface FileOverview {
  total_files: number;
  total_size_bytes: number;
  total_size_mb: number;
  files_by_category: Record<string, number>;
  files_by_visibility: Record<string, number>;
  top_tags: Array<{ tag: string; count: number }>;
  recent_uploads: FileMetadata[];
  storage_usage: Record<string, number>;
}

interface FileSearchResponse {
  total_hits: number;
  hits: FileMetadata[];
  took_ms: number;
}

const categoryIcons: Record<string, string> = {
  document: '📄',
  image: '🖼️',
  video: '🎥',
  audio: '🎵',
  spreadsheet: '📊',
  presentation: '📽️',
  archive: '📦',
  other: '📎',
};

const visibilityColors: Record<string, string> = {
  private: 'bg-red-500/15 text-red-400',
  tenant: 'bg-blue-500/15 text-blue-400',
  public: 'bg-green-500/15 text-green-400',
};

export default function FileManager() {
  const [activeRoute, setActiveRoute] = useState('files');
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [files, setFiles] = useState<FileMetadata[]>([]);
  const [overview, setOverview] = useState<FileOverview | null>(null);
  const [loading, setLoading] = useState(true);
  const [totalHits, setTotalHits] = useState(0);
  const [tookMs, setTookMs] = useState(0);
  const [query, setQuery] = useState('');
  const [filterCategory, setFilterCategory] = useState<string | null>(null);
  const [filterVisibility, setFilterVisibility] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'files' | 'overview'>('files');
  const [uploadModal, setUploadModal] = useState(false);

  const fileServiceUrl = FILE_SERVICE_URL;

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      try {
        const [filesRes, overviewRes] = await Promise.all([
          fetch(`${fileServiceUrl}/files?size=50`, {
            headers: { 'Content-Type': 'application/json' },
          }),
          fetch(`${fileServiceUrl}/files/overview`, {
            headers: { 'Content-Type': 'application/json' },
          }),
        ]);

        if (filesRes.ok) {
          const filesData: FileSearchResponse = await filesRes.json();
          setFiles(filesData.hits);
          setTotalHits(filesData.total_hits);
          setTookMs(filesData.took_ms);
        }

        if (overviewRes.ok) {
          const overviewData: FileOverview = await overviewRes.json();
          setOverview(overviewData);
        }
      } catch (error) {
        console.error('Error loading file data:', error);
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
      const params = new URLSearchParams();
      params.set('q', query);
      params.set('size', '50');
      if (filterCategory) params.set('file_categories', filterCategory);
      if (filterVisibility) params.set('visibility', filterVisibility);

      const response = await fetch(
        `${fileServiceUrl}/files?${params.toString()}`,
        { headers: { 'Content-Type': 'application/json' } }
      );

      if (response.ok) {
        const data: FileSearchResponse = await response.json();
        setFiles(data.hits);
        setTotalHits(data.total_hits);
        setTookMs(data.took_ms);
      }
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleUpload = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const file = formData.get('file') as File;
    const visibility = formData.get('visibility') as string;
    const tags = formData.get('tags') as string;

    if (!file) return;

    const uploadFormData = new FormData();
    uploadFormData.append('file', file);
    uploadFormData.append('visibility', visibility);
    if (tags) uploadFormData.append('tags', tags);

    try {
      const response = await fetch(`${fileServiceUrl}/files/upload`, {
        method: 'POST',
        body: uploadFormData,
      });

      if (response.ok) {
        const result = await response.json();
        setFiles([result, ...files]);
        setUploadModal(false);
        (e.target as HTMLFormElement).reset();
      }
    } catch (error) {
      console.error('Upload failed:', error);
    }
  };

  const handleDelete = async (fileId: string) => {
    if (!confirm('Are you sure you want to delete this file?')) return;

    try {
      const response = await fetch(`${fileServiceUrl}/files/${fileId}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
      });

      if (response.ok) {
        setFiles(files.filter(f => f.id !== fileId));
      }
    } catch (error) {
      console.error('Delete failed:', error);
    }
  };

  const clearFilters = () => {
    setQuery('');
    setFilterCategory(null);
    setFilterVisibility(null);
  };

  const formatFileSize = (bytes: number) => {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
  };

  const getCategoryIcon = (category: string) => {
    return categoryIcons[category] || categoryIcons.other;
  };

  const getVisibilityClass = (visibility: string) => {
    return visibilityColors[visibility] || visibilityColors.private;
  };

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      <Sidebar activeRoute={activeRoute} onRouteChange={setActiveRoute} />

      <main className="flex-1 overflow-y-auto">
        <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
          style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
          <div>
            <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
              File Manager
            </h1>
            <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
              Manage files, uploads, and shared links
            </p>
          </div>
          <div className="flex items-center gap-3">
            <button
              onClick={() => setUploadModal(true)}
              className="px-4 py-2 text-sm font-semibold rounded-lg transition-all"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              + Upload
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
          {/* Tabs */}
          <div className="flex gap-1 p-1 rounded-lg" style={{ background: 'var(--color-muted)' }}>
            <button
              onClick={() => setActiveTab('files')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'files' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'files' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'files' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Files
            </button>
            <button
              onClick={() => setActiveTab('overview')}
              className={`flex-1 px-4 py-2 text-sm font-semibold rounded-md transition-all ${
                activeTab === 'overview' ? 'shadow' : 'hover:opacity-80'
              }`}
              style={{
                background: activeTab === 'overview' ? 'var(--color-card)' : 'transparent',
                color: activeTab === 'overview' ? 'var(--color-foreground)' : 'var(--color-muted-foreground)',
              }}
            >
              Overview
            </button>
          </div>

          {activeTab === 'files' ? (
            <>
              {/* Search & Filters */}
              <div className="flex flex-col sm:flex-row gap-3">
                <input
                  type="text"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Search files..."
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
                  <option value="document">Document</option>
                  <option value="image">Image</option>
                  <option value="video">Video</option>
                  <option value="audio">Audio</option>
                  <option value="spreadsheet">Spreadsheet</option>
                  <option value="presentation">Presentation</option>
                  <option value="archive">Archive</option>
                </select>
                <select
                  value={filterVisibility || ''}
                  onChange={(e) => setFilterVisibility(e.target.value || null)}
                  className="px-3 py-2 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                >
                  <option value="">All Visibility</option>
                  <option value="private">Private</option>
                  <option value="tenant">Tenant</option>
                  <option value="public">Public</option>
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
                <span>{totalHits} files in {tookMs}ms</span>
              </div>

              {/* Files Table */}
              <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                <div className="overflow-x-auto">
                  <table className="w-full">
                    <thead>
                      <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>File</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Category</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Size</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Visibility</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Downloads</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Uploaded</th>
                        <th className="text-left px-4 py-3 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {loading ? (
                        <tr>
                          <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            Loading files...
                          </td>
                        </tr>
                      ) : files.length === 0 ? (
                        <tr>
                          <td colSpan={7} className="px-4 py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                            No files found
                          </td>
                        </tr>
                      ) : (
                        files.map(file => (
                          <tr key={file.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                            <td className="px-4 py-3">
                              <div className="flex items-center gap-2">
                                <span className="text-xl">{getCategoryIcon(file.file_category)}</span>
                                <div>
                                  <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{file.filename}</div>
                                  {file.tags && file.tags.length > 0 && (
                                    <div className="flex flex-wrap gap-1 mt-1">
                                      {file.tags.slice(0, 3).map(tag => (
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
                              {file.file_category}
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-foreground)' }}>
                              {formatFileSize(file.file_size)}
                            </td>
                            <td className="px-4 py-3">
                              <span className={`text-xs px-2 py-1 rounded-full ${getVisibilityClass(file.visibility)}`}>
                                {file.visibility}
                              </span>
                            </td>
                            <td className="px-4 py-3 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                              {file.download_count}
                            </td>
                            <td className="px-4 py-3 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                              {new Date(file.created_at).toLocaleDateString()}
                            </td>
                            <td className="px-4 py-3">
                              <div className="flex gap-2">
                                <a
                                  href={file.download_url}
                                  className="text-xs px-2 py-1 rounded hover:underline"
                                  style={{ color: 'var(--color-primary)' }}
                                >
                                  Download
                                </a>
                                <button
                                  onClick={() => handleDelete(file.id)}
                                  className="text-xs px-2 py-1 rounded hover:underline"
                                  style={{ color: '#cd4239' }}
                                >
                                  Delete
                                </button>
                              </div>
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
            /* Overview Tab */
            overview && (
              <div className="space-y-6">
                {/* Summary Cards */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                  <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Files</div>
                    <div className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>{overview.total_files.toLocaleString()}</div>
                  </div>
                  <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Total Size</div>
                    <div className="text-2xl font-bold" style={{ color: '#2c84e0' }}>{overview.total_size_mb.toFixed(1)} MB</div>
                  </div>
                  <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Categories</div>
                    <div className="text-2xl font-bold" style={{ color: '#2c8c66' }}>{Object.keys(overview.files_by_category).length}</div>
                  </div>
                  <div className="rounded-xl p-4 border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                    <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>Public Files</div>
                    <div className="text-2xl font-bold" style={{ color: '#7c44a6' }}>{overview.files_by_visibility.public || 0}</div>
                  </div>
                </div>

                {/* Files by Category */}
                <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Files by Category</h3>
                  <div className="space-y-2">
                    {Object.entries(overview.files_by_category).map(([category, count]) => (
                      <div key={category} className="flex items-center gap-3">
                        <span className="w-24 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          {getCategoryIcon(category)} {category}
                        </span>
                        <div className="flex-1 h-2 rounded" style={{ background: 'var(--color-muted)' }}>
                          <div
                            className="h-2 rounded"
                            style={{
                              width: `${(count / overview.total_files) * 100}%`,
                              background: 'var(--color-primary)',
                            }}
                          />
                        </div>
                        <span className="text-sm" style={{ color: 'var(--color-foreground)' }}>{count}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Storage Usage */}
                <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Storage Usage by Category</h3>
                  <div className="space-y-2">
                    {Object.entries(overview.storage_usage).map(([category, size]) => (
                      <div key={category} className="flex items-center gap-3">
                        <span className="w-24 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                          {getCategoryIcon(category)} {category}
                        </span>
                        <div className="flex-1 h-2 rounded" style={{ background: 'var(--color-muted)' }}>
                          <div
                            className="h-2 rounded"
                            style={{
                              width: `${(size / overview.total_size_bytes) * 100}%`,
                              background: '#2c8c66',
                            }}
                          />
                        </div>
                        <span className="text-sm" style={{ color: 'var(--color-foreground)' }}>{formatFileSize(size)}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Top Tags */}
                <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Top Tags</h3>
                  <div className="flex flex-wrap gap-2">
                    {overview.top_tags.map((item) => (
                      <div key={item.tag} className="flex items-center gap-2 px-3 py-1.5 rounded-lg"
                        style={{ background: 'var(--color-muted)' }}>
                        <span className="text-sm" style={{ color: 'var(--color-foreground)' }}>{item.tag}</span>
                        <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{item.count}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Recent Uploads */}
                <div className="rounded-xl border p-4" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
                  <h3 className="text-sm font-semibold mb-3" style={{ color: 'var(--color-foreground)' }}>Recent Uploads</h3>
                  <div className="space-y-2">
                    {overview.recent_uploads.map(file => (
                      <div key={file.id} className="flex items-center gap-3">
                        <span className="text-xl">{getCategoryIcon(file.file_category)}</span>
                        <div className="flex-1">
                          <div className="text-sm font-medium" style={{ color: 'var(--color-foreground)' }}>{file.filename}</div>
                          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                            {formatFileSize(file.file_size)} · {new Date(file.created_at).toLocaleDateString()}
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )
          )}
        </div>
      </main>

      {/* Upload Modal */}
      {uploadModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="rounded-xl p-6 w-full max-w-md" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <h2 className="text-lg font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Upload File</h2>
            <form onSubmit={handleUpload} className="space-y-4">
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  File *
                </label>
                <input
                  type="file"
                  name="file"
                  required
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Visibility
                </label>
                <select
                  name="visibility"
                  defaultValue="private"
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                >
                  <option value="private">Private</option>
                  <option value="tenant">Tenant</option>
                  <option value="public">Public</option>
                </select>
              </div>
              <div>
                <label className="text-xs font-semibold block mb-1" style={{ color: 'var(--color-muted-foreground)' }}>
                  Tags (comma-separated)
                </label>
                <input
                  type="text"
                  name="tags"
                  placeholder="e.g. important, q3, finance"
                  className="w-full px-3 py-2 rounded-lg text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div className="flex justify-end gap-3 pt-4">
                <button
                  type="button"
                  onClick={() => setUploadModal(false)}
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
                  Upload
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