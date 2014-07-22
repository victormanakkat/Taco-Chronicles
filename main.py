# main.py
# By Tyler Spadgenske
VERSION = '1.0.19'

def main():
    #Really important values
    showFPS = True
    TOTAL_OBJECTS = 1

    #Import modules
    import pygame, sys, os
    from pygame.locals import *

    #import custom classes
    import background, button, toolbar, selectGun, selectTool, person, powerups, baddieAI
    from background import Level_1
    from button import Button
    from toolbar import Toolbar
    from selectGun import selectGunMenu
    from selectTool import selectToolMenu
    from person import Person
    from powerups import Powerups
    from baddieAI import AI
    from l1 import L1
    import load
    from screen import Screen
    from file import File

    #Setup game data
    getFiles = File()
    highscore, totalscore, firstRun, lockedGuns = getFiles.read()

    #Show Important information if program is run for first time
    if firstRun:
        from installer import Install
        firstRun = False
    #Setup the main screen display and clock
    pygame.init()

    os.environ ['SDL_VIDEO_WINDOW_POS'] = 'center'
    WINDOWWIDTH = 1200
    WINDOWHIEGHT = 600
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHIEGHT), 0, 32)
    icon = pygame.image.load('files\\icon.png')
    pygame.display.set_caption('The Taco Chronicles')
    pygame.display.set_icon(icon)
    mainClock = pygame.time.Clock()
    load.Credits(windowSurface)
    #Setup Colors
    BLUE = (0,0,255)
    SKY_BLUE = (0, 255, 255)

    windowSurface.fill(SKY_BLUE)

    lockedTools = {'crowbar':False, 'rope':True, 'key':True, 'TNT':True, 'jetpack':True}
    sound = True
    gameData = {'sound':sound, 'lockedGuns':lockedGuns, 'lockedTools':lockedTools}
    restart = True

    start = Screen(windowSurface)
    clicked = False
    windowSurface.fill((255, 255, 255))
    pygame.mixer.music.load('files//sound//gameTheme.mp3')
    exit = False

    while True:        
        restart = True
        clicked = False
        pygame.mixer.music.play(-1, 0.0)
        windowSurface.fill((255, 255, 255))
        while True:
            if exit:
                getFiles.write(highscore, totalscore, firstRun, lockedGuns)
                pygame.quit()
                sys.exit()
            clicked, exit = start.startScreen(highscore, clicked)
            if clicked:
                break
        
        pygame.mixer.music.stop()

        load.Load(windowSurface)
    
        #Run the gameplay
        count = 0
        while True:
            level = L1(windowSurface, mainClock, SKY_BLUE, gameData, showFPS)
            restart, goBack, highscore, totalscore, exit = level.play(highscore, totalscore)
            if goBack:
                break
            if exit:
                break

        if totalscore > 10000:
            lockedGuns['shotgun'] = False
        if totalscore > 15000:
            lockedGuns['AK-47'] = False
        if totalscore > 30000:
            lockedGuns['bazooka'] = False
        if totalscore > 35000:
            lockedGuns['flamethrower'] = False

if __name__ == '__main__':
    main()

    


