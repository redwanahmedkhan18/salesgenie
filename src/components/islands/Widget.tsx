import React from 'react';
import AppProviders from './AppProviders';

export default function Widget() {
  return (
    <AppProviders>
      <WidgetContent />
    </AppProviders>
  );
}

function WidgetContent() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>Widget Manager</h2>
        <p className="text-muted-foreground">Configure your AI widgets and chat experiences.</p>
      </div>
      
      <div className="rounded-xl border p-6" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <h3 className="font-semibold mb-4" style={{ color: 'var(--color-foreground)' }}>No widgets configured</h3>
        <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
          Add widgets to your website to embed AI-powered chat and support experiences.
        </p>
      </div>
    </div>
  );
}