import pygame
from setting import *

class Gem(pygame.sprite.Sprite):
    def __init__(self, row, col, color : str):
        super().__init__()
        # attribute
        self.color = color
        # animation
        self.size = 0
        self.image = pygame.image.load(f"../Image/Gems/{self.color}.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        # position
        self.rect = self.image.get_rect()
        self.set_position(row, col)
    
    def set_position(self, row, col):
        self.rect.center = (PUZZLE_X + GRID_SIZE / 2 + row * GRID_SIZE, 
                            PUZZLE_Y + GRID_SIZE / 2 + col * GRID_SIZE)
    
    def update(self):
        # animation
        if (self.size < GEM_SIZE):
            old_center = self.rect.center
            self.size += 3
            self.image = pygame.image.load(f"../Image/Gems/{self.color}.png")
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.rect = self.image.get_rect()
            self.rect.center = old_center