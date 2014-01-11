#Baddie Module By Tyler Spadgenske
import pygame, sys
from pygame.locals import *
#Custom Modules
import person   
pygame.init()

WINDOWWIDTH = 1200
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('Baddie AI Module (Version 0.0.1)')
mainClock = pygame.time.Clock()
WHITE = (255, 255, 255)
windowSurface.fill(WHITE)

#Setup variables
direction = 1
walkLeft = False
walkRight = False
goUp = None
shootBullet = False
skillLevel = 800
x = 900
character = 'officer'

class AI(person.Person):
    def __init__(self, skillLevel):
        self.skillLevel = skillLevel
        self.walkLeft = False
        self.walkRight = False
        self.takeStep = False
        self.direction = 0
        self.baddieX = 50
        self.baddieGunX = {'right':abs(self.baddieX) - 16, 'left':self.baddieX + 5600}
        self.shoot = False
        self.time = 0
        super(AI, self).__init__(character, windowSurface, abs(self.baddieX), self.baddieGunX)

    def move(self):
        if self.direction == 0:
            self.baddieX -= 2
            self.baddieGunX['right'] -= 2
            self.baddieGunX['left'] -= 2
        if self.direction == 1:
            self.baddieX += 2
            self.baddieGunX['right'] += 2
            self.baddieGunX['left'] += 2
        return self.baddieX, self.baddieGunX['right'], self.baddieGunX['left']
    
    def think(self,  x):
        self.time += 1
        #Deside whether to walk forward or shoot left
        if x < self.baddieX:
            if abs(self.baddieX - x) < self.skillLevel:
                self.direction = 0
                self.walkLeft = True
                self.walkRight = False
                if self.baddieX - x > 399:
                    self.baddieX, self.baddieGunX['right'], self.baddieGunX['left'] = self.move()
            if self.baddieX - x < 400:
                self.walkLeft = False
                self.walkRight = False
                if self.time == 20:
                    self.shoot = True

        #Deside whether to walk right or shoot right
        else:
            if abs(self.baddieX) + self.skillLevel <= x:
                self.direction = 1
                self.walkLeft = False
                self.walkRight = True
                if abs(self.baddieX) + 400 <= x:
                    self.baddieX, self.baddieGunX['right'], self.baddieGunX['left'] = self.move()
            if abs(self.baddieX) + 400 >= x - 400:
                self.direction = 1
                self.walkLeft = False
                self.walkRight = False
                if self.time == 20:
                    self.shoot = True
      
        self.takeStep = super(AI, self).walk(self.takeStep, self.direction, self.walkLeft, self.walkRight, self.baddieX) 
        self.shoot = super(AI, self).shootPistol(self.shoot, self.direction, self.baddieGunX)

        if self.time == 20:
            self.time = 0
            

    def die(self):
        pass

    def shoot(self):
        pass
    
badGuy = AI(skillLevel)
while True:
    badGuy.think(x)
    mainClock.tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
  
