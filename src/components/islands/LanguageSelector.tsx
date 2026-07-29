import React, { useState } from 'react';
import { useAuth } from '../../auth/AuthProvider';
import { apiClient } from '../../lib/api-client';
import { SUPPORTED_LANGUAGES, type Language } from '../../lib/types';

export function LanguageSelector({ 
  className = '', 
  showLabel = false 
}: { 
  className?: string;
  showLabel?: boolean;
}) {
  const { user, hasRole } = useAuth();
  const [selectedLanguage, setSelectedLanguage] = useState<Language>(
    SUPPORTED_LANGUAGES.find(l => l.code === (user?.language || 'en')) || SUPPORTED_LANGUAGES[0]
  );
  const [showDropdown, setShowDropdown] = useState(false);
  const [saving, setSaving] = useState(false);

  const handleLanguageChange = async (language: Language) => {
    if (!user) return;
    
    setSaving(true);
    try {
      await apiClient.updateUserPreferences({ language: language.code });
      setSelectedLanguage(language);
      localStorage.setItem('salesgenie-language', language.code);
      window.location.reload();
    } catch (error) {
      console.error('Failed to update language:', error);
    } finally {
      setSaving(false);
    }
  };

  const activeLanguages = SUPPORTED_LANGUAGES.filter(l => l.is_active);

  return (
    <div className={`relative ${className}`}>
      {showLabel && (
        <label className="block text-xs font-semibold mb-1.5" style={{ color: 'var(--color-muted-foreground)' }}>
          Language
        </label>
      )}
      <div className="relative">
        <button
          onClick={() => setShowDropdown(!showDropdown)}
          disabled={saving}
          className="flex items-center gap-2 px-3 py-1.5 rounded-xl text-sm outline-none transition-colors"
          style={{
            background: 'var(--color-card)',
            color: 'var(--color-foreground)',
            border: '1px solid var(--color-border)',
          }}
        >
          <span className="text-base">{selectedLanguage.flag || '🌐'}</span>
          <span className="font-medium">{selectedLanguage.name}</span>
          <svg 
            className={`w-4 h-4 transition-transform ${showDropdown ? 'rotate-180' : ''}`}
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        {showDropdown && (
          <div 
            className="absolute top-full left-0 mt-2 w-64 rounded-xl border shadow-lg z-50 overflow-hidden"
            style={{
              background: 'var(--color-card)',
              borderColor: 'var(--color-border)',
            }}
          >
            <div className="max-h-80 overflow-y-auto">
              {activeLanguages.map((language) => (
                <button
                  key={language.code}
                  onClick={() => handleLanguageChange(language)}
                  disabled={saving}
                  className="w-full text-left px-3 py-2 text-sm hover:opacity-80 transition-colors flex items-center gap-2"
                  style={{
                    background: selectedLanguage.code === language.code ? 'var(--color-primary)' : 'transparent',
                    color: selectedLanguage.code === language.code ? 'var(--color-on-primary)' : 'var(--color-foreground)',
                  }}
                >
                  <span className="text-base">{language.flag || '🌐'}</span>
                  <span className="flex-1 text-left">{language.name}</span>
                  <span className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                    {language.native_name}
                  </span>
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}