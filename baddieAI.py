#Baddie AI Module By Tyler Spadgenske
import pygame, sys
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
        self.baddieGunX = {'right':abs(officerX) + 45, 'left':officerX + 7}
        self.time = 0
        self.character = 'officer'
        self.centered = False
        self.reload = False
        self.back = False
        super(AI, self).__init__(self.character, windowSurface, abs(self.baddieX), self.baddieGunX)
        
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
    
    def think(self,  x, baddieX, baddieGunX, dead, hit, sound, gunData):
        gunData['direction'] = self.direction
        print 'A: ',gunData['gunX']
        gunData['gunX'] = self.baddieGunX
        if dead == False:
            self.time += 1
            #Deside whether to walk forward or shoot left
            if x[0] < baddieX:
                if baddieX - x[0] < self.skillLevel and baddieX - x[0] > self.skillLevel / 2:
                    self.direction = 0
                    self.walkLeft = True
                    self.walkRight = False
                    baddieX, gunData['gunX']['right'], gunData['gunX']['left'] = self.move(baddieX, gunData['gunX'])
                else:
                    self.walkLeft = False
                    self.direction = 0
                if baddieX - x[0] <= 398:
                    self.walkLeft = False
                    self.walkRight = False
                    if self.time == 20:
                        gunData['shootBullet'] = True

            #Deside whether to walk right or shoot right
            else:
                if abs(baddieX) + self.skillLevel <= x[0]:
                    self.direction = 1
                    self.walkLeft = False
                    self.walkRight = True
                    if abs(baddieX) + 400 <= x[0]:
                        baddieX, gunData['gunX']['right'], gunData['gunX']['left'] = self.move(baddieX, gunData['gunX'])
                if abs(baddieX) + 400 >= x[0] - 400:
                    self.direction = 1
                    self.walkLeft = False
                    self.walkRight = False
                    if self.time == 30:
                        gunData['shootBullet'] = True
      
            self.takeStep, self.centered = super(AI, self).walk(self.takeStep, self.direction, self.walkLeft, self.walkRight, baddieX, '9mm')
            gunData = super(AI, self).shootPistol(gunData)

        if self.time == 30:
            self.time = 0
        return hit, self.reload
