import pygame
from minigames import puntReturn

def main():
    pygame.init()
    pygame.display.init()

    # Set up the game screen
    screen = pygame.display.set_mode((1400, 1050))
    pygame.display.set_caption("Punt Return Game")

    # Create an instance of the PuntReturn class
    punt_return_game = puntReturn.exec(screen)

    print(punt_return_game)

if __name__ == "__main__":
    main()
