import pygame
from setting import *

class Bar():
    def __init__(self, x, y, width, height, base_color, bar_color, current_num, total_num):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.base_color = base_color
        self.bar_color = bar_color
        self.current_num = current_num
        self.total_num = total_num

    def update(self, num):
        if (num <= self.total_num):
            self.current_num = num
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.base_color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(surface, self.bar_color, (self.x, self.y, self.width * self.current_num / self.total_num, self.height), 0)
        pass

class Progress(Bar):
    def __init__(self, time, total_time):
        x = PUZZLE_WIDTH
        y = 0
        width = ROAD_WIDTH
        height = BAR_HRIGHT
        base_color = WHITE
        bar_color = GREEN
        super().__init__(x, y, width, height, base_color, bar_color, time, total_time)

class HpBar(Bar):
    def __init__(self, hp, total_hp):
        x = 0
        y = 0
        width = PUZZLE_WIDTH
        height = BAR_HRIGHT
        base_color = BLACK
        bar_color = RED
        super().__init__(x, y, width, height, base_color, bar_color, hp, total_hp)