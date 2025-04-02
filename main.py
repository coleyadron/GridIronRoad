import pygame
from screens import experienceSelection
from screens import draft
from screens import coachingStaff
from screens import teamSelection
from screens import seasonOverview
from screens import pregameDecisions
import gridironRoad
import json
# from screens.minigames import puntReturn

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
    matchup = seasonOverview.seasonOverview(screen)

    pregameDecisions.preGameDecisions(screen, matchup)

def  newGame(screen):
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

    DRAFT = draft.draft(screen)
    # print(DRAFT)
    gridironRoad.updateGlobalState("draft", DRAFT)

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
                print("Game is already started")
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