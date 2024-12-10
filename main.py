import pygame
import sys
from setting import *
from game import Game


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffix")

clock = pygame.time.Clock()


game = Game()

running = True


while running:
    # Checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.select_gem(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            game.selected_gem = None
        elif event.type == pygame.MOUSEMOTION and game.selected_gem:
            game.drag_gem(event.pos)

    # Update
    if game.run:
        game.update()

    # Drawing
    if game.run or game.wait:
        game.draw(screen)
    

    pygame.display.update()
    clock.tick(FPS)
