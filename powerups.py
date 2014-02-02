#The Powerups class
import pygame, sys
from pygame.locals import *

class Powerups(object):
    '''
The Powerups class
*********************
The Powerups class is a class written to put power ups in the game.
In the Taco Chronicles, there are three power ups: taco, health, and ammo.
Each powerup is its own function.

object.__init__(surface, score)
The __init__ fuction take just two pieces of data:

The screen the powerups should be blit to
The current score so when the powerups are recieved the score increases.


score, ammo = object.ammoBox(x, y, rect, ammo):
The ammoBox function takes three pieces of dat to sucessfully put the box on the screen.

x: the x coordinate of the box.
y: the y coordinate of the box.
rect: the rect object that will run into the box.
ammo: the current amount of ammo.

score = object.taco(x, y, rect)
The taco function takes almost the same data as the ammoBox function.

x: The x coordinate of the box.
y: The y coordinate of the box.
rect: The rect object that will run into the box.

score, health = object.healthBox(x, y, rect, health)
The healthBox fuction is also very similar to the ammoBox function.

x: The x coordinate of the box.
y: The y coordinate of the box.
rect: The rect object that will run into the box.
health: the current amount of health left in the player.

More Info
************
Use the Powerups class in the Toolbar class.
'''
    def __init__(self, windowSurface, score):
        self.windowSurface = windowSurface
        self.score = score
        self.clear = False
        self.sound = pygame.mixer.Sound('sound\\powerupSound.wav')
        

    def ammoBox(self, x, y, rect, ammo, score, sound):
        self.ammoBoxImage = pygame.image.load('powerups\\ammoBox.png')
        self.ammoBoxRect = self.ammoBoxImage.get_rect()
        self.ammoBoxRect[0] = x
        self.ammoBoxRect[1] = y
        if self.clear == False:
            self.windowSurface.blit(self.ammoBoxImage, self.ammoBoxRect)

            if rect[0] in range(self.ammoBoxRect[0] - 50, self.ammoBoxRect[0] + 50):
                score += 25
                ammo += 25
                if sound:
                    self.sound.play()
                self.clear = True
        return score, ammo


    def taco(self, x, y, rect):
        self.tacoImage2 = pygame.image.load('powerups\\taco.png')
        self.tacoImage = pygame.transform.scale(self.tacoImage2, (50, 20))
        self.tacoRect = self.tacoImage.get_rect()
        self.tacoRect[0] = x
        self.tacoRect[1] = y
        self.windowSurface.blit(self.tacoImage, self.tacoRect)

        if rect.colliderect(self.tacoRect):
            self.score += 100
            self.sound.play()
            return self.score
        
    def healthBox(self, x, y, rect, health, sound, score):
        self.healthBoxImage = pygame.image.load('powerups\\healthBox.png')
        self.healthBoxRect = self.healthBoxImage.get_rect()
        self.healthBoxRect[0] = x
        self.healthBoxRect[1] = y
        if self.clear == False:
            self.windowSurface.blit(self.healthBoxImage, self.healthBoxRect)

            if rect[0] in range(self.healthBoxRect[0] - 50, self.healthBoxRect[0] + 50):
                score += 25
                health -= 5
                if sound:
                    self.sound.play()
                self.clear = True

        return score, health
    
    def TNT(self):
        pass
