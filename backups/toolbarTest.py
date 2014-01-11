#Toolbar for Taco Chronicles
#By Tyler Spadgenske

import pygame, sys, time
from pygame.locals import *
#Button, selectTool, and selectGun are custom classes
import button, selectGun, selectTool

pygame.init()

WINDOWWIDTH = 1200
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Creating the Toolbar class (Version 0.0.1)')
mainClock = pygame.time.Clock()

WHITE = (255, 255, 255)
windowSurface.fill(WHITE)

currentWeapon = '9mm'
currentTool = 'crowbar'
dropDownGun = False
dropDownTool = False
lockedGuns = {'9mm':False, 'shotgun':True, 'AK-47':True, 'bazooka':True, 'flamethrower':True}
lockedTools = {'crowbar':False, 'rope':True, 'key':True, 'TNT':True, 'jetpack':True}
score = 0
ammo = 15
hit = False

gunButtonCoords = [695, 30, 735, 30, 715, 50]
toolButtonCoords = [395, 30, 435, 30, 415, 50]
class Toolbar():
    def __init__(self, lockedGuns):
        self.ORANGE = (255, 103, 1)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (71, 213, 15)
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        
        self.gunClicked = 0
        self.lockedGuns = lockedGuns
        self.scoreSize = 80
        self.weaponType = 'Ammo: '
        
        self.healthBarColor = self.GREEN
        self.healthBarLength = 200

        #Initialize main bar
        self.upperBar = {'rect':pygame.Rect(0, 0, 1200, 75),'color':self.ORANGE}
        self.lowerBar = {'rect':pygame.Rect(0, 525, 1200, 75),'color':self.ORANGE}

    def countScore(self, score):
        score = str(score)
        self.scoreLength = len(score)
        if self.scoreLength == 6:
            self.scoreSize = 70
        self.scoreFont = pygame.font.SysFont(None, self.scoreSize)
        self.scoreText = self.scoreFont.render(score, True, self.WHITE, self.ORANGE)
        self.scoreRect = self.scoreText.get_rect()
        self.scoreRect[0] = 100
        windowSurface.blit(self.scoreText, self.scoreRect)
        
    def health(self, hit):
        if hit:
            self.healthBarLength -= 10
        if self.healthBarLength < 50:
            self.healthBarColor = self.RED
        if self.healthBarLength < 0:
            self.healthBarLength = 0
        
        self.healthBar = {'rect':pygame.Rect(900, 10, self.healthBarLength, 20),'color':self.healthBarColor}
        pygame.draw.rect(windowSurface, self.healthBar['color'], self.healthBar['rect'])

        self.healthFont = pygame.font.SysFont(None, 24)
        self.healthText = self.healthFont.render('Health', True, self.WHITE, self.ORANGE)
        self.healthRect = self.healthText.get_rect()
        self.healthRect[0] = 900
        self.healthRect[1] = 40
        windowSurface.blit(self.healthText, self.healthRect)
        


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
        windowSurface.blit(self.ammoText, self.ammoRect)
    
    def messageBox(self, message):
        self.messageFont = pygame.font.SysFont(None, 48)
        self.messageText = self.messageFont.render(message, True, self.WHITE, self.ORANGE)
        self.messageRect = self.messageText.get_rect()
        self.messageRect.centerx = windowSurface.get_rect().centerx
        self.messageRect[1] = 550
        windowSurface.blit(self.messageText, self.messageRect)
        
    def display(self):
        pygame.draw.rect(windowSurface, self.upperBar['color'], self.upperBar['rect'])
        pygame.draw.rect(windowSurface, self.lowerBar['color'], self.lowerBar['rect'])

toolBar = Toolbar(lockedGuns)
gunMenu = selectGun.selectGunMenu(lockedGuns)
toolMenu = selectTool.selectToolMenu(lockedTools)
gunArrowButton = button.Button()
toolArrowButton = button.Button()
while True:
    toolBar.display()
    
    toolBar.messageBox('This is the Message Box.')
    toolBar.countScore(score)
    toolBar.countAmmo(ammo, currentWeapon)
    toolBar.health(hit)
    
    dropDownGun, currentWeapon = gunMenu.chooseGun(windowSurface, dropDownGun, currentWeapon)
    dropDownTool, currentTool = toolMenu.chooseTool(windowSurface, dropDownTool, currentTool)
    
    gunArrowButton.blitArrow(windowSurface, dropDownGun, gunButtonCoords)
    toolArrowButton.blitArrow(windowSurface, dropDownTool, toolButtonCoords)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        dropDownGun = gunArrowButton.arrow(dropDownGun, event, gunButtonCoords)
        dropDownTool = toolArrowButton.arrow(dropDownTool, event, toolButtonCoords)
        if dropDownGun:
            currentWeapon = gunMenu.selectGunButton(currentWeapon, event)
        if dropDownTool:
            currentTool = toolMenu.selectToolButton(currentTool, event)
        if event.type == KEYDOWN:
            if event.key == K_SPACE: 
                hit = True
        if event.type == KEYUP:
            hit = False
            
            
    pygame.display.update()
    mainClock.tick()
    windowSurface.fill(WHITE)
    
  
