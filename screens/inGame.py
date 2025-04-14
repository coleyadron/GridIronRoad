import pygame
# import json
import random
import gridironRoad
from minigames import puntReturn, fieldGoal

def killgame():
    pygame.quit()
    quit()

def miniGameHandler(screen):
    # #pick random mini-game
    miniGames = [puntReturn, fieldGoal]
    miniGame = random.choice(miniGames)
    print("Selected mini-game: ", miniGame.__name__)
    # #start mini-game
    miniGame.exec(screen)

def inGame(screen, matchup, scenarios):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    screen.fill((0, 0, 0))

    print("Game is starting")

    preText = "Welcome to week " + str(matchup["week"]) + " vs " + matchup["opponent"] + "!"
    pregameText = font.render(preText, True, (255, 255, 255))
    screen.blit(pregameText, (screen.get_width() / 2 - pregameText.get_width() / 2, 50))

    bottomText = font.render("Press ENTER to start the game", True, (255, 255, 255))
    screen.blit(bottomText, (screen.get_width() / 2 - bottomText.get_width() / 2, screen.get_height() - 100))
    pygame.display.update()

    for scenario in scenarios:
        print(scenario["description"])

    inGame = True
    while inGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("ENTER action, start game")
                    # inGame = False
                    miniGameHandler(screen)
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE action, quitting game")
                    gridironRoad.killgame(screen)

    