# Import necessary libraries
import pygame as pg  # For game development
import psycopg2     # For PostgreSQL database connection
import random      # For random number generation
import time       # For time-related functions
import sys       # For system-specific parameters and functions
from config import load_config  # Custom config loader
from enum import Enum, auto  # For creating enumerations

# Initialize pygame and pygame font module
pg.init()
pg.font.init()

# Game constants
SCREEN_WIDTH  = 1080  # Width of game window
SCREEN_HEIGHT = 1080  # Height of game window
FPS = 15  # Frames per second for game loop

# Database class to handle all database operations
class Database:
    def __init__(self):
        # Load database configuration
        self.config = load_config()

    def get_user(self, username):
        """Retrieve user data from database"""
        try:
            # Connect to database
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    # SQL query to get user data with their highest score
                    cur.execute("""
                        SELECT users.user_id, users.user_name, users_score.level, users_score.score
                        FROM users
                        JOIN users_score ON users.user_id = users_score.user_id
                        WHERE users.user_name = %s
                        ORDER BY users_score.score DESC
                        LIMIT 1
                      
                                """, (username,))

                    result = cur.fetchone()
                    if result:
                        # Return Player object if user exists
                        return Player(result[1], result[2], result[3])
                    
                    return None
        except Exception as error:
            print("Error getting user:", error)
            return None
        
    def create_user(self, username):
        """Create a new user in database"""
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    # Insert new user or ignore if already exists
                    cur.execute("""
                            INSERT INTO users (user_name)
                            VALUES (%s)
                            ON CONFLICT (user_name) DO NOTHING
                            RETURNING user_id
                            """, (username,))
                    
                    user_id_row = cur.fetchone()
                        
                    # If user already exists, get their ID
                    if user_id_row is None:
                        cur.execute("SELECT user_id FROM users WHERE user_name = %s", (username,))
                        user_id = cur.fetchone()[0]
                    else:
                        user_id = user_id_row[0]

                    # Insert initial score for user
                    cur.execute("""
                            INSERT INTO users_score (user_id, score, level)
                            VALUES (%s, %s, %s)
                            """, (user_id, 0, 1))

                    conn.commit()
                    # Return new Player object
                    return Player(username, 1, 0)

        except Exception as error:
                print("Error creating user:", error)
                return None

    def safe_game(self, player):
        """Save player's game progress to database"""
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    # Get user ID
                    cur.execute("SELECT user_id FROM users WHERE user_name = %s", (player.name,))
                    user_id = cur.fetchone()[0]

                    # Insert new score record
                    cur.execute("""
                            INSERT INTO users_score (user_id, score, level)
                            VALUES (%s, %s, %s)
                            """, (user_id, player.score, player.level))

                    # Commit changes
                    conn.commit()
                    return True

        except Exception as error:
                print("Error saving game:", error)
                return False

# Color definitions using pygame Color class
class Colors:
    Black  = pg.Color(0, 0, 0)
    White  = pg.Color(255, 255, 255)
    Ground = pg.Color(16, 128, 31)  # Green for game ground
    Food   = pg.Color(212, 13, 82)  # Red for regular food
    Snake  = pg.Color(0, 0, 255)    # Blue for snake
    Wall   = pg.Color(18, 61, 4)    # Dark green for walls
    SpFood = pg.Color(255, 0, 0)    # Special food color
    GreenB = pg.Color(0, 255, 0)    # Green for buttons
    RedB   = pg.Color(255, 0, 0)    # Red for buttons
    TextInput = pg.Color(200, 200, 200)  # Gray for text input

# Game states enumeration
class GameState(Enum):
    Login   = auto()  # Login screen
    Menu    = auto()  # Main menu
    Playing = auto()  # Gameplay
    Paused  = auto()  # Paused game
    Win     = auto()  # Level completed
    Lose    = auto()  # Game over

# Button rectangle definitions
class Buttons:
    FULL_SCREEN = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)  # Full screen area
    START       = pg.Rect(100, 400, 340, 60)  # Start game button
    PLAY_AGAIN  = pg.Rect(370, 540, 340, 60)  # Play again button
    SAVE_GAME   = pg.Rect(100, 400, 340, 60)  # Save game button
    LOGIN       = pg.Rect(400, 500, 200, 50)  # Login button

# Player class to store player data
class Player:
    def __init__(self, name, level=1, score=0):
        self.name  = name   # Player name
        self.level = level  # Current level
        self.score = score  # Current score

