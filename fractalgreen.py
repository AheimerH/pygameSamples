import pygame, sys, math
from pygame.locals import *

def tree(x, y, length, angle):
    if(length < 3):
        return
    x_top = int(x + math.cos(math.radians(angle)) * length)
    y_top = int( y - math.sin(math.radians(angle)) * length)
    
    pygame.draw.line(DISPLAYSURF, THE_COLOR, (x, y), (x_top, y_top), int(length / 10) + 1)
    tree(x_top, y_top, int(length/2), angle+30)
    tree(x_top, y_top, int(length/3), angle+80)
    tree(x_top, y_top, int(length/1.3), angle+5)
    tree(x_top, y_top, int(length/1.6), angle-45)

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1800, 1000), 0, 32)
pygame.display.set_caption('Little Fractal')


BACKGROUND = (50, 100, 50)
THE_COLOR = (100, 200, 100)

# draw on the surface object
DISPLAYSURF.fill(BACKGROUND)
tree(500, 1050, 250,90)

# rund the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()


