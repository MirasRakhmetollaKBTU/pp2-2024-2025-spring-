import pygame as pg
import psycopg2
import random
import time
import sys
from config import load_config
from enum import Enum, auto

pg.init()
pg.font.init()

SCREEN_WIDTH  = 1080
SCREEN_HEIGHT = 1080
FPS = 15


class Database:
    def __init__(self):
        self.config = load_config()

    def get_user(self, username):
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    
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
                        return Player(result[1], result[2], result[3])
                    
                    return None
        except Exception as error:
            print("Error getting user:", error)
            return None
        
    def create_user(self, username):
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:

                    cur.execute("""
                            INSERT INTO users (user_name)
                            VALUES (%s)
                            ON CONFLICT (user_name) DO NOTHING
                            RETURNING user_id
                            """, (username,))
                    
                    user_id_row = cur.fetchone()
                        
                    if user_id_row is None:
                        cur.execute("SELECT user_id FROM users WHERE user_name = %s", (username,))
                        user_id = cur.fetchone()[0]
                    else:
                        user_id = user_id_row[0]

                    
                    cur.execute("""
                            INSERT INTO users_score (user_id, score, level)
                            VALUES (%s, %s, %s)
                            """, (user_id, 0, 1))

                    conn.commit()
                    return Player(username, 1, 0)

        except Exception as error:
                print("Error creating user:", error)
                return None

    def safe_game(self, player):
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                        
                    cur.execute("SELECT user_id FROM users WHERE user_name = %s", (player.name,))
                    user_id = cur.fetchone()[0]

                    
                    cur.execute("""
                            INSERT INTO users_score (user_id, score, level)
                            VALUES (%s, %s, %s)
                            """, (user_id, player.score, player.level))

                    
                    conn.commit()
                    return True

        except Exception as error:
                print("Error saving game:", error)
                return False



class Colors:
    Black  = pg.Color(0, 0, 0)
    White  = pg.Color(255, 255, 255)
    Ground = pg.Color(16, 128, 31)
    Food   = pg.Color(212, 13, 82)
    Snake  = pg.Color(0, 0, 255)
    Wall   = pg.Color(18, 61, 4)
    SpFood = pg.Color(255, 0, 0)
    GreenB = pg.Color(0, 255, 0)
    RedB   = pg.Color(255, 0, 0)    
    TextInput = pg.Color(200, 200, 200)

class GameState(Enum):
    Login   = auto()
    Menu    = auto()
    Playing = auto()
    Paused  = auto()
    Win     = auto()
    Lose    = auto()


class Buttons:
    FULL_SCREEN = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    START       = pg.Rect(100, 400, 340, 60)
    PLAY_AGAIN  = pg.Rect(370, 540, 340, 60)
    SAVE_GAME   = pg.Rect(100, 400, 340, 60)
    LOGIN       = pg.Rect(400, 500, 200, 50)


class Player:
    def __init__(self, name, level=1, score=0):
        self.name  = name
        self.level = level
        self.score = score

class Snake:
    def __init__(self, speed=7):
        self.body_size = 20
        self.step      = speed
        self.direction = (self.step, 0)
        self.score     = 0
        self.step_grow = 2
        self.speed_increase_interval = 3
        self.initial_position()

    def initial_position(self):
        center_x  = (SCREEN_WIDTH - self.body_size) // 2
        center_y  = (SCREEN_HEIGHT - self.body_size) // 2
        self.head = pg.Rect(center_x, center_y, self.body_size, self.body_size)
        self.body = [self.head.copy(), pg.Rect(center_x - self.body_size, center_y, self.body_size, self.body_size)]
    
    def move(self, current_level):
        head_x, head_y = self.body[0].x, self.body[0].y
        dx, dy = self.direction
        new_head = pg.Rect(head_x + dx, head_y + dy, self.body_size, self.body_size)

        if current_level.check_collision(new_head) or new_head in self.body[1:]:
            return False

        self.body.insert(0, new_head)
        self.body.pop()
        return True

    def grow(self):
        self.body.append(self.body[-1].copy())
        self.score += 1

        if self.score % self.speed_increase_interval == 0:
            self.step += self.step_grow

    def set_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def draw(self, surface):
        for i, segment in enumerate(self.body):
            pg.draw.rect(surface, Colors.Snake, segment)

