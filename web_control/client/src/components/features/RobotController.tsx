import React from 'react';
import { Card } from '../ui/Card';
import { Button } from '../ui/Button';
import { ArrowUp, ArrowDown, ArrowLeft, ArrowRight, Wifi, StopCircle } from 'lucide-react';

interface RobotControllerProps {
  connected: boolean;
  onSendPing: () => void;
  onMoveCommand: (direction: string) => void;
}

export const RobotController: React.FC<RobotControllerProps> = ({
  connected,
  onSendPing,
  onMoveCommand
}) => {
  return (
    <Card title="Robot Control" className="h-fit">
      <div className="mb-6">
        <h4 className="text-sm font-medium text-gray-700 mb-3">Connection Test</h4>
        <Button
          onClick={onSendPing}
          disabled={!connected}
          variant="secondary"
          className="w-full"
        >
          <Wifi className="w-4 h-4 mr-2" />
          Send Ping
        </Button>
      </div>

      <div className="mb-6">
        <h4 className="text-sm font-medium text-gray-700 mb-3">Movement Control</h4>
        <div className="space-y-3">
          <div className="flex space-x-2">
            <Button
              onClick={() => onMoveCommand('forward')}
              disabled={!connected}
              className="flex-1"
            >
              <ArrowUp className="w-4 h-4 mr-1" />
              Forward
            </Button>
            <Button
              onClick={() => onMoveCommand('backward')}
              disabled={!connected}
              className="flex-1"
            >
              <ArrowDown className="w-4 h-4 mr-1" />
              Backward
            </Button>
          </div>
          
          <div className="flex space-x-2">
            <Button
              onClick={() => onMoveCommand('left')}
              disabled={!connected}
              className="flex-1"
            >
              <ArrowLeft className="w-4 h-4 mr-1" />
              Left
            </Button>
            <Button
              onClick={() => onMoveCommand('right')}
              disabled={!connected}
              className="flex-1"
            >
              <ArrowRight className="w-4 h-4 mr-1" />
              Right
            </Button>
          </div>

          <Button
            onClick={() => onMoveCommand('stop')}
            disabled={!connected}
            variant="danger"
            size="lg"
            className="w-full"
          >
            <StopCircle className="w-5 h-5 mr-2" />
            Emergency Stop
          </Button>
        </div>
      </div>

      <div className="text-xs text-gray-500 text-center">
        Use direction buttons to control robot movement
      </div>
    </Card>
  );
};