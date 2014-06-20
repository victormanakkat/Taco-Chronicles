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
        
        self.font = pygame.font.Font('files\\font\\arial.ttf', 24)
        #Create "Level Complete!" Text.
        self.winText = self.font.render('Level Complete!', True, self.ORANGE, self.WHITE)
        self.winTextRect = self.winText.get_rect()
        self.winTextRect.centerx = self.window.get_rect().centerx + 7
        self.winTextRect.centery = self.window.get_rect().centery - 150

        #Create "GAME OVER" Text.
        self.text = self.font.render('GAME OVER', True, self.ORANGE, self.WHITE)
        self.textRect = self.text.get_rect()
        self.textRect.centerx = self.window.get_rect().centerx
        self.textRect.centery = self.window.get_rect().centery - 150

        #Create taco image
        self.tacoImageBIG = pygame.image.load('files\\powerups\\taco.png')
        self.tacoRect = self.tacoImageBIG.get_rect()
        self.tacoRect.centerx = self.window.get_rect().centerx 
        self.tacoRect.centery = self.window.get_rect().centery - 60
        self.tacoImage = pygame.transform.scale(self.tacoImageBIG, (50, 50))
        
        #Setup variables
        self.location = [550, 365]
        self.enlarge_reload = False
        self.reload = False
        self.backLocation = [660, 365]
        self.enlarge_back = False
        self.enlarge_sound = False
        self.enlarge_pause = False
        self.back = False
        
        #Create button object
        self.buttons = Button(self.window)
        
    def alert(self):
        print "Alert Not complete."
    
    def endgame(self):
        while True:
            self.tacoImage = pygame.image.load('files\\Characters\\blownUp.gif')
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

    def wingame(self, score, tacosCollected):
        while True:
            #Draw the white box
            block = {'rect':pygame.Rect(475, 115, 270, 300),'color':self.WHITE}
            pygame.draw.rect(self.window, block['color'], block['rect'])

            #Add the buttons and blit text to screen
            self.reload = self.buttons.roundButton( None, 'reload', self.location)
            self.back = self.buttons.roundButton( None, 'back', self.backLocation, flip = True)
                
            self.window.blit(self.winText, self.winTextRect)
            for event in pygame.event.get():
                self.reload = self.buttons.roundButton( event, 'reload', self.location)
                self.back = self.buttons.roundButton( event, 'back', self.backLocation, flip = True)

            #Add the score text
            self.scoreText = self.font.render('Score: ' + str(score), True, self.ORANGE, self.WHITE)
            self.scoreTextRect = self.scoreText.get_rect()
            self.scoreTextRect.centerx = self.window.get_rect().centerx
            self.scoreTextRect.centery = self.window.get_rect().centery - 15
            self.window.blit(self.scoreText, self.scoreTextRect)

            #Add taco image
            self.window.blit(self.tacoImage, self.tacoRect)

            #Add the Taco's collected text.
            self.tacoText = self.font.render(' : ' + str(tacosCollected), True, self.ORANGE, self.WHITE)
            self.tacoTextRect = self.tacoText.get_rect()
            self.tacoTextRect.centerx = self.window.get_rect().centerx - 10
            self.tacoTextRect.centery = self.window.get_rect().centery - 95
            self.window.blit(self.tacoText, self.tacoTextRect)

            pygame.display.update()
            self.mainClock.tick()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.back = True
                    
            if self.reload or self.back:
                break
        
        
    
        return self.reload, self.back
