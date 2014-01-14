#Intro Loading
#By Tyler Spadgenske
import pygame, sys
from pygame.locals import *

pygame.init()

def Intro(windowSurface):
    WHITE = (255, 255, 255)
    GRAY = (168, 168, 168)
    Font = pygame.font.SysFont(None, 20)
    windowSurface.fill(WHITE)
    logoImage = pygame.image.load('logo.png')
    logoRect = logoImage.get_rect()
    logoRect.centerx = windowSurface.get_rect().centerx
    logoRect.centery = windowSurface.get_rect().centery
    windowSurface.blit(logoImage, logoRect)

    text = Font.render('Initializing...', True, GRAY, WHITE)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx
    textRect.centery = windowSurface.get_rect().centery + 100
    
    windowSurface.blit(text, textRect)
    pygame.display.update()
