#Creating the level 1 class
#By Tyler Spadgenske
import pygame, sys
from pygame.locals import *

#import custom classes
import background, button, toolbar, selectGun, selectTool, person, powerups, baddieAI
from background import Level_1
from button import Button
from toolbar import Toolbar
from selectGun import selectGunMenu
from selectTool import selectToolMenu
from person import Person
from powerups import Powerups
from baddieAI import AI

class L1(object):
    def __init__(self, windowSurface, mainClock, SKY_BLUE, gameData):

        #Create game data
        self.TOTAL_COPS = 10
        self.lockedGuns = gameData['lockedGuns']
        self.lockedTools = gameData['lockedTools']
        self.sound = gameData['sound']
        self.runGame = True

        #Constants
        self.BPS = 8 #(Bullets Per Second)
        #Variables
        self.windowSurface = windowSurface
        self.clock = mainClock
        self.SKY_BLUE = SKY_BLUE
        self.moveRight = False
        self.moveLeft = False
        self.currentWeapon = '9mm'
        self.currentTool = 'crowbar'
        self.dropDownGun = False
        self.dropDownTool = False
        self.score = 0
        self.ammo = 15
        self.hit = False
        self.gunButtonCoords = [695, 30, 735, 30, 715, 50]
        self.toolButtonCoords = [395, 30, 435, 30, 415, 50]
        self.officerX = 1500
        self.officerGunX = {'right':abs(self.officerX) + 45, 'left':self.officerX + 7}
        self.gunXlist = []
        self.takeStep = 0
        self.direction = 1
        self.goUp = None
        self.shootBullet = False
        self.message = 'This is the Message Box.'
        self.skill_level = 800
        self.centered = False
        self.drop = False
        self.paused = False
        self.reload = False
        self.endReload = False
        self.endBack = False
        self.die = False
        self.val = None
        self.rapidFire = [0, False]

        #Initialize Objects
        self.level_1 = Level_1(self.windowSurface)
        self.tools = Toolbar(self.lockedGuns, self.windowSurface)
        self.gunMenu = selectGunMenu(self.lockedGuns)
        self.toolMenu = selectToolMenu(self.lockedTools)
        self.gunArrowButton = Button(self.windowSurface)
        self.toolArrowButton = Button(self.windowSurface)
        self.DrTaco = Person('Doctor Taco', self.windowSurface, self.officerX, self.officerGunX)
        self.ammoBoxes = Powerups(self.windowSurface, self.score)
        self.ammoBoxCoords = [600, 490]
        self.copList = []
        self.Xlist = [1000, 600, 1200, 1800, 2400, 2800, 3400, 3700, 4000, 5000]
        self.index = 0
        for cop in range(0, self.TOTAL_COPS):
            self.copList.append(AI(self.windowSurface, self.skill_level, self.Xlist[self.index]))
            self.index += 1

        self.index = 0
        for i in range(0, self.TOTAL_COPS):
            self.gunXlist.append({'right':abs(self.Xlist[self.index]) + 45, 'left':self.Xlist[self.index] + 7})
            self.index += 1

    def play(self):
        #If there is no quit event, (i.e reload or back)
        while self.runGame == True:
            #Setup rect list and blit background
            self.reload = False
            self.rectList = [self.ammoBoxCoords]
            self.rectList = self.level_1.blitBackground(self.moveRight, self.moveLeft, self.rectList, self.copList, self.centered)

            #Setup all the cops gun position.
            self.index = 0
            for cop in self.copList:
                self.gunXlist[self.index] = {'right':self.copList[self.index].get_rect()[0] + 45, 'left':self.copList[self.index].get_rect()[0] + 7}
                self.index += 1
                
            for event in pygame.event.get():
                self.sound, self.paused, self.reload = self.tools.addButtons(self.sound, event)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.direction = 1
                        self.moveRight = True 
                        self.moveLeft = False
                    if event.key == K_LEFT:
                        self.direction = 0
                        self.moveLeft = True
                        self.moveRight = False
                    if event.key == K_UP:
                        self.goUp = True
                    if event.key == K_SPACE:
                        self.shootBullet = True
                        self.rapidFire[1] = True
                if event.type == KEYUP:
                    self.moveRight = False
                    self.moveLeft = False
                    self.shootBullet = False
                    self.rapidFire[1] = False
                    if self.currentWeapon == 'flamethrower':
                        self.shootBullet =  False

                self.dropDownGun = self.gunArrowButton.arrow(self.dropDownGun, event, self.gunButtonCoords)
                self.dropDownTool = self.toolArrowButton.arrow(self.dropDownTool, event, self.toolButtonCoords)
                if self.dropDownGun:
                    self.currentWeapon = self.gunMenu.selectGunButton(self.currentWeapon, event)
                if self.dropDownTool:
                    self.currentTool = self.toolMenu.selectToolButton(self.currentTool, event)

            self.rapidFire[0] += 1
            if self.rapidFire[0] == self.BPS:
                self.rapidFire[0] = 0
                if self.rapidFire[1]:
                    if self.currentWeapon == 'AK-47':
                        self.shootBullet = True
            
            self.tools.display()
    
            self.tools.messageBox(self.message)
            self.tools.countScore(self.score)
            self.tools.countAmmo(self.ammo, self.currentWeapon)
            self.sound, self.paused, self.reaload = self.tools.addButtons(self.sound, None)
            self.hit = self.tools.health(self.hit)
    
            self.dropDownGun, self.currentWeapon = self.gunMenu.chooseGun(self.windowSurface, self.dropDownGun, self.currentWeapon)
            self.dropDownTool, self.currentTool = self.toolMenu.chooseTool(self.windowSurface, self.dropDownTool, self.currentTool)    
            self.gunArrowButton.blitArrow(self.windowSurface, self.dropDownGun, self.gunButtonCoords)
            self.toolArrowButton.blitArrow(self.windowSurface, self.dropDownTool, self.toolButtonCoords)

            if self.paused != True:
                self.takeStep, self.centered = self.DrTaco.walk(self.takeStep, self.direction, self.moveLeft, self.moveRight, self.currentWeapon)
                self.goUp = self.DrTaco.jump(self.goUp)
                if self.currentWeapon == '9mm':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val = self.DrTaco.shootPistol(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score)
                if self.currentWeapon == 'shotgun':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val = self.DrTaco.shootShotgun(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score)
                if self.currentWeapon == 'AK-47':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val = self.DrTaco.shootAK(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score)
                    self.shootBullet = False
                if self.currentWeapon == 'bazooka':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val = self.DrTaco.shootBazooka(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score,
                        self.currentWeapon)
                if self.currentWeapon == 'flamethrower':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val = self.DrTaco.shootFlame(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score,
                        self.currentWeapon)
                    

                self.score, self.ammo = self.ammoBoxes.ammoBox(self.ammoBoxCoords[0], self.ammoBoxCoords[1], self.DrTaco.get_rect(),
                                                                self.ammo, self.score, self.sound)

                self.index = 0
                for cop in self.copList:                
                    self.hit, self.endReload = cop.think(self.DrTaco.get_rect(), self.copList[self.index].get_rect()[0], self.gunXlist[self.index],
                                                         self.drop, self.hit, self.sound)
                    self.index += 1

            pygame.display.update()
            self.clock.tick()
            self.windowSurface.fill(self.SKY_BLUE)
            if self.endReload:
                self.runGame = False
                self.reload = True
            if self.reload:
                self.runGame = False

        return self.reload

