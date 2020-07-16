""" Atom dosent have a # DEBUG: so im fucking dumb but apparently VSC still has a collobration
 tool so might use that
"""
import os
import sys

# from pg.locals import * # WTF am i doing here, where the fuck is locals
import pygame as pg
import random
from pygame.locals import *

""""
import numpy # use numpy to model path

"""
from BeyBlade import BeyBlade
from GeneralSprite import GeneralSprite

os.environ['SDL_VIDEO_CENTERED'] = '1'  # prepriping info gathering

# This part is important, creates an array of each bey's images. Cycling through the images makes it spin.
# Each image is transformed and made smaller to better fit the arena
player1Spin = [pg.transform.scale(pg.image.load(
    'Images/Pegasus/Pegasus1.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/Pegasus/Pegasus2.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/Pegasus/Pegasus3.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/Pegasus/Pegasus4.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/Pegasus/Pegasus5.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/Pegasus/Pegasus6.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/Pegasus/Pegasus7.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/Pegasus/Pegasus8.png'), (220, 220)),
    pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus9.png'), (220, 220))]

player2Spin = [pg.transform.scale(pg.image.load(
    'Images/LDrago/LDrago1.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/LDrago/LDrago2.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/LDrago/LDrago3.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/LDrago/LDrago4.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/LDrago/LDrago5.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/LDrago/LDrago6.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/LDrago/LDrago7.png'), (220, 220)),
    pg.transform.scale(pg.image.load(
        'Images/LDrago/LDrago8.png'), (220, 220)),
    pg.transform.scale(pg.image.load('Images/LDrago/LDrago9.png'), (220, 220))]

pg.init()  # initializes stuff, you need to put most of the important code after this.

Background = pg.transform.scale(pg.image.load('Images/ArenaBeyBladeVroom.jpg'), (1110, 1110))

pg.display.set_caption('BeyBlade Game')

# image needs to be in the main file struct cant store in seprate folder, see if u can fix
# Background obj

# load method can have a specfied path - take that stack overflow u dumb bitch
# nvm they were right it cant be path specfic

screenInfo = pg.display.Info()  # grabbing
Screen_Width = screenInfo.current_w
Screen_Height = screenInfo.current_h
screen = pg.display.set_mode(
    (Screen_Width, Screen_Height))  # set size here

# player obj - Pegasus
player1 = BeyBlade(player1Spin, 1)
position = player1.rect
player2 = BeyBlade(player2Spin, 1)
player2.rect.x = Screen_Width / 2 - 100
player2.rect.y = Screen_Height / 2 - 100
player1.rect.x = Screen_Width / 2 + 100
player1.rect.y = Screen_Height / 2 + 100

boundsPicture = pg.transform.scale(pg.image.load('Images/bounds.png'), (650, 650))
arena = GeneralSprite(boundsPicture)
arena.rect.y = Screen_Height / 2 - 250
arena.rect.x = (Screen_Width / 2) - 325

pg.display.set_caption('BeyBlade Game')

player1Counter = 0
player2Counter = 0

ClickPostWidth = Screen_Width // 2
ClickPostHeight = Screen_Height // 2 - 100
# pregame sextion

healthSurface = pg.surface.Surface((Screen_Width, Screen_Height))
player1Health = 100
player2Health = 100

timer = 11
while timer != 0:
    timer -= 1
    pg.time.delay(500)
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == pg.K_q:
                player1Counter += 1

            # if event.type == KEYDOWN:
            if event.key == pg.K_m:
                player2Counter += 1

    screen.fill((114, 89, 255))
    myfont = pg.font.SysFont('Robotico', 150)

    text = str(timer)
    textsurface = myfont.render(text, False, (0, 0, 0))
    screen.blit(textsurface, (ClickPostWidth, ClickPostHeight))

    pg.display.flip()

    print("Player 1 Count:{}, Player 2 Count {}".format(
        player1Counter, player2Counter))

ClickPostWidth -= 250
pg.mixer.music.load("Song/letRip.mp3")
pg.mixer.music.play(0)

pg.display.flip()

# image needs to be in the main file struct cant store in seprate folder, see if u can fix
# Background obj

screen.blit(Background, (360, 0))

clock = pg.time.Clock()
i = 0
# Speeed is the refresh rate of the game, making it smaller makes it seem as if both beys are going faster. Lowest number
# is 1 highest number is 80. After 60 it starts to look wonky.
speeed = 50

# velocity of players in the x direction
player1x = 15
player2x = 10
# velocity of players in the y direction
player1y = 0
player2y = 0
done = False
sprites = pg.sprite.Group()
players = pg.sprite.Group()
players.add(player2)
sprites.add(arena)

done = True

while done:

    # screen.blit(player,(500,500)) #blit is temporary and crashes , How to fix?
    # format error screen.blit(object (x,y))
    # update probaby needs to happen hear in loop
    i += 4
    i = i % 9
    if not pg.sprite.spritecollide(player1, sprites, False, pg.sprite.collide_mask):
        player1x = player1x * -1 + random.random() * 10
        player1y = player1y * -1 + random.random() * 10

    if not pg.sprite.spritecollide(player2, sprites, False, pg.sprite.collide_mask):
        player2x = player2x * -1 + random.random() * 5
        player2y = player2y * -1 + random.random() * 5

    elif pg.sprite.spritecollide(player1, players, False, pg.sprite.collide_mask):
        if (player1x * player2x) < 0:
            if (player1y * player2y) < 0:
                player1y = player1y * -1 + random.random() * 10
                player2y = player2y * -1 + random.random() * 10
            else:
                player1y = player1y * -1 + random.random() * 10
                player2y = player2y + random.random() * 10
            player1x = player1x * -1 + random.random() * 10
            player2x = player2x * -1 + random.random() * 10
        else:
            player1x = player1x * -1 + random.random() * 10
            player2x = player2x + random.random() * 10

    player1.update(player1x, player1y)
    player2.update(player2x, player2y)
    screen.blit(Background, (360, 0))
    player2.draw(screen)
    player1.draw(screen)
    pg.display.flip()
    pg.time.delay(speeed)

    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
                sys.exit()
    # ---------------------------------------------HEALTH BARS-------------------------------------------------------------------
    pg.draw.rect(healthSurface, [255, 255, 255], (50, 100, 0, 0))

    # ---------------------------------------------HEALTH BARS-------------------------------------------------------------------

    # screen.blit(healthSurface)
    pg.display.flip()
    pg.time.delay(speeed)

# for movement we cant use random values but we can [A,B,C,D] and change the rates at which each grow and decrease to
# make random movement
