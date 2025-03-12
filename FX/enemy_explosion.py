class EnemyExplosion:
    def __init__(self, image, center_pos):
        self.image = image
        self.rect = self.image.get_rect(center=center_pos)
        self.timer = 300

    def update(self, withdraw_time):
        self.timer -= withdraw_time

    def draw(self, screen):
        screen.blit(self.image, self.rect)