import pygame
import settings as s
import colors

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(s.SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 64)


# function to draw text
def draw_text(x, y, text, color):
    text = font.render(text, True, color)
    text_rect = text.get_rect(topleft=(x, y))
    screen.blit(text, text_rect)
    return text_rect


# Game class
class Game:
    def __init__(self):
        self.running = True
        self.game_state_manager = GameStateManager("main_menu")
        self.main_menu = MainMenu(self.game_state_manager)
        self.play = Play(self.game_state_manager)
        self.states = {"main_menu": self.main_menu,
                       "play": self.play}

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.states[self.game_state_manager.get_state()].update(events)

            pygame.display.flip()
            clock.tick(s.FPS)

# Class Game State Manager
class GameStateManager:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

# Main Menu
class MainMenu:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

    def update(self, events):
        screen.fill(colors.dark_purple)
        play_rect = draw_text(s.WIDTH // 2 - 50, 300, "Play", colors.white)
        pos = pygame.mouse.get_pos()

        for event in events:

            if event.type == pygame.MOUSEBUTTONUP:
                if play_rect.collidepoint(pos):
                    self.game_state_manager.set_state("play")


class Play:
    def __init__(self, game_state_manager):
        self.game_state_manager = game_state_manager

    def update(self, events):
        screen.fill(colors.dark_blue_black)



if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()

