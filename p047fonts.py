import pygame, sys, time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('HeLlo wOrlD')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('RugeBoogie-Regular.ttf', 64)
textSurfaceObj = fontObj.render('Hällö worLD!§', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
textSurfaceObj2 = fontObj.render('Greetings from the horse without name', False, GREEN)
textRectObj2 = textSurfaceObj2.get_rect()
textRectObj2.top = textRectObj.bottom + 2
textRectObj2.left = textRectObj.left



while True: # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
    
    pygame.display.update()
    
    # Loading and playing a sound effect:
    soundObj = pygame.mixer.Sound('sounds/beep-01.wav')
    soundObj.play(-1, 0, 0)
    # Loading and playing background music:
    # ...some more of your code goes here...
    time.sleep(1) # wait and let the sound play for 1 second
    soundObj.stop()
    time.sleep(10) 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    
                
