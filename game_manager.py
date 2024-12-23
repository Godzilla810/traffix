import pygame
from setting import *
from game import Game

class GameManager:
    def __init__(self, level):
        self.game_over = False
        self.game_pass = False
        self.wait = False
        self.run = True
        self.level = level
        self.background = pygame.image.load("Image/background_1_lower.jpg")
        self.game = Game(self.level * 10, max(1500 - self.level * 250, 250))

    def update(self):
        self.game.update()
        self.check_for_state()
        pass

    def draw(self, surface):
        self.game.draw(surface)

        if (self.game_over == True):
            self.draw_text(surface, "GAME OVER!!", 40, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75)
            self.draw_text(surface, "Press R to Restart", 24, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 25)
        
        if (self.game_pass == True):
            self.draw_text(surface, f"LEVEL {self.level} PASS!!", 40, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75)
            self.draw_text(surface, "Press N to Next Level", 24, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 25)


    def draw_text(self, surface, text, size, color, bold, x, y):
        font = pygame.font.Font("Font/BoutiqueBitmap9x9_Bold_1.9.ttf", size=size)
        text_surface = font.render(text, bold, color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surface.blit(text_surface, text_rect)

    def check_for_state(self):
        if (self.game.hp == 0):
            self.game_over = True
            self.run = False
            self.wait = True
        if (self.game.game_pass == True):
            self.game_pass = True
            self.run = False
            self.wait = True
        pass


    def reset(self, level):
        self.__init__(level)
        pass

