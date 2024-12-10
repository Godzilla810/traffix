import pygame
from setting import *

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        for row in range(ROW):
            for col in range(COL):
                color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
                pygame.draw.rect(screen, color, (row * GRID_SIZE, PUZZLE_HEIGHT_Y + col * GRID_SIZE, GRID_SIZE, GRID_SIZE))