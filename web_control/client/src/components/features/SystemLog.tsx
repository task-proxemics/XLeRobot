import React, { useRef, useEffect } from 'react';
import { Card } from '../ui/Card';
import { Terminal, Info, CheckCircle, AlertTriangle, XCircle } from 'lucide-react';
import type { SystemMessage } from '../../types';

interface SystemLogProps {
  messages: SystemMessage[];
}

export const SystemLog: React.FC<SystemLogProps> = ({ messages }) => {
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  const getMessageIcon = (type: SystemMessage['type']) => {
    switch (type) {
      case 'success':
        return <CheckCircle className="w-3 h-3 text-green-500" />;
      case 'warning':
        return <AlertTriangle className="w-3 h-3 text-yellow-500" />;
      case 'error':
        return <XCircle className="w-3 h-3 text-red-500" />;
      default:
        return <Info className="w-3 h-3 text-blue-500" />;
    }
  };

  const getMessageClass = (type: SystemMessage['type']) => {
    switch (type) {
      case 'success':
        return 'bg-green-50 border-green-200 text-green-900';
      case 'warning':
        return 'bg-yellow-50 border-yellow-200 text-yellow-900';
      case 'error':
        return 'bg-red-50 border-red-200 text-red-900';
      default:
        return 'bg-blue-50 border-blue-200 text-blue-900';
    }
  };

  return (
    <Card title="System Log" className="h-[500px] flex flex-col">
      <div className="flex items-center justify-between mb-3">
        <div className="flex items-center text-gray-500">
          <Terminal className="w-4 h-4 mr-2" />
          <span className="text-xs">Show last 50 messages</span>
        </div>
        <span className="text-xs text-gray-400">
          {messages.length} records
        </span>
      </div>
      
      <div
        ref={scrollRef}
        className="flex-1 bg-gray-50 rounded-lg p-3 overflow-y-auto space-y-1"
      >
        {messages.length === 0 ? (
          <div className="text-center text-gray-400 text-sm py-8">
            No messages
          </div>
        ) : (
          messages.map((msg) => (
            <div
              key={msg.id}
              className={`text-sm py-1.5 px-2 rounded border ${getMessageClass(msg.type)} 
                         hover:shadow-sm transition-all flex items-start space-x-2`}
            >
              <div className="mt-0.5">{getMessageIcon(msg.type)}</div>
              <div className="flex-1">
                <span className="text-xs text-gray-500 mr-2">
                  {new Date(msg.timestamp).toLocaleTimeString()}
                </span>
                <span className="font-mono text-xs">{msg.content}</span>
              </div>
            </div>
          ))
        )}
      </div>
    </Card>
  );
};