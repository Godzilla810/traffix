import pygame
from animation import Animation
from setting import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, col):
        super().__init__()
        self.animation = Animation(pygame.image.load(f"Image/People/Red/red_walk_WEST-Sheet.png").convert_alpha(), ENEMY_SPRITE_COUNT, 50)
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
