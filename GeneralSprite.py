import pygame


class GeneralSprite(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.olist = self.mask.outline()

    def update(self):
        self.mask = pygame.mask.from_surface(self.image.convert_alpha())

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
