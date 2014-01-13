# main.py
# By Tyler Spadgenske
VERSION = '0.1.0'
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
from l1 import L1

pygame.init()

WINDOWWIDTH = 1200
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Creating the Level 1 class v' + VERSION)
mainClock = pygame.time.Clock()

BLUE = (0,0,255)
SKY_BLUE = (0, 255, 255)

windowSurface.fill(SKY_BLUE)

level1 = L1(windowSurface, mainClock, SKY_BLUE)
level1.play()
