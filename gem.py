import pygame
from setting import *

class Gem(pygame.sprite.Sprite):
    def __init__(self, row, col, color_name):
        super().__init__()
        self.color = color_name
        self.size = 0
        self.image = pygame.image.load(f"Image/Gems/{self.color}.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.set_position(row, col)
    
    # 設定珠子位置
    def set_position(self, row, col):
        self.rect.center = (PUZZLE_X + GRID_SIZE / 2 + row * GRID_SIZE, 
                            PUZZLE_Y + GRID_SIZE / 2 + col * GRID_SIZE)
    
    def update(self):
        # 放大動畫
        if (self.size < GEM_SIZE):
            old_center = self.rect.center
            self.size += 3
            self.image = pygame.image.load(f"Image/Gems/{self.color}.png")
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.rect = self.image.get_rect()
            self.rect.center = old_center