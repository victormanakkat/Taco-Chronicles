import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 900
WINDOWHIEGHT = 650
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Test')
mainClock = pygame.time.Clock()

BLUE = (0,0,255)
WHITE = (255, 255, 255)

class Button:
    def __init__():
        pass
    def arrow():
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] > 695 and event.pos[0] < 735:
                if event.pos[1] > 30 and event.pos[1] < 50:
                    dropDownButton = True
                    if dropDownGun == True:
                        dropDownGun = False
                    else:
                        dropDownGun = True
        if event.type == MOUSEMOTION:
            if event.pos[0] > 695 and event.pos[0] < 735:
                if event.pos[1] > 30 and event.pos[1] < 50:
                    dropDownButton = True                       
                else:
                    dropDownButton = False
            else:
                dropDownButton = False
                
block = {'rect':pygame.Rect(200, 200, 50, 50),'color':BLUE}
windowSurface.fill(WHITE)
pygame.draw.rect(windowSurface, block['color'], block['rect'])

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    mainClock.tick()
  
