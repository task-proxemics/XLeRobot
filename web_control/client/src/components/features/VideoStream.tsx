import React, { useEffect, useRef, useState } from 'react';
import { Card } from '../ui/Card';
import { Button } from '../ui/Button';
import { StatusBadge } from '../ui/StatusBadge';
import { Play, Square, Camera } from 'lucide-react';
import { Socket } from 'socket.io-client';

interface VideoStreamProps {
  socket: Socket | null;
  connected: boolean;
  onStartStream: () => void;
  onStopStream: () => void;
}

export const VideoStream: React.FC<VideoStreamProps> = ({
  socket,
  connected,
  onStartStream,
  onStopStream
}) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [isStreaming, setIsStreaming] = useState(false);
  const [frameCount, setFrameCount] = useState(0);

  useEffect(() => {
    if (!socket) return;

    const handleVideoFrame = (data: any) => {
      if (canvasRef.current) {
        const ctx = canvasRef.current.getContext('2d');
        if (ctx) {
          setFrameCount(prev => prev + 1);
          
          if (data.frame) {
            const img = new Image();
            img.onload = () => {
              ctx.drawImage(img, 0, 0, 640, 480);
              
              // Display frame info
              ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
              ctx.fillRect(0, 0, 200, 30);
              ctx.fillStyle = '#0f0';
              ctx.font = '14px monospace';
              ctx.fillText(`Frame: ${frameCount} | ${new Date().toLocaleTimeString()}`, 10, 20);
            };
            img.src = `data:image/jpeg;base64,${data.frame}`;
          } else {
            // Display placeholder
            ctx.fillStyle = '#1f2937';
            ctx.fillRect(0, 0, 640, 480);
            ctx.fillStyle = '#fff';
            ctx.font = '20px system-ui';
            ctx.fillText('Waiting for video stream...', 200, 240);
            
            // Display camera icon
            ctx.strokeStyle = '#4b5563';
            ctx.lineWidth = 2;
            ctx.strokeRect(280, 200, 80, 60);
            ctx.beginPath();
            ctx.arc(320, 230, 15, 0, 2 * Math.PI);
            ctx.stroke();
          }
        }
      }
    };

    socket.on('video_frame', handleVideoFrame);

    return () => {
      socket.off('video_frame', handleVideoFrame);
    };
  }, [socket, frameCount]);

  const handleStartStream = () => {
    onStartStream();
    setIsStreaming(true);
    setFrameCount(0);
  };

  const handleStopStream = () => {
    onStopStream();
    setIsStreaming(false);
  };

  return (
    <Card title="Video Stream" className="h-fit">
      <div className="flex items-center justify-between mb-4">
        <div className="flex space-x-2">
          <Button
            onClick={handleStartStream}
            disabled={!connected || isStreaming}
            variant="success"
            size="sm"
          >
            <Play className="w-4 h-4 mr-1" />
            Start Video Stream
          </Button>
          <Button
            onClick={handleStopStream}
            disabled={!connected || !isStreaming}
            variant="danger"
            size="sm"
          >
            <Square className="w-4 h-4 mr-1" />
            Stop Video Stream
          </Button>
        </div>
        
        <StatusBadge
          status={isStreaming ? 'connected' : 'disconnected'}
          text={isStreaming ? 'Streaming' : 'Stopped'}
          pulse={isStreaming}
        />
      </div>
      
      <div className="bg-gray-900 rounded-lg overflow-hidden border-2 border-gray-200">
        <canvas
          ref={canvasRef}
          width={640}
          height={480}
          className="w-full h-auto object-cover block"
        />
      </div>
      
      <div className="mt-4 grid grid-cols-2 gap-4 text-sm text-gray-600">
        <div className="flex items-center">
          <Camera className="w-4 h-4 mr-2" />
          <span className="font-medium">Transmission Mode:</span>
          <span className="ml-2">Socket.IO</span>
        </div>
        <div>
          <span className="font-medium">Frames Received:</span>
          <span className="ml-2 font-mono text-blue-600">{frameCount}</span>
        </div>
      </div>
    </Card>
  );
};