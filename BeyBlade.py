import pygame


class BeyBlade(pygame.sprite.Sprite):
    number = 0

    def __init__(self, list, number):
        pygame.sprite.Sprite.__init__(self)

        self.list = list
        self.number = number
        self.image = list[BeyBlade.number % 9]

        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.olist = self.mask.outline()

    def update(self, numm):
        BeyBlade.number += 1
        self.rect.x = self.rect.x + numm
        self.image = self.list[BeyBlade.number % 9]
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())
        self.olist = self.mask.outline()

    def draw(self, screen, y):
        screen.blit(self.image, (self.rect.x, y))


