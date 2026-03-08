import pygame
from space_invaders.settings import HEIGHT, WIDTH

class Player:
    def __init__(self):
        self.image =  pygame.transform.scale(
            pygame.image.load('resources/player.png').convert_alpha(),
            (96,64)
        )
        self.health = 3
        self.position = (0,64*(HEIGHT-1))

    def move(self, displacement):
        position = self.position[0] + displacement
        self.position = (
            max(0, min((WIDTH-1)*96, position)), 
            self.position[1]
        )