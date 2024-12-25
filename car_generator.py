import pygame
from collections import Counter
from setting import *
from car import Car

class CarGenerator():
    def __init__(self, car_group : pygame.sprite.Group):
        self.car_group = car_group

    def generate_car(self, matches : Counter):
        for row, col, color in matches:
            self.car_group.add(Car(row, col, color, matches[row, col, color]))