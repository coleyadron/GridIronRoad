import pygame
# import json
import random
import gridironRoad
from minigames import puntReturn, fieldGoal, runPlay, blockPass
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

MORALE_TOTAL = 0
PERFORMANCE_TOTAL = 0

preImage = pygame.image.load("assets/images/pregames.png")
postImage = pygame.image.load("assets/images/postgame.png")
scoreBoard = pygame.image.load("assets/images/scoreBoard.png")

def killgame():
    pygame.quit()
    quit()

def handleEndGame(screen, gameResult):
    global OPPOSING_TEAM, TEAM_SCORE, OPPONENT_SCORE, MY_TEAM

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    screen.fill((0, 0, 0))

    screen.blit(postImage, (0, 0))

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

def handleTeamGlobals(opponent):
    global OPPOSING_TEAM, OPPOSING_OVERALL, OPPOSING_OFFENSE, OPPOSING_DEFENSE, OPPOSING_SPECIAL
    global MY_TEAM, MY_OVERALL, MY_OFFENSE, MY_DEFENSE, MY_SPECIAL

    opponent = gridironRoad.getOpponent(opponent)

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
    bigFont = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 50)

    screen.fill((0, 0, 0))

    screen.blit(scoreBoard, (0, 0))

    quarterScoreText = ""
    match QUARTER:
        case 1:
            quarterScoreText = "1st"
        case 2:
            quarterScoreText = "2nd"
        case 3:
            quarterScoreText = "3rd"
        case 4:
            quarterScoreText = "4th"


    teamText = font.render(MY_TEAM, True, (255, 255, 255))
    opponentText = font.render(OPPOSING_TEAM.split()[-1], True, (255, 255, 255))

    teamScoreText = bigFont.render(str(TEAM_SCORE), True, (255, 255, 255))
    OppScoreText = bigFont.render(str(OPPONENT_SCORE), True, (255, 255, 255))

    screen.blit(teamText, (screen.get_width() / 4 - teamText.get_width() / 2 + 10, screen.get_height() / 2 - 50))
    screen.blit(opponentText, (screen.get_width() * .75 - opponentText.get_width() / 2 - 5, screen.get_height() / 2 - 50))

    screen.blit(teamScoreText, (screen.get_width() / 4 - teamScoreText.get_width() / 2 + 5, screen.get_height() / 2))
    screen.blit(OppScoreText, (screen.get_width() * .75 - OppScoreText.get_width() / 2, screen.get_height() / 2))

    quarterText = bigFont.render(quarterScoreText, True, (255, 255, 255))

    screen.blit(quarterText, (screen.get_width() / 2 - quarterText.get_width() / 2, screen.get_height() / 2 - quarterText.get_height() / 2 + 50))

    headerText = font.render("GridIron Road", True, (255,255,255))
    screen.blit(headerText, (screen.get_width() / 2 - headerText.get_width() / 2 + 5, screen.get_height() / 4 + headerText.get_height() / 2 + 50))

    pygame.display.update()

    # time.sleep(1.5)

    # preText = "Week " + str(WEEK) + " vs " + OPPOSING_TEAM + "!"
    # pregameText = font.render(preText, True, (255, 255, 255))
    # screen.blit(pregameText, (screen.get_width() / 2 - pregameText.get_width() / 2, 80))

    # bottomText = font.render("Press ENTER to start the game", True, (255, 255, 255))
    # screen.blit(bottomText, (screen.get_width() / 2 - bottomText.get_width() / 2, screen.get_height() - 100))

    # teamScoreboardText = "%s: %s" % (MY_TEAM, TEAM_SCORE)
    # opponentScoreboardText = "%s: %s" % (OPPOSING_TEAM, OPPONENT_SCORE)

    # quarterText = font.render(quaterScoreText, True, (255, 255, 255))
    # teamScoreText = font.render(teamScoreboardText, True, (255, 255, 255))
    # opponentScoreText = font.render(opponentScoreboardText, True, (255, 255, 255))

    # y_offset = screen.get_height() / 2 - 50

    # screen.blit(quarterText, (screen.get_width() / 2 - quarterText.get_width() / 2, y_offset))
    # y_offset += 50
    # screen.blit(teamScoreText, (screen.get_width() / 2 - teamScoreText.get_width() / 2, y_offset))
    # y_offset += 50
    # screen.blit(opponentScoreText, (screen.get_width() / 2 - opponentScoreText.get_width() / 2, y_offset))

    # pygame.display.update()

    # time.sleep(2)

