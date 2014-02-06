#Creating the Gameplay class
#By Tyler Spadgenske

import pygame, sys
from pygame.locals import *

pygame.init()

class Background(object):
    def __init__(self):
        self.farLeft = True
        self.SPEED = 5
    def move(self, buildings, moveRight, moveLeft, cops, ammoX, healthX, tacoX, centered):
        #If Dr. Taco is in the center of the screen, continue
        if centered:
            if buildings[0][0] >= 250:
                self.farLeft = False
            else:
                self.farLeft = True

            #If Dr. Taco is moving right, move buildings, cops, and supplies right.
            if moveRight:
                #Move buildings
                for i in buildings:
                    i[0] -= self.SPEED
                #Move Cops
                self.index = 0
                for x in cops:
                    x.get_rect()[0] -= self.SPEED
                    self.index += 1
                #Move Supplies
                for i in range(0, len(ammoX)):
                    ammoX[i] -= self.SPEED
                for i in range(0, len(healthX)):
                    healthX[i] -= self.SPEED
                for i in range(0, len(tacoX)):
                    tacoX[i] -= self.SPEED
            #If Dr. Taco is moving right, move buildings, cops, and supplies left.
            if moveLeft and self.farLeft:
                #Move Buildings
                for i in buildings:
                    i[0] += self.SPEED
                #Move Cops
                self.index = 0
                for x in cops:
                    x.get_rect()[0] += self.SPEED
                    self.index += 1
                #Move Supplies
                for i in range(0, len(ammoX)):
                    ammoX[i] += self.SPEED
                for i in range(0, len(healthX)):
                    healthX[i] += self.SPEED
                for i in range(0, len(tacoX)):
                    tacoX[i] += self.SPEED
                
class Level_1(Background):
    def __init__(self, surface):
        self.SPEED = 2
        self.moveStuff = Background()
        #Setup important values
        self.windowSurface = surface
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
                     
    def blitBackground(self, moveRight, moveLeft, ammoX, healthX, tacoX, copList, centered):
        if self.bananaBeesRect[0] > -536:
            self.windowSurface.blit(self.bananaBeesImage, self.bananaBeesRect)
        if self.fireStationRect[0] > -995:
            self.windowSurface.blit(self.fireStationImage, self.fireStationRect)
        if self.apt1Rect[0] > -774:
            self.windowSurface.blit(self.apt1Image, self.apt1Rect)
        if self.apt2Rect[0] > -760:
            self.windowSurface.blit(self.apt2Image, self.apt2Rect)
        if self.apt3Rect[0] > -760:
            self.windowSurface.blit(self.apt3Image, self.apt3Rect)
        if self.apt4Rect[0] > -760:
            self.windowSurface.blit(self.apt4Image, self.apt4Rect)
        if self.TVLandRect[0] > -760:
            self.windowSurface.blit(self.TVLandImage, self.TVLandRect)
        if self.PoliceStationRect[0] > -900:
            self.windowSurface.blit(self.PoliceStationImage, self.PoliceStationRect)
        if self.treeRect[0] > -760:
            self.windowSurface.blit(self.tree, self.treeRect)
        if self.consPizzaRect[0] > -760:
            self.windowSurface.blit(self.consPizzaImage, self.consPizzaRect)
        if self.TacoBellRect[0] > -900:
            self.windowSurface.blit(self.TacoBellImage, self.TacoBellRect)
        self.moveStuff.move(self.L1Buildings, moveRight, moveLeft, copList, ammoX, healthX, tacoX, centered)
        return ammoX, healthX, tacoX, self.TacoBellRect[0]

class Level_2(Background):
    def  __init__(self, surface):
        #Setup important values
        self.windowSurface = surface
        #Setup Outside skyscraper Image
        self.skyscraperImage = pygame.image.load('Buildings\\skyscraper.png')
        self.skyscraperRect = self.skyscraperImage.get_rect()
        self.skyscraperRect[0] = 3150
        self.skyscraperRect[1] = 31
        #Setup Burger Barn Image
        self.burgerBarnImage = pygame.image.load('Buildings\\burgerBarn.png')
        self.burgerBarnRect = self.burgerBarnImage.get_rect()
        self.burgerBarnRect[0] = 2300
        self.burgerBarnRect[1] = 130
        #Setup Central Park Image
        self.centralParkImage = pygame.image.load('Buildings\\centralPark.png')
        self.centralParkRect = self.centralParkImage.get_rect()
        self.centralParkRect[0] = 250
        self.centralParkRect[1] = 100

        self.L2Buildings = [self.centralParkRect, self.burgerBarnRect, self.skyscraperRect]

    def blitBackground(self, moveRight, moveLeft, rectList, centered):
        if self.skyscraperRect[0] > -812:
            self.windowSurface.blit(self.skyscraperImage, self.skyscraperRect)
        if self.burgerBarnRect[0] > -554:
            self.windowSurface.blit(self.burgerBarnImage, self.burgerBarnRect)
        if self.centralParkRect[0] > -1858:
            self.windowSurface.blit(self.centralParkImage, self.centralParkRect)

        super(Level_2, self).move(self.L2Buildings, moveRight, moveLeft, rectList, centered)
class Level_3():
    def __init__():
         pass
class Level_4():
    def __init__():
        pass
