import pygame
# import gridironRoad
import json
# import pregameDecisions
from screens import teamOverview
from screens import freeAgentSelection

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def killgame():
    pygame.quit()
    quit()

def loadSeason():
    try:
        with open("json/userSeason.json", "r") as file:
            season = json.load(file)
            return season["regularSeason"]
    except FileNotFoundError:
        print("Error finding season file")
        return None
    except json.JSONDecodeError:
        print("Error decoding season file")
        return None
    except Exception as e:
        print("Error reading season file: ", e)
        return None
    except KeyError as e:
        print("Error reading season file: ", e)
        return None
    
def display_matchup(game):
    # print(game)
    week = game["week"]
    opponent = game["opponent"]
    played = game["played"]
    result = game["result"]

    if played:
        text = f"Week {week}: {opponent} - {result.capitalize()}"
    else:
        text = f"Week {week}: {opponent}"

    return text

def findCurrentWeek(season):
    for game in season["matchups"]:
        if not game["played"] or (game["opponent"] == "Bye Week" and not game["played"]):
            return game
    return None

def seasonOverview(screen):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    screen.fill((0, 0, 0))

    overviewText = font.render("Season Overview", True, (255, 255, 255))
    screen.blit(overviewText, (0,0))

    season = loadSeason()

    if not season:
        print("No matchups found. Exiting.")
        return

    y_offset = 100
    for game in season["matchups"]:
        text = display_matchup(game)
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (50, y_offset))
        y_offset += 40

    nextScreenText = font.render("Press SPACE to enter the next game", True, WHITE)
    viewTeamText = font.render("Press 1 to view team", True, WHITE)
    viewFreeAgentsText = font.render("Press 2 to view free agents", True, WHITE)
    screen.blit(viewFreeAgentsText, (0, screen.get_height() - 50))
    screen.blit(nextScreenText, (0, screen.get_height() - 150))
    screen.blit(viewTeamText, (0, screen.get_height() - 100 ))

    pygame.display.update()

    matchup = findCurrentWeek(season)
    print(matchup)

    seasonOverviewOpen = True
    while seasonOverviewOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                killgame()
                # gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    killgame()
                    # gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("SPACE action, next screen")
                    # pregameDecisions.preGameDecisions(screen, matchup)
                    seasonOverviewOpen = False
                    return matchup
                if event.key == pygame.K_RETURN:
                    print("ENTER action, next screen")
                    # pregameDecisions.preGameDecisions(screen, matchup)
                    seasonOverviewOpen = False
                    return matchup
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    print("1 action, view team")
                    overViewCopy = screen.copy()
                    teamOverview.teamOverview(screen, 'season')
                    screen.blit(overViewCopy, (0, 0))
                    pygame.display.flip()
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    print("2 action, view team")
                    overViewCopy = screen.copy()
                    freeAgentSelection.free_agents(screen)
                    screen.blit(overViewCopy, (0, 0))
                    pygame.display.flip()

    return

def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1050))
    seasonOverview(screen)

if __name__ == "__main__":
    main()