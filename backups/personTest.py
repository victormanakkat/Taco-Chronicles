#Creating the Person class
#By Tyler Spadgenske
import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1200 #Set up the window
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Creating the person class (Version 0.0.3)')

mainClock = pygame.time.Clock()
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
windowSurface.fill(WHITE)
direction = 1
takeStep = False
walkLeft = False
walkRight = False
goUp = None
shootBullet = False
character = 'officer'
class Person(object): #Create the Person class
    def __init__(self, character):
        self.x = 100
        self.y = 100
        self.jumpCount = 0
        self.countWalk = 0
        self.takeStep = False
        self.countJump = 0
        self.location = [{'right':573, 'left':518},{'right':580, 'left':543}]
        self.character = character

        #Create Doctor Taco Images
        #Initialize Dr. Taco standing right image
        self.DrTacoRightImage = pygame.image.load('Characters\\DrTacoRight.gif')

        #Initialize Dr. Taco rect
        self.rect = self.DrTacoRightImage.get_rect()
        self.rect.centerx = windowSurface.get_rect().centerx
        self.rect.centery = windowSurface.get_rect().centery + 200
        self.DrTacoRight = pygame.transform.scale(self.DrTacoRightImage, (70, 100))

        #Initialize Dr. Taco walking right image
        self.tacoImage2 = pygame.image.load('Characters\\DrTacoWalkRight.gif')

        #Initialize Dr. Taco walking rect
        self.rect2 = self.tacoImage2.get_rect()
        self.rect2.centerx = windowSurface.get_rect().centerx
        self.rect2.centery = windowSurface.get_rect().centery + 200
        self.DrTacoWalkRight = pygame.transform.scale(self.tacoImage2, (70, 100))
        
        #Initialize Dr. Taco walking left image
        self.tacoWalkLeftImage = pygame.image.load('Characters\\DrTacoWalkLeft.gif')
        self.DrTacoWalkLeft = pygame.transform.scale(self.tacoWalkLeftImage, (70, 100))

        #Initialize Dr. Taco standing left image
        self.tacoLeftImage = pygame.image.load('Characters\\DrTacoLeft.gif')
        self.DrTacoLeft = pygame.transform.scale(self.tacoLeftImage, (70, 100))

        self.DrTacoStandingImages = [self.DrTacoLeft, self.DrTacoRight]
        self.DrTacoWalkingImages = [self.DrTacoWalkLeft, self.DrTacoWalkRight]

        #Create Officer 1 images   
        #Initialize officer standing right image
        self.officerRightImage = pygame.image.load('Characters\\officerRight.gif')

        #Initialize officer rect
        self.officerRect = self.officerRightImage.get_rect()
        self.officerRect.centerx = windowSurface.get_rect().centerx
        self.officerRect.centery = windowSurface.get_rect().centery + 200
        self.officerRight = pygame.transform.scale(self.officerRightImage, (70, 100))

        #Initialize officer walking right image
        self.officerImage2 = pygame.image.load('Characters\\officerWalkRight.gif')

        #Initialize officer walking rect
        self.officerRect2 = self.officerImage2.get_rect()
        self.officerRect2.centerx = windowSurface.get_rect().centerx
        self.officerRect2.centery = windowSurface.get_rect().centery + 200
        self.officerWalkRight = pygame.transform.scale(self.officerImage2, (70, 100))
        
        #Initialize officer walking left image
        self.officerWalkLeftImage = pygame.image.load('Characters\\officerWalkLeft.gif')
        self.officerWalkLeft = pygame.transform.scale(self.officerWalkLeftImage, (70, 100))

        #Initialize officer standing left image
        self.officerLeftImage = pygame.image.load('Characters\\officerLeft.gif')
        self.officerLeft = pygame.transform.scale(self.officerLeftImage, (70, 100))

        self.officerStandingImages = [self.officerLeft, self.officerRight]
        self.officerWalkingImages = [self.officerWalkLeft, self.officerWalkRight]
        
        #Draw 9mm in hand
        #Initialize 9mm Images
        self.right9mmImage = pygame.image.load('Weapons\\9mmRight.gif')
        self.right9mm = pygame.transform.scale(self.right9mmImage, (20, 15))

        self.left9mmImage = pygame.image.load('Weapons\\9mmLeft.gif')
        self.left9mm = pygame.transform.scale(self.left9mmImage, (20, 15))

        #Setup 9mm rect        
        self.gunRect = self.right9mmImage.get_rect()
        if self.character == 'Doctor Taco':
            self.gunRect.centerx = self.rect.centerx + 110
            self.gunRect.centery = self.rect.centery + 25
        if self.character == 'officer':
            self.gunRect[1] = 452

        #Setup the bullets
        self.bullets = []
        self.shootBullet = True
        self.num = 0
        self.bulletDirection = []
        self.BulletNum = 0
        
    def walk(self, takeStep): #This function is used to make Dr. Taco move his legs from walking position to standing.
        self.countWalk += 1
        if self.countWalk == 5:
            self.takeStep = False
        if self.countWalk == 10:
            self.countWalk = 0
            if walkRight or walkLeft:
                self.takeStep = True
        windowSurface.fill(WHITE)
        if self.character == 'Doctor Taco':
            windowSurface.blit(self.DrTacoStandingImages[direction], self.rect)
        if self.character == 'officer':
            windowSurface.blit(self.officerStandingImages[direction], self.officerRect)
        if takeStep == True:
             windowSurface.fill(WHITE)
             if self.character == 'Doctor Taco':
                 windowSurface.blit(self.DrTacoWalkingImages[direction], self.rect2)
             if self.character == 'officer':
                 windowSurface.blit(self.officerWalkingImages[direction], self.officerRect2)
                 
        return self.takeStep #Return takeStep so it knows what position it is in.
        
    def jump(self, goUp): #Draws character jumping up and going down.
        if self.countJump == -65:
            goUp = False
        if goUp:
            if self.character == 'Doctor Taco':
                self.rect[1] -= 5
                self.rect2[1] -= 5
            if self.character == 'officer':
                self.officerRect[1] -= 5
                self.officerRect2[1] -= 5
            self.countJump -= 5
            self.gunRect[1] -= 5
        elif goUp == False:
            if self.character == 'Doctor Taco':
                self.rect[1] += 5
                self.rect2[1] += 5
            if self.character == 'officer':
                self.officerRect[1] += 5
                self.officerRect2[1] += 5
            self.countJump += 5
            self.gunRect[1] += 5
        if self.countJump == 0:
            goUp = None
        return goUp
        
    def shootPistol(self, shootBullet, direction): #Fires bullets and moves pistol to right location
        if direction == 1:
            if  self.character == 'Doctor Taco':
                self.gunRect[0] = self.location[0]['right']
            if self.character == 'officer':
                self.gunRect[0] = self.location[1]['right']
            windowSurface.blit(self.right9mm, self.gunRect)
        if direction == 0:
            if self.character == 'Doctor Taco':
                self.gunRect[0] = self.location[0]['left']
            if self.character == 'officer':
                self.gunRect[0] = self.location[1]['left']
            windowSurface.blit(self.left9mm, self.gunRect)
        if shootBullet == True:
            self.bullets.append(pygame.Rect(self.gunRect[0], self.gunRect[1], 4, 4))
            self.bulletDirection.append(direction)
            shootBullet = False
        for i in self.bullets:
            pygame.draw.rect(windowSurface, BLACK, i)
        for i in self.bullets:
            if self.bulletDirection[self.bulletNum] == 0:
                i[0] -= 10
            else:
                i[0] += 10
            self.bulletNum += 1
            self.num += 1
        self.bulletNum = 0
        self.num = 0
        return shootBullet
    
    def useTool():
        pass
    def die():
        pass

DocTaco = Person(character)
while True:
    takeStep = DocTaco.walk(takeStep)
    goUp = DocTaco.jump(goUp)
    shootBullet = DocTaco.shootPistol(shootBullet, direction)
    mainClock.tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direction = 1
                walkRight = True
                walkLeft = False
            if event.key == K_LEFT:
                direction = 0
                walkRight = False
                walkLeft = True
            if event.key == K_UP:
                goUp = True
            if event.key == K_SPACE:
                shootBullet = True
        if event.type == KEYUP:
            walkRight = False
            walkLeft = False
                 
    pygame.display.update()
 
        
  
