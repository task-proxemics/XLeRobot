import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import { Moon, Sun, Radio } from 'lucide-react';
import { useSocket } from './hooks/useSocket';
import { RobotVideoCanvas } from './components/features/RobotVideoCanvas';
import { MultiTabPanel } from './components/features/MultiTabPanel';
import { BottomControlConsole } from './components/features/BottomControlConsole';
import type { SystemMessage } from './types';

function nowTime() {
  return new Date().toLocaleTimeString();
}

export default function App() {
  const {
    socket,
    status,
    messages,
    sendPing,
    sendMoveCommand,
    startVideoStream,
    stopVideoStream,
    telemetry: realTelemetry,
    networkMetrics,
    armPositions,
    // Continuous movement
    pressedKeys,
    currentSpeed,
    setMovementSpeed,
    stopContinuousMovement
  } = useSocket();
  
  // UI State
  const [theme, setTheme] = useState<'light' | 'dark'>('light');
  const [speedLevel, setSpeedLevel] = useState<'low' | 'medium' | 'high'>('medium');
  const [recording, setRecording] = useState(false);
  
  // Helper function to display "N/A" for null data
  const formatValue = (value: string | number | null, fallback = 'N/A') => {
    return value === null ? fallback : value.toString();
  };
  
  // Use real data with fallbacks
  const displayTelemetry = {
    battery: formatValue(realTelemetry.battery),
    speed: formatValue(realTelemetry.speed),
    temp: formatValue(realTelemetry.temp),
    voltage: formatValue(realTelemetry.voltage)
  };
  
  const displayLatency = networkMetrics.latency || 'N/A';
  const displayFps = networkMetrics.fps || 'N/A';
  const displayArmAngles = armPositions.angles || [null, null, null, null];

  // No more mock data - all data comes from real socket events

  // Theme effect
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    if (theme === 'dark') {
      document.body.classList.add('dark');
    } else {
      document.body.classList.remove('dark');
    }
  }, [theme]);

  const handleQuickMove = (direction: string) => {
    const speedMultiplier = speedLevel === 'low' ? 0.5 : speedLevel === 'high' ? 1.5 : 1.0;
    sendMoveCommand(direction, speedMultiplier);
  };

  const handleEmergencyStop = () => {
    // Use the new continuous movement stop function
    stopContinuousMovement();
    // Also send traditional stop command as backup
    sendMoveCommand('stop', 0);
    console.warn('EMERGENCY STOP ACTIVATED - Continuous movement stopped');
  };

  const handleSnapshot = () => {
    // This would be implemented with actual canvas capture
    const timestamp = Date.now();
    const link = document.createElement('a');
    link.download = `xlerobot-snapshot-${timestamp}.png`;
    // In real implementation, this would capture the video canvas
    console.log('Snapshot captured');
  };

  const toggleRecording = () => {
    setRecording(prev => !prev);
    console.log(recording ? 'Recording stopped' : 'Recording started');
  };

  const toggleVideoStream = () => {
    if (status.video === 'streaming') {
      stopVideoStream();
    } else {
      startVideoStream();
    }
  };

  return (
    <div className={`min-h-screen transition-colors duration-200 ${
      theme === 'dark' ? 'bg-gray-900 text-gray-100' : 'bg-gray-50 text-gray-900'
    }`}>
      <div className="max-w-7xl mx-auto px-6 py-6">
        {/* Header */}
        <header className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-4">
            <h1 className="text-2xl font-bold">XLeRobot Control Console</h1>
            <div className="text-sm text-gray-500">
              Session: <span className="font-mono">DEFAULT</span>
            </div>
          </div>

          <div className="flex items-center gap-6">
            {/* Status Panel */}
            <div className={`flex items-center gap-3 p-3 rounded-lg shadow-sm ${
              theme === 'dark' ? 'bg-gray-800' : 'bg-white/80'
            }`}>
              <div className={`w-3 h-3 rounded-full ${
                status.socket === 'connected' ? 'bg-green-400' : 
                status.socket === 'error' ? 'bg-red-500' : 'bg-yellow-400'
              }`} />
              <div className="text-xs">
                Socket: <span className="font-medium">{status.socket}</span>
              </div>
              <div className="text-xs pl-4 border-l border-gray-200">
                Video: <span className="font-medium">{status.video}</span>
              </div>
              <div className="text-xs pl-4 border-l border-gray-200">
                Latency: <span className="font-mono">{displayLatency === 'N/A' ? displayLatency : `${displayLatency}ms`}</span>
              </div>
              {/* Continuous Movement Status */}
              {pressedKeys.size > 0 && (
                <div className="text-xs pl-4 border-l border-green-300">
                  <div className="flex items-center gap-1">
                    <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                    <span className="text-green-600 font-medium">
                      Keys: {Array.from(pressedKeys).join(', ')}
                    </span>
                  </div>
                </div>
              )}
            </div>

            {/* Controls */}
            <div className="flex items-center gap-2">
              <button
                onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}
                className={`flex items-center gap-2 px-3 py-2 rounded-md shadow-sm text-sm transition-colors ${
                  theme === 'dark' ? 'bg-gray-800 hover:bg-gray-700' : 'bg-white/80 hover:bg-white'
                }`}
              >
                {theme === 'light' ? (
                  <>
                    <Moon size={16} />
                    Dark
                  </>
                ) : (
                  <>
                    <Sun size={16} />
                    Light
                  </>
                )}
              </button>
              <button 
                onClick={sendPing}
                className={`flex items-center gap-2 px-3 py-2 rounded-md shadow-sm text-sm transition-colors ${
                  theme === 'dark' ? 'bg-gray-800 hover:bg-gray-700' : 'bg-white/80 hover:bg-white'
                }`}
              >
                <Radio size={16} />
                Ping
              </button>
            </div>
          </div>
        </header>

        {/* Main Layout - 7:5 ratio */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Video Stream Area - 7 columns */}
          <div className="lg:col-span-7">
            <RobotVideoCanvas
              socket={socket}
              videoStatus={status.video}
              telemetry={displayTelemetry}
              latency={displayLatency === 'N/A' ? 'N/A' : Number(displayLatency)}
              fps={displayFps === 'N/A' ? 'N/A' : Number(displayFps)}
              recording={recording}
              onSnapshot={handleSnapshot}
              onToggleRecording={toggleRecording}
              onToggleVideoStream={toggleVideoStream}
              theme={theme}
            />
            <div className="mt-3 text-sm text-gray-500">
              <div className="mb-2">
                Main camera view. Video stream from ManiSkill simulation with XLeRobot.
              </div>
              <div className="text-xs">
                <strong>Keyboard Controls:</strong> WASD or Arrow Keys for movement, Q/E for rotation.
                Press and hold keys for continuous movement - release to stop immediately.
              </div>
            </div>
          </div>

          {/* Side Panel - 5 columns */}
          <div className="lg:col-span-5">
            <MultiTabPanel
              telemetry={displayTelemetry}
              armAngles={displayArmAngles}
              latency={displayLatency === 'N/A' ? 'N/A' : Number(displayLatency)}
              fps={displayFps === 'N/A' ? 'N/A' : Number(displayFps)}
              messages={messages}
              socketStatus={status.socket}
              videoStatus={status.video}
              frameCount={0}
              theme={theme}
            />
          </div>
        </div>
      </div>

      {/* Bottom Control Console - Fixed positioned */}
      <BottomControlConsole
        speedLevel={speedLevel}
        onSpeedChange={setSpeedLevel}
        onQuickMove={handleQuickMove}
        onEmergencyStop={handleEmergencyStop}
        telemetrySpeed={displayTelemetry.speed}
        theme={theme}
        connected={status.socket === 'connected'}
      />
    </div>
  );
}
