import pygame
from animation import Animation
from setting import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, col, color : str, speed : int):
        super().__init__()
        # attribute
        self.color = color
        # animation
        self.animation = Animation(f"Image/Enemies/{self.color}.png", 80, 8)
        self.image = self.animation.image
        # position
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH
        self.rect.centery = GRID_SIZE / 2 +  PUZZLE_Y + col * GRID_SIZE

        self.speed = speed

    def update(self):
        # animation
        self.animation.update()
        self.image = self.animation.image
        # move
        self.rect.x -= self.speed
