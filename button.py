# Button class 
# By Tyler Spadgenske

#Import modules
import pygame
from pygame.locals import *
class Button:
    def __init__(self, windowSurface):
        #Setup values
        self.windowSurface = windowSurface
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 0)
        self.ORANGE = (255, 103, 1)
        self.turnColor = False
        self.enlarge_reload = False
        self.reload = False
        self.enlarge_back = False
        self.back = False
        self.enlarge_sound = False
        self.enlarge_pause = False
        self.exit = False

        #Setup stuff for startButton()
        self.comicFont = pygame.font.Font('/home/pi/Taco-Chronicles/files/font/font.ttf', 60)
        self.buttonColor = [self.WHITE, self.ORANGE]
    def arrow(self, clickedOn, event, coords): #coords example: [695, 30, 735, 30, 715, 50]
        #Detect whether the mouse is on the triangle, if
        #so, make triangle yellow. If you click, drop down the menu.
        if event.type == MOUSEBUTTONDOWN:
            if event.pos[0] > coords[0] and event.pos[0] < coords[2]:
                if event.pos[1] > coords[1] and event.pos[1] < coords[5]:
                    self.turnColor = True
                    if clickedOn == True:
                        clickedOn = False
                    else:
                        clickedOn = True
        if event.type == MOUSEMOTION:
            if event.pos[0] > coords[0] and event.pos[0] < coords[2]:
                if event.pos[1] > coords[1] and event.pos[1] < coords[5]:
                    self.turnColor = True                       
                else:
                    self.turnColor = False
            else:
                self.turnColor = False
        return clickedOn
    def blitArrow(self, windowSurface, clickedOn, coords):
        #Change triangle color based on mouse position.
        if self.turnColor:
            if clickedOn:
                self.chooseGunButton = pygame.draw.polygon(windowSurface, self.YELLOW, ((coords[0], coords[5]), (coords[4], coords[1]), (coords[2], coords[5])))
            else:
                self.chooseGunButton = pygame.draw.polygon(windowSurface, self.YELLOW, ((coords[0], coords[1]), (coords[4], coords[5]), (coords[2], coords[1])))
        else:
            if clickedOn:
                self.chooseGunButton = pygame.draw.polygon(windowSurface, self.WHITE, ((coords[0], coords[5]), (coords[4], coords[1]), (coords[2], coords[5])))
            else:
                self.chooseGunButton = pygame.draw.polygon(windowSurface, self.WHITE, ((coords[0], coords[1]), (coords[4], coords[5]), (coords[2], coords[1])))

    def roundButton(self, event, button, location, flip = False):

        #Setup reload image and rect
        self.reloadImage = pygame.image.load('/home/pi/Taco-Chronicles/files/buttons/reload.png')
        self.rect = self.reloadImage.get_rect()
        self.rect.centerx = location[0]
        self.rect.centery = location[1]
        self.reloadImageBIG = pygame.transform.scale(self.reloadImage, (75, 75))

        #Setup back image and Rect
        self.backImage = pygame.image.load('/home/pi/Taco-Chronicles/files/buttons/back.png')
        self.backRect = self.backImage.get_rect()
        self.backRect.centerx = location[0]
        self.backRect.centery = location[1]
        self.backImageBIG = pygame.transform.scale(self.backImage, (75, 75))

        self.backImageBIGflip = pygame.transform.flip(self.backImageBIG, True, False)
        self.backImageFlip = pygame.transform.flip(self.backImage, True, False)

        #Setup sound on image and Rect
        self.soundOnImage = pygame.image.load('/home/pi/Taco-Chronicles/files/buttons/soundOn.png')
        self.soundRect = self.soundOnImage.get_rect()
        self.soundRect.centerx = location[0]
        self.soundRect.centery = location[1]
        self.soundOnImageBIG = pygame.transform.scale(self.soundOnImage, (75, 75))

        #Setup sound off image
        self.soundOffImage = pygame.image.load('/home/pi/Taco-Chronicles/files/buttons/soundOff.png')
        self.soundOffImageBIG = pygame.transform.scale(self.soundOffImage, (75, 75))

        #Setup pause image and rectangle
        self.pauseImage = pygame.image.load('/home/pi/Taco-Chronicles/files/buttons/pause.png')
        self.pauseRect = self.pauseImage.get_rect()
        self.pauseRect.centerx = location[0]
        self.pauseRect.centery = location[1]
        self.pauseImageBIG = pygame.transform.scale(self.pauseImage, (75, 75))

        #If reload button is selected, make it big or small
        if self.enlarge_reload != True:
            if button == 'reload':
                self.windowSurface.blit(self.reloadImage, self.rect)
        else:
            if button == 'reload':
                self.windowSurface.blit(self.reloadImageBIG, self.rect)

        #If back button is selected, make it big or small
        if self.enlarge_back != True:
            if button == 'back':
                if flip:
                    self.windowSurface.blit(self.backImageFlip, self.backRect)
                else:   
                    self.windowSurface.blit(self.backImage, self.backRect)
        else:
            if button == 'back':
                if flip:
                    self.windowSurface.blit(self.backImageBIGflip, self.backRect)                          
                else:
                    self.windowSurface.blit(self.backImageBIG, self.backRect)

        #If Sound button is selected, make it big or small
        if self.enlarge_sound != True:
            if button == 'sound on':
                self.windowSurface.blit(self.soundOnImage, self.soundRect)
            if button == 'sound off':
                self.windowSurface.blit(self.soundOffImage, self.soundRect)
        else:
            if button == 'sound on':
                self.windowSurface.blit(self.soundOnImageBIG, self.soundRect)
            if button == 'sound off':
                self.windowSurface.blit(self.soundOffImageBIG, self.soundRect)

        #If pause button is selected, make it big or small
        if self.enlarge_pause != True:
            if button == 'pause':
                self.windowSurface.blit(self.pauseImage, self.pauseRect)
        else:
            if button == 'pause':
                self.windowSurface.blit(self.pauseImageBIG, self.pauseRect)
            

        if event != None:
            if event.type == MOUSEMOTION:
                if event.pos[0] > location[0] - 70 and event.pos[0] < location[0] + 70 and event.pos[1] > location[1] - 70 and event.pos[1] < location[1] + 70:
                    if button == 'reload':
                        self.enlarge_reload = True
                    if button == 'back':
                        self.enlarge_back = True
                    if button == 'sound on' or 'sound off':
                        self.enlarge_sound = True
                    if button == 'pause':
                        self.enlarge_pause = True
                else:
                    if button == 'reload':
                        self.enlarge_reload = False
                    if button == 'back':
                        self.enlarge_back = False
                    if button == 'sound on' or 'sound off':
                        self.enlarge_sound = False
                    if button == 'pause':
                        self.enlarge_pause = False
                    
            if event.type == MOUSEBUTTONDOWN:
                if event.pos[0] > location[0] - 70 and event.pos[0] < location[0] + 70 and event.pos[1] > location[1] - 70 and event.pos[1] < location[1] + 70:
                    if button == 'reload':
                        self.reload = True
                        return self.reload
                    if button == 'back':
                        self.back = True
                        return self.back
                    if button == 'sound on' or 'sound off':
                        self.sound = True
                        return self.sound
                    if button == 'pause':
                        self.pause = True
                        return self.pause

    def startButton(self, clicked):
        self.startText = self.comicFont.render('START', True, self.buttonColor[0], self.buttonColor[1])
        self.startRect = self.startText.get_rect()
        self.startRect.centerx = self.windowSurface.get_rect().centerx
        self.startRect.centery = self.windowSurface.get_rect().centery
        self.windowSurface.blit(self.startText, self.startRect)

        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                if self.startRect.collidepoint(event.pos[0], event.pos[1]):
                    self.buttonColor = [self.ORANGE, self.YELLOW]
                else:
                    self.buttonColor = [self.WHITE, self.ORANGE]
            if event.type == MOUSEBUTTONDOWN:
                if self.startRect.collidepoint(event.pos[0], event.pos[1]):
                    clicked = True
                    break
            if event.type == QUIT:
                self.exit = True
        return self.exit, clicked
