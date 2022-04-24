import pygame
from settings import Settings

WIDTH = Settings().WIDTH


class Snail:

    '''
        This class is a obstacle so player cannot hit this unless you will lose.
    '''

    def __init__(self):
        self.snail_surface = pygame.Surface((80, 80))
        self.xpos = WIDTH

        self.snail_rect = self.snail_surface.get_rect(
            midbottom=(self.xpos, 540))

    def move_forward(self, speed, move_per_frame):
        self.snail_rect.x -= speed * move_per_frame

    def move_to_default(self):
        self.snail_rect.left = WIDTH

    def move(self, move_per_frame):
        self.move_forward(5, move_per_frame)
        if(self.snail_rect.right < 0):
            self.move_to_default()  # if snail out of screen
