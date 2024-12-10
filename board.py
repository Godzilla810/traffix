import pygame
import random
from setting import *
from gem import Gem

class Board(pygame.sprite.Sprite):
    def __init__(self):
        self.grid = [[0 for _ in range(COL)] for _ in range(ROW)]
        self.gem_group = pygame.sprite.Group()
        self.selected_gem = None

        for i in range(ROW):
            for j in range(COL):
                gem = Gem(i, j, random.choice(COLOR_LIST))
                self.gem_group.add(gem)
                self.grid[i][j] = gem

    def update(self):
        self.gem_group.update()
        self.check_input()
        if (self.selected_gem != None):
            print(self.selected_gem.color_name)
            

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.select_gem(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.selected_gem = None
            elif event.type == pygame.MOUSEMOTION and self.selected_gem:
                self.drag_gem(event.pos)

    def select_gem(self, pos):
        for gem in self.gem_group:
            if gem.rect.collidepoint(pos):
                self.selected_gem = gem
                Gem.vacant_row = gem.row
                Gem.vacant_col = gem.col
                break

    def drag_gem(self, pos):
        self.selected_gem.rect.center = pos
    
    def draw(self, screen):
        for row in range(ROW):
            for col in range(COL):
                color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
                pygame.draw.rect(screen, color, (row * GRID_SIZE, SCREEN_HEIGHT_BOARD + col * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        self.gem_group.draw(screen)