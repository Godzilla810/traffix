import pygame
from enum import Enum, auto
from background import BackGround
from setting import *
from game import Game

# 定義遊戲狀態
class State(Enum):
    MENU = auto()
    IN_GAME = auto()
    GAME_PASS = auto()
    GAME_OVER = auto()


class GameManager:
    def __init__(self):
        self.state : State = State.MENU
        self.level = 1
        self.score = 0
        self.background = BackGround("Image/background.jpg")
        self.game = None
        self.play_bgm()
    
    def play_bgm(self):
        pygame.mixer.music.load("Sound/BGM/Run-Amok(chosic.com).mp3")
        pygame.mixer.music.play(-1)

    def restart_game(self):
        self.score = 0
        self.play_bgm()
        self.start_game()

    def start_game(self, level = 1):
        self.level = level
        self.game = Game(self.level)

    def update(self):
        match self.state:
            case State.MENU:
                return
            case State.IN_GAME:
                self.game.update()
                self.check_for_state()
                return
        pass

    def check_for_state(self):
        if (self.game.game_pass == True):
            # 停止音效
            self.score += self.game.score
            pygame.mixer.stop()
            self.state = State.GAME_PASS
        elif (self.game.game_over == True):
            # 關掉所有聲音
            self.score += self.game.score
            pygame.mixer.stop()
            pygame.mixer.music.stop()
            self.state = State.GAME_OVER
        pass

    def draw(self, surface):
        match self.state:
            case State.MENU:
                self.background.draw(surface)
                self.draw_text(surface, "Press Any Key", 24, WHITE, True, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
                return
            case State.IN_GAME:
                self.game.draw(surface)
                self.draw_text(surface, f"LEVEL{self.level}", 24, WHITE, False, SCREEN_WIDTH - 50, 20)
                return
            case State.GAME_PASS:
                self.game.draw(surface)
                self.draw_text(surface, f"LEVEL{self.level}  PASS!!", 40, WHITE, True, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 80)
                self.draw_text(surface, "Press Any Key to Next Level", 24, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 25)
                return
            case State.GAME_OVER:
                self.game.draw(surface)
                self.draw_text(surface, "GAME OVER!!", 40, WHITE, True, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 85)
                self.draw_text(surface, f"YOUR SCORE: {self.score}", 28, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 10)
                self.draw_text(surface, "Press Any Key to Restart", 24, WHITE, False, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)
                return

    def draw_text(self, surface, text, size, color, bold, x, y):
        font = pygame.font.Font("Font/BoutiqueBitmap9x9_Bold_1.9.ttf", size=size)
        text_surface = font.render(text, bold, color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surface.blit(text_surface, text_rect)


