#Creating the level 1 class
#By Tyler Spadgenske
import pygame, sys, random
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
from popups import Popups

class L1(object):
    def __init__(self, windowSurface, mainClock, SKY_BLUE, gameData, showFPS):

        #Create game data
        self.lockedGuns = gameData['lockedGuns']
        self.lockedTools = gameData['lockedTools']
        self.sound = gameData['sound']
        self.runGame = True
        self.showFPS = showFPS

        #Setup theme music
        pygame.mixer.music.load('sound//gameTheme.mp3')

        #Constants
        self.BPS = 8 #(Bullets Per Second)
        self.TOTAL_SUPPLIES = 12 #Total Supplies for each powerup
        self.SKY_BLUE = SKY_BLUE #Sky color
        self.TOTAL_COPS = 32 #Total number of all cops in level
        #Variables
        self.windowSurface = windowSurface
        self.clock = mainClock
        #Setup Dr. Taco's Direction
        self.moveRight = False
        self.moveLeft = False
        #Set Start Weapon and tool, and make sure menus are closed.
        self.currentWeapon = '9mm'
        self.currentTool = 'crowbar'
        self.dropDownGun = False
        self.dropDownTool = False
        #Set Basic Values
        self.score = 0
        self.ammo = 30
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
        self.lifeLeft = 0
        self.endPoint = 0
        self.back = False
        self.tacosCollected = 0
        self.first = True

        #Initialize Objects
        self.level_1 = Level_1(self.windowSurface)
        self.tools = Toolbar(self.lockedGuns, self.windowSurface)
        self.gunMenu = selectGunMenu(self.lockedGuns)
        self.toolMenu = selectToolMenu(self.lockedTools)
        self.gunArrowButton = Button(self.windowSurface)
        self.toolArrowButton = Button(self.windowSurface)
        self.DrTaco = Person('Doctor Taco', self.windowSurface, self.officerX, self.officerGunX)
        
        self.wingame = Popups(self.windowSurface)

        #Default lists
        self.copList = []
        self.Xlist = []
        self.num = 700
        #Add a cop every 250 pixels for the range in TOTAL_COPS
        for i in range(0, self.TOTAL_COPS):
            self.Xlist.append(self.num)
            self.num += 250
        self.num = 0

        #Add the cop object
        self.index = 0
        for cop in range(0, self.TOTAL_COPS):
            self.copList.append(AI(self.windowSurface, self.skill_level, self.Xlist[self.index]))
            self.index += 1

        #Add the cops gun
        self.index = 0
        for i in range(0, self.TOTAL_COPS):
            self.gunXlist.append({'right':abs(self.Xlist[self.index]) + 45, 'left':self.Xlist[self.index] + 7})
            self.index += 1

        #Add Supplies to random locations
        self.healthX = []
        self.tacosX = []
        self.tacosY = []
        self.ammoX = []
        self.ammoBoxes = []
        self.healthBoxes = []
        self.tacos = []
        for i in range(0, self.TOTAL_SUPPLIES):
            self.ammoBoxes.append(Powerups(self.windowSurface, self.score))
            self.healthBoxes.append(Powerups(self.windowSurface, self.score))
            for i in range(0, 2):
                self.tacos.append(Powerups(self.windowSurface, self.score))
                self.tacosX.append(random.randint(300, 9000))
                self.tacosY.append(random.randint(300, 490))
            self.healthX.append(random.randint(300, 9000))
            self.ammoX.append(random.randint(300, 9000))

    def play(self):
        #If there is no quit event, (i.e reload or back)
        while self.runGame == True:
            #Setup rect list and blit background
            self.reload = False
            self.ammoX, self.healthX, self.tacosX, self.endPoint = self.level_1.blitBackground(self.moveRight, self.moveLeft, self.ammoX,
                                                                                               self.healthX, self.tacosX, self.copList, self.centered)
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

            #Add Health bar, score, message box, buttons, and ammo text to screen
            self.tools.display()
            self.tools.messageBox(self.message)
            self.tools.countScore(self.score)
            self.tools.countAmmo(self.ammo, self.currentWeapon)
            self.sound, self.paused, self.reaload = self.tools.addButtons(self.sound, None)
            self.tools.health(self.lifeLeft)

            #Blit select gun menu, select tool menu, and drop down arrows to screen and allow user to select weapon (or gun)
            self.dropDownGun, self.currentWeapon = self.gunMenu.chooseGun(self.windowSurface, self.dropDownGun, self.currentWeapon)
            self.dropDownTool, self.currentTool = self.toolMenu.chooseTool(self.windowSurface, self.dropDownTool, self.currentTool)    
            self.gunArrowButton.blitArrow(self.windowSurface, self.dropDownGun, self.gunButtonCoords)
            self.toolArrowButton.blitArrow(self.windowSurface, self.dropDownTool, self.toolButtonCoords)

            #Get Frames per second and and it to screen
            self.fps = int(self.clock.get_fps())
            self.tools.FPS(self.fps, self.showFPS)

            #If game is not paused, let Dr. Taco walk, jump, and shoot selected weapon
            if self.paused != True:
                #Make it so Dr. Taco can jump and move
                self.takeStep, self.centered = self.DrTaco.walk(self.takeStep, self.direction, self.moveLeft, self.moveRight, self.currentWeapon)
                self.goUp = self.DrTaco.jump(self.goUp)
                #If weapon is the Pistol, put it in Dr. Taco's hand and enable it for use.
                if self.currentWeapon == '9mm':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val, self.lifeLeft = self.DrTaco.shootPistol(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score,
                        lifeLeft = self.lifeLeft)
                #If weapon is the Shotgun, put it in Dr. Taco's hand and enable it for use.
                if self.currentWeapon == 'shotgun':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val, self.lifeLeft = self.DrTaco.shootShotgun(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score,
                        lifeLeft = self.lifeLeft)
                #If weapon is the AK-47, put it in Dr. Taco's hand and enable it for use.
                if self.currentWeapon == 'AK-47':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val, self.lifeLeft = self.DrTaco.shootAK(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score,
                        lifeLeft = self.lifeLeft)
                    self.shootBullet = False
                #If weapon is the bazooka, put it in Dr. Taco's hand and enable it for use.
                if self.currentWeapon == 'bazooka':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val, self.lifeLeft = self.DrTaco.shootBazooka(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score,
                        self.currentWeapon, lifeLeft = self.lifeLeft)
                #If weapon is the flamethrower, put it in Dr. Taco's hand and enable it for use.
                if self.currentWeapon == 'flamethrower':
                    self.shootBullet, self.hit, self.ammo, self.message, self.score, self.officerX, self.drop, self.val, self.lifeLeft = self.DrTaco.shootFlame(
                        self.shootBullet, self.hit, self.direction, self.officerGunX, self.sound, self.copList, self.ammo, self.message, self.score,
                        self.currentWeapon, self.lifeLeft)
                

                #Make all the cops think
                self.index = 0
                for cop in self.copList:                
                    self.hit, self.endReload, self.lifeLeft = cop.think(self.DrTaco.get_rect(), self.copList[self.index].get_rect()[0], self.gunXlist[self.index],
                                                         self.drop, self.hit, self.sound, self.lifeLeft)
                    #If Dr. Taco is dead break out of loop
                    if self.endReload:
                        break
                    self.index += 1

            #Blit all the supplies to the screen by running their functions
            self.index = 0
            for box in self.ammoBoxes:
                self.score, self.ammo = box.ammoBox(self.ammoX[self.index], 490, self.DrTaco.get_rect(), self.ammo, self.score, self.sound)
                self.index += 1
            self.index = 0
            for box in self.healthBoxes:
                self.score, self.lifeLeft = box.healthBox(self.healthX[self.index], 490, self.DrTaco.get_rect(), self.lifeLeft, self.sound, self.score)
                self.index += 1
            self.index = 0
            for box in self.tacos:
                self.score, self.tacosCollected = box.taco(self.tacosX[self.index], self.tacosY[self.index],
                                                           self.DrTaco.get_rect(), self.sound, self.score, self.tacosCollected)
                self.index += 1

            #If Dr. Taco has reached the end of the level, display level completed popup and exit loop
            if self.endPoint < 298:
                self.endReload, self.back = self.wingame.wingame(self.score, self.tacosCollected)
            #If the health bar length is too much set it to right size
            if self.lifeLeft >= 20:
                self.lifeLeft = 20

            #Update screen and fill background
            pygame.display.update()
            self.clock.tick()
            self.windowSurface.fill(self.SKY_BLUE)

            #If reload button is clicked exit loop and enter another object
            if self.endReload:
                pygame.mixer.music.stop()
                self.runGame = False
                self.reload = True
            if self.reload:
                pygame.mixer.music.stop()
                self.runGame = False

            #Play music
            if self.sound == True:
                if self.first:
                    pygame.mixer.music.play(-1, 0.0)
                    self.first = False
            else:
                pygame.mixer.music.stop()
                self.first = True
        return self.reload
