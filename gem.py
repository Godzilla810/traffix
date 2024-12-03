import pygame
from setting import *
import random


class Gem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color_name = random.choice(COLOR_LIST)
        self.image = pygame.image.load(f"Image/Gems/{self.color_name}.png")
        self.image = pygame.transform.scale(self.image, (57, 66))
        self.rect = self.image.get_rect(center=(self.x, self.y))
