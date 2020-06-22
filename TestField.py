""" Atom dosent have a # DEBUG: so im fucking dumb but apparently VSC still has a collobration
 tool so might use that
"""
import pygame
from pygame.locals import *
#WTF am i doing here, where the fuck is locals
from BeyBlade import BeyBlade
from GeneralSprite import GeneralSprite
""""
import numpy # use numpy to model path

"""

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

pygame.init()  # isnt inatilizing secondary modules GARBAGE SHIT FACE CODE

screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption('BeyBlade Game')

# image needs to be in the main file struct cant store in seprate folder, see if u can fix
# Background obj
Background = pygame.image.load('ArenaBeyBladeVroom.jpg').convert()
screen.blit(Background, (0, 0))



# load method can have a specfied path - take that stack overflow u dumb bitch
# nvm they were right it cant be path specfic
arena = GeneralSprite(pygame.image.load('arenaBounds.png').convert())


# player obj - Pegasus
player = BeyBlade(player1Spin, 1)
position = player.rect
colisionimage = BeyBlade(player2Spin,1)
colisionimage.rect.x = 500
colisionimage.rect.y = 200
player.rect.y = 0
pygame.display.update()
# https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate

# player2 obj - El Drago
player2 = player2Spin[0]

screen.blit(player2, (650, 650))
pygame.display.update()
clock = pygame.time.Clock()

#pygame.sprite.collide_circle(player, player2)
i = 0
# Speeed is the refresh rate of the game, making it smaller makes it seem as if both beys are going faster. Lowest number
# is 1 highest number is 80. After 60 it starts to look wonky.
speeed = 100
# x is just something I was testing, it's not needed
x = 2
playerx = 15
done = False
sprites = pygame.sprite.Group()
sprites.add(colisionimage)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # screen.blit(player,(500,500)) #blit is temporary and crashes , How to fix?
    # format error screen.blit(object (x,y))
    # update probaby needs to happen hear in loop
    print(position)
    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(500, 500, 100, 100))
    screen.blit(Background, (0, 0))
    player2 = player2Spin[i]
    # Again, please ignore x.
    x += 25
    # changing i also changes how the beyblades look like when spinning. i = 1 means normal i = 4 means slightly faster
    # looking spinning. not that useful but thought u should know
    i += 1
    i = i % 9
    screen.blit(player2, (550, 500))
    if pygame.sprite.spritecollide(player, sprites, False, pygame.sprite.collide_mask):
        pygame.draw.polygon(screen, (200, 150, 150), colisionimage.olist, 0)
        playerx = playerx * -1

    player.update(playerx)
    colisionimage.update(0)
    colisionimage.draw(screen,200)
    player.draw(screen,150)

    pygame.display.flip()
    pygame.time.delay(speeed)
# for movement we cant use random values but we can [A,B,C,D] and change the rates at which each grow and decrease to
# make random movement
