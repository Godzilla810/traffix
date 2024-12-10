import eventmanager
import model
import view
import controller

def run():
    evManager = eventmanager.EventManager()
    gamemodel = model.GameEngine(evManager)
    playerInput = controller.PlayerInput(evManager, gamemodel)
    gameView = view.GameView(evManager, gamemodel)
    gamemodel.run()

if __name__ == '__main__':
    run()
