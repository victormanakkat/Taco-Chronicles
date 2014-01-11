#Creating the level 1 class
#By Tyler Spadgenske
print 'Loading...'
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

pygame.init()

WINDOWWIDTH = 1200
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Creating the Level 1 class (Version 0.0.1)')
mainClock = pygame.time.Clock()

BLUE = (0,0,255)
SKY_BLUE = (0, 255, 255)

windowSurface.fill(SKY_BLUE)

#Variables
moveRight = False
moveLeft = False
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
officerX = 1500
officerGunX = {'right':abs(officerX) + 45, 'left':officerX + 7}
takeStep = 0
direction = 1
goUp = None
shootBullet = False
message = 'This is the Message Box.'
skill_level = 800
centered = False
drop = False
sound = True
paused = False

#Objects
level_1 = Level_1(windowSurface)
toolBar = Toolbar(lockedGuns, windowSurface)
gunMenu = selectGunMenu(lockedGuns)
toolMenu = selectToolMenu(lockedTools)
gunArrowButton = Button(windowSurface)
toolArrowButton = Button(windowSurface)
DrTaco = Person('Doctor Taco', windowSurface, officerX, officerGunX)
ammoBoxes = Powerups(windowSurface, score)
ammoBoxCoords = [600, 490]
cop = AI(windowSurface, skill_level, officerX)

print 'Loading Complete'
while True:
    rectList = [ammoBoxCoords, cop.get_rect(), cop.get_gun_rect()]
    rectList = level_1.blitBackground(moveRight, moveLeft, rectList, centered)
    officerGunX = {'right':rectList[1][0] + 45, 'left':rectList[1][0] + 7}
    for event in pygame.event.get():
        sound, paused = toolBar.addButtons(sound, event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direction = 1
                moveRight = True 
                moveLeft = False
            if event.key == K_LEFT:
                direction = 0
                moveLeft = True
                moveRight = False
            if event.key == K_UP:
                goUp = True
            if event.key == K_SPACE:
                shootBullet = True
        if event.type == KEYUP:
            moveRight = False
            moveLeft = False
            shootBullet = False

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        dropDownGun = gunArrowButton.arrow(dropDownGun, event, gunButtonCoords)
        dropDownTool = toolArrowButton.arrow(dropDownTool, event, toolButtonCoords)
        if dropDownGun:
            currentWeapon = gunMenu.selectGunButton(currentWeapon, event)
        if dropDownTool:
            currentTool = toolMenu.selectToolButton(currentTool, event)
            
    toolBar.display()
    
    toolBar.messageBox(message)
    toolBar.countScore(score)
    toolBar.countAmmo(ammo, currentWeapon)
    sound, paused = toolBar.addButtons(sound, None)
    hit = toolBar.health(hit)
    
    dropDownGun, currentWeapon = gunMenu.chooseGun(windowSurface, dropDownGun, currentWeapon)
    dropDownTool, currentTool = toolMenu.chooseTool(windowSurface, dropDownTool, currentTool)    
    gunArrowButton.blitArrow(windowSurface, dropDownGun, gunButtonCoords)
    toolArrowButton.blitArrow(windowSurface, dropDownTool, toolButtonCoords)

    if paused != True:
        takeStep, centered = DrTaco.walk(takeStep, direction, moveLeft, moveRight, officerX)
        goUp = DrTaco.jump(goUp)
        shootBullet, hit, ammo, message, score, officerX, drop = DrTaco.shootPistol(shootBullet, hit, direction, officerGunX, sound, cop.get_rect(), ammo, message, score)

        score, ammo = ammoBoxes.ammoBox(ammoBoxCoords[0], ammoBoxCoords[1], DrTaco.get_rect(), ammo, score, sound)

        hit = cop.think(DrTaco.get_rect(), cop.get_rect()[0], officerGunX, drop, hit, sound)
    
    pygame.display.update()
    mainClock.tick()
    windowSurface.fill(SKY_BLUE)
