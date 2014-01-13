#Creating the Person class
#By Tyler Spadgenske
import pygame, sys
from pygame.locals import *

pygame.init()

class Person(object): #Create the Person class
    '''
The Person() class
***********************
The person class is one of the most important class
in the Taco Chronlicles. It creates the characters,
including Dr. Taco, the main character. It handles the
weapons, and shoots bullets on command.
'''
    def __init__(self, character, windowSurface, officerX, officerGunX):
        self.JUMP_SPEED = 5 #Must be multiple of "self.JUMP_HEIGHT"
        self.JUMP_HEIGHT = -120 #In pixels Remember, it must be lower than zero.
        self.MOVING_SPEED = 6 #Pixels per loop rotation
        self.SHOTS_TILL_COPS_DEATH = 5
        self._SHOTS_TILL_TACOS_DEATH = 20
        self.x = 100
        self.y = 100
        self.jumpCount = 0
        self.countWalk = 0
        self.takeStep = False
        self.countJump = 0
        self.location = [{'right':130, 'left':72},{'right':officerGunX['right'], 'left':officerGunX['left']}]
        self.centered = False

        #Some Colors
        self.WHITE = (0, 255, 255)
        self.BLACK = (0, 0, 0)
        
        self.character = character
        self.windowSurface = windowSurface

        #Create Doctor Taco Images
        #Initialize Dr. Taco standing right image
        self.DrTacoRightImage = pygame.image.load('Characters\\DrTacoRight.gif')

        #Initialize Dr. Taco rect
        self.rect = self.DrTacoRightImage.get_rect()
        self.rect.centerx = 152
        self.rect.centery = 535
        self.DrTacoRight = pygame.transform.scale(self.DrTacoRightImage, (80, 110))

        #Initialize Dr. Taco walking right image
        self.tacoImage2 = pygame.image.load('Characters\\DrTacoWalkRight.gif')

        #Initialize Dr. Taco walking rect
        self.rect2 = self.tacoImage2.get_rect()
        self.rect2.centerx = 150
        self.rect2.centery = 535
        self.DrTacoWalkRight = pygame.transform.scale(self.tacoImage2, (80, 110))
        
        #Initialize Dr. Taco walking left image
        self.tacoWalkLeftImage = pygame.image.load('Characters\\DrTacoWalkLeft.gif')
        self.DrTacoWalkLeft = pygame.transform.scale(self.tacoWalkLeftImage, (80, 110))

        #Initialize Dr. Taco standing left image
        self.tacoLeftImage = pygame.image.load('Characters\\DrTacoLeft.gif')
        self.DrTacoLeft = pygame.transform.scale(self.tacoLeftImage, (80, 110))

        self.DrTacoStandingImages = [self.DrTacoLeft, self.DrTacoRight]
        self.DrTacoWalkingImages = [self.DrTacoWalkLeft, self.DrTacoWalkRight]

        #Create Officer images   
        #Initialize officer standing right image
        self.officerRightImage = pygame.image.load('Characters\\officerRight.gif')

        #Initialize officer rect
        self.officerRect = self.officerRightImage.get_rect()
        self.officerRect.centerx = officerX
        self.officerRect.centery = 528
        self.officerRight = pygame.transform.scale(self.officerRightImage, (70, 100))

        #Initialize officer walking right image
        self.officerImage2 = pygame.image.load('Characters\\officerWalkRight.gif')

        #Initialize officer walking rect
        self.officerRect2 = self.officerImage2.get_rect()
        self.officerRect2.centerx = officerX
        self.officerRect2.centery = 528
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
            self.gunRect.centery = self.rect.centery + 30
        if self.character == 'officer':
            self.gunRect[1] = 480

        #Setup the bullets
        self.bullets = []
        self.shootBullet = True
        self.num = 0
        self.bulletDirection = []
        self.bulletNum = 0
        self.hitBullet = -1
        self.wound = 0
        self.drop = False

        #Setup sound
        self.gunshot = pygame.mixer.Sound('sound\\gunshot.wav')
        self.gunclick = pygame.mixer.Sound('sound\\gunclick.wav')
        
    def get_rect(self):
        if self.character == 'Doctor Taco':
            return self.rect
        if self.character == 'officer':
            return self.officerRect

    def get_gun_rect(self):
        return self.gunRect

    def move(self, rect, walkingRect, location):
        centered = False
        if rect[0] < 600:
            rect[0] += self.MOVING_SPEED
            walkingRect[0] += self.MOVING_SPEED
            self.location[0]['right'] += self.MOVING_SPEED
            self.location[0]['left'] += self.MOVING_SPEED
        else: centered = True
        return rect, walkingRect, location, centered

    def shot(self, bulletList, bulletDirList, score, target_rect, message, hit):
        if self.drop == False:
            if target_rect != None:
                for every_bullet in bulletList:
                    if every_bullet.colliderect(target_rect):
                        bulletList.pop()
                        bulletDirList.pop()
                        self.wound += 1
                        if self.character == 'officer':
                            hit = True
                if self.character == 'Doctor Taco':
                    if self.wound == self.SHOTS_TILL_COPS_DEATH:
                        if self.character == 'Doctor Taco':
                            message = 'Nice Shot!'
                            score += 100
                        self.wound = -100
                        self.drop = True

                if self.character == 'officer':
                    if self.wound == self.SHOTS_TILL_TACOS_DEATH:
                        if self.character == 'officer':
                            print 'Your dead!'
                        self.wound = -100
                        self.drop = True

        return score, message, hit

    def burned():
        pass
                
    def walk(self, takeStep, direction, walkLeft, walkRight, officerX): #This function is used to make Dr. Taco move his legs from walking position to standing.
        self.officerRect[0] = officerX
        self.officerRect2[0] = officerX
        self.countWalk += 1
        if self.countWalk == 5:
            self.takeStep = False
        if self.countWalk == 20:
            self.countWalk = 0
            if walkRight or walkLeft:
                self.takeStep = True
                
        if self.character == 'Doctor Taco' and takeStep == False:
            self.windowSurface.blit(self.DrTacoStandingImages[direction], self.rect)
        if self.character == 'officer':
            self.windowSurface.blit(self.officerStandingImages[direction], self.officerRect)
        if takeStep == True:
             if self.character == 'Doctor Taco':
                self.windowSurface.blit(self.DrTacoWalkingImages[direction], self.rect2)
                self.rect, self.rect2, self.location, self.centered = self.move(self.rect, self.rect2, self.location)
             if self.character == 'officer':
                 self.windowSurface.blit(self.officerWalkingImages[direction], self.officerRect2)
                 
        return self.takeStep, self.centered #Return takeStep so it knows what position it is in.
        
    def jump(self, goUp): #Draws character jumping up and going down.
        if self.countJump == self.JUMP_HEIGHT:
            goUp = False
        if goUp:
            if self.character == 'Doctor Taco':
                self.rect[1] -= self.JUMP_SPEED
                self.rect2[1] -= self.JUMP_SPEED
            if self.character == 'officer':
                self.officerRect[1] -= self.JUMP_SPEED
                self.officerRect2[1] -= self.JUMP_SPEED
            self.countJump -= self.JUMP_SPEED
            self.gunRect[1] -= self.JUMP_SPEED
        elif goUp == False:
            if self.character == 'Doctor Taco':
                self.rect[1] += self.JUMP_SPEED
                self.rect2[1] += self.JUMP_SPEED
            if self.character == 'officer':
                self.officerRect[1] += self.JUMP_SPEED
                self.officerRect2[1] += self.JUMP_SPEED
            self.countJump += self.JUMP_SPEED
            self.gunRect[1] += self.JUMP_SPEED
        if self.countJump == 0:
            goUp = None
        return goUp
        
    def shootPistol(self, shootBullet, hit, direction, officerGunX, sound, target_rect = None, ammoLeft = 0, message = '', score = 0): #Fires bullets and moves pistol to right location
        self.location[1]['right'] = officerGunX['right']
        self.location[1]['left'] = officerGunX['left']
        self.message = message
        if direction == 1:
            if  self.character == 'Doctor Taco':
                self.gunRect[0] = self.location[0]['right']
            if self.character == 'officer':
                self.gunRect[0] = self.location[1]['right']
            self.windowSurface.blit(self.right9mm, self.gunRect)
        if direction == 0:
            if self.character == 'Doctor Taco':
                self.gunRect[0] = self.location[0]['left']
            if self.character == 'officer':
                self.gunRect[0] = self.location[1]['left']
            self.windowSurface.blit(self.left9mm, self.gunRect)
        if shootBullet == True:
            if ammoLeft > 0 and self.character == 'Doctor Taco':
                self.bullets.append(pygame.Rect(self.gunRect[0], self.gunRect[1], 4, 4))
                self.bulletDirection.append(direction)
                shootBullet = False
                ammoLeft -= 1
                if sound:
                    self.gunshot.stop()
                    self.gunshot.play()
            if ammoLeft <= 0 and self.character == 'Doctor Taco':
                if sound:
                    self.gunclick.stop()
                    self.gunclick.play()
                self.message = 'No Ammo Left!'
            else:
                self.gunclick.stop()
            if self.character == 'officer':
                self.bullets.append(pygame.Rect(self.gunRect[0], self.gunRect[1], 4, 4))
                self.bulletDirection.append(direction)
                shootBullet = False
                if sound:
                    self.gunshot.stop()
                    self.gunshot.play()
                
        if self.character == 'Doctor Taco':
            score, self.message, hit = self.shot(self.bullets, self.bulletDirection, score, target_rect, self.message, hit)
        if self.character == 'officer':
            score, self.message, hit = self.shot(self.bullets, self.bulletDirection, score, target_rect, self.message, hit)
                
        for i in self.bullets:
            pygame.draw.rect(self.windowSurface, self.BLACK, i)
        for i in self.bullets:
            if self.bulletDirection[self.bulletNum] == 0:
                i[0] -= 10
            else:
                i[0] += 10
        #If bullets go off screen remove them from list.
        for bullet in self.bullets:
            if bullet[0] > 1200 or bullet[0] < 0:
                self.bullets.remove(bullet)
                
            self.bulletNum += 1
            self.num += 1
        self.bulletNum = 0
        self.num = 0
        
        return shootBullet, hit, ammoLeft, self.message, score, self.officerRect[1], self.drop           

#Total of 270 lines
