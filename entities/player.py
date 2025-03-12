import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(settings.WIDTH // 2, settings.HEIGHT - 80))
        self.speed = 5
        self.hit = False
        self.hit_enemy = False
        self.lives = 3
        self.score = 0
        self.shoot_cooldown = 500

    def move(self, keys):
        if keys[pygame.K_a]:  # Move left
            self.rect.x -= self.speed
        if keys[pygame.K_d]:  # Move right
            self.rect.x += self.speed

        # Check edge collision
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.right >= settings.WIDTH:
            self.rect.right = settings.WIDTH

    def update(self, keys):
        if not settings.enemies_stop:
            self.move(keys)