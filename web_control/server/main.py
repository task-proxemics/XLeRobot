# XLeRobot Web Control Server

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
import uvicorn
import asyncio
from api.streaming import video_manager, webrtc_manager
from robot_interface.factory import get_or_create_controller, cleanup_controller

# Get controller type from environment variable or default to mujoco
CONTROLLER_TYPE = os.environ.get('ROBOT_CONTROLLER', 'mujoco')
print(f"🤖 Using {CONTROLLER_TYPE} controller")

# Create robot controller using factory
robot_controller = get_or_create_controller(
    controller_type=CONTROLLER_TYPE,
    config={
        'enable_viewer': False  # No GUI for web server
    }
)

# 应用启动事件
async def startup_event():
    # Initialize robot controller on startup
    print("正在初始化机器人控制器...")
    if robot_controller:
        await robot_controller.connect()
        print(f"✅ {robot_controller.get_controller_type()} 初始化完成")
    else:
        print("❌ 机器人控制器初始化失败")

# 应用关闭事件
async def shutdown_event():
    # Cleanup resources on shutdown
    print("正在关闭机器人控制器...")
    if robot_controller:
        await robot_controller.disconnect()
    cleanup_controller()
    print("✅ 机器人控制器已关闭")

# 创建 Socket.IO 服务器
sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*',  # 开发环境允许所有来源，生产环境需要限制
    logger=True,
    engineio_logger=True
)

# 创建 FastAPI 应用
app = FastAPI(title="XLeRobot Web Control API", version="0.1.0")

# 注册启动和关闭事件
app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 开发服务器
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 将 Socket.IO 挂载到 FastAPI
socket_app = socketio.ASGIApp(sio, app)

@app.get("/")
async def root():
    """根路径测试端点"""
    return {"message": "XLeRobot Web Control Server is running"}

@app.get("/health")
async def health_check():
    """健康检查端点"""
    controller_info = {}
    if robot_controller:
        controller_info = {
            'type': robot_controller.get_controller_type(),
            'connected': robot_controller.is_connected(),
            'capabilities': robot_controller.get_capabilities()
        }
    
    return {
        "status": "healthy", 
        "service": "XLeRobot Web Control",
        "controller": controller_info
    }

@app.get("/robot/info")
async def robot_info():
    """机器人控制器信息端点"""
    if not robot_controller:
        return {"error": "No robot controller available"}
    
    return {
        'controller_type': robot_controller.get_controller_type(),
        'connected': robot_controller.is_connected(),
        'capabilities': robot_controller.get_capabilities(),
        'state': await robot_controller.get_state() if robot_controller.is_connected() else None
    }

@app.get("/robot/controllers")
async def available_controllers():
    """获取可用控制器列表"""
    from robot_interface.factory import RobotControllerFactory
    return RobotControllerFactory.get_available_controllers()

# Socket.IO 事件处理器
@sio.event
async def connect(sid, environ, auth):
    """客户端连接事件"""
    print(f"客户端已连接: {sid}")
    await sio.emit('connection_established', {'message': '成功连接到 XLeRobot 控制服务器'}, to=sid)

@sio.event
async def disconnect(sid):
    """客户端断开连接事件"""
    print(f"客户端已断开: {sid}")
    
    # 清理该客户端的视频流任务
    if sid in video_manager.stream_tasks:
        task = video_manager.stream_tasks[sid]
        if not task.cancelled():
            task.cancel()
            print(f"已取消断开客户端 {sid} 的视频流任务")
        del video_manager.stream_tasks[sid]

@sio.event
async def ping(sid, data):
    """测试用 ping-pong 事件"""
    print(f"收到来自 {sid} 的 ping: {data}")
    await sio.emit('pong', {'message': 'pong', 'timestamp': data.get('timestamp')}, to=sid)

@sio.event
async def move_command(sid, data):
    """移动命令处理器"""
    direction = data.get('direction')
    speed = data.get('speed', 1.0)
    print(f"收到移动命令: 方向={direction}, 速度={speed}")
    
    if not robot_controller:
        await sio.emit('command_received', {
            'type': 'move',
            'status': 'error',
            'message': 'Robot controller not available'
        }, to=sid)
        return
    
    # 调用机器人控制器
    result = await robot_controller.move(direction, speed)
    
    # 获取当前状态
    robot_state = await robot_controller.get_state()
    
    await sio.emit('command_received', {
        'type': 'move',
        'direction': direction,
        'speed': speed,
        'status': result.get('status', 'executed'),
        'robot_state': robot_state
    }, to=sid)

# 视频流相关事件处理器
@sio.event
async def start_video_stream(sid):
    """开始视频流传输"""
    print(f"客户端 {sid} 请求开始视频流")
    
    # 如果该客户端已有流任务，先取消
    if sid in video_manager.stream_tasks:
        task = video_manager.stream_tasks[sid]
        if not task.cancelled():
            task.cancel()
        del video_manager.stream_tasks[sid]
    
    result = await video_manager.start_stream()
    await sio.emit('stream_status', result, to=sid)
    
    # 启动帧传输任务并跟踪
    task = asyncio.create_task(video_manager.stream_frames(sio, sid))
    video_manager.stream_tasks[sid] = task

@sio.event
async def stop_video_stream(sid):
    """停止视频流传输"""
    print(f"客户端 {sid} 请求停止视频流")
    result = await video_manager.stop_stream(sid)  # 传递 sid 参数
    await sio.emit('stream_status', result, to=sid)

@sio.event
async def webrtc_offer(sid, data):
    """处理 WebRTC offer（第三阶段实现）"""
    print(f"收到来自 {sid} 的 WebRTC offer")
    answer = await webrtc_manager.handle_offer(data, sid)
    await sio.emit('webrtc_answer', answer, to=sid)

@sio.event
async def webrtc_ice_candidate(sid, data):
    """处理 ICE 候选（第三阶段实现）"""
    await webrtc_manager.handle_ice_candidate(data, sid)

if __name__ == "__main__":
    # 启动服务器
    # 使用导入字符串来支持 reload 功能
    uvicorn.run(
        "main:socket_app",  # 使用导入字符串格式
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )