import pygame
from environment.background import Background
from environment.snail import Snail
from settings import Settings, get_fps
from sys import exit

# loading every class here
settings = Settings()
snail = Snail()
background = Background()

# constants
NAME = settings.NAME
FPS = settings.FPS
WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT


class StartGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(NAME)


class Font:
    def __init__(self):
        self.font = pygame.font.Font('font/ubuntu.ttf', 50)
        self.fpsfont = pygame.font.Font('font/ubuntu.ttf', 20)


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()


class Drawing:
    def __init__(self):

        font = Font()

        # drawing surface
        self.sky_surface = background.sky_surface
        background.SetSkyColor('lightblue')

        # drawing ground
        self.ground_surface = background.ground_surface
        background.SetGroundColor('lightgreen')

        # drawing font
        self.font_surface = font.font.render(NAME, True, 'Black')
        self.font_position = self.font_surface.get_rect(
            center=(WIDTH/2, (HEIGHT/2) - 300))


class Game:
    def __init__(self):

        self.start = StartGame()
        self.screen = Screen().screen
        self.clock = Screen().clock
        self.draw = Drawing()
        self.font = Font()

    def LoopFunction(self):
        # draw everything
        screen = self.screen
        screen.blit(self.draw.sky_surface, (0, 0))
        screen.blit(self.draw.ground_surface, (0, 520))
        screen.blit(self.draw.font_surface, self.draw.font_position)
        screen.blit(snail.snail_surface, (snail.xpos, 460))
        screen.blit(get_fps(self.font.fpsfont, self.clock), (0, 0))

        # snail
        snail.move_forward(5)  # snail moving
        if(snail.xpos > WIDTH + 100):
            snail.move_to_default()  # if snail out of screen

        # updating display
        pygame.display.update()
        self.clock.tick(FPS)

        # quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
