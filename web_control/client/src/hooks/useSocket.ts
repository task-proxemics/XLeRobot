import { useEffect, useState, useCallback, useRef } from 'react';
import { io, Socket } from 'socket.io-client';
import type { SocketStatus, SystemMessage } from '../types';

interface RobotTelemetry {
  battery: string | null;
  temp: string | null;
  speed: string | null;
  voltage: string | null;
}

interface NetworkMetrics {
  latency: number | null;
  fps: number | null;
  packetLoss: number | null;
}

interface ArmPositions {
  angles: number[] | null;
  positions: string[] | null;
}

export const useSocket = () => {
  const [socket, setSocket] = useState<Socket | null>(null);
  const [status, setStatus] = useState<SocketStatus>({
    socket: 'disconnected',
    video: 'disconnected'
  });
  const [messages, setMessages] = useState<SystemMessage[]>([]);

  const [telemetry, setTelemetry] = useState<RobotTelemetry>({
    battery: null,
    temp: null,
    speed: null,
    voltage: null
  });
  
  const [networkMetrics, setNetworkMetrics] = useState<NetworkMetrics>({
    latency: null,
    fps: null,
    packetLoss: null
  });
  
  const [armPositions, setArmPositions] = useState<ArmPositions>({
    angles: null,
    positions: null
  });

  const [pressedKeys, setPressedKeys] = useState<Set<string>>(new Set());
  const [currentSpeed, setCurrentSpeed] = useState<number>(1.0);
  const continuousIntervalRef = useRef<NodeJS.Timeout | null>(null);
  const pressedKeysRef = useRef<Set<string>>(new Set());

  const keyToDirection: { [key: string]: string } = {
    'w': 'forward',
    'W': 'forward',
    's': 'backward',
    'S': 'backward',
    'a': 'left',
    'A': 'left',
    'd': 'right',
    'D': 'right',
    'q': 'rotate_left',
    'Q': 'rotate_left',
    'e': 'rotate_right',
    'E': 'rotate_right',
    'ArrowUp': 'forward',
    'ArrowDown': 'backward',
    'ArrowLeft': 'left',
    'ArrowRight': 'right'
  };

  const addMessage = useCallback((content: string, type: SystemMessage['type'] = 'info') => {
    const message: SystemMessage = {
      id: Date.now().toString(),
      content,
      timestamp: Date.now(),
      type
    };
    setMessages(prev => [...prev.slice(-49), message]);
  }, []);

  useEffect(() => {
    const newSocket = io('http://100.116.148.99:8000', {
      transports: ['websocket'],
      reconnection: true,
      reconnectionDelay: 1000,
      reconnectionAttempts: 5,
    });

    newSocket.on('connect', () => {
      setStatus(prev => ({ ...prev, socket: 'connected' }));
      addMessage(`Connected to server (ID: ${newSocket.id})`, 'success');
    });

    newSocket.on('disconnect', () => {
      setStatus(prev => ({ ...prev, socket: 'disconnected' }));
      addMessage('Disconnected from server', 'warning');
    });

    newSocket.on('connect_error', (error) => {
      setStatus(prev => ({ ...prev, socket: 'error' }));
      addMessage(`Connection error: ${error.message}`, 'error');
    });

    newSocket.on('connection_established', (data) => {
      addMessage(data.message, 'success');
    });

    newSocket.on('pong', (data) => {
      addMessage(`Pong: ${JSON.stringify(data)}`, 'info');
    });

    newSocket.on('command_received', (data) => {
      addMessage(`Command received: ${data.type} - ${data.direction}`, 'success');
    });

    newSocket.on('stream_status', (data) => {
      if (data.status === 'streaming_started') {
        setStatus(prev => ({ ...prev, video: 'streaming' }));
        addMessage('Video stream started successfully', 'success');
      } else if (data.status === 'streaming_stopped') {
        setStatus(prev => ({ ...prev, video: 'disconnected' }));
        addMessage('Video stream stopped', 'info');
      }
    });

    newSocket.on('video_stream_error', (error) => {
      setStatus(prev => ({ ...prev, video: 'error' }));
      addMessage(`Video stream error: ${error.message || error}`, 'error');
    });

    newSocket.on('video_frame', (data) => {
    });

    newSocket.on('telemetry_update', (data) => {
      setTelemetry({
        battery: data.battery || null,
        temp: data.temperature || null,
        speed: data.speed || null,
        voltage: data.voltage || null
      });
    });

    newSocket.on('network_metrics', (data) => {
      setNetworkMetrics({
        latency: data.latency || null,
        fps: data.fps || null,
        packetLoss: data.packetLoss || null
      });
    });

    newSocket.on('arm_position_update', (data) => {
      setArmPositions({
        angles: data.angles || null,
        positions: data.positions || null
      });
    });

    newSocket.on('camera_action_result', (data) => {
      if (data.action === 'reset') {
        if (data.status === 'success') {
          addMessage('Camera reset successful', 'success');
        } else {
          addMessage(`Camera reset failed: ${data.message || 'Unknown error'}`, 'error');
        }
      }
    });

    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, [addMessage]);

  const startContinuousMovement = useCallback(() => {
    if (continuousIntervalRef.current) {
      clearInterval(continuousIntervalRef.current);
    }

    continuousIntervalRef.current = setInterval(() => {
      const currentKeys = pressedKeysRef.current;
      if (currentKeys.size === 0) return;

      const keysArray = Array.from(currentKeys);
      const primaryKey = keysArray[keysArray.length - 1]; // Use most recently pressed
      const direction = keyToDirection[primaryKey];

      if (direction && socket && status.socket === 'connected') {
        socket.emit('move_command', { direction, speed: currentSpeed });
        if (Math.random() < 0.1) {
          addMessage(`Continuous movement: ${direction}`, 'info');
        }
      }
    }, 100);
  }, [socket, status.socket, currentSpeed, keyToDirection, addMessage]);

  const stopContinuousMovement = useCallback(() => {
    if (continuousIntervalRef.current) {
      clearInterval(continuousIntervalRef.current);
      continuousIntervalRef.current = null;
    }

    if (socket && status.socket === 'connected') {
      socket.emit('move_command', { direction: 'stop', speed: 0 });
      addMessage('Movement stopped', 'info');
    }
  }, [socket, status.socket, addMessage]);

  const handleKeyDown = useCallback((event: KeyboardEvent) => {
    const key = event.key;

    if (!keyToDirection[key]) return;

    event.preventDefault();

    if (pressedKeysRef.current.has(key)) return;

    pressedKeysRef.current.add(key);
    setPressedKeys(new Set(pressedKeysRef.current));

    if (pressedKeysRef.current.size === 1) {
      startContinuousMovement();
    }
  }, [keyToDirection, startContinuousMovement]);

  const handleKeyUp = useCallback((event: KeyboardEvent) => {
    const key = event.key;

    if (!keyToDirection[key]) return;

    event.preventDefault();

    pressedKeysRef.current.delete(key);
    setPressedKeys(new Set(pressedKeysRef.current));

    if (pressedKeysRef.current.size === 0) {
      stopContinuousMovement();
    }
  }, [keyToDirection, stopContinuousMovement]);

  useEffect(() => {
    if (status.socket === 'connected') {
      window.addEventListener('keydown', handleKeyDown);
      window.addEventListener('keyup', handleKeyUp);

      return () => {
        window.removeEventListener('keydown', handleKeyDown);
        window.removeEventListener('keyup', handleKeyUp);

        if (continuousIntervalRef.current) {
          clearInterval(continuousIntervalRef.current);
          continuousIntervalRef.current = null;
        }

        pressedKeysRef.current.clear();
        setPressedKeys(new Set());
      };
    }
  }, [status.socket, handleKeyDown, handleKeyUp]);

  const sendPing = useCallback(() => {
    if (socket && status.socket === 'connected') {
      const timestamp = Date.now();
      socket.emit('ping', { timestamp, message: 'ping from client' });
      addMessage(`Sent Ping (timestamp: ${timestamp})`, 'info');
    }
  }, [socket, status.socket, addMessage]);

  const sendMoveCommand = useCallback((direction: string, speed = 1.0) => {
    if (socket && status.socket === 'connected') {
      socket.emit('move_command', { direction, speed });
      addMessage(`Sent move command: ${direction}`, 'info');
    }
  }, [socket, status.socket, addMessage]);

  const startVideoStream = useCallback(() => {
    if (socket && status.socket === 'connected') {
      socket.emit('start_video_stream');
      setStatus(prev => ({ ...prev, video: 'connecting' }));
      addMessage('Starting video stream', 'info');
    }
  }, [socket, status.socket, addMessage]);

  const stopVideoStream = useCallback(() => {
    if (socket && status.socket === 'connected') {
      socket.emit('stop_video_stream');
      setStatus(prev => ({ ...prev, video: 'disconnected' }));
      addMessage('Stopping video stream', 'info');
    }
  }, [socket, status.socket, addMessage]);

  const setMovementSpeed = useCallback((speed: number) => {
    setCurrentSpeed(Math.max(0.1, Math.min(2.0, speed)));
  }, []);

  return {
    socket,
    status,
    messages,
    sendPing,
    sendMoveCommand,
    startVideoStream,
    stopVideoStream,
    telemetry,
    networkMetrics,
    armPositions,
    pressedKeys,
    currentSpeed,
    setMovementSpeed,
    stopContinuousMovement,
  };
};