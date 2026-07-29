import React, { useState, useEffect } from 'react';
import { apiClient } from '../../lib/api-client';
import type { WorkspaceMember, PlatformRole } from '../../lib/types';

const ROLE_OPTIONS: { value: PlatformRole; label: string; description: string }[] = [
  { value: 'super_admin', label: 'Super Admin', description: 'Full platform access' },
  { value: 'workspace_admin', label: 'Workspace Admin', description: 'Organization-wide management' },
  { value: 'org_admin', label: 'Organization Admin', description: 'Organization management' },
  { value: 'sales_manager', label: 'Sales Manager', description: 'Manage sales team and leads' },
  { value: 'sales_agent', label: 'Sales Agent', description: 'Handle sales inquiries' },
  { value: 'support_manager', label: 'Support Manager', description: 'Manage support team' },
  { value: 'support_agent', label: 'Support Agent', description: 'Handle customer support' },
  { value: 'knowledge_manager', label: 'Knowledge Manager', description: 'Manage knowledge base' },
  { value: 'auditor', label: 'Auditor', description: 'Read-only access to analytics' },
  { value: 'end_user', label: 'End User', description: 'Basic customer access' },
];

export function TeamManagement({ tenantId }: { tenantId: string }) {
  const [members, setMembers] = useState<WorkspaceMember[]>([]);
  const [loading, setLoading] = useState(true);
  const [showAddModal, setShowAddModal] = useState(false);
  const [newUserId, setNewUserId] = useState('');
  const [newUserRole, setNewUserRole] = useState<PlatformRole>('support_agent');
  const [actionLoading, setActionLoading] = useState<string | null>(null);

  useEffect(() => {
    loadMembers();
  }, [tenantId]);

  const loadMembers = async () => {
    setLoading(true);
    try {
      const data = await apiClient.getWorkspaceMembers(tenantId);
      setMembers(data);
    } catch (error) {
      console.error('Failed to load members:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddMember = async () => {
    if (!newUserId) return;
    setActionLoading('add');
    try {
      await apiClient.addWorkspaceMember(tenantId, newUserId, newUserRole);
      setShowAddModal(false);
      setNewUserId('');
      setNewUserRole('support_agent');
      await loadMembers();
    } catch (error) {
      console.error('Failed to add member:', error);
    } finally {
      setActionLoading(null);
    }
  };

  const handleUpdateRole = async (memberId: string, role: PlatformRole) => {
    setActionLoading(memberId);
    try {
      await apiClient.updateMemberRole(tenantId, memberId, role);
      await loadMembers();
    } catch (error) {
      console.error('Failed to update role:', error);
    } finally {
      setActionLoading(null);
    }
  };

  const handleRemoveMember = async (memberId: string) => {
    if (!confirm('Remove this member from the workspace?')) return;
    setActionLoading(memberId);
    try {
      await apiClient.removeWorkspaceMember(tenantId, memberId);
      await loadMembers();
    } catch (error) {
      console.error('Failed to remove member:', error);
    } finally {
      setActionLoading(null);
    }
  };

  const getRoleLabel = (role: string) => {
    return ROLE_OPTIONS.find(r => r.value === role)?.label || role;
  };

  const getRoleDescription = (role: string) => {
    return ROLE_OPTIONS.find(r => r.value === role)?.description || '';
  };

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>Team & Roles</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
            Manage workspace members and their roles
          </p>
        </div>
        <button
          onClick={() => setShowAddModal(true)}
          className="px-4 py-2 rounded-xl font-semibold text-sm transition-all"
          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
        >
          + Add Member
        </button>
      </div>

      <div className="rounded-xl border" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr style={{ borderBottom: '1px solid var(--color-border)' }}>
                <th className="text-left py-3 px-4 text-xs font-semibold uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>
                  Member
                </th>
                <th className="text-left py-3 px-4 text-xs font-semibold uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>
                  Role
                </th>
                <th className="text-left py-3 px-4 text-xs font-semibold uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>
                  Status
                </th>
                <th className="text-left py-3 px-4 text-xs font-semibold uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>
                  Joined
                </th>
                <th className="text-right py-3 px-4 text-xs font-semibold uppercase tracking-wider" style={{ color: 'var(--color-muted-foreground)' }}>
                  Actions
                </th>
              </tr>
            </thead>
            <tbody>
              {loading ? (
                Array.from({ length: 3 }).map((_, i) => (
                  <tr key={i} style={{ borderBottom: '1px solid var(--color-border)' }}>
                        <td colSpan={5} className="py-4">
                          <div className="skeleton h-4 w-full rounded" />
                        </td>
                      </tr>
                ))
              ) : members.length === 0 ? (
                <tr>
                  <td colSpan={5} className="py-8 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
                    No team members found
                  </td>
                </tr>
              ) : (
                members.map(member => (
                  <tr key={member.id} style={{ borderBottom: '1px solid var(--color-border)' }}>
                    <td className="py-3 px-4">
                      <div className="flex items-center gap-3">
                        <div className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold"
                          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                          {member.user_id.slice(0, 2).toUpperCase()}
                        </div>
                        <div>
                          <div className="text-sm font-medium" style={{ color: 'var(--color-foreground)' }}>
                            {member.user_id.slice(0, 8)}...
                          </div>
                          <div className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                            {member.user_id}
                          </div>
                        </div>
                      </div>
                    </td>
                    <td className="py-3 px-4">
                      <select
                        value={member.role}
                        onChange={(e) => handleUpdateRole(member.id, e.target.value as PlatformRole)}
                        disabled={actionLoading === member.id}
                        className="text-sm px-2 py-1 rounded border outline-none"
                        style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                      >
                        {ROLE_OPTIONS.map(role => (
                          <option key={role.value} value={role.value}>
                            {role.label}
                          </option>
                        ))}
                      </select>
                      <div className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                        {getRoleDescription(member.role)}
                      </div>
                    </td>
                    <td className="py-3 px-4">
                      <span className="inline-flex items-center gap-1 text-xs px-2 py-0.5 rounded-full"
                        style={{
                          background: member.status === 'active' ? 'rgba(44,140,102,0.15)' : 'rgba(205,66,63,0.15)',
                          color: member.status === 'active' ? '#2c8c66' : '#cd4239',
                        }}>
                        ● {member.status}
                      </span>
                    </td>
                    <td className="py-3 px-4 text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                      {new Date(member.created_at).toLocaleDateString()}
                    </td>
                    <td className="py-3 px-4 text-right">
                      <button
                        onClick={() => handleRemoveMember(member.id)}
                        disabled={actionLoading === member.id}
                        className="text-xs px-2 py-1 rounded border transition-colors hover:bg-red-500/10"
                        style={{ borderColor: 'rgba(205,66,63,0.3)', color: '#cd4239' }}
                      >
                        Remove
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {showAddModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
          <div className="rounded-2xl p-6 w-full max-w-md" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
            <h2 className="text-xl font-bold mb-4" style={{ color: 'var(--color-foreground)' }}>Add Team Member</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  User ID
                </label>
                <input
                  type="text"
                  value={newUserId}
                  onChange={(e) => setNewUserId(e.target.value)}
                  placeholder="Enter user UUID"
                  className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                  Role
                </label>
                <select
                  value={newUserRole}
                  onChange={(e) => setNewUserRole(e.target.value as PlatformRole)}
                  className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                  style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
                >
                  {ROLE_OPTIONS.map(role => (
                    <option key={role.value} value={role.value}>
                      {role.label} - {role.description}
                    </option>
                  ))}
                </select>
              </div>
            </div>
            <div className="flex gap-3 mt-6">
              <button
                onClick={() => setShowAddModal(false)}
                className="flex-1 px-4 py-2.5 rounded-xl font-semibold text-sm transition-colors"
                style={{ background: 'var(--color-muted)', color: 'var(--color-foreground)' }}
              >
                Cancel
              </button>
              <button
                onClick={handleAddMember}
                disabled={!newUserId || actionLoading === 'add'}
                className="flex-1 px-4 py-2.5 rounded-xl font-semibold text-sm transition-all disabled:opacity-60"
                style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
              >
                {actionLoading === 'add' ? 'Adding...' : 'Add Member'}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
