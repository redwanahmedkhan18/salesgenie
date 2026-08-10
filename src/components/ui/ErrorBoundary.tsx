import React, { Component } from 'react';
import type { ErrorInfo, ReactNode } from 'react';
import { get_structured_logger } from '../../lib/logger';

const logger = get_structured_logger('salesgenie.frontend', 'ErrorBoundary');

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
  componentName?: string;
}

interface State {
  hasError: boolean;
  error: Error | null;
  errorInfo: ErrorInfo | null;
}

export class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error, errorInfo: null };
  }

  override componentDidCatch(error: Error, errorInfo: ErrorInfo): void {
    this.setState({ errorInfo });
    logger.error('React component error', {
      extra: {
        component: this.props.componentName ?? 'unknown',
        error: error.message,
        stack: error.stack,
        componentStack: errorInfo.componentStack,
      },
    });
  }

  private handleReset = () => {
    this.setState({ hasError: false, error: null, errorInfo: null });
  };

  override render(): ReactNode {
    if (this.state.hasError) {
      if (this.props.fallback) {
        return this.props.fallback;
      }

      return (
        <div
          className="flex flex-col items-center justify-center min-h-[400px] p-6 text-center"
          style={{ background: 'var(--color-background)' }}
        >
          <div
            className="p-4 rounded-xl max-w-md"
            style={{
              background: 'var(--color-card)',
              border: '1px solid var(--color-border)',
            }}
          >
            <div className="text-4xl mb-4">⚠️</div>
            <h2
              className="text-xl font-bold mb-2"
              style={{ color: 'var(--color-foreground)' }}
            >
              Something went wrong
            </h2>
            <p
              className="text-sm mb-4"
              style={{ color: 'var(--color-muted-foreground)' }}
            >
              An error occurred in the{' '}
              <code className="text-xs" style={{ color: 'var(--color-link-blue)' }}>
                {this.props.componentName ?? 'component'}
              </code>
              . Please try again or contact support.
            </p>
            <div className="flex gap-2 justify-center">
              <button
                onClick={this.handleReset}
                className="px-4 py-2 rounded text-sm font-semibold"
                style={{
                  background: 'var(--color-primary)',
                  color: 'var(--color-on-primary)',
                }}
              >
                Try again
              </button>
              {this.state.error && (
                <button
                  onClick={() => {
                    const detail = `${this.state.error?.message}\n\n${this.state.errorInfo?.componentStack ?? ''}`;
                    navigator.clipboard.writeText(detail);
                  }}
                  className="px-4 py-2 rounded text-sm font-semibold"
                  style={{
                    background: 'var(--color-surface-dark)',
                    color: 'var(--color-foreground)',
                    border: '1px solid var(--color-border)',
                  }}
                >
                  Copy error details
                </button>
              )}
            </div>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}

export const withErrorBoundary = <P extends object>(
  Component: React.ComponentType<P>,
  componentName?: string,
  fallback?: ReactNode,
) => {
  const Wrapped: React.FC<P> = (props: P) => (
    <ErrorBoundary fallback={fallback} componentName={componentName ?? Component.name}>
      <Component {...props} />
    </ErrorBoundary>
  );
  Wrapped.displayName = `withErrorBoundary(${Component.name})`;
  return Wrapped;
};
