import pygame
import gridironRoad
import json
import random

def getExperienceLevels():
    try:
        with open("json/experience.json", "r") as file:
            data = json.load(file)

            rookie_level = data["experienceLevels"]["Rookie"]
            experienced_level = data["experienceLevels"]["Experienced"]
            legendary_level = data["experienceLevels"]["Legendary"]

            rookie_choice = random.choice(rookie_level)
            experienced_choice = random.choice(experienced_level)
            legendary_choice = random.choice(legendary_level)

            return [rookie_choice, experienced_choice, legendary_choice]

    except FileNotFoundError:
        print("Error finding experience file")
        return ["Rookie", "Experienced", "Legendary"]
    except json.JSONDecodeError:
        print("Error decoding experience levels")
        return ["Rookie", "Experienced", "Legendary"]
    except Exception as e:
        print("Error reading experience levels: ", e)
        return ["Rookie", "Experienced", "Legendary"]
    except KeyError as e:
        print("Error reading experience levels: ", e)
        return ["Rookie", "Experienced", "Legendary"]

def selectExperience(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    expStrings = []

    expStrings = getExperienceLevels()
    moreInfoString = '4. More info on each experience level'
    
    experience1 = font.render('1. ' + expStrings[0]['displayName'], True, (255, 255, 255))
    experience2 = font.render('2. ' + expStrings[1]['displayName'], True, (255, 255, 255))
    experience3 = font.render('3. ' + expStrings[2]['displayName'], True, (255, 255, 255))
    moreInfo = font.render(moreInfoString, True, (255, 255, 255))

    screen.blit(experience1, (0, 0))
    screen.blit(experience2, (0, 50))
    screen.blit(experience3, (0, 100))
    screen.blit(moreInfo, (0, 150))

    inputSelection = font.render("Select your selection:", True, (255, 255, 255))   

    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height()))

    pygame.display.update()

    experienceOpen = True
    confirmSelection = False
    while experienceOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN and experienceOpen:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1 and not confirmSelection:
                    # print("Experience 1 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your experience: 1", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(experience1, (0, 0))
                    screen.blit(experience2, (0, 50))
                    screen.blit(experience3, (0, 100))
                    screen.blit(moreInfo, (0, 150))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height()))
                    pygame.display.update()

                elif event.key == pygame.K_2  or event.key == pygame.K_KP2 and not confirmSelection:
                    # print("Experience 2 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your experience: 2", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(experience1, (0, 0))
                    screen.blit(experience2, (0, 50))
                    screen.blit(experience3, (0, 100))
                    screen.blit(moreInfo, (0, 150))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height()))
                    pygame.display.update()

                elif event.key == pygame.K_3 or event.key == pygame.K_KP3 and not confirmSelection:
                    # print("Experience 3 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your experience: 3", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(experience1, (0, 0))
                    screen.blit(experience2, (0, 50))
                    screen.blit(experience3, (0, 100))
                    screen.blit(moreInfo, (0, 150))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height()))
                    pygame.display.update()

                elif event.key == pygame.K_4 or event.key == pygame.K_KP4 and not confirmSelection:
                    # print("Experience 4 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your experience: 4", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(experience1, (0, 0))
                    screen.blit(experience2, (0, 50))
                    screen.blit(experience3, (0, 100))
                    screen.blit(moreInfo, (0, 150))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height()))
                    pygame.display.update()

                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER and confirmSelection:
                    experienceOpen = False
                    # print("Enter action, next screen")
                    return
                if event.key == pygame.K_ESCAPE:
                    # print("Game has been closed")
                    gridironRoad.killgame(screen)
                if event.key == pygame.K_BACKSPACE and confirmSelection:
                    confirmSelection = False
                    # print("Backspace action, reselect experience")

                    inputSelection = font.render("Select your experience:", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(experience1, (0, 0))
                    screen.blit(experience2, (0, 50))
                    screen.blit(experience3, (0, 100))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))
                    pygame.display.update()