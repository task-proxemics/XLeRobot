"""
Video streaming module
"""

from typing import Optional
import asyncio
import json
import base64
import numpy as np

class VideoStreamManager:
    """Video stream manager"""
    
    def __init__(self):
        self.streaming = False
        self.frame_rate = 30  # FPS
        self.frame_interval = 1.0 / self.frame_rate
        self.stream_tasks = {}
        
    async def start_stream(self):
        """Start video stream"""
        self.streaming = True
        print("Video stream started")
        return {'status': 'streaming_started'}
    
    async def stop_stream(self, sid: str = None):
        """Stop video stream"""
        self.streaming = False
        
        if sid and sid in self.stream_tasks:
            task = self.stream_tasks[sid]
            if not task.cancelled():
                task.cancel()
                print(f"Cancelled video stream task for client {sid}")
            del self.stream_tasks[sid]
        
        elif sid is None:
            for client_sid, task in list(self.stream_tasks.items()):
                if not task.cancelled():
                    task.cancel()
                    print(f"Cancelled video stream task for client {client_sid}")
            self.stream_tasks.clear()
        
        print("Video stream stopped")
        return {'status': 'streaming_stopped'}
    
    async def get_test_frame(self) -> dict:
        """
        Get video frame from robot controller or test data
        """
        from robot_interface.factory import get_current_controller
        
        controller = get_current_controller()
        
        frame_base64 = None
        if controller and controller.is_connected():
            frame_base64 = await controller.get_camera_frame_base64()
        
        if frame_base64:
            return {
                'frame': frame_base64,
                'width': 640,
                'height': 480,
                'channels': 3,
                'timestamp': asyncio.get_event_loop().time(),
                'source': controller.get_controller_type().lower() if controller else 'unknown'
            }
        else:
            test_frame = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
            frame_bytes = test_frame.tobytes()
            frame_base64 = base64.b64encode(frame_bytes).decode('utf-8')
            
            return {
                'frame': frame_base64,
                'width': 640,
                'height': 480,
                'channels': 3,
                'timestamp': asyncio.get_event_loop().time(),
                'source': 'test'
            }
    
    async def stream_frames(self, socket_io, sid: str):
        """
        Stream video frames to client continuously
        """
        try:
            while self.streaming:
                try:
                    if asyncio.current_task().cancelled():
                        print(f"Stream task cancelled for client {sid}")
                        break
                        
                    frame_data = await self.get_test_frame()
                    await socket_io.emit('video_frame', frame_data, to=sid)
                    await asyncio.sleep(self.frame_interval)
                except asyncio.CancelledError:
                    print(f"Stream task cancelled for client {sid}")
                    break
                except Exception as e:
                    print(f"Stream error: {e}")
                    break
        finally:
            if sid in self.stream_tasks:
                del self.stream_tasks[sid]
            print(f"Video stream ended for client {sid}")

video_manager = VideoStreamManager()

class WebRTCManager:
    """WebRTC manager (placeholder)"""
    
    def __init__(self):
        self.peer_connections = {}
        
    async def handle_offer(self, offer: dict, sid: str) -> dict:
        """
        Handle WebRTC offer
        """
        return {
            'type': 'answer',
            'sdp': 'placeholder_answer_sdp'
        }
    
    async def handle_ice_candidate(self, candidate: dict, sid: str):
        """Handle ICE candidate"""
        pass
    
    async def close_connection(self, sid: str):
        """Close WebRTC connection"""
        if sid in self.peer_connections:
            del self.peer_connections[sid]

webrtc_manager = WebRTCManager()