def miniGameHandler(screen):
    global QUARTER, OPPONENT_SCORE, TEAM_SCORE
    global MY_OFFENSE, MY_DEFENSE, MY_SPECIAL
    global OPPOSING_OFFENSE, OPPOSING_DEFENSE, OPPOSING_SPECIAL
    global PERFORMANCE_TOTAL, MORALE_TOTAL

    #pick random mini-game
    miniGames = [puntReturn, fieldGoal, runPlay, blockPass]
    # miniGame = miniGames[QUARTER - 1]
    miniGame = random.choice(miniGames)
    print("Selected mini-game: ", miniGame.__name__)

    pregame_Copy = screen.copy()

    # #start mini-game
    gameResult = miniGame.exec(screen)
    print("Game result: ", gameResult)
    QUARTER += 1

    drives = random.randint(1, 3)

    #update the score based on the mini-game result
    if gameResult == True:
        print(miniGame.__name__, "result: ", gameResult)
        if miniGame.__name__ == "minigames.puntReturn":
            TEAM_SCORE += 7
        elif miniGame.__name__ == "minigames.fieldGoal":
            TEAM_SCORE += 3
        elif miniGame.__name__ == "minigames.runPlay":
            TEAM_SCORE += 7
        elif miniGame.__name__ == "minigames.blockPass":
            drives -= 1
    else:
        if miniGame.__name__ == "minigames.blockPass":
            drives += 1

    screen.blit(pregame_Copy, (0, 0))

    #call the prob engine with the outcome of the mini-game
    if QUARTER < 5:
        #call probEngine with result of drive
        for i in range(drives):
            probEngineResult = probEngine.simulateDrive(
                MY_OFFENSE,
                MY_DEFENSE,
                MY_SPECIAL,
                OPPOSING_OFFENSE,
                OPPOSING_DEFENSE,
                OPPOSING_SPECIAL,
                PERFORMANCE_TOTAL,
                MORALE_TOTAL,
                gameResult)
            
            print("Prob engine result: ", probEngineResult)

            #update the score based on the probEngine result
            if probEngineResult > 0:
                # you scored
                TEAM_SCORE += probEngineResult
            elif probEngineResult < 0:
                # they scored
                OPPONENT_SCORE += abs(probEngineResult)

            updateScoreboard(screen)
            print("Current score: ", TEAM_SCORE, OPPONENT_SCORE)
        time.sleep(2)
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

def resetWeek():
    global TEAM_SCORE, OPPONENT_SCORE, QUARTER
    TEAM_SCORE = 0
    OPPONENT_SCORE = 0
    QUARTER = 1

def singularMiniGame(screen):
    #pick random mini-game
    miniGames = [puntReturn, fieldGoal, runPlay, blockPass]
    miniGame = random.choice(miniGames)
    print("Selected mini-game: ", miniGame.__name__)

    pregame_Copy = screen.copy()

    # #start mini-game
    gameResult = miniGame.exec(screen)
    print("Game result: ", gameResult)

    screen.blit(pregame_Copy, (0, 0))

def byeWeek(screen):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    screen.fill((0, 0, 0))

    screen.blit(preImage, (0, 0))

    print("Bye week is starting")

    preText = "Welcome to this week's bye week practice!"
    pregameText = font.render(preText, True, (255, 255, 255))
    screen.blit(pregameText, (screen.get_width() / 2 - pregameText.get_width() / 2, 80))

    bottomText = font.render("Press ENTER to continue", True, (255, 255, 255))
    screen.blit(bottomText, (screen.get_width() / 2 - bottomText.get_width() / 2, screen.get_height() - 100))
    pygame.display.update()

    byeWeek = True
    while byeWeek:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    singularMiniGame(screen)
                    byeWeek = False
                    return


def inGame(screen, matchup, scenarios):
    global WEEK, TEAM_SCORE, OPPONENT_SCORE, QUARTER
    global MORALE_TOTAL, PERFORMANCE_TOTAL

    resetWeek()

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    screen.fill((0, 0, 0))

    screen.blit(preImage, (0, 0))

    print("Game is starting")

    WEEK = matchup["week"]

    preText = "Welcome to week " + str(matchup["week"]) + " vs " + matchup["opponent"] + "!"
    pregameText = font.render(preText, True, (255, 255, 255))
    screen.blit(pregameText, (screen.get_width() / 2 - pregameText.get_width() / 2, screen.get_height() / 2))

    bottomText = font.render("Press ENTER to start the game", True, (255, 255, 255))
    screen.blit(bottomText, (screen.get_width() / 2 - bottomText.get_width() / 2, screen.get_height() - 100))
    pygame.display.update()

    for scenario in scenarios:
        print(scenario["description"])

    for scenario in scenarios:
        MORALE_TOTAL += scenario["effect"]["morale"]
        PERFORMANCE_TOTAL += scenario["effect"]["performance"]

    print("Morale total: ", MORALE_TOTAL)
    print("Performance total: ", PERFORMANCE_TOTAL)

    handleTeamGlobals(matchup["opponent"])

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

    