import pygame

class Projectile:
    def __init__(self, player_position):
        self.image =  pygame.transform.scale(
            pygame.image.load('resources/projectile.png').convert_alpha(),
            (32,64)
        )
        self.position = (
            player_position[0] + 32,
            player_position[1] - 64
        )
    
    def move(self):
        self.position = (
            self.position[0],
            self.position[1] - 32
        )