# Snake class for the snake object
class Snake:
    def __init__(self, speed=7):
        self.body_size = 20              # Size of each snake segment
        self.step      = speed           # Movement speed
        self.direction = (self.step, 0)  # Initial direction (right)
        self.score     = 0               # Current score
        self.step_grow = 2               # Speed increase when growing
        self.speed_increase_interval = 3 # Score interval for speed increase
        self.initial_position()          # Set initial position

    def initial_position(self):
        """Set snake to starting position"""
        center_x  = (SCREEN_WIDTH - self.body_size) // 2  # Center X
        center_y  = (SCREEN_HEIGHT - self.body_size) // 2  # Center Y
        self.head = pg.Rect(center_x, center_y, self.body_size, self.body_size)  # Head rectangle
        self.body = [self.head.copy(), pg.Rect(center_x - self.body_size, center_y, self.body_size, self.body_size)]  # Body segments
    
    def move(self, current_level):
        """Move the snake"""
        head_x, head_y = self.body[0].x, self.body[0].y  # Current head position
        dx, dy   = self.direction  # Direction vector
        new_head = pg.Rect(head_x + dx, head_y + dy, self.body_size, self.body_size)  # New head position

        # Check for collisions with walls or self
        if current_level.check_collision(new_head) or new_head in self.body[1:]:
            return False  # Game over

        # Move snake by adding new head and removing tail
        self.body.insert(0, new_head)
        self.body.pop()
        return True  # Move successful

    def grow(self):
        """Increase snake length and score"""
        self.body.append(self.body[-1].copy())  # Add new segment
        self.score += 1  # Increase score

        # Increase speed at intervals
        if self.score % self.speed_increase_interval == 0:
            self.step += self.step_grow

    def set_direction(self, dx, dy):
        """Change snake direction (prevent 180° turns)"""
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def draw(self, surface):
        """Draw snake on surface"""
        if len(self.body) != self.score:
            for i in range(len(self.body), self.score):
                self.body.append(self.body[-1].copy())
        for i, segment in enumerate(self.body):
            pg.draw.rect(surface, Colors.Snake, segment)

# Level class for game levels
class Level:
    def __init__(self, level_num):
        self.game_board = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)  # Full game area
        self.level_num  = level_num  # Current level number
        self.walls      = []  # Wall rectangles
        self.wall1 = [
                pg.Rect(100, 0, 15, 800),
                pg.Rect(700, 200, 15, 700),
                pg.Rect(700, 500, 300, 15),
                pg.Rect(800, 700, 280, 15),
                pg.Rect(800, 200, 280, 15),
                pg.Rect(0, 900, 715, 15),
                pg.Rect(300, 200, 415, 15)
            ]
        self.wall2 = [
                pg.Rect(100, 0, 15, 1000),
                pg.Rect(1000, 100, 15, 980),
                pg.Rect(700, 200, 15, 785),
                pg.Rect(300, 100, 15, 700),
                pg.Rect(200, 100, 815, 15),
                pg.Rect(100, 985, 800, 15)
            ]
        self.wall3 = [
                pg.Rect(0, 600, 900, 15),
                pg.Rect(100, 400, 980, 15),
                pg.Rect(114, 60, 15, 340),
                pg.Rect(114, 600, 15, 400),
                pg.Rect(314, 60, 15, 340),
                pg.Rect(314, 600, 15, 400),
                pg.Rect(514, 60, 15, 340),
                pg.Rect(514, 600, 15, 400),
                pg.Rect(714, 60, 15, 340),
                pg.Rect(714, 600, 15, 400)
            ]

        self._setup_level()  # Setup level walls

    def _setup_level(self):
        """Create walls for each level"""
        if self.level_num == 1:
            self.walls = self.wall1

        elif self.level_num == 2:
            self.walls = self.wall2

        elif self.level_num == 3:
            self.walls = self.wall3
        
    def draw(self, surface):
        """Draw level on surface"""
        pg.draw.rect(surface, Colors.Ground, self.game_board)  # Draw ground
        for wall in self.walls:  # Draw all walls
            pg.draw.rect(surface, Colors.Wall, wall)

    def check_collision(self, rect):
        """Check if rectangle collides with any wall or screen edge"""
        for wall in self.walls:
            if rect.colliderect(wall):
                return True

        return (rect.left <= 0 or rect.right >= SCREEN_WIDTH or rect.top <= 0 or rect.bottom >= SCREEN_HEIGHT)
    
    def check_collision_for_food(self, food_rect):
        """Check if food would collide with walls and Screen border"""
        if food_rect.x <= 0 or food_rect.x >= SCREEN_WIDTH or food_rect.y <= 0 or food_rect.y >= SCREEN_HEIGHT:
            return True

        for wall in self.walls:
            if wall.colliderect(food_rect): return True
 
        return False

