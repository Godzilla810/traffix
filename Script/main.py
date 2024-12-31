import pygame
import sys
from setting import *
from game_manager import *


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Traffix")

cursor_image = pygame.image.load("../Image/drag.png").convert_alpha()
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

game_manager = GameManager()

running = True


while running:
    # Checking for events
    # 這裡要改成peek，不然會跟主邏輯衝突
    if pygame.event.peek(pygame.QUIT):
        pygame.mixer.quit()
        pygame.quit()
        sys.exit()
        running = False

    keys = pygame.key.get_pressed()
    if any(keys):
        match game_manager.state:
            case State.MENU:
                game_manager.start_game()
                game_manager.state = State.IN_GAME
            case State.GAME_PASS:
                game_manager.start_game(game_manager.level + 1)
                game_manager.state = State.IN_GAME
            case State.GAME_OVER:
                game_manager.restart_game()
                game_manager.state = State.IN_GAME

    game_manager.update()
    game_manager.draw(screen)
    
    screen.blit(cursor_image, pygame.mouse.get_pos())
    pygame.display.update()
    clock.tick(FPS)
