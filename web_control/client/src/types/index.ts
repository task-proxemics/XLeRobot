export interface SocketStatus {
  socket: 'connected' | 'connecting' | 'disconnected' | 'error';
  video: 'connected' | 'connecting' | 'disconnected' | 'error';
}

export interface RobotCommand {
  direction: 'forward' | 'backward' | 'left' | 'right' | 'stop';
  speed?: number;
}

export interface VideoStreamData {
  frame?: string;
  source?: string;
  timestamp: number;
}

export interface SystemMessage {
  id: string;
  content: string;
  timestamp: number;
  type: 'info' | 'success' | 'warning' | 'error';
}

export interface JoystickData {
  angle: {
    radian: number;
    degree: number;
  };
  force: number;
  distance: number;
}