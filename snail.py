import pygame

class Snail:
    def __init__(self) -> None:
        self.snail_surface =  pygame.Surface((80,80))
        self.xpos = 0
    def update_pos(self):
        self.xpos += 10