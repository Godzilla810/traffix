import pygame
from setting import *

class Gem(pygame.sprite.Sprite):
    vacant_row = 0
    vacant_col = 0
    def __init__(self, row, col, color_name):
        super().__init__()
        self.row = row
        self.col = col
        self.color_name = color_name
        self.image = pygame.image.load(f"Image/Gems/{self.color_name}.png")
        self.image = pygame.transform.scale(self.image, (GEM_SIZE, GEM_SIZE))
        self.rect = self.image.get_rect(center=(GRID_SIZE / 2 + self.row * GRID_SIZE, 
                                                GRID_SIZE / 2 +  SCREEN_HEIGHT_BOARD + self.col * GRID_SIZE))

    def move_to(self, x, y):
        self.rect.center = (x, y)