#!/bin/bash

# XLeRobot ManiSkill Host Startup Script
# This script starts the ManiSkill simulation with remote control capability

echo "🎯 Starting XLeRobot ManiSkill Host..."
echo "📍 Make sure you have ManiSkill and all dependencies installed"
echo ""

# Check if we're in the right directory
if [ ! -f "simulation/Maniskill/run_xlerobot_sim_host.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    echo "   Current directory: $(pwd)"
    echo "   Expected file: simulation/Maniskill/run_xlerobot_sim_host.py"
    exit 1
fi

# Add current directory to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/simulation/Maniskill"

echo "🚀 Starting ManiSkill Host..."
echo "   - Simulation will run on main thread (OpenGL safe)"
echo "   - Remote control listening on ports 5555/5556"
echo "   - Press Ctrl+C to stop"
echo ""

# Start the host
python simulation/Maniskill/run_xlerobot_sim_host.py

echo "✅ ManiSkill Host stopped"