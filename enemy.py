import pygame
from animation import Animation
from setting import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, col, color):
        super().__init__()
        self.color = color

        self.animation = Animation(f"Image/Enemies/{self.color}.png", 50, 8)
        self.image = self.animation.image

        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH
        self.rect.centery = GRID_SIZE / 2 +  PUZZLE_Y + col * GRID_SIZE

    def update(self):
        # animation
        self.animation.update()
        self.image = self.animation.image
        # move
        self.rect.x -= 2
