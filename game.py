import pygame
import random
from enemy_generator import EnemyGenerator
from gem_manager import GemManager
from setting import *
from board import Board
from road import Road
from bar import *

class Game():
    def __init__(self, level):
        self.level = level
        self.game_over = False
        self.game_pass = False
        
        self.start_time = pygame.time.get_ticks()
        self.time = self.level * 10000
        self.hp = max(self.level, 5)

        self.road = Road()
        self.board = Board()
        
        self.progress = Progress(self.time)
        self.hp_bar = HpBar(self.hp)

        self.gem_group = pygame.sprite.Group()
        self.car_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        self.gem_manager = GemManager(self.gem_group)
        self.enemy_generator = EnemyGenerator(self.time, max(1500 - self.level * 250, 250), self.enemy_group)

    def update(self):
        self.progress.update(self.time - pygame.time.get_ticks() + self.start_time)

        self.gem_group.update()
        self.car_group.update()
        self.enemy_group.update()

        self.enemy_generator.update()

        self.check_for_state()
        self.check_for_collisions()
        self.check_input()

    # 檢查遊戲狀態
    def check_for_state(self):
        if self.hp == 0:
            self.game_over = True
        if pygame.time.get_ticks() - self.start_time >= self.time and len(self.enemy_group) == 0:
            self.game_pass = True

    # 檢查碰撞
    def check_for_collisions(self):
        # 檢查敵人是否與車子相撞
        for car in self.car_group:
            for enemy in self.enemy_group:
                if pygame.sprite.collide_rect(enemy, car) and car.capacity > 0:
                    enemy.kill()
                    car.capacity -= 1
                    if (car.capacity == 0):
                        car.kill()

        # 檢查敵人是否與基地相撞
        for enemy in self.enemy_group:
            if  pygame.sprite.collide_rect(enemy, self.board):
                self.hp -= 1
                self.hp_bar.update(self.hp)
                enemy.kill()

    # 檢查輸入
    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.gem_manager.drag_start(event.pos)
            elif event.type == pygame.MOUSEMOTION and self.gem_manager.tile:
                self.gem_manager.dragging(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.gem_manager.drag_end()
            
    def draw(self, screen):
        self.road.draw(screen)
        self.board.draw(screen)

        self.gem_group.draw(screen)
        self.car_group.draw(screen)
        self.enemy_group.draw(screen)

        self.progress.draw(screen)
        self.hp_bar.draw(screen)