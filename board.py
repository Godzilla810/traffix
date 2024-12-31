import pygame
from setting import *

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, PUZZLE_Y, PUZZLE_WIDTH, PUZZLE_HEIGHT)

    def draw(self, screen):
        for row in range(ROW):
            for col in range(COL):
                color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
                pygame.draw.rect(screen, color, (row * GRID_SIZE, PUZZLE_Y + col * GRID_SIZE, GRID_SIZE, GRID_SIZE))