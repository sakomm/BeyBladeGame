import pygame
import sys
import os
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)
 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        
        if button_1.collidepoint((mx, my)):
            if click:
                game()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    screen = pygame.display.set_mode((1200, 1200))
    pygame.display.set_caption('BeyBlade Game')

    # image needs to be in the main file struct cant store in seprate folder, see if u can fix
    #Background obj
    Background = pygame.image.load('ArenaBeyBladeVroom.jpg').convert()
    screen.blit(Background,(0,0))

        #load method can have a specfied path - take that stack overflow u dumb bitch
        #nvm they were right it cant be path specfic

    #player obj - Pegasus
    player = pygame.image.load('PegasusIsLame.jpg') # i think i spelled Pegasus wrong
    position = player.get_rect() #make Pegasus smaller its a bit big
    screen.blit(player, (100,100))
    pygame.display.update()
    #https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate

    # player2 obj - El Drago
    player2 = pygame.image.load('ELDrago.png') # i think i spelled Pegasus wrong
    screen.blit(player2, (650,650))
    pygame.display.update()

    done = False

    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
            #screen.blit(player,(500,500)) #blit is temporary and crashes , How to fix?
                                        # format error screen.blit(object (x,y))
                # update probaby needs to happen hear in loop

            #pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(500, 500, 100, 100))

        player = pygame.transform.rotate(player,90)
        screen.blit(player, (100,100))


        player2 = pygame.transform.rotate(player2,-90)
        screen.blit(player2, (650,650))

        pygame.display.flip()

 

 
main_menu()