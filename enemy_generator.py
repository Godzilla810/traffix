import random
import pygame
from setting import *
from enemy import Enemy

class EnemyGenerator():
    def __init__(self, total_generate_time : int, generate_delay : int, enemy_speed : int, enemy_group : pygame.sprite.Group):
        self.start_time = pygame.time.get_ticks()
        self.total_generate_time = total_generate_time
        self.generate_delay = generate_delay
        self.generate_time = 0
        self.generate_count = 0
        self.enemy_speed = enemy_speed
        self.enemy_group = enemy_group

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.start_time >= self.total_generate_time:
            return
        # 如果產生了很多敵人，會停頓比較久
        elif now - self.generate_time > self.generate_delay * self.generate_count:
            self.generate_time = now
            self.generate_count = random.randint(1, COL)
            self.generate_enemy(self.generate_count)

    def generate_enemy(self, count):
        start_col = random.randint(0, COL-count)
        color = random.choice(COLOR_LIST)
        for _ in range(count):
            self.enemy_group.add(Enemy(start_col, color, self.enemy_speed))
            start_col += 1