import pygame
import settings

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, midbottom):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom
        self.speed = 4

    def update(self):
        self.rect.y -= self.speed