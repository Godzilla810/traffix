import pygame
from enum import Enum, auto
from background import BackGround
from setting import *
from game import Game

# 定義遊戲狀態
class State(Enum):
    MENU = auto()
    GAME = auto()

class GameManager:
    def __init__(self):
        self.wait = False
        self.run = True
        self.level = 1
        self.score = 0
        self.state = State.MENU
        self.start_page = BackGround("Image/background.jpg")
        self.game = None

    def start_game(self, level = 1):
        self.wait = False
        self.run = True
        self.level = level
        self.game = Game(level)

    def update(self):
        if self.state == State.MENU:
            return
        self.game.update()
        self.check_for_state()
        pass

    def check_for_state(self):
        if (self.game.game_pass == True or self.game.game_over == True):
            self.score += self.game.score
            self.run = False
            self.wait = True
        pass

    def draw(self, surface):
        if self.state == State.MENU:
            self.start_page.draw(surface)
            self.draw_text(surface, "Press S to Start", 24, WHITE, True, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
            return
        
        self.game.draw(surface)
        self.draw_text(surface, f"LEVEL{self.level}", 24, WHITE, False, SCREEN_WIDTH - 50, 20)

        if (self.game.game_over == True):
            self.draw_text(surface, "GAME OVER!!", 40, WHITE, True, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 85)
            self.draw_text(surface, f"YOUR SCORE:{self.score}", 28, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 10)
            self.draw_text(surface, "Press R to Restart", 24, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)
        
        if (self.game.game_pass == True):
            self.draw_text(surface, f"LEVEL{self.level}  PASS!!", 40, WHITE, True, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 80)
            self.draw_text(surface, "Press N to Next Level", 24, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 25)


    def draw_text(self, surface, text, size, color, bold, x, y):
        font = pygame.font.Font("Font/BoutiqueBitmap9x9_Bold_1.9.ttf", size=size)
        text_surface = font.render(text, bold, color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surface.blit(text_surface, text_rect)


