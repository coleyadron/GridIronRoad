import pygame
import json
import random

def killgame():
    pygame.quit()
    quit()

def loadDecisions():
    try:
        with open("json/postgameScenarios.json", "r") as file:
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
    
def pickScenario(scenarios):
    # Pick a random scenario from the list
    scenario = random.choice(scenarios["scenarios"])
    # Remove the scenario from the list to avoid duplicates
    scenarios["scenarios"].remove(scenario)
    return scenario

def postGameDecisions(screen, matchup):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    BGI = pygame.image.load("assets/images/postgame.png")
    

    scenarios = loadDecisions()

    if scenarios is None:
        print("No scenarios found")
        return

    screen.fill((0, 0, 0))
    screen.blit(BGI, (0, 0))

    preText = "After week " + str(matchup["week"]) + " vs " + matchup["opponent"] + "!"

    pregameText = font.render(preText, True, (255, 255, 255))
    screen.blit(pregameText, (screen.get_width() / 2 - pregameText.get_width() / 2, 80))

    start_screen = screen.copy()

    pickedScenarios = []

    numberScenarios = random.randint(1, 4)
    for i in range(numberScenarios):
        #pick and display scenario
        scenario = pickScenario(scenarios)
        pickedScenarios.append(scenario)
        # print(scenario["description"])
        y_offset = screen.get_height() / 2 - 50

        scenarioText = font.render(scenario["description"], True, (255, 255, 255))
        screen.blit(scenarioText, (screen.get_width() / 2 - scenarioText.get_width() / 2, y_offset))
        y_offset += 50
        
        moraleStr = "Morale: " + str(scenario["effect"]["morale"])
        moraleText = font.render(moraleStr, True, (255, 255, 255))
        screen.blit(moraleText, (screen.get_width() / 2 - moraleText.get_width() / 2, y_offset))
        y_offset += 50

        performanceStr = "Performance: " + str(scenario["effect"]["performance"])
        performanceText = font.render(performanceStr, True, (255, 255, 255))
        screen.blit(performanceText, (screen.get_width() / 2 - performanceText.get_width() / 2, y_offset))

        #confirm effect
        confirmStr = "Press SPACE to confirm"
        confirmText = font.render(confirmStr, True, (255, 255, 255))
        screen.blit(confirmText, (screen.get_width() / 2 - confirmText.get_width() / 2, screen.get_height() - confirmText.get_height() - 30))

        pygame.display.update()

        #wait for user input
        confirmEffect = True
        while confirmEffect:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    killgame()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("Effect confirmed")
                        confirmEffect = False

        #restore screen
        screen.blit(start_screen, (0, 0))

    print("Scenarios complete entering game")
    return(pickedScenarios)

    # pygame.display.update()


    # decisionMaking = True
    # while decisionMaking:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             killgame()
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_SPACE:
    #                 print("Starting new game")
    #                 decisionMaking = False
    #             if event.key == pygame.K_ESCAPE:
    #                 print("Loading game")
    #                 decisionMaking = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1050))
    matchup = {"week": 1, "opponent": "Bears", "played": False, "result": "None"}
    postGameDecisions(screen, matchup)

if __name__ == "__main__":
    main()    