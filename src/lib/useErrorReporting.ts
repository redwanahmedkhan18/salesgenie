/**
 * Frontend Error Reporting Hook
 * Captures unhandled errors and promise rejections, sending them to the
 * backend for processing (which forwards to Sentry if configured).
 * 
 * SECURITY: Never sends PII — only error messages, stack traces, component
 * names, and request context. Tokens and user data are redacted.
 */

import { useEffect } from 'react';
import { get_structured_logger } from './logger';

const logger = get_structured_logger('salesgenie.frontend', 'ErrorReporter');

interface ErrorReport {
  error: string;
  componentStack?: string;
  url?: string;
  userAgent?: string;
  timestamp: string;
  isUnhandledRejection?: boolean;
}

const SENSITIVE_PATTERNS = [
  /auth_token["']?\s*[:=]\s*["'][^"']+["']/gi,
  /refresh_token["']?\s*[:=]\s*["'][^"']+["']/gi,
  /password["']?\s*[:=]\s*["'][^"']+["']/gi,
  /[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/gi,
];

const sanitizeErrorText = (text: string): string => {
  let sanitized = text;
  for (const pattern of SENSITIVE_PATTERNS) {
    sanitized = sanitized.replace(pattern, '[REDACTED]');
  }
  return sanitized;
};

export const useErrorReporting = (): void => {
  useEffect(() => {
    if (process.env.NODE_ENV !== 'production') {
      return;
    }

    const reportError = (error: unknown, isUnhandledRejection = false): void => {
      if (!error) return;

      const errorObj = error as Error;
      const errorReport: ErrorReport = {
        error: sanitizeErrorText(
          errorObj?.message || errorObj?.toString() || String(error)
        ),
        componentStack: sanitizeErrorText(errorObj?.stack || ''),
        url: window.location.href,
        userAgent: navigator.userAgent,
        timestamp: new Date().toISOString(),
        isUnhandledRejection,
      };

      logger.error('Frontend error captured', errorReport as unknown as Record<string, unknown>);

      // Send to backend error endpoint
      if (typeof window !== 'undefined' && window.requestIdleCallback) {
        window.requestIdleCallback(() => {
          fetch('/api/v1/logs/frontend/error', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(errorReport),
            keepalive: true,
          }).catch(() => {});
        });
      }
    };

    const handleUnhandledRejection = (event: PromiseRejectionEvent): void => {
      event.preventDefault();
      reportError(event.reason, true);
    };

    const handleErrorHandler = (
      event: ErrorEvent
    ): void => {
      reportError(event.error || new Error(event.message), false);
    };

    window.addEventListener('unhandledrejection', handleUnhandledRejection);
    window.addEventListener('error', handleErrorHandler);

    return () => {
      window.removeEventListener('unhandledrejection', handleUnhandledRejection);
      window.removeEventListener('error', handleErrorHandler);
    };
  }, []);
};
