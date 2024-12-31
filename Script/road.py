import pygame
from setting import *


class Road(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = SCREEN_WIDTH - PUZZLE_WIDTH  # 馬路的總寬度
        self.lane_count = COL  # 車道數量
        self.lane_width = GRID_SIZE  # 每條車道的寬度

    def draw(self, screen):
        # 畫馬路背景
        pygame.draw.rect(screen, GRAY, (PUZZLE_WIDTH, PUZZLE_Y, self.width, SCREEN_HEIGHT))  # 灰色背景

        # 畫虛線車道線
        dash_length = 40  # 每段虛線的長度
        gap_length = 20    # 每段虛線之間的間隔
        for i in range(1, self.lane_count):
            lane_y = PUZZLE_Y + i * self.lane_width
            x_start = PUZZLE_WIDTH
            while x_start < SCREEN_WIDTH:
                x_end = min(x_start + dash_length, SCREEN_WIDTH)
                pygame.draw.line(screen, WHITE, (x_start, lane_y), (x_end, lane_y), 3)
                x_start += dash_length + gap_length