larila = Level(1)

# Food class for regular food
class Food:
    def __init__(self, size=30):
        self.size = size  # Food size
        self.position = (0, 0)  # Food position
        self.rect = pg.Rect(0, 0, size, size)  # Food rectangle
        self.generate_new_postion()  # Set initial position

    def generate_new_postion(self, snake=None):
        """Generate valid food position"""
        if snake  is None: snake_body = []  # Default empty snake body
        else: snake_body = snake.body  # Get snake body segments

        while True:
            # Random position within screen bounds
            x = random.randint(0, (SCREEN_WIDTH - self.size) // self.size) * self.size
            y = random.randint(0, (SCREEN_HEIGHT - self.size) // self.size) * self.size
            self.rect.x = x
            self.rect.y = y

            # Check for collisions
            collision = False
            for segment in snake_body:  # Check snake collision
                if self.rect.colliderect(segment):
                    collision = True
                    break


            if not collision:
                if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.size or self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - self.size:
                    collision = True

            if not collision:
                for wall in larila.wall1 + larila.wall2 + larila.wall3:
                    if self.rect.colliderect(wall):
                        collision = True
                        break

            if not collision:  # Valid position found
                self.position = (x, y)
                return

    def draw(self, surface):
        """Draw food on surface"""
        pg.draw.rect(surface, Colors.Food, self.rect)

# Special food class (inherits from Food)
class SpecialFood(Food):
    def __init__(self):
        super().__init__(size=40)     # Larger size than regular food
        self.color  = Colors.SpFood   # Special color
        self.timer  = 0               # Timer for spawn/lifetime
        self.active = False           # Whether special food is active
        self.spawn_interval = 5 * FPS # Time between spawns (in frames)
        self.life_time = 5 * FPS      # Time active (in frames)
 
    def update(self, snake=None, levels=None):
        """Update special food timer and state"""
        if not self.active:
            self.timer += 1
            if self.timer >= self.spawn_interval:  # Time to spawn
                self.generate_new_postion(snake)
                self.active = True
                self.timer  = 0
        else:
            self.timer += 1
            if self.timer >= self.life_time:  # Time to disappear
                self.active = False
                self.timer  = 0
    
    def generate_new_postion(self, snake=None):
        """Generate valid position (override parent method)"""
        if snake  is None: snake_body = []
        else: snake_body = snake.body

        super().generate_new_postion(snake)

    def draw(self, surface):
        """Draw only if active"""
        if self.active: pg.draw.rect(surface, self.color, self.rect)

# Text input box for login
class TextInput:
    def __init__(self, x, y, width, height, font_size=32):
        self.rect  = pg.Rect(x, y, width, height)  # Input box rectangle
        self.color = Colors.TextInput              # Box color
        self.text  = ''                            # Current text
        self.font  = pg.font.SysFont('Comic Sans MS', font_size)  # Text font
        self.activate = True  # Whether input is active

    def handle_event(self, event):
        """Handle input events"""
        if event.type == pg.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)  # Activate on click
        elif event.type == pg.KEYDOWN and self.activate:
            if event.key == pg.K_RETURN:  # Enter key
                return True
            elif event.key == pg.K_BACKSPACE:  # Backspace
                self.text = self.text[:-1]
            else:  # Regular character
                self.text += event.unicode
        return False

    def draw(self, surface):
        """Draw input box and text"""
        pg.draw.rect(surface, self.color, self.rect, 2)  # Box with border
        text_surface = self.font.render(self.text, True, Colors.Black)  # Render text
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))  # Draw text

