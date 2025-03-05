import pygame
import settings as s
import colors


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(s.SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 42)


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

            self.states[self.game_state_manager.get_state()].update(events)
            if self.game_state_manager.get_state() == "quit":
                self.running = False

            pygame.display.flip()
            clock.tick(s.FPS)


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

    def update(self, events):
        screen.fill(colors.dark_purple)
        play_rect = draw_text(s.WIDTH // 2 - 80, 300, "Play", colors.white)
        highscore_rect = draw_text(s.WIDTH// 2 - 80, 350, "Highscore", colors.white)
        quit_rect = draw_text(s.WIDTH // 2 - 80, 400, "Quit", colors.white)
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

    def update(self, events):
        screen.fill(colors.dark_blue_black)


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
