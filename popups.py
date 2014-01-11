#The Popups() class
#By Tyler Spadgenske

import pygame, sys
from pygame.locals import *
#Import custom classes
from button import Button

pygame.init()

class Popups(object, Button):
    def __init__(self):
        self.windowSurface = pygame.display.set_mode((300, 350), 0, 32)
        pygame.display.set_caption('GAME OVER')
        self.mainClock = pygame.time.Clock()

        self.WHITE = (255, 255, 255)
        self.ORANGE = (255, 103, 1)
        
        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render('GAME OVER', True, self.ORANGE, self.WHITE)
        self.textRect = self.text.get_rect()
        self.textRect.centerx = self.windowSurface.get_rect().centerx
        self.textRect.centery = self.windowSurface.get_rect().centery - 150
        self.location = [200, 300]
        self.enlarge_reload = False
        self.reload = False
        self.backLocation = [100, 300]
        self.enlarge_back = False
        self.enlarge_sound = False
        self.enlarge_pause = False
        self.back = False
        
    def alert(self):
        pass
    
    def endgame(self):
        while True:
            self.tacoImage = pygame.image.load('Characters\\blownUp.gif')

            #Initialize reload image rect
            self.tacoRect = self.tacoImage.get_rect()
            self.tacoRect.centerx = 190
            self.tacoRect.centery = 185
            self.tacoImageBIG = pygame.transform.scale(self.tacoImage, (150, 150))

            self.windowSurface.blit(self.tacoImageBIG, self.tacoRect)
            self.windowSurface.blit(self.text, self.textRect)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.mainClock.tick()

            self.windowSurface.fill(self.WHITE)
            self.reload = Button.roundButton(self, event, 'reload', self.location)
            self.back = Button.roundButton(self, event, 'back', self.backLocation)
            if self.reload or self.back:
                break
            
        pygame.quit()   
        return self.reload, self.back
        
test = Popups()
test.endgame()


  
