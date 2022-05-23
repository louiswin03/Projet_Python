import pygame
from player import *


class full_health:

    def __init__(self):
        self.box = pygame.image.load('heartFull.png')

    def render(self, screen):
        screen.blit(self.box, (720, 0))


class mid_health:

    def __init__(self):
        self.box = pygame.image.load('heartMid.png')

    def render(self, screen):
        screen.blit(self.box, (720, 0))
