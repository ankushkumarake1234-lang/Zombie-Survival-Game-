"""
🧟 ZOMBIE SURVIVAL GAME 🧟
==========================
Ek complete aur professional zombie survival game!
Python + Pygame se bani hui game jisme waves, weapons, zombies sab kuch hai!

CONTROLS:
- W/A/S/D: Move karo player ko
- Mouse Click / SPACE: Shoot karo
- R: Restart game after game over
- ESC: Quit game
- 1: Pistol select karo
- 2: Rifle select karo

Author: Pygame Expert
"""

import pygame
import random
import math
import sys
import os

# ======================
# PYGAME INITIALIZATION
# ======================
pygame.init()
pygame.mixer.init()

# ======================
# GAME CONSTANTS
# ======================
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Colors (Professional color palette)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 200, 80)
BLUE = (50, 150, 255)
DARK_GREEN = (20, 100, 40)
DARK_RED = (150, 20, 20)
YELLOW = (255, 220, 50)
ORANGE = (255, 150, 50)
PURPLE = (150, 50, 200)
DARK_GRAY = (40, 40, 40)
GRAY = (100, 100, 100)

# Player constants
PLAYER_SIZE = 40
PLAYER_SPEED = 5
PLAYER_MAX_HEALTH = 100

# Weapon constants
PISTOL_DAMAGE = 25
PISTOL_FIRE_RATE = 300  # milliseconds
PISTOL_BULLET_SPEED = 12

RIFLE_DAMAGE = 15
RIFLE_FIRE_RATE = 100  # milliseconds - auto fire!
RIFLE_BULLET_SPEED = 15

BULLET_SIZE = 8

# Zombie constants
SLOW_ZOMBIE_SPEED = 1.5
SLOW_ZOMBIE_HEALTH = 100
SLOW_ZOMBIE_DAMAGE = 10
SLOW_ZOMBIE_SIZE = 45

FAST_ZOMBIE_SPEED = 3.5
FAST_ZOMBIE_HEALTH = 50
FAST_ZOMBIE_DAMAGE = 5
FAST_ZOMBIE_SIZE = 38

ZOMBIE_HIT_COOLDOWN = 1000  # milliseconds

# Wave constants
INITIAL_ZOMBIES = 5
WAVE_INCREMENT = 3
WAVE_BREAK_TIME = 3000  # milliseconds

# ======================
# SETUP SCREEN
# ======================
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🧟 Zombie Survival Game 🧟")
clock = pygame.time.Clock()

# ======================
# FONTS
# ======================
try:
    title_font = pygame.font.Font(None, 80)
    large_font = pygame.font.Font(None, 60)
    medium_font = pygame.font.Font(None, 40)
    small_font = pygame.font.Font(None, 30)
    tiny_font = pygame.font.Font(None, 20)
except:
    title_font = pygame.font.SysFont('Arial', 80, bold=True)
    large_font = pygame.font.SysFont('Arial', 60, bold=True)
    medium_font = pygame.font.SysFont('Arial', 40, bold=True)
    small_font = pygame.font.SysFont('Arial', 30)
    tiny_font = pygame.font.SysFont('Arial', 20)

