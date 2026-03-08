import pygame

class Alien:
    def __init__(self, speed, random_number):
        self.image = pygame.transform.scale(
            pygame.image.load('resources/alien.png').convert_alpha(),
            (96,64)
        )
        self.speed = speed
        self.position = (
            random_number*96,
            64
        )
    
    def move(self):
        self.position = (
            self.position[0],
            self.position[1] + self.speed
        )