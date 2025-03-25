import pygame as pg
import math

# Initialize Pygame module
pg.init()

# Set screen dimensions
WIDTH, HEIGHT = 1080, 1080

# Initialize game loop flag and create display window
running = True
screen  = pg.display.set_mode((WIDTH, HEIGHT))
# Set window title
pg.display.set_caption("Paint")
# Initialize font module
pg.font.init()
# Create font object for text rendering
font = pg.font.SysFont("Comic Sans MC", 30)
# Define basic color palette
Color = [
    (0, 0, 0),        # Border 
    (255, 255, 255), # FOLDER 
    (93, 145, 163), # Background
    (96, 173, 117) # Environment
]

# Define drawing color options
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

# Main drawing surface class
class MAIN_FOLDER :
    def __init__(self):
        # Create drawing surface with white background
        self.folder = pg.Surface((WIDTH - 100, HEIGHT))
        self.folder.fill(Color[1])
        # Track drawing state
        self.drawing   = False
        self.start_pos = None  # Starting position for shapes

    # Draw the folder surface onto the main screen
    def drawfolder(self):
        screen.blit(self.folder, (100, 0))

    # Core drawing logic based on mode and position
    def core(self, pos, mode, color):
        pos = (pos[0] - 100, pos[1])  # Adjust position for folder offset
        # Eraser mode 
        if mode == "eraser" and self.start_pos:
            pg.draw.circle(self.folder, Color[1], pos, 10)
        
        # Circle mode 
        if mode == "circle" and self.start_pos:
            radious = max(abs(pos[0] - self.start_pos[0]), (pos[1] - self.start_pos[1]))
            pg.draw.circle(self.folder, color, self.start_pos, radious, 5)
        
        # Rectangle mode 
        if mode == "rect" and self.start_pos:
            rect = pg.Rect(*self.start_pos, pos[0] - self.start_pos[0], pos[1] - self.start_pos[1])
            pg.draw.rect(self.folder, color, rect, 5)

        # Pen mode 
        if mode == "pen" and self.start_pos:
            pg.draw.circle(self.folder, color, pos, 10)

        # Square mode 
        if mode == "square" and self.start_pos:
            pg.draw.rect(self.folder, helper.current_color, pg.Rect(self.start_pos[0], self.start_pos[1], helper.current_length, helper.current_length))
        
        # Right triangle mode 
        if mode == "right_tran" and self.start_pos:
            point1 = self.start_pos
            point2 = (pos[0], self.start_pos[1])
            point3 = (self.start_pos[0], pos[1])
            pg.draw.polygon(self.folder, helper.current_color, [point1, point2, point3], 5)
        
        # Equilateral triangle mode 
        if mode == "equiv_tran" and self.start_pos: 
            base_length = abs(pos[0] - self.start_pos[0])
            height = (math.sqrt(3) / 2) * base_length
            point1 = ((self.start_pos[0] + pos[0]) // 2, self.start_pos[1] - height)
            point2 = self.start_pos
            point3 = (pos[0], self.start_pos[1])
            pg.draw.polygon(self.folder, helper.current_color, [point1, point2, point3])
        
        # Rhombus mode 
        if mode == "romb" and self.start_pos:
            center_x, center_y = self.start_pos
            point1 = (center_x, center_y - helper.current_length)
            point2 = (center_x + helper.current_length, center_y)
            point3 = (center_x, center_y + helper.current_length)
            point4 = (center_x - helper.current_length, center_y)
            pg.draw.polygon(self.folder, helper.current_color, [point1, point2, point3, point4])

# Toolbar/helper class for controls
class HELPER_FOLDER:
    def __init__(self):
        # Initialize default settings
        self.current_color  = ColorForDraw["Black"]  # Default drawing color
        self.current_mode   = "pen"                 # Default drawing mode
        self.current_length = 50                   # Default shape size
        # Define button rectangles
        self.eraser_but = pg.Rect(10, 10, 30, 30)                         # Eraser button
        self.rect_but   = pg.Rect(10, 85, 40, 30)                         # Rectangle button
        self.circle_but = pg.Rect(10, 40, 40, 40)                         # Circle button
        self.pen_but    = pg.Rect(10, 125, 30, 30)                        # Pen button
        self.square_but = pg.Rect(10, 175, 30, 30)                        # Square button
        self.right_tran = pg.Rect(10, 225, 40, 40)                        # Right triangle button
        self.points_rtran = [(10, 270), (10, 230), (40, 270)]             # Right triangle icon points
        self.equiv_tran = pg.Rect(50, 225, 40, 40)                        # Equilateral triangle button
        self.points_etran = [(50, 270), (65, 230), (80, 270)]             # Equilateral triangle icon points
        self.pluse_but  = pg.Rect(50, 175, 30, 30)                        # Increase size button
        self.pluse_points = [(50, 190), (80, 190), (65, 175), (65, 205)]  # Plus sign points
        self.minus_but  = pg.Rect(50, 125, 30, 30)                        # Decrease size button
        self.minus_points = [(50, 140), (80, 140)]                        # Minus sign points
        self.rombulus_b = pg.Rect(50, 10, 30, 30)                         # Rhombus button
        self.romb_points  = [(50, 25), (65, 10), (80, 25), (65, 40)]      # Rhombus icon points
        # Create color selection buttons
        self.color_list = []
        cash = 1
        cash_x, cash_y = 0, (HEIGHT - 500) // 2
        cash_x1 = 50
        for color in ColorForDraw:
            if cash < 6:
                rect = pg.Rect(cash_x, cash_y, 50, 50)  # First column of colors
                self.color_list.append((rect, ColorForDraw[color]))
                cash += 1
                cash_y += 50
            else:
                cash_y -= 50
                rect = pg.Rect(cash_x1, cash_y, 50, 50)  # Second column of colors
                self.color_list.append((rect, ColorForDraw[color]))
        
    # Draw the toolbar interface
    def drawfolder(self):
        pg.draw.rect(screen, Color[2], pg.Rect(0, 0, WIDTH, HEIGHT))  # Draw background
        pg.draw.rect(screen, Color[3], pg.Rect(0, (HEIGHT - 500) // 2, 100, 250))  # Draw toolbar area
        # Draw color selection rectangles
        for rect, color in self.color_list:
            pg.draw.rect(screen, color, rect)
        # Render and display current length
        self.show_lenght    = font.render(f"{self.current_length / 5}", True, Color[0])
        screen.blit(self.show_lenght, (50, 90))
        # Draw tool buttons and icons
        pg.draw.rect(screen, Color[1], self.eraser_but)       # Eraser button background
        pg.draw.circle(screen, Color[0], (25, 65), 15, 5)     # Circle button
        pg.draw.rect(screen, Color[0], self.rect_but, 5)      # Rectangle button
        pg.draw.rect(screen, Color[0], self.pen_but)          # Pen button
        pg.draw.rect(screen, Color[0], self.square_but, 5)    # Square button
        pg.draw.polygon(screen, Color[0], self.points_rtran)  # Right triangle icon
        pg.draw.polygon(screen, Color[0], self.points_etran)  # Equilateral triangle icon
        pg.draw.polygon(screen, Color[0], self.romb_points)   # Rhombus icon
        pg.draw.line(screen, Color[0], self.pluse_points[0], self.pluse_points[1], 5)  # Plus horizontal
        pg.draw.line(screen, Color[0], self.pluse_points[2], self.pluse_points[3], 5)  # Plus vertical
        pg.draw.line(screen, Color[0], self.minus_points[0], self.minus_points[1], 5)  # Minus sign

    # Handle color and mode selection from clicks
    def get_color_and_mode(self, pos):
        for rect, color in self.color_list:
            if rect.collidepoint(pos):  # Select color if clicked
                self.current_color = color
        # Set drawing mode based on button clicked
        if self.eraser_but.collidepoint(pos): self.current_mode = "eraser"
        if self.rect_but.collidepoint(pos):   self.current_mode = "rect"
        if self.circle_but.collidepoint(pos): self.current_mode = "circle"
        if self.pen_but.collidepoint(pos):    self.current_mode = "pen"
        if self.square_but.collidepoint(pos): self.current_mode = "square"
        if self.right_tran.collidepoint(pos): self.current_mode = "right_tran"
        if self.equiv_tran.collidepoint(pos): self.current_mode = "equiv_tran"
        if self.rombulus_b.collidepoint(pos): self.current_mode = "romb"
        if self.pluse_but.collidepoint(pos):  self.current_length += 10  # Increase size
        if self.minus_but.collidepoint(pos) and self.current_length >= 10:  self.current_length -= 10  # Decrease size
        # Debug print current settings
        print(helper.current_color)
        print(helper.current_mode)

# Create instances of helper and main folder
helper = HELPER_FOLDER()
folder = MAIN_FOLDER()

# Main game loop
while running:
    screen.fill(Color[2])  # Fill screen with background color

    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False  # Exit on window close
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if event.pos[0] > 100:  # Click in drawing area
                    folder.drawing = True
                    folder.start_pos = (event.pos[0] - 100, event.pos[1])
                else:  # Click in toolbar
                    helper.get_color_and_mode(event.pos)
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse release
                folder.drawing = False
        elif event.type == pg.MOUSEMOTION:
            if folder.drawing:  # Draw while mouse is moving and button held
                folder.core(event.pos, helper.current_mode, helper.current_color)

    # Update display
    helper.drawfolder()  # Draw toolbar
    folder.drawfolder()  # Draw main folder
    pg.display.flip()    # Update screen    
