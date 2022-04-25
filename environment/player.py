from typing import Tuple
import pygame


class Player:

    '''
        This class is about player and you are controlling this.
    '''

    def __init__(self):

        # create player object
        self.player_surface = pygame.Surface((100, 100))
        self.player_surface.fill("red")

        # default player position
        self.xpos = 150
        self.gravity = 0

        # player hitbox
        self.player_rect = self.player_surface.get_rect(
            midbottom=(self.xpos, 540))

    def floor(self):
        if self.player_rect.bottom >= 540:
            self.player_rect.bottom = 540

    def add_gravity(self, move_per_frame):

        self.gravity += move_per_frame

    def set_gravity(self, value):

        self.gravity = value

    def move(self, move_per_frame):

        self.player_rect.y += self.gravity * move_per_frame

    def isCollide(self, obstacle):

        return self.player_rect.colliderect(obstacle)

    def get_collidepoint(self, pos: Tuple):

        return self.player_rect.collidepoint(pos)
