import pygame
import gridironRoad
import json

SELECTED = 0

def getContracts():
    try:
        with open("json/contract.json", "r") as file:
            data = json.load(file)

            experience = "Rookie"

            easy_level = data["contracts"][experience]['Easy']
            medium_level = data["contracts"][experience]['Medium']
            hard_level = data["contracts"][experience]['Hard']

            return [easy_level, medium_level, hard_level]

    except FileNotFoundError:
        print("Error finding contracts file")
        return ["Easy", "Medium", "Hard"]
    except json.JSONDecodeError:
        print("Error decoding contract levels")
        return ["Easy", "Medium", "Hard"]
    except Exception as e:
        print("Error reading contract levels: ", e)
        return ["Easy", "Medium", "Hard"]
    except KeyError as e:
        print("Error reading contract: ", e)
        return ["Easy", "Medium", "Hard"]
    
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


def selectTeam(screen):
    global SELECTED

    def displayEmpty(topRow):
        screen.fill((0, 0, 0))
        screen.blit(bgi, (0, 0))

        if topRow:
            inputSelection = font.render("Select your team:", True, (255, 255, 255))
            screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))

        screen.blit(team1, (85, 55))
        screen.blit(team2, (85, 105))
        screen.blit(team3, (85, 155))

        if topRow:
            pygame.display.update()

        return

    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    bgi = pygame.image.load("assets/images/BGI-1.png")

    contractStrings = []
    contractStrings = getContracts()

    team1 = font.render('1. ' + contractStrings[0]['level'] + ': ' + contractStrings[0]['displayName'], True, (255, 255, 255))
    team2 = font.render('2. ' + contractStrings[1]['level'] + ': ' + contractStrings[1]['displayName'], True, (255, 255, 255))
    team3 = font.render('3. ' + contractStrings[2]['level'] + ': ' + contractStrings[2]['displayName'], True, (255, 255, 255))

    screen.blit(bgi, (0, 0))
    screen.blit(team1, (85, 55))
    screen.blit(team2, (85, 105))
    screen.blit(team3, (85, 155))

    inputSelection = font.render("Select your team:", True, (255, 255, 255))

    screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))

    pygame.display.update()

    teamOpen = True
    confirmSelection = False
    while teamOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN and teamOpen:
                if (event.key == pygame.K_1 or event.key == pygame.K_KP1) and not confirmSelection:
                    SELECTED = 1
                    # print("Team 1 selected")
                    confirmSelection = True

                    displayEmpty(False)

                    inputSelection = font.render("Select your team: 1", True, (255, 255, 255))
                    screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))
                    
                    wrapped_lines = wrap_text(contractStrings[0]['description'], font, screen.get_width() - 200)

                    y_offset = 10
                    for line in wrapped_lines:
                        text = font.render(line, True, (255, 255, 255))
                        screen.blit(text, (85, screen.get_height() / 2 + y_offset))
                        y_offset += text.get_height()
                    
                    pygame.display.update()
                
                elif (event.key == pygame.K_2  or event.key == pygame.K_KP2) and not confirmSelection:
                    SELECTED = 2
                    # print("Team 2 selected")
                    confirmSelection = True

                    displayEmpty(False)

                    inputSelection = font.render("Select your team: 2", True, (255, 255, 255))
                    screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))
                    
                    wrapped_lines = wrap_text(contractStrings[1]['description'], font, screen.get_width() - 200)

                    y_offset = 10
                    for line in wrapped_lines:
                        text = font.render(line, True, (255, 255, 255))
                        screen.blit(text, (85, screen.get_height() / 2 + y_offset))
                        y_offset += text.get_height()
                    
                    pygame.display.update()

                elif (event.key == pygame.K_3 or event.key == pygame.K_KP3) and not confirmSelection:
                    SELECTED = 3
                    # print("Team 3 selected")
                    confirmSelection = True

                    displayEmpty(False)

                    inputSelection = font.render("Select your team: 3", True, (255, 255, 255))
                    screen.blit(inputSelection, (75, screen.get_height() - inputSelection.get_height() - 30))
                    
                    wrapped_lines = wrap_text(contractStrings[2]['description'], font, screen.get_width() - 200)

                    y_offset = 10
                    for line in wrapped_lines:
                        text = font.render(line, True, (255, 255, 255))
                        screen.blit(text, (85, screen.get_height() / 2 + y_offset))
                        y_offset += text.get_height()
                    
                    pygame.display.update()
                
                if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and confirmSelection:
                    # print("Team selection confirmed")
                    teamOpen = False
                    return contractStrings[SELECTED - 1]
                if event.key == pygame.K_ESCAPE:
                    # print("Game has been closed")
                    gridironRoad.killgame(screen)
                if event.key == pygame.K_BACKSPACE and confirmSelection:
                    # print("Team selection cancelled")
                    confirmSelection = False
                    
                    displayEmpty(True)