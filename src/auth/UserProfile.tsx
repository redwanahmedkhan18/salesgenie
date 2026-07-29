import React, { useState, useEffect } from 'react';
import { useAuth } from '../auth/AuthProvider';
import { apiClient } from '../lib/api-client';
import type { UserPreferences } from '../lib/types';

export function UserProfile() {
  const { user, logout } = useAuth();
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [jobTitle, setJobTitle] = useState('');
  const [department, setDepartment] = useState('');
  const [avatarUrl, setAvatarUrl] = useState('');
  const [preferences, setPreferences] = useState<Partial<UserPreferences>>({});
  const [saving, setSaving] = useState(false);
  const [activeTab, setActiveTab] = useState<'profile' | 'preferences' | 'security'>('profile');

  useEffect(() => {
    if (user) {
      setFullName(user.full_name || '');
      setEmail(user.email || '');
    }
    loadPreferences();
  }, [user]);

  const loadPreferences = async () => {
    try {
      const prefs = await apiClient.getUserPreferences();
      setPreferences(prefs);
    } catch (error) {
      console.error('Failed to load preferences:', error);
    }
  };

  const handleSaveProfile = async () => {
    setSaving(true);
    try {
      await apiClient.updateUserProfile({
        full_name: fullName,
        phone_number: phoneNumber,
        job_title: jobTitle,
        department,
        avatar_url: avatarUrl,
      } as any);
    } catch (error) {
      console.error('Failed to update profile:', error);
    } finally {
      setSaving(false);
    }
  };

  const handleSavePreferences = async () => {
    setSaving(true);
    try {
      await apiClient.updateUserPreferences(preferences);
    } catch (error) {
      console.error('Failed to update preferences:', error);
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold" style={{ color: 'var(--color-foreground)' }}>User Profile</h1>
          <p className="text-sm mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>Manage your account settings and preferences</p>
        </div>
        <button
          onClick={logout}
          className="px-4 py-2 text-sm font-semibold rounded-lg transition-colors"
          style={{ background: 'var(--color-muted)', color: 'var(--color-foreground)' }}
        >
          Sign Out
        </button>
      </div>

      <div className="flex gap-2 mb-6 border-b" style={{ borderColor: 'var(--color-border)' }}>
        <button
          onClick={() => setActiveTab('profile')}
          className={`px-4 py-2 text-sm font-medium transition-colors border-b-2 ${activeTab === 'profile' ? 'border-amber-500' : 'border-transparent'}`}
          style={{ color: activeTab === 'profile' ? 'var(--color-primary)' : 'var(--color-muted-foreground)' }}
        >
          Profile
        </button>
        <button
          onClick={() => setActiveTab('preferences')}
          className={`px-4 py-2 text-sm font-medium transition-colors border-b-2 ${activeTab === 'preferences' ? 'border-amber-500' : 'border-transparent'}`}
          style={{ color: activeTab === 'preferences' ? 'var(--color-primary)' : 'var(--color-muted-foreground)' }}
        >
          Preferences
        </button>
        <button
          onClick={() => setActiveTab('security')}
          className={`px-4 py-2 text-sm font-medium transition-colors border-b-2 ${activeTab === 'security' ? 'border-amber-500' : 'border-transparent'}`}
          style={{ color: activeTab === 'security' ? 'var(--color-primary)' : 'var(--color-muted-foreground)' }}
        >
          Security
        </button>
      </div>

      {activeTab === 'profile' && (
        <div className="space-y-5">
          <div className="flex items-center gap-6">
            <div className="w-20 h-20 rounded-full flex items-center justify-center text-2xl font-bold flex-shrink-0"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
              {fullName ? fullName.slice(0, 2).toUpperCase() : '??'}
            </div>
            <div className="flex-1">
              <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                Avatar URL
              </label>
              <input
                type="url"
                value={avatarUrl}
                onChange={(e) => setAvatarUrl(e.target.value)}
                placeholder="https://example.com/avatar.png"
                className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
              />
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                Full Name
              </label>
              <input
                type="text"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                Email Address
              </label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                disabled
                className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                style={{ background: 'var(--color-muted)', color: 'var(--color-muted-foreground)', border: '1px solid var(--color-border)' }}
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                Phone Number
              </label>
              <input
                type="tel"
                value={phoneNumber}
                onChange={(e) => setPhoneNumber(e.target.value)}
                placeholder="+1-555-0199"
                className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                Job Title
              </label>
              <input
                type="text"
                value={jobTitle}
                onChange={(e) => setJobTitle(e.target.value)}
                placeholder="Lead AI Engineer"
                className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
              />
            </div>
            <div className="md:col-span-2">
              <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                Department
              </label>
              <input
                type="text"
                value={department}
                onChange={(e) => setDepartment(e.target.value)}
                placeholder="Engineering"
                className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
              />
            </div>
          </div>

          <div className="flex justify-end">
            <button
              onClick={handleSaveProfile}
              disabled={saving}
              className="px-6 py-2.5 rounded-xl font-semibold text-sm transition-all disabled:opacity-60"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              {saving ? 'Saving...' : 'Save Profile'}
            </button>
          </div>
        </div>
      )}

      {activeTab === 'preferences' && (
        <div className="space-y-5">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                Theme
              </label>
              <select
                value={preferences.theme || 'dark'}
                onChange={(e) => setPreferences({ ...preferences, theme: e.target.value })}
                className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
              >
                <option value="dark">Dark</option>
                <option value="light">Light</option>
                <option value="system">System</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium mb-1.5" style={{ color: 'var(--color-foreground)' }}>
                Language
              </label>
              <select
                value={preferences.language || 'en'}
                onChange={(e) => setPreferences({ ...preferences, language: e.target.value })}
                className="w-full px-4 py-2.5 rounded-xl text-sm outline-none"
                style={{ background: 'var(--color-background)', color: 'var(--color-foreground)', border: '1px solid var(--color-border)' }}
              >
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
                <option value="de">German</option>
                <option value="ja">Japanese</option>
              </select>
            </div>
            <div className="flex items-center justify-between p-4 rounded-xl" style={{ background: 'var(--color-background)', border: '1px solid var(--color-border)' }}>
              <div>
                <label className="block text-sm font-medium" style={{ color: 'var(--color-foreground)' }}>
                  Email Notifications
                </label>
                <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                  Receive email notifications for mentions and updates
                </p>
              </div>
              <label className="relative inline-flex h-6 w-10 items-center rounded-full">
                <input
                  type="checkbox"
                  checked={preferences.email_notifications ?? true}
                  onChange={(e) => setPreferences({ ...preferences, email_notifications: e.target.checked })}
                  className="sr-only"
                />
                <span className="absolute inset-0 rounded-full transition-colors"
                  style={{ background: preferences.email_notifications ? 'var(--color-primary)' : 'var(--color-border)' }} />
                <span className="absolute top-1/2 left-1 h-4 w-4 transform -translate-y-1/2 rounded-full bg-white transition-transform"
                  style={{ left: preferences.email_notifications ? '24px' : '4px' }} />
              </label>
            </div>
            <div className="flex items-center justify-between p-4 rounded-xl" style={{ background: 'var(--color-background)', border: '1px solid var(--color-border)' }}>
              <div>
                <label className="block text-sm font-medium" style={{ color: 'var(--color-foreground)' }}>
                  Slack Notifications
                </label>
                <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                  Send notifications to Slack channel
                </p>
              </div>
              <label className="relative inline-flex h-6 w-10 items-center rounded-full">
                <input
                  type="checkbox"
                  checked={preferences.slack_notifications ?? false}
                  onChange={(e) => setPreferences({ ...preferences, slack_notifications: e.target.checked })}
                  className="sr-only"
                />
                <span className="absolute inset-0 rounded-full transition-colors"
                  style={{ background: preferences.slack_notifications ? 'var(--color-primary)' : 'var(--color-border)' }} />
                <span className="absolute top-1/2 left-1 h-4 w-4 transform -translate-y-1/2 rounded-full bg-white transition-transform"
                  style={{ left: preferences.slack_notifications ? '24px' : '4px' }} />
              </label>
            </div>
            <div className="flex items-center justify-between p-4 rounded-xl" style={{ background: 'var(--color-background)', border: '1px solid var(--color-border)' }}>
              <div>
                <label className="block text-sm font-medium" style={{ color: 'var(--color-foreground)' }}>
                  Keyboard Shortcuts
                </label>
                <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                  Enable keyboard navigation shortcuts
                </p>
              </div>
              <label className="relative inline-flex h-6 w-10 items-center rounded-full">
                <input
                  type="checkbox"
                  checked={preferences.keyboard_shortcuts ?? true}
                  onChange={(e) => setPreferences({ ...preferences, keyboard_shortcuts: e.target.checked })}
                  className="sr-only"
                />
                <span className="absolute inset-0 rounded-full transition-colors"
                  style={{ background: preferences.keyboard_shortcuts ? 'var(--color-primary)' : 'var(--color-border)' }} />
                <span className="absolute top-1/2 left-1 h-4 w-4 transform -translate-y-1/2 rounded-full bg-white transition-transform"
                  style={{ left: preferences.keyboard_shortcuts ? '24px' : '4px' }} />
              </label>
            </div>
          </div>

          <div className="flex justify-end">
            <button
              onClick={handleSavePreferences}
              disabled={saving}
              className="px-6 py-2.5 rounded-xl font-semibold text-sm transition-all disabled:opacity-60"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              {saving ? 'Saving...' : 'Save Preferences'}
            </button>
          </div>
        </div>
      )}

      {activeTab === 'security' && (
        <div className="space-y-5">
          <div className="p-4 rounded-xl" style={{ background: 'var(--color-background)', border: '1px solid var(--color-border)' }}>
            <h3 className="font-semibold mb-2" style={{ color: 'var(--color-foreground)' }}>Multi-Factor Authentication</h3>
            <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
              Add an extra layer of security to your account with MFA.
            </p>
            <button
              onClick={async () => {
                try {
                  const mfa = await apiClient.setupMFA();
                  alert(`MFA Secret: ${mfa.secret_key}\nBackup Codes: ${mfa.backup_codes.join(', ')}`);
                } catch (error) {
                  console.error('MFA setup failed:', error);
                }
              }}
              className="mt-3 px-4 py-2 rounded-lg text-sm font-medium transition-colors"
              style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
            >
              Set Up MFA
            </button>
          </div>

          <div className="p-4 rounded-xl" style={{ background: 'var(--color-background)', border: '1px solid var(--color-border)' }}>
            <h3 className="font-semibold mb-2" style={{ color: 'var(--color-foreground)' }}>Active Sessions</h3>
            <p className="text-sm mb-3" style={{ color: 'var(--color-muted-foreground)' }}>
              You can revoke access from any device here.
            </p>
            <button
              onClick={async () => {
                try {
                  const sessions = await apiClient.getSessions();
                  console.log('Sessions:', sessions);
                } catch (error) {
                  console.error('Failed to fetch sessions:', error);
                }
              }}
              className="px-4 py-2 rounded-lg text-sm font-medium transition-colors"
              style={{ background: 'var(--color-muted)', color: 'var(--color-foreground)' }}
            >
              View Sessions
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
