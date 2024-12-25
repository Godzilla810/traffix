import pygame
from setting import *
from animation import Animation

class Car(pygame.sprite.Sprite):
    def __init__(self, row, col, color : str, matches_num : int):
        super().__init__()
        # attribute
        self.color = color
        self.capacity = min(max(2 ** (matches_num - 1), 1), 4)
        # animation
        self.animation = Animation(f"Image/Vehicles/{VEHICLE_TYPE.get(self.capacity)}/{self.color}", 180)
        self.image = self.animation.image
        # position
        self.rect = self.image.get_rect()
        self.set_position(row, col)
    
    def set_position(self, row, col):
        self.rect.center = (PUZZLE_X + GRID_SIZE / 2 + row * GRID_SIZE, 
                            PUZZLE_Y + GRID_SIZE / 2 + col * GRID_SIZE)

    def update(self):
        # animation
        self.animation.update()
        self.image = self.animation.image
        # move
        self.rect.x += 5
        # constraint
        if self.rect.x > SCREEN_WIDTH:
            self.kill()
