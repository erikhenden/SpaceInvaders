import pygame

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()  # Lager surface som aktuell frame 'blittes' på
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))  # Henter ut den aktuelle framen frå spritesheet
        image = pygame.transform.scale(image, (width * scale, height * scale))  # Endrer størrelsen
        image.set_colorkey(color)  # Fjerner bakgrunnsfargen som er rundt det aktuelle bildet
        return image

    def get_image_flipped(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()  # Laster spritesheet
        image.blit(self.sheet, (0, 0),
                   ((frame * width), 0, width, height))  # Henter ut den aktuelle framen frå spritesheet
        image = pygame.transform.scale(image, (width * scale, height * scale))  # Endrer størrelsen
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(color)  # Fjerner bakgrunnsfargen som er rundt det aktuelle bildet
        return image