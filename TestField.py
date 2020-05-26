""" Atom dosent have a # DEBUG: so im fucking dumb but apparently VSC still has a collobration
 tool so might use that
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True


        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(500, 500, 100, 100))
        pygame.display.flip()
