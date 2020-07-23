<<<<<<< HEAD
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
=======
""" Atom dosent have a # DEBUG: so im fucking dumb but apparently VSC still has a collobration tool so might use that"""import osimport sys# from pg.locals import * # WTF am i doing here, where the fuck is localsimport pygame as pgimport randomfrom pygame.locals import *""""import numpy # use numpy to model path"""from BeyBlade import BeyBladefrom GeneralSprite import GeneralSpriteos.environ['SDL_VIDEO_CENTERED'] = '1'  # prepriping info gathering# This part is important, creates an array of each bey's images. Cycling through the images makes it spin.# Each image is transformed and made smaller to better fit the arenaplayer1Spin = [pg.transform.scale(pg.image.load(    'Images/Pegasus/Pegasus1.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/Pegasus/Pegasus2.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/Pegasus/Pegasus3.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/Pegasus/Pegasus4.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/Pegasus/Pegasus5.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/Pegasus/Pegasus6.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/Pegasus/Pegasus7.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/Pegasus/Pegasus8.png'), (220, 220)),    pg.transform.scale(pg.image.load('Images/Pegasus/Pegasus9.png'), (220, 220))]player2Spin = [pg.transform.scale(pg.image.load(    'Images/LDrago/LDrago1.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/LDrago/LDrago2.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/LDrago/LDrago3.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/LDrago/LDrago4.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/LDrago/LDrago5.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/LDrago/LDrago6.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/LDrago/LDrago7.png'), (220, 220)),    pg.transform.scale(pg.image.load(        'Images/LDrago/LDrago8.png'), (220, 220)),    pg.transform.scale(pg.image.load('Images/LDrago/LDrago9.png'), (220, 220))]pg.init()  #read this in a british accentBackground = pg.transform.scale(pg.image.load('Images/ArenaBeyBladeVroom.jpg'), (1110, 1110))pg.display.set_caption('BeyBlade Game')screenInfo = pg.display.Info()  # grabbingScreen_Width = screenInfo.current_wScreen_Height = screenInfo.current_h + 70screen = pg.display.set_mode(    (Screen_Width, Screen_Height))  # set size here# player1 obj - Pegasusplayer1 = BeyBlade(player1Spin, 1)player1.rect.x = Screen_Width / 2 - 200player1.rect.y = Screen_Height / 2 + 100# player2 obj - LDragoplayer2 = BeyBlade(player2Spin, 1)player2.rect.x = Screen_Width / 2 + 50player2.rect.y = Screen_Height / 2 - 50boundsPicture = pg.transform.scale(pg.image.load('Images/bounds.png'), (1100, 1100))arena = GeneralSprite(boundsPicture)arena.rect.y = Screen_Height / 2 - 530arena.rect.x = (Screen_Width / 2) - 600pg.display.set_caption('BeyBlade Game')player1Counter = 0player2Counter = 0ClickPostWidth = Screen_Width // 2ClickPostHeight = Screen_Height // 2 - 100# pregame sextionhealthSurface = pg.surface.Surface((Screen_Width, Screen_Height))player1Health = 100player2Health = 100timer = 11while timer != 0:    timer -= 1    pg.time.delay(500)    for event in pg.event.get():        if event.type == KEYDOWN:            if event.key == pg.K_q:                player1Counter += 1            # if event.type == KEYDOWN:            if event.key == pg.K_m:                player2Counter += 1    screen.fill((114, 89, 255))    myfont = pg.font.SysFont('Robotico', 150)    text = str(timer)    textsurface = myfont.render(text, False, (0, 0, 0))    screen.blit(textsurface, (ClickPostWidth, ClickPostHeight))    pg.display.flip()    print("Player 1 Count:{}, Player 2 Count {}".format(        player1Counter, player2Counter))ClickPostWidth -= 250pg.mixer.music.load("Song/letRip.mp3")pg.mixer.music.play(0)pg.display.flip()# image needs to be in the main file struct cant store in seprate folder, see if u can fix# Background objscreen.blit(Background, (360, 0))clock = pg.time.Clock()i = 0# Speeed is the refresh rate of the game, making it smaller makes it seem as if both beys are going faster. Lowest number# is 1 highest number is 80. After 60 it starts to look wonky.speeed = 50# velocity of players in the x direction (will be based off of how much they let it rip)player1x = -1player2x = -15# velocity of players in the y direction (will be based off of how much they let it rip)player1y = 0player2y = 0done = Falsesprites = pg.sprite.Group()players = pg.sprite.Group()players.add(player2)sprites.add(arena)done = True#the variation whenever the beys bump off the arena, so they wont go the opposite directionWallCollisionVar = 5#the variation whenever the beys collide off of each otherBeyCollisionVar = 5while done:    #refresh rate of the player images    i += 3    i = i % 9    #so the beys don't fly themselves off the map after gaining a shit ton of speed    if(player1x > 50):        player1x = player1x - WallCollisionVar    if(player2x > 50):        player2x = player2x - WallCollisionVar    if(player1y > 50):        player1y = player1y - WallCollisionVar    if(player2y > 50):        player2y = player2y - WallCollisionVar    if pg.sprite.spritecollide(player1, sprites, False, pg.sprite.collide_mask):        player1x = player1x * -1        if(player1x > 0):            player1x = player1x + random.randint(0, WallCollisionVar)        if(player1x < 0):            player1x = player1x + random.randint(-WallCollisionVar, 0)        player1y = player1y * -1        if(player1y > 0):            player1y = player1y + random.randint(0, WallCollisionVar)        if(player1y < 0):            player1y = player1y + random.randint(-WallCollisionVar, 0)    if pg.sprite.spritecollide(player2, sprites, False, pg.sprite.collide_mask):        player2x = player2x * -1        if(player2x > 0):            player2x = player2x + random.randint(0, WallCollisionVar)        if(player2x < 0):            player2x = player2x + random.randint(-WallCollisionVar, 0)        player2y = player2y * -1        if(player2y > 0):            player2y = player2y + random.randint(0, WallCollisionVar)        if(player2y < 0):            player2y = player2y + random.randint(-WallCollisionVar, 0)    elif pg.sprite.spritecollide(player1, players, False, pg.sprite.collide_mask):        if (player1x * player2x) < 0:            if(player1x < 0):                player1x = -player1x + random.randint(0, BeyCollisionVar)                player2x = -player2x + random.randint(-BeyCollisionVar, 0)            else:                player1x = -player1x + random.randint(-BeyCollisionVar, 0)                player2x = -player2x + random.randint(0, BeyCollisionVar)        else:            if(player1x < 0):                player1x = -player1x + random.randint(0, BeyCollisionVar)                player2x = player2x + random.randint(-BeyCollisionVar, 0)            else:                player1x = -player1x + random.randint(-BeyCollisionVar, 0)                player2x = player2x + random.randint(0, BeyCollisionVar)        if (player1y * player2y) < 0:            if(player1y < 0):                player1y = -player1y + random.randint(0, BeyCollisionVar)                player2y = -player2y + random.randint(-BeyCollisionVar, 0)            else:                player1y = -player1y + random.randint(-BeyCollisionVar, 0)                player2y = -player2y + random.randint(0, BeyCollisionVar)        else:            if(player1y < 0):                player1y = -player1y + random.randint(0, BeyCollisionVar)                player2y = player2y + random.randint(-BeyCollisionVar, 0)            else:                player1y = -player1y + random.randint(-BeyCollisionVar, 0)                player2y = player2y + random.randint(0, BeyCollisionVar)    player1.update(player1x, player1y)    player2.update(player2x, player2y)    screen.blit(Background, (360, 0))    player2.draw(screen)    player1.draw(screen)    pg.display.flip()    pg.time.delay(speeed)    for event in pg.event.get():        if event.type == KEYDOWN:            if event.key == K_ESCAPE:                pg.quit()                sys.exit()    # ---------------------------------------------HEALTH BARS-------------------------------------------------------------------    pg.draw.rect(healthSurface, [255, 255, 255], (50, 100, 0, 0))    # ---------------------------------------------HEALTH BARS-------------------------------------------------------------------    # screen.blit(healthSurface)    pg.display.flip()    pg.time.delay(speeed)# for movement we cant use random values but we can [A,B,C,D] and change the rates at which each grow and decrease to# make random movement
>>>>>>> b5b29579303bc0a070badab3e0564fc6fca00ed9
