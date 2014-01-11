import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1200
WINDOWHIEGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
pygame.display.set_caption('power ups class (Version 0.0.1)')
mainClock = pygame.time.Clock()

BLUE = (0,0,255)
WHITE = (255, 255, 255)

block = {'rect':pygame.Rect(200, 200, 50, 50),'color':BLUE}

windowSurface.fill(BLUE)
score = 0
ammo = 0
health = 0
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
        

    def ammoBox(self, x, y, rect, ammo):
        self.ammoBoxImage = pygame.image.load('powerups\\ammoBox.png')
        self.ammoBoxRect = self.ammoBoxImage.get_rect()
        self.ammoBoxRect[0] = x
        self.ammoBoxRect[1] = y
        self.windowSurface.blit(self.ammoBoxImage, self.ammoBoxRect)

        if rect.colliderect(self.ammoBoxRect):
            self.score += 25
            ammo += 15
            return self.score, ammo


    def taco(self, x, y, rect):
        self.tacoImage2 = pygame.image.load('powerups\\taco.png')
        self.tacoImage = pygame.transform.scale(self.tacoImage2, (50, 20))
        self.tacoRect = self.tacoImage.get_rect()
        self.tacoRect[0] = x
        self.tacoRect[1] = y
        self.windowSurface.blit(self.tacoImage, self.tacoRect)

        if rect.colliderect(self.tacoRect):
            self.score += 100
            return self.score
        
    def healthBox(self, x, y, rect, health):
        self.healthBoxImage = pygame.image.load('powerups\\healthBox.png')
        self.healthBoxRect = self.healthBoxImage.get_rect()
        self.healthBoxRect[0] = x
        self.healthBoxRect[1] = y
        self.windowSurface.blit(self.healthBoxImage, self.healthBoxRect)

        if rect.colliderect(self.healthBoxRect):
            health += 50
            self.score += 50
            return self.score, health
    
    def TNT(self):
        pass

test = Powerups(windowSurface, score)
while True:
    test.ammoBox(100, 100, block['rect'], ammo)
    test.taco(500, 200, block['rect'])
    test.healthBox(700, 100, block['rect'], health)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    mainClock.tick()

  
