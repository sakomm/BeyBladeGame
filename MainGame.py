""" Atom dosent have a # DEBUG: so im fucking dumb but apparently VSC still has a collobration
 tool so might use that
"""
from BeyBlade import BeyBlade
from GeneralSprite import GeneralSprite
import sys
import os

# from pg.locals import * # WTF am i doing here, where the fuck is locals
import random

import pygame as pg
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # prepriping info gathering

# This part is important, creates an array of each bey's images. Cycling through the images makes it spin.
# Each image is transformed and made smaller to better fit the arena

player1Spin = [ pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus1.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus2.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus3.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus4.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus5.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus6.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus7.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus8.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus9.png'), (260, 260))]


player2Spin = [ pg.transform.scale(pg.image.load('Images/LDrago/LDrago1.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/LDrago/LDrago2.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/LDrago/LDrago3.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/LDrago/LDrago4.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/LDrago/LDrago5.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/LDrago/LDrago6.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/LDrago/LDrago7.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/LDrago/LDrago8.png'), (260, 260)),
                pg.transform.scale(pg.image.load('Images/LDrago/LDrago9.png'), (260, 260))]
pg.init()  # read this in a british accent

Background = pg.transform.scale(pg.image.load(
    'Images/ArenaBeyBladeVroom.jpg'), (1110, 1110))

pg.display.set_caption('BeyBlade Game')

screenInfo = pg.display.Info()  # grabbing
Screen_Width = screenInfo.current_w
Screen_Height = screenInfo.current_h 
screen = pg.display.set_mode(
    (Screen_Width, Screen_Height))  # set size here


# player1 obj - Pegasus
player1 = BeyBlade(player1Spin, 1)
player1.rect.x = Screen_Width / 2 - 200
player1.rect.y = Screen_Height / 2 + 100
# player2 obj - LDrago
player2 = BeyBlade(player2Spin, 1)
player2.rect.x = Screen_Width / 2 + 50
player2.rect.y = Screen_Height / 2 - 50


boundsPicture = pg.transform.scale(pg.image.load('Images/bounds.png'), (1100, 1100))
arena = GeneralSprite(boundsPicture)
arena.rect.y = Screen_Height / 2 - 530
arena.rect.x = (Screen_Width / 2) - 600

pg.display.set_caption('BeyBlade Game')

player1Counter = 0
player2Counter = 0

ClickPostWidth = Screen_Width // 2
ClickPostHeight = Screen_Height // 2 - 100
# pregame sextion

healthSurface = pg.Surface((Screen_Width, Screen_Height))

MiniGameSurface = pg.Surface((100,100))
# init the player health

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
screen.blit(healthSurface, (0, 0))
screen.blit(MiniGameSurface, (Screen_Width//2,Screen_Height//2))



i = 0
# Speeed is the refresh rate of the game, making it smaller makes it seem as if both beys are going faster. Lowest number
# is 1 highest number is 80. After 60 it starts to look wonky.
speeed = 50

# velocity of players in the x direction (will be based off of how much they let it rip)
player1x = -10
player2x = -player2Counter * 2
# velocity of players in the y direction (will be based off of how much they let it rip)
player1y = random.randint(-10, 10)
player2y = random.randint(-10, 10)
done = False
sprites = pg.sprite.Group()
players = pg.sprite.Group()
players.add(player2)
sprites.add(arena)

def Walls(player1xT,player1yT):
    if(player1.rect.x < 300):
        print(player1xT)
        player1x = player1xT + 3

done = True
# the variation whenever the beys bump off the arena, so they wont go the opposite direction
WallCollisionVar = 15
# the variation whenever the beys collide off of each other
BeyCollisionVar = 20
healthMinimizerInator = 500
healthMinimizerInator2 = 500

while done:

    # ---------------------------------------------HEALTH BARS-------------------------------------------------------------------
    #pg.draw.rect(healthSurface, [255, 0, 0], (50, 100, 50, 50))
    
    redBar = pg.Rect((50,50), (50, 500))
    greenBar = pg.Rect((50,50), (50, healthMinimizerInator))

    pg.display.update(pg.draw.rect(healthSurface, (250, 0, 0), redBar))
    pg.display.update(pg.draw.rect(healthSurface, (0, 250, 0), greenBar))
    
    #healthMinimizerInator = healthMinimizerInator - 
    redBar2 = pg.Rect((1335,50),(50,500))
    greenBar2 = pg.Rect((1335,50), (50, healthMinimizerInator2))

    pg.display.update(pg.draw.rect(healthSurface, (250, 0, 0), redBar2))
    pg.display.update(pg.draw.rect(healthSurface, (0, 250, 0), greenBar2))
    
    if pg.sprite.spritecollide(player1, players, False, pg.sprite.collide_mask):
        healthMinimizerInator = healthMinimizerInator - 20
        healthMinimizerInator2 = healthMinimizerInator2 - 20
        

    screen.blit(healthSurface,(200,100))
    
  
    # ---------------------------------------------HEALTH BARS-------------------------------------------------------------------

    # refresh rate of the player images
    i += 3
    i = i % 9

    # so the beys don't fly themselves off the map after gaining a shit ton of speed
    if(player1x > 50):
        player1x = player1x - 20
    if(player2x > 50):
        player2x = player2x - 20
    if(player1y > 50):
        player1y = player1y - 20
    if(player2y > 50):
        player2y = player2y - 20
    print(player1x)
    Walls(player1x,player1y)


    print(player1x)

    if pg.sprite.spritecollide(player2, sprites, False, pg.sprite.collide_mask):
        player2x = player2x * -1
        if(player2x > 0):
            player2x = player2x + random.randint(0, WallCollisionVar)
        if(player2x < 0):
            player2x = player2x + random.randint(-WallCollisionVar, 0)
        player2y = player2y * -1
        if(player2y > 0):
            player2y = player2y + random.randint(0, WallCollisionVar)
        if(player2y < 0):
            player2y = player2y + random.randint(-WallCollisionVar, 0)
    elif pg.sprite.spritecollide(player1, players, False, pg.sprite.collide_mask):
        if (player1x * player2x) < 0:
            if(player1x < 0):
                player1x = -player1x + random.randint(0, BeyCollisionVar)
                player2x = -player2x + random.randint(-BeyCollisionVar, 0)
            else:
                player1x = -player1x + random.randint(-BeyCollisionVar, 0)
                player2x = -player2x + random.randint(0, BeyCollisionVar)
        else:
            if(player1x < 0):
                player1x = -player1x + random.randint(0, BeyCollisionVar)
                player2x = player2x + random.randint(-BeyCollisionVar, 0)
            else:
                player1x = -player1x + random.randint(-BeyCollisionVar, 0)
                player2x = player2x + random.randint(0, BeyCollisionVar)
        if (player1y * player2y) < 0:
            if(player1y < 0):
                player1y = -player1y + random.randint(0, BeyCollisionVar)
                player2y = -player2y + random.randint(-BeyCollisionVar, 0)
            else:
                player1y = -player1y + random.randint(-BeyCollisionVar, 0)
                player2y = -player2y + random.randint(0, BeyCollisionVar)
        else:
            if(player1y < 0):
                player1y = -player1y + random.randint(0, BeyCollisionVar)
                player2y = player2y + random.randint(-BeyCollisionVar, 0)
            else:
                player1y = -player1y + random.randint(-BeyCollisionVar, 0)
                player2y = player2y + random.randint(0, BeyCollisionVar)

    player1.update(player1x, player1y)
    player2.update(player2x, player2y)
    
    screen.blit(Background, (360, 0))
    
    player2.draw(screen)
    player1.draw(screen)
    
    screen.blit(boundsPicture, (arena.rect.x, arena.rect.y))
    
    pg.display.flip()
    
    pg.time.delay(speeed)

    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
                sys.exit()
            
            if event.key == pg.K_q:
                player1Counter += 1

            # if event.type == KEYDOWN:
            if event.key == pg.K_m:
                player2Counter += 1

    # screen.blit(healthSurface)
    pg.display.flip()
    pg.display.update()
    pg.time.delay(speeed)


    
# for movement we cant use random values but we can [A,B,C,D] and change the rates at which each grow and decrease to
# make random movement
