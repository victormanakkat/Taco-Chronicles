#Toolbar for Taco Chronicles
#By Tyler Spadgenske

import pygame, sys, time
from pygame.locals import *
#Button, selectTool, and selectGun are custom classes
import button, selectGun, selectTool
from button import Button

pygame.init()

class Toolbar(Button):
    def __init__(self, lockedGuns, surface):
        self.ORANGE = (255, 103, 1)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (71, 213, 15)
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)

        self.windowSurface = surface
        
        self.gunClicked = 0
        self.lockedGuns = lockedGuns
        self.scoreSize = 80
        self.weaponType = 'Ammo: '
        
        self.healthBarColor = self.GREEN
        self.healthBarLength = 200

        #Initialize main bar
        self.upperBar = {'rect':pygame.Rect(0, 0, 1200, 75),'color':self.ORANGE}
        self.lowerBar = {'rect':pygame.Rect(0, 525, 1200, 75),'color':self.ORANGE}

        self.reload = False
        self.sound = False
        self.pause = False
        self.back = False
        self.soundIcon = 'sound on'
        self.paused = False
        Button.__init__(self, self.windowSurface)

    def countScore(self, score):
        score = str(score)
        self.scoreLength = len(score)
        if self.scoreLength == 6:
            self.scoreSize = 70
        self.scoreFont = pygame.font.SysFont(None, self.scoreSize)
        self.scoreText = self.scoreFont.render(score, True, self.WHITE, self.ORANGE)
        self.scoreRect = self.scoreText.get_rect()
        self.scoreRect[0] = 100
        self.windowSurface.blit(self.scoreText, self.scoreRect)
        
    def health(self, lifeLeft):
        #Set health bar length
        if lifeLeft == 1:
            self.healthBarLength = 190
        if lifeLeft == 2:
            self.healthBarLength = 180
        if lifeLeft == 3:
            self.healthBarLength = 170
        if lifeLeft == 4:
            self.healthBarLength = 160
        if lifeLeft == 5:
            self.healthBarLength = 150
        if lifeLeft == 6:
            self.healthBarLength = 140
        if lifeLeft == 7:
            self.healthBarLength = 130
        if lifeLeft == 8:
            self.healthBarLength = 120
        if lifeLeft == 9:
            self.healthBarLength = 110
        if lifeLeft == 10:
            self.healthBarLength = 100
        if lifeLeft == 11:
            self.healthBarLength = 90
        if lifeLeft == 12:
            self.healthBarLength = 80
        if lifeLeft == 13:
            self.healthBarLength = 70
        if lifeLeft == 14:
            self.healthBarLength = 60
        if lifeLeft == 15:
            self.healthBarLength = 50
        if lifeLeft == 16:
            self.healthBarLength = 40
        if lifeLeft == 17:
            self.healthBarLength = 30
        if lifeLeft == 18:
            self.healthBarLength = 20
        if lifeLeft == 19:
            self.healthBarLength = 10
        if lifeLeft == 20:
            self.healthBarLength = 0
            
            
        if self.healthBarLength < 50:
            self.healthBarColor = self.RED
        if self.healthBarLength < 0:
            self.healthBarLength = 0

        self.healthBar = {'rect':pygame.Rect(900, 10, self.healthBarLength, 20),'color':self.healthBarColor}
        pygame.draw.rect(self.windowSurface, self.healthBar['color'], self.healthBar['rect'])

        self.healthFont = pygame.font.SysFont(None, 24)
        self.healthText = self.healthFont.render('Health', True, self.WHITE, self.ORANGE)
        self.healthRect = self.healthText.get_rect()
        self.healthRect[0] = 900
        self.healthRect[1] = 40
        self.windowSurface.blit(self.healthText, self.healthRect)
        
    def countAmmo(self, ammo, currentWeapon):
        ammo = str(ammo)      
        if currentWeapon == 'flamethrower':
            self.weaponType = 'Fuel: '
        else:
            self.weaponType = 'Ammo: '
            
        self.ammoFont = pygame.font.SysFont(None, 20)
        self.ammoText = self.ammoFont.render(self.weaponType + ammo, True, self.WHITE, self.ORANGE)
        self.ammoRect = self.ammoText.get_rect()
        self.ammoRect[0] = 100
        self.ammoRect[1] = 55
        self.windowSurface.blit(self.ammoText, self.ammoRect)
    
    def messageBox(self, message):
        self.messageFont = pygame.font.SysFont(None, 48)
        self.messageText = self.messageFont.render(message, True, self.WHITE, self.ORANGE)
        self.messageRect = self.messageText.get_rect()
        self.messageRect.centerx = self.windowSurface.get_rect().centerx
        self.messageRect[1] = 550
        self.windowSurface.blit(self.messageText, self.messageRect)
        
    def display(self):
        pygame.draw.rect(self.windowSurface, self.upperBar['color'], self.upperBar['rect'])
        pygame.draw.rect(self.windowSurface, self.lowerBar['color'], self.lowerBar['rect'])

    def pauseGame(self, paused, event):
        if paused:
            self.pauseText = self.messageFont.render('Game Paused', True, self.WHITE, self.ORANGE)
            self.pauseRect = self.pauseText.get_rect()
            self.pauseRect.centerx = self.windowSurface.get_rect().centerx
            self.pauseRect.centery = self.windowSurface.get_rect().centery
            self.windowSurface.blit(self.pauseText, self.pauseRect)

            if event != None:
                if event.type == KEYDOWN:
                    paused = False

        return paused
                        
    
    def addButtons(self, sound, event = None):
        self.reload = Button.roundButton(self, event, 'reload', [135, 562])
        self.back = Button.roundButton(self, event, 'back', [50, 562])
        self.pause = Button.roundButton(self, event, 'pause', [1150, 562])
        self.sound = Button.roundButton(self, event, self.soundIcon, [1060, 562])

        if self.pause:
            self.paused = True
    
        self.paused = self.pauseGame(self.paused, event)
        
        if self.sound:
            self.sound = False
            if sound:
                sound = False
                self.soundIcon = 'sound off'
            else:
                sound = True
                self.soundIcon = 'sound on'

        return sound, self.paused, self.reload
