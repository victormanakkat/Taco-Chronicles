#SelectTool class
#By Tyler Spadgenske
#Version 0.0.1

import pygame
from pygame.locals import *
WHITE = (255, 255, 255)
class selectToolMenu():
    '''
The selectToolMenu Class
*****************************
The selectToolMenu class in practically identical to the
selectGunMenu class, but the coordinates are different,
so are images. Instead of a list of the locked guns,
there is a list of the locked tools. The only reason these two
class were not combined is all the images are different and
I didn't want such a large program. 
'''
    def __init__(self, lockedTools):
        self.ORANGE = (255, 103, 1)
        self.YELLOW = (255, 255, 0)
        self.gunClicked = 0
        self.lockedTools = lockedTools

        #Initialize main bar
        self.upperBar = {'rect':pygame.Rect(0, 0, 1200, 75),'color':self.ORANGE}
        self.lowerBar = {'rect':pygame.Rect(0, 525, 1200, 75),'color':self.ORANGE}

        #Initialize boxes
        self.gunMenuBox = {'rect':pygame.Rect(450, 2, 90, 70), 'color':WHITE}
        self.gunMenuBox2 = {'rect':pygame.Rect(453, 5, 85, 65), 'color':self.ORANGE}

        #Initialize lock rect and image
        self.LockImage = pygame.image.load('Weapons\\lock.gif')
        self.lockImage1 = pygame.transform.scale(self.LockImage, (30, 40))
        
        self.lockRect1 = self.lockImage1.get_rect()
        self.lockRect2 = self.lockImage1.get_rect()
        self.lockRect3 = self.lockImage1.get_rect()
        self.lockRect4 = self.lockImage1.get_rect()

        #Initialize tool images and text
        #Crowbar text and images
        self.CrowbarImage = pygame.image.load('Tools\\crowbar.gif')
        self.crowbarImage = pygame.transform.scale(self.CrowbarImage, (60, 55))
        self.crowbarRect = self.crowbarImage.get_rect()

        self.crowbarFont = pygame.font.SysFont(None, 15)
        self.crowbarText = self.crowbarFont.render('crowbar', True, WHITE, self.ORANGE)
        self.crowbarTextRect = self.crowbarText.get_rect()
        self.crowbarTextRect[0] = 455
        self.crowbarTextRect[1] = 55

        #Initialize rope images and text
        self.RopeImage = pygame.image.load('Tools\\rope.gif')
        self.ropeImage = pygame.transform.scale(self.RopeImage, (65, 65))
        self.ropeRect = self.ropeImage.get_rect()

        self.ropeFont = pygame.font.SysFont(None, 24)
        self.ropeText = self.crowbarFont.render('rope', True, WHITE, self.ORANGE)
        self.ropeTextRect = self.ropeText.get_rect()
        self.ropeTextRect[0] = 510
        self.ropeTextRect[1] = 55
        
        #Initialize key images and text
        self.keyImage2 = pygame.image.load('Tools\\key.gif')
        self.keyImage = pygame.transform.scale(self.keyImage2, (50, 50))
        self.keyRect = self.keyImage.get_rect()

        self.keyFont = pygame.font.SysFont(None, 24)
        self.keyText = self.keyFont.render('key', True, WHITE, self.ORANGE)
        self.keyTextRect = self.keyText.get_rect()
        self.keyTextRect[0] = 500
        self.keyTextRect[1] = 50

        #Initialize TNT Images and text
        self.TNTImage2 = pygame.image.load('Tools\\TNT.png')
        self.TNTimage = pygame.transform.scale(self.TNTImage2, (40, 40))
        self.TNTrect = self.TNTimage.get_rect()

        #Initialize jetapack images and text
        self.jetpackImage2 = pygame.image.load('Tools\\jetpack.png')
        self.jetpackImage = pygame.transform.scale(self.jetpackImage2, (22, 64))
        self.jetpackRect = self.jetpackImage.get_rect()
        
        self.jetpackFont = pygame.font.SysFont(None, 17)
        self.jetpackText = self.jetpackFont.render('Jetpack', True, WHITE, self.ORANGE)
        self.jetpackTextRect = self.jetpackText.get_rect()
        self.jetpackTextRect[0] = 490
        self.jetpackTextRect[1] = 50

        #Draw dropdown menu
        self.gunDropDownBox = {'rect':pygame.Rect(450, 2, 90, 400), 'color':self.ORANGE}
        self.gunBox1 = {'rect':pygame.Rect(453, 240, 85, 70), 'color':WHITE}
        self.gunBox2 = {'rect':pygame.Rect(453, 80, 85, 70), 'color':WHITE}
        self.gunBox3 = {'rect':pygame.Rect(453, 160, 85, 70), 'color':WHITE}
        self.gunBox4 = {'rect':pygame.Rect(453, 320, 85, 70), 'color':WHITE}
        
    def chooseTool(self, windowSurface, dropDownTool, currentTool):
        pygame.draw.rect(windowSurface, self.gunMenuBox['color'], self.gunMenuBox['rect'])
        pygame.draw.rect(windowSurface, self.gunMenuBox2['color'], self.gunMenuBox2['rect'])

        #Draw menu boxes
        if dropDownTool:
            pygame.draw.rect(windowSurface, self.gunDropDownBox['color'], self.gunDropDownBox['rect'])
            pygame.draw.rect(windowSurface, self.gunBox1['color'], self.gunBox1['rect'])
            pygame.draw.rect(windowSurface, self.gunBox2['color'], self.gunBox2['rect'])
            pygame.draw.rect(windowSurface, self.gunBox3['color'], self.gunBox3['rect'])
            pygame.draw.rect(windowSurface, self.gunBox4['color'], self.gunBox4['rect'])
        
        if currentTool == 'crowbar':
            #Blit crowbar in selected square
            self.crowbarRect[0] = 465
            self.crowbarRect[1] = 10
            windowSurface.blit(self.crowbarImage, self.crowbarRect)
            windowSurface.blit(self.crowbarText, self.crowbarTextRect)
            if dropDownTool:
                #Blit rope in square one
                self.ropeRect[0] = 460
                self.ropeRect[1] = 85
                windowSurface.blit(self.ropeImage, self.ropeRect)

                #If rope is locked, add lock image
                if self.lockedTools['rope']:
                    self.lockRect1[0] = 480
                    self.lockRect1[1] = 95
                    windowSurface.blit(self.lockImage1, self.lockRect1)

                #Blit key in square two
                self.keyRect[0] = 470
                self.keyRect[1] = 170
                windowSurface.blit(self.keyImage, self.keyRect)

                #If key is locked, add lock image
                if self.lockedTools['key']:
                    self.lockRect2[0] = 480
                    self.lockRect2[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect2)

                #Blit TNT in square three
                self.TNTrect[0] = 475
                self.TNTrect[1] = 257
                windowSurface.blit(self.TNTimage, self.TNTrect)

                #If Bazooka is locked, add lock image
                if self.lockedTools['TNT']:
                    self.lockRect3[0] = 480
                    self.lockRect3[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect3)

                #Blit jetpack in square four
                self.jetpackRect[0] = 485
                self.jetpackRect[1] = 322
                windowSurface.blit(self.jetpackImage, self.jetpackRect)

                #If jetpack is locked, add lock image
                if self.lockedTools['jetpack']:
                    self.lockRect4[0] = 480
                    self.lockRect4[1] = 330
                    windowSurface.blit(self.lockImage1, self.lockRect4)
                
        if currentTool == 'rope':
            #Blit rope in main square
            self.ropeRect[0] = 461
            self.ropeRect[1] = 5
            windowSurface.blit(self.ropeImage, self.ropeRect)
            windowSurface.blit(self.ropeText, self.ropeTextRect)
            if dropDownTool:
                #Blit crowbar in first square
                self.crowbarRect[0] = 465
                self.crowbarRect[1] = 87
                windowSurface.blit(self.crowbarImage, self.crowbarRect)
                
                #Blit key in second square
                self.keyRect[0] = 470
                self.keyRect[1] = 170
                windowSurface.blit(self.keyImage, self.keyRect)

                #If key is locked, add lock image
                if self.lockedTools['key']:
                    self.lockRect2[0] = 480
                    self.lockRect2[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect2)

                #Blit TNT in third square
                self.TNTrect[0] = 475
                self.TNTrect[1] = 257
                windowSurface.blit(self.TNTimage, self.TNTrect)

                #If TNT is locked, add lock image
                if self.lockedTools['TNT']:
                    self.lockRect3[0] = 630
                    self.lockRect3[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect3)

                #Blit jetpack in fourth square
                self.jetpackRect[0] = 485
                self.jetpackRect[1] = 322
                windowSurface.blit(self.jetpackImage, self.jetpackRect)

                #If jetpack is locked, add lock image
                if self.lockedTools['jetpack']:
                    self.lockRect4[0] = 480
                    self.lockRect4[1] = 330
                    windowSurface.blit(self.lockImage1, self.lockRect4)
                
        if currentTool == 'key':
            #Blit AK-47 in main square
            self.keyRect[0] = 470
            self.keyRect[1] = 10
            windowSurface.blit(self.keyImage, self.keyRect)
            windowSurface.blit(self.keyText, self.keyTextRect) 
            if dropDownTool:
                #Blit crowbar in first square
                self.crowbarRect[0] = 465
                self.crowbarRect[1] = 87
                windowSurface.blit(self.crowbarImage, self.crowbarRect)

                #Blit rope in second square
                self.ropeRect[0] = 460
                self.ropeRect[1] = 165
                windowSurface.blit(self.ropeImage, self.ropeRect)
                
                #If rope is locked, add lock image
                if self.lockedTools['rope']:
                    self.lockRect1[0] = 630
                    self.lockRect1[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect1)

                #Blit TNT in third square
                self.TNTrect[0] = 475
                self.TNTrect[1] = 257
                windowSurface.blit(self.TNTimage, self.TNTrect)

                #If TNT is locked, add lock image
                if self.lockedTools['TNT']:
                    self.lockRect3[0] = 630
                    self.lockRect3[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect3)

                #Blit jetpack in fourth square
                self.jetpackRect[0] = 485
                self.jetpackRect[1] = 322
                windowSurface.blit(self.jetpackImage, self.jetpackRect)

                #If jetpack is locked, add lock image
                if self.lockedTools['jetpack']:
                    self.lockRect4[0] = 480
                    self.lockRect4[1] = 330
                    windowSurface.blit(self.lockImage1, self.lockRect4)
                
        if currentTool == 'TNT':
            #Blit TNT in main square
            self.TNTrect[0] = 475
            self.TNTrect[1] = 16
            windowSurface.blit(self.TNTimage, self.TNTrect)
            if dropDownTool:
                #Blit crowbar in first square
                self.crowbarRect[0] = 465
                self.crowbarRect[1] = 87
                windowSurface.blit(self.crowbarImage, self.crowbarRect)
                
                #Blit rope in second square
                self.ropeRect[0] = 460
                self.ropeRect[1] = 165
                windowSurface.blit(self.ropeImage, self.ropeRect)

                #If rope is locked, add lock image
                if self.lockedTools['rope']:
                    self.lockRect1[0] = 630
                    self.lockRect1[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect1)

                #Blit key in third Square
                self.keyRect[0] = 470
                self.keyRect[1] = 245
                windowSurface.blit(self.keyImage, self.keyRect)

                #If key is locked, add lock image
                if self.lockedTools['key']:
                    self.lockRect2[0] = 630
                    self.lockRect2[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect2)

                #Blit jetpack in Fourth square
                self.jetpackRect[0] = 485
                self.jetpackRect[1] = 322
                windowSurface.blit(self.jetpackImage, self.jetpackRect)

                #If jetpack is locked, add lock image
                if self.lockedTools['jetpack']:
                    self.lockRect4[0] = 480
                    self.lockRect4[1] = 330
                    windowSurface.blit(self.lockImage1, self.lockRect4)

        if currentTool == 'jetpack':
            #Blit jetpack in main square
            self.jetpackRect[0] = 468
            self.jetpackRect[1] = 7
            windowSurface.blit(self.jetpackImage, self.jetpackRect)
            windowSurface.blit(self.jetpackText, self.jetpackTextRect)
            if dropDownTool:
                #Blit crowbar in first square
                self.crowbarRect[0] = 465
                self.crowbarRect[1] = 87
                windowSurface.blit(self.crowbarImage, self.crowbarRect)

                #Blit rope in second square
                self.ropeRect[0] = 460
                self.ropeRect[1] = 165
                windowSurface.blit(self.ropeImage, self.ropeRect)

                #If rope is locked, add lock image
                if self.lockedTools['rope']:
                    self.lockRect1[0] = 630
                    self.lockRect1[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect1)
                    
                #Blit key in third square
                self.keyRect[0] = 470
                self.keyRect[1] = 245
                windowSurface.blit(self.keyImage, self.keyRect)
                
                #If key is locked, add lock image
                if self.lockedTools['key']:
                    self.lockRect2[0] = 630
                    self.lockRect2[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect2)
                
                #Blit TNT in Fourth square
                self.TNTrect[0] = 475
                self.TNTrect[1] = 335
                windowSurface.blit(self.TNTimage, self.TNTrect)
                
                #If TNT is locked, add lock image
                if self.lockedTools['TNT']:
                    self.lockRect3[0] = 630
                    self.lockRect3[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect3)
                
        return dropDownTool, currentTool
                
    def selectToolButton(self, currentTool, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] > 453 and event.pos[0] < 537:
                if event.pos[1] > 80 and event.pos[1] < 150:
                    self.gunClicked = 1

            if event.pos[0] > 453 and event.pos[0] < 537:
                if event.pos[1] > 159 and event.pos[1] < 228:
                    self.gunClicked = 2

            if event.pos[0] > 453 and event.pos[0] < 537:
                if event.pos[1] > 239 and event.pos[1] < 309:
                    self.gunClicked = 3
                    
            if event.pos[0] > 453 and event.pos[0] < 537:
                if event.pos[1] > 319 and event.pos[1] < 389:
                    self.gunClicked = 4
                    
        if currentTool == 'crowbar':
            if self.gunClicked == 1:
                if self.lockedTools['rope'] == False:
                    currentTool = 'rope'
            if self.gunClicked == 2:
                if self.lockedTools['key'] == False:
                   currentTool = 'key'
            if self.gunClicked == 3:
                if self.lockedTools['TNT'] == False:
                    currentTool = 'TNT'
            if self.gunClicked == 4:
                if self.lockedTools['jetpack'] == False:
                    currentTool = 'jetpack'
                
        elif currentTool == 'rope':
            if self.gunClicked == 1:
                currentTool = 'crowbar'
            if self.gunClicked == 2:
                if self.lockedTools['key'] == False:
                    currentTool = 'key'
            if self.gunClicked == 3:
                if self.lockedTools['TNT'] == False:
                    currentTool = 'TNT'
            if self.gunClicked == 4:
                if self.lockedTools['jetpack'] == False:
                    currentTool = 'jetpack'
                
        elif currentTool == 'key':
            if self.gunClicked == 1:
                currentTool = 'crowbar'
            if self.gunClicked == 2:
                if self.lockedTools['rope'] == False:
                    currentTool = 'rope'
            if self.gunClicked == 3:
                if self.lockedTools['TNT'] == False:
                    currentTool = 'TNT'
            if self.gunClicked == 4:
                if self.lockedTools['jetpack'] == False:
                    currentTool = 'jetpack'

        elif currentTool == 'TNT':
            if self.gunClicked == 1:
                currentTool = 'crowbar'
            if self.gunClicked == 2:
                if self.lockedTools['rope'] == False:
                    currentTool = 'rope'
            if self.gunClicked == 3:
                if self.lockedTools['key'] == False:
                    currentTool = 'key'
            if self.gunClicked == 4:
                if self.lockedTools['jetpack'] == False:
                    currentTool = 'jetpack'

        elif currentTool == 'jetpack':
            if self.gunClicked == 1:
                currentTool = 'crowbar'
            if self.gunClicked == 2:
                if self.lockedTools['rope'] == False:
                    currentTool = 'rope'
            if self.gunClicked == 3:
                if self.lockedTools['key'] == False:
                    currentTool = 'key'
            if self.gunClicked == 4:
                if self.lockedTools['TNT'] == False:
                    currentTool = 'TNT'
        self.gunClicked = 0
        return currentTool
