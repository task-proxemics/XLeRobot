import React, { useEffect, useRef } from 'react';
import type { Socket } from 'socket.io-client';
import { 
  Battery, 
  Thermometer, 
  Zap, 
  Square, 
  Play, 
  Camera, 
  Circle, 
  Gauge, 
  Monitor, 
  Wifi, 
  Radio, 
  WifiOff, 
  AlertTriangle, 
  RefreshCw, 
  Settings 
} from 'lucide-react';

interface RobotVideoCanvasProps {
  socket: Socket | null;
  videoStatus: string;
  telemetry: {
    battery: string;
    temp: string;
    speed: string;
    voltage: string;
  };
  latency: number;
  fps: number;
  recording: boolean;
  onSnapshot: () => void;
  onToggleRecording: () => void;
  onToggleVideoStream: () => void;
  theme: 'light' | 'dark';
}

export function RobotVideoCanvas({
  socket,
  videoStatus,
  telemetry,
  latency,
  fps,
  recording,
  onSnapshot,
  onToggleRecording,
  onToggleVideoStream,
  theme
}: RobotVideoCanvasProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  // Canvas animation effect - only when no real video
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    
    let animationId: number;
    let time = 0;

    const draw = () => {
      // Only animate when not streaming real video
      if (videoStatus === 'streaming') {
        return;
      }

      time += 0.016;
      const width = canvas.width;
      const height = canvas.height;

      // Create animated gradient background
      const gradient = ctx.createLinearGradient(0, 0, width, height);
      const alpha = 0.5 + 0.5 * Math.sin(time * 0.4);
      gradient.addColorStop(0, `rgba(${120 + Math.floor(60 * alpha)}, 140, 200, 1)`);
      gradient.addColorStop(1, `rgba(60, ${80 + Math.floor(80 * alpha)}, 160, 1)`);
      
      ctx.fillStyle = gradient;
      ctx.fillRect(0, 0, width, height);

      // Draw animated elements (simulating robot vision)
      for (let i = 0; i < 5; i++) {
        const x = (0.5 + 0.35 * Math.sin(time * (0.5 + i * 0.16) + i)) * width;
        const y = (0.5 + 0.35 * Math.cos(time * (0.6 + i * 0.12) + i)) * height;
        const radius = 14 + 8 * Math.sin(time * (0.7 + i * 0.08));
        
        ctx.beginPath();
        ctx.fillStyle = `rgba(${200 - i * 20}, ${180 - i * 10}, ${160 + i * 12}, 0.9)`;
        ctx.arc(x, y, Math.abs(radius), 0, Math.PI * 2);
        ctx.fill();
      }

      // Draw demo overlays
      drawVideoOverlays(ctx, width, height);

      animationId = requestAnimationFrame(draw);
    };

    const resizeCanvas = () => {
      const rect = canvas.getBoundingClientRect();
      canvas.width = rect.width * devicePixelRatio;
      canvas.height = rect.height * devicePixelRatio;
      ctx.scale(devicePixelRatio, devicePixelRatio);
      canvas.style.width = rect.width + 'px';
      canvas.style.height = rect.height + 'px';
    };

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    animationId = requestAnimationFrame(draw);

    return () => {
      cancelAnimationFrame(animationId);
      window.removeEventListener('resize', resizeCanvas);
    };
  }, [videoStatus]);

  // Listen for video frames from socket
  useEffect(() => {
    if (!socket) return;

    const handleVideoFrame = (data: any) => {
      const canvas = canvasRef.current;
      if (!canvas) return;

      const ctx = canvas.getContext('2d');
      if (!ctx) return;

      // Get the logical dimensions (CSS pixels) for correct drawing
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;

      // Calculate logical dimensions
      const logicalWidth = canvas.width / dpr;
      const logicalHeight = canvas.height / dpr;

      try {
        if (data.frame) {
          // If server sends base64 image data
          const img = new Image();

          img.onload = () => {
            // Clear canvas and draw using logical dimensions
            ctx.clearRect(0, 0, logicalWidth, logicalHeight);
            ctx.drawImage(img, 0, 0, logicalWidth, logicalHeight);

            // Draw overlays on top of real video using logical dimensions
            drawVideoOverlays(ctx, logicalWidth, logicalHeight);
          };

          img.onerror = (error) => {
            console.error('Error processing video frame:', error);
          };

          img.src = `data:image/jpeg;base64,${data.frame}`;
        } else if (data.url) {
          // If server sends image URL
          const img = new Image();

          img.onload = () => {
            ctx.clearRect(0, 0, logicalWidth, logicalHeight);
            ctx.drawImage(img, 0, 0, logicalWidth, logicalHeight);
            drawVideoOverlays(ctx, logicalWidth, logicalHeight);
          };

          img.onerror = (error) => {
            console.error('Error loading image from URL:', error);
          };

          img.src = data.url;
        }
      } catch (error) {
        console.error('Error processing video frame:', error);
      }
    };

    socket.on('video_frame', handleVideoFrame);

    return () => {
      socket.off('video_frame', handleVideoFrame);
    };
  }, [socket]);

  // Function to draw overlays on top of video
  const drawVideoOverlays = (ctx: CanvasRenderingContext2D, width: number, height: number) => {
    // Draw grid overlay (robot vision effect)
    ctx.strokeStyle = 'rgba(0, 255, 255, 0.3)';
    ctx.lineWidth = 1;
    const gridSize = 50;
    for (let x = 0; x < width; x += gridSize) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    for (let y = 0; y < height; y += gridSize) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }

    // Draw crosshair in center
    ctx.strokeStyle = 'rgba(0, 255, 255, 0.8)';
    ctx.lineWidth = 2;
    const centerX = width / 2;
    const centerY = height / 2;
    const crossSize = 20;
    
    ctx.beginPath();
    ctx.moveTo(centerX - crossSize, centerY);
    ctx.lineTo(centerX + crossSize, centerY);
    ctx.moveTo(centerX, centerY - crossSize);
    ctx.lineTo(centerX, centerY + crossSize);
    ctx.stroke();

    // Draw corner frame
    ctx.strokeStyle = 'rgba(0, 255, 255, 0.8)';
    ctx.lineWidth = 3;
    const frameSize = 30;
    
    // Top-left
    ctx.beginPath();
    ctx.moveTo(20, 20 + frameSize);
    ctx.lineTo(20, 20);
    ctx.lineTo(20 + frameSize, 20);
    ctx.stroke();

    // Top-right
    ctx.beginPath();
    ctx.moveTo(width - 20 - frameSize, 20);
    ctx.lineTo(width - 20, 20);
    ctx.lineTo(width - 20, 20 + frameSize);
    ctx.stroke();

    // Bottom-left
    ctx.beginPath();
    ctx.moveTo(20, height - 20 - frameSize);
    ctx.lineTo(20, height - 20);
    ctx.lineTo(20 + frameSize, height - 20);
    ctx.stroke();

    // Bottom-right
    ctx.beginPath();
    ctx.moveTo(width - 20 - frameSize, height - 20);
    ctx.lineTo(width - 20, height - 20);
    ctx.lineTo(width - 20, height - 20 - frameSize);
    ctx.stroke();
  };

  const nowTime = () => new Date().toLocaleTimeString();

  return (
    <div className="rounded-2xl overflow-hidden shadow-lg relative bg-black">
      <div className="relative" style={{ paddingTop: '56.25%' }}>
        <canvas 
          ref={canvasRef}
          className="absolute inset-0 w-full h-full"
        />

        {/* Top-left overlays */}
        <div className="absolute top-4 left-4 flex gap-3">
          <div className="flex items-center gap-2 px-3 py-2 bg-black/50 backdrop-blur-sm rounded-md text-white text-xs border border-white/20">
            <Battery size={14} />
            {telemetry.battery}
          </div>
          <div className="flex items-center gap-2 px-3 py-2 bg-black/50 backdrop-blur-sm rounded-md text-white text-xs border border-white/20">
            <Thermometer size={14} />
            {telemetry.temp}
          </div>
          <div className="flex items-center gap-2 px-3 py-2 bg-black/50 backdrop-blur-sm rounded-md text-white text-xs border border-white/20">
            <Zap size={14} />
            {telemetry.voltage}
          </div>
        </div>

        {/* Top-right controls */}
        <div className="absolute top-4 right-4 flex gap-2">
          <button
            onClick={onToggleVideoStream}
            className={`flex items-center gap-2 px-3 py-2 rounded-md text-sm shadow transition-all ${
              videoStatus === 'streaming' 
                ? 'bg-red-500 hover:bg-red-600 text-white' 
                : 'bg-white/90 hover:bg-white text-gray-900'
            }`}
          >
            {videoStatus === 'streaming' ? (
              <>
                <Square size={14} />
                Stop
              </>
            ) : (
              <>
                <Play size={14} />
                Start
              </>
            )}
          </button>
          <button
            onClick={onSnapshot}
            className="flex items-center gap-2 px-3 py-2 bg-white/90 hover:bg-white rounded-md text-sm shadow transition-all text-gray-900"
          >
            <Camera size={14} />
            Snapshot
          </button>
          <button
            onClick={onToggleRecording}
            className={`flex items-center gap-2 px-3 py-2 rounded-md text-sm shadow transition-all ${
              recording 
                ? 'bg-red-500 hover:bg-red-600 text-white animate-pulse' 
                : 'bg-white/90 hover:bg-white text-gray-900'
            }`}
          >
            {recording ? (
              <>
                <Circle size={14} className="fill-current" />
                Recording
              </>
            ) : (
              <>
                <Circle size={14} />
                Record
              </>
            )}
          </button>
        </div>

        {/* Recording indicator */}
        {recording && (
          <div className="absolute top-4 left-1/2 transform -translate-x-1/2">
            <div className="bg-red-500 text-white px-4 py-2 rounded-full text-sm font-bold animate-pulse border-2 border-red-300">
              <Circle size={12} className="fill-current" /> REC {nowTime()}
            </div>
          </div>
        )}

        {/* Bottom status bar */}
        <div className="absolute left-1/2 -translate-x-1/2 bottom-4 bg-black/60 backdrop-blur-sm px-6 py-3 rounded-full text-white text-sm flex items-center gap-4 border border-white/20">
          <div className="flex items-center gap-2">
            <Gauge size={14} />
            Speed: <span className="font-mono text-blue-300">{telemetry.speed}</span>
          </div>
          <div className="w-px h-4 bg-white/30"></div>
          <div className="flex items-center gap-2">
            <Monitor size={14} />
            FPS: <span className="font-mono text-green-300">{fps}</span>
          </div>
          <div className="w-px h-4 bg-white/30"></div>
          <div className="flex items-center gap-2">
            <Wifi size={14} />
            Latency: <span className="font-mono text-yellow-300">{latency}ms</span>
          </div>
          <div className="w-px h-4 bg-white/30"></div>
          <div className="flex items-center gap-2">
            <Radio size={14} />
            Status: 
            <span className={`font-mono ${
              videoStatus === 'streaming' ? 'text-green-300' : 
              videoStatus === 'error' ? 'text-red-300' : 'text-gray-300'
            }`}>
              {videoStatus.toUpperCase()}
            </span>
          </div>
        </div>

        {/* Connection status overlay */}
        {videoStatus === 'disconnected' && (
          <div className="absolute inset-0 bg-black/80 flex items-center justify-center">
            <div className="text-center text-white">
              <div className="mb-4">
                <WifiOff size={64} className="mx-auto text-gray-400" />
              </div>
              <div className="text-xl font-bold mb-2">Video Stream Disconnected</div>
              <div className="text-gray-300 mb-4">Click "Start" to begin video stream</div>
              <button
                onClick={onToggleVideoStream}
                className="flex items-center px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-bold transition-colors"
              >
                <Play size={16} className="mr-2" />
                Start Video Stream
              </button>
            </div>
          </div>
        )}

        {/* Error state overlay */}
        {videoStatus === 'error' && (
          <div className="absolute inset-0 bg-red-900/80 flex items-center justify-center">
            <div className="text-center text-white">
              <div className="mb-4">
                <AlertTriangle size={64} className="mx-auto text-red-400" />
              </div>
              <div className="text-xl font-bold mb-2">Video Stream Error</div>
              <div className="text-red-200 mb-4">Unable to connect to video stream</div>
              <button
                onClick={onToggleVideoStream}
                className="flex items-center px-6 py-3 bg-red-600 hover:bg-red-700 text-white rounded-lg font-bold transition-colors"
              >
                <RefreshCw size={16} className="mr-2" />
                Retry Connection
              </button>
            </div>
          </div>
        )}

        {/* Loading state */}
        {videoStatus === 'connecting' && (
          <div className="absolute inset-0 bg-blue-900/80 flex items-center justify-center">
            <div className="text-center text-white">
              <div className="mb-4">
                <Settings size={64} className="mx-auto text-blue-400 animate-spin" />
              </div>
              <div className="text-xl font-bold mb-2">Connecting...</div>
              <div className="text-blue-200">Establishing video stream connection</div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}