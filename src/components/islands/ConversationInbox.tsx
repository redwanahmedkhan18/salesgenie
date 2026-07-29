import React, { useState, useRef, useEffect } from 'react';
import { useAuth } from '../../auth/AuthProvider';
import { apiClient } from '../../lib/api-client';
import type { Message, SupportTicket } from '../../lib/types';

const CHANNELS = ['Website', 'WhatsApp', 'Email', 'Slack', 'Telegram', 'Discord'];
const CHANNEL_ICONS: Record<string, string> = {
  Website: '🌐', WhatsApp: '📱', Email: '✉️', Slack: '💜', Telegram: '✈️', Discord: '🎮',
};

interface ConversationThread {
  id: string;
  customer: string;
  channel: string;
  lastMessage: string;
  time: string;
  unread: number;
  status: 'active' | 'escalated' | 'open' | 'resolved';
  aiConf: number;
}

export default function ConversationInbox() {
  const { hasRole, hasAnyRole } = useAuth();
  const [threads, setThreads] = useState<ConversationThread[]>([]);
  const [selectedThread, setSelectedThread] = useState<ConversationThread | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [showCopilot, setShowCopilot] = useState(true);
  const [loading, setLoading] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [activeFilter, setActiveFilter] = useState('All');

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  useEffect(() => {
    loadConversations();
  }, [activeFilter]);

  const loadConversations = async () => {
    setLoading(true);
    try {
      const response = await apiClient.fetchTickets({
        status: activeFilter === 'All' ? 'all' : activeFilter.toLowerCase(),
        size: '50',
      });
      
      if (response) {
        const threadList = response.map(t => ({
          id: t.id,
          customer: t.title || 'Unknown',
          channel: t.source || 'Website',
          lastMessage: t.description?.substring(0, 60) || 'No description',
          time: new Date(t.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
          unread: Math.floor(Math.random() * 5),
          status: t.status as 'active' | 'escalated' | 'open' | 'resolved',
          aiConf: t.satisfaction_score ? t.satisfaction_score / 100 : 0.85,
        }));
        setThreads(threadList);
      }
    } catch (error) {
      console.error('Failed to load conversations:', error);
    } finally {
      setLoading(false);
    }
  };

  const loadMessages = async (conversationId: string) => {
    const response = await apiClient.fetchTickets({ id: conversationId } as any);
    if (response) {
      const msgs: Message[] = [
        {
          id: 'm1',
          role: 'user',
          content: 'Hello, I need help with my order',
          timestamp: new Date(Date.now() - 3600000),
        },
        {
          id: 'm2',
          role: 'assistant',
          content: 'Of course! I can help you with that. What is your order number?',
          timestamp: new Date(Date.now() - 3500000),
          agentType: 'support_agent',
          confidence: 0.92,
        },
      ];
      setMessages(msgs);
    }
  };

  const handleSelectThread = (thread: ConversationThread) => {
    setSelectedThread(thread);
    loadMessages(thread.id);
  };

  const sendMessage = async () => {
    if (!inputText.trim() || !selectedThread) return;
    
    const userMsg: Message = {
      id: `m${Date.now()}`,
      role: 'user',
      content: inputText,
      timestamp: new Date(),
    };
    setMessages(prev => [...prev, userMsg]);
    setInputText('');
    setIsTyping(true);

    setTimeout(() => {
      const aiMsg: Message = {
        id: `m${Date.now() + 1}`,
        role: 'assistant',
        content: "Thank you for your message! I've noted your request and our team will respond shortly.",
        timestamp: new Date(),
        agentType: 'support_agent',
        confidence: 0.94,
      };
      setMessages(prev => [...prev, aiMsg]);
      setIsTyping(false);
    }, 1000);
  };

  const statusColors: Record<string, string> = {
    active: '#2c8c66', escalated: '#cd4239', open: '#f7a501', resolved: '#9b9c92',
  };

  if (!hasAnyRole(['support_manager', 'support_agent', 'sales_manager', 'sales_agent', 'org_admin', 'super_admin'])) {
    return (
      <div className="flex items-center justify-center min-h-screen" style={{ background: 'var(--color-background)' }}>
        <div className="text-center p-8 rounded-xl" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)' }}>
          <div className="text-4xl mb-4">🔒</div>
          <h2 className="text-xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>Access Denied</h2>
          <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
            You don't have permission to access the conversation inbox.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-screen overflow-hidden" style={{ background: 'var(--color-background)' }}>
      {/* Thread List */}
      <div className="w-72 flex-shrink-0 border-r flex flex-col" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
        <div className="px-4 py-4 border-b" style={{ borderColor: 'var(--color-border)' }}>
          <h1 className="font-bold text-sm" style={{ color: 'var(--color-foreground)' }}>Omnichannel Inbox</h1>
          <p className="text-xs mt-0.5" style={{ color: 'var(--color-muted-foreground)' }}>
            {threads.length} conversations
          </p>
          <div className="flex gap-1 mt-3 flex-wrap">
            {['All', 'Active', 'Escalated', 'Resolved'].map(ch => (
              <button
                key={ch}
                onClick={() => setActiveFilter(ch)}
                className={`text-xs px-2 py-0.5 rounded-full border transition-colors ${activeFilter === ch ? 'bg-amber-500/8' : ''}`}
                style={{
                  borderColor: 'var(--color-border)',
                  color: activeFilter === ch ? 'var(--color-on-primary)' : 'var(--color-muted-foreground)',
                  background: activeFilter === ch ? 'var(--color-primary)' : 'transparent',
                }}
              >
                {ch}
              </button>
            ))}
          </div>
        </div>
        <div className="flex-1 overflow-y-auto">
          {loading ? (
            <div className="p-4 space-y-3">
              {[...Array(5)].map((_, i) => (
                <div key={i} className="skeleton h-4 w-full rounded" />
              ))}
            </div>
          ) : threads.length === 0 ? (
            <div className="p-4 text-center" style={{ color: 'var(--color-muted-foreground)' }}>
              No conversations found
            </div>
          ) : (
            threads.map(thread => (
              <button
                key={thread.id}
                onClick={() => handleSelectThread(thread)}
                className={`w-full text-left px-4 py-3.5 border-b transition-colors ${selectedThread?.id === thread.id ? 'bg-amber-500/8' : 'hover:bg-white/3'}`}
                style={{ borderColor: 'var(--color-border)' }}
              >
                <div className="flex items-start gap-3">
                  <div className="w-9 h-9 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0"
                    style={{ background: 'var(--color-surface-soft)', color: 'var(--color-foreground)' }}>
                    {thread.customer.slice(0, 2).toUpperCase()}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-semibold truncate" style={{ color: 'var(--color-foreground)' }}>{thread.customer}</span>
                      <span className="text-xs flex-shrink-0 ml-2" style={{ color: 'var(--color-muted-foreground)' }}>{thread.time}</span>
                    </div>
                    <div className="flex items-center gap-1.5 mt-0.5">
                      <span className="text-xs">{CHANNEL_ICONS[thread.channel] || '🌐'}</span>
                      <span className="text-xs truncate" style={{ color: 'var(--color-muted-foreground)' }}>{thread.lastMessage}</span>
                    </div>
                    <div className="flex items-center gap-2 mt-1.5">
                      <span className="inline-flex items-center gap-1 text-xs px-1.5 py-0.5 rounded-full"
                        style={{ background: `${statusColors[thread.status]}20`, color: statusColors[thread.status] }}>
                        ● {thread.status}
                      </span>
                      {thread.unread > 0 && (
                        <span className="text-xs w-4 h-4 rounded-full flex items-center justify-center font-bold"
                          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                          {thread.unread}
                        </span>
                      )}
                    </div>
                  </div>
                </div>
              </button>
            ))
          )}
        </div>
      </div>

      {/* Chat Area */}
      <div className="flex-1 flex flex-col min-w-0">
        {selectedThread ? (
          <>
            {/* Chat Header */}
            <div className="flex items-center justify-between px-5 py-4 border-b flex-shrink-0"
              style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="flex items-center gap-3">
                <div className="w-9 h-9 rounded-full flex items-center justify-center text-xs font-bold"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                  {selectedThread.customer.slice(0, 2).toUpperCase()}
                </div>
                <div>
                  <div className="font-semibold text-sm" style={{ color: 'var(--color-foreground)' }}>{selectedThread.customer}</div>
                  <div className="text-xs flex items-center gap-1.5" style={{ color: 'var(--color-muted-foreground)' }}>
                    <span>{CHANNEL_ICONS[selectedThread.channel] || '🌐'}</span>
                    <span>via {selectedThread.channel}</span>
                  </div>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-xs px-2 py-1 rounded-lg" style={{ background: 'rgba(44,132,224,0.15)', color: '#2c84e0' }}>
                  AI Conf: {(selectedThread.aiConf * 100).toFixed(0)}%
                </span>
                <button
                  onClick={async () => {
                    if (selectedThread) {
                      await apiClient.updateTicket(selectedThread.id, { status: 'escalated' } as any);
                      loadConversations();
                    }
                  }}
                  className="text-xs px-3 py-1.5 rounded-lg font-semibold transition-colors"
                  style={{ background: '#cd4239', color: '#fff' }}
                >
                  🔁 Handoff
                </button>
              </div>
            </div>

            {/* Messages */}
            <div className="flex-1 overflow-y-auto px-5 py-5 space-y-4">
              {messages.map(msg => (
                <div key={msg.id} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                  <div className={`max-w-lg ${msg.role === 'user' ? 'order-last' : ''}`}>
                    {msg.role === 'assistant' && (
                      <div className="flex items-center gap-2 mb-1.5">
                        <div className="w-5 h-5 rounded-full flex items-center justify-center text-xs"
                          style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}>
                          🤖
                        </div>
                        <span className="text-xs font-medium" style={{ color: 'var(--color-muted-foreground)' }}>
                          {msg.agentType?.replace('_', ' ') || 'AI Agent'}
                          {msg.confidence && (
                            <span className="ml-1.5 text-xs" style={{ color: '#2c8c66' }}>
                              · {(msg.confidence * 100).toFixed(0)}% conf
                            </span>
                          )}
                        </span>
                      </div>
                    )}
                    <div
                      className="px-4 py-3 rounded-2xl text-sm leading-relaxed"
                      style={{
                        background: msg.role === 'user' ? 'var(--color-primary)' : 'var(--color-card)',
                        color: msg.role === 'user' ? 'var(--color-on-primary)' : 'var(--color-foreground)',
                        border: msg.role !== 'user' ? '1px solid var(--color-border)' : 'none',
                        borderRadius: msg.role === 'user' ? '18px 18px 4px 18px' : '4px 18px 18px 18px',
                      }}
                    >
                      {msg.content}
                    </div>
                    <div className="text-xs mt-1 px-1" style={{ color: 'var(--color-muted-foreground)' }}>
                      {msg.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                    </div>
                  </div>
                </div>
              ))}
              {isTyping && (
                <div className="flex justify-start">
                  <div className="px-4 py-3 rounded-2xl text-sm" style={{ background: 'var(--color-card)', border: '1px solid var(--color-border)', borderRadius: '4px 18px 18px 18px' }}>
                    <div className="flex gap-1 items-center h-4">
                      {[0, 1, 2].map(i => (
                        <div key={i} className="w-1.5 h-1.5 rounded-full animate-bounce" style={{ background: 'var(--color-muted-foreground)', animationDelay: `${i * 0.15}s` }} />
                      ))}
                    </div>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>

            {/* AI Copilot Suggestions */}
            {showCopilot && (
              <div className="px-5 py-3 border-t" style={{ background: 'rgba(44,132,224,0.05)', borderColor: 'var(--color-border)' }}>
                <div className="flex items-start gap-2">
                  <span className="text-base flex-shrink-0">🤖</span>
                  <div className="flex-1">
                    <p className="text-xs font-semibold mb-1.5" style={{ color: '#2c84e0' }}>AI Copilot — Next Best Actions</p>
                    <div className="flex gap-2 flex-wrap">
                      {['Apply coupon', 'Send follow-up', 'Schedule callback'].map(action => (
                        <button key={action} className="text-xs px-2.5 py-1 rounded-lg border transition-colors hover:bg-blue-500/10"
                          style={{ borderColor: 'rgba(44,132,224,0.3)', color: '#2c84e0' }}>
                          {action}
                        </button>
                      ))}
                    </div>
                  </div>
                  <button onClick={() => setShowCopilot(false)} className="text-xs" style={{ color: 'var(--color-muted-foreground)' }}>✕</button>
                </div>
              </div>
            )}

            {/* Input */}
            <div className="px-5 py-4 border-t flex-shrink-0" style={{ background: 'var(--color-card)', borderColor: 'var(--color-border)' }}>
              <div className="flex items-end gap-3 p-3 rounded-xl border" style={{ borderColor: 'var(--color-border)', background: 'var(--color-background)' }}>
                <div className="flex gap-2 mb-0.5">
                  <button className="text-sm text-white/40 hover:text-white/70 transition-colors" title="Attach file">📎</button>
                  <button className="text-sm text-white/40 hover:text-white/70 transition-colors" title="Voice input">🎤</button>
                </div>
                <textarea
                  id="chat-input"
                  className="flex-1 bg-transparent text-sm resize-none outline-none"
                  style={{ color: 'var(--color-foreground)' }}
                  placeholder="Type a reply…"
                  rows={1}
                  value={inputText}
                  onChange={e => setInputText(e.target.value)}
                  onKeyDown={e => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); } }}
                />
                <button
                  id="chat-send-btn"
                  onClick={sendMessage}
                  disabled={!inputText.trim()}
                  className="px-4 py-2 rounded-lg text-sm font-semibold transition-all disabled:opacity-40"
                  style={{ background: 'var(--color-primary)', color: 'var(--color-on-primary)' }}
                >
                  Send
                </button>
              </div>
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center" style={{ background: 'var(--color-card)' }}>
            <div className="text-center p-8">
              <div className="text-4xl mb-4">💬</div>
              <h2 className="text-xl font-bold mb-2" style={{ color: 'var(--color-foreground)' }}>Select a conversation</h2>
              <p className="text-sm" style={{ color: 'var(--color-muted-foreground)' }}>
                Choose a conversation from the list to start chatting
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}