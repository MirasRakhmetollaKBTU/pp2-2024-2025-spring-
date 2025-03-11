import pygame as pyg

pyg.init()
screen = pyg.display.set_mode((1000, 800))


done   = False
color  = (255, 0, 0)
radius = 25

x = 30
y = 30

while not done:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            done = True
        
        
        pressed = pyg.key.get_pressed()

        
        if pressed[pyg.K_DOWN]:  y += 20
        if pressed[pyg.K_UP]:    y -= 20
        if pressed[pyg.K_LEFT]:  x -= 20
        if pressed[pyg.K_RIGHT]: x += 20
        
        if (x < radius):        x = radius
        if (x > 1000 - radius): x = 1000 - radius
        if (y < radius):        y = radius
        if (y > 800 - radius):  y = 800 - radius
        

        screen.fill((255, 255, 255))

        pyg.draw.circle(screen, color, (x, y), radius)

        pyg.display.flip()
