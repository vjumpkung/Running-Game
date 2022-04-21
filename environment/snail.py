import pygame


class Snail:

    def __init__(self):
        self.snail_surface = pygame.Surface((80, 80))
        self.xpos = 0

    def move_forward(self, speed):
        self.xpos += speed

    def move_to_default(self):
        self.xpos = -50
