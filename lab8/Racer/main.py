import pygame as pg  # Importing pygame library
import sys, random, time  # Importing required modules
from pygame.locals import *  # Importing all constants from pygame.locals

# Initialize pygame and font module
pg.init()
pg.font.init()

# Game settings
FPS = 60  # Frames per second
FramePerSecond = pg.time.Clock()  # Clock object to control FPS
pg.mixer.Sound("Assets/background.wav").play(-1)  # Play background sound in a loop

# Define colors using RGB format
Color = {
    "white" : (255, 255, 255),
    "black" : (0, 0, 0),
    "blue"  : (0, 0, 255),
    "green" : (0, 255, 0),
    "red"   : (255, 0, 0),
    "yellow": (255, 255, 85)
}

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))  # Create game window
screen.fill(Color["white"])  # Fill screen with white color
pg.display.set_caption("Game")  # Set window title

running = True  # Variable to control game loop

# Load fonts
font = pg.font.SysFont("Verdena", 60)  # Main font for "Game Over"
sfont = pg.font.SysFont("Verdena", 40)  # Smaller font for score display

# Render game over text
game_over = font.render("Game Over", True, Color["black"])

# Load background image
backgraund = pg.image.load("Assets/AnimatedStreet.png")

# Initialize game variables
Score  = 0  # Score for avoiding enemies
Espeed = 5  # Speed of falling objects (enemy, coin)
Coin_score = 0  # Score for collecting coins

# Enemy car class
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Assets/Enemy.png")  # Load enemy image
        self.rect  = self.image.get_rect()  # Get rectangular bounds of enemy
        self.rect.center = (random.randint(40, WIDTH - 40), 0)  # Random starting position

    def move(self):
        self.rect.move_ip(0, Espeed)  # Move enemy downward

        # If enemy moves out of the screen, reset position and increase score
        if self.rect.bottom > HEIGHT:
            global Score
            Score += 1  # Increase score when enemy passes
            self.rect.top = 0  # Reset enemy to top
            self.rect.center = (random.randint(30, 370), 0)  # Randomize X position

# Player car class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Assets/Player.png")  # Load player image
        self.rect  = self.image.get_rect()  # Get rectangular bounds of player
        self.rect.center = (160, 520)  # Set initial position

    def move(self):
        pressed_K = pg.key.get_pressed()  # Get pressed keys

        # Move left if left arrow key is pressed and player is within bounds
        if self.rect.left > 0:
            if pressed_K[K_LEFT]: 
                self.rect.move_ip(-5, 0)
        
        # Move right if right arrow key is pressed and player is within bounds
        if self.rect.right < WIDTH:
            if pressed_K[K_RIGHT]: 
                self.rect.move_ip(5, 0)

# Coin class
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create transparent surface to draw a circle
        self.image = pg.Surface((30, 30), pg.SRCALPHA)  
        pg.draw.circle(self.image, Color["yellow"], (15, 15), 15)  # Draw yellow circle

        self.rect = self.image.get_rect()  # Get rectangular bounds of coin
        self.rect.center = (random.randint(30, WIDTH - 30), 0)  # Random starting position

    def move(self):
        global Coin_score
        self.rect.move_ip(0, Espeed)  # Move coin downward
        
        # If player collects the coin
        if self.rect.colliderect(P.rect):
            Coin_score += 1  # Increase coin score
            self.respawn()  # Respawn coin

        # If coin moves out of screen, respawn it
        if self.rect.top > HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.top = 0  # Reset coin position to top
        self.rect.center = (random.randint(30, WIDTH - 30), 0)  # Randomize X position

# Create game objects
P = Player()  # Player object
E = Enemy()  # Enemy object
C = Coin()  # Coin object

# Create sprite groups
enemies = pg.sprite.Group()  # Group for enemy sprites
enemies.add(E)  

all_sprites = pg.sprite.Group()  # Group for all game objects
all_sprites.add(P)  # Add player to group
all_sprites.add(E)  # Add enemy to group
all_sprites.add(C)  # Add coin to group

# Event to increase speed over time
INC_SPEED = pg.USEREVENT + 1  
pg.time.set_timer(INC_SPEED, 1000)  # Trigger event every 1 second

# Main game loop
while running:
    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:  # If player closes window
            running = False
        if event.type == INC_SPEED:  # Increase speed over time
            Espeed += 1

    pg.display.update()  # Update display

    screen.fill(Color["white"])  # Clear screen
    
    screen.blit(backgraund, (0,0))  # Draw background image

    # Display score on screen
    score_counter = sfont.render(str(Score), True, Color["black"])
    Coin_score_count = sfont.render("coin : " + str(Coin_score), True, Color["black"])
    screen.blit(Coin_score_count, (290, 10))  # Draw coin score
    screen.blit(score_counter, (10, 10))  # Draw enemy dodge score
    
    # Move and draw all game objects
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)  # Draw each object
        entity.move()  # Move each object

    # Check collision between player and enemy
    if pg.sprite.spritecollideany(P, enemies):
        pg.mixer.Sound("Assets/crash.wav").play()  # Play crash sound
        time.sleep(0.5)  # Pause game briefly

        # Show "Game Over" screen
        screen.fill(Color["red"])
        screen.blit(game_over, (30, 250))

        pg.display.update()  # Refresh screen
        for entity in all_sprites:
            entity.kill()  # Remove all objects
        
        time.sleep(2)  # Pause before exiting
        pg.quit()  # Quit pygame
        sys.exit()  # Exit program
    
    pg.display.update()  # Update display
    FramePerSecond.tick(FPS)  # Maintain FPS

