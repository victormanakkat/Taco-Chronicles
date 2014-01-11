#Creating the level 2 class
#By Tyler Spadgenske
VERSION = '0.1.0'
print 'Loading...'
import pygame, sys
from pygame.locals import *
#Import custom classes
from background import Level_2
from toolbar import Toolbar
from button import Button
from person import Person
from selectGun import selectGunMenu
from selectTool import selectToolMenu

#Initalize pygame and setup screen
pygame.init()

WINDOWWIDTH = 1200
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Creating the Level 2 class v' + VERSION)
mainClock = pygame.time.Clock()

BLUE = (0,0,255)
SKY_BLUE = (0, 255, 255)

windowSurface.fill(SKY_BLUE)


#Set all variables
lockedGuns = {'9mm':False, 'shotgun':True, 'AK-47':True, 'bazooka':True, 'flamethrower':True}
lockedTools = {'crowbar':False, 'rope':True, 'key':True, 'TNT':True, 'jetpack':True}
moveRight = False
moveLeft = False
shootBullet = False
rectList = []
centered = False
officerX = 1500
officerGunX = {'right':abs(officerX) + 45, 'left':officerX + 7}
takeStep = 0
direction = 1
shootBullet = False
hit = False
ammo = 15
message = 'Get those cops Dr. Taco!'
score = 0
drop = False
sound = True
goUp = None
currentWeapon = '9mm'
currentTool = 'crowbar'
dropDownGun = False
dropDownTool = False
paused = False
gunButtonCoords = [695, 30, 735, 30, 715, 50]
toolButtonCoords = [395, 30, 435, 30, 415, 50]

#Setup all objects
level2 = Level_2(windowSurface)
tools = Toolbar(lockedGuns, windowSurface)
DrTaco = Person('Doctor Taco', windowSurface, officerX, officerGunX)
cop = Person('officer', windowSurface, officerX, officerGunX)
gunMenu = selectGunMenu(lockedGuns)
toolMenu = selectToolMenu(lockedTools)
gunButton = Button(windowSurface)
toolButton = Button(windowSurface)

print 'Loading Complete'
while True:
    #Blit the buildings to the background through the Level_2 object
    level2.blitBackground(moveRight, moveLeft, rectList, centered)

    #Add the tools to the screen
    tools.display()
    tools.messageBox(message)
    tools.countScore(score)
    tools.countAmmo(ammo, currentWeapon)
    sound, paused = tools.addButtons(sound, None)
    hit = tools.health(hit)
    
    for event in pygame.event.get():
        #Add standard buttons to bottom of screen
        sound, paused = tools.addButtons(sound, event)

        #Add arrow buttons for select gun and tool menus
        dropDownGun = gunButton.arrow(dropDownGun, event, gunButtonCoords)
        dropDownTool = toolButton.arrow(dropDownTool, event, toolButtonCoords)
        if dropDownGun:
            currentWeapon = gunMenu.selectGunButton(currentWeapon, event)
        if dropDownTool:
            currentTool = toolMenu.selectToolButton(currentTool, event)

        #look for quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            #Change direction based on key pressed
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
        #Stop movement if no key pressed
        if event.type == KEYUP:
            moveRight = False
            moveLeft = False
            shootBullet = False
        
    #Call Dr Taco's walk, shootPistol, and jump functions
    takeStep, centered = DrTaco.walk(takeStep, direction, moveLeft, moveRight, officerX)
    shootBullet, hit, ammo, message, score, officerX, drop = DrTaco.shootPistol(shootBullet, hit, direction, officerGunX, sound, cop.get_rect(), ammo, message, score)
    goUp = DrTaco.jump(goUp)

    #Blit the tool and gun menus
    dropDownGun, currentWeapon = gunMenu.chooseGun(windowSurface, dropDownGun, currentWeapon)
    dropDownTool, currentTool = toolMenu.chooseTool(windowSurface, dropDownTool, currentTool)
    gunButton.blitArrow(windowSurface, dropDownGun, gunButtonCoords)
    toolButton.blitArrow(windowSurface, dropDownTool, toolButtonCoords)

    #Update and fill screen   
    pygame.display.update()
    windowSurface.fill(SKY_BLUE)
    mainClock.tick()
  
