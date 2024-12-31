import pygame
from collections import Counter
from setting import *
from car import Car

class CarGenerator():
    def __init__(self, car_group : pygame.sprite.Group):
        self.car_group = car_group
        # sound
        self.sound = pygame.mixer.Sound("../Sound/Effect/車のエンジンをかける1.mp3")

    def generate_car(self, matches : Counter):
        # 避免聲音疊加
        pygame.mixer.stop()
        self.sound.play()
        for row, col, color in matches:
            self.car_group.add(Car(row, col, color, matches[row, col, color]))