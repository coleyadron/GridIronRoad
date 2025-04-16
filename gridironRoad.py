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

def calculateTeamOverall():
    offensivePositions = ["QB", "RB", "WR", "TE", "OL"]
    defensivePositions = ["DL", "LB", "CB", "S"]
    specialTeamsPositions = ["K", "P", "LS"]

    team = loadTeam()
    overall = 0
    offensiveOverall = 0
    offenseCount = 0
    defensiveOverall = 0
    defenseCount = 0
    specialOverall = 0
    specialCount = 0

    # Calculate the overall rating of the team
    players = team["players"]
    for player in players:
        overall += player["stats"]["overall"]
        if player["position"] in offensivePositions:
            offensiveOverall += player["stats"]["overall"]
            offenseCount += 1
        elif player["position"] in defensivePositions:
            defensiveOverall += player["stats"]["overall"]
            defenseCount += 1
        elif player["position"] in specialTeamsPositions:
            specialOverall += player["stats"]["overall"]
            specialCount += 1


    # Calculate rating
    overall = overall // len(players)
    if offenseCount > 0:
        offensiveOverall = offensiveOverall // offenseCount
    if defenseCount > 0:
        defensiveOverall = defensiveOverall // defenseCount
    if specialCount > 0:
        specialOverall = specialOverall // specialCount

    #create dictionary
    teamOverall = {
        "name": team["team_name"],
        "overall": overall,
        "offense": offensiveOverall,
        "defense": defensiveOverall,
        "special_teams": specialOverall
    }

    return teamOverall

def getRecord():
    try:
        with open("json/userSeason.json", "r") as file:
            data = json.load(file)

            record = data["regularSeason"]["matchups"]

            wins = 0
            losses = 0
            ties = 0

            for matchup in record:
                if matchup["played"]:
                    if matchup["result"] == "win":
                        wins += 1
                    elif matchup["result"] == "loss":
                        losses += 1
                    elif matchup["result"] == "tie":
                        ties += 1
            totalGames = wins + losses + ties

            print("Wins: ", wins)
            print("Losses: ", losses)
            print("Ties: ", ties)
            print("Total games: ", totalGames)

            if totalGames == 0:
                winPercentage = 0
            else:
                winPercentage = (wins / totalGames) * 100
            record = {
                "wins": wins,
                "losses": losses,
                "ties": ties,
                "totalGames": totalGames,
                "winPercentage": winPercentage
            }
            return record
        
    except FileNotFoundError:
        print("Error finding JSON file")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON file")
        return None
    except Exception as e:
        print("Error reading JSON file: ", e)
        return None

def getOpponent(opponentName):
    opponent = None
    try:
        with open("json/leagueTeams.json", "r") as file:
            data = json.load(file)
            
            for team in data["teams"]:
                if team["name"] == opponentName:
                    opponent = team
                    break
            
        if opponent is None:
            print(f"Opponent '{opponentName}' not found.")
            return None
        else:
            # Extract the ratings from the opponent dictionary
            opponentRatings = {
                "name": opponent["name"],
                "overall": opponent["ratings"]["overall"],
                "offense": opponent["ratings"]["offense"],
                "defense": opponent["ratings"]["defense"],
                "special_teams": opponent["ratings"]["special_teams"]
            }
            return opponentRatings
        
    except FileNotFoundError:
        print("Error finding JSON file")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON file")
        return None
    except Exception as e:
        print("Error reading JSON file: ", e)
        return None

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

def updateSeason(matchup, game_result):
    myScore = game_result["score"]
    opponentScore = game_result["opponent_score"]

    week = matchup["week"]
    opponent = matchup["opponent"]

    updatedWeek = {
        "week": week,
        "opponent": opponent,
        "played": True,
        "user_score": myScore,
        "opponent_score": opponentScore,
        "result": game_result["game_result"]
    }

    # print("Updated week: ", updatedWeek)

    try:
        with open("json/userSeason.json", "r") as file:
            data = json.load(file)
            season = data['regularSeason']["matchups"]
            season[week - 1] = updatedWeek

        with open("json/userSeason.json", "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print("Error updating season: ", e)

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