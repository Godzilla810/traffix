import pygame
import random
from setting import *
from gem import Gem
from board import Board

class Puzzle():
    def __init__(self):
        self.board = Board()
        self.gem_group = pygame.sprite.Group()
        self.selected_gem = None

        for i in range(ROW):
            for j in range(COL):
                gem = Gem(i, j, random.choice(COLOR_LIST))
                self.gem_group.add(gem)

    def update(self):
        self.gem_group.update()
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

    
    def draw(self, screen):
        self.board.draw(screen)
        self.gem_group.draw(screen)