import pygame
from random import randint
from environment.background import Background
from environment.snail import Snail
from environment.player import Player
from settings import Settings, get_fps, MaximumScore
from key_input import KeyboardInput
from time import time


# loading every class here
settings = Settings()
background = Background()
snail = Snail()
player = Player()
maximum = MaximumScore()

'''
    loading constants from settings.py
'''

# constants
NAME = settings.NAME
FPS = 60
WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT

# pygame init
class StartGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(NAME)


# loading font and size
class Font:
    def __init__(self):
        self.font = pygame.font.Font('font/Minecraft.ttf', 50)
        self.fpsfont = pygame.font.Font('font/Minecraft.ttf', 20)
        self.score = pygame.font.Font('font/Minecraft.ttf', 30)

# loading screen
class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

# drawing font
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
        self.font_surface = font.font.render(NAME, False, 'Black')
        self.font_position = self.font_surface.get_rect(
            center=(WIDTH/2, (HEIGHT/2) - 300))

        # drawing game over
        self.gameover = font.font.render('GAME OVER', False, 'Black')
        self.gameover_rect = self.gameover.get_rect(
            center=(WIDTH/2, (HEIGHT/2)))

        # drawing score
        self.score_font = font.score.render(f'SCORE : 0', False, 'Black')
        self.score_font_rect = self.score_font.get_rect(topleft=(10, 50))

        # drawing personal best
        self.max_font = font.score.render(
            f'PERSONAL BEST : {maximum.personal_best}', False, 'Black')
        self.max_font_rect = self.max_font.get_rect(topleft=(10, 80))

# update score and save personal best score
class Score:
    def __init__(self):
        self.score = 0
        self.font = Font()

    def update_score(self, draw):

        self.score += 1
        draw.score_font = self.font.score.render(
            f'SCORE : {self.score}', False, 'Black')

    def reset_score(self, draw):
        self.score = 0
        draw.score_font = self.font.score.render(
            f'SCORE : {self.score}', False, 'Black')

    def update_best_score(self, draw):
        draw.max_font = self.font.score.render(
            f'PERSONAL BEST : {maximum.personal_best}', False, 'Black')

# loading everything goes here.
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
        self.score = Score()
        self.now_time = time()
        self.move_per_second = 60
        self.isActive = True

    '''
        Loop until you stop the game.
    '''

    def LoopFunction(self):

        running = True

        while running:
            # tick
            self.ms_frame = self.clock.tick(FPS)
            self.move_per_frame = self.move_per_second * self.ms_frame / 1000

            if self.isActive:

                '''
                    When game is still running and not end.
                '''

                # draw everything

                screen = self.screen
                screen.blit(self.draw.sky_surface, (0, 0))
                screen.blit(self.draw.ground_surface, (0, 540))
                screen.blit(self.draw.font_surface, self.draw.font_position)
                screen.blit(player.player_surface, player.player_rect)
                screen.blit(snail.snail_surface, snail.snail_rect)
                screen.blit(get_fps(self.font.fpsfont, self.clock), (10, 10))
                screen.blit(self.draw.score_font, self.draw.score_font_rect)
                screen.blit(self.draw.max_font, self.draw.max_font_rect)

                # entities

                if(snail.move(self.move_per_frame)):
                    self.score.update_score(self.draw)
                    if self.score.score % 5 == 0:
                        snail.add_acceleration()

                # player

                player.add_gravity(self.move_per_frame)
                player.move(self.move_per_frame)
                player.floor()

                # collide check

                if player.isCollide(snail.snail_rect):
                    # stopping game
                    self.isActive = False

                    # update max score
                    maximum.update_score(self.score.score)
                    self.score.update_best_score(self.draw)
                    pygame.draw.rect(screen, "lightblue", self.draw.max_font_rect)
                    screen.blit(self.draw.max_font, self.draw.max_font_rect)

            else:
                '''
                    GAMEOVER when self.isActive = False
                '''
                screen.blit(self.draw.gameover, self.draw.gameover_rect)

            # get keyboard input

            self.kb = KeyboardInput()

            # updating display
            
            pygame.display.update()

            # event handle
            
            for event in pygame.event.get():

                # check quit event

                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

                # using SPACE , left click button or up button to jump

                if self.kb.jump(event, pygame.K_SPACE) and 540 <= player.player_rect.bottom <= 542:
                    player.set_gravity(-27)

                # using r to retry game and reset score to 0

                if self.kb.retry(event, pygame.K_r) and not self.isActive:
                    snail.reset_acceleration()
                    snail.move_to_default()
                    self.score.reset_score(self.draw)
                    self.isActive = True
                    continue
