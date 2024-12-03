import pygame
import random
from setting import *
from gem import Gem
from background import BackGround
from animation import Explosion


class Game:
    def __init__(self):
        self.run = True
        self.background = BackGround("Image/background.png", 0, 0)
        self.gem_group = pygame.sprite.Group()
        for i in range(ROW):
            for j in range(COLUMN):
                gem = Gem(i * 75 + 50, j * 75 + 50)
                self.gem_group.add(gem)

    def update(self):
        self.gem_group.update()
        pass

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
        # (3)---判斷當生命值歸0時，發生self.game_over()的狀況---
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