class Level:
    def __init__(self, level_num):
        self.game_board = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.level_num  = level_num
        self.walls      = []
        self._setup_level()

    def _setup_level(self):
        if self.level_num == 1:
            self.walls = [
                pg.Rect(100, 0, 15, 800),
                pg.Rect(700, 200, 15, 700),
                pg.Rect(700, 500, 300, 15),
                pg.Rect(800, 700, 280, 15),
                pg.Rect(800, 200, 280, 15),
                pg.Rect(0, 900, 715, 15),
                pg.Rect(300, 200, 415, 15)
            ]
        elif self.level_num == 2:
            self.walls = [
                pg.Rect(100, 0, 15, 1000),
                pg.Rect(1000, 100, 15, 980),
                pg.Rect(700, 200, 15, 785),
                pg.Rect(300, 100, 15, 700),
                pg.Rect(200, 100, 815, 15),
                pg.Rect(100, 985, 800, 15)
            ]
        elif self.level_num == 3:
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
        
    def draw(self, surface):
        pg.draw.rect(surface, Colors.Ground, self.game_board)
        for wall in self.walls:
            pg.draw.rect(surface, Colors.Wall, wall)

    def check_collision(self, rect):
        for wall in self.walls:
            if rect.colliderect(wall):
                return True

        return (rect.left <= 0 or rect.right >= SCREEN_WIDTH or rect.top <= 0 or rect.bottom >= SCREEN_HEIGHT)
    
    def check_collision_for_food(self, food_rect):
        return any(food_rect.colliderect(wall) for wall in self.walls)

