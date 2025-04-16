import pygame
# import json
import random
import gridironRoad
from minigames import puntReturn, fieldGoal
from logic import probEngine
import time

TEAM_SCORE = 0
OPPONENT_SCORE = 0
QUARTER = 1

WEEK = None

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

def handleEndGame(screen, gameResult):
    global OPPOSING_TEAM, TEAM_SCORE, OPPONENT_SCORE, MY_TEAM

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    screen.fill((0, 0, 0))

    if gameResult == "win":
        endText = "You beat the %s! Final score: %s - %s" % (OPPOSING_TEAM, TEAM_SCORE, OPPONENT_SCORE)
    elif gameResult == "loss":
        endText = "You lost to the %s! Final score: %s - %s" % (OPPOSING_TEAM, TEAM_SCORE, OPPONENT_SCORE)
    elif gameResult == "tie":
        endText = "You tied with the %s. Final score: %s - %s" % (OPPOSING_TEAM, TEAM_SCORE, OPPONENT_SCORE)

    endGameText = font.render(endText, True, (255, 255, 255))
    screen.blit(endGameText, (screen.get_width() / 2 - endGameText.get_width() / 2, screen.get_height() / 2))

    bottomText = font.render("Press ENTER to exit", True, (255, 255, 255))
    screen.blit(bottomText, (screen.get_width() / 2 - bottomText.get_width() / 2, screen.get_height() - 100))

    pygame.display.update()
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             gridironRoad.killgame(screen)
    #             running = False
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_RETURN:
    #                 running = False
    #                 return {
    #                     "score": TEAM_SCORE,
    #                     "opponent_score": OPPONENT_SCORE,
    #                     "game_result": gameResult
    #                 }
    #             if event.key == pygame.K_ESCAPE:
    #                 gridironRoad.killgame(screen)
    #                 running = False

def handleTeamGlobals():
    global OPPOSING_TEAM, OPPOSING_OVERALL, OPPOSING_OFFENSE, OPPOSING_DEFENSE, OPPOSING_SPECIAL
    global MY_TEAM, MY_OVERALL, MY_OFFENSE, MY_DEFENSE, MY_SPECIAL

    opponent = gridironRoad.getOpponent("Pittsburgh Steelers")

    OPPOSING_TEAM = opponent['name']
    OPPOSING_OVERALL = opponent["overall"]
    OPPOSING_OFFENSE = opponent["offense"]
    OPPOSING_DEFENSE = opponent["defense"]
    OPPOSING_SPECIAL = opponent["special_teams"]

    # print("Opponent team: ", OPPOSING_TEAM)
    # print("Opponent overall: ", OPPOSING_OVERALL)
    # print("Opponent offense: ", OPPOSING_OFFENSE)
    # print("Opponent defense: ", OPPOSING_DEFENSE)
    # print("Opponent special teams: ", OPPOSING_SPECIAL)

    my_team_overalls = gridironRoad.calculateTeamOverall()

    MY_TEAM = my_team_overalls["name"]
    MY_OVERALL = my_team_overalls["overall"]
    MY_OFFENSE = my_team_overalls["offense"]
    MY_DEFENSE = my_team_overalls["defense"]
    MY_SPECIAL = my_team_overalls["special_teams"]

    # print("My team: ", MY_TEAM)
    # print("My overall: ", MY_OVERALL)
    # print("My offense: ", MY_OFFENSE)
    # print("My defense: ", MY_DEFENSE)
    # print("My special teams: ", MY_SPECIAL)

def updateScoreboard(screen):
    global TEAM_SCORE, OPPONENT_SCORE, QUARTER, OPPOSING_TEAM, WEEK

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    screen.fill((0, 0, 0))

    preText = "Welcome to week " + str(WEEK) + " vs " + OPPOSING_TEAM + "!"
    pregameText = font.render(preText, True, (255, 255, 255))
    screen.blit(pregameText, (screen.get_width() / 2 - pregameText.get_width() / 2, 50))

    # bottomText = font.render("Press ENTER to start the game", True, (255, 255, 255))
    # screen.blit(bottomText, (screen.get_width() / 2 - bottomText.get_width() / 2, screen.get_height() - 100))

    quaterScoreText = "Quarter: %s" % QUARTER
    teamScoreboardText = "%s: %s" % (MY_TEAM, TEAM_SCORE)
    opponentScoreboardText = "%s: %s" % (OPPOSING_TEAM, OPPONENT_SCORE)

    quarterText = font.render(quaterScoreText, True, (255, 255, 255))
    teamScoreText = font.render(teamScoreboardText, True, (255, 255, 255))
    opponentScoreText = font.render(opponentScoreboardText, True, (255, 255, 255))

    y_offset = screen.get_height() / 2 - 50

    screen.blit(quarterText, (screen.get_width() / 2 - quarterText.get_width() / 2, y_offset))
    y_offset += 50
    screen.blit(teamScoreText, (screen.get_width() / 2 - teamScoreText.get_width() / 2, y_offset))
    y_offset += 50
    screen.blit(opponentScoreText, (screen.get_width() / 2 - opponentScoreText.get_width() / 2, y_offset))

    pygame.display.update()

    time.sleep(1)

def miniGameHandler(screen):
    global QUARTER, OPPONENT_SCORE, TEAM_SCORE
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
    if QUARTER < 5:
        #call probEngine with result of drive
        OPPONENT_SCORE += 7
        TEAM_SCORE += 3
        updateScoreboard(screen)
    else:
        #game is over
        gameResult = False
        if OPPONENT_SCORE > TEAM_SCORE:
            print("You lost the game")
            gameResult = "loss"
        elif OPPONENT_SCORE == TEAM_SCORE:
            print("You tied the game")
            gameResult = "tie"
        else:
            print("You won the game")
            gameResult = "win"

        handleEndGame(screen, gameResult)       

    pygame.display.update()



def inGame(screen, matchup, scenarios):
    global WEEK, TEAM_SCORE, OPPONENT_SCORE, QUARTER

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    screen.fill((0, 0, 0))

    print("Game is starting")

    WEEK = matchup["week"]

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

    handleTeamGlobals()

    inGame = True
    gameOver = False
    while inGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and QUARTER < 5 and not gameOver:
                    print("ENTER action, start game")
                    # inGame = False
                    while QUARTER < 5:
                        miniGameHandler(screen)
                    gameOver = True
                elif event.key == pygame.K_RETURN and QUARTER >= 5 and gameOver:
                    print("ENTER action, game over")

                    game_result = "loss" if OPPONENT_SCORE > TEAM_SCORE else "win" if OPPONENT_SCORE < TEAM_SCORE else "tie"

                    return {
                        "score": TEAM_SCORE,
                        "opponent_score": OPPONENT_SCORE,
                        "game_result": game_result
                    }
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE action, quitting game")
                    gridironRoad.killgame(screen)

    