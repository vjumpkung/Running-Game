from snail import Snail
import pygame
from sys import exit

# Init pygame
pygame.init()
pygame.display.set_caption("Paimon Running")
FPS = 60

#loading font
font = pygame.font.Font('font/ubuntu.ttf',50)
fpsfont = pygame.font.Font('font/ubuntu.ttf',20)

# create screen
screen = pygame.display.set_mode((1280,720))
clock  = pygame.time.Clock()

# drawing surface
sky_surface = pygame.Surface((1280,720))
sky_surface.fill('lightblue')

# drawing ground
ground_surface = pygame.Surface((1280,200))
ground_surface.fill('lightgreen')

# drawing font
font_surface = font.render('Paimon', True, 'Black')
# drawing snail

snail = Snail()

# main game
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,520))
    screen.blit(font_surface,(530,60))
    screen.blit(fpsfont.render(f'FPS {clock.get_fps():.0f}',True,'Black'),(0,0))
    
    # snail moving
    screen.blit(snail.snail_surface,(snail.xpos,460))
    snail.update_pos()
    
    if(snail.xpos > 1380):
        snail.xpos = -40
        
        
    # draw everything
    pygame.display.update()
    clock.tick(FPS)
    
    