import pygame
import random
from setting import *
from gem import Gem
from background import BackGround
from animation import Explosion


class Game:
    def __init__(self):
        print("Game init")
        self.run = True
        self.background = BackGround("Image/background.png", 0, 0)
        self.selected_gem = None
        self.gem_group = pygame.sprite.Group()
        for i in range(ROW):
            for j in range(COLUMN):
                gem = Gem(i * SPACE + OFFSET, j * SPACE + OFFSET, random.choice(COLOR_LIST))
                self.gem_group.add(gem)

    def update(self):
        self.gem_group.update()
        if (self.selected_gem != None):
            print(self.selected_gem.color_name)
        pass

    def select_gem(self, pos):
        for gem in self.gem_group:
            if gem.rect.collidepoint(pos):
                self.selected_gem = gem
                Gem.vacant_x = gem.x
                Gem.vacant_y = gem.y
                break

    def drag_gem(self, pos):
        self.selected_gem.rect.center = pos


    def draw(self, surface):
        self.background.draw(surface)
        self.gem_group.draw(surface)


    def draw_text(self, surface, text, size, color, bold, x, y):
        font = pygame.font.Font("Font/BoutiqueBitmap9x9_Bold_1.9.ttf", size=size)
        text_surface = font.render(text, bold, color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surface.blit(text_surface, text_rect)

    def check_for_state(self):
        if (self.lives == 0):
            self.game_over()
        pass


    def game_over(self):
        # (3)---self.run、self.wait的狀態改變---
        self.run = False
        self.wait = True
        pass


    def reset(self):
        self.__init__()
        pass

