import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1200
WINDOWHIEGHT = 650
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Test')
mainClock = pygame.time.Clock()

def intro(windowsSurface):
    WHITE = (255, 255, 255)
    GRAY = (168, 168, 168)
    Font = pygame.font.SysFont(None, 20)
    windowSurface.fill(WHITE)
    logoImage = pygame.image.load('logo.png')
    logoRect = logoImage.get_rect()
    logoRect.centerx = windowsSurface.get_rect().centerx
    logoRect.centery = windowsSurface.get_rect().centery
    windowsSurface.blit(logoImage, logoRect)

    text = Font.render('Initializing...', True, GRAY, WHITE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery + 100
    
    windowSurface.blit(text, textRect)
    pygame.display.update()
    pygame.time.delay(5000)
    
    #Remove when full version is complete
    pygame.quit()
    sys.exit()
 
intro(windowSurface)
   
