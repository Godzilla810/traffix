import pygame
from setting import *

class Gem(pygame.sprite.Sprite):
    def __init__(self, row, col, color_name):
        super().__init__()
        self.row = row
        self.col = col
        self.color_name = color_name
        self.size = 0
        self.image = pygame.image.load(f"Image/Gems/{self.color_name}.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.set_rect()
        
    def get_standard_position(self):
        return (GRID_SIZE / 2 + self.row * GRID_SIZE, 
                GRID_SIZE / 2 +  PUZZLE_HEIGHT + self.col * GRID_SIZE)
    
    def set_rect(self):
        self.rect.center = self.get_standard_position()

    def is_adjacent(self, target: 'Gem'):
        return abs(self.row - target.row) + abs(self.col - target.col) == 1
    
    def swap(self, target : 'Gem'):
        self.row, target.row = target.row, self.row
        self.col, target.col = target.col, self.col

    def update(self):
        if (self.size < GEM_SIZE):
            self.size += 3
            self.image = pygame.image.load(f"Image/Gems/{self.color_name}.png")
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.rect = self.image.get_rect()
            self.set_rect()