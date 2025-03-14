import pygame
# import gridironRoad
import json

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
            return season
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
    screen.blit(nextScreenText, (0, screen.get_height() - 100))


    pygame.display.update()

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
                    seasonOverviewOpen = False
                    return
                if event.key == pygame.K_RETURN:
                    print("ENTER action, next screen")
                    seasonOverviewOpen = False

    return

def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1050))
    seasonOverview(screen)

if __name__ == "__main__":
    main()