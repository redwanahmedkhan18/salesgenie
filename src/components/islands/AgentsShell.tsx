import React from 'react';
import AgentBuilder from './AgentBuilder';

interface AgentsShellProps {
  activeAgentId?: string;
  onAgentSelect?: (agentId: string) => void;
}

export default function AgentsShell(_: AgentsShellProps = {}) {
  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto">
        <AgentBuilder />
      </div>
    </div>
  );
}