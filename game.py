import pygame
from setting import *
from board import Board
from road import Road
from bar import Progress, HpBar
from gem_manager import GemManager
from car_generator import CarGenerator
from enemy_generator import EnemyGenerator

class Game():
    def __init__(self, level):
        self.level = level
        self.game_over = False
        self.game_pass = False
        
        self.start_time = pygame.time.get_ticks()
        self.time = self.level * 10000
        self.hp = max(self.level, 5)
        self.score = 0

        self.road = Road()
        self.board = Board()
        
        self.progress = Progress(self.time)
        self.hp_bar = HpBar(self.hp)

        self.gem_group = pygame.sprite.Group()
        self.car_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        self.gem_manager = GemManager(self.gem_group)
        self.car_generator = CarGenerator(self.car_group)
        self.enemy_generator = EnemyGenerator(self.time, max(1500 - self.level * 100, 500), self.enemy_group)

        self.can_process = False
        self.is_waiting = False
        self.wait_time = 0
        self.wait_delay = 800

    def update(self):
        self.progress.update(self.time - pygame.time.get_ticks() + self.start_time)

        self.gem_group.update()
        self.car_group.update()
        self.enemy_group.update()

        self.enemy_generator.update()

        self.check_for_state()
        self.check_for_collisions()
        self.check_input()
        self.try_process_matches()

    # 檢查遊戲狀態
    def check_for_state(self):
        if self.hp <= 0:
            self.game_over = True
        elif pygame.time.get_ticks() - self.start_time >= self.time and len(self.enemy_group) == 0:
            self.game_pass = True

    # 檢查碰撞
    def check_for_collisions(self):
        # 檢查敵人是否與車子相撞
        for enemy in self.enemy_group:
            for car in self.car_group:
                if pygame.sprite.collide_rect(enemy, car) and car.color == enemy.color:
                    self.score += 1
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
                self.can_process = True

    # 需要時處理配對
    def try_process_matches(self):
        if not self.can_process:
            return
        if self.is_waiting:
            self.count_down()
            return
        matches = self.gem_manager.check_matches()
        if not matches:
            self.can_process = False
            return
        self.gem_manager.process_matches(matches)
        self.car_generator.generate_car(matches)
        self.is_waiting = True
        self.wait_time = pygame.time.get_ticks()
    
    # 等待生成珠子與車子的動畫
    def count_down(self):
        now = pygame.time.get_ticks()
        if now - self.wait_time > self.wait_delay:
            self.is_waiting = False

            
    def draw(self, screen):
        self.road.draw(screen)
        self.board.draw(screen)

        self.gem_group.draw(screen)
        self.car_group.draw(screen)
        self.enemy_group.draw(screen)

        self.progress.draw(screen)
        self.hp_bar.draw(screen)