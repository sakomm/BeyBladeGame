import sys
import os
import pygame
from pygame.locals import *
import time
import TestField

os.environ['SDL_VIDEO_CENTERED'] = '1'  # prepriping info gathering
mainClock = pygame.time.Clock()

pygame.init()
pygame.font.init()


screenInfo = pygame.display.Info()  # grabbing
Screen_Width = screenInfo.current_w
Screen_Height = screenInfo.current_h
screen = pygame.display.set_mode(
    (Screen_Width, Screen_Height))  # set size here


def MainMenu():
    # print(Screen_Width,Screen_Height)
    # Song Loop ----------------------------------------------------------
    time.sleep(1)
    pygame.mixer.music.load("Song/BMF_Song.mp3")
    pygame.mixer.music.play(-1)
    #---------------------------------------------------------------------
    while True:     # add a second button that adds instructions
        #click = False
        Background = pygame.image.load('Images/BackgroundMain.jpg')
        Background = pygame.transform.scale(Background, (1920, 1080))

        screen.blit(Background, (0, 0))

        MouseX, MouseY = pygame.mouse.get_pos()

        button_1 = pygame.Rect(400, 800, 200, 100)
        button_2 = pygame.Rect(1300, 800, 200, 100)

        if button_1.collidepoint((MouseX, MouseY)):
            if click:
                pygame.mixer.music.stop()

                MainGame()

        if button_2.collidepoint((MouseX, MouseY)):
            if click:
                pygame.mixer.music.stop()

                Instuctions()

        pygame.draw.rect(screen, (0, 0, 0), button_1, 5)
        pygame.draw.rect(screen, (0, 0, 0), button_2, 5)

        # add a custom font, normal font looks like garbage
        
        #Font For Button 1 
        myfont = pygame.font.SysFont('Robotico', 50)

        textsurface = myfont.render('Start Game', False, (0, 0, 0))
        screen.blit(textsurface, (410, 830))

        #--------------------------------------------------------------------
        #font for button 2 
        myfont = pygame.font.SysFont('Robotico', 40)

        textsurface = myfont.render('Instructions', False, (0, 0, 0))
        screen.blit(textsurface, (1310, 830))

        #---------------------------------------------------------------------


        click = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def Instuctions(): # Make instuctions when everything is done 
    sys.exit()


def MainGame():
    print("test passed")
    TestField


MainMenu()