# ======================
# SOUND SYSTEM
# ======================
class SoundManager:
    """Sound aur voice audio manage karne ke liye"""
    def __init__(self):
        self.sounds = {}
        self.voices = {}
        
        # Simple beep sounds generate karte hain (placeholder)
        # Actual game mein aap real sound files use kar sakte ho
        try:
            # Generate simple sound effects using pygame
            self.shoot_sound = pygame.mixer.Sound(buffer=self._generate_shoot_sound())
            self.zombie_hit_sound = pygame.mixer.Sound(buffer=self._generate_hit_sound())
            self.zombie_death_sound = pygame.mixer.Sound(buffer=self._generate_death_sound())
            self.player_hurt_sound = pygame.mixer.Sound(buffer=self._generate_hurt_sound())
        except:
            # Agar sound nahi bana to silent mode
            self.shoot_sound = None
            self.zombie_hit_sound = None
            self.zombie_death_sound = None
            self.player_hurt_sound = None
        
    def _generate_shoot_sound(self):
        """Shoot sound generate karo"""
        sample_rate = 22050
        duration = 0.1
        frequency = 400
        samples = int(sample_rate * duration)
        wave = [int(32767 * 0.3 * math.sin(2 * math.pi * frequency * i / sample_rate)) for i in range(samples)]
        # Fade out
        for i in range(len(wave)):
            wave[i] = int(wave[i] * (1 - i / len(wave)))
        sound_array = pygame.sndarray.make_sound(bytearray([b & 0xff for b in wave] + [(b >> 8) & 0xff for b in wave]))
        return sound_array
        
    def _generate_hit_sound(self):
        """Hit sound generate karo"""
        sample_rate = 22050
        duration = 0.15
        frequency = 200
        samples = int(sample_rate * duration)
        wave = [int(32767 * 0.2 * math.sin(2 * math.pi * frequency * i / sample_rate)) for i in range(samples)]
        sound_array = pygame.sndarray.make_sound(bytearray([b & 0xff for b in wave] + [(b >> 8) & 0xff for b in wave]))
        return sound_array
        
    def _generate_death_sound(self):
        """Death sound generate karo"""
        sample_rate = 22050
        duration = 0.3
        samples = int(sample_rate * duration)
        wave = []
        for i in range(samples):
            freq = 300 - (i / samples) * 200  # Frequency decreases
            wave.append(int(32767 * 0.2 * math.sin(2 * math.pi * freq * i / sample_rate)))
        sound_array = pygame.sndarray.make_sound(bytearray([b & 0xff for b in wave] + [(b >> 8) & 0xff for b in wave]))
        return sound_array
        
    def _generate_hurt_sound(self):
        """Player hurt sound generate karo"""
        sample_rate = 22050
        duration = 0.2
        frequency = 150
        samples = int(sample_rate * duration)
        wave = [int(32767 * 0.25 * math.sin(2 * math.pi * frequency * i / sample_rate)) for i in range(samples)]
        sound_array = pygame.sndarray.make_sound(bytearray([b & 0xff for b in wave] + [(b >> 8) & 0xff for b in wave]))
        return sound_array
    
    def play_shoot(self):
        """Shoot sound play karo"""
        if self.shoot_sound:
            self.shoot_sound.play()
    
    def play_zombie_hit(self):
        """Zombie hit sound play karo"""
        if self.zombie_hit_sound:
            self.zombie_hit_sound.play()
    
    def play_zombie_death(self):
        """Zombie death sound play karo"""
        if self.zombie_death_sound:
            self.zombie_death_sound.play()
    
    def play_player_hurt(self):
        """Player hurt sound play karo"""
        if self.player_hurt_sound:
            self.player_hurt_sound.play()

# Initialize sound manager
sound_manager = SoundManager()

# ======================
# BULLET CLASS
# ======================
class Bullet:
    """Bullet class - player ke shots ko represent karta hai"""
    def __init__(self, x, y, target_x, target_y, damage, speed):
        self.x = x
        self.y = y
        self.damage = damage
        self.speed = speed
        
        # Calculate direction towards target (mouse position)
        dx = target_x - x
        dy = target_y - y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            self.vel_x = (dx / distance) * speed
            self.vel_y = (dy / distance) * speed
        else:
            self.vel_x = 0
            self.vel_y = 0
        
        self.radius = BULLET_SIZE // 2
        
    def update(self):
        """Bullet ko move karo"""
        self.x += self.vel_x
        self.y += self.vel_y
        
    def is_off_screen(self):
        """Check karo ki bullet screen se bahar gaya kya"""
        return (self.x < 0 or self.x > SCREEN_WIDTH or 
                self.y < 0 or self.y > SCREEN_HEIGHT)
    
    def draw(self, surface):
        """Bullet ko draw karo"""
        # Glowing bullet effect
        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), self.radius + 2)
        pygame.draw.circle(surface, ORANGE, (int(self.x), int(self.y)), self.radius)

