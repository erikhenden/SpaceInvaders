import pygame
import settings
import spritesheet_helper
import colors

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, image, midbottom):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom
        self.speed = 8

    def update(self):
        self.rect.y -= self.speed


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, animation_list, mid_top):
        super().__init__()
        self.frame = 0
        self.animation_list = animation_list
        self.image = self.animation_list[self.frame]
        self.rect = self.image.get_rect(midtop=mid_top)
        self.speed = 6
        self.animation_timer = 0

    def update(self, add_time):
        self.animation_timer += add_time
        if self.animation_timer >= settings.ENEMY_BULLET_ANIMATION_COOLDOWN:
            if self.frame == 0:
                self.frame = 1
            else:
                self.frame = 0

            self.image = self.animation_list[self.frame]  # Update animation frame
            self.animation_timer = 0  # Reset timer

        self.rect.y += self.speed