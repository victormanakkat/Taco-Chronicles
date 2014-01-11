#Creating the Gameplay class
#By Tyler Spadgenske

import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1200
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Creating the Gameplay class (Version 0.0.1)')
mainClock = pygame.time.Clock()
pygame.display.toggle_fullscreen()

BLUE = (0,0,255)
SKY_BLUE = (0, 255, 255)

block = {'rect':pygame.Rect(0, 0, 1200, 75),'color':BLUE}
block2 = {'rect':pygame.Rect(0, 525, 1200, 75),'color':BLUE}
windowSurface.fill(SKY_BLUE)
moveRight = False
moveLeft = False
class Background(object):
    def __init__():
        self.farLeft = True
    def move(self, buildings):
        if buildings[0][0] >= 250:
            self.farLeft = False
        else:
            self.farLeft = True
        if moveRight:
            for i in buildings:
                i[0] -= 2
        if moveLeft and self.farLeft:
            for i in buildings:
                i[0] += 2
                
    def complete():
        pass
class Level_1(Background):
    def __init__(self):
        #Setup Bannanabees Image
        self.bananaBeesImage = pygame.image.load('Buildings\\BananaBees.gif')
        self.bananaBeesRect = self.bananaBeesImage.get_rect()
        self.bananaBeesRect[0] = 250
        self.bananaBeesRect[1] = 225

        #Initialize Fire Station Image
        self.fireStationImage = pygame.image.load('Buildings\\FireStation.png')
        self.fireStationRect = self.fireStationImage.get_rect()
        self.fireStationRect[0] = 900
        self.fireStationRect[1] = 170

        #Initialize Apartment Images
        #Apt. 1
        self.apt1Image = pygame.image.load('Buildings\\Apt1.png')
        self.apt1Rect = self.apt1Image.get_rect()
        self.apt1Rect[0] = 2000
        self.apt1Rect[1] = -60

        #Apt. 2
        self.apt2Image = pygame.image.load('Buildings\\Apt2.png')
        self.apt2Rect = self.apt2Image.get_rect()
        self.apt2Rect[0] = 3000
        self.apt2Rect[1] = -60

        #Apt. 3
        self.apt3Image = pygame.image.load('Buildings\\Apt3.png')
        self.apt3Rect = self.apt3Image.get_rect()
        self.apt3Rect[0] = 4000
        self.apt3Rect[1] = -60

        #Apt. 4
        self.apt4Image = pygame.image.load('Buildings\\Apt4.png')
        self.apt4Rect = self.apt4Image.get_rect()
        self.apt4Rect[0] = 5000
        self.apt4Rect[1] = -60

        #Initialize TV LAND image
        self.TVLandImage = pygame.image.load('Buildings\\TV_LAND.png')
        self.TVLandRect = self.TVLandImage.get_rect()
        self.TVLandRect[0] = 6000
        self.TVLandRect[1] = 163

        #Initialize tree image
        self.treeImage = pygame.image.load('Buildings\\tree.gif')
        self.tree = pygame.transform.scale(self.treeImage, (500, 550))
        self.treeRect = self.treeImage.get_rect()
        self.treeRect[0] = 6750
        self.treeRect[1] = 0
        
        #Initialize Police Station image
        self.PoliceStationImage = pygame.image.load('Buildings\\PoliceStation.png')
        self.PoliceStationRect = self.PoliceStationImage.get_rect()
        self.PoliceStationRect[0] = 7200
        self.PoliceStationRect[1] = 165

        #Initialize Papa Con's Pizza image
        self.consPizzaImage = pygame.image.load('Buildings\\consPizza.png')
        self.consPizzaRect = self.consPizzaImage.get_rect()
        self.consPizzaRect[0] = 8200
        self.consPizzaRect[1] = 122

        #Initialize Taco Bell image
        self.TacoBellImage = pygame.image.load('Buildings\\TacoBell.png')
        self.TacoBellRect = self.TacoBellImage.get_rect()
        self.TacoBellRect[0] = 9200
        self.TacoBellRect[1] = 95
        
        self.L1Buildings = [self.bananaBeesRect, self.fireStationRect, self.apt1Rect, self.apt2Rect, self.apt3Rect,
                            self.apt4Rect, self.TVLandRect, self.PoliceStationRect, self.treeRect, self.consPizzaRect,
                            self.TacoBellRect]
                     
    def blitBackground(self):
        if self.bananaBeesRect[0] > -536:
            windowSurface.blit(self.bananaBeesImage, self.bananaBeesRect)
        if self.fireStationRect[0] > -995:
            windowSurface.blit(self.fireStationImage, self.fireStationRect)
        if self.apt1Rect[0] > -774:
            windowSurface.blit(self.apt1Image, self.apt1Rect)
        if self.apt2Rect[0] > -760:
            windowSurface.blit(self.apt2Image, self.apt2Rect)
        if self.apt3Rect[0] > -760:
            windowSurface.blit(self.apt3Image, self.apt3Rect)
        if self.apt4Rect[0] > -760:
            windowSurface.blit(self.apt4Image, self.apt4Rect)
        if self.TVLandRect[0] > -760:
            windowSurface.blit(self.TVLandImage, self.TVLandRect)
        if self.PoliceStationRect[0] > -900:
            windowSurface.blit(self.PoliceStationImage, self.PoliceStationRect)
        if self.treeRect[0] > -760:
            windowSurface.blit(self.tree, self.treeRect)
        if self.consPizzaRect[0] > -760:
            windowSurface.blit(self.consPizzaImage, self.consPizzaRect)
        if self.TacoBellRect[0] > -900:
            windowSurface.blit(self.TacoBellImage, self.TacoBellRect)
        super(Level_1, self).move(self.L1Buildings)
        pygame.draw.rect(windowSurface, block['color'], block['rect'])
        pygame.draw.rect(windowSurface, block2['color'], block2['rect'])

        if self.TacoBellRect[0] == 600: pass
class Level_2():
    def  __init__():
        pass
class Level_3():
    def __init__():
         pass
class Level_4():
    def __init__():
        pass
class Level_5():
    def __init__():
        pass
L1 = Level_1()
while True:
    L1.blitBackground()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
            if event.key == K_LEFT:
                moveLeft = True
                moveRight = False
        if event.type == KEYUP:
            moveRight = False
            moveLeft = False
            
    pygame.display.update()
    mainClock.tick()
    windowSurface.fill(SKY_BLUE)
    pygame.draw.rect(windowSurface, block['color'], block['rect'])
    pygame.draw.rect(windowSurface, block2['color'], block2['rect'])
