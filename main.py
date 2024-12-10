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
    # 這裡要改成peek，不然會跟主邏輯衝突
    if pygame.event.peek(pygame.QUIT):
        pygame.quit()
        sys.exit()
        running = False

    # Update
    if game.run:
        game.update()

    # Drawing
    if game.run or game.wait:
        game.draw(screen)
    

    pygame.display.update()
    clock.tick(FPS)
