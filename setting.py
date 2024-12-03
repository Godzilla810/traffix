import pygame

FPS = 60

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 800

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

LIVES_ICON = pygame.image.load("Image/spaceship.png")
LIVES_ICON = pygame.transform.scale(LIVES_ICON, (50, 35))

ROW = 5
COLUMN = 4
COLOR_LIST = ["black", "blue", "green", "orange", "purple", "red", "white", "yellow"]
