import pygame
import random
from typing import Optional
from collections import Counter
from setting import *
from gem import Gem

class Tile:
    def __init__(self, row : int, col : int):
        self.row = row
        self.col = col

class GemManager():
    def __init__(self, gem_group : pygame.sprite.Group):
        self.grid : list[list[Optional[Gem]]] = [[None for _ in range(COL)] for _ in range(ROW)]
        self.tile : Tile = None
        self.gem_group : pygame.sprite.Group = gem_group
        self.initialize_grid()

    def initialize_grid(self):
        while True:
            self.gem_group.empty()
            for i in range(ROW):
                for j in range(COL):
                    gem = Gem(i, j, random.choice(COLOR_LIST))
                    self.grid[i][j] = gem
                    self.gem_group.add(gem)
            if not self.check_matches():
                break

    def drag_start(self, pos):
        if not self.in_range(pos):
            return
        self.tile = Tile(pos[0] // GRID_SIZE, pos[1] // GRID_SIZE)
    
    def dragging(self, pos):
        # 拖曳珠子
        if not self.tile and not self.in_range(pos):
            return
        target_tile = Tile(pos[0] // GRID_SIZE, pos[1] // GRID_SIZE)
        # 讓選取的珠子跟著移動
        self.grid[self.tile.row][self.tile.col].rect.center = pos

        if (self.tile != target_tile and self.is_adjacent(self.tile, target_tile)):
            # 交換位置
            self.grid[target_tile.row][target_tile.col].set_position(self.tile.row, self.tile.col)
            self.swap_tile(self.tile, target_tile)
            self.tile = target_tile

    def drag_end(self):
        # 釋放珠子
        if not self.tile:
            return
        self.grid[self.tile.row][self.tile.col].set_position(self.tile.row, self.tile.col)
        self.tile = None

    def in_range(self, pos):
        return pos[0] // GRID_SIZE in range(ROW) and pos[1] // GRID_SIZE in range(COL)

    def swap_tile(self, tileA : Tile, tileB : Tile):
        self.grid[tileA.row][tileA.col], self.grid[tileB.row][tileB.col] = self.grid[tileB.row][tileB.col], self.grid[tileA.row][tileA.col]

    def is_adjacent(self, tileA : Tile, tileB : Tile):
        return abs(tileA.row - tileB.row) + abs(tileA.col - tileB.col) == 1
    
    def process_matches(self, matches):
        self.remove_matches(matches)
        self.refill_grid(matches)

    def check_matches(self):
        matches = Counter()
        for row in range(ROW):
            for col in range(COL - 2):
                if self.grid[row][col] and self.grid[row][col].color == self.grid[row][col+1].color == self.grid[row][col+2].color:
                    color = self.grid[row][col].color
                    matches.update([(row, col, color), (row, col+1, color), (row, col+2, color)])
        for col in range(COL):
            for row in range(ROW - 2):
                if self.grid[row][col] and self.grid[row][col].color == self.grid[row+1][col].color == self.grid[row+2][col].color:
                    color = self.grid[row][col].color
                    matches.update([(row, col, color), (row+1, col, color), (row+2, col, color)])
        return matches

    def remove_matches(self, matches):
        for row, col, _ in matches:
            self.grid[row][col].kill()

    def refill_grid(self, matches):
        for row, col, _ in matches:
            gem = Gem(row, col, random.choice(COLOR_LIST))
            self.grid[row][col] = gem
            self.gem_group.add(gem)