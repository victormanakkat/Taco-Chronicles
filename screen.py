#Start Screen
#By Tyler Spadgenske

import pygame, sys
from pygame.locals import *
#Import custom classes
from button import Button

pygame.init()

class Screen():
    def __init__(self, screen):
        self.buttons = Button(screen)
        self.screen = screen
        #Setup colors
        self.ORANGE = (255, 103, 1)
        self.WHITE = (255, 255, 255)
        #Setup title text
        self.comicFont = pygame.font.Font('fonts//font.ttf', 64)
        self.title = self.comicFont.render('THE TACO CHRONICLES', True, self.ORANGE, self.WHITE)
        self.titleRect = self.title.get_rect()
        self.titleRect.centerx = self.screen.get_rect().centerx
        self.titleRect.centery = self.screen.get_rect().centery - 180

        #Setup Highscore text
        self.highscoreFont = pygame.font.Font('fonts//font.ttf', 30)
        self.scoreText = self.highscoreFont.render('HIGHSCORE ', True, self.ORANGE, self.WHITE)
        self.scoreRect = self.scoreText.get_rect()
        self.scoreRect.centerx = self.screen.get_rect().centerx
        self.scoreRect.centery = self.screen.get_rect().centery        
        
    def startScreen(self, score, clicked):
        #Setup Highscore text
        pygame.display.update()
        self.highscoreFont = pygame.font.Font('fonts//font.ttf', 30)
        self.scoreText = self.highscoreFont.render('HIGHSCORE ' + str(score), True, self.ORANGE, self.WHITE)
        self.scoreRect = self.scoreText.get_rect()
        self.scoreRect.centerx = self.screen.get_rect().centerx
        self.scoreRect.centery = self.screen.get_rect().centery + 200

        #Blit text to screen
        self.screen.blit(self.title, self.titleRect)
        self.screen.blit(self.scoreText, self.scoreRect)

        clicked = self.buttons.startButton(clicked)
        return clicked
