""" Atom dosent have a # DEBUG: so im fucking dumb but apparently VSC still has a collobration
 tool so might use that
"""
import pygame  # from pygame.locals import * # WTF am i doing here, where the fuck is locals

""""
import numpy # use numpy to model path

"""

# This part is important, creates an array of each bey's images. Cycling through the images makes it spin.
# Each image is transformed and made smaller to better fit the arena
player1Spin = [pygame.transform.scale(pygame.image.load('Images/Pegasus/Pegasus1.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/Pegasus/Pegasus2.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/Pegasus/Pegasus3.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/Pegasus/Pegasus4.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/Pegasus/Pegasus5.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/Pegasus/Pegasus6.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/Pegasus/Pegasus7.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/Pegasus/Pegasus8.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Images/Pegasus/Pegasus9.png'), (220, 220))]

player2Spin = [pygame.transform.scale(pygame.image.load('Images/LDrago/LDrago1.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/LDrago/LDrago2.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/LDrago/LDrago3.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/LDrago/LDrago4.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/LDrago/LDrago5.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/LDrago/LDrago6.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/LDrago/LDrago7.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load(
                   'Images/LDrago/LDrago8.png'), (220, 220)),
               pygame.transform.scale(pygame.image.load('Images/LDrago/LDrago9.png'), (220, 220))]

pygame.init()  # isnt inatilizing secondary modules GARBAGE SHIT FACE CODE

screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption('BeyBlade Game')

# image needs to be in the main file struct cant store in seprate folder, see if u can fix
# Background obj
Background = pygame.image.load('Images/ArenaBeyBladeVroom.jpg').convert()
screen.blit(Background, (0, 0))

# load method can have a specfied path - take that stack overflow u dumb bitch
# nvm they were right it cant be path specfic

# player obj - Pegasus
player = player1Spin[0]
player = pygame.transform.scale(player, (300, 300))
position = player.get_rect()
screen.blit(player, (250, 250))

screen.blit(Background, position, position)
pygame.display.update()
# https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate

# player2 obj - El Drago
player2 = player2Spin[0]
player2 = pygame.transform.scale(player2, (250, 250))
# i think i spelled Pegasus wrong
# nah you didn't
screen.blit(player2, (650, 650))
pygame.display.update()
clock = pygame.time.Clock()
i = 0
# Speeed is the refresh rate of the game, making it smaller makes it seem as if both beys are going faster. Lowest number
# is 1 highest number is 80. After 60 it starts to look wonky.
speeed = 60
# x is just something I was testing, it's not needed
x = 2
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # screen.blit(player,(500,500)) #blit is temporary and crashes , How to fix?
    # format error screen.blit(object (x,y))
    # update probaby needs to happen hear in loop

    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(500, 500, 100, 100))
    screen.blit(Background, (0, 0))
    player = player1Spin[i]
    screen.blit(player, (650 - x, 250))
    player2 = player2Spin[i]
    # Again, please ignore x.
    x += 25
    # changing i also changes how the beyblades look like when spinning. i = 1 means normal i = 4 means slightly faster
    # looking spinning. not that useful but thought u should know
    i += 4
    i = i % 9
    screen.blit(player2, (550, 500))

    pygame.display.flip()
    pygame.time.delay(speeed)
# for movement we cant use random values but we can [A,B,C,D] and change the rates at which each grow and decrease to
# make random movement
