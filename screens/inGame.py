import pygame
# import json
import random
import gridironRoad
from minigames import puntReturn, fieldGoal
from logic import probEngine

TEAM_SCORE = 0
OPPONENT_SCORE = 0
QUARTER = 1

OPPOSING_TEAM = None
OPPOSING_OVERALL = None
OPPOSING_OFFENSE = None
OPPOSING_DEFENSE = None
OPPOSING_SPECIAL = None

MY_TEAM = None
MY_OVERALL = None
MY_OFFENSE = None
MY_DEFENSE = None
MY_SPECIAL = None

def killgame():
    pygame.quit()
    quit()

def handleTeamGlobals(matchup):
    global OPPOSING_TEAM, OPPOSING_OVERALL, OPPOSING_OFFENSE, OPPOSING_DEFENSE, OPPOSING_SPECIAL
    global MY_TEAM, MY_OVERALL, MY_OFFENSE, MY_DEFENSE, MY_SPECIAL

    opponent = gridironRoad.getOpponent("Pittsburgh Steelers")

    OPPOSING_TEAM = opponent
    OPPOSING_OVERALL = opponent["overall"]
    OPPOSING_OFFENSE = opponent["offense"]
    OPPOSING_DEFENSE = opponent["defense"]
    OPPOSING_SPECIAL = opponent["special_teams"]

    print("Opponent team: ", OPPOSING_TEAM)
    print("Opponent overall: ", OPPOSING_OVERALL)
    print("Opponent offense: ", OPPOSING_OFFENSE)
    print("Opponent defense: ", OPPOSING_DEFENSE)
    print("Opponent special teams: ", OPPOSING_SPECIAL)

    my_team_overalls = gridironRoad.calculateTeamOverall()

    MY_TEAM = my_team_overalls["name"]
    MY_OVERALL = my_team_overalls["overall"]
    MY_OFFENSE = my_team_overalls["offense"]
    MY_DEFENSE = my_team_overalls["defense"]
    MY_SPECIAL = my_team_overalls["special_teams"]

    print("My team: ", MY_TEAM)
    print("My overall: ", MY_OVERALL)
    print("My offense: ", MY_OFFENSE)
    print("My defense: ", MY_DEFENSE)
    print("My special teams: ", MY_SPECIAL)

def miniGameHandler(screen):
    global QUARTER
    #pick random mini-game
    miniGames = [puntReturn]
    miniGame = random.choice(miniGames)
    print("Selected mini-game: ", miniGame.__name__)

    pregame_Copy = screen.copy()

    # #start mini-game
    gameResult = miniGame.exec(screen)
    print("Game result: ", gameResult)
    QUARTER += 1

    screen.blit(pregame_Copy, (0, 0))

    #call the prob engine with the outcome of the mini-game
    if QUARTER < 6:
        #call probEngine with result of drive
        pass
    else:
        #game is over
        pass

    pygame.display.update()



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

    moraleTotal = 0
    performanceTotal = 0
    for scenario in scenarios:
        moraleTotal += scenario["effect"]["morale"]
        performanceTotal += scenario["effect"]["performance"]

    print("Morale total: ", moraleTotal)
    print("Performance total: ", performanceTotal)

    handleTeamGlobals(matchup)

    inGame = True
    while inGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and QUARTER < 5:
                    print("ENTER action, start game")
                    # inGame = False
                    miniGameHandler(screen)
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE action, quitting game")
                    gridironRoad.killgame(screen)

    