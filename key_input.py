import pygame


class KeyboardInput:

    # get key press
    def __init__(self):
        self.keys = pygame.key.get_pressed()

    # jump key
    def jump(self, event, button):
        if event.type == pygame.KEYDOWN:
            if event.key == button or event.key == pygame.K_UP:
                return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                return True
        return False

    # retry key
    def retry(self, event, button):
        if event.type == pygame.KEYDOWN:
            if event.key == button:
                return True
