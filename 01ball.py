import sys, pygame
pygame.init()

size = width, height = 1520, 900
speed = [2, 3]

rgbColor = red, green, blue, alpha = 0, 0, 0, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left+100 < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        pygame.draw.circle(screen, (0,200,200), (ballrect.right, ballrect.bottom), 20, 0)
        
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        
    red = ballrect.right/5 % 256
    blue = ballrect.bottom/5  % 256
    green = (red + blue)/3 % 256
    rgbColor = red, green, blue, 255

    screen.fill(rgbColor)
    screen.blit(ball, ballrect)
    
    pygame.display.flip()