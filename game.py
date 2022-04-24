import pygame
from environment.background import Background
from environment.snail import Snail
from environment.player import Player
from settings import Settings, get_fps
from sys import exit
from time import time

# loading every class here
settings = Settings()
background = Background()
snail = Snail()
player = Player()

'''
    loading constatns from settings.py
'''

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

    '''
        Loading only one time.
    '''

    def __init__(self):

        self.start = StartGame()
        self.screen = Screen().screen
        self.clock = Screen().clock
        self.draw = Drawing()
        self.font = Font()
        self.now_time = time()
        self.move_per_second = 60

    '''
        Loop until you stop the game.
    '''

    def LoopFunction(self):

        running = True

        while running:
            # tick
            self.ms_frame = self.clock.tick(FPS)
            self.move_per_frame = round(
                self.move_per_second * self.ms_frame / 1000)

            # draw everything
            screen = self.screen
            screen.blit(self.draw.sky_surface, (0, 0))
            screen.blit(self.draw.ground_surface, (0, 540))
            screen.blit(self.draw.font_surface, self.draw.font_position)
            screen.blit(player.player_surface, player.player_rect)
            screen.blit(snail.snail_surface, snail.snail_rect)
            screen.blit(get_fps(self.font.fpsfont, self.clock), (0, 0))

            # entities
            snail.move(self.move_per_frame)
            # player.move(self.move_per_frame)

            # updating display
            pygame.display.update()
            screen.fill("lightblue")

            # quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
