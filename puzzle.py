import pygame
import random
from setting import *
from gem import Gem
from board import Board

# 處理轉珠邏輯
class Puzzle():
    def __init__(self):
        self.board = Board()
        self.gem_group = pygame.sprite.Group()
        self.selected_gem = None
        self.grid = [[None for _ in range(COL)] for _ in range(ROW)]
        self.initialize_grid()

    def update(self):
        # 更新遊戲盤
        self.gem_group.update()
        self.check_input()

    def initialize_grid(self):
        """初始化棋盤，避免出現初始匹配的情況"""
        while True:
            for y in range(ROW):
                for x in range(COL):
                    color = random.choice(COLOR_LIST)
                    self.grid[y][x] = color
                    self.update_gem_group()
            if not self.check_matches():  # 沒有匹配則結束
                break

    def process_matches(self):
        """反覆檢查並移除三消匹配，直到沒有新的匹配"""
        while True:
            matches = self.check_matches()
            if not matches:
                break
            self.remove_matches(matches)
            self.refill_grid()

    def update_gem_group(self):
        """根據 grid 更新 gem_group"""
        self.gem_group.empty()  # 清空原有的 sprites
        for y in range(ROW):
            for x in range(COL):
                if self.grid[y][x]:  # 如果該位置有珠子
                    gem = Gem(y, x, self.grid[y][x])  # 創建新的 Gem 實例
                    self.gem_group.add(gem)

    def check_matches(self):
        """檢查是否有三消的匹配"""
        matches = set()
        for y in range(ROW):
            for x in range(COL - 2):
                if self.grid[y][x] == self.grid[y][x+1] == self.grid[y][x+2]:
                    matches.update([(x, y), (x+1, y), (x+2, y)])
        for x in range(COL):
            for y in range(ROW - 2):
                if self.grid[y][x] == self.grid[y+1][x] == self.grid[y+2][x]:
                    matches.update([(x, y), (x, y+1), (x, y+2)])
        return matches
    
    def remove_matches(self, matches):
        """移除匹配的珠子"""
        for x, y in matches:
            self.grid[y][x] = None
        self.update_gem_group()

    def refill_grid(self):
        """補充空缺的珠子"""
        for x in range(COL):
            for y in range(ROW-1, -1, -1):
                if self.grid[y][x] is None:
                    for above_y in range(y-1, -1, -1):
                        if self.grid[above_y][x]:
                            self.grid[y][x] = self.grid[above_y][x]
                            self.grid[above_y][x] = None
                            break
                    else:
                        self.grid[y][x] = random.choice(COLOR_LIST)
        self.update_gem_group()

    def swap_tiles(self, pos1, pos2):
        """交換兩個位置的珠子"""
        self.grid[pos1[1]][pos1[0]], self.grid[pos2[1]][pos2[0]] = self.grid[pos2[1]][pos2[0]], self.grid[pos1[1]][pos1[0]]

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.select_gem(event.pos)
            elif event.type == pygame.MOUSEMOTION and self.selected_gem:
                self.drag_gem(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.release_gem()
                self.process_matches()

    def select_gem(self, pos):
        # 選擇珠子
        for gem in self.gem_group:
            if gem.rect.collidepoint(pos):
                self.selected_gem = gem
                break

    def drag_gem(self, pos):
        # 拖曳珠子
        self.selected_gem.rect.center = pos
        for gem in self.gem_group:
            if gem != self.selected_gem and gem.rect.collidepoint(pos) and self.selected_gem.is_adjacent(gem):
                self.swap_tiles((self.selected_gem.col, self.selected_gem.row), (gem.col, gem.row))
                self.selected_gem.swap(gem)
                break

    def release_gem(self):
        # 釋放珠子
        self.selected_gem.set_rect()
        self.selected_gem = None

    
    def draw(self, screen):
        # 繪製遊戲盤格
        self.board.draw(screen)
        self.gem_group.draw(screen)