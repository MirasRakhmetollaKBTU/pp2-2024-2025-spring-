import pygame as pg
import random
import math

pg.init()
pg.font.init()
pg.display.set_caption("Snake Game")
Width  = 1080
Height = 1080
Color  = [
    (0, 0, 0), #black
    (255, 255, 255), #White
    (16, 128, 31), #ground
    (212, 13, 82), #point
    (0, 0, 240), #Snake
    (0, 0, 255), #Snake_Head
    (18, 61, 4) #Wall
]

fin_s = 1
etap  = 4
clock = pg.time.Clock()
game_s_lose = False

       
def distance_point_to_segment(px, py, x1, y1, x2, y2):
    length_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if length_sq == 0:
        return math.hypot(px - x1, py - y1)
    t = max(0, min(1, ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / length_sq))
    proj_x = x1 + t * (x2 - x1)
    proj_y = y1 + t * (y2 - y1)
    return math.hypot(px - proj_x, py - proj_y)


But = [
    pg.Rect(0, 0, Width, Height),
    pg.Rect(100, 400, 340, 60),
    pg.Rect(370, 540, 340, 60)
]


class GameState:
    def __init__(self, title_text, button_text=None):
        self.my_font = pg.freetype.SysFont("Comic Sans MS", 80)
        self.my_font2 = pg.freetype.SysFont("Comic Sans MS", 60)
        self.title_text = title_text
        self.button_text = button_text

    def draw(self):
        screen.fill(Color[1])
        pg.draw.rect(screen, (255, 0, 0), But[0])
        if self.button_text:
            pg.draw.rect(screen, (0, 255, 0), But[2])
            self.my_font2.render_to(screen, (380, 540), self.button_text, Color[0])
        self.my_font.render_to(screen, (340, 270), self.title_text, Color[0])

class Game_Welcom(GameState):
    def __init__(self):
        super().__init__("", "Start game")
        self.my_font = pg.freetype.SysFont("Comic Sans MS", 60)
    
    def draw(self):
        screen.fill(Color[1])
        pg.draw.rect(screen, (255, 0, 0), But[0])
        pg.draw.rect(screen, (0, 255, 0), But[1])
        self.my_font.render_to(screen, (100, 400), "Start game", Color[0])

class WIN(GameState):
    def __init__(self):
        super().__init__("YOU WIN!", "Play Again")

class LOSE(GameState):
    def __init__(self):
        super().__init__("YOU Lose!", "Play Again")

class NEXT(GameState):
    def __init__(self):
        super().__init__("GO Next", "GO LEVEL UP")


