/**
 * Frontend structured logger.
 * In production, sends errors to the observability backend.
 * Never logs PII or secrets.
 */

type LogLevel = 'debug' | 'info' | 'warn' | 'error';

interface LogEntry {
  level: LogLevel;
  message: string;
  service: string;
  component: string;
  timestamp: string;
  extra?: Record<string, unknown>;
}

const isDevelopment = process.env.NODE_ENV !== 'production';

class FrontendLogger {
  private service: string;
  private component: string;

  constructor(service: string, component: string) {
    this.service = service;
    this.component = component;
  }

  private log(level: LogLevel, message: string, extra?: Record<string, unknown>): void {
    const entry: LogEntry = {
      level,
      message,
      service: this.service,
      component: this.component,
      timestamp: new Date().toISOString(),
      extra,
    };

    if (isDevelopment) {
      const consoleMethod = level === 'error' ? console.error : level === 'warn' ? console.warn : console.log;
      consoleMethod(`[${this.component}] [${level.toUpperCase()}] ${message}`, extra ?? '');
    } else {
      if (level === 'error' || level === 'warn') {
        if (typeof window !== 'undefined') {
          fetch('/api/v1/logs/frontend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(entry),
            keepalive: true,
          }).catch(() => {});
        }
      }
    }
  }

  debug(message: string, extra?: Record<string, unknown>): void {
    this.log('debug', message, extra);
  }

  info(message: string, extra?: Record<string, unknown>): void {
    this.log('info', message, extra);
  }

  warn(message: string, extra?: Record<string, unknown>): void {
    this.log('warn', message, extra);
  }

  error(message: string, extra?: Record<string, unknown>): void {
    this.log('error', message, extra);
  }
}

export const get_structured_logger = (service: string, component: string): FrontendLogger => {
  return new FrontendLogger(service, component);
};

export const frontendLogger = new FrontendLogger('salesgenie.frontend', 'Root');
