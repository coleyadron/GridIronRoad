import pygame, sys
import json
# from main import retrieveState

EXPERIENCE = None
TEAM = None
STAFF = None
DRAFT = None

def loadTeam():
    try:
        with open("json/userTeam.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error finding JSON file")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON file")
        return None
    except Exception as e:
        print("Error reading JSON file: ", e)
        return None

def calculateSalaryCap():
    team = loadTeam()

    # salary_cap = 279200000
    teamSalary = 0

    # Calculate the total salary of the team
    players = team["players"]
    for player in players:
        teamSalary += player["salary"]

    # Calculate the percentage of the salary cap used
    # salary_percentage = (teamSalary / salary_cap) * 100

    return teamSalary

def updateGlobalState(variable, value):
    global EXPERIENCE, TEAM, STAFF, DRAFT
    if variable == "experience":
        EXPERIENCE = value
    elif variable == "team":
        TEAM = value
    elif variable == "staff":
        STAFF = value
    elif variable == "draft":
        DRAFT = value
    else:
        print("Variable not found")

# def retrieveGameState():
#     state = retrieveState()
#     return state

def saveGameState():
    try:
        if EXPERIENCE is None and TEAM is None and STAFF is None and DRAFT is None:
            print("No game data to save")
            return
        with open("json/userState.json", "w") as f:
            state = {
                "started": True,
                "experience": EXPERIENCE,
                "team": TEAM,
                "staff": STAFF,
                "draft": DRAFT
            }
            json.dump(state, f, indent=4)
    except Exception as e:
        print("Error saving game state: ", e)
    print("Game is saved")

def killgame(screen):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    copy_screen = screen.copy()

    confirmationText = font.render("Are you sure you want to quit the game?", True, (0, 0, 0))
    yesText = font.render("Press SPACE to exit", True, (0, 0, 0))
    
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
                # data = retrieveGameState()
                saveGameState()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # data = retrieveGameState()
                    saveGameState()
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    screen.blit(copy_screen, (0, 0))
                    pygame.display.update()
                    return