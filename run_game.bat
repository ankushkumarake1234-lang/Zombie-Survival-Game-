@echo off
REM Quick start script for Zombie Survival Game (Windows)
REM Yeh script automatically game run kar dega

echo ==================================
echo 🧟 Zombie Survival Game Launcher 🧟
echo ==================================
echo.
echo Checking Python installation...

REM Check if python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found!
    echo Please install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python found
echo.
echo Checking Pygame installation...

REM Check if pygame is installed
python -c "import pygame" >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Pygame not found!
    echo Installing Pygame...
    pip install pygame
    
    if %errorlevel% neq 0 (
        echo ❌ Failed to install Pygame
        echo Please manually install: pip install pygame
        pause
        exit /b 1
    )
    echo ✅ Pygame installed successfully!
) else (
    echo ✅ Pygame found
)

echo.
echo ==================================
echo 🎮 Starting Game...
echo ==================================
echo.

REM Run the game
python zombie_survival.py

echo.
echo ==================================
echo Game closed. Thanks for playing!
echo ==================================
pause
