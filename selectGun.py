#Select Gun class
#By Tyler Spadgenske
#Version 0.0.1

import pygame
from pygame.locals import *
WHITE = (255, 255, 255)
class selectGunMenu():
    '''
The selectGunMenu class
*************************
The selctGunMenu class includes only two functions, selectGunButton and
chooseGun. The class is used to make the dropdown menu work. It also
determins what weapons are locked.

object.__init__(lockedGuns)
The __init__ function takes one piece of data, a list of what guns
are locked and what guns are unlocked.

dropDownGun, currentWeapon = object.chooseGun(surface, dropDownGun,
currentWeapon)
The function chooseGun takes three pieces of data:

surface: The surface to blit everything on.
dropDownGun: A boolean used to determin whether to
    blit the drop down menu onto the screen.
currentWeapon: A string of the current weapon in use.
    it determins what order to put the other weapons,
    and what gun to blit in the main square.

object.selectGunButton(currentWeapon, event)
The selectGunButton function controls all of the mouse events and
decides what wheapon you chose. It does not handle the arrow, that
is part of the Button() class. It only handles the buttons within the
drop down section. It takes two pieces of data:

currentWeapon: The currentWeapon you are using.
event: An object of what the current keyboard events are. 

This class is only used inside the Toolbar() class
******************************************************************


'''
    def __init__(self, lockedGuns):
        self.ORANGE = (255, 103, 1)
        self.YELLOW = (255, 255, 0)
        self.gunClicked = 0
        self.lockedGuns = lockedGuns

        #Initialize main bar
        self.upperBar = {'rect':pygame.Rect(0, 0, 1200, 75),'color':self.ORANGE}
        self.lowerBar = {'rect':pygame.Rect(0, 525, 1200, 75),'color':self.ORANGE}

        #Initialize boxes
        self.gunMenuBox = {'rect':pygame.Rect(600, 2, 90, 70), 'color':WHITE}
        self.gunMenuBox2 = {'rect':pygame.Rect(603, 5, 85, 65), 'color':self.ORANGE}

        #Initialize lock rect and image
        self.LockImage = pygame.image.load('/home/pi/Taco-Chronicles/files/Weapons/lock.gif')
        self.lockImage1 = pygame.transform.scale(self.LockImage, (30, 40))
        
        self.lockRect1 = self.lockImage1.get_rect()
        self.lockRect2 = self.lockImage1.get_rect()
        self.lockRect3 = self.lockImage1.get_rect()
        self.lockRect4 = self.lockImage1.get_rect()

        #Initialize Gun images and text
        #9mm text and images
        self.PistolImage = pygame.image.load('/home/pi/Taco-Chronicles/files/Weapons/9mmRight.gif')
        self.pistolImage = pygame.transform.scale(self.PistolImage, (60, 55))
        self.rect9mm = self.pistolImage.get_rect()
        self.rect9mm[0] = 615
        self.rect9mm[1] = 10

        self.font9mm = pygame.font.SysFont(None, 24)
        self.text9mm = self.font9mm.render('9mm', True, WHITE, self.ORANGE)
        self.text9mmRect = self.text9mm.get_rect()
        self.text9mmRect[0] = 640
        self.text9mmRect[1] = 50

        #Initialize Shotgun images and text
        self.ShotgunImage = pygame.image.load('/home/pi/Taco-Chronicles/files/Weapons/shotgun.gif')
        self.shotgunImage = pygame.transform.scale(self.ShotgunImage, (90, 90))
        self.shotgunRect = self.shotgunImage.get_rect()
        self.shotgunRect[0] = 615
        self.shotgunRect[1] = 10

        self.shotgunFont = pygame.font.SysFont(None, 24)
        self.shotgunText = self.font9mm.render('shotgun', True, WHITE, self.ORANGE)
        self.shotgunTextRect = self.shotgunText.get_rect()
        self.shotgunTextRect[0] = 615
        self.shotgunTextRect[1] = 50

        #Initialize AK-47 images and text
        self.AK47Image2 = pygame.image.load('/home/pi/Taco-Chronicles/files/Weapons/AK-47.gif')
        self.AK47Image = pygame.transform.scale(self.AK47Image2, (90, 90))
        self.AK47Rect = self.AK47Image.get_rect()
        self.AK47Rect[0] = 615
        self.AK47Rect[1] = 10

        self.AK47Font = pygame.font.SysFont(None, 24)
        self.AK47Text = self.AK47Font.render('AK-47', True, WHITE, self.ORANGE)
        self.AK47TextRect = self.AK47Text.get_rect()
        self.AK47TextRect[0] = 615
        self.AK47TextRect[1] = 50

        #Initialize Bazooka Images and text
        self.bazookaImage2 = pygame.image.load('/home/pi/Taco-Chronicles/files/Weapons/bazooka.gif')
        self.bazookaImage = pygame.transform.scale(self.bazookaImage2, (90, 40))
        self.bazookaRect = self.bazookaImage.get_rect()
        self.bazookaRect[0] = 615
        self.bazookaRect[1] = 10

        self.bazookaFont = pygame.font.SysFont(None, 24)
        self.bazookaText = self.bazookaFont.render('Bazooka', True, WHITE, self.ORANGE)
        self.bazookaTextRect = self.bazookaText.get_rect()
        self.bazookaTextRect[0] = 615
        self.bazookaTextRect[1] = 50
    
        #Initialize Flamethrower images and text
        self.flamethrowerImage2 = pygame.image.load('/home/pi/Taco-Chronicles/files/Weapons/flamethrower.gif')
        self.flamethrowerImage = pygame.transform.scale(self.flamethrowerImage2, (90, 40))
        self.flamethrowerRect = self.flamethrowerImage.get_rect()
        self.flamethrowerRect[0] = 615
        self.flamethrowerRect[1] = 10

        self.flamethrowerFont = pygame.font.SysFont(None, 17)
        self.flamethrowerText = self.flamethrowerFont.render('Flamethrower', True, WHITE, self.ORANGE)
        self.flamethrowerTextRect = self.flamethrowerText.get_rect()
        self.flamethrowerTextRect[0] = 605
        self.flamethrowerTextRect[1] = 50

        #Draw dropdown menu
        self.gunDropDownBox = {'rect':pygame.Rect(600, 2, 90, 400), 'color':self.ORANGE}
        self.gunBox1 = {'rect':pygame.Rect(603, 240, 85, 70), 'color':WHITE}
        self.gunBox2 = {'rect':pygame.Rect(603, 80, 85, 70), 'color':WHITE}
        self.gunBox3 = {'rect':pygame.Rect(603, 160, 85, 70), 'color':WHITE}
        self.gunBox4 = {'rect':pygame.Rect(603, 320, 85, 70), 'color':WHITE}
        
    def chooseGun(self, windowSurface, dropDownGun, currentWeapon):
        pygame.draw.rect(windowSurface, self.gunMenuBox['color'], self.gunMenuBox['rect'])
        pygame.draw.rect(windowSurface, self.gunMenuBox2['color'], self.gunMenuBox2['rect'])

        #Draw menu boxes
        if dropDownGun:
            pygame.draw.rect(windowSurface, self.gunDropDownBox['color'], self.gunDropDownBox['rect'])
            pygame.draw.rect(windowSurface, self.gunBox1['color'], self.gunBox1['rect'])
            pygame.draw.rect(windowSurface, self.gunBox2['color'], self.gunBox2['rect'])
            pygame.draw.rect(windowSurface, self.gunBox3['color'], self.gunBox3['rect'])
            pygame.draw.rect(windowSurface, self.gunBox4['color'], self.gunBox4['rect'])
        
        if currentWeapon == '9mm':
            #Blit 9mm in selected square
            self.rect9mm[0] = 615
            self.rect9mm[1] = 10
            windowSurface.blit(self.pistolImage, self.rect9mm)
            windowSurface.blit(self.text9mm, self.text9mmRect)
            if dropDownGun:
                #Blit shotgun in square one
                self.shotgunRect[0] = 600
                self.shotgunRect[1] = 70
                windowSurface.blit(self.shotgunImage, self.shotgunRect)

                #If shotgun is locked, add lock image
                if self.lockedGuns['shotgun']:
                    self.lockRect1[0] = 630
                    self.lockRect1[1] = 90
                    windowSurface.blit(self.lockImage1, self.lockRect1)

                #Blit AK-47 in square two
                self.AK47Rect[0] = 600
                self.AK47Rect[1] = 150
                windowSurface.blit(self.AK47Image, self.AK47Rect)

                #If AK-47 is locked, add lock image
                if self.lockedGuns['AK-47']:
                    self.lockRect2[0] = 630
                    self.lockRect2[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect2)

                #Blit Bazooka in square three
                self.bazookaRect[0] = 600
                self.bazookaRect[1] = 250
                windowSurface.blit(self.bazookaImage, self.bazookaRect)

                #If Bazooka is locked, add lock image
                if self.lockedGuns['bazooka']:
                    self.lockRect3[0] = 630
                    self.lockRect3[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect3)

                #Blit Flamethrower in square four
                self.flamethrowerRect[0] = 600
                self.flamethrowerRect[1] = 330
                windowSurface.blit(self.flamethrowerImage, self.flamethrowerRect)

                #If Flamethrower is locked, add lock image
                if self.lockedGuns['flamethrower']:
                    self.lockRect4[0] = 630
                    self.lockRect4[1] = 330
                    windowSurface.blit(self.lockImage1, self.lockRect4)
                
        if currentWeapon == 'shotgun':
            #Blit shotgun in main square
            self.shotgunRect[0] = 600
            self.shotgunRect[1] = -10
            windowSurface.blit(self.shotgunImage, self.shotgunRect)
            windowSurface.blit(self.shotgunText, self.shotgunTextRect)
            if dropDownGun:
                #Blit 9mm in first square
                self.rect9mm[0] = 615
                self.rect9mm[1] = 90
                windowSurface.blit(self.pistolImage, self.rect9mm)
                
                #Blit AK-47 in second square
                self.AK47Rect[0] = 600
                self.AK47Rect[1] = 150
                windowSurface.blit(self.AK47Image, self.AK47Rect)

                #If AK-47 is locked, add lock image
                if self.lockedGuns['AK-47']:
                    self.lockRect2[0] = 630
                    self.lockRect2[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect2)

                #Blit Bazooka in third square
                self.bazookaRect[0] = 600
                self.bazookaRect[1] = 250
                windowSurface.blit(self.bazookaImage, self.bazookaRect)

                #If Bazooka is locked, add lock image
                if self.lockedGuns['bazooka']:
                    self.lockRect3[0] = 630
                    self.lockRect3[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect3)

                #Blit Flamethrower in fourth square
                self.flamethrowerRect[0] = 600
                self.flamethrowerRect[1] = 330
                windowSurface.blit(self.flamethrowerImage, self.flamethrowerRect)

                #If Flamethrower is locked, add lock image
                if self.lockedGuns['flamethrower']:
                    self.lockRect4[0] = 630
                    self.lockRect4[1] = 330
                    windowSurface.blit(self.lockImage1, self.lockRect4)
                
        if currentWeapon == 'AK-47':
            #Blit AK-47 in main square
            self.AK47Rect[0] = 600
            self.AK47Rect[1] = -20
            windowSurface.blit(self.AK47Image, self.AK47Rect)
            windowSurface.blit(self.AK47Text, self.AK47TextRect) 
            if dropDownGun:
                #Blit 9mm in first square
                self.rect9mm[0] = 615
                self.rect9mm[1] = 90
                windowSurface.blit(self.pistolImage, self.rect9mm)

                #Blit shotgun in second square
                self.shotgunRect[0] = 600
                self.shotgunRect[1] = 150
                windowSurface.blit(self.shotgunImage, self.shotgunRect)
                
                #If shotgun is locked, add lock image
                if self.lockedGuns['shotgun']:
                    self.lockRect1[0] = 630
                    self.lockRect1[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect1)

                #Blit Bazooka in third square
                self.bazookaRect[0] = 600
                self.bazookaRect[1] = 250
                windowSurface.blit(self.bazookaImage, self.bazookaRect)

                #If Bazooka is locked, add lock image
                if self.lockedGuns['bazooka']:
                    self.lockRect3[0] = 630
                    self.lockRect3[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect3)

                #Blit Flamethrower in fourth square
                self.flamethrowerRect[0] = 600
                self.flamethrowerRect[1] = 330
                windowSurface.blit(self.flamethrowerImage, self.flamethrowerRect)

                #If Flamethrower is locked, add lock image
                if self.lockedGuns['flamethrower']:
                    self.lockRect4[0] = 630
                    self.lockRect4[1] = 330
                    windowSurface.blit(self.lockImage1, self.lockRect4)
                
        if currentWeapon == 'bazooka':
            #Blit bazooka in main square
            self.bazookaRect[0] = 600
            self.bazookaRect[1] = 10
            windowSurface.blit(self.bazookaImage, self.bazookaRect)
            windowSurface.blit(self.bazookaText, self.bazookaTextRect)
            if dropDownGun:
                #Blit 9mm in first square
                self.rect9mm[0] = 615
                self.rect9mm[1] = 90
                windowSurface.blit(self.pistolImage, self.rect9mm)

                #Blit shotgun in second square
                self.shotgunRect[0] = 600
                self.shotgunRect[1] = 150
                windowSurface.blit(self.shotgunImage, self.shotgunRect)

                #If shotgun is locked, add lock image
                if self.lockedGuns['shotgun']:
                    self.lockRect1[0] = 630
                    self.lockRect1[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect1)

                #Blit AK-47 in third Square
                self.AK47Rect[0] = 600
                self.AK47Rect[1] = 225
                windowSurface.blit(self.AK47Image, self.AK47Rect)

                #If AK-47 is locked, add lock image
                if self.lockedGuns['AK-47']:
                    self.lockRect2[0] = 630
                    self.lockRect2[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect2)

                #Blit Flamethrower in Fourth square
                self.flamethrowerRect[0] = 600
                self.flamethrowerRect[1] = 330
                windowSurface.blit(self.flamethrowerImage, self.flamethrowerRect)

                #If Flamethrower is locked, add lock image
                if self.lockedGuns['flamethrower']:
                    self.lockRect4[0] = 630
                    self.lockRect4[1] = 330
                    windowSurface.blit(self.lockImage1, self.lockRect4)

        if currentWeapon == 'flamethrower':
            #Blit flamethrower in main square
            self.flamethrowerRect[0] = 600
            self.flamethrowerRect[1] = 10
            windowSurface.blit(self.flamethrowerImage, self.flamethrowerRect)
            windowSurface.blit(self.flamethrowerText, self.flamethrowerTextRect)
            if dropDownGun:
                #Blit 9mm in first square
                self.rect9mm[0] = 615
                self.rect9mm[1] = 90
                windowSurface.blit(self.pistolImage, self.rect9mm)

                #Blit shotgun in second square
                self.shotgunRect[0] = 600
                self.shotgunRect[1] = 150
                windowSurface.blit(self.shotgunImage, self.shotgunRect)

                #If shotgun is locked, add lock image
                if self.lockedGuns['shotgun']:
                    self.lockRect1[0] = 630
                    self.lockRect1[1] = 170
                    windowSurface.blit(self.lockImage1, self.lockRect1)

                #Blit AK-47 in third square
                self.AK47Rect[0] = 600
                self.AK47Rect[1] = 225
                windowSurface.blit(self.AK47Image, self.AK47Rect)

                #If AK-47 is locked, add lock image
                if self.lockedGuns['AK-47']:
                    self.lockRect2[0] = 630
                    self.lockRect2[1] = 250
                    windowSurface.blit(self.lockImage1, self.lockRect2)

                #Blit Bazooka in Fourth square 
                self.bazookaRect[0] = 600
                self.bazookaRect[1] = 330
                windowSurface.blit(self.bazookaImage, self.bazookaRect)

                #If Bazooka is locked, add lock image
                if self.lockedGuns['bazooka']:
                    self.lockRect3[0] = 630
                    self.lockRect3[1] = 330
                    windowSurface.blit(self.lockImage1, self.lockRect3)
        return dropDownGun, currentWeapon
                
    def selectGunButton(self, currentWeapon, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] > 603 and event.pos[0] < 688:
                if event.pos[1] > 70 and event.pos[1] < 148:
                    self.gunClicked = 1

            if event.pos[0] > 603 and event.pos[0] < 688:
                if event.pos[1] > 159 and event.pos[1] < 228:
                    self.gunClicked = 2

            if event.pos[0] > 603 and event.pos[0] < 688:
                if event.pos[1] > 239 and event.pos[1] < 309:
                    self.gunClicked = 3
                    
            if event.pos[0] > 603 and event.pos[0] < 688:
                if event.pos[1] > 319 and event.pos[1] < 389:
                    self.gunClicked = 4
                    
        if currentWeapon == '9mm':
            if self.gunClicked == 1:
                if self.lockedGuns['shotgun'] == False:
                    currentWeapon = 'shotgun'
            if self.gunClicked == 2:
                if self.lockedGuns['AK-47'] == False:
                   currentWeapon = 'AK-47'
            if self.gunClicked == 3:
                if self.lockedGuns['bazooka'] == False:
                    currentWeapon = 'bazooka'
            if self.gunClicked == 4:
                if self.lockedGuns['flamethrower'] == False:
                    currentWeapon = 'flamethrower'
                
        elif currentWeapon == 'shotgun':
            if self.gunClicked == 1:
                currentWeapon = '9mm'
            if self.gunClicked == 2:
                if self.lockedGuns['AK-47'] == False:
                    currentWeapon = 'AK-47'
            if self.gunClicked == 3:
                if self.lockedGuns['bazooka'] == False:
                    currentWeapon = 'bazooka'
            if self.gunClicked == 4:
                if self.lockedGuns['flamethrower'] == False:
                    currentWeapon = 'flamethrower'
                
        elif currentWeapon == 'AK-47':
            if self.gunClicked == 1:
                currentWeapon = '9mm'
            if self.gunClicked == 2:
                if self.lockedGuns['shotgun'] == False:
                    currentWeapon = 'shotgun'
            if self.gunClicked == 3:
                if self.lockedGuns['bazooka'] == False:
                    currentWeapon = 'bazooka'
            if self.gunClicked == 4:
                if self.lockedGuns['flamethrower'] == False:
                    currentWeapon = 'flamethrower'

        elif currentWeapon == 'bazooka':
            if self.gunClicked == 1:
                currentWeapon = '9mm'
            if self.gunClicked == 2:
                if self.lockedGuns['shotgun'] == False:
                    currentWeapon = 'shotgun'
            if self.gunClicked == 3:
                if self.lockedGuns['AK-47'] == False:
                    currentWeapon = 'AK-47'
            if self.gunClicked == 4:
                if self.lockedGuns['flamethrower'] == False:
                    currentWeapon = 'flamethrower'

        elif currentWeapon == 'flamethrower':
            if self.gunClicked == 1:
                currentWeapon = '9mm'
            if self.gunClicked == 2:
                if self.lockedGuns['shotgun'] == False:
                    currentWeapon = 'shotgun'
            if self.gunClicked == 3:
                if self.lockedGuns['AK-47'] == False:
                    currentWeapon = 'AK-47'
            if self.gunClicked == 4:
                if self.lockedGuns['bazooka'] == False:
                    currentWeapon = 'bazooka'
        self.gunClicked = 0
        return currentWeapon
