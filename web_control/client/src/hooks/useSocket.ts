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
  
  // Real robot data states
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

  // Continuous movement state
  const [pressedKeys, setPressedKeys] = useState<Set<string>>(new Set());
  const [currentSpeed, setCurrentSpeed] = useState<number>(1.0);
  const continuousIntervalRef = useRef<NodeJS.Timeout | null>(null);
  const pressedKeysRef = useRef<Set<string>>(new Set());

  // Key mapping for movement
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
    setMessages(prev => [...prev.slice(-49), message]); // Keep last 50 messages
  }, []);

  useEffect(() => {
    const newSocket = io('http://localhost:8000', {
      transports: ['websocket'],
      reconnection: true,
      reconnectionDelay: 1000,
      reconnectionAttempts: 5,
    });

    // Connection events
    newSocket.on('connect', () => {
      console.log('Connected to server');
      setStatus(prev => ({ ...prev, socket: 'connected' }));
      addMessage(`Connected to server (ID: ${newSocket.id})`, 'success');
    });

    newSocket.on('disconnect', () => {
      console.log('Disconnected from server');
      setStatus(prev => ({ ...prev, socket: 'disconnected' }));
      addMessage('Disconnected from server', 'warning');
    });

    newSocket.on('connect_error', (error) => {
      console.error('Connection error:', error);
      setStatus(prev => ({ ...prev, socket: 'error' }));
      addMessage(`Connection error: ${error.message}`, 'error');
    });

    // Robot control events
    newSocket.on('connection_established', (data) => {
      console.log('Server message:', data);
      addMessage(data.message, 'success');
    });

    newSocket.on('pong', (data) => {
      console.log('Received pong:', data);
      addMessage(`Pong: ${JSON.stringify(data)}`, 'info');
    });

    newSocket.on('command_received', (data) => {
      console.log('Command received:', data);
      addMessage(`Command received: ${data.type} - ${data.direction}`, 'success');
    });

    // Video stream events
    newSocket.on('stream_status', (data) => {
      console.log('Stream status update:', data);
      if (data.status === 'streaming_started') {
        setStatus(prev => ({ ...prev, video: 'streaming' }));
        addMessage('Video stream started successfully', 'success');
      } else if (data.status === 'streaming_stopped') {
        setStatus(prev => ({ ...prev, video: 'disconnected' }));
        addMessage('Video stream stopped', 'info');
      }
    });

    newSocket.on('video_stream_error', (error) => {
      console.error('Video stream error:', error);
      setStatus(prev => ({ ...prev, video: 'error' }));
      addMessage(`Video stream error: ${error.message || error}`, 'error');
    });

    newSocket.on('video_frame', (data) => {
      // Video frame received - this will be handled by RobotVideoCanvas component
      console.log('Video frame received:', data.timestamp);
    });

    // Real robot data events
    newSocket.on('telemetry_update', (data) => {
      console.log('Telemetry update:', data);
      setTelemetry({
        battery: data.battery || null,
        temp: data.temperature || null,
        speed: data.speed || null,
        voltage: data.voltage || null
      });
    });

    newSocket.on('network_metrics', (data) => {
      console.log('Network metrics:', data);
      setNetworkMetrics({
        latency: data.latency || null,
        fps: data.fps || null,
        packetLoss: data.packetLoss || null
      });
    });

    newSocket.on('arm_position_update', (data) => {
      console.log('Arm position update:', data);
      setArmPositions({
        angles: data.angles || null,
        positions: data.positions || null
      });
    });

    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, [addMessage]);

  // Continuous movement functions
  const startContinuousMovement = useCallback(() => {
    if (continuousIntervalRef.current) {
      clearInterval(continuousIntervalRef.current);
    }

    continuousIntervalRef.current = setInterval(() => {
      const currentKeys = pressedKeysRef.current;
      if (currentKeys.size === 0) return;

      // Handle multiple keys - prioritize the most recent one
      const keysArray = Array.from(currentKeys);
      const primaryKey = keysArray[keysArray.length - 1]; // Use most recently pressed
      const direction = keyToDirection[primaryKey];

      if (direction && socket && status.socket === 'connected') {
        socket.emit('move_command', { direction, speed: currentSpeed });
        // Only log occasionally to avoid spam
        if (Math.random() < 0.1) {
          addMessage(`Continuous movement: ${direction}`, 'info');
        }
      }
    }, 100); // Send commands every 100ms
  }, [socket, status.socket, currentSpeed, keyToDirection, addMessage]);

  const stopContinuousMovement = useCallback(() => {
    if (continuousIntervalRef.current) {
      clearInterval(continuousIntervalRef.current);
      continuousIntervalRef.current = null;
    }

    // Send stop command
    if (socket && status.socket === 'connected') {
      socket.emit('move_command', { direction: 'stop', speed: 0 });
      addMessage('Movement stopped', 'info');
    }
  }, [socket, status.socket, addMessage]);

  // Keyboard event handlers
  const handleKeyDown = useCallback((event: KeyboardEvent) => {
    const key = event.key;

    // Ignore if key is not a movement key
    if (!keyToDirection[key]) return;

    // Prevent default browser behavior
    event.preventDefault();

    // Ignore repeated keydown events
    if (pressedKeysRef.current.has(key)) return;

    // Add key to pressed keys
    pressedKeysRef.current.add(key);
    setPressedKeys(new Set(pressedKeysRef.current));

    // Start continuous movement if this is the first key
    if (pressedKeysRef.current.size === 1) {
      startContinuousMovement();
    }
  }, [keyToDirection, startContinuousMovement]);

  const handleKeyUp = useCallback((event: KeyboardEvent) => {
    const key = event.key;

    // Ignore if key is not a movement key
    if (!keyToDirection[key]) return;

    // Prevent default browser behavior
    event.preventDefault();

    // Remove key from pressed keys
    pressedKeysRef.current.delete(key);
    setPressedKeys(new Set(pressedKeysRef.current));

    // Stop movement if no keys are pressed
    if (pressedKeysRef.current.size === 0) {
      stopContinuousMovement();
    }
  }, [keyToDirection, stopContinuousMovement]);

  // Add/remove keyboard event listeners
  useEffect(() => {
    // Only add listeners if socket is connected
    if (status.socket === 'connected') {
      window.addEventListener('keydown', handleKeyDown);
      window.addEventListener('keyup', handleKeyUp);

      return () => {
        window.removeEventListener('keydown', handleKeyDown);
        window.removeEventListener('keyup', handleKeyUp);

        // Clean up interval when component unmounts or disconnects
        if (continuousIntervalRef.current) {
          clearInterval(continuousIntervalRef.current);
          continuousIntervalRef.current = null;
        }

        // Reset pressed keys
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

  // Speed control function
  const setMovementSpeed = useCallback((speed: number) => {
    setCurrentSpeed(Math.max(0.1, Math.min(2.0, speed))); // Clamp between 0.1 and 2.0
  }, []);

  return {
    socket,
    status,
    messages,
    sendPing,
    sendMoveCommand,
    startVideoStream,
    stopVideoStream,
    // Real robot data
    telemetry,
    networkMetrics,
    armPositions,
    // Continuous movement
    pressedKeys,
    currentSpeed,
    setMovementSpeed,
    stopContinuousMovement, // Emergency stop function
  };
};