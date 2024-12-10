import pygame
from setting import *
import random


class Gem(pygame.sprite.Sprite):
    vacant_x = 0
    vacant_y = 0
    def __init__(self, x, y, color_name):
        super().__init__()
        self.x = x
        self.y = y
        self.color_name = color_name
        self.image = pygame.image.load(f"Image/Gems/{self.color_name}.png")
        self.image = pygame.transform.scale(self.image, (57, 66))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move_to(self, x, y):
        self.rect.center = (x, y)