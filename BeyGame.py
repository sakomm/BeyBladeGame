import sys
import os 
import pygame 
from pygame.locals import *
import math


os.environ['SDL_VIDEO_CENTERED'] = '1' #prepriping info gathering  
mainClock = pygame.time.Clock()

pygame.init()

screenInfo  = pygame.display.Info() # grabbing 
Screen_Width = screenInfo.current_w
Screen_Height = screenInfo.current_h
screen = pygame.display.set_mode((Screen_Width, Screen_Height)) # set size here


def MainMenu():
    print(Screen_Width,Screen_Height)
    while True:    
        Background = pygame.image.load('BackGroundMain.png')
        Background = pygame.transform.scale(Background,(1920,1080))
        
        
        screen.blit(Background,(0,0))
        
        MouseX, MouseY = pygame.mouse.get_pos()

        button_1 = pygame.Rect(500, 700, 200, 100)
        
        
        

        if button_1.collidepoint((MouseX, MouseY)):
            if click:
                MainGame()

        pygame.draw.rect(screen, (0,0,235), button_1, 1)
        
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

def Tangent(x, y):
    LimDeriv = 0

def MainGame():
    sys.exit()

MainMenu()

