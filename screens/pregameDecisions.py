import pygame
import json
import random

def killgame():
    pygame.quit()
    quit()

def preGameDecisions(screen):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    pregameText = font.render("Welcome to Gridiron Road!", True, (255, 255, 255))
    screen.blit(pregameText, (screen.get_width() / 2 - pregameText.get_width() / 2, 0))

    pygame.display.update()


    decisionMaking = True
    while decisionMaking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                killgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Starting new game")
                    decisionMaking = False
                if event.key == pygame.K_ESCAPE:
                    print("Loading game")
                    decisionMaking = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1050))
    preGameDecisions(screen)

if __name__ == "__main__":
    main()    