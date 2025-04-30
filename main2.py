import pygame
from minigames import puntReturn
from minigames import runPlay

def main():
    pygame.init()
    pygame.display.init()

    # Set up the game screen
    screen = pygame.display.set_mode((1400, 1050))
    pygame.display.set_caption("mini game test")

    # Create an instance of the PuntReturn class
    minigame = puntReturn.exec(screen)

    print(minigame)

if __name__ == "__main__":
    main()
