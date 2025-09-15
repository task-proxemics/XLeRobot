# XLeRobot Web Control System

基于 WebSocket 和 WebRTC 的 XLeRobot 网页控制系统。

## 项目结构

```
web_control/
├── server/                 # 后端服务器 (FastAPI + Socket.IO)
│   ├── main.py            # 主服务器文件
│   ├── requirements.txt   # Python 依赖
│   ├── api/               # API 模块
│   │   ├── __init__.py
│   │   └── streaming.py   # 视频流处理
│   └── robot_interface/   # 机器人接口
│       ├── __init__.py
│       └── sim_interface.py # 仿真接口
└── client/                # 前端客户端 (React + TypeScript)
    ├── src/
    │   ├── App.tsx        # 主应用组件
    │   ├── components/    # React 组件
    │   │   └── VideoStream.tsx
    │   └── services/      # 服务层
    │       ├── socketService.ts
    │       └── webrtcService.ts
    └── package.json       # Node.js 依赖
```

## 快速开始

### 前提条件

- Python 3.11.9
- Node.js 18.x LTS
- npm 或 yarn

### 1. 安装后端依赖

```bash
cd web_control/server

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. 安装前端依赖

```bash
cd web_control/client
npm install
# 或
yarn install
```

### 3. 启动后端服务器

```bash
cd web_control/server
python main.py
```

服务器将在 http://localhost:8000 启动

### 4. 启动前端开发服务器

新开一个终端：

```bash
cd web_control/client
npm start
# 或
yarn start
```

前端将在 http://localhost:3000 启动

## 功能测试

### ✅ 第一阶段成功标志

1. 打开浏览器访问 http://localhost:3000
2. 页面显示"已连接"状态（绿色）
3. 点击"发送 Ping"按钮，消息日志显示 ping-pong 通信
4. 浏览器控制台无 CORS 或版本不兼容错误
5. 后端控制台显示"客户端已连接"日志

### 基础功能

- **WebSocket 连接测试**: Ping-Pong 通信验证
- **移动控制按钮**: 前进、后退、左转、右转、停止（占位功能）
- **视频流框架**: 基础视频流传输结构（待实现 WebRTC）
- **实时消息日志**: 显示所有通信事件

## 开发计划

### 第二阶段：仿真控制
- 集成 MuJoCo 仿真环境
- 实现实际的机器人控制逻辑
- 通过网页控制仿真机器人

### 第三阶段：WebRTC 视频流
- 使用 aiortc 实现 WebRTC 服务器
- 低延迟视频传输
- 从 MuJoCo 获取第一人称视角

### 第四阶段：高级控制
- 虚拟摇杆（nipplejs）
- 机械臂关节控制
- 状态反馈面板
- 紧急停止功能

### 第五阶段：远程访问
- Tailscale/ngrok 集成
- 公网访问配置
- 完整文档编写

## 技术栈

### 后端
- **Python**: 3.11.9
- **FastAPI**: 0.116.1
- **python-socketio**: 5.13.0
- **Uvicorn**: 0.29.0

### 前端
- **React**: 19.x (TypeScript)
- **socket.io-client**: 4.8.1
- **Node.js**: 18.x LTS

### 计划集成（后续阶段）
- **aiortc**: 1.13.0 (WebRTC)
- **MuJoCo**: 机器人仿真
- **nipplejs**: 0.10.2 (虚拟摇杆)

## 故障排除

### WebSocket 连接失败
1. 确保后端服务器正在运行
2. 检查端口 8000 是否被占用
3. 确认防火墙允许本地连接

### CORS 错误
1. 确保前端运行在 http://localhost:3000
2. 检查后端 CORS 配置是否正确

### 依赖安装问题
1. 使用指定的 Python 和 Node.js 版本
2. 清理缓存后重新安装：
   ```bash
   # Python
   pip cache purge
   
   # Node.js
   npm cache clean --force
   ```

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

[项目许可证信息]