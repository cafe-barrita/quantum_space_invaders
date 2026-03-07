import sys
import pygame
from pygame.locals import *
from space_invaders.settings import WIDTH, HEIGHT, QBITS
from space_invaders.QuantumRng import QuantumRng
from space_invaders.Player import Player

if __name__ == "__main__":
    rng = QuantumRng(QBITS)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH*96, (HEIGHT+1)*64))
    background = pygame.Surface(screen.get_size())
    background.fill((0,0,0,255))
    player = Player()
    alien = pygame.image.load('resources/alien.png').convert_alpha()
    empty_heart = pygame.image.load('resources/empty_heart.png').convert_alpha()
    empty_heart = pygame.transform.scale(empty_heart, (32,64))
    full_heart = pygame.image.load('resources/full_heart.png').convert_alpha()
    full_heart = pygame.transform.scale(full_heart, (32,64))
    projectile = pygame.image.load('resources/projectile.png').convert_alpha()
    font = pygame.font.SysFont('Courier New', 16)
    clock = pygame.time.Clock()
    score = 0
    keep_playing =True
    while keep_playing:
        if player.health == 0:
            keep_playing = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False
        # TODO keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-16)
        if keys[pygame.K_RIGHT]:
            player.move(16)
        screen.blit(background, (0,0))
        for i in range(player.health):
            screen.blit(full_heart, (32*i, 0))
        for i in range(3 - player.health):
            screen.blit(empty_heart, (32*(i + player.health), 0))
        screen.blit(font.render(f'Score: {score}', True, pygame.Color('white')), (96,24))
        screen.blit(player.image, player.position)
        # TODO draw alien and projectiles
        pygame.display.update()
        clock.tick(36)
    pygame.quit()
    sys.exit()