import pygame
from screens import experienceSelection
from screens import draft
from screens import coachingStaff
from screens import teamSelection
from screens import seasonOverview
from screens import pregameDecisions
from screens import postgameDecisions
from screens import inGame
from logic import scheduler
import gridironRoad
import json
import random

EXPERIENCE = None
TEAM = None
STAFF = None
DRAFT = None

# def retrieveState():
#     state = {
#         "started": True,
#         "experience": EXPERIENCE,
#         "team": TEAM, 
#         "staff": STAFF,
#         "draft": DRAFT
#     }
#     print(state)
#     return state

def playGame(screen):
    print("Game is starting")

    whereSeason = seasonOverview.findCurrentWeek(seasonOverview.loadSeason("regularSeason"))
    if whereSeason is None:
        currentMatch = seasonOverview.findCurrentWeek(seasonOverview.loadSeason("postSeason"))
        if currentMatch is not None:
            print("Current Match: ", currentMatch)
        currentWeek = 20
    else:
        matchup = seasonOverview.seasonOverview(screen)
        currentWeek = matchup["week"]

    while currentWeek <= 18:
        if not matchup["opponent"] == "Bye":
            preScenarios = pregameDecisions.preGameDecisions(screen, matchup)

            game_result = inGame.inGame(screen, matchup, preScenarios)

            gridironRoad.updateSeason(matchup, game_result)

            postScenarios = postgameDecisions.postGameDecisions(screen, matchup)

            print("Scenarios: ", postScenarios)

            overView = seasonOverview.seasonOverview(screen)
        else:
            print("Practice week")

            #execute bye
            inGame.byeWeek(screen)
            #update season with the bye
            bye_result = { 
                "week": matchup["week"],
                "opponent": matchup["opponent"],
                "played": True,
                "score": None,
                "opponent_score": None,
                "game_result": None
            }
            gridironRoad.updateSeason(matchup, bye_result)

        #find next week
        matchup = seasonOverview.findCurrentWeek(seasonOverview.loadSeason("regularSeason"))

        if matchup is not None:
            print("Matchup: ", matchup)
            currentWeek = matchup["week"]
        else:
            print("Playoffs?")
            currentWeek = 20

    postSeason = True
    while postSeason:
        matchups = seasonOverview.loadSeason('postSeason')

        # print("Matchups: ", matchups)

        currentMatchup = seasonOverview.findCurrentWeek(matchups)

        if currentMatchup is None:
            print("No more matchups")
            break
        print("Current matchup: ", currentMatchup)
        
        #check record
        record = gridironRoad.getRecord()

        # if record["ties"] > 0:
        #     print("Record: %s - %s - %s" % (record["wins"], record["losses"], record["ties"]))
        # else:
        #     print("Record: %s - %s" % (record["wins"], record["losses"]))

        #if record over benchmark go into playoffs loop
        # playoffs record for playoffs --> random 8 - 10
        # first week bye record -> 14+
        #else end season 

        wins_for_playoffs = random.randint(8, 10)
        first_round_bye = 14

        if record["wins"] >= first_round_bye:
            # print("First round bye playoffs")
            if currentMatchup["game_name"] == "Wild Card":
                game_result = {
                    "game_name": "Wild Card - Bye Week",
                    "opponent": "Bye Week",
                    "played": True,
                    "score": None,
                    "opponent_score": None,
                    "game_result": None
                }
                
                gridironRoad.updateSeason(currentMatchup, game_result, postSeason=True)

                inGame.byeWeek(screen)

        elif record["wins"] >= wins_for_playoffs:
            print("Playoff games")

            preScenarios = pregameDecisions.preGameDecisions(screen, currentMatchup)

            game_result = inGame.inGame(screen, currentMatchup, preScenarios)

            gridironRoad.updateSeason(currentMatchup, game_result, postSeason=True)

            if game_result["game_result"] == "loss":
                print("You lost the game")
                postSeason = False
            
            else:
                print("You won the game")
                postScenarios = postgameDecisions.postGameDecisions(screen, currentMatchup)

                # print("Scenarios: ", postScenarios)

                #check if there are more matchups
                currentMatchup = seasonOverview.findCurrentWeek(seasonOverview.loadSeason("postSeason"))

                if currentMatchup is None:
                    print("No more matchups")
                    break
                else:
                    print("Next matchup: ", currentMatchup)
                    continue

        else:
            print("Season over")
            postSeason = False


