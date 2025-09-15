"""
视频流处理模块
第三阶段将实现 WebRTC 视频传输
"""

from typing import Optional
import asyncio
import json
import base64
import numpy as np

class VideoStreamManager:
    """视频流管理器"""
    
    def __init__(self):
        self.streaming = False
        self.frame_rate = 30  # FPS
        self.frame_interval = 1.0 / self.frame_rate
        self.stream_tasks = {}  # 跟踪每个客户端的流任务
        
    async def start_stream(self):
        """开始视频流"""
        self.streaming = True
        print("视频流已启动")
        return {'status': 'streaming_started'}
    
    async def stop_stream(self, sid: str = None):
        """停止视频流"""
        self.streaming = False
        
        # 取消指定客户端的流任务
        if sid and sid in self.stream_tasks:
            task = self.stream_tasks[sid]
            if not task.cancelled():
                task.cancel()
                print(f"已取消客户端 {sid} 的视频流任务")
            del self.stream_tasks[sid]
        
        # 如果没有指定客户端，取消所有流任务
        elif sid is None:
            for client_sid, task in list(self.stream_tasks.items()):
                if not task.cancelled():
                    task.cancel()
                    print(f"已取消客户端 {client_sid} 的视频流任务")
            self.stream_tasks.clear()
        
        print("视频流已停止")
        return {'status': 'streaming_stopped'}
    
    async def get_test_frame(self) -> dict:
        """
        获取视频帧（从机器人控制器或测试数据）
        """
        from robot_interface.factory import get_current_controller
        
        # 获取当前机器人控制器
        controller = get_current_controller()
        
        # 尝试从控制器获取真实画面
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
            # 回退到测试数据
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
        持续发送视频帧到客户端
        """
        try:
            while self.streaming:
                try:
                    # 检查任务是否被取消
                    if asyncio.current_task().cancelled():
                        print(f"客户端 {sid} 的流任务被取消")
                        break
                        
                    frame_data = await self.get_test_frame()
                    await socket_io.emit('video_frame', frame_data, to=sid)
                    await asyncio.sleep(self.frame_interval)
                except asyncio.CancelledError:
                    print(f"客户端 {sid} 的流任务被取消")
                    break
                except Exception as e:
                    print(f"流传输错误: {e}")
                    break
        finally:
            # 清理任务引用
            if sid in self.stream_tasks:
                del self.stream_tasks[sid]
            print(f"客户端 {sid} 的视频流已结束")

# 创建全局视频流管理器实例
video_manager = VideoStreamManager()

# WebRTC 相关的占位代码（第三阶段实现）
class WebRTCManager:
    """WebRTC 管理器（第三阶段实现）"""
    
    def __init__(self):
        self.peer_connections = {}
        
    async def handle_offer(self, offer: dict, sid: str) -> dict:
        """
        处理 WebRTC offer
        第三阶段将实现完整的 WebRTC 信令交换
        """
        # TODO: 实现 aiortc 的 RTCPeerConnection 处理
        return {
            'type': 'answer',
            'sdp': 'placeholder_answer_sdp'
        }
    
    async def handle_ice_candidate(self, candidate: dict, sid: str):
        """处理 ICE 候选"""
        # TODO: 实现 ICE 候选处理
        pass
    
    async def close_connection(self, sid: str):
        """关闭 WebRTC 连接"""
        if sid in self.peer_connections:
            # TODO: 清理 peer connection
            del self.peer_connections[sid]

webrtc_manager = WebRTCManager()