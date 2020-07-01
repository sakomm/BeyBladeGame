""" Atom dosent have a # DEBUG: so im fucking dumb but apparently VSC still has a collobration
 tool so might use that
"""
import os
import sys



# from pygame.locals import * # WTF am i doing here, where the fuck is locals
import pygame as pg
from pygame.locals import *
""""
import numpy # use numpy to model path

"""
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

pg.init()  # isnt inatilizing secondary modules GARBAGE SHIT FACE CODE

screenInfo = pg.display.Info()  # grabbing
Screen_Width = screenInfo.current_w
Screen_Height = screenInfo.current_h
screen = pg.display.set_mode(
    (Screen_Width, Screen_Height))  # set size here

pg.display.set_caption('BeyBlade Game')

player1Counter = 0
player2Counter = 0

ClickPostWidth = Screen_Width // 2 
ClickPostHeight = Screen_Height // 2  - 100
# pregame sextion

healthSurface = pg.surface.Surface((Screen_Width, Screen_Height))

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
    
    print("Player 1 Count:{}, Player 2 Count {}".format(
        player1Counter, player2Counter))

ClickPostWidth -= 250
pg.mixer.music.load("Song/letRip.mp3")
pg.mixer.music.play(0)
screen.blit(textsurface, (ClickPostWidth, ClickPostHeight))

pg.display.flip()





# image needs to be in the main file struct cant store in seprate folder, see if u can fix
# Background obj
Background = pg.image.load('Images/ArenaBeyBladeVroom.jpg')

screen.blit(Background, (360, 0))

# load method can have a specfied path - take that stack overflow u dumb bitch

# player obj - Pegasus
player = player1Spin[0]
player1Health = 100
player = pg.transform.scale(player, (360, 300))
position = player.get_rect()
screen.blit(player, (250, 250))

screen.blit(Background, position, position)
# pygame.display.update()
# https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate

# player2 obj - El Drago
player2 = player2Spin[0]
player2 = pg.transform.scale(player2, (250, 250))
# i think i spelled Pegasus wrong
# nah you didn't

player2Health = 100
screen.blit(player2, (650, 650))
pg.display.update()
clock = pg.time.Clock()
i = 0
# Speeed is the refresh rate of the game, making it smaller makes it seem as if both beys are going faster. Lowest number
# is 1 highest number is 80. After 60 it starts to look wonky.
speeed = 60
# x is just something I was testing, it's not needed
x = 2

done = True
screen.fill((114, 89, 255))

while done:

    # screen.blit(player,(500,500)) #blit is temporary and crashes , How to fix?
    # format error screen.blit(object (x,y))
    # update probaby needs to happen hear in loop

    pg.draw.rect(screen, [255, 255, 255], (100, 50, 100, 100))

    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(500, 500, 100, 100))
    screen.blit(Background, (360, 0))
    player = player1Spin[i]
    screen.blit(player, (650 - x, 250))
    player2 = player2Spin[i]
    # Again, please ignore x.
    x += 0
    # changing i also changes how the beyblades look like when spinning. i = 1 means normal i = 4 means slightly faster
    # looking spinning. not that useful but thought u should know
    i += 4
    i = i % 9
    screen.blit(player2, (550, 500))


    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
                sys.exit()
    #---------------------------------------------HEALTH BARS-------------------------------------------------------------------
    pg.draw.rect(healthSurface,[255,255,255], (50,100,0,0))

    #---------------------------------------------HEALTH BARS-------------------------------------------------------------------
    
    #screen.blit(healthSurface)
    pg.display.flip()
    pg.time.delay(speeed)

# for movement we cant use random values but we can [A,B,C,D] and change the rates at which each grow and decrease to
# make random movement
