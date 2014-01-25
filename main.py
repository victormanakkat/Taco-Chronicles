# main.py
# By Tyler Spadgenske
VERSION = '0.1.0'

import pygame, sys, os
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
from l1 import L1
from intro import Intro

#Setup the main screen display and clock
pygame.init()

os.environ ['SDL_VIDEO_WINDOW_POS'] = 'center'
WINDOWWIDTH = 1200
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('The Taco Chronicles v' + VERSION)
mainClock = pygame.time.Clock()

#Setup Colors
BLUE = (0,0,255)
SKY_BLUE = (0, 255, 255)

windowSurface.fill(SKY_BLUE)

#Setup game data
lockedGuns = {'9mm':False, 'shotgun':False, 'AK-47':False, 'bazooka':False, 'flamethrower':True}
lockedTools = {'crowbar':False, 'rope':True, 'key':True, 'TNT':True, 'jetpack':True}
sound = True
gameData = {'sound':sound, 'lockedGuns':lockedGuns, 'lockedTools':lockedTools}
restart = True

l1List = []
Intro(windowSurface)
for i in range(0, 19):
    l1List.append(L1(windowSurface, mainClock, SKY_BLUE, gameData))


#Run the gameplay
for i in l1List:
    restart = i.play()
    if restart == False:
        break

