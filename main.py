import sys
import pygame
from pygame.locals import *
from space_invaders.settings import WIDTH, HEIGHT, QBITS, BACKEND, API_KEY
from quantum.quantum_rng import QuantumRng
from space_invaders.player import Player
from space_invaders.alien import Alien
from space_invaders.projectile import Projectile

if __name__ == "__main__":
    rng = QuantumRng(QBITS, BACKEND, API_KEY)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH*96, HEIGHT*64))
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
    frames_to_spawn = 0
    alien_speed = 4
    aliens = []
    projectiles = []
    keep_playing =True
    while keep_playing:
        destroyed_aliens = []
        destroyed_projectiles = []
        if player.health == 0:
            keep_playing = False

        for alien in aliens:
            alien.move()
            if alien.position[1] >= (HEIGHT-1) * 64:
                player.health -= 1
                destroyed_aliens.append(alien)
        for projectile in projectiles:
            projectile.move()
            for alien in aliens:
                if alien.position[0] + 16 <= projectile.position[0] <= alien.position[0] + 80 and \
                    projectile.position[1] <= alien.position[1] + 32:
                    score += 1
                    destroyed_aliens.append(alien)
                    destroyed_projectiles.append(projectile)
            if projectile.position[1] <= 64:
                destroyed_projectiles.append(projectile)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                projectiles.append(Projectile(player.position))
        
        if frames_to_spawn == 0:
            aliens.append(
                Alien(
                    alien_speed,
                    rng.generate()
                )
            )
            frames_to_spawn = 36
            alien_speed = min(alien_speed+1,24)
        else:
            frames_to_spawn -= 1

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
        for alien in aliens:
            screen.blit(alien.image, alien.position)
        for projectile in projectiles:
            screen.blit(projectile.image, projectile.position)

        for alien in destroyed_aliens:
            try:
                aliens.remove(alien)
            except:
                pass
        for projectile in destroyed_projectiles:
            try:
                projectiles.remove(projectile)
            except:
                pass
        pygame.display.update()
        clock.tick(36)
    pygame.quit()
    sys.exit()