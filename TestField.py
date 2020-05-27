""" Atom dosent have a # DEBUG: so im fucking dumb but apparently VSC still has a collobration
 tool so might use that
"""
import pygame #from pygame.locals import * # WTF am i doing here, where the fuck is locals

pygame.init() # isnt inatilizing secondary modules GARBAGE SHIT FACE CODE



screen = pygame.display.set_mode((1000, 1000))

#player obj

player = pygame.image.load('PegasusIsLame.jpg') # i think i spelled Pegasus wrong
position = player.get_rect()
screen.blit(player, position)
pygame.display.update()

# image needs to be in the main file struct cant store in seprate folder, see if u can fix
#https://www.pygame.org/docs/ref/transform.html#pygame.transform.rotate


done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.blit(player,500,500) #blit is temporary and crashes , How to fix?

        #pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(500, 500, 100, 100))
        pygame.display.flip()



# for movement we cant use random values but we can [A,B,C,D] and change the rates at which each grow and decrease to
# make random movement
