#The Popups() class
#By Tyler Spadgenske

import pygame, sys
from pygame.locals import *
#Import custom classes
from button import Button

pygame.init()

class Popups(object, Button):
    def __init__(self, window):
        self.window = window
        self.mainClock = pygame.time.Clock()

        self.WHITE = (255, 255, 255)
        self.ORANGE = (255, 103, 1)
        
        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render('GAME OVER', True, self.ORANGE, self.WHITE)
        self.textRect = self.text.get_rect()
        self.textRect.centerx = self.window.get_rect().centerx
        self.textRect.centery = self.window.get_rect().centery - 150
        self.location = [550, 365]
        self.enlarge_reload = False
        self.reload = False
        self.backLocation = [660, 365]
        self.enlarge_back = False
        self.enlarge_sound = False
        self.enlarge_pause = False
        self.back = False

        self.buttons = Button(self.window)
        
    def alert(self):
        pass
    
    def endgame(self):
        while True:
            self.tacoImage = pygame.image.load('Characters\\blownUp.gif')
            block = {'rect':pygame.Rect(475, 115, 250, 300),'color':self.WHITE}
            pygame.draw.rect(self.window, block['color'], block['rect'])
            #Initialize reload image rect
            self.tacoRect = self.tacoImage.get_rect()
            self.tacoRect.centerx = self.window.get_rect().centerx + 50
            self.tacoRect.centery = self.window.get_rect().centery
            self.tacoImageBIG = pygame.transform.scale(self.tacoImage, (150, 150))

            self.reload = self.buttons.roundButton( None, 'reload', self.location)
            self.back = self.buttons.roundButton( None, 'back', self.backLocation)
                
            self.window.blit(self.tacoImageBIG, self.tacoRect)
            self.window.blit(self.text, self.textRect)
            for event in pygame.event.get():
                self.reload = self.buttons.roundButton( event, 'reload', self.location)
                self.back = self.buttons.roundButton( event, 'back', self.backLocation)

            pygame.display.update()
            self.mainClock.tick()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.back = True
                    
            if self.reload or self.back:
                break
    
        return self.reload, self.back
