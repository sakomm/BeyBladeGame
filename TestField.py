""" Atom dosent have a # DEBUG: so im fucking dumb but apparently VSC still has a collobration
 tool so might use that
"""
import pygame #from pygame.locals import * # WTF am i doing here, where the fuck is locals
""""
import numpy # use numpy to model path

"""
player2Spin = [pygame.image.load('L-Drago/LDrago.png'),pygame.image.load('L-Drago/LDrago1.png'),
               pygame.image.load('L-Drago/LDrago2.png'),pygame.image.load('L-Drago/LDrago3.png'),
               pygame.image.load('L-Drago/LDrago4.png'),pygame.image.load('L-Drago/LDrago5.png'),
               pygame.image.load('L-Drago/LDrago6.png'),pygame.image.load('L-Drago/LDrago7.png'),
               pygame.image.load('L-Drago/LDrago8.png')]
pygame.init() # isnt inatilizing secondary modules GARBAGE SHIT FACE CODE


screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption('BeyBlade Game')

# image needs to be in the main file struct cant store in seprate folder, see if u can fix
#Background obj
Background = pygame.image.load('ArenaBeyBladeVroom.jpg').convert()
screen.blit(Background,(0,0))

    #load method can have a specfied path - take that stack overflow u dumb bitch
    #nvm they were right it cant be path specfic

#player obj - Pegasus
player = pygame.image.load('PegasusIsLame.png')
player = pygame.transform.scale(player, (300, 300))
# i think i spelled Pegasus wrong
position = player.get_rect()
#make Pegasus smaller its a bit big
screen.blit(player, (250,250))
screen.blit(Background, position, position)
pygame.display.update()
#https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate

# player2 obj - El Drago
player2 = pygame.image.load('ELDrago1.png')
player2 = pygame.transform.scale(player2, (250, 250))
# i think i spelled Pegasus wrong
# nah you didn't
screen.blit(player2, (650,650))
pygame.display.update()
clock = pygame.time.Clock()
i = 0
speeed = 50

done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #screen.blit(player,(500,500)) #blit is temporary and crashes , How to fix?
                                    # format error screen.blit(object (x,y))
            # update probaby needs to happen hear in loop

        #pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(500, 500, 100, 100))
        screen.blit(Background, (0, 0))
        player = pygame.transform.rotate(player,90)
        screen.blit(player, (250,250))
        player2 = pygame.transform.scale(player2Spin[i], (250,250))
        i+= 3
        if i >= len(player2Spin):
                i = 0
        screen.blit(player2, (550,500))

        pygame.display.flip()
        pygame.time.delay(speeed)
# for movement we cant use random values but we can [A,B,C,D] and change the rates at which each grow and decrease to
# make random movement