class Food:
    def __init__(self, size=30):
        self.size     = size
        self.position = (0, 0)
        self.rect     = pg.Rect(0, 0, size, size)
        self.generate_new_postion()

    def generate_new_postion(self, snake=None, levels=None):
        if levels is None: levels = []
        if snake  is None: snake_body = []
        else: snake_body = snake.body

        while True:
            x = random.randint(0, (SCREEN_WIDTH - self.size) // self.size) * self.size
            y = random.randint(0, (SCREEN_HEIGHT - self.size) // self.size) * self.size
            self.rect.x = x
            self.rect.y = y

            collision = False
            for segment in snake_body:
                if self.rect.colliderect(segment):
                    collision = True
                    break

            if not collision:
                for level in levels:
                    if level.check_collision_for_food(self.rect):
                        collision = True
                        break

            if not collision:
                self.position = (x, y)
                return

    def draw(self, surface):
                pg.draw.rect(surface, Colors.Food, self.rect)


class SpecialFood(Food):
    def __init__(self):
        super().__init__(size=40)
        self.color  = Colors.SpFood
        self.timer  = 0
        self.active = False
        self.color  = Colors.SpFood
        self.spawn_interval = 5 * FPS
        self.life_time      = 5 * FPS

    def update(self):
        if not self.active:
            self.timer += 1
            if self.timer >= self.spawn_interval:
                self.generate_new_postion()
                self.active = True
                self.timer = 0
        else:
            self.timer += 1
            if self.timer >= self.life_time:
                self.active = False
                self.timer = 0
    
    def generate_new_postion(self, snake=None, levels=None):
        if levels is None: levels = []
        if snake  is None: snake_body = []
        else: snake_body = snake.body

        super().generate_new_postion(snake, levels)

    def draw(self, surface):
        if self.active: pg.draw.rect(surface, self.color, self.rect)

class TextInput:
    def __init__(self, x, y, width, height, font_size=32):
        self.rect  = pg.Rect(x, y, width, height)
        self.color = Colors.TextInput
        self.text  = ''
        self.font  = pg.font.SysFont('Arial', font_size)
        self.activate = True

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pg.KEYDOWN and self.activate:
            if event.key == pg.K_RETURN:
                return True
            elif event.key ==pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return False

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, Colors.Black)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
    

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Snake Game")
        self.clock  = pg.time.Clock()
        self.db     = Database()
        
    
        self.snake         = None
        self.current_level = None
        self.food          = None
        self.special_food  = None
        
    
        self.state  = GameState.Login
        self.player = None
        self.text_input = TextInput(400, 400, 280, 50)
        
    
        self.title_font  = pg.freetype.SysFont("Comic Sans MS", 80)
        self.button_font = pg.freetype.SysFont("Comic Sans MS", 60)
        self.score_font  = pg.freetype.SysFont("Comic Sans MS", 40)
        self.info_font   = pg.freetype.SysFont("Comic Sans MS", 30)
   
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
           
            if self.state == GameState.Login:
                if self.text_input.handle_event(event):
                    self.handle_login()
                elif event.type == pg.MOUSEBUTTONDOWN and Buttons.LOGIN.collidepoint(event.pos):
                    self.handle_login()

            elif event.type == pg.MOUSEBUTTONDOWN: self.handle_mouse_click(event.pos)
            elif event.type == pg.KEYDOWN:         self.handle_key_press(event.key)

        return True

    def handle_login(self):
        username = self.text_input.text.strip()
        if username:
            self.player = self.db.get_user(username)
            if not self.player:
                self.player = self.db.create_user(username)

            if self.player:
                self.state = GameState.Menu
                self.initialize_game()

    def handle_mouse_click(self, pos):
        if   self.state == GameState.Win    and Buttons.PLAY_AGAIN.collidepoint(pos) and self.player.level == 3: self.reset_game()
        elif self.state == GameState.Menu   and Buttons.START.collidepoint(pos):      self.start_game()
        elif self.state == GameState.Lose   and Buttons.PLAY_AGAIN.collidepoint(pos): self.reset_game()
        elif self.state == GameState.Win    and Buttons.PLAY_AGAIN.collidepoint(pos): self.next_level()
        elif self.state == GameState.Paused and Buttons.SAVE_GAME.collidepoint(pos):  self.save_game()
    
    def handle_key_press(self, key):
        if self.state == GameState.Playing:
            if key == pg.K_DOWN:   self.snake.set_direction(0, self.snake.step)
            if key == pg.K_UP:     self.snake.set_direction(0, -self.snake.step)
            if key == pg.K_LEFT:   self.snake.set_direction(-self.snake.step, 0)
            if key == pg.K_RIGHT:  self.snake.set_direction(self.snake.step, 0)
            if key == pg.K_ESCAPE: self.state = GameState.Paused
            if key == pg.K_p:      self.state = GameState.Paused 

        if self.state == GameState.Paused:
            if key == pg.K_s: 
                self.player.score = self.snake.score
                self.player.level = self.current_level.level_num
                self.db.safe_game(self.player)
                self.state = GameState.Playing

    def initialize_game(self):
        initial_speed      = 7 + (self.player.level * 2 - 1) * 2
        self.snake         = Snake(initial_speed)
        self.current_level = Level(self.player.level)
        self.food          = Food()
        self.special_food  = SpecialFood()
        self.snake.score   = self.player.score


    def start_game(self):
        self.state = GameState.Playing
        self.initialize_game()

    def reset_game(self):
        if self.player.level == 3: self.player.level = 1; self.player.score = 0
        self.initialize_game()
        self.state = GameState.Playing

    def next_level(self):
        if self.player.level < 3:
            self.player.level += 1
            self.player.score += 1
            self.player.score  = self.snake.score
            self.db.safe_game(self.player)
            self.initialize_game()
            self.state = GameState.Playing
        else:
            self.state = GameState.Win

    def save_game(self):
        self.player.score = self.snake.score
        if self.db.safe_game(self.player):
            self.state = GameState.Menu

    def update(self):
        if self.state != GameState.Playing:
            return

        if not self.snake.move(self.current_level):
            self.state = GameState.Lose
            return


        if self.snake.body[0].colliderect(self.food.rect):
            self.snake.grow()
            self.food.generate_new_postion(self.snake, [self.current_level])

        if self.snake.score >= self.player.level * 5:
            self.state = GameState.Win

        self.special_food.update()

        if (self.special_food.active and self.snake.body[0].colliderect(self.special_food.rect)):
            self.snake.grow()
            self.snake.score += 1
            self.special_food.active = False
            self.special_food.timer  = 0
    

    def draw(self):
        self.screen.fill(Colors.White)

        if self.state == GameState.Login:   self.draw_login()
        if self.state == GameState.Menu:    self.draw_menu()
        if self.state == GameState.Playing: self.draw_game()
        if self.state == GameState.Win:     self.draw_win()
        if self.state == GameState.Lose:    self.draw_lose()
        if self.state == GameState.Paused:  self.draw_paused()

        if self.state in [GameState.Playing, GameState.Paused]:
            self.draw_score()

        pg.display.flip()
        
        if self.state == GameState.Win and self.player.level == 3: pass

    def draw_login(self):
        self.title_font.render_to(self.screen, (340, 270), "Enter Username", Colors.Black)
        self.text_input.draw(self.screen)
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.LOGIN)
        self.button_font.render_to(self.screen, (Buttons.LOGIN.x + 50, Buttons.LOGIN.y + 10), "Login", Colors.Black)

    def draw_paused(self):
        self.title_font.render_to(self.screen, (80, 270), "PAUSED / press S to save", Colors.Black)
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.SAVE_GAME)
        self.button_font.render_to(self.screen, (Buttons.SAVE_GAME.x + 20, Buttons.SAVE_GAME.y + 10), "Save & Play", Colors.Black)

    def draw_menu(self):
        pg.draw.rect(self.screen, Colors.RedB, Buttons.FULL_SCREEN)
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.START)
        self.button_font.render_to(self.screen, (Buttons.START.x + 20, Buttons.START.y + 10), "Start Game", Colors.Black)

        info_text = f"Welcom {self.player.name}! Level: {self.player.level}, Score: {self.player.score}"
        self.info_font.render_to(self.screen, (100, 100), info_text, Colors.Black)

    def draw_win(self):
        self.title_font.render_to(self.screen, (340, 270), "Level Complete!", Colors.Black)
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.PLAY_AGAIN)
        
        if self.player.level < 3: text = "Next Level"
        else: text = "Play again"
        
        self.button_font.render_to(self.screen, (Buttons.PLAY_AGAIN.x + 20, Buttons.PLAY_AGAIN.y + 10), text, Colors.Black)

    def draw_game(self):
        self.current_level.draw(self.screen)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.special_food.draw(self.screen)
    
    def draw_lose(self):
        self.title_font.render_to(self.screen, (340, 270), "Game Over!", Colors.Black)
        pg.draw.rect(self.screen, Colors.GreenB, Buttons.PLAY_AGAIN)
        self.button_font.render_to(self.screen, (Buttons.PLAY_AGAIN.x + 20, Buttons.PLAY_AGAIN.y + 10), "Playe again", Colors.Black)

    def draw_score(self):
        self.score_font.render_to(self.screen, (20, 20), f"Score: {self.snake.score}", Colors.Black)
        self.score_font.render_to(self.screen, (900, 20), f"Level: {self.player.level}", Colors.Black)
        if self.special_food.active:
            remaining_time = (self.special_food.life_time - self.special_food.timer) // FPS
            self.score_font.render_to(self.screen, (450, 20), f"Timer: {remaining_time}", Colors.Black)


    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
    pg.quit()
