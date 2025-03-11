import pygame as pyg
import os

music  = [m for m in os.listdir("songs/") if os.path.isfile(os.path.join("songs/", m))]

def play_song():
    global music
    if pyg.mixer.music.get_busy():
        return
    if pyg.mixer.music.get_pos() > 0:
        pyg.mixer.music.unpause()
    elif music:
        pyg.mixer.music.load(f"songs/{music[0]}")
        pyg.mixer.music.play()

def pause():
    if pyg.mixer.music.get_busy():
        pyg.mixer.music.pause()

def play_next_song():
    global music
    if music:
        music.append(music.pop(0))
        pyg.mixer.music.load(f"songs/{music[0]}")
        pyg.mixer.music.play()

def play_previous_song():
    global music
    if music:
        music.insert(0, music.pop()) 
        pyg.mixer.music.load(f"songs/{music[0]}")
        pyg.mixer.music.play()

def button_(functional : str, screen, x : int, y : int, width : int, left : int):
    cash_color = (255, 255, 204)
    color      = (255, 204, 153)
    
    pyg.draw.rect(screen, cash_color, pyg.Rect(x, y, width, left))
    pyg.draw.rect(screen, color, pyg.Rect(x + 10, y + 10, width - 20, left -20))

    if functional == "play":
        point_list = [(30, 30), (30, 90), (90, 60)]
        pyg.draw.polygon(screen, (0, 0, 0), point_list)
    if functional == "stop":
         line1_start = (165, 30)
         line1_end   = (165, 90)
         line2_start = (195, 30)
         line2_end   = (195, 90)
         pyg.draw.line(screen, (0, 0, 0), line1_start, line1_end, 10)
         pyg.draw.line(screen, (0, 0, 0), line2_start, line2_end, 10)
    if functional == "previouse":
         point_list = [(250, 60), (280, 30), (280, 90)]
         line_start = (280, 60)
         line_end   = (340, 60)
         pyg.draw.polygon(screen, (0, 0, 0), point_list)
         pyg.draw.line(screen, (0, 0, 0), line_start, line_end, 10)
    if functional == "next":
         point_list = [(469, 60), (440, 30), (440, 90)]
         line_start = (380, 60)
         line_end   = (440, 60)
         pyg.draw.polygon(screen, (0, 0, 0), point_list)
         pyg.draw.line(screen, (0, 0, 0), line_start, line_end, 10)



pyg.init()
screen = pyg.display.set_mode((480, 120))
done   = False

buttons = [
  pyg.Rect(10, 10, 100, 100),
  pyg.Rect(120, 10, 100, 100),
  pyg.Rect(240, 10, 100, 100),
  pyg.Rect(360, 10, 100, 100)
]

while not done:
    for event in pyg.event.get():
        pyg.mixer.music.set_endevent(pyg.USEREVENT)
        if event.type == pyg.QUIT:
            done = True
        if event.type == pyg.USEREVENT:
            play_next_song()
        if event.type == pyg.MOUSEBUTTONDOWN:
            mous_x, mous_y = event.pos
            print(mous_x, ", ", mous_y)
   
            for i, button in enumerate(buttons):
                if button.collidepoint(mous_x, mous_y):
                    if mous_x >= 10 and mous_x <= 110 and mous_y >= 10 and mous_y <= 110:  play_song()
                    if mous_x >= 130 and mous_x <= 230 and mous_y >= 10 and mous_y <= 110: pause()
                    if mous_x >= 250 and mous_x <= 350 and mous_y >= 10 and mous_y <= 110: play_next_song()
                    if mous_x >= 370 and mous_x <= 470 and mous_y >= 10 and mous_y <= 110: play_previous_song()

        
        button_("play", screen, 0, 0, 120, 120)
        button_("stop", screen, 120, 0, 120, 120)
        button_("previouse", screen, 240, 0, 120, 120)
        button_("next", screen, 360, 0, 120, 120)
        
        
        pyg.display.flip()
