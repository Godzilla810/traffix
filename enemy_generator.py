import random
import pygame
from setting import *
from enemy import Enemy

class EnemyGenerator():
    def __init__(self, total_generate_time : int, generate_delay : int, enemy_group : pygame.sprite.Group):
        self.start_time = pygame.time.get_ticks()
        self.total_generate_time = total_generate_time
        self.generate_time = 0
        self.generate_delay = generate_delay
        self.enemy_group = enemy_group

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.start_time >= self.total_generate_time:
            return
        elif now - self.generate_time > self.generate_delay:
            self.generate_time = now
            self.generate_enemy()

    def generate_enemy(self):
        self.enemy_group.add(Enemy(random.randint(0, COL-1)))