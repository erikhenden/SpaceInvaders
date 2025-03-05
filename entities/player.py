import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT - 80))
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_a]:  # Move left
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  # Move right
            self.rect.x += self.speed

    def shoot(self, keys):
        if keys[pygame.K_SPACE]:
            pass

    def update(self, keys):
        self.move(keys)
        self.shoot(keys)