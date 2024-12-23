import pygame
from setting import *

class Car(pygame.sprite.Sprite):
    def __init__(self, row, col, capacity):
        super().__init__()
        self.row = row
        self.col = col
        self.capacity = capacity
        self.image = pygame.image.load(f"Image/Cars/car01iso_0007.png")
        self.image = pygame.transform.scale(self.image, (GEM_SIZE, GEM_SIZE))
        self.rect = self.image.get_rect()
        self.set_rect()
        
    def set_rect(self):
        self.rect.center = (GRID_SIZE / 2 + self.row * GRID_SIZE, 
                            GRID_SIZE / 2 +  PUZZLE_Y + self.col * GRID_SIZE)

    def update(self):
        self.rect.x += 5
        if self.rect.x > SCREEN_WIDTH:
            self.kill()
