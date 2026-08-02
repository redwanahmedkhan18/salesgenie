import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';
import type { KnowledgeCategory, KnowledgeDocument } from '../../lib/types';

interface KnowledgeBaseManagerProps {
  tenantId: string;
}

export default function KnowledgeBaseManager({ tenantId }: KnowledgeBaseManagerProps) {
  const [categories, setCategories] = useState<KnowledgeCategory[]>([]);
  const [documents, setDocuments] = useState<KnowledgeDocument[]>([]);
  const [loading, setLoading] = useState(true);
  const [showAddDoc, setShowAddDoc] = useState(false);
  const [newDoc, setNewDoc] = useState({
    title: '',
    content: '',
    category: '',
    tags: '',
  });

  useEffect(() => {
    loadData();
  }, [tenantId]);

  const loadData = async () => {
    setLoading(true);
    try {
      const [categoriesRes, docsRes] = await Promise.all([
        apiClient.fetchKnowledgeCategories(),
        apiClient.fetchDocuments(tenantId),
      ]);
      setCategories(categoriesRes || []);
      setDocuments(docsRes || []);
    } catch (error) {
      console.error('Failed to load knowledge data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddDocument = async () => {
    if (!newDoc.title || !newDoc.content) return;
    
    try {
      await apiClient.createDocument({
        title: newDoc.title,
        content: newDoc.content,
        category: newDoc.category,
        tags: newDoc.tags.split(',').map(t => t.trim()),
        tenant_id: tenantId,
      });
      setShowAddDoc(false);
      setNewDoc({ title: '', content: '', category: '', tags: '' });
      loadData();
    } catch (error) {
      console.error('Failed to add document:', error);
    }
  };

  if (loading) {
    return <div className="text-center py-8">Loading knowledge base...</div>;
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Knowledge Base</h3>
        <button
          onClick={() => setShowAddDoc(true)}
          className="text-xs px-3 py-1 rounded"
          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
        >
          Add Document
        </button>
      </div>

      {/* Add Document Modal */}
      {showAddDoc && (
        <div className="rounded-xl p-4" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <h4 className="font-semibold mb-3">Add New Document</h4>
          <div className="space-y-3">
            <input
              type="text"
              placeholder="Document Title"
              value={newDoc.title}
              onChange={e => setNewDoc({ ...newDoc, title: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <textarea
              placeholder="Content"
              value={newDoc.content}
              onChange={e => setNewDoc({ ...newDoc, content: e.target.value })}
              rows={4}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="text"
              placeholder="Category ID (optional)"
              value={newDoc.category}
              onChange={e => setNewDoc({ ...newDoc, category: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
            <input
              type="text"
              placeholder="Tags (comma separated)"
              value={newDoc.tags}
              onChange={e => setNewDoc({ ...newDoc, tags: e.target.value })}
              className="w-full px-3 py-2 rounded border"
              style={{ background: 'var(--color-card)', color: 'var(--color-foreground)', borderColor: 'var(--color-border)' }}
            />
          </div>
          <div className="mt-4 flex gap-2">
            <button onClick={handleAddDocument} style={{ color: 'var(--color-on-primary)' }}>Save</button>
            <button onClick={() => setShowAddDoc(false)} style={{ color: 'var(--color-muted-foreground)' }}>Cancel</button>
          </div>
        </div>
      )}

      {/* Categories */}
      <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="p-4 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <h4 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Categories</h4>
        </div>
        <div className="p-4">
          {categories.length > 0 ? (
            <div className="flex flex-wrap gap-2">
              {categories.map(cat => (
                <span key={cat.id} className="px-3 py-1 text-xs rounded" style={{ background: 'var(--color-secondary)/10', color: 'var(--color-secondary)' }}>
                  {cat.name}
                </span>
              ))}
            </div>
          ) : (
            <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No categories yet.</p>
          )}
        </div>
      </div>

      {/* Documents */}
      <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="p-4 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <h4 className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>Documents</h4>
        </div>
        <div className="p-4">
          {documents.length > 0 ? (
            <table className="w-full">
              <thead>
                <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                  <th className="text-left px-3 py-2 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Title</th>
                  <th className="text-left px-3 py-2 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Category</th>
                  <th className="text-left px-3 py-2 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Tags</th>
                  <th className="text-left px-3 py-2 text-xs font-semibold" style={{ color: 'var(--color-muted-foreground)' }}>Created</th>
                </tr>
              </thead>
              <tbody>
                {documents.slice(0, 10).map(doc => (
                  <tr key={doc.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                    <td className="px-3 py-2 text-sm">{doc.title}</td>
                    <td className="px-3 py-2 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>{doc.category || '-'}</td>
                    <td className="px-3 py-2 text-xs">
                      {doc.tags?.map(t => (
                        <span key={t} className="px-2 py-0.5 mr-1 text rounded" style={{ background: 'var(--color-secondary)/10', color: 'var(--color-secondary)' }}>
                          {t}
                        </span>
                      ))}
                    </td>
                    <td className="px-3 py-2 text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                      {new Date(doc.created_at).toLocaleDateString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>No documents yet.</p>
          )}
        </div>
      </div>
    </div>
  );
}