# Main game class
class Game:
    def __init__(self):
        # Initialize game window
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Snake Game")
        self.clock  = pg.time.Clock()  # For controlling frame rate
        self.db     = Database()  # Database handler
        
        # Game objects
        self.snake         = None  # Snake object
        self.current_level = None  # Current level
        self.food          = None  # Regular food
        self.special_food  = None  # Special food
        
        # Game state
        self.state      = GameState.Login  # Current game state
        self.player     = None  # Player object
        self.text_input = TextInput(400, 400, 280, 50)  # Username input
        
        # Fonts
        self.title_font  = pg.freetype.SysFont("Comic Sans MS", 80)  # Large title font
        self.button_font = pg.freetype.SysFont("Comic Sans MS", 60)  # Button font
        self.score_font  = pg.freetype.SysFont("Comic Sans MS", 40)  # Score display
        self.info_font   = pg.freetype.SysFont("Comic Sans MS", 30)  # Info text
   
    def handle_events(self):
        """Handle all pygame events"""
        for event in pg.event.get():
            if event.type == pg.QUIT:  # Window close
                return False
           
            # Login screen events
            if self.state == GameState.Login:
                if self.text_input.handle_event(event):  # Text input handling
                    self.handle_login()
                elif event.type == pg.MOUSEBUTTONDOWN and Buttons.LOGIN.collidepoint(event.pos):  # Login button
                    self.handle_login()

            # Other screen events
            elif event.type == pg.MOUSEBUTTONDOWN:  self.handle_mouse_click(event.pos)# Mouse clicks
            elif event.type == pg.KEYDOWN:          self.handle_key_press(event.key)# Keyboard presses

        return True

    def handle_login(self):
        """Process login attempt"""
        username = self.text_input.text.strip()  # Get username
        if username:
            # Try to get existing user
            self.player = self.db.get_user(username)
            if not self.player:  # Create new user if doesn't exist
                self.player = self.db.create_user(username)

            if self.player:  # If login/create successful
                self.state = GameState.Menu
                self.initialize_game()

    def handle_mouse_click(self, pos):
        """Handle mouse clicks based on game state"""
        if   self.state == GameState.Win    and Buttons.PLAY_AGAIN.collidepoint(pos) and self.player.level == 3:  self.reset_game()# Final level complete
        elif self.state == GameState.Menu   and Buttons.START.collidepoint(pos):      self.start_game()# Start game
        elif self.state == GameState.Lose   and Buttons.PLAY_AGAIN.collidepoint(pos): self.reset_game()# Game over
        elif self.state == GameState.Win    and Buttons.PLAY_AGAIN.collidepoint(pos): self.next_level()# Level complete
        elif self.state == GameState.Paused and Buttons.SAVE_GAME.collidepoint(pos):  self.save_game()# Save game
    
    def handle_key_press(self, key):
        """Handle keyboard input based on game state"""
        if self.state == GameState.Playing:  # Gameplay controls
            if key == pg.K_DOWN:   self.snake.set_direction(0, self.snake.step)# Move down
            if key == pg.K_UP:     self.snake.set_direction(0, -self.snake.step)# Move up
            if key == pg.K_LEFT:   self.snake.set_direction(-self.snake.step, 0)# Move left
            if key == pg.K_RIGHT:  self.snake.set_direction(self.snake.step, 0)# Move right
            if key == pg.K_ESCAPE: self.state = GameState.Paused# Pause game
            if key == pg.K_p:      self.state = GameState.Paused # Pause game (alternative key)
                

        # Pause menu controls
        if self.state == GameState.Paused:
            if key == pg.K_s:  # Save game
                self.player.score = self.snake.score
                self.player.level = self.current_level.level_num
                self.db.safe_game(self.player)
                self.state = GameState.Playing

    def initialize_game(self):
        """Initialize game objects based on player level"""
        initial_speed      = 7 + (self.player.level * 2 - 1) * 2  # Speed based on level
        self.snake         = Snake(initial_speed)  # Create snake
        self.current_level = Level(self.player.level)  # Create level
        self.food          = Food()  # Create regular food
        self.special_food  = SpecialFood()  # Create special food
        self.snake.score   = self.player.score  # Set initial score

    def start_game(self):
        """Start the game from menu"""
        self.state = GameState.Playing
        self.initialize_game()

    def reset_game(self):
        """Reset game to initial state"""
        if self.player.level == 3:  # Reset to level 1 if completed all levels
            self.player.level = 1
            self.player.score = 0
        self.initialize_game()
        self.state = GameState.Playing

    def next_level(self):
        """Advance to next level"""
        if self.player.level < 3:  # If not final level
            self.player.level += 1  # Increase level
            self.player.score += 1  # Bonus score
            self.player.score  = self.snake.score  # Update player score
            self.db.safe_game(self.player)  # Save progress
            self.initialize_game()  # Initialize next level
            self.state = GameState.Playing  # Start playing
        else:  # If final level completed
            self.state = GameState.Win  # Show win screen

    def save_game(self):
        """Save current game state"""
        self.player.score = self.snake.score  # Update score
        if self.db.safe_game(self.player):  # If save successful
            self.state = GameState.Menu  # Return to menu

    def update(self):
        """Update game state"""
        if self.state != GameState.Playing:  # Only update during gameplay
            return

        # Move snake and check for game over
        if not self.snake.move(self.current_level):
            self.state = GameState.Lose
            return

        # Check if snake ate regular food
        if self.snake.body[0].colliderect(self.food.rect):
            self.snake.grow()  # Grow snake
            self.food.generate_new_postion(self.snake)  # New food position

        # Check if level completed (score threshold)
        if self.snake.score >= self.player.level * 5:
            self.state = GameState.Win

        # Update special food
        self.special_food.update(self.snake)

        # Check if snake ate special food
        if (self.special_food.active and self.snake.body[0].colliderect(self.special_food.rect)):
            self.snake.grow()  # Grow snake
            self.snake.score  += 1  # Bonus score
            self.special_food.active = False  # Deactivate special food
            self.special_food.timer  = 0  # Reset timer
    
    def draw(self):
        """Draw current game state"""
        self.screen.fill(Colors.White)  # Clear screen

        # Draw appropriate screen based on game state
        if self.state == GameState.Login:   self.draw_login()
        if self.state == GameState.Menu:    self.draw_menu()
        if self.state == GameState.Playing: self.draw_game()
        if self.state == GameState.Win:     self.draw_win()
        if self.state == GameState.Lose:    self.draw_lose()
        if self.state == GameState.Paused:  self.draw_paused()

        # Draw score during gameplay and pause
        if self.state in [GameState.Playing, GameState.Paused]:
            self.draw_score()

        pg.display.flip()  # Update display
        
        # Special case for final level completion
        if self.state == GameState.Win and self.player.level == 3: pass

    def draw_login(self):
        """Draw login screen"""
        self.title_font.render_to(self.screen, (340, 270), "Enter Username", Colors.Black)
        self.text_input.draw(self.screen)  # Draw text input box
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.LOGIN)  # Draw login button
        self.button_font.render_to(self.screen, (Buttons.LOGIN.x + 50, Buttons.LOGIN.y + 10), "Login", Colors.Black)

    def draw_paused(self):
        """Draw pause screen"""
        self.title_font.render_to(self.screen, (80, 270), "PAUSED / press S to save", Colors.Black)
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.SAVE_GAME)  # Save button
        self.button_font.render_to(self.screen, (Buttons.SAVE_GAME.x + 20, Buttons.SAVE_GAME.y + 10), "Save & Play", Colors.Black)

    def draw_menu(self):
        """Draw main menu"""
        pg.draw.rect(self.screen, Colors.RedB, Buttons.FULL_SCREEN)  # Background
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.START)  # Start button
        self.button_font.render_to(self.screen, (Buttons.START.x + 20, Buttons.START.y + 10), "Start Game", Colors.Black)

        # Welcome message with player info
        info_text = f"Welcom {self.player.name}! Level: {self.player.level}, Score: {self.player.score}"
        self.info_font.render_to(self.screen, (100, 100), info_text, Colors.Black)

    def draw_win(self):
        """Draw level complete screen"""
        self.title_font.render_to(self.screen, (340, 270), "Level Complete!", Colors.Black)
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.PLAY_AGAIN)  # Continue button
        
        # Button text depends on whether it's final level
        if self.player.level < 3: text = "Next Level"
        else: text = "Play again"
        
        self.button_font.render_to(self.screen, (Buttons.PLAY_AGAIN.x + 20, Buttons.PLAY_AGAIN.y + 10), text, Colors.Black)

    def draw_game(self):
        """Draw gameplay screen"""
        self.current_level.draw(self.screen)  # Draw level
        self.snake.draw(self.screen)  # Draw snake
        self.food.draw(self.screen)  # Draw regular food
        self.special_food.draw(self.screen)  # Draw special food if active
    
    def draw_lose(self):
        """Draw game over screen"""
        self.title_font.render_to(self.screen, (340, 270), "Game Over!", Colors.Black)
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.PLAY_AGAIN)  # Play again button
        self.button_font.render_to(self.screen, (Buttons.PLAY_AGAIN.x + 20, Buttons.PLAY_AGAIN.y + 10), "Playe again", Colors.Black)

    def draw_score(self):
        """Draw score and level info"""
        self.score_font.render_to(self.screen, (20, 20), f"Score: {self.snake.score}", Colors.Black)
        self.score_font.render_to(self.screen, (900, 20), f"Level: {self.player.level}", Colors.Black)
        # Draw special food timer if active
        if self.special_food.active:
            remaining_time = (self.special_food.life_time - self.special_food.timer) // FPS
            self.score_font.render_to(self.screen, (450, 20), f"Timer: {remaining_time}", Colors.Black)

    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()  # Process events
            self.update()  # Update game state
            self.draw()  # Render screen
            self.clock.tick(FPS)  # Maintain frame rate

# Entry point
if __name__ == "__main__":
    game = Game()  # Create game instance
    game.run()  # Start game
    pg.quit()  # Clean up pygame
