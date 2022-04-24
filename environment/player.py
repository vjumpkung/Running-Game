import pygame

class Player:
    
    '''
        This class is about player and you are controlling this.
    '''
    
    def __init__(self):
        
        # create player object
        self.player_surface = pygame.Surface((100,100))
        self.player_surface.fill("red")
        
        # default player position
        self.xpos = 150
        
        # player hitbox
        self.player_rect = self.player_surface.get_rect(midbottom = (self.xpos,540))
        
    def move(self, move_per_frame):
        
        self.player_rect.left += 3 * move_per_frame
        
        