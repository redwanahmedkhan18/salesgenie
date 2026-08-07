import React, { useState } from 'react';
import { AuthProvider } from "../../auth/AuthProvider";
import { ProtectedRoute } from "../../auth/ProtectedRoute";
import { Sidebar, CommandPalette } from './AppShell';

interface AppShellPageProps {
  activeRoute: string;
  onRouteChange: (id: string) => void;
  children: React.ReactNode;
  header?: React.ReactNode;
}

export default function AppShellPage({
  activeRoute,
  onRouteChange,
  children,
  header,
}: AppShellPageProps) {
  const [paletteOpen, setPaletteOpen] = useState(false);
  
  const handleNavigate = (id: string) => {
    onRouteChange(id);
    if (id !== 'command-palette') {
      window.history.pushState({}, '', `/app/${id}`);
    }
  };

  return (
    <AuthProvider>
      <ProtectedRoute>
        <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
          <Sidebar activeRoute={activeRoute} onRouteChange={onRouteChange} />

          <main className="flex-1 overflow-y-auto">
            {header || (
              <header className="sticky top-0 z-20 flex items-center justify-between px-6 py-4 border-b"
                style={{ background: 'var(--color-background)', borderColor: 'var(--color-border)' }}>
                <div>
                  <h1 className="text-xl font-bold" style={{ color: 'var(--color-foreground)' }}>
                    SalesGenie
                  </h1>
                  <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
                    Enterprise AI Platform
                  </p>
                </div>
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
              </header>
            )}

            <div className="px-6 py-6">
              {children}
            </div>
          </main>

          <CommandPalette open={paletteOpen} onClose={() => setPaletteOpen(false)} onNavigate={handleNavigate} />
        </div>
      </ProtectedRoute>
    </AuthProvider>
  );
}