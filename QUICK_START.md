# 🧟 ZOMBIE SURVIVAL - QUICK START GUIDE 🧟

## ⚡ INSTANT START (1 Minute Setup!)

### 1️⃣ Install Pygame (Agar pehle se nahi hai)
```bash
pip3 install pygame
```

### 2️⃣ Run Game
```bash
python3 zombie_survival.py
```

**YA double-click karo launcher script pe:**
- **Mac/Linux**: `run_game.sh`
- **Windows**: `run_game.bat`

---

## 🎮 CONTROLS (Yaad rakho!)

| Action | Keys |
|--------|------|
| ⬆️ Move Up | **W** |
| ⬇️ Move Down | **S** |
| ⬅️ Move Left | **A** |
| ➡️ Move Right | **D** |
| 🔫 Shoot | **Mouse Click** or **SPACE** |
| 🔫 Auto-Fire (Rifle) | **Hold Mouse** |
| 1️⃣ Pistol | **1** |
| 2️⃣ Rifle | **2** |
| 🔄 Restart | **R** |
| ❌ Quit | **ESC** |

---

## 🎯 QUICK TIPS

### Weapon Strategy
- **Pistol** 🔫: High damage, slow fire → Use for **slow zombies**
- **Rifle** 🔫: Low damage, fast fire → Use for **fast zombies** & **multiple enemies**

### Survival Tips
1. **Keep Moving**: Mat ruko! Zombies fast hain
2. **Circle Pattern**: Gol gol ghumo, corners se bacho
3. **Weapon Switch**: Situation ke hisaab se weapon badlo
4. **Health Watch**: Health bar red ho toh careful!
5. **Wave Breaks**: Break ka use strategy banane ke liye karo

### Zombie Types
- 🟢 **Green (Slow)**: Slow but tanky → Careful aim!
- 🔴 **Red (Fast)**: Fast but weak → Quick shots!

---

## 🏆 SCORING

- Slow Zombie Kill = **+10 points**
- Fast Zombie Kill = **+20 points**
- High Score **auto-save** hota hai!

---

## 🌊 WAVE SYSTEM

```
Wave 1 → 5 zombies
Wave 2 → 8 zombies
Wave 3 → 11 zombies
...
```

Har wave mein:
- ⬆️ Zombie COUNT badhta hai
- ⬆️ Zombie SPEED badhti hai
- ⬆️ Zombie HEALTH badhta hai

---

## ⚙️ CUSTOMIZATION (Optional)

Game ko customize karna hai? File kholo: `zombie_survival.py`

### Player Speed Badao:
Line 37:
```python
PLAYER_SPEED = 7  # Default: 5
```

### Weapon Damage Badao:
Lines 40-41:
```python
PISTOL_DAMAGE = 30  # Default: 25
RIFLE_DAMAGE = 20   # Default: 15
```

### Screen Size Change Karo:
Lines 28-29:
```python
SCREEN_WIDTH = 1200   # Default: 1000
SCREEN_HEIGHT = 800   # Default: 700
```

---

## 🐛 TROUBLESHOOTING

### "ModuleNotFoundError: No module named 'pygame'"
```bash
pip3 install pygame
```

### Game slow hai?
- Close other programs
- Screen size reduce karo (code mein)

### Sound nahi aa raha?
- Check speakers
- Volume badao
- Game default sounds use karta hai (procedurally generated)

---

## 📊 GAME STATS

After game over, tumhe milega:
- 🎯 Final Score
- 🏆 High Score
- 🌊 Waves Survived
- 🔄 Restart Option

---

## 🎓 BEGINNER TIPS

### First Time Playing?
1. **Start slow**: Pehle pistol se practice karo
2. **Learn patterns**: Zombie movement pattern samjho
3. **Don't panic**: Calm raho, aim carefully
4. **Use breaks**: Wave breaks mein next wave plan karo
5. **Experiment**: Dono weapons try karo

### Getting Better?
1. **Master kiting**: Moving + shooting simultaneously
2. **Weapon switching**: Quick weapon change practice karo
3. **Damage optimize**: Right weapon for right zombie
4. **High waves**: Wave 10+ jana aim rakho
5. **High score**: Personal best break karo!

---

## 🎮 GAME MODES

Currently available:
- ✅ **Endless Survival**: Jitne waves survive kar sako!

Future updates (optional to add):
- 🚧 Boss Waves
- 🚧 Power-ups
- 🚧 Multiple Maps
- 🚧 Multiplayer

---

## 📱 SHARE YOUR SCORE!

Game khel ke apna high score share karo!

Screenshot lo aur friends ko challenge do! 🏆

---

## 💡 DID YOU KNOW?

- Game **60 FPS** pe chalti hai for smooth experience
- Zombies ke **different colors** different types ko represent karte hain
- **Health bars** color change hote hain damage ke hisaab se
- **High score** automatically `high_score.txt` mein save hota hai
- Game **100% Python** mein banai gayi hai!

---

## ✨ ENJOY THE GAME!

```
🧟 KILL ZOMBIES → SURVIVE WAVES → BEAT HIGH SCORE 🧟
```

**Ab game khelo aur maza karo! Good luck, survivor! 🔫**

---

*Pro tip: Rifle ke saath mouse hold kar ke auto-fire mode mein jao! 🔥*
