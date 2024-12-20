import pygame
import random
from setting import *
from gem import Gem
from car import Car
from board import Board

class Puzzle():
    def __init__(self):
        self.board = Board()
        self.gem_group = pygame.sprite.Group()
        self.car_group = pygame.sprite.Group()
        self.selected_gem = None

        for i in range(ROW):
            for j in range(COL):
                gem = Gem(i, j, random.choice(COLOR_LIST))
                self.gem_group.add(gem)

    def update(self):
        self.gem_group.update()
        self.car_group.update()
        self.check_input()
            

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.select_gem(event.pos)
            elif event.type == pygame.MOUSEMOTION and self.selected_gem:
                self.drag_gem(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.release_gem()

    def select_gem(self, pos):
        for gem in self.gem_group:
            if gem.rect.collidepoint(pos):
                self.selected_gem = gem
                break

    def drag_gem(self, pos):
        # 拖曳珠子
        if not self.selected_gem:
            return
        self.selected_gem.rect.center = pos
        for gem in self.gem_group:
            if gem != self.selected_gem and gem.rect.collidepoint(pos) and self.selected_gem.is_adjacent(gem):
                self.selected_gem.swap(gem)
                gem.set_rect()
                break

    def release_gem(self):
        # 釋放珠子
        if not self.selected_gem:
            return
        self.selected_gem.set_rect()
        self.selected_gem = None
        # 將珠子轉換為 grid
        grid = [[None for _ in range(COL)] for _ in range(ROW)]
        for gem in self.gem_group:
            grid[gem.row][gem.col] = gem.color_name

        # 檢查匹配
        matches = self.check_matches(grid)
        if matches:
            self.process_matches(matches)

    def check_matches(self, grid):
        """檢查是否有三消的匹配"""
        matches = set()
        for row in range(ROW):
            for col in range(COL - 2):
                if grid[row][col] and grid[row][col] == grid[row][col+1] == grid[row][col+2]:
                    matches.update([(row, col), (row, col+1), (row, col+2)])
        for col in range(COL):
            for row in range(ROW - 2):
                if grid[row][col] and grid[row][col] == grid[row+1][col] == grid[row+2][col]:
                    matches.update([(row, col), (row+1, col), (row+2, col)])
        return matches
    
    def process_matches(self, matches):
        """處理匹配的珠子"""
        for row, col in matches:
            for gem in self.gem_group:
                if gem.row == row and gem.col == col:
                    gem.kill()
                    car = Car(row, col, 1)
                    self.car_group.add(car)

        # 重整珠子並補充
        self.refill_grid()

    def refill_grid(self):
        """補充空缺的珠子"""
        for col in range(COL):
            empty_rows = [row for row in range(ROW) if not any(gem.row == row and gem.col == col for gem in self.gem_group)]
            for empty_row in empty_rows:
                new_gem = Gem(empty_row, col, random.choice(COLOR_LIST))
                self.gem_group.add(new_gem)

    def draw(self, screen):
        self.board.draw(screen)
        self.gem_group.draw(screen)
        self.car_group.draw(screen)
        