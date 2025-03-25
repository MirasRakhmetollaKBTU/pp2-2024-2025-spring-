import pygame as pg
import random
import math

# Initialize Pygame and font modules
pg.init()
pg.font.init()
# Set the window title
pg.display.set_caption("Snake Game")
# Define screen dimensions | Warniing, it was tested One 3840x2610 display monitor, so game may be out of your device 
Width  = 1080
Height = 1080
# Define color palette as RGB tuples
Color  = [
    (0, 0, 0), #black
    (255, 255, 255), #White
    (16, 128, 31), #ground
    (212, 13, 82), #point
    (0, 0, 240), #Snake
    (0, 0, 255), #Snake_Head
    (18, 61, 4) #Wall
]


# Create clock object for controlling frame rate
clock = pg.time.Clock()
# Game over flag
game_s_lose = False

# Define button rectangles for UI
But = [
    pg.Rect(0, 0, Width, Height),    # Full screen rectangle
    pg.Rect(100, 400, 340, 60),      # Start game button
    pg.Rect(370, 540, 340, 60)       # Play again button
]

# Base class for game state screens
class GameState:
    def __init__(self, title_text, button_text=None):
        # Initialize fonts for title and buttons
        self.my_font = pg.freetype.SysFont("Comic Sans MS", 80)
        self.my_font2 = pg.freetype.SysFont("Comic Sans MS", 60)
        self.title_text = title_text      # Title text to display
        self.button_text = button_text    # Button text if applicable

    # Draw the game state screen
    def draw(self):
        screen.fill(Color[1])  # Fill with white background
        pg.draw.rect(screen, (255, 0, 0), But[0])  # Draw full screen red rectangle
        if self.button_text:
            pg.draw.rect(screen, (0, 255, 0), But[2])  # Draw green button
            self.my_font2.render_to(screen, (380, 540), self.button_text, Color[0])  # Render button text
        self.my_font.render_to(screen, (340, 270), self.title_text, Color[0])  # Render title text

# Welcome screen class inheriting from GameState
class Game_Welcom(GameState):
    def __init__(self):
        super().__init__("", "Start game")  # Initialize with empty title and start button
        self.my_font = pg.freetype.SysFont("Comic Sans MS", 60)  # Override font size
    
    # Custom draw method for welcome screen
    def draw(self):
        screen.fill(Color[1])  # White background
        pg.draw.rect(screen, (255, 0, 0), But[0])  # Red full screen rectangle
        pg.draw.rect(screen, (0, 255, 0), But[1])  # Green start button
        self.my_font.render_to(screen, (100, 400), "Start game", Color[0])  # Start game text

# Win screen class
class WIN(GameState):
    def __init__(self):
        super().__init__("YOU WIN!", "Play Again")  # Initialize with win message and play again button

# Lose screen class
class LOSE(GameState):
    def __init__(self):
        screen.fill((0,0,0))  # Fill screen with black (only on init)
        super().__init__("YOU Lose!", "Play Again")  # Initialize with lose message and play again button