def  newGame(screen):
    #reset user team and free agents
    gridironRoad.resetJsons()

    # print("SPACE action, next screen")
    EXPERIENCE = experienceSelection.selectExperience(screen)
    # print(EXPERIENCE)
    gridironRoad.updateGlobalState("experience", EXPERIENCE) 

    TEAM = teamSelection.selectTeam(screen, EXPERIENCE)
    # print(TEAM)
    gridironRoad.updateGlobalState("team", TEAM)

    STAFF = coachingStaff.inputStaff(screen)
    # print(STAFF)
    gridironRoad.updateGlobalState("staff", STAFF)

    gridironRoad.updateUserTeam(STAFF[0])

    DRAFT = draft.draft(screen)
    # print(DRAFT)
    gridironRoad.updateGlobalState("draft", DRAFT)

       # make season
    scheduler.scheduler()

    #start game
    playGame(screen)
    

def loadGame(screen, state):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    confirmationText = font.render("Would you like to load your save file?", True, (0, 0, 0))
    yesText = font.render("Press SPACE to load or ESCAPE for a new file", True, (0, 0, 0))
    
    pygame.draw.rect(screen, (225, 225, 225), (screen.get_width() / 2 -  confirmationText.get_width() * 1.25 / 2,
                                               screen.get_height() / 4,
                                               confirmationText.get_width() * 1.25, screen.get_height() * .5))

    screen.blit(confirmationText, (screen.get_width() / 2 - confirmationText.get_width() / 2, screen.get_height() * .33))
    
    screen.blit(yesText, (screen.get_width() / 2 - yesText.get_width() / 2, screen.get_height() * .66))
        
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Starting new game")
                    newGame(screen)
                    running = False
                if event.key == pygame.K_SPACE:
                    print("Loading game")

                    gridironRoad.updateGlobalState("experience", state["experience"])
                    gridironRoad.updateGlobalState("team", state["team"])
                    gridironRoad.updateGlobalState("staff", state["staff"])
                    gridironRoad.updateGlobalState("draft", state["draft"])     

                    EXPERIENCE = state["experience"]
                    TEAM = state["team"]
                    STAFF = state["staff"]
                    DRAFT = state["draft"]

                    # print("Experience: ", EXPERIENCE)
                    # print("Team: ", TEAM)
                    # print("Staff: ", STAFF)
                    # print("Draft: ", DRAFT)

                    playGame(screen)

                running = False

def startGame(screen):
    try:
        with open("json/userState.json", "r") as f:
            state = json.load(f)
            if not state:
                print("No save file found")
                newGame(screen)
                return
            elif not state["started"]:
                print("Game started is False")
                newGame(screen)
                return
            print(state)
            if state["started"]:
                # print("Game is already started but who cares")
                loadGame(screen, state)
                return
            else:
                print("Starting new game")
                newGame(screen)
    except Exception as e:
        print("Error starting game: ", e)
    except FileNotFoundError:
        print("No save file found")
    except json.JSONDecodeError:
        print("Error decoding save file")

def main():
    global EXPERIENCE, TEAM, STAFF, DRAFT

    pygame.init()
    pygame.display.init()

    # info = pygame.display.Info()
    screen = pygame.display.set_mode((1400, 1050))

    pygame.display.set_caption("GridIron Road")
    pygame.display.set_icon(pygame.image.load("assets/images/gridIronLogo.PNG"))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    mainScreenLogo = pygame.image.load("assets/images/giLogoBorder.png").convert_alpha()
    mainScreenImage = pygame.image.load("assets/images/startScreen.png").convert()
    startText = font.render("Press SPACE to Start Game", True, (255, 255, 255))

    screen.blit(mainScreenImage, (screen.get_width() / 2 - mainScreenImage.get_width() / 2,
                                screen.get_height() / 3 - mainScreenImage.get_height() / 3))

    screen.blit(mainScreenLogo, (screen.get_width() / 2 - mainScreenLogo.get_width() / 2, 
                                screen.get_height() / 10 - mainScreenLogo.get_height() / 10))

    screen.blit(startText, (screen.get_width() / 2 - startText.get_width() / 2, 
                            screen.get_height() - startText.get_height() - 30))

    pygame.display.update()

    running = True

    # def kill_game():
    #     pygame.quit()
    #     sys.exit()

    mainScreen = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # print("Game has been closed")
                    gridironRoad.killgame(screen)

                if event.key == pygame.K_SPACE and mainScreen:
                    mainScreen = False
                    startGame(screen)
                    
if __name__ == "__main__":
    main()