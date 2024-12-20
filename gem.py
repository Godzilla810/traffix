import pygame
from setting import *

class Gem(pygame.sprite.Sprite):
    def __init__(self, row, col, color_name):
        super().__init__()
        self.row = row
        self.col = col
        self.color_name = color_name
        self.image = pygame.image.load(f"Image/Gems/{self.color_name}.png")
        self.image = pygame.transform.scale(self.image, (GEM_SIZE, GEM_SIZE))
        self.set_rect()
        
    def set_rect(self):
        self.rect = self.image.get_rect(center=(GRID_SIZE / 2 + self.row * GRID_SIZE, 
                                                GRID_SIZE / 2 +  PUZZLE_HEIGHT_Y + self.col * GRID_SIZE))

    def is_adjacent(self, target: 'Gem'):
        return abs(self.row - target.row) + abs(self.col - target.col) == 1
    
    def swap(self, target : 'Gem'):
        self.row, target.row = target.row, self.row
        self.col, target.col = target.col, self.col

