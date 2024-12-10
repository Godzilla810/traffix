import pygame
import model
from eventmanager import *

class PlayerInput(object):
    """
    Handles keyboard input.
    """

    def __init__(self, evManager, model):
        """
        evManager (EventManager): Allows posting messages to the event queue.
        model (GameEngine): a strong reference to the game Model.
        """
        self.evManager = evManager
        evManager.RegisterListener(self)
        self.model = model

    def notify(self, event):
        """
        Receive events posted to the message queue. 
        """

        if isinstance(event, TickEvent):
            # Called for each game tick. We check our keyboard presses here.
            for event in pygame.event.get():
                # handle window manager closing our window
                if event.type == pygame.QUIT:
                    self.evManager.Post(QuitEvent())
                # handle key down events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.evManager.Post(QuitEvent())
                    else:
                        # post any other keys to the message queue for everyone else to see
                        self.evManager.Post(InputEvent(event.unicode, None))

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    game.select_gem(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    game.selected_gem = None
                elif event.type == pygame.MOUSEMOTION and game.selected_gem:
                    game.drag_gem(event.pos)

                    
