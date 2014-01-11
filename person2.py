#Creating the Person class
#By Tyler Spadgenske
import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1200 #Set up the window
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Creating the person class (Version 0.0.2)')

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
class Person(): #Create the Person class
    def __init__(self):
        self.x = 100
        self.y = 100
        self.jumpCount = 0
        self.countWalk = 0
        self.takeStep = False
        self.countJump = 0

        #Initialize Dr. Taco standing right image
        self.DrTacoRightImage = pygame.image.load('DrTacoRight.gif')

        #Initialize Dr. Taco rect
        self.rect = self.DrTacoRightImage.get_rect()
        self.rect.centerx = windowSurface.get_rect().centerx
        self.rect.centery = windowSurface.get_rect().centery + 200
        self.DrTacoRight = pygame.transform.scale(self.DrTacoRightImage, (70, 100))

        #Initialize Dr. Taco walking right image
        self.tacoImage2 = pygame.image.load('DrTacoWalkRight.gif')

        #Initialize Dr. Taco walking rect
        self.rect2 = self.tacoImage2.get_rect()
        self.rect2.centerx = windowSurface.get_rect().centerx
        self.rect2.centery = windowSurface.get_rect().centery + 200
        self.DrTacoWalkRight = pygame.transform.scale(self.tacoImage2, (70, 100))
        
        #Initialize Dr. Taco walking left image
        self.tacoWalkLeftImage = pygame.image.load('DrTacoWalkLeft.gif')
        self.DrTacoWalkLeft = pygame.transform.scale(self.tacoWalkLeftImage, (70, 100))

        #Initialize Dr. Taco standing left image
        self.tacoLeftImage = pygame.image.load('DrTacoLeft.gif')
        self.DrTacoLeft = pygame.transform.scale(self.tacoLeftImage, (70, 100))

        self.standingImages = [self.DrTacoLeft, self.DrTacoRight]
        self.walkingImages = [self.DrTacoWalkLeft, self.DrTacoWalkRight]

        #Initialize 9mm Images
        self.right9mmImage = pygame.image.load('Weapons\\9mmRight.gif')
        self.right9mm = pygame.transform.scale(self.right9mmImage, (20, 15))

        self.left9mmImage = pygame.image.load('Weapons\\9mmLeft.gif')
        self.left9mm = pygame.transform.scale(self.left9mmImage, (20, 15))

        #Setup 9mm rect        
        self.gunRect = self.right9mmImage.get_rect()
        self.gunRect.centerx = self.rect.centerx + 110
        self.gunRect.centery = self.rect.centery + 25

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
        windowSurface.blit(self.standingImages[direction], self.rect)
        if takeStep == True:
             windowSurface.fill(WHITE)
             windowSurface.blit(self.walkingImages[direction], self.rect2)
        return self.takeStep #Return takeStep so it knows what position it is in.
        
    def jump(self, goUp):
        if self.countJump == -65:
            goUp = False
        if goUp:
            self.rect[1] -= 5
            self.rect2[1] -= 5
            self.countJump -= 5
            self.gunRect[1] -= 5
        elif goUp == False:
            self.rect[1] += 5
            self.rect2[1] += 5
            self.countJump += 5
            self.gunRect[1] += 5
        if self.countJump == 0:
            goUp = None
        return goUp
        
    def shoot(self, shootBullet):
        if direction == 1: 
            self.gunRect[0] = 573
            windowSurface.blit(self.right9mm, self.gunRect)
        if direction == 0:
            self.gunRect[0] = 518
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

DocTaco = Person()
while True:
    takeStep = DocTaco.walk(takeStep)
    goUp = DocTaco.jump(goUp)
    shootBullet = DocTaco.shoot(shootBullet)
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
 
        
  
