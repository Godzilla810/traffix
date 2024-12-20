import pygame
from setting import *


class BackGround():
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, PUZZLE_HEIGHT_Y))
        
    
    def draw(self, screen):
        screen.blit(self.image, (0, 0))
