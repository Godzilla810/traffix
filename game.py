import pygame
import random
from setting import *
from gem import Gem
from background import BackGround
from board import Board
from animation import Explosion


class Game:
    def __init__(self):
        print("Game init")
        self.run = True
        self.background = BackGround("Image/background.png", 0, 0)
        self.board = Board()

    def update(self):
        self.board.update()
        pass

    def draw(self, surface):
        self.background.draw(surface)
        self.board.draw(surface)


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
        self.run = False
        self.wait = True
        pass


    def reset(self):
        self.__init__()
        pass

