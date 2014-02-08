#Baddie AI Module By Tyler Spadgenske
import pygame, sys, random
from pygame.locals import *
#Custom Modules
from person import Person

class AI(Person):
    '''
The AI class is in charge of the bad guy's intellagence.
it has four functions: get_rect(), get_gun_rect(), move(X, gunX),
and think(x, baddieX, baddieGunX, dead, hit, sound)
get_rect() and get_gun_rect() just return the officer's position, and gun position.
move(x, gunX)is called inside the think() function. It is called when
the officer needs to move forward or backward. think(x, baddieX, baddieGunX,
dead, hit, sound) is the function used in the l1-4 classes. It takes Dr. Taco's position,
it's own position,wether itself is dead or not, a boolean of if a bullet struck itself,
and another boolean the determins if it should play sound.'''
    def __init__(self, windowSurface, skillLevel, officerX):
        self.SHOTS_TILL_COPS_DEATH = 5
        self.SHOTS_TILL_TACOS_DEATH = 20
        self.skillLevel = skillLevel
        self.walkLeft = False
        self.walkRight = False
        self.takeStep = False
        self.direction = 0
        self.baddieX = officerX
        self.baddieGunX = {'right':abs(self.baddieX) + 45, 'left':self.baddieX + 7}
        self.shoot = False
        self.time = 0
        self.characters = ['sheriff', 'deputy']
        self.centered = False
        self.reload = False
        self.back = False
        super(AI, self).__init__('officer', windowSurface, abs(self.baddieX), self.baddieGunX, random.choice(self.characters))

    def get_rect(self):
        return super(AI, self).get_rect()
    
    def get_gun_rect(self):
        return super(AI, self).get_gun_rect()

    def move(self, baddieX, baddieGunX):
        if self.direction == 0:
            baddieX -= 2
            baddieGunX['right'] -= 2
            baddieGunX['left'] -= 2
        if self.direction == 1:
            baddieX += 2
            baddieGunX['right'] += 2
            baddieGunX['left'] += 2
        return baddieX, baddieGunX['right'], baddieGunX['left']
    
    def think(self,  x, baddieX, baddieGunX, dead, hit, sound, lifeLeft):
        if dead == False:
            self.time += 1
            #Deside whether to walk forward or shoot left
            if x[0] < baddieX:
                if baddieX - x[0] < self.skillLevel and baddieX - x[0] > self.skillLevel / 2:
                    self.direction = 0
                    self.walkLeft = True
                    self.walkRight = False
                    baddieX, baddieGunX['right'], baddieGunX['left'] = self.move(baddieX, baddieGunX)
                else:
                    self.walkLeft = False
                    self.direction = 0
                if baddieX - x[0] <= 398:
                    self.walkLeft = False
                    self.walkRight = False
                if baddieX - x[0] <= 500:
                    if self.time == 10:
                        self.shoot = True

            #Deside whether to walk right or shoot right
            else:
                if abs(baddieX) + self.skillLevel <= x[0]:
                    self.direction = 1
                    self.walkLeft = False
                    self.walkRight = True
                    if abs(baddieX) + 400 <= x[0]:
                        baddieX, baddieGunX['right'], baddieGunX['left'] = self.move(baddieX, baddieGunX)
                if abs(baddieX) + 400 >= x[0] - 400:
                    self.direction = 1
                    self.walkLeft = False
                    self.walkRight = False
                if baddieX - x[0] >= 500:
                    if self.time == 10:
                        self.shoot = True
      
            self.takeStep, self.centered = super(AI, self).walk(self.takeStep, self.direction, self.walkLeft, self.walkRight, '9mm', baddieX) 
            self.shoot, hit, ammo, message, score, officerX, drop, self.reload, self.back, lifeLeft = super(AI, self).shootPistol(self.shoot, hit,
                                                                                                                       self.direction, baddieGunX, sound, x,
                                                                                                                       lifeLeft = lifeLeft)

        if self.time == 10:
            self.time = 0

        return hit, self.reload, self.back, lifeLeft
