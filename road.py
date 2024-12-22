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
        pygame.draw.rect(screen, GRAY, (PUZZLE_WIDTH, PUZZLE_HEIGHT, self.width, SCREEN_HEIGHT))  # 灰色背景

        # 畫車道線
        for i in range(1, self.lane_count):
            lane_y = PUZZLE_HEIGHT + i * self.lane_width
            pygame.draw.line(screen, WHITE, (PUZZLE_WIDTH, lane_y), (SCREEN_WIDTH, lane_y), 3)  # 白色車道線