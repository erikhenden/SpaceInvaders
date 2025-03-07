import pygame
import settings
from random import randint
from entities import bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, animation_list, x, y, position, bullet_animation_list):
        super().__init__()
        self.frame = 0
        self.animation_list = animation_list
        self.image = self.animation_list[self.frame]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 12
        self.direction = "left"
        self.movement_timer = 0
        self.position = position
        self.move_down = False
        self.bullet_timer = randint(0, 2000)
        self.bullet_animation_list = bullet_animation_list

        # Calculate reversed position, used to stay in correct position when the group of enemies has reached the
        # right side of the screen
        poslist = [i for i in range(12)]
        reverse_poslist = sorted(poslist, reverse=True)
        self.reverse_position = reverse_poslist[self.position]

    def shoot(self, add_time, enemy_bullet_group):
        self.bullet_timer += add_time
        if self.bullet_timer >= randint(2000, 3500):
            if randint(0, 20) == 20:
                enemy_bullet_group.add(bullet.EnemyBullet(self.bullet_animation_list, self.rect.midbottom))
            self.bullet_timer = 0

    def update(self, add_time, enemy_bullet_group):
        self.movement_timer += add_time
        if self.movement_timer > settings.enemy_animation_cooldown:

            # Update frame
            if self.frame == 0:
                self.frame = 1
            else:
                self.frame = 0

            # Move
            if self.direction == "left":
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed

            if self.move_down:
                self.rect.y += 40
                self.move_down = False

            self.movement_timer = 0

            self.image = self.animation_list[self.frame]

        # Check border collision, change direction
        if self.rect.x <= 0 + (self.position * (settings.ENEMY_SCALE * 32)):
            self.direction = "right"
            self.move_down = True
        if self.rect.right >= settings.WIDTH - (self.reverse_position * (settings.ENEMY_SCALE * 32)):
            self.direction = "left"
            self.move_down = True

        # Shoot
        self.shoot(add_time, enemy_bullet_group)
