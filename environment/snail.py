import pygame
from random import randint
from utils.settings import Settings

WIDTH = Settings().WIDTH


class Snail:

    '''
        This class is a obstacle so player cannot hit this unless you will lose.
    '''

    def __init__(self):
        self.snail_surface = pygame.Surface((40, 40))
        self.xpos = WIDTH
        self.speed = 6
        self.snail_rect = self.snail_surface.get_rect(
            midbottom=(self.xpos, 540))
        self.acceleration = 0

    def random_size(self):
        self.size = randint(40, 60)
        self.snail_surface = pygame.Surface((self.size, self.size))
        self.snail_rect = self.snail_surface.get_rect(
            midbottom=(self.xpos, 540))

    def random_speed(self):
        self.speed = randint(6 + self.acceleration, 10 + self.acceleration)

    def move_forward(self, move_per_frame):
        self.snail_rect.x -= self.speed * move_per_frame

    def move_to_default(self):
        self.snail_rect.left = WIDTH
        self.random_speed()

    def move(self, move_per_frame):
        self.move_forward(move_per_frame)
        if(self.snail_rect.right < 0):
            self.move_to_default()  # if snail out of screen
            self.random_size()
            return True

    def add_acceleration(self):
        if self.acceleration < 25:
            self.acceleration += 1
        else:
            pass

    def reset_acceleration(self):
        self.acceleration = 0