class Food:
    def __init__(self):
        self.size = 30
        self.position = self.generate_pos(snake, current_lvl)

    def generate_pos(self, snake, level):
        while True:
            x = random.randint(0, (Width - self.size) // self.size) * self.size
            y = random.randint(0, (Height - self.size) // self.size) * self.size
            rect = pg.Rect(x, y, self.size, self.size)

            if not any(segment.colliderect(rect) for segment in snake.Full_Body) and not lvl1.check_collision_for_food(rect) and not lvl2.check_collision_for_food(rect) and not lvl3.check_collision_for_food(rect):
                return x, y

    def draw(self):
        pg.draw.rect(screen, Color[3], (self.position[0], self.position[1], self.size, self.size))
        

class Snake:
    body_size = 30
    step = 15
    def __init__(self):
        cord_X = (Width - self.body_size) // 2
        cord_Y = (Height - self.body_size) // 2

        self.Head = pg.Rect(cord_X, cord_Y, self.body_size, self.body_size)
        self.Body = pg.Rect(cord_X - self.body_size, cord_Y, self.body_size, self.body_size)
        
        self.direction = (self.step, 0)
        self.Full_Body = [self.Head, self.Body]

        self.step_grow = 10
        self.score = 0
    def draw_snake(self):
        for snake in self.Full_Body:
            if snake == self.Full_Body[0]: pg.draw.rect(screen, Color[4], snake)
            else: pg.draw.rect(screen, Color[5], snake)
    
    def move(self, level):
        global game_s_lose  

        head_x, head_y = self.Full_Body[0].x, self.Full_Body[0].y
        dx, dy = self.direction 

        new_head = pg.Rect(head_x + dx, head_y + dy, self.body_size, self.body_size)

        if level.check_collision(new_head) or new_head in self.Full_Body:
            game_s_lose = True
            return

        self.Full_Body.insert(0, new_head)  
        self.Full_Body.pop()
   
    def grow(self):
        self.Full_Body.append(self.Full_Body[-1].copy())
        self.score += 1
        if self.score % 3 == 0: 
            self.step += self.step_grow 
        
    def set_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)




class Level:
    def __init__(self):
        self.game_board = pg.Rect(0, 0, Width, Height)
        self.walls = []
    
    def draw_game_board(self):
        pg.draw.rect(screen, Color[2], self.game_board)
        for wall in self.walls:
            pg.draw.line(screen, Color[6], wall[0], wall[1], 30)

    def check_collision(self, snake_head):
        head_center = (snake_head.x + snake_head.width // 2, snake_head.y + snake_head.height // 2)

        for (start, end) in self.walls:
            if distance_point_to_segment(*head_center, *start, *end) < 15:
                status = -1
                pg.time.wait(1000)
                return True
        if snake_head.x <= 0 or snake_head.x + snake_head.width >= Width or snake_head.y <= 0 or snake_head.y >= Height:
            status = -1
            pg.time.wait(3000)
            return True

        return False

    def check_collision_for_food(self, food_rect):   
        for start, end in self.walls:
            if distance_point_to_segment(food_rect.x + food_rect.width // 2, food_rect.y + food_rect.height // 2, *start, *end) < 35:
                return True
        return False  


class Level1(Level):
    def __init__(self):
        super().__init__()
        self.walls = [
            ((100, 0), (100, 800)),
            ((700, 200), (700, 900)),
            ((700, 500), (1000, 500)),
            ((800, 700), (1080, 700)),
            ((800, 200), (1080, 200)),
            ((0, 900), (715, 900)),
            ((300, 200), (715, 200))
        ]

class Level2(Level):
    def __init__(self):
        super().__init__()
        self.walls = [
            ((100, 0), (100, 1000)),
            ((1000, 100), (1000, 1080)),
            ((700, 985), (700, 200)),
            ((300, 100), (300, 800)),
            ((1015, 100), (200, 100)),
            ((100, 985), (900, 985))
        ]

class Level3(Level):
    def __init__(self):
        super().__init__()
        self.walls = [
            ((0, 600), (900, 600)),
            ((1080, 400), (100, 400)),
            ((114, 400), (114, 60)),
            ((114, 600), (114, 1000)),
            ((314, 400), (314, 60)),
            ((314, 600), (314, 1000)),
            ((514, 400), (514, 60)),
            ((514, 600), (514, 1000)),
            ((714, 400), (714, 60)),
            ((714, 600), (714, 1000))
        ]


screen = pg.display.set_mode((Width, Height))
gm_run = True

game_start = False

FPS = 15

snake = Snake()
lvl1  = Level1()
lvl2  = Level2()
lvl3  = Level3()
lose  = LOSE()

welcome = Game_Welcom()
status  = 0

You_win = WIN()

welcome.draw()
score_font = pg.freetype.SysFont("Comic Sans MS", 40)

current_lvl = lvl1

food = Food()
food.draw()
quantity_food = 1

while gm_run:
    screen.fill(Color[1])
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            gm_run = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            mous_x, mous_y = event.pos
            print(event)
            if But[1].collidepoint(mous_x, mous_y):
                game_start = True
                status = 1
            if But[2].collidepoint(mous_x, mous_y) and game_s_lose:
                game_s_lose = False
                status = 1
                snake = Snake()  
                food = Food()    
                current_lvl = lvl1  


        if event.type == pg.KEYDOWN:
            print(event)
            if status != -1:
                if event.key == pg.K_DOWN:  snake.set_direction(0, snake.step)
                if event.key == pg.K_UP:    snake.set_direction(0, -snake.step)
                if event.key == pg.K_LEFT:  snake.set_direction(-snake.step, 0)
                if event.key == pg.K_RIGHT: snake.set_direction(snake.step, 0)
    
    if game_start and not game_s_lose:
        if status == 1: lvl1.draw_game_board()
        if status == 2: lvl2.draw_game_board()
        if status == 3: lvl3.draw_game_board()
        if status == 4: You_win.draw()

        if status != 4 and status != -1: 
            snake.move(current_lvl)
            if snake.Full_Body[0].colliderect(pg.Rect(food.position[0], food.position[1], food.size, food.size)):            
                snake.grow()
                food = Food()

                if snake.score == 3:  status = 2; current_lvl = lvl2
                if snake.score == 6:  status = 3; current_lvl = lvl3
                if snake.score == 9: status = 4

        snake.draw_snake()
        food.draw()  
    else:
        welcome.draw()

    
    if game_start and game_s_lose == True:
        lose.draw()
    
    score_font.render_to(screen, (20, 20), f"Score: {snake.score}", Color[0])
    score_font.render_to(screen, (900, 20), f"Level: {status}", Color[0])

    pg.display.update()
    pg.display.flip()
