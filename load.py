#Intro Loading
#By Tyler Spadgenske
import pygame, sys, time
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

def Credits(screen):
    num = 0
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    screen.fill(WHITE)
    icon = pygame.image.load('files\\tylabs.png')
    rect = icon.get_rect()
    tylabs = pygame.transform.scale(icon, (300, 300))
    rect.centerx = screen.get_rect().centerx + 190
    rect.centery = screen.get_rect().centery + 120
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        comicFont = pygame.font.Font('files\\font\\font.ttf', 20)
        text = comicFont.render('CREATED BY TYLER SPADGENSKE', True, RED, WHITE)
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery + 150
        screen.blit(text, textRect)
        screen.blit(tylabs, rect)
        pygame.display.update()
        num += 1
        if num > 1000:
            break