# Food class for snake to eat
class Food:
    def __init__(self):
        self.size = 30  # Food square size
        self.position = self.generate_pos(snake, current_lvl)  # Initial position

    # Generate random food position that doesn't collide with snake or walls
    def generate_pos(self, snake, level):
        while True:
            x = random.randint(0, (Width - self.size) // self.size) * self.size  # Random x position
            y = random.randint(0, (Height - self.size) // self.size) * self.size  # Random y position
            rect = pg.Rect(x, y, self.size, self.size)  # Create food rectangle
            # Check for no collisions with snake or walls
            if not any(segment.colliderect(rect) for segment in snake.Full_Body) and not lvl1.check_collision_for_food(rect) and not lvl2.check_collision_for_food(rect) and not lvl3.check_collision_for_food(rect):
                return x, y

    # Draw food on screen
    def draw(self):
        pg.draw.rect(screen, Color[3], (self.position[0], self.position[1], self.size, self.size))

class Special_Food:
    def __init__(self):
        self.size = 40
        self.position = self.generate_pos(snake, current_lvl)

    def generate_pos(self, snake, level):
        while True:
            x = random.randint(0, (Width - self.size) // self.size) * self.size
            y = random.randint(0, (Height - self.size) // self.size) * self.size
            rect = pg.Rect(x, y, self.size, self.size)

            if not any(segment.colliderect(rect) for segment in snake.Full_Body) and not lvl1.check_collision_for_food(rect) and not lvl2.check_collision_for_food(rect) and not lvl3.check_collision_for_food(rect):
                return x, y

    def draw(self):
        pg.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], self.size, self.size))
# Snake class handling movement and behavior
class Snake:
    body_size = 20  # Size of snake segments
    step = 7       # Movement speed
    def __init__(self):
        cord_X = (Width - self.body_size) // 2   # Center x position
        cord_Y = (Height - self.body_size) // 2  # Center y position
        self.Head = pg.Rect(cord_X, cord_Y, self.body_size, self.body_size)  # Head segment
        self.Body = pg.Rect(cord_X - self.body_size, cord_Y, self.body_size, self.body_size)  # Initial body segment
        self.direction = (self.step, 0)  # Initial movement right
        self.Full_Body = [self.Head, self.Body]  # List of all segments
        self.step_grow = 10  # Speed increase increment
        self.score = 0      # Player score

    # Draw snake segments
    def draw_snake(self):
        for snake in self.Full_Body:
            if snake == self.Full_Body[0]: pg.draw.rect(screen, Color[4], snake)  # Draw head
            else: pg.draw.rect(screen, Color[5], snake)  # Draw body
    
    # Move snake in current direction
    def move(self, level):
        global game_s_lose  
        head_x, head_y = self.Full_Body[0].x, self.Full_Body[0].y  # Current head position
        dx, dy = self.direction  # Movement direction
        new_head = pg.Rect(head_x + dx, head_y + dy, self.body_size, self.body_size)  # New head position
        # Check for collisions
        if level.check_collision(new_head) or new_head in self.Full_Body:
            game_s_lose = True  # Set game over flag
            return
        self.Full_Body.insert(0, new_head)  # Add new head
        self.Full_Body.pop()  # Remove tail
   
    # Increase snake length when eating food
    def grow(self):
        self.Full_Body.append(self.Full_Body[-1].copy())  # Add new segment
        self.score += 1  # Increment score
        if self.score % 3 == 0: 
            self.step += self.step_grow  # Increase speed every 3 points

    # Set new direction if not opposite to current
    def set_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

# Base level class for game boards
class Level:
    def __init__(self):
        self.game_board = pg.Rect(0, 0, Width, Height)  # Full screen game area
        self.walls = []  # List of wall rectangles
    
    # Draw game board and walls
    def draw_game_board(self):
        pg.draw.rect(screen, Color[2], self.game_board)  # Draw ground
        for wall in self.walls:
            pg.draw.rect(screen, Color[6], wall)  # Draw walls

    # Check if snake head collides with walls or borders
    def check_collision(self, snake_head):
        for wall in self.walls:
            if snake_head.colliderect(wall):
                status = -1  # Unused assignment
                pg.time.wait(1000)  # Delay on wall collision
                return True
        if (
            snake_head.left <= 0 or 
            snake_head.right >= Width or 
            snake_head.top <= 0 or 
            snake_head.bottom >= Height
        ):
            status = -1  # Unused assignment
            pg.time.wait(3000)  # Delay on border collision
            return True
        return False

    # Check if food rectangle collides with walls
    def check_collision_for_food(self, food_rect):   
        for wall in self.walls:
            if food_rect.colliderect(wall):
                return True
        return False  

# Level 1 with specific wall layout
class Level1(Level):
    def __init__(self):
        super().__init__()
        self.walls = [
            pg.Rect(100, 0, 15, 800),  
            pg.Rect(700, 200, 15, 700),  
            pg.Rect(700, 500, 300, 15),  
            pg.Rect(800, 700, 280, 15), 
            pg.Rect(800, 200, 280, 15),
            pg.Rect(0, 900, 715, 15), 
            pg.Rect(300, 200, 415, 15)
        ]

# Level 2 with different wall layout
class Level2(Level):
    def __init__(self):
        super().__init__()
        self.walls = [
            pg.Rect(100, 0, 15, 1000), 
            pg.Rect(1000, 100, 15, 980), 
            pg.Rect(700, 200, 15, 785),  
            pg.Rect(300, 100, 15, 700),  
            pg.Rect(200, 100, 815, 15),  
            pg.Rect(100, 985, 800, 15)   
        ]

# Level 3 with vertical pillars
class Level3(Level):
    def __init__(self):
        super().__init__()
        self.walls = [
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

# Create game window
screen = pg.display.set_mode((Width, Height))
gm_run = True  # Main game loop flag
game_start = False  # Game started flag
FPS = 15  # Frames per second

# Initialize game objects
snake = Snake()
lvl1  = Level1()
lvl2  = Level2()
lvl3  = Level3()
lose  = LOSE()
welcome = Game_Welcom()
status  = 0  # Game status: 0=menu, 1-3=levels, 4=win, -1=lose
You_win = WIN()
welcome.draw()  # Draw initial welcome screen
score_font = pg.freetype.SysFont("Comic Sans MS", 40)  # Score display font
current_lvl = lvl1  # Initial level
food = Food()  # Initial food object
food.draw()    # Draw initial food
quantity_food = 1  # Unused variable
Special_Food_timer = 75 * 15
special_f = Special_Food()
special_f.draw()

# Main game loop
while gm_run:
    screen.fill(Color[1])  # Clear screen with white
    clock.tick(FPS)  # Control frame rate

    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gm_run = False  # Exit game on window close
        
        if event.type == pg.MOUSEBUTTONDOWN:
            mous_x, mous_y = event.pos
            print(event)  # Debug print mouse event
            if But[1].collidepoint(mous_x, mous_y):  # Start button clicked
                game_start = True
                status = 1
            if But[2].collidepoint(mous_x, mous_y) and game_s_lose:  # Play again after losing
                game_s_lose = False
                status = 1
                snake = Snake()  
                food = Food()    
                current_lvl = lvl1  
            if But[2].collidepoint(mous_x, mous_y) and not game_s_lose:  # Restart from win screen
                status = 1
                snake = Snake()
                food = Food()
                current_lvl = lvl1

        if event.type == pg.KEYDOWN:
            print(event)  # Debug print key event
            if status != -1:  # Only process if not lost
                if event.key == pg.K_DOWN:  snake.set_direction(0, snake.step)  # Move down
                if event.key == pg.K_UP:    snake.set_direction(0, -snake.step)  # Move up
                if event.key == pg.K_LEFT:  snake.set_direction(-snake.step, 0)  # Move left
                if event.key == pg.K_RIGHT: snake.set_direction(snake.step, 0)    # Move right
    
    # Game logic when started and not lost
    if game_start and not game_s_lose:
        if status == 1: lvl1.draw_game_board()  # Draw level 1
        if status == 2: lvl2.draw_game_board()  # Draw level 2
        if status == 3: lvl3.draw_game_board()  # Draw level 3
        if status == 4: You_win.draw()         # Draw win screen

        if status != 4 and status != -1: 
            snake.move(current_lvl)  # Move snake
            # Check if snake eats food
            if snake.Full_Body[0].colliderect(pg.Rect(food.position[0], food.position[1], food.size, food.size)):            
                snake.grow()  # Grow snake
                food = Food()  # Spawn new food

            if snake.Full_Body[0].colliderect(pg.Rect(special_f.position[0], special_f.position[1], special_f.size, special_f.size)):            
                snake.grow()  # Grow snake
                snake.score += 1
                special_f = Special_Food()
                Special_Food_timer = 75 * 15

            if Special_Food_timer == 0:
                special_f = Special_Food()
                Special_Food_timer = 75 * 15
            else:
                Special_Food_timer -= FPS

                # Progress levels based on score
            if snake.score >= 3 and current_lvl == lvl1:  status = 2; current_lvl = lvl2
            if snake.score >= 6 and current_lvl == lvl2:  status = 3; current_lvl = lvl3
            if snake.score >= 9 and current_lvl == lvl3:  status = 4
        

        snake.draw_snake()  # Draw snake
        food.draw()        # Draw food
        special_f.draw()
    else:
        welcome.draw()  # Draw welcome screen if game not started
    
    # Draw lose screen if game over
    if game_start and game_s_lose == True:
        lose.draw()
    
    # Draw score and level info
    score_font.render_to(screen, (20, 20), f"Score: {snake.score}", Color[0])
    score_font.render_to(screen, (900, 20), f"Level: {status}", Color[0])
    score_font.render_to(screen, (450, 20), f"Timer: {Special_Food_timer // (75 * 3)}", Color[0])
    pg.display.update()  # Update display
    pg.display.flip()    # Flip buffersa
    
    
#WARNING IN 3th LEVEL SNAKE WILL BE AS STEP - STEP NOT MONOTONIK. IT IS NOT A BUG OR MISTAKE. IT WAS IN PLAN :)
