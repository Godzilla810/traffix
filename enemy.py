import pygame
from sprite_sheet import SpriteSheet
from setting import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, col):
        super().__init__()
        self.col = col
        self.sprite_sheet = pygame.image.load(f"Image/People/Blue/blue_walk_WEST-Sheet.png").convert_alpha()
        self.animation = SpriteSheet.extract_images(self.sprite_sheet, ENEMY_SPRITE_COUNT)
        self.frame = 0
        self.animation_time = 0
        self.animation_delay = 50
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.set_pos()

    def set_pos(self):
        self.rect.center = (SCREEN_WIDTH, 
                            GRID_SIZE / 2 +  PUZZLE_HEIGHT + self.col * GRID_SIZE)

    def update(self):
        self.rect.x -= 2
        if self.rect.x < PUZZLE_WIDTH:
            self.kill()

        now = pygame.time.get_ticks()
        if now - self.animation_time > self.animation_delay:
            self.frame += 1
            self.animation_time = pygame.time.get_ticks()
            self.image = self.animation[self.frame % len(self.animation)]      
