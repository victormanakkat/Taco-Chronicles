#Intro Loading
#By Tyler Spadgenske
import pygame, sys
from pygame.locals import *

pygame.init()

def Load(screen):
    WHITE = (255, 255, 255)
    ORANGE = (255, 103, 1)
    screen.fill(WHITE)
    comicFont = pygame.font.Font('files\\font\\font.ttf', 40)
    text = comicFont.render('PLEASE WAIT...', True, ORANGE, WHITE)
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery 
    screen.blit(text, textRect)
    pygame.display.update()

