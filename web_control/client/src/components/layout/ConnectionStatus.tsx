import React from 'react';
import { StatusBadge } from '../ui/StatusBadge';
import type { SocketStatus } from '../../types';

interface ConnectionStatusProps {
  status: SocketStatus;
  serverUrl: string;
}

export const ConnectionStatus: React.FC<ConnectionStatusProps> = ({
  status,
  serverUrl
}) => {
  const getStatusText = (connectionStatus: string) => {
    switch (connectionStatus) {
      case 'connected': return '已连接';
      case 'connecting': return '连接中';
      case 'disconnected': return '已断开';
      case 'error': return '连接错误';
      default: return '未知状态';
    }
  };

  return (
    <div className="bg-white border-b border-gray-200 px-4 py-3 sticky top-0 z-50">
      <div className="flex items-center justify-between max-w-7xl mx-auto">
        <div className="flex items-center space-x-4">
          <h1 className="text-xl font-bold text-gray-900">XLeRobot 控制台</h1>
        </div>
        
        <div className="flex items-center space-x-4">
          <div className="text-right">
            <div className="flex items-center space-x-2">
              <span className="text-sm text-gray-600">Socket:</span>
              <StatusBadge
                status={status.socket}
                text={getStatusText(status.socket)}
                pulse={status.socket === 'connecting'}
              />
            </div>
            <div className="flex items-center space-x-2 mt-1">
              <span className="text-sm text-gray-600">视频:</span>
              <StatusBadge
                status={status.video}
                text={getStatusText(status.video)}
                pulse={status.video === 'connecting'}
              />
            </div>
          </div>
          
          <div className="text-xs text-gray-400 border-l border-gray-200 pl-4">
            服务器: <span className="font-mono">{serverUrl}</span>
          </div>
        </div>
      </div>
    </div>
  );
};