#Creating the Person class
#By Tyler Spadgenske
#TODO: Add more functions and make file more orderly.
import pygame, sys, random
from pygame.locals import *
pygame.init()

from popups import Popups

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
        self.MOVING_SPEED = 10 #Pixels per loop rotation
        self.SHOTS_TILL_COPS_DEATH = 5
        self._SHOTS_TILL_TACOS_DEATH = 20
        self.x = 100
        self.y = 100
        self.jumpCount = 0
        self.countWalk = 0
        self.takeStep = False
        self.countJump = 0
        self.location = {'9mm':[{'right':130, 'left':72},{'right':officerGunX['right'], 'left':officerGunX['left']}], 'AK-47':[{'right':117, 'left':50}], 'shotgun':
                         [{'right':117, 'left':10}],'bazooka': [{'right':100, 'left':40}], 'flamethrower': [{'right':130, 'left':30}]}
        self.centered = False

        self.endgame = Popups(windowSurface)
        #Some Colors
        self.WHITE = (0, 255, 255)
        self.BLACK = (0, 0, 0)
        
        self.character = character
        self.windowSurface = windowSurface

        #Create Doctor Taco Images
        #Initialize Dr. Taco standing right image
        self.DrTacoRightImage = pygame.image.load('files\\Characters\\DrTacoRight.gif')

        #Initialize Dr. Taco rect
        self.rect = self.DrTacoRightImage.get_rect()
        self.rect.centerx = 152
        self.rect.centery = 535
        self.DrTacoRight = pygame.transform.scale(self.DrTacoRightImage, (80, 110))

        #Initialize Dr. Taco walking right image
        self.tacoImage2 = pygame.image.load('files\\Characters\\DrTacoWalkRight.gif')

        #Initialize Dr. Taco walking rect
        self.rect2 = self.tacoImage2.get_rect()
        self.rect2.centerx = 150
        self.rect2.centery = 535
        self.DrTacoWalkRight = pygame.transform.scale(self.tacoImage2, (80, 110))
        
        #Initialize Dr. Taco walking left image
        self.tacoWalkLeftImage = pygame.transform.flip(self.DrTacoWalkRight, True, False)
        self.DrTacoWalkLeft = pygame.transform.scale(self.tacoWalkLeftImage, (80, 110))

        #Initialize Dr. Taco standing left image
        self.tacoLeftImage = pygame.transform.flip(self.DrTacoRight, True, False)
        self.DrTacoLeft = pygame.transform.scale(self.tacoLeftImage, (80, 110))

        self.DrTacoStandingImages = [self.DrTacoLeft, self.DrTacoRight]
        self.DrTacoWalkingImages = [self.DrTacoWalkLeft, self.DrTacoWalkRight]

        #Create Officer images   
        #Initialize officer standing right image
        self.color = random.choice(['red', 'green', 'blue', 'yellow'])
        if self.color == 'red':
            self.monster = 'files\\Characters\\red.png'
            self.monsterW = 'files\\Characters\\redW.png'
        if self.color == 'green':
            self.monster = 'files\\Characters\\green.png'
            self.monsterW = 'files\\Characters\\greenW.png'
        if self.color == 'blue':
            self.monster = 'files\\Characters\\blue.png'
            self.monsterW = 'files\\Characters\\blueW.png'
        if self.color == 'yellow':
            self.monster = 'files\\Characters\\yellow.png'
            self.monsterW = 'files\\Characters\\yellowW.png'
        
        self.officerRightImage = pygame.image.load(self.monster)

        #Initialize officer rect
        self.officerRect = self.officerRightImage.get_rect()
        self.officerRect.centerx = officerX
        self.officerRect.centery = 463
        self.officerRight = self.officerRightImage

        #Initialize officer walking right image
        self.officerImage2 = pygame.image.load(self.monsterW)

        #Initialize officer walking rect
        self.officerRect2 = self.officerImage2.get_rect()
        self.officerRect2.centerx = officerX
        self.officerRect2.centery = 463
        self.officerWalkRight = self.officerImage2
        
        #Initialize officer walking left image
        self.officerWalkLeftImage = pygame.transform.flip(self.officerWalkRight, True, False)
        self.officerWalkLeft = self.officerWalkLeftImage

        #Initialize officer standing left image
        self.officerLeftImage = pygame.transform.flip(self.officerRight, True, False)
        self.officerLeft = self.officerLeftImage

        self.officerStandingImages = [self.officerLeft, self.officerRight]
        self.officerWalkingImages = [self.officerWalkLeft, self.officerWalkRight]


        #Draw 9mm in hand
        #Initialize 9mm Images
        self.right9mmImage = pygame.image.load('files\\Weapons\\9mmRight.gif')
        self.right9mm = pygame.transform.scale(self.right9mmImage, (20, 15))

        self.left9mm = pygame.transform.flip(self.right9mm, True, False)

        #Setup 9mm rect        
        self.gunRect = self.right9mmImage.get_rect()
        if self.character == 'Doctor Taco':
            self.gunRect.centerx = self.rect.centerx + 110
            self.gunRect.centery = self.rect.centery + 30
        if self.character == 'officer':
            self.gunRect[1] = 470

        #Initialize AK-47 image and rect
        self.rightAKimage = pygame.image.load('files\\Weapons\\AK-47.gif')
        self.AKright = pygame.transform.scale(self.rightAKimage, (65, 55))

        self.AKleft = pygame.transform.flip(self.AKright, True, False)
       
        self.AKgunRect = self.rightAKimage.get_rect()
        self.AKgunRect.centerx = self.rect.centerx + 170
        self.AKgunRect.centery = self.rect.centery + 5
        
        #Initialize shotgun image and rect
        self.rightShotgunimage = pygame.image.load('files\\Weapons\\shotgun.gif')
        self.shotgunRight = pygame.transform.scale(self.rightShotgunimage, (90, 90))

        self.shotgunLeft = pygame.transform.flip(self.shotgunRight, True, False)
       
        self.shotgunRect = self.rightShotgunimage.get_rect()
        self.shotgunRect.centerx = self.rect.centerx + 170
        self.shotgunRect.centery = self.rect.centery + 15

        #Initialize bazooka image and rect
        self.rightBazookaImage = pygame.image.load('files\\Weapons\\bazooka.gif')
        self.bazookaRight = pygame.transform.scale(self.rightBazookaImage, (90, 40))

        self.bazookaLeft = pygame.transform.flip(self.bazookaRight, True, False)
       
        self.bazookaRect = self.rightBazookaImage.get_rect()
        self.bazookaRect.centery = self.rect.centery - 25

        #Create rocket image
        self.rocketRight = pygame.image.load('files\\Weapons\\rocket.png')
        self.rocketLeft = pygame.transform.flip(self.rocketRight, True, False)

        #Initialize flamethrower image and rect
        self.rightFlamethrowerImage = pygame.image.load('files\\Weapons\\flamethrower.gif')
        self.flamethrowerRight = pygame.transform.scale(self.rightFlamethrowerImage, (70, 30))

        self.flamethrowerLeft = pygame.transform.flip(self.flamethrowerRight, True, False)
       
        self.flamethrowerRect = self.flamethrowerRight.get_rect()
        self.flamethrowerRect.centery = self.rect.centery - 50

        #Create flame image
        self.flameRight = pygame.image.load('files\\Weapons\\flame.png')
        self.flameLeft = pygame.transform.flip(self.flameRight, True, False)
        self.flameRect = self.flameRight.get_rect()
        
        #Setup the bullets
        self.bullets = []
        self.shootBullet = True
        self.num = 0
        self.bulletDirection = []
        self.bulletNum = 0
        self.hitBullet = -1
        self.wound = 0
        self.drop = False
        self.reload = False
        self.back = False
        self.die = False
        self.showFlame = False
        self.flameDirection = 1

        #Setup sound
        self.gunshot = pygame.mixer.Sound('files\\sound\\gunshot.wav')
        self.gunclick = pygame.mixer.Sound('files\\sound\\gunclick.wav')
        self.whoosh = pygame.mixer.Sound('files\\sound\\rocket.wav')
        self.flame = pygame.mixer.Sound('files\\sound\\flame.wav')
        
    #This function returns the characters rect
    def get_rect(self):
        if self.character == 'Doctor Taco':
            return self.rect
        if self.character == 'officer':
            return self.officerRect

    #This function returns the characters gun rect
    def get_gun_rect(self):
        return self.gunRect

    #This function moves Dr. Taco (and his gun) at the beginning of the game to center screen
    def move(self, rect, walkingRect, location, weapon):
        centered = False
        if rect[0] < 600:
            rect[0] += self.MOVING_SPEED
            walkingRect[0] += self.MOVING_SPEED
            self.location[weapon][0]['right'] += self.MOVING_SPEED
            self.location[weapon][0]['left'] += self.MOVING_SPEED
        else: centered = True
        return rect, walkingRect, location, centered

    def shot(self, bulletList, bulletDirList, score, target_rect, message, hit, weapon = '', lifeLeft = None, flame = False):
        #If person is still alive continue on
        if self.drop == False:
            #If class is run by Doctor Taco continue on
            if target_rect != None:
                for cop in target_rect:
                    for every_bullet in bulletList:
                        #If a bullet hits the closest target remove it from bullet list
                        if self.character == 'Doctor Taco':
                            #If bullet collides with cops rectangle.
                            if every_bullet.colliderect(cop.get_rect()):
                                #Remove the bullet from list unless it is flame from the flamethrower.
                                if weapon != 'flamethrower':
                                    bulletList.pop()
                                    bulletDirList.pop()
                                #If Dr. Taco is using the bazooka, give cop even more damage.
                                if weapon == 'bazooka':
                                    self.wound += self.SHOTS_TILL_COPS_DEATH - 1
                                self.wound += 1
                        else:
                            #If a bullet collides with Dr. Taco remove it from list and set hit to true to lower health beam.
                            if every_bullet.colliderect(target_rect):
                                bulletList.pop()
                                bulletDirList.pop()
                                if flame == False:
                                    hit = True
                                    lifeLeft += 1
                                
                    if self.character == 'Doctor Taco':
                        #If person is Dr. Taco and the officer has been hit the maximum times, add score and stop blitting the person
                        if self.wound >= self.SHOTS_TILL_COPS_DEATH:
                            if self.character == 'Doctor Taco':
                                message = 'Nice Shot!'
                                score += 100
                            self.wound = 0
                            target_rect.remove(cop)
                            break

                    if self.character == 'officer':
                        if lifeLeft == self.SHOTS_TILL_TACOS_DEATH:
                            #If Dr. Taco is dead, end game
                            self.reload, self.back = self.endgame.endgame()
                            lifeLeft = -100
                            self.drop = True
                        
        return score, message, hit, self.reload, self.back, lifeLeft
                
    def walk(self, takeStep, direction, walkLeft, walkRight, weapon, officerX = None): #This function is used to make Dr. Taco move his legs from walking position to standing.
        if officerX != None:
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
                self.rect, self.rect2, self.location, self.centered = self.move(self.rect, self.rect2, self.location, weapon)
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
            self.AKgunRect[1] -= self.JUMP_SPEED
            self.shotgunRect[1] -= self.JUMP_SPEED
            self.bazookaRect[1] -= self.JUMP_SPEED
            self.flamethrowerRect[1] -= self.JUMP_SPEED
        elif goUp == False:
            if self.character == 'Doctor Taco':
                self.rect[1] += self.JUMP_SPEED
                self.rect2[1] += self.JUMP_SPEED
            if self.character == 'officer':
                self.officerRect[1] += self.JUMP_SPEED
                self.officerRect2[1] += self.JUMP_SPEED
            self.countJump += self.JUMP_SPEED
            self.gunRect[1] += self.JUMP_SPEED
            self.AKgunRect[1] += self.JUMP_SPEED
            self.shotgunRect[1] += self.JUMP_SPEED
            self.bazookaRect[1] += self.JUMP_SPEED
            self.flamethrowerRect[1] += self.JUMP_SPEED
        if self.countJump == 0:
            goUp = None
        return goUp
        
    def shootPistol(self, shootBullet, hit, direction, officerGunX, sound, target_rect = None, ammoLeft = 0, message = '', score = 0, lifeLeft = None, flame = False): 
        #Get message box value and setup the cops location
        self.location['9mm'][1]['right'] = officerGunX['right']
        self.location['9mm'][1]['left'] = officerGunX['left']

        #Move gun to correct position for Dr. Taco
        if self.character == 'Doctor Taco':
            if self.get_rect()[0] > 599:
                self.location['9mm'][0]['right'] = 660
                self.location['9mm'][0]['left'] = 600
        self.message = message
        #If person is facing right set coordinates and blit gun to screen
        if direction == 1:
            if  self.character == 'Doctor Taco':
                self.gunRect[0] = self.location['9mm'][0]['right']
            if self.character == 'officer':
                self.gunRect[0] = self.location['9mm'][1]['right']
            self.windowSurface.blit(self.right9mm, self.gunRect)
        #If person is facing left set coordinates and blit gun to screen
        if direction == 0:
            if self.character == 'Doctor Taco':
                self.gunRect[0] = self.location['9mm'][0]['left']
            if self.character == 'officer':
                self.gunRect[0] = self.location['9mm'][1]['left']
            self.windowSurface.blit(self.left9mm, self.gunRect)
        #If gun is fired add a bullet to the bullet list with its direction. Then, subtract one from ammLeft
        if shootBullet == True:
            if ammoLeft > 0 and self.character == 'Doctor Taco':
                self.bullets.append(pygame.Rect(self.gunRect[0], self.gunRect[1], 4, 4))
                self.bulletDirection.append(direction)
                shootBullet = False
                ammoLeft -= 1
                #If the sound is on stop previous sound and play the gun shot
                if sound:
                    self.gunshot.stop()
                    self.gunshot.play()
            # If your out of ammo, play a click and change the message
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

        #If run self.shot() to move bullets and determin whether the person is dead
        if self.character == 'Doctor Taco':
            score, self.message, hit, self.die, self.back, lifeLeft = self.shot(self.bullets, self.bulletDirection, score,
                                                                                target_rect, self.message, hit, lifeLeft = lifeLeft)
        if self.character == 'officer':
            score, self.message, hit, self.die, self.back, lifeLeft = self.shot(self.bullets, self.bulletDirection, score,
                                                                                target_rect, self.message, hit, lifeLeft = lifeLeft, flame = flame)

        # for every bullet in the bullet list blit it and move it in the correct direction
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
                self.bullets.pop()
                self.bulletDirection.pop()
                
            self.bulletNum += 1
            self.num += 1
        self.bulletNum = 0
        self.num = 0

        return shootBullet, hit, ammoLeft, self.message, score, self.officerRect[1], self.drop, self.die, self.back, lifeLeft

    def shootAK(self, shootBullet, hit, direction, officerGunX, sound, target_rect = None, ammoLeft = 0, message = '', score = 0, lifeLeft = None):
        #Get message box value
        self.message = message

        #Move gun to correct position for Dr. Taco
        if self.character == 'Doctor Taco':
            if self.get_rect()[0] > 599:
                self.location['AK-47'][0]['right'] = 650
                self.location['AK-47'][0]['left'] = 570
                
        #If person is facing right set coordinates and blit gun to screen
        if direction == 1:
            if  self.character == 'Doctor Taco':
                self.AKgunRect[0] = self.location['AK-47'][0]['right']
            self.windowSurface.blit(self.AKright, self.AKgunRect)
            
        #If person is facing left set coordinates and blit gun to screen
        if direction == 0:
            if self.character == 'Doctor Taco':
                self.AKgunRect[0] = self.location['AK-47'][0]['left']
            self.windowSurface.blit(self.AKleft, self.AKgunRect)
            
        #If gun is fired add a bullet to the bullet list with its direction. Then, subtract one from ammoLeft
        if shootBullet == True:
            if ammoLeft > 0:
                self.bullets.append(pygame.Rect(self.AKgunRect[0] + 15, self.AKgunRect[1] + 20, 4, 4))
                self.bulletDirection.append(direction)
                ammoLeft -= 1
                #If the sound is on stop previous sound and play the gun shot
                if sound:
                    self.gunshot.play()
            # If your out of ammo, play a click and change the message
            if ammoLeft <= 0:
                if sound:
                    self.gunclick.stop()
                    self.gunclick.play()
                self.message = 'No Ammo Left!'
            else:
                self.gunclick.stop()

        #If run self.shot() to move bullets and determin whether the person is dead
        if self.character == 'Doctor Taco':
            score, self.message, hit, self.die, self.back, lifeLeft = self.shot(self.bullets, self.bulletDirection, score, target_rect,
                                                                                self.message, hit, lifeLeft = lifeLeft)

        # for every bullet in the bullet list blit it and move it in the correct direction
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
                self.bullets.pop()
                self.bulletDirection.pop()
                break
                
            self.bulletNum += 1
            self.num += 1
        self.bulletNum = 0
        self.num = 0

        return shootBullet, hit, ammoLeft, self.message, score, self.officerRect[1], self.drop, self.die, lifeLeft
        
    def shootShotgun(self, shootBullet, hit, direction, officerGunX, sound, target_rect = None, ammoLeft = 0, message = '', score = 0, lifeLeft = None):
        #Get message box value
        self.message = message

        #Move gun to correct position for Dr. Taco
        if self.character == 'Doctor Taco':
            if self.get_rect()[0] > 599:
                self.location['shotgun'][0]['right'] = 645
                self.location['shotgun'][0]['left'] = 550
                
        #If person is facing right set coordinates and blit gun to screen
        if direction == 1:
            if  self.character == 'Doctor Taco':
                self.shotgunRect[0] = self.location['shotgun'][0]['right']
            self.windowSurface.blit(self.shotgunRight, self.shotgunRect)
            
        #If person is facing left set coordinates and blit gun to screen
        if direction == 0:
            if self.character == 'Doctor Taco':
                self.shotgunRect[0] = self.location['shotgun'][0]['left']
            self.windowSurface.blit(self.shotgunLeft, self.shotgunRect)
            
        #If gun is fired add a bullet to the bullet list with its direction. Then, subtract one from ammoLeft
        if shootBullet == True:
            if ammoLeft > 0:
                self.bullets.append(pygame.Rect(self.shotgunRect[0] + 40, self.shotgunRect[1] + 30, 4, 4))
                self.bullets.append(pygame.Rect(self.shotgunRect[0] + 40, self.shotgunRect[1] + 40, 4, 4))
                self.bullets.append(pygame.Rect(self.shotgunRect[0] + 40, self.shotgunRect[1] + 50, 4, 4))
                self.bulletDirection.append(direction)
                self.bulletDirection.append(direction)
                self.bulletDirection.append(direction)
                shootBullet = False
                ammoLeft -= 3
                #If the sound is on stop previous sound and play the gun shot
                if sound:
                    self.gunshot.play()
            # If your out of ammo, play a click and change the message
            if ammoLeft <= 0:
                if sound:
                    self.gunclick.stop()
                    self.gunclick.play()
                self.message = 'No Ammo Left!'
            else:
                self.gunclick.stop()

        #If run self.shot() to move bullets and determin whether the person is dead
        if self.character == 'Doctor Taco':
            score, self.message, hit, self.die, self.back, lifeLeft = self.shot(self.bullets, self.bulletDirection, score,
                                                                               target_rect, self.message, hit, lifeLeft = lifeLeft)

        # for every bullet in the bullet list blit it and move it in the correct direction
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
                self.bullets.pop()
                self.bulletDirection.pop()
                
            self.bulletNum += 1
            self.num += 1
        self.bulletNum = 0
        self.num = 0

        return shootBullet, hit, ammoLeft, self.message, score, self.officerRect[1], self.drop , self.die, lifeLeft

    def shootBazooka(self, shootBullet, hit, direction, officerGunX, sound, target_rect = None, ammoLeft = 0, message = '', score = 0, weapon = '', lifeLeft = None):
        #Get message box value 
        self.message = message

        #Move gun to correct position for Dr. Taco
        if self.character == 'Doctor Taco':
            if self.get_rect()[0] > 599:
                self.location['bazooka'][0]['right'] = 625
                self.location['bazooka'][0]['left'] = 570
                
        #If person is facing right set coordinates and blit gun to screen
        if direction == 1:
            if self.character == 'Doctor Taco':
                self.bazookaRect[0] = self.location['bazooka'][0]['right']
            self.windowSurface.blit(self.bazookaRight, self.bazookaRect)
            
        #If person is facing left set coordinates and blit gun to screen
        if direction == 0:
            if self.character == 'Doctor Taco':
                self.bazookaRect[0] = self.location['bazooka'][0]['left']
            self.windowSurface.blit(self.bazookaLeft, self.bazookaRect)
            
        #If gun is fired add a bullet to the bullet list with its direction. Then, subtract one from ammoLeft
        if shootBullet == True:
            if ammoLeft > 0:
                self.bullets.append(pygame.Rect(self.bazookaRect[0] + 40, self.bazookaRect[1] + 10, 4, 4))
                self.bulletDirection.append(direction)
                shootBullet = False
                ammoLeft -= 1
                #If the sound is on stop previous sound and play the gun shot
                if sound:
                    self.whoosh.play()
            # If your out of ammo, play a click and change the message
            if ammoLeft <= 0:
                if sound:
                    self.gunclick.stop()
                    self.gunclick.play()
                self.message = 'No Ammo Left!'
            else:
                self.gunclick.stop()

        #If run self.shot() to move bullets and determin whether the person is dead
        if self.character == 'Doctor Taco':
            score, self.message, hit, self.die, self.back, lifeLeft = self.shot(self.bullets, self.bulletDirection, score, target_rect, self.message, hit,
                                                                     weapon, lifeLeft = lifeLeft)

        # for every bullet in the bullet list blit it and move it in the correct direction
        for rect in self.bullets:
            if self.bulletDirection[self.num] == 1:
                self.windowSurface.blit(self.rocketRight, rect)
            else:
                self.windowSurface.blit(self.rocketLeft, rect)
            self.num += 1
        self.num = 0
        for i in self.bullets:
            if self.bulletDirection[self.bulletNum] == 0:
                i[0] -= 10
            else:
                i[0] += 10
                
        #If bullets go off screen remove them from list.
        for bullet in self.bullets:
            if bullet[0] > 1200 or bullet[0] < 0:
                self.bullets.pop()
                self.bulletDirection.pop()
                
            self.bulletNum += 1
            self.num += 1
        self.bulletNum = 0
        self.num = 0

        return shootBullet, hit, ammoLeft, self.message, score, self.officerRect[1], self.drop , self.die, lifeLeft

    def shootFlame(self, shootBullet, hit, direction, officerGunX, sound, target_rect = None, ammoLeft = 0, message = '', score = 0, weapon = '', lifeLeft = None):
        #Get message box value
        self.message = message

        #Move gun to correct position for Dr. Taco
        if self.character == 'Doctor Taco':
            if self.get_rect()[0] > 599:
                self.location['flamethrower'][0]['right'] = 645
                self.location['flamethrower'][0]['left'] = 550
                
        #If person is facing right set coordinates and blit gun to screen
        if direction == 1:
            if  self.character == 'Doctor Taco':
                self.flamethrowerRect[0] = self.location['flamethrower'][0]['right']
            self.windowSurface.blit(self.flamethrowerRight, self.flamethrowerRect)
            self.flameDirection = 1
            
        #If person is facing left set coordinates and blit gun to screen
        if direction == 0:
            if self.character == 'Doctor Taco':
                self.flamethrowerRect[0] = self.location['flamethrower'][0]['left']
            self.windowSurface.blit(self.flamethrowerLeft, self.flamethrowerRect)
            self.flameDirection = 0
            
        #If gun is fired add a bullet to the bullet list with its direction. Then, subtract one from ammoLeft
        if shootBullet == True:
            if ammoLeft > 0:
                self.showFlame = True
                self.flameDirection = direction
                ammoLeft -= .1
                #If the sound is on stop previous sound and play the gun shot
                if sound:
                    self.flame.play()
            # If your out of ammo, play a click and change the message
            if ammoLeft <= 0:
                self.showFlame = False
                self.shootBullet = False
                if sound:
                    self.gunclick.stop()
                    self.gunclick.play()
                self.message = 'No Ammo Left!'
            else:
                self.gunclick.stop()

        else:
            self.showFlame = False
            self.flame.stop()

        #If run self.shot() to move bullets and determin whether the person is dead
        if self.character == 'Doctor Taco':
            score, self.message, hit, self.die, self.back, lifeLeft = self.shot([self.flameRect], self.bulletDirection, score, target_rect, self.message, hit, 'flamethrower',
                                                                     lifeLeft = lifeLeft)

        # for every bullet in the bullet list blit it and move it in the correct direction
        if self.showFlame:
            if self.flameDirection == 1:
                self.flameRect[0] = self.flamethrowerRect[0] + 60
                self.flameRect[1] = self.flamethrowerRect[1] - 45
                self.windowSurface.blit(self.flameRight, self.flameRect)
            if self.flameDirection == 0:
                self.flameRect[0] = self.flamethrowerRect[0] - 60
                self.flameRect[1] = self.flamethrowerRect[1] - 45
                self.windowSurface.blit(self.flameLeft, self.flameRect)
                
                
            self.bulletNum += 1
            self.num += 1
        self.bulletNum = 0
        self.num = 0

        return shootBullet, hit, ammoLeft, self.message, score, self.officerRect[1], self.drop , self.die, lifeLeft, self.showFlame
        
