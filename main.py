import pygame
import sys
from setting import *
from game_manager import GameManager


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffix")

clock = pygame.time.Clock()


game_manager = GameManager(1)

running = True


while running:
    # Checking for events
    # 這裡要改成peek，不然會跟主邏輯衝突
    if pygame.event.peek(pygame.QUIT):
        pygame.quit()
        sys.exit()
        running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        print("restart")
    if keys[pygame.K_r] and game_manager.game_over == True:
        game_manager.reset(1)
    if keys[pygame.K_n] and game_manager.game_pass == True:
        game_manager.reset(game_manager.level + 1)

    # Update
    if game_manager.run:
        game_manager.update()

    # Drawing
    if game_manager.run or game_manager.wait:
        game_manager.draw(screen)
    

    pygame.display.update()
    clock.tick(FPS)
