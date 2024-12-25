import pygame
from setting import *

class Car(pygame.sprite.Sprite):
    def __init__(self, row, col, color, matches_num):
        super().__init__()
        self.color = color
        self.capacity = 2 ** (matches_num - 1)
        self.image = pygame.image.load(f"Image/Vehicles/{VEHICLE_TYPE.get(self.capacity)}/{self.color}.png")
        self.image = pygame.transform.scale(self.image, (GEM_SIZE, GEM_SIZE))
        self.rect = self.image.get_rect()
        self.set_position(row, col)
    
    def set_position(self, row, col):
        self.rect.center = (PUZZLE_X + GRID_SIZE / 2 + row * GRID_SIZE, 
                            PUZZLE_Y + GRID_SIZE / 2 + col * GRID_SIZE)

    def update(self):
        # animation
        # move
        self.rect.x += 5
        # constraint
        if self.rect.x > SCREEN_WIDTH:
            self.kill()
