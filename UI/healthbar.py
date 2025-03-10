import pygame


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, animationlist, x, y):
        super().__init__()
        self.animation_list = animationlist
        self.frame = 2
        self.image = self.animation_list[self.frame]
        self.rect = self.image.get_rect(topleft=(x, y))

    def reduce(self):
        if self.frame > 0:
            self.frame -= 1
            self.image = self.animation_list[self.frame]