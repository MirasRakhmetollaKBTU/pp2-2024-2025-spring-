import pygame as pyg
import os
import datetime

pyg.init()
screen = pyg.display.set_mode((1400, 1050))
done   = False

image      = pyg.image.load('png/mickeyclock.png')
long_hand  = pyg.image.load('png/long.png')
short_hand = pyg.image.load('png/short.png')

short_hand = pyg.transform.scale(short_hand, (67, 295))
long_hand  = pyg.transform.scale(long_hand, (80, 400))

im_rect    = image.get_rect(center=(700, 525))
im_long_h  = long_hand.get_rect(center=(700,525))
im_short_h = short_hand.get_rect(center=(700, 525))

start_time = pyg.time.get_ticks()

while  not done:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            done = True
    
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    
    long_angle = seconds * 6
    short_angle = minutes * 6 

    rotated_long_hand  = pyg.transform.rotate(long_hand, -long_angle)
    rotated_short_hand = pyg.transform.rotate(short_hand, -short_angle)

    long_rect  = rotated_long_hand.get_rect(center=(700,525))
    short_rect = rotated_short_hand.get_rect(center=(700, 525))


    screen.blit(image, im_rect)
    screen.blit(rotated_long_hand, long_rect)
    screen.blit(rotated_short_hand, short_rect)
    

    pyg.display.flip()
