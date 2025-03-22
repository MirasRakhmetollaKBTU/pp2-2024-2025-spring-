import pygame as pg


pg.init()

WIDTH, HEIGHT = 1080, 1080

running = True
screen  = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Paint")

Color = [
    (0, 0, 0), # Border
    (255, 255, 255), # FOLDER
    (93, 145, 163), # Background
    (96, 173, 117) # Environment
]

ColorForDraw = {
    "Black"  :  (0, 0, 0),
    "Red"    :  (255, 0, 0),
    "Green"  :  (0, 255, 0),
    "Blue"   :  (0, 0, 255),
    "Yellow" :  (255, 255, 0),
    "White"  :  (255, 255, 255),
    "Pink"   :  (255, 0, 255),
    "Silver" :  (100, 100, 100),
    "Brown"  :  (185, 122, 87),
    "Orange" :  (255, 127, 39)
}

class MAIN_FOLDER :
    def __init__(self):
        self.folder = pg.Surface((WIDTH - 100, HEIGHT))
        self.folder.fill(Color[1])
        self.drawing   = False
        self.start_pos = None

    def drawfolder(self):
        screen.blit(self.folder, (100, 0))

    def core(self, pos, mode, color):
        pos = (pos[0] - 100, pos[1])
        if mode == "eraser" and self.start_pos:
            pg.draw.circle(self.folder, Color[1], pos, 10)
        
        if mode == "circle" and self.start_pos:
            radious = max(abs(pos[0] - self.start_pos[0]), (pos[1] - self.start_pos[1]))
            pg.draw.circle(self.folder, color, self.start_pos, radious, 5)
        
        if mode == "rect" and self.start_pos:
            rect = pg.Rect(*self.start_pos, pos[0] - self.start_pos[0], pos[1] - self.start_pos[1])
            pg.draw.rect(self.folder, color, rect, 5)

        if mode == "pen" and self.start_pos:
            pg.draw.circle(self.folder, color, pos, 10)

class HELPER_FOLDER:
    def __init__(self):

        self.current_color  = ColorForDraw["Black"]
        self.current_mode   = "pen"
        self.current_radius = 5

        self.eraser_but = pg.Rect(10, 10, 30, 30)
        self.rect_but   = pg.Rect(10, 85, 30, 30)
        self.circle_but = pg.Rect(25, 65, 20, 20)
        self.pen_but    = pg.Rect(10, 125, 30, 30)
        
        self.color_list = []
        cash = 1
        cash_x, cash_y = 0, (HEIGHT - 500) // 2
        cash_x1 = 50
        for color in ColorForDraw:
            if cash < 6:
                rect = pg.Rect(cash_x, cash_y, 50, 50)
                self.color_list.append((rect, ColorForDraw[color]))
                cash += 1
                cash_y += 50
            else:
                cash_y -= 50
                rect = pg.Rect(cash_x1, cash_y, 50, 50)
                self.color_list.append((rect, ColorForDraw[color]))
        
    def drawfolder(self):
        pg.draw.rect(screen, Color[2], pg.Rect(0, 0, WIDTH, HEIGHT))
        pg.draw.rect(screen, Color[3], pg.Rect(0, (HEIGHT - 500) // 2, 100, 250))
           
        
        for rect, color in self.color_list:
            pg.draw.rect(screen, color, rect)

        pg.draw.rect(screen, Color[1], self.eraser_but)
        pg.draw.circle(screen, Color[0], (25, 65), 15, 5)
        pg.draw.rect(screen, Color[0], self.rect_but, 5)
        pg.draw.rect(screen, Color[0], self.pen_but)


    def get_color_and_mode(self, pos):
        for rect, color in self.color_list:
            if rect.collidepoint(pos):
                self.current_color = color

        if self.eraser_but.collidepoint(pos): self.current_mode = "eraser"
        if self.rect_but.collidepoint(pos):   self.current_mode = "rect"
        if self.circle_but.collidepoint(pos): self.current_mode = "circle"
        if self.pen_but.collidepoint(pos): self.current_mode = "pen"

        print(helper.current_color)
        print(helper.current_mode)

helper = HELPER_FOLDER()
folder = MAIN_FOLDER()

while running:
    screen.fill(Color[2])

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] > 100:
                    folder.drawing = True
                    folder.start_pos = (event.pos[0] - 100, event.pos[1])
                else:
                    helper.get_color_and_mode(event.pos)

        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                folder.drawing = False

        elif event.type == pg.MOUSEMOTION:
            if folder.drawing:
                folder.core(event.pos, helper.current_mode, helper.current_color)

    

    helper.drawfolder()
    folder.drawfolder()
    pg.display.flip()
