import React from 'react';
import AgentBuilder from './AgentBuilder';

interface AgentsShellProps {
  activeAgentId?: string;
  onAgentSelect?: (agentId: string) => void;
}

export default function AgentsShell({ activeAgentId, onAgentSelect }: AgentsShellProps) {
  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto">
        <AgentBuilder activeAgentId={activeAgentId} onAgentSelect={onAgentSelect} />
      </div>
    </div>
  );
}