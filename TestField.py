import os
import sys

import pygame
from pygame.locals import *

import random
#WTF am i doing here, where the fuck is locals
from BeyBlade import BeyBlade
from GeneralSprite import GeneralSprite

""""
import numpy # use numpy to model path

""" 

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()
    
screenInfo = pygame.display.Info()  # grabbing
Screen_Width = screenInfo.current_w
Screen_Height = screenInfo.current_h
screen = pygame.display.set_mode(
    (Screen_Width, Screen_Height))  # set size here
 
# This part is important, creates an array of each bey's images. Cycling through the images makes it spin.
# Each image is transformed and made smaller to better fit the arena
player1Spin = [pygame.transform.scale(pygame.image.load('Pegasus/Pegasus1.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Pegasus/Pegasus2.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Pegasus/Pegasus3.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Pegasus/Pegasus4.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Pegasus/Pegasus5.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Pegasus/Pegasus6.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Pegasus/Pegasus7.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Pegasus/Pegasus8.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Pegasus/Pegasus9.png'), (220, 220))]

player2Spin = [pygame.transform.scale(pygame.image.load('LDrago/LDrago1.png'), (200, 200)),
               pygame.transform.scale(pygame.image.load('LDrago/LDrago2.png'), (200, 200)),
               pygame.transform.scale(pygame.image.load('LDrago/LDrago3.png'), (200, 200)),
               pygame.transform.scale(pygame.image.load('LDrago/LDrago4.png'), (200, 200)),
               pygame.transform.scale(pygame.image.load('LDrago/LDrago5.png'), (200, 200)),
               pygame.transform.scale(pygame.image.load('LDrago/LDrago6.png'), (200, 200)),
               pygame.transform.scale(pygame.image.load('LDrago/LDrago7.png'), (200, 200)),
               pygame.transform.scale(pygame.image.load('LDrago/LDrago8.png'), (200, 200)),
               pygame.transform.scale(pygame.image.load('LDrago/LDrago9.png'), (200, 200))]





Background = pygame.transform.scale(pygame.image.load('Images/ArenaBeyBladeVroom.jpg').convert(), (Screen_Height,Screen_Height))

boundsPicture = pygame.transform.scale(pygame.image.load('bounds.png'), (750, 750))

pygame.display.set_caption('BeyBlade Game')

# image needs to be in the main file struct cant store in seprate folder, see if u can fix
# Background obj

# load method can have a specfied path - take that stack overflow u dumb bitch
# nvm they were right it cant be path specfic

arena = GeneralSprite(boundsPicture)
arena.rect.y = 220
arena.rect.x = 220

# player obj - Pegasus
player1 = BeyBlade(player1Spin, 1)
position = player1.rect
player2 = BeyBlade(player2Spin,1)
player2.rect.x = 500
player2.rect.y = 200
player1.rect.x = 200
player1.rect.y = 200
pygame.display.update()
# https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate

# player2 obj - El Drago

pygame.display.update()
clock = pygame.time.Clock()

#pygame.sprite.collide_circle(player, player2)
i = 0
# Speeed is the refresh rate of the game, making it smaller makes it seem as if both beys are going faster. Lowest number
# is 1 highest number is 80. After 60 it starts to look wonky.
speeed = 50
#velocity of players in the x direction
player1x = 15
player2x = 10
#velocity of players in the y direction
player1y = 0
player2y = 0
done = False
sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
players.add(player2)
sprites.add(arena)

timer = 11
while timer != 0:
    timer -= 1
    pg.time.delay(500)
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == pg.K_q:
                player1Counter += 1

        #if event.type == KEYDOWN:
            if event.key == pg.K_m:
                player2Counter += 1

    screen.fill((114, 89, 255))
    myfont = pg.font.SysFont('Robotico', 150)
    

    text = str(timer)
    textsurface = myfont.render(text, False, (0, 0, 0))
    screen.blit(textsurface, (ClickPostWidth, ClickPostHeight))

    pg.display.flip()


while not done:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
            
                done = True
    # screen.blit(player,(500,500)) #blit is temporary and crashes , How to fix?
    # format error screen.blit(object (x,y))
    # update probaby needs to happen hear in loop
<<<<<<< HEAD
    print(position) 
=======
>>>>>>> b5b29579303bc0a070badab3e0564fc6fca00ed9
    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(500, 500, 100, 100))
    screen.blit(Background, (Screen_Width//2 - 550, 0))
    # Again, please ignore x.
    # changing i also changes how the beyblades look like when spinning. i = 1 means normal i = 4 means slightly faster
    # looking spinning. not that useful but thought u should know
    i += 1
    i = i % 9
    if not pygame.sprite.spritecollide(player1, sprites, False, pygame.sprite.collide_mask):
        player1x = player1x * -1 + random.random() * 10
        player1y = player1y * -1 + random.random() * 10
        player2x = player2x * -1
        player2y = player2y * -1


    elif pygame.sprite.spritecollide(player1, players, False, pygame.sprite.collide_mask):
        player1x = player1x * -1 + random.random() * 10
        player1y = player1y * -1 + random.random() * 10
        player2x = player2x * -1
        player2y = player2y * -1

    player1.update(player1x, player1y)
    player2.update(player2x, player2y)
    player2.draw(screen)
    player1.draw(screen)
    arena.update()
    pygame.display.flip()
    pygame.time.delay(speeed)
# for movement we cant use random values but we can [A,B,C,D] and change the rates at which each grow and decrease to
# make random movement
