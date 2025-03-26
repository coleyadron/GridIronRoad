import pygame
import json
import random

def killgame():
    pygame.quit()
    quit()

def loadDecisions():
    try:
        with open("json/pregameScenarios.json", "r") as file:
            decisions = json.load(file)
            return decisions
    except FileNotFoundError:
        print("Error finding decisions file")
        return None
    except json.JSONDecodeError:
        print("Error decoding decisions file")
        return None
    except Exception as e:
        print("Error reading decisions file: ", e)
        return None
    except KeyError as e:
        print("Error reading decisions file: ", e)
        return None

def preGameDecisions(screen, matchup):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    scenarios = loadDecisions()
    print(scenarios)

    screen.fill((0, 0, 0))

    pregameText = font.render("Welcome to Gridiron Road!", True, (255, 255, 255))
    screen.blit(pregameText, (screen.get_width() / 2 - pregameText.get_width() / 2, 0))

    pygame.display.update()


    decisionMaking = True
    while decisionMaking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                killgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Starting new game")
                    decisionMaking = False
                if event.key == pygame.K_ESCAPE:
                    print("Loading game")
                    decisionMaking = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1050))
    matchup = {"week": 1, "opponent": "Bears", "played": False, "result": "None"}
    preGameDecisions(screen, matchup)

if __name__ == "__main__":
    main()    