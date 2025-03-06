import pygame

from entities.bullet import Bullet
from entities import enemy
import settings
import colors
import spritesheet_helper
from entities import player


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(settings.SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 42)


# Load player image
player_image = spritesheet_helper.SpriteSheet(pygame.image.load("images/player.png").convert_alpha())
player_image = player_image.get_image(0, 32, 32, 1, colors.black)

# Load enemy spritesheet
enemy1_animations = []
enemy2_animations = []
enemy3_animations = []

enemy1_spritesheet = spritesheet_helper.SpriteSheet(pygame.image.load("images/enemy1.png").convert_alpha())
enemy2_spritesheet = spritesheet_helper.SpriteSheet(pygame.image.load("images/enemy2_crab.png").convert_alpha())
enemy3_spritesheet = spritesheet_helper.SpriteSheet(pygame.image.load("images/enemy3.png").convert_alpha())

# Add enemy_spritesheet images
for frame in range(2):  # 2 animations/frames
    enemy1_animations.append(enemy1_spritesheet.get_image(frame, 32, 32, settings.ENEMY_SCALE, colors.black))

for frame in range(2):  # 2 animations/frames
    enemy2_animations.append(enemy2_spritesheet.get_image(frame, 32, 32, settings.ENEMY_SCALE, colors.black))

for frame in range(2):  # 2 animations/frames
    enemy3_animations.append(enemy3_spritesheet.get_image(frame, 32, 32, settings.ENEMY_SCALE, colors.black))


# Load bullet image
bullet_image = spritesheet_helper.SpriteSheet(pygame.image.load("images/bullet.png").convert_alpha())
bullet_image = bullet_image.get_image(0, 8, 8, 1, colors.black)


# Function to draw text
def draw_text(x, y, text, color):
    text = font.render(text, True, color)
    text_rect = text.get_rect(topleft=(x, y))
    screen.blit(text, text_rect)
    return text_rect


class Game:
    def __init__(self):
        self.running = True
        self.game_state_manager = GameStateManager("main_menu")
        self.main_menu = MainMenu(self.game_state_manager)
        self.play = Play(self.game_state_manager)
        self.quit = Quit(self.game_state_manager)

        self.states = {"main_menu": self.main_menu,
                       "play": self.play,
                       "quit": self.quit
                       }

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.states[self.game_state_manager.get_state()].update(events, keys)
            if self.game_state_manager.get_state() == "quit":
                self.running = False

            pygame.display.flip()
            clock.tick(settings.FPS)


class GameStateManager:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state


class MainMenu:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

    def update(self, events, keys):
        screen.fill(colors.dark_purple)
        play_rect = draw_text(settings.WIDTH // 2 - 80, 300, "Play", colors.white)
        highscore_rect = draw_text(settings.WIDTH// 2 - 80, 350, "Highscore", colors.white)
        quit_rect = draw_text(settings.WIDTH // 2 - 80, 400, "Quit", colors.white)
        pos = pygame.mouse.get_pos()

        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_rect.collidepoint(pos):
                    self.game_state_manager.set_state("play")
                if highscore_rect.collidepoint(pos):
                    pass
                if quit_rect.collidepoint(pos):
                    self.game_state_manager.set_state("quit")


class Play:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

        # Groups
        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        # Add player
        self.player = player.Player(player_image)
        self.player_group.add(self.player)

        # Add enemies
        startpos = 150
        current_row = 0
        for row in range(settings.TOTAL_ROWS):

            # Get correct enemy spritesheet
            if current_row == 0 or current_row == 1:
                animations = enemy1_animations
            elif current_row == 2 or current_row == 3:
                animations = enemy2_animations
            elif current_row == 4 or current_row == 5:
                animations = enemy3_animations

            for i in range(12):
                new_enemy = enemy.Enemy(animations, (startpos + (i * 32)) * settings.ENEMY_SCALE, 70 + (current_row * (settings.ENEMY_SCALE * 32)), i)
                self.enemy_group.add(new_enemy)
            current_row += 1

    def update(self, events, keys):
        screen.fill(colors.dark_blue_black)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state_manager.set_state("main_menu")
                if event.key == pygame.K_SPACE:
                    self.bullet_group.add(Bullet(bullet_image, self.player.rect.midtop))

        # Check bullet-enemy collision
        pygame.sprite.groupcollide(self.enemy_group, self.bullet_group, True, True)

        # Update
        self.player_group.update(keys)
        self.enemy_group.update(clock.get_time())
        self.bullet_group.update()

        # Draw
        self.player_group.draw(screen)
        self.enemy_group.draw(screen)
        self.bullet_group.draw(screen)


class Quit:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

    def update(self):
        pass


class HighScore:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

    def update(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
