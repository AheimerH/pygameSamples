import pygame, sys, math
from pygame.locals import *

def tree(x, y, length, angle):
    if(length < 5):
        return
    x_top = int(x + math.cos(math.radians(angle)) * length)
    y_top = int( y - math.sin(math.radians(angle)) * length)
    
    pygame.draw.line(DISPLAYSURF, THE_COLOR, (x, y), (x_top, y_top), int(length / 10) + 1)
    tree(x_top, y_top, int(length/2), angle+30)
    tree(x_top, y_top, int(length/1.3), angle+10)
    tree(x_top, y_top, int(length/1.5), angle-20)

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((1800, 900), 0, 32)
pygame.display.set_caption('Little Fractal')


BACKGROUND = (100, 0, 100)
THE_COLOR = (255, 100, 200)

# draw on the surface object
DISPLAYSURF.fill(BACKGROUND)
tree(450, 1000, 250,60)

# rund the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()


