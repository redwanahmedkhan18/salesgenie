/**
 * Minimal i18n module for SalesGenie frontend.
 * Uses browser language detection with English fallback.
 */

export type Locale = 'en' | 'es' | 'fr' | 'de';

interface TranslationNamespace {
  [key: string]: string | string[] | TranslationNamespace;
}

const translations: Record<Locale, TranslationNamespace> = {
  en: {
    cookies: {
      banner: 'We use cookies to improve your experience. By continuing, you consent to our use of cookies.',
      privacyPolicy: 'Privacy Policy',
      acceptAll: 'Accept All',
      reject: 'Reject',
      customize: 'Customize',
      title: 'Cookie Preferences',
      back: 'Back',
      save: 'Save Preferences',
      categories: {
        essential: 'Essential',
        analytics: 'Analytics',
        marketing: 'Marketing',
        ai_training: 'AI Training',
      },
      descriptions: {
        essential: 'Required for core functionality (authentication, security).',
        analytics: 'Help us understand how you use the platform (Google Analytics).',
        marketing: 'Used for targeted advertising and marketing communications.',
        ai_training: 'Used to train our AI models (opt-in, can be revoked anytime).',
      },
    },
  },
  es: {
    cookies: {
      banner: 'Usamos cookies para mejorar su experiencia. Al continuar, acepta nuestro uso de cookies.',
      privacyPolicy: 'Política de Privacidad',
      acceptAll: 'Aceptar Todo',
      reject: 'Rechazar',
      customize: 'Personalizar',
      title: 'Preferencias de Cookies',
      back: 'Atrás',
      save: 'Guardar Preferencias',
      categories: {
        essential: 'Esenciales',
        analytics: 'Analíticas',
        marketing: 'Marketing',
        ai_training: 'Entrenamiento de IA',
      },
      descriptions: {
        essential: 'Necesario para funcionalidad básica (autenticación, seguridad).',
        analytics: 'Ayúdanos a entender cómo usa la plataforma (Google Analytics).',
        marketing: 'Usado para publicidad y comunicaciones comerciales.',
        ai_training: 'Usado para entrenar nuestros modelos de IA (opcional).',
      },
    },
  },
  fr: {
    cookies: {
      banner: 'Nous utilisons des cookies pour améliorer votre expérience. En continuant, vous consentez à notre utilisation des cookies.',
      privacyPolicy: 'Politique de Confidentialité',
      acceptAll: 'Accepter Tous',
      reject: 'Refuser',
      customize: 'Personnaliser',
      title: 'Préférences de Cookies',
      back: 'Retour',
      save: 'Enregistrer',
      categories: {
        essential: 'Essentiels',
        analytics: 'Analytiques',
        marketing: 'Marketing',
        ai_training: 'Entraînement d\'IA',
      },
      descriptions: {
        essential: 'Nécessaire pour le fonctionnement de base (authentification, sécurité).',
        analytics: 'Nous aident à comprendre comment vous utilisez la plateforme (Google Analytics).',
        marketing: 'Utilisé pour la publicité et le marketing ciblié.',
        ai_training: 'Utilisé pour entraîner nos modèles d\'IA (optionnel).',
      },
    },
  },
  de: {
    cookies: {
      banner: 'Wir verwenden Cookies, um Ihr Erlebnis zu verbessern. Wenn Sie fortfahren, stimmen Sie unserer Cookie-Nutzung zu.',
      privacyPolicy: 'Datenschutzrichtlinie',
      acceptAll: 'Alle akzeptieren',
      reject: 'Ablehnen',
      customize: 'Anpassen',
      title: 'Cookie-Einstellungen',
      back: 'Zurück',
      save: 'Speichern',
      categories: {
        essential: 'Essentiell',
        analytics: 'Analytik',
        marketing: 'Marketing',
        ai_training: 'KI-Training',
      },
      descriptions: {
        essential: 'Erforderlich für Kernfunktionalität (Authentifizierung, Sicherheit).',
        analytics: 'Helfen uns zu verstehen, wie Sie die Plattform nutzen (Google Analytics).',
        marketing: 'Wird für gezielte Werbung und Marketingkommunikation verwendet.',
        ai_training: 'Wird verwendet, um unsere KI-Modelle zu trainieren (freiwillig).',
      },
    },
  },
};

const detectLocale = (): Locale => {
  if (typeof window === 'undefined') return 'en';
  const browserLang = navigator.language.split('-')[0] as Locale;
  return translations[browserLang] ? browserLang : 'en';
};

const currentLocale = detectLocale();

const flatPath = (obj: TranslationNamespace, prefix = ''): Record<string, string> => {
  const result: Record<string, string> = {};
  for (const [key, value] of Object.entries(obj)) {
    const path = prefix ? `${prefix}.${key}` : key;
    if (typeof value === 'string') {
      result[path] = value;
    } else if (typeof value === 'object' && value !== null) {
      Object.assign(result, flatPath(value as TranslationNamespace, path));
    }
  }
  return result;
};

export const useTranslation = () => {
  const t = (key: string): string => {
    const flat = flatPath(translations[currentLocale] ?? translations.en);
    return flat[key] ?? key;
  };

  return { t, locale: currentLocale };
};
