import { useState, useEffect } from 'react';
import { useTranslation } from '../../lib/i18n';


interface ConsentPreferences {
  essential: boolean;
  analytics: boolean;
  marketing: boolean;
  ai_training: boolean;
}

const CONSENT_KEY = 'salesgenie_cookie_consent';

const DEFAULT_CONSENT: ConsentPreferences = {
  essential: true,
  analytics: false,
  marketing: false,
  ai_training: false,
};

export function useCookieConsent(): {
  preferences: ConsentPreferences;
  setPreferences: (prefs: ConsentPreferences) => void;
  hasConsented: boolean;
  acceptAll: () => void;
  rejectNonEssential: () => void;
} {
  const [preferences, setPreferencesState] = useState<ConsentPreferences>(DEFAULT_CONSENT);
  const [hasConsented, setHasConsented] = useState(false);

  useEffect(() => {
    const stored = localStorage.getItem(CONSENT_KEY);
    if (stored) {
      const parsed = JSON.parse(stored);
      setPreferencesState(parsed);
      setHasConsented(true);
      applyConsent(parsed);
    } else {
      setHasConsented(false);
    }
  }, []);

  const applyConsent = (prefs: ConsentPreferences) => {
    if (typeof window === 'undefined') return;

    // Enable/disable analytics scripts based on consent
    const gaConsent = prefs.analytics ? 'granted' : 'denied';
    if (window.gtag) {
      window.gtag('consent', 'update', {
        analytics_storage: gaConsent,
        ad_storage: prefs.marketing ? 'granted' : 'denied',
      });
    }
  };

  const setPreferences = (prefs: ConsentPreferences) => {
    setPreferencesState(prefs);
    setHasConsented(true);
    localStorage.setItem(CONSENT_KEY, JSON.stringify(prefs));
    applyConsent(prefs);
  };

  const acceptAll = () => {
    const all = { essential: true, analytics: true, marketing: true, ai_training: true };
    setPreferences(all);
  };

  const rejectNonEssential = () => {
    setPreferences({ essential: true, analytics: false, marketing: false, ai_training: false });
  };

  return { preferences, setPreferences, hasConsented, acceptAll, rejectNonEssential };
}

declare global {
  interface Window {
    gtag?: (...args: unknown[]) => void;
  }
}

export function CookieConsentBanner() {
  const { preferences, setPreferences, hasConsented, acceptAll, rejectNonEssential } = useCookieConsent();
  const { t } = useTranslation();
  const [showDetails, setShowDetails] = useState(false);

  if (hasConsented) {
    return null;
  }

  return (
    <div
      className="fixed bottom-0 left-0 right-0 z-50 border-t shadow-lg"
      style={{
        background: 'var(--color-surface-dark)',
        borderTopColor: 'var(--color-border)',
        color: 'var(--color-foreground)',
      }}
    >
      <div className="max-w-7xl mx-auto p-4">
        {!showDetails ? (
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
            <p className="text-sm flex-1">
              {t('cookies.banner')}
              <a
                href="/privacy"
                className="ml-1 underline"
                style={{ color: 'var(--color-link-blue)' }}
              >
                {t('cookies.privacyPolicy')}
              </a>
            </p>
            <div className="flex gap-2">
              <button
                onClick={rejectNonEssential}
                className="px-4 py-2 text-sm rounded border"
                style={{
                  borderColor: 'var(--color-border)',
                  color: 'var(--color-foreground)',
                }}
              >
                {t('cookies.reject')}
              </button>
              <button
                onClick={acceptAll}
                className="px-4 py-2 text-sm rounded"
                style={{
                  background: 'var(--color-primary)',
                  color: 'var(--color-on-primary)',
                }}
              >
                {t('cookies.acceptAll')}
              </button>
              <button
                onClick={() => setShowDetails(true)}
                className="px-4 py-2 text-sm rounded border"
                style={{
                  borderColor: 'var(--color-border)',
                  color: 'var(--color-foreground)',
                }}
              >
                {t('cookies.customize')}
              </button>
            </div>
          </div>
        ) : (
          <div className="space-y-4">
            <h3 className="font-semibold" style={{ color: 'var(--color-foreground)' }}>
              {t('cookies.title')}
            </h3>
            {Object.entries(preferences).map(([category, granted]) => (
              <div key={category} className="flex items-center justify-between">
                <div className="flex-1">
                  <span className="font-medium text-sm" style={{ color: 'var(--color-foreground)' }}>
                    {t(`cookies.categories.${category}`)}
                  </span>
                  <p className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>
                    {t(`cookies.descriptions.${category}`)}
                  </p>
                </div>
                <label className="relative inline-flex h-6 w-10 items-center rounded-full transition-colors ml-4">
                  <input
                    type="checkbox"
                    className="sr-only"
                    checked={granted}
                    disabled={category === 'essential'}
                    onChange={(e) =>
                      setPreferences({ ...preferences, [category]: e.target.checked })
                    }
                  />
                  <span
                    className={`inline-block h-5 w-5 transform rounded-full transition ${
                      granted ? 'translate-x-5 bg-primary' : 'translate-x-1 bg-gray-300'
                    }`}
                  />
                </label>
              </div>
            ))}
            <div className="flex gap-2 pt-2">
              <button
                onClick={() => setShowDetails(false)}
                className="px-4 py-2 text-sm rounded border"
                style={{
                  borderColor: 'var(--color-border)',
                  color: 'var(--color-foreground)',
                }}
              >
                {t('cookies.back')}
              </button>
              <button
                onClick={() => setPreferences(preferences)}
                className="px-4 py-2 text-sm rounded"
                style={{
                  background: 'var(--color-primary)',
                  color: 'var(--color-on-primary)',
                }}
              >
                {t('cookies.save')}
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
