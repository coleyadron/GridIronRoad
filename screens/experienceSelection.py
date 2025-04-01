import pygame
import gridironRoad
import json
import random

SELECTED = 0

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

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + ' '
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
    lines.append(current_line)

    return lines

def showMoreInfo(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    rookie = font.render("Rookie", True, (255, 255, 255))
    experienced = font.render("Experienced", True, (255, 255, 255))
    legendary = font.render("Legendary", True, (255, 255, 255))

    rookieText = 'Rookie description'
    experiencedText = 'Experienced description'
    legendaryText = 'Legendary description'

    wrapped_rookie = wrap_text(rookieText, font, screen.get_width() - 100)
    wrapped_experienced = wrap_text(experiencedText, font, screen.get_width() - 100)
    wrapped_legendary = wrap_text(legendaryText, font, screen.get_width() - 100)

    y_offset = 10

    screen.blit(rookie, (0, y_offset))
    y_offset += font.get_linesize()
    for line in wrapped_rookie:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (50, y_offset))
        y_offset += font.get_linesize()


    screen.blit(experienced, (0, y_offset))
    y_offset += font.get_linesize()
    for line in wrapped_experienced:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (50, y_offset))
        y_offset += font.get_linesize()


    screen.blit(legendary, (0, y_offset))
    y_offset += font.get_linesize()
    for line in wrapped_legendary:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (50, y_offset))
        y_offset += font.get_linesize()


    returnText = font.render("Press ENTER to return to experience selection", True, (255, 255, 255))
    screen.blit(returnText, (0, screen.get_height() - returnText.get_height()))

    pygame.display.update()

    return

def selectExperience(screen):
    global SELECTED

    def displayEmpty(topRow):
        screen.fill((0, 0, 0))
        screen.blit(bgi, (0, 0))

        if topRow:
            inputSelection = font.render("Select your experience:", True, (255, 255, 255))
            screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))

        screen.blit(experience1, (85, 55))
        screen.blit(experience2, (85, 105))
        screen.blit(experience3, (85, 155))
        screen.blit(moreInfo, (85, 205))

        if topRow:
            pygame.display.update()

        return

    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    bgi = pygame.image.load("assets/images/BGI-1.png")

    expStrings = []

    expStrings = getExperienceLevels()
    moreInfoString = '4. More info on each experience level'
    
    experience1 = font.render('1. ' + expStrings[0]['displayName'], True, (255, 255, 255))
    experience2 = font.render('2. ' + expStrings[1]['displayName'], True, (255, 255, 255))
    experience3 = font.render('3. ' + expStrings[2]['displayName'], True, (255, 255, 255))
    moreInfo = font.render(moreInfoString, True, (255, 255, 255))

    screen.blit(bgi, (0, 0))
    screen.blit(experience1, (85, 55))
    screen.blit(experience2, (85, 105))
    screen.blit(experience3, (85, 155))
    screen.blit(moreInfo, (85, 205))

    inputSelection = font.render("Select your experience:", True, (255, 255, 255))   

    screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))

    pygame.display.update()

    experienceOpen = True
    confirmSelection = False
    moreInfoOpen = False
    returnMore = False

    while experienceOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN and experienceOpen:
                if (event.key == pygame.K_1 or event.key == pygame.K_KP1) and not confirmSelection:
                    SELECTED = 1
                    # print("Experience 1 selected")
                    confirmSelection = True
                    returnMore = False

                    inputSelection = font.render("Select your experience: 1", True, (255, 255, 255))
                    
                    displayEmpty(False)
                    
                    screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))

                    wrapped_lines = wrap_text(expStrings[0]['description'], font, screen.get_width() - 200)  # 20 pixels padding

                    y_offset = 10
                    for line in wrapped_lines:
                        text_surface = font.render(line, True, (255, 255, 255))
                        screen.blit(text_surface, (85, screen.get_height() / 2 + y_offset))
                        y_offset += font.get_linesize()

                    pygame.display.update()

                elif (event.key == pygame.K_2  or event.key == pygame.K_KP2) and not confirmSelection:
                    SELECTED = 2
                    # print("Experience 2 selected")
                    confirmSelection = True
                    returnMore = False

                    inputSelection = font.render("Select your experience: 2", True, (255, 255, 255))
                    
                    displayEmpty(False)

                    screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))

                    wrapped_lines = wrap_text(expStrings[1]['description'], font, screen.get_width() - 200)  # 20 pixels padding

                    y_offset = 10
                    for line in wrapped_lines:
                        text_surface = font.render(line, True, (255, 255, 255))
                        screen.blit(text_surface, (85, screen.get_height() / 2 + y_offset))
                        y_offset += font.get_linesize()

                    pygame.display.update()

                elif (event.key == pygame.K_3 or event.key == pygame.K_KP3) and not confirmSelection:
                    SELECTED = 3
                    # print("Experience 3 selected")
                    confirmSelection = True
                    returnMore = False

                    inputSelection = font.render("Select your experience: 3", True, (255, 255, 255))
                    
                    displayEmpty(False)

                    screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))

                    wrapped_lines = wrap_text(expStrings[2]['description'], font, screen.get_width() - 200)  # 20 pixels padding

                    y_offset = 10
                    for line in wrapped_lines:
                        text_surface = font.render(line, True, (255, 255, 255))
                        screen.blit(text_surface, (85, screen.get_height() / 2 + y_offset))
                        y_offset += font.get_linesize()

                    pygame.display.update()

                elif (event.key == pygame.K_4 or event.key == pygame.K_KP4) and not confirmSelection:
                    # print("Experience 4 selected")
                    confirmSelection = True
                    moreInfoOpen = True
                    returnMore = True

                    inputSelection = font.render("Select your experience: 4", True, (255, 255, 255))
                    
                    displayEmpty(False)
                    

                    screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))
                    pygame.display.update()

                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER and confirmSelection:
                    # experienceOpen = False
                    # print("Enter action, next screen")

                    if moreInfoOpen:
                        showMoreInfo(screen)
                        moreInfoOpen = False
                        returnMore = True
                    elif returnMore:
                        displayEmpty(True)
                        confirmSelection = False
                    else:
                        experienceOpen = False
                        return expStrings[SELECTED - 1]
                

                if event.key == pygame.K_ESCAPE:
                    # print("Game has been closed")
                    gridironRoad.killgame(screen)
                if event.key == pygame.K_BACKSPACE and confirmSelection:
                    confirmSelection = False
                    # print("Backspace action, reselect experience")
                    displayEmpty(True)