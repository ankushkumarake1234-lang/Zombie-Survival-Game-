# 🧟 Zombie Survival Game 🧟

Ek **COMPLETE aur PROFESSIONAL** 2D Zombie Survival Game using Python aur Pygame!

![Game Status](https://img.shields.io/badge/status-fully%20functional-brightgreen)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Pygame](https://img.shields.io/badge/pygame-2.0%2B-orange)

---

## 🎮 Game Features

### ✅ Core Gameplay
- **Player System**: WASD se movement, screen ke andar rehna padega
- **Multiple Weapons**: 
  - 🔫 **Pistol**: Single shot, zyada damage
  - 🔫 **Rifle**: Auto fire (mouse hold karo), kam damage but fast
- **Shooting System**: Mouse click ya SPACE se shoot karo
- **Smooth Controls**: 60 FPS smooth gameplay

### 🧟 Zombie AI
- **Two Zombie Types**:
  - **Slow Zombie** (Green): Slow but high health & damage
  - **Fast Zombie** (Red): Fast but low health & damage
- **Smart AI**: Zombies humesha player ko follow karte hain
- **Spawn System**: Map edges se zombies spawn hote hain
- **Collision Detection**: Zombies player ko touch kar ke damage dete hain

### 🌊 Wave System
- **Progressive Difficulty**: Har wave mein zyada zombies aate hain
- **Wave Breaks**: Har wave ke beech mein 3 second break
- **Difficulty Scaling**: 
  - Zombie count badhta hai
  - Zombie speed badhti hai
  - Zombie health badhta hai
- **Wave Complete Screen**: Congratulations screen with next wave info

### ❤️ Health & Damage
- **Player Health Bar**: Screen pe visible (green → yellow → red)
- **Zombie Health Bars**: Har zombie ke upar health bar
- **Damage System**: Realistic damage calculation
- **Game Over**: Health 0 hone pe game over

### 🎯 Score System
- **Kill Points**: 
  - Slow Zombie = 10 points
  - Fast Zombie = 20 points
- **High Score**: Automatically save hota hai local file mein
- **Live Score Display**: Game screen pe score dikhta hai

### 🔊 Sound Effects
- **Shoot Sound**: Har shot pe sound
- **Zombie Hit**: Bullet hit hone pe sound
- **Zombie Death**: Zombie marne pe sound
- **Player Hurt**: Player ko damage lagne pe sound
- **Generated Sounds**: Pygame se procedurally generated beep sounds

### 🎨 Graphics & UI
- **Colorful Sprites**: 
  - Blue player with direction indicator
  - Green slow zombies with red eyes
  - Red fast zombies with yellow eyes
  - Glowing yellow-orange bullets
- **Multiple Screens**:
  - 🎯 **Start Screen**: Instructions and controls
  - 🎮 **Game Screen**: Actual gameplay
  - 🎊 **Wave Complete**: Celebration screen
  - 💀 **Game Over**: Final stats and restart option
- **Professional HUD**: Score, wave number, health, weapon info
- **Health Bars**: Player aur zombies ke liye color-coded health bars
- **Grid Background**: Depth effect ke liye

### 🎮 Controls
| Key | Action |
|-----|--------|
| **W/A/S/D** | Player movement |
| **Mouse Click** | Shoot (hold for rifle auto-fire) |
| **SPACE** | Shoot / Start game / Continue |
| **1** | Select Pistol |
| **2** | Select Rifle |
| **R** | Restart game |
| **ESC** | Quit game / Return to menu |

---

## 📁 Folder Structure

```
Zombie Survival Game 🧟/
│
├── zombie_survival.py          # Main game file (RUN THIS!)
├── README.md                    # Yeh file
├── high_score.txt               # High score (automatically created)
│
├── images/                      # Image assets (optional)
│   ├── player.png
│   ├── zombie_slow.png
│   ├── zombie_fast.png
│   ├── bullet.png
│   └── background.png
│
└── sounds/                      # Sound assets (optional)
    ├── shoot.wav
    ├── zombie_hit.wav
    ├── zombie_death.wav
    └── player_hurt.wav
```

**Note**: Game currently uses colored shapes (circles, rectangles) which look great! Agar aap custom images/sounds add karna chahte ho, toh `images/` aur `sounds/` folders mein daal do.

---

## 🚀 Installation & Setup

### Step 1: Python Install Karo
Python 3.7 ya usse upar hona chahiye.

**Check karo ki Python installed hai:**
```bash
python3 --version
```

Agar nahi hai, toh download karo: [python.org](https://www.python.org/downloads/)

### Step 2: Pygame Install Karo
Terminal/Command Prompt mein ye command run karo:

```bash
pip3 install pygame
```

**Mac users ke liye:**
```bash
python3 -m pip install pygame
```

**Windows users ke liye:**
```bash
pip install pygame
```

**Linux users ke liye:**
```bash
sudo apt-get install python3-pygame
# ya
pip3 install pygame
```

### Step 3: Verify Installation
Check karo ki pygame sahi se install hua:
```bash
python3 -c "import pygame; print(pygame.ver)"
```

---

## ▶️ How to Run the Game

### Quick Start (sabse aasan tarika!)

**Terminal kholo aur game folder mein jao:**
```bash
cd "/Users/ankushkumar/Desktop/Game/Zombie Survival Game 🧟"
```

**Game run karo:**
```bash
python3 zombie_survival.py
```

### Alternative Methods

**Method 1: Direct run**
```bash
python3 zombie_survival.py
```

**Method 2: Make executable (Mac/Linux)**
```bash
chmod +x zombie_survival.py
./zombie_survival.py
```

**Method 3: Double-click (Windows)**
- File explorer mein jao
- `zombie_survival.py` pe right-click karo
- "Open with Python" select karo

---

## 🎯 Gameplay Tips

1. **Weapon Selection**:
   - Pistol: Slow firing but high damage → Slow zombies ke liye best
   - Rifle: Fast auto-fire but low damage → Fast zombies ke liye best

2. **Movement Strategy**:
   - Zombies se door bhago
   - Corners mein mat phasho
   - Circle pattern mein ghumo

3. **Wave Management**:
   - First waves mein pistol use karo (ammo bachao)
   - Later waves mein rifle preferable hai
   - Wave breaks ka use health plan karne ke liye karo

4. **Zombie Types**:
   - **Green (Slow)**: Carefully aim karke shoot karo
   - **Red (Fast)**: Quick shots, mat socho bas shoot karo!

5. **Survival**:
   - Keep moving! Kabhi ruko mat
   - Health bar dekh ke planning karo
   - High waves mein kiting strategy use karo

---

## 🐛 Troubleshooting

### Problem: Pygame import nahi ho raha
**Solution:**
```bash
pip3 install --upgrade pygame
```

### Problem: Sound nahi aa raha
**Solution:**
- Check karo ki speakers on hain
- Game procedurally generated sounds use karta hai, koi audio file required nahi

### Problem: Game slow chal raha hai
**Solution:**
- Unnecessary programs band karo
- FPS constant 60 pe set hai game mein
- Python ki latest version use karo

### Problem: `ModuleNotFoundError: No module named 'pygame'`
**Solution:**
```bash
# Python version check karo
python3 --version

# Sahi Python ke saath pygame install karo
python3 -m pip install pygame
```

### Problem: Black screen aa raha hai
**Solution:**
- Graphics driver update karo
- Full screen mode try karo (code mein modify kar sakte ho)

---

## 🎨 Customization Options

### Change Screen Size
`zombie_survival.py` mein lines 28-29:
```python
SCREEN_WIDTH = 1200  # Default: 1000
SCREEN_HEIGHT = 800  # Default: 700
```

### Change Player Speed
Line 37:
```python
PLAYER_SPEED = 7  # Default: 5 (Higher = faster)
```

### Change Weapon Damage
Lines 40-47:
```python
PISTOL_DAMAGE = 30  # Default: 25
RIFLE_DAMAGE = 20   # Default: 15
```

### Change Initial Zombies
Line 65:
```python
INITIAL_ZOMBIES = 10  # Default: 5
```

### Add Your Own Images
1. `images/` folder mein apni images dalo
2. Code mein `pygame.image.load("images/player.png")` use karo
3. Current colored shapes ke jagah use karo

---

## 📊 Code Structure

### Main Classes
1. **`Player`**: Player movement, shooting, health management
2. **`Zombie`**: AI, movement, different types (slow/fast)
3. **`Weapon`**: Pistol aur Rifle with fire rate control
4. **`Bullet`**: Projectile movement and collision
5. **`WaveManager`**: Wave spawning, difficulty scaling
6. **`Game`**: Complete game state management
7. **`SoundManager`**: Sound effects generation and playback

### Key Functions
- `main()`: Main game loop
- `update()`: Game logic update har frame
- `draw()`: Rendering sab kuch screen pe
- `handle_shoot()`: Shooting mechanics
- `check_collision()`: Built into update logic

---

## 🔧 System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 7+, macOS 10.12+, Linux (any modern distro) |
| **Python** | 3.7 or higher |
| **Pygame** | 2.0 or higher |
| **RAM** | 512 MB minimum |
| **Storage** | 50 MB |
| **Display** | 1024x768 minimum resolution |

---

## 📝 Game Mechanics Explained

### Zombie Spawning
- Zombies map ke edges (top, bottom, left, right) se spawn hote hain
- Random intervals pe spawn hote hain
- Har wave mein zyada zombies spawn hote hain

### Difficulty Scaling
```
Wave 1: 5 zombies, 1.0x speed/health
Wave 2: 8 zombies, 1.15x speed/health
Wave 3: 11 zombies, 1.30x speed/health
...and so on
```

### Damage Calculation
- Pistol: 25 damage per shot
- Rifle: 15 damage per shot
- Slow Zombie: 10 damage per hit
- Fast Zombie: 5 damage per hit

### Score Calculation
- Slow Zombie kill = +10 points
- Fast Zombie kill = +20 points
- High score automatically file mein save hota hai

---

## 🌟 Features Checklist

- ✅ Player movement (WASD)
- ✅ Boundary collision (player screen ke andar)
- ✅ Multiple weapons (Pistol + Rifle)
- ✅ Shooting system (Mouse + SPACE)
- ✅ Auto-fire rifle
- ✅ Bullet system with speed
- ✅ Two zombie types (Slow + Fast)
- ✅ Zombie AI (chase player)
- ✅ Zombie spawning at edges
- ✅ Wave system with breaks
- ✅ Progressive difficulty
- ✅ Health system (Player + Zombies)
- ✅ Health bars (visible)
- ✅ Damage system
- ✅ Score tracking
- ✅ High score saving
- ✅ Sound effects (procedurally generated)
- ✅ Graphics (colored shapes)
- ✅ Start screen
- ✅ Game screen
- ✅ Wave complete screen
- ✅ Game over screen
- ✅ Smooth 60 FPS
- ✅ Professional HUD
- ✅ Clean code structure
- ✅ Well commented (Hinglish)
- ✅ Beginner-friendly

**Result: 100% COMPLETE! 🎉**

---

## 🎓 Code Learning Points

### For Beginners:
1. **Classes**: Har entity (Player, Zombie, Bullet) ek class hai
2. **Game Loop**: `while running:` infinite loop game chalata hai
3. **Event Handling**: Keyboard/mouse input capture karna
4. **Collision Detection**: Distance formula use karke
5. **State Management**: Different game states handle karna

### Advanced Concepts:
1. **Vector Math**: Direction calculation using dx/dy
2. **Difficulty Scaling**: Multiplier system
3. **Sound Generation**: Procedural audio using wave synthesis
4. **Object-Oriented Design**: Proper class hierarchy
5. **Frame-Independent Logic**: Using `clock.tick(FPS)`

---

## 🤝 Credits

- **Game Engine**: Pygame
- **Language**: Python 3
- **Author**: Expert Python Game Developer
- **Style**: Clean, Professional, Beginner-Friendly
- **Comments**: Simple Hinglish for easy understanding

---

## 📞 Support

### Agar koi problem aaye:

1. **Pygame install issues**: 
   ```bash
   pip3 install --upgrade pygame
   ```

2. **Python version issues**:
   - Python 3.7+ chahiye
   - Check: `python3 --version`

3. **Game not starting**:
   - Check terminal for error messages
   - Make sure aap sahi folder mein ho

4. **Performance issues**:
   - Close other programs
   - Reduce SCREEN_WIDTH and SCREEN_HEIGHT

---

## 🎮 Enjoy the Game!

**Game ko open karo aur enjoy karo! Zombies ko maro aur high score banao! 🧟‍♂️🔫**

```
████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝
   ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
```

**Happy Gaming! 🎉🧟🔫**

---

*Made with ❤️ using Python & Pygame*
