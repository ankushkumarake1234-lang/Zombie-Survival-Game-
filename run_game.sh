#!/bin/bash
# Quick start script for Zombie Survival Game
# Yeh script automatically game run kar dega

echo "=================================="
echo "🧟 Zombie Survival Game Launcher 🧟"
echo "=================================="
echo ""
echo "Checking Python installation..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 not found!"
    echo "Please install Python from: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""
echo "Checking Pygame installation..."

# Check if pygame is installed
python3 -c "import pygame" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ Pygame found: $(python3 -c 'import pygame; print(pygame.ver)')"
else
    echo "❌ Pygame not found!"
    echo "Installing Pygame..."
    pip3 install pygame
    
    if [ $? -eq 0 ]; then
        echo "✅ Pygame installed successfully!"
    else
        echo "❌ Failed to install Pygame"
        echo "Please manually install: pip3 install pygame"
        exit 1
    fi
fi

echo ""
echo "=================================="
echo "🎮 Starting Game..."
echo "=================================="
echo ""

# Run the game
python3 zombie_survival.py

echo ""
echo "=================================="
echo "Game closed. Thanks for playing!"
echo "=================================="