# ======================
# WEAPON CLASS
# ======================
class Weapon:
    """Weapon class - pistol ya rifle"""
    def __init__(self, weapon_type):
        self.type = weapon_type
        
        if weapon_type == "pistol":
            self.damage = PISTOL_DAMAGE
            self.fire_rate = PISTOL_FIRE_RATE
            self.bullet_speed = PISTOL_BULLET_SPEED
            self.name = "Pistol"
            self.color = BLUE
        elif weapon_type == "rifle":
            self.damage = RIFLE_DAMAGE
            self.fire_rate = RIFLE_FIRE_RATE
            self.bullet_speed = RIFLE_BULLET_SPEED
            self.name = "Rifle"
            self.color = RED
        
        self.last_shot_time = 0
        
    def can_shoot(self):
        """Check karo ki shoot kar sakte hain kya"""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.fire_rate:
            self.last_shot_time = current_time
            return True
        return False
    
    def shoot(self, x, y, target_x, target_y):
        """Bullet create karo"""
        if self.can_shoot():
            sound_manager.play_shoot()
            return Bullet(x, y, target_x, target_y, self.damage, self.bullet_speed)
        return None

# ======================
# ZOMBIE CLASS
# ======================
class Zombie:
    """Zombie class - slow ya fast zombie"""
    def __init__(self, zombie_type, spawn_edge):
        self.type = zombie_type
        
        # Spawn zombie at random position on given edge
        if spawn_edge == "top":
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y = -50
        elif spawn_edge == "bottom":
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y = SCREEN_HEIGHT + 50
        elif spawn_edge == "left":
            self.x = -50
            self.y = random.randint(0, SCREEN_HEIGHT)
        else:  # right
            self.x = SCREEN_WIDTH + 50
            self.y = random.randint(0, SCREEN_HEIGHT)
        
        if zombie_type == "slow":
            self.speed = SLOW_ZOMBIE_SPEED
            self.max_health = SLOW_ZOMBIE_HEALTH
            self.health = self.max_health
            self.damage = SLOW_ZOMBIE_DAMAGE
            self.size = SLOW_ZOMBIE_SIZE
            self.color = DARK_GREEN
            self.score_value = 10
        else:  # fast
            self.speed = FAST_ZOMBIE_SPEED
            self.max_health = FAST_ZOMBIE_HEALTH
            self.health = self.max_health
            self.damage = FAST_ZOMBIE_DAMAGE
            self.size = FAST_ZOMBIE_SIZE
            self.color = DARK_RED
            self.score_value = 20
        
        self.last_hit_time = 0
        
    def update(self, player_x, player_y):
        """Zombie ko player ki taraf move karo"""
        # Calculate direction towards player
        dx = player_x - self.x
        dy = player_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
    
    def take_damage(self, damage):
        """Zombie ko damage do"""
        self.health -= damage
        sound_manager.play_zombie_hit()
        
        if self.health <= 0:
            sound_manager.play_zombie_death()
            return True  # Zombie mar gaya
        return False
    
    def can_damage_player(self):
        """Check karo ki player ko damage de sakte hain kya"""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit_time >= ZOMBIE_HIT_COOLDOWN:
            self.last_hit_time = current_time
            return True
        return False
    
    def draw(self, surface):
        """Zombie ko draw karo"""
        # Zombie body
        if self.type == "slow":
            # Slow zombie - bigger, green
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size // 2)
            pygame.draw.circle(surface, GREEN, (int(self.x), int(self.y)), self.size // 2 - 5)
            # Eyes
            pygame.draw.circle(surface, RED, (int(self.x - 8), int(self.y - 5)), 4)
            pygame.draw.circle(surface, RED, (int(self.x + 8), int(self.y - 5)), 4)
        else:
            # Fast zombie - smaller, red
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size // 2)
            pygame.draw.circle(surface, RED, (int(self.x), int(self.y)), self.size // 2 - 5)
            # Eyes
            pygame.draw.circle(surface, YELLOW, (int(self.x - 6), int(self.y - 5)), 3)
            pygame.draw.circle(surface, YELLOW, (int(self.x + 6), int(self.y - 5)), 3)
        
        # Health bar above zombie
        health_bar_width = 40
        health_bar_height = 5
        health_percentage = self.health / self.max_health
        
        # Background (red)
        pygame.draw.rect(surface, RED, 
                        (int(self.x - health_bar_width // 2), 
                         int(self.y - self.size // 2 - 10),
                         health_bar_width, health_bar_height))
        # Health (green)
        pygame.draw.rect(surface, GREEN, 
                        (int(self.x - health_bar_width // 2), 
                         int(self.y - self.size // 2 - 10),
                         int(health_bar_width * health_percentage), health_bar_height))

# ======================
# PLAYER CLASS
# ======================
class Player:
    """Player class - main character jo user control karta hai"""
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.size = PLAYER_SIZE
        self.speed = PLAYER_SPEED
        self.max_health = PLAYER_MAX_HEALTH
        self.health = self.max_health
        
        # Weapons
        self.weapons = {
            "pistol": Weapon("pistol"),
            "rifle": Weapon("rifle")
        }
        self.current_weapon = "pistol"
        
    def move(self, keys):
        """Player ko move karo using WASD"""
        if keys[pygame.K_w] and self.y - self.size // 2 > 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.y + self.size // 2 < SCREEN_HEIGHT:
            self.y += self.speed
        if keys[pygame.K_a] and self.x - self.size // 2 > 0:
            self.x -= self.speed
        if keys[pygame.K_d] and self.x + self.size // 2 < SCREEN_WIDTH:
            self.x += self.speed
    
    def switch_weapon(self, weapon_type):
        """Weapon change karo"""
        if weapon_type in self.weapons:
            self.current_weapon = weapon_type
    
    def shoot(self, target_x, target_y):
        """Shoot karo current weapon se"""
        weapon = self.weapons[self.current_weapon]
        return weapon.shoot(self.x, self.y, target_x, target_y)
    
    def take_damage(self, damage):
        """Player ko damage do"""
        self.health -= damage
        sound_manager.play_player_hurt()
        
        if self.health < 0:
            self.health = 0
    
    def is_alive(self):
        """Check karo ki player zinda hai kya"""
        return self.health > 0
    
    def draw(self, surface):
        """Player ko draw karo"""
        # Player body (blue circle with border)
        pygame.draw.circle(surface, BLUE, (int(self.x), int(self.y)), self.size // 2)
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.size // 2 - 5)
        
        # Direction indicator (small circle in front)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > 0:
            indicator_x = self.x + (dx / distance) * (self.size // 2 + 5)
            indicator_y = self.y + (dy / distance) * (self.size // 2 + 5)
            
            weapon_color = self.weapons[self.current_weapon].color
            pygame.draw.circle(surface, weapon_color, (int(indicator_x), int(indicator_y)), 5)
        
        # Health bar above player
        health_bar_width = 60
        health_bar_height = 8
        health_percentage = self.health / self.max_health
        
        # Background (dark gray)
        pygame.draw.rect(surface, DARK_GRAY, 
                        (int(self.x - health_bar_width // 2), 
                         int(self.y - self.size // 2 - 15),
                         health_bar_width, health_bar_height))
        # Health (green to red based on health)
        if health_percentage > 0.5:
            health_color = GREEN
        elif health_percentage > 0.25:
            health_color = YELLOW
        else:
            health_color = RED
            
        pygame.draw.rect(surface, health_color, 
                        (int(self.x - health_bar_width // 2), 
                         int(self.y - self.size // 2 - 15),
                         int(health_bar_width * health_percentage), health_bar_height))

# ======================
# WAVE MANAGER CLASS
# ======================
class WaveManager:
    """Wave system manage karta hai"""
    def __init__(self):
        self.current_wave = 1
        self.zombies_in_wave = INITIAL_ZOMBIES
        self.zombies_spawned = 0
        self.zombies_killed = 0
        self.wave_active = False
        self.wave_break_timer = 0
        self.difficulty_multiplier = 1.0
        
    def start_wave(self):
        """Naya wave start karo"""
        self.wave_active = True
        self.zombies_spawned = 0
        self.zombies_killed = 0
        
        # Difficulty badhao har wave ke saath
        self.difficulty_multiplier = 1.0 + (self.current_wave - 1) * 0.15
        
    def end_wave(self):
        """Wave khatam karo"""
        self.wave_active = False
        self.wave_break_timer = pygame.time.get_ticks()
        self.current_wave += 1
        self.zombies_in_wave += WAVE_INCREMENT
        
    def is_wave_complete(self, active_zombies_count):
        """Check karo ki wave complete hui kya"""
        return (self.zombies_spawned >= self.zombies_in_wave and 
                active_zombies_count == 0)
    
    def can_start_new_wave(self):
        """Check karo ki naya wave start kar sakte hain kya"""
        if not self.wave_active:
            current_time = pygame.time.get_ticks()
            if current_time - self.wave_break_timer >= WAVE_BREAK_TIME:
                return True
        return False
    
    def get_zombie_type(self):
        """Random zombie type return karo (difficulty ke according)"""
        # Higher waves mein zyada fast zombies
        fast_zombie_chance = min(0.5, 0.2 + (self.current_wave - 1) * 0.05)
        
        if random.random() < fast_zombie_chance:
            return "fast"
        return "slow"
    
    def get_zombie_spawn_edge(self):
        """Random edge se zombie spawn karo"""
        return random.choice(["top", "bottom", "left", "right"])

# ======================
# GAME CLASS
# ======================
class Game:
    """Main game class - sab kuch manage karta hai"""
    def __init__(self):
        self.reset_game()
        
    def reset_game(self):
        """Game ko reset karo"""
        self.player = Player()
        self.bullets = []
        self.zombies = []
        self.wave_manager = WaveManager()
        self.score = 0
        self.high_score = self.load_high_score()
        self.game_state = "start"  # start, playing, wave_complete, game_over
        
    def load_high_score(self):
        """High score load karo file se"""
        try:
            if os.path.exists("high_score.txt"):
                with open("high_score.txt", "r") as f:
                    return int(f.read())
        except:
            pass
        return 0
    
    def save_high_score(self):
        """High score save karo file mein"""
        try:
            with open("high_score.txt", "w") as f:
                f.write(str(self.high_score))
        except:
            pass
    
    def update(self):
        """Game state update karo"""
        if self.game_state != "playing":
            return
        
        # Wave management
        if not self.wave_manager.wave_active:
            if self.wave_manager.can_start_new_wave():
                self.wave_manager.start_wave()
                self.game_state = "playing"
        else:
            # Spawn zombies
            if self.wave_manager.zombies_spawned < self.wave_manager.zombies_in_wave:
                # Random interval mein spawn karo
                if random.random() < 0.02:  # 2% chance har frame
                    zombie_type = self.wave_manager.get_zombie_type()
                    spawn_edge = self.wave_manager.get_zombie_spawn_edge()
                    zombie = Zombie(zombie_type, spawn_edge)
                    
                    # Apply difficulty multiplier
                    zombie.speed *= self.wave_manager.difficulty_multiplier
                    zombie.health *= self.wave_manager.difficulty_multiplier
                    zombie.max_health = zombie.health
                    
                    self.zombies.append(zombie)
                    self.wave_manager.zombies_spawned += 1
            
            # Check wave complete
            if self.wave_manager.is_wave_complete(len(self.zombies)):
                self.wave_manager.end_wave()
                self.game_state = "wave_complete"
        
        # Update player movement
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        
        # Update bullets
        for bullet in self.bullets[:]:
            bullet.update()
            
            # Remove if off screen
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
                continue
            
            # Check collision with zombies
            for zombie in self.zombies[:]:
                dx = bullet.x - zombie.x
                dy = bullet.y - zombie.y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance < zombie.size // 2:
                    # Hit!
                    if zombie.take_damage(bullet.damage):
                        # Zombie mara
                        self.zombies.remove(zombie)
                        self.score += zombie.score_value
                        
                        # Update high score
                        if self.score > self.high_score:
                            self.high_score = self.score
                    
                    # Remove bullet
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    break
        
        # Update zombies
        for zombie in self.zombies:
            zombie.update(self.player.x, self.player.y)
            
            # Check collision with player
            dx = zombie.x - self.player.x
            dy = zombie.y - self.player.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance < (zombie.size // 2 + self.player.size // 2):
                # Zombie player ko touch kar raha hai
                if zombie.can_damage_player():
                    self.player.take_damage(zombie.damage)
        
        # Check game over
        if not self.player.is_alive():
            self.game_state = "game_over"
            self.save_high_score()
    
    def handle_shoot(self, target_x, target_y):
        """Shooting handle karo"""
        if self.game_state == "playing":
            bullet = self.player.shoot(target_x, target_y)
            if bullet:
                self.bullets.append(bullet)
    
    def draw(self):
        """Sab kuch draw karo"""
        # Background
        screen.fill(DARK_GRAY)
        
        # Grid pattern for depth
        for x in range(0, SCREEN_WIDTH, 50):
            pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, 50):
            pygame.draw.line(screen, (50, 50, 50), (0, y), (SCREEN_WIDTH, y), 1)
        
        if self.game_state == "start":
            self.draw_start_screen()
        elif self.game_state == "playing":
            self.draw_game_screen()
        elif self.game_state == "wave_complete":
            self.draw_game_screen()  # Still show game
            self.draw_wave_complete_overlay()
        elif self.game_state == "game_over":
            self.draw_game_screen()  # Still show game
            self.draw_game_over_screen()
    
    def draw_start_screen(self):
        """Start screen draw karo"""
        # Title
        title_text = title_font.render("🧟 ZOMBIE SURVIVAL 🧟", True, GREEN)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        
        # Shadow effect
        shadow_text = title_font.render("🧟 ZOMBIE SURVIVAL 🧟", True, DARK_GREEN)
        shadow_rect = shadow_text.get_rect(center=(SCREEN_WIDTH // 2 + 3, 153))
        screen.blit(shadow_text, shadow_rect)
        screen.blit(title_text, title_rect)
        
        # Instructions
        instructions = [
            "CONTROLS:",
            "W/A/S/D - Move Player",
            "Mouse Click / SPACE - Shoot",
            "1 - Select Pistol",
            "2 - Select Rifle",
            "R - Restart Game",
            "ESC - Quit Game",
            "",
            "Survive the zombie waves!",
            "Kill zombies to earn points!",
            "",
            "Press SPACE to Start"
        ]
        
        y_offset = 250
        for instruction in instructions:
            if instruction.startswith("CONTROLS") or instruction.startswith("Press"):
                text = medium_font.render(instruction, True, YELLOW)
            else:
                text = small_font.render(instruction, True, WHITE)
            
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 35
        
        # High Score
        high_score_text = medium_font.render(f"High Score: {self.high_score}", True, ORANGE)
        high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(high_score_text, high_score_rect)
    
    def draw_game_screen(self):
        """Game screen draw karo"""
        # Draw bullets
        for bullet in self.bullets:
            bullet.draw(screen)
        
        # Draw zombies
        for zombie in self.zombies:
            zombie.draw(screen)
        
        # Draw player
        self.player.draw(screen)
        
        # Draw HUD
        self.draw_hud()
    
    def draw_hud(self):
        """HUD (score, wave, health) draw karo"""
        # Score
        score_text = medium_font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (20, 20))
        
        # Wave
        wave_text = medium_font.render(f"Wave: {self.wave_manager.current_wave}", True, YELLOW)
        screen.blit(wave_text, (20, 60))
        
        # Zombies remaining
        zombies_left = self.wave_manager.zombies_in_wave - self.wave_manager.zombies_spawned + len(self.zombies)
        zombie_text = small_font.render(f"Zombies: {zombies_left}", True, RED)
        screen.blit(zombie_text, (20, 100))
        
        # Health bar (bottom)
        health_bar_width = 300
        health_bar_height = 30
        health_percentage = self.player.health / self.player.max_health
        
        # Border
        pygame.draw.rect(screen, WHITE, 
                        (SCREEN_WIDTH // 2 - health_bar_width // 2 - 2, 
                         SCREEN_HEIGHT - 50 - 2,
                         health_bar_width + 4, health_bar_height + 4), 2)
        
        # Background
        pygame.draw.rect(screen, DARK_GRAY, 
                        (SCREEN_WIDTH // 2 - health_bar_width // 2, 
                         SCREEN_HEIGHT - 50,
                         health_bar_width, health_bar_height))
        
        # Health
        if health_percentage > 0.5:
            health_color = GREEN
        elif health_percentage > 0.25:
            health_color = YELLOW
        else:
            health_color = RED
            
        pygame.draw.rect(screen, health_color, 
                        (SCREEN_WIDTH // 2 - health_bar_width // 2, 
                         SCREEN_HEIGHT - 50,
                         int(health_bar_width * health_percentage), health_bar_height))
        
        # Health text
        health_text = small_font.render(f"HP: {int(self.player.health)}/{self.player.max_health}", True, WHITE)
        health_rect = health_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 35))
        screen.blit(health_text, health_rect)
        
        # Current weapon (top right)
        weapon = self.player.weapons[self.player.current_weapon]
        weapon_text = medium_font.render(f"Weapon: {weapon.name}", True, weapon.color)
        screen.blit(weapon_text, (SCREEN_WIDTH - 250, 20))
    
    def draw_wave_complete_overlay(self):
        """Wave complete overlay draw karo"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Wave complete text
        wave_text = large_font.render(f"Wave {self.wave_manager.current_wave - 1} Complete!", True, GREEN)
        wave_rect = wave_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(wave_text, wave_rect)
        
        # Next wave info
        next_text = medium_font.render(f"Next Wave: {self.wave_manager.current_wave}", True, YELLOW)
        next_rect = next_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(next_text, next_rect)
        
        # Continue prompt
        continue_text = small_font.render("Press SPACE to Continue", True, WHITE)
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
        screen.blit(continue_text, continue_rect)
    
    def draw_game_over_screen(self):
        """Game over screen draw karo"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # Game Over text
        game_over_text = title_font.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120))
        screen.blit(game_over_text, game_over_rect)
        
        # Final stats
        stats = [
            f"Final Score: {self.score}",
            f"High Score: {self.high_score}",
            f"Waves Survived: {self.wave_manager.current_wave - 1}",
            "",
            "Press R to Restart",
            "Press ESC to Quit"
        ]
        
        y_offset = SCREEN_HEIGHT // 2 - 20
        for stat in stats:
            if "High Score" in stat and self.score >= self.high_score:
                text = medium_font.render(stat, True, YELLOW)
            elif stat.startswith("Press"):
                text = small_font.render(stat, True, GREEN)
            else:
                text = medium_font.render(stat, True, WHITE)
            
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 45

# ======================
# MAIN GAME LOOP
# ======================
def main():
    """Main game loop - yahan se sab start hota hai"""
    game = Game()
    running = True
    
    # Mouse shooting ke liye
    mouse_pressed = False
    
    while running:
        clock.tick(FPS)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                # Start screen
                if game.game_state == "start":
                    if event.key == pygame.K_SPACE:
                        game.game_state = "playing"
                        game.wave_manager.start_wave()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                
                # Playing
                elif game.game_state == "playing":
                    if event.key == pygame.K_SPACE:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        game.handle_shoot(mouse_x, mouse_y)
                    elif event.key == pygame.K_1:
                        game.player.switch_weapon("pistol")
                    elif event.key == pygame.K_2:
                        game.player.switch_weapon("rifle")
                    elif event.key == pygame.K_ESCAPE:
                        game.game_state = "start"
                        game.reset_game()
                
                # Wave complete
                elif game.game_state == "wave_complete":
                    if event.key == pygame.K_SPACE:
                        game.game_state = "playing"
                
                # Game over
                elif game.game_state == "game_over":
                    if event.key == pygame.K_r:
                        game.reset_game()
                        game.game_state = "start"
                    elif event.key == pygame.K_ESCAPE:
                        running = False
            
            # Mouse shooting
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pressed = True
                    if game.game_state == "playing":
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        game.handle_shoot(mouse_x, mouse_y)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_pressed = False
        
        # Auto fire for rifle when mouse held down
        if mouse_pressed and game.game_state == "playing":
            if game.player.current_weapon == "rifle":
                mouse_x, mouse_y = pygame.mouse.get_pos()
                game.handle_shoot(mouse_x, mouse_y)
        
        # Update game
        game.update()
        
        # Draw everything
        game.draw()
        
        # Update display
        pygame.display.flip()
    
    # Cleanup
    pygame.quit()
    sys.exit()

# ======================
# GAME START
# ======================
if __name__ == "__main__":
    print("🧟 Zombie Survival Game Starting... 🧟")
    print("=" * 50)
    print("Controls:")
    print("  W/A/S/D - Move")
    print("  Mouse Click / SPACE - Shoot")
    print("  1/2 - Switch Weapons")
    print("  R - Restart")
    print("  ESC - Quit")
    print("=" * 50)
    main()
