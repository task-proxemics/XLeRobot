import React from 'react';
import { motion } from 'framer-motion';

interface StatusBadgeProps {
  status: 'connected' | 'connecting' | 'disconnected' | 'error';
  text: string;
  showDot?: boolean;
  pulse?: boolean;
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({
  status,
  text,
  showDot = true,
  pulse = false
}) => {
  const statusConfig = {
    connected: {
      bgColor: 'bg-green-100',
      textColor: 'text-green-800',
      dotColor: 'bg-green-400',
    },
    connecting: {
      bgColor: 'bg-yellow-100',
      textColor: 'text-yellow-800',
      dotColor: 'bg-yellow-400',
    },
    disconnected: {
      bgColor: 'bg-gray-100',
      textColor: 'text-gray-800',
      dotColor: 'bg-gray-400',
    },
    error: {
      bgColor: 'bg-red-100',
      textColor: 'text-red-800',
      dotColor: 'bg-red-400',
    }
  };

  const config = statusConfig[status];

  return (
    <motion.span
      initial={{ opacity: 0, scale: 0.8 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.2 }}
      className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${config.bgColor} ${config.textColor}`}
    >
      {showDot && (
        <div
          className={`w-2 h-2 mr-1.5 ${config.dotColor} ${
            pulse ? 'animate-pulse' : ''
          } rounded-full`}
        />
      )}
      {text}
    </motion.span>
  );
};