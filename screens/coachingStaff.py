import pygame
import gridironRoad
from cursor import TextCursor

def inputStaff(screen):
    bgi = pygame.image.load("assets/images/BGI-2.png")

    screen.fill((0, 0, 0))
    screen.blit(bgi, (0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    offensiveCoordinator = font.render("Offensive Coordinator: ", True, (255, 255, 255))
    defensiveCoordinator = font.render("Defensive Coordinator: ", True, (255, 255, 255))
    specialTeamsCoordinator = font.render("Special Teams Coordinator: ", True, (255, 255, 255))
    confirmation = font.render("Are these names correct: ", True, (0,0,0))


    screen.blit(offensiveCoordinator, (85, 55))
    screen.blit(defensiveCoordinator, (85, 105))
    screen.blit(specialTeamsCoordinator, (85, 155))

    offenseInput = pygame.Rect(offensiveCoordinator.get_width() + 85, 55, 140, 35)
    defenseInput = pygame.Rect(defensiveCoordinator.get_width() + 85, 105, 140, 35)
    specialInput = pygame.Rect(specialTeamsCoordinator.get_width() + 85, 155, 140, 35)
    confirmationInput = pygame.Rect(confirmation.get_width() + 80, screen.get_height() - confirmation.get_height() - 30, 140, 35)

    pygame.display.update()

    color = pygame.Color('black')

    cursor = TextCursor(35, 35, 15, offenseInput.height)
    cursor.draw(screen)
    cursor.activate()


    offenseText = ''
    defenseText = ''
    specialText = ''
    confirmationText = ''

    activeText = 1
    staffOpen = True

    while staffOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN and staffOpen:
                if event.key == pygame.K_RETURN:
                    if activeText < 3:
                        if activeText == 1 and offenseText != '':
                            activeText += 1
                            cursor.rect.x = defenseInput.x + font.size(defenseText)[0]
                        elif activeText == 2 and defenseText != '':
                            activeText += 1
                            cursor.rect.x = specialInput.x + font.size(specialText)[0]
                    elif activeText == 3 and specialText != '':
                        activeText += 1
                        cursor.rect.x = confirmationInput.x + font.size(confirmationText)[0]

                        confirmation = font.render("Are these names correct: ", True, (255, 255, 255))
                        screen.blit(confirmation, (80, screen.get_height() - confirmation.get_height() - 30))
                        pygame.display.flip()

                    elif activeText == 4:
                        confirmationText = confirmationText.strip().upper()
                        print(confirmationText)
                        print(confirmationText.upper())
                        if confirmationText == 'YES' or confirmationText == 'Y':
                            print("YES CHECK")
                            staffOpen = False
                            return [offenseText.strip(), defenseText.strip(), specialText.strip()]
                        elif confirmationText == 'NO' or confirmationText == 'N':
                            print("NO CHECK")
                            activeText = 1
                            confirmationText = ''
                        else:
                            print("RESET")
                            activeText = 1
                            confirmationText = ''
                            cursor.rect.x = offenseInput.x + font.size(offenseText)[0]

                if event.key == pygame.K_ESCAPE:
                    gridironRoad.killgame(screen)

                if event.key == pygame.K_BACKSPACE:
                    if activeText == 1:
                        offenseText = offenseText[:-1]
                        cursor.setX(offenseInput.x + font.size(offenseText)[0])
                        # cursor.rect.x = offenseInput.x + font.size(offenseText)[0]
                    elif activeText == 2:
                        defenseText = defenseText[:-1]
                        cursor.setX(offenseInput.x + font.size(offenseText)[0]) 
                    elif activeText == 3:
                        specialText = specialText[:-1]
                        cursor.setX(offenseInput.x + font.size(offenseText)[0]) 
                    elif activeText == 4:
                        confirmationText = confirmationText[:-1]
                        cursor.setX(offenseInput.x + font.size(offenseText)[0]) 
                else:
                    if activeText == 1:
                        offenseText += event.unicode
                        cursor.setX(offenseInput.x + font.size(offenseText)[0])                     
                    elif activeText == 2:
                        defenseText += event.unicode
                        cursor.setX(offenseInput.x + font.size(offenseText)[0]) 
                    elif activeText == 3:
                        specialText += event.unicode
                        cursor.setX(offenseInput.x + font.size(offenseText)[0]) 
                    elif activeText == 4:
                        confirmationText += event.unicode
                        cursor.setX(offenseInput.x + font.size(offenseText)[0]) 

                if event.key == pygame.K_UP:
                    if activeText > 1:
                        activeText -= 1
                elif event.key == pygame.K_DOWN:
                    if activeText < 4:
                        if activeText == 1 and offenseText != '':
                            activeText += 1
                        elif activeText == 2 and defenseText != '':
                            activeText += 1
                        elif activeText == 3 and specialText != '':
                            activeText += 1

        if activeText == 1:
            cursor.update(offenseInput.x + font.size(offenseText)[0], offenseInput.y, offenseInput.height)
        elif activeText == 2:
            cursor.update(defenseInput.x + font.size(defenseText)[0], defenseInput.y, defenseInput.height)
        elif activeText == 3:
            cursor.update(specialInput.x + font.size(specialText)[0], specialInput.y, specialInput.height)
        elif activeText == 4:
            cursor.update(confirmationInput.x + font.size(confirmationText)[0], confirmationInput.y, confirmationInput.height)

        pygame.draw.rect(screen, color, offenseInput)
        pygame.draw.rect(screen, color, defenseInput)
        pygame.draw.rect(screen, color, specialInput)
        pygame.draw.rect(screen, color, confirmationInput)

        offenseDisplay = font.render(offenseText, True, (255, 255, 255))
        defenseDisplay = font.render(defenseText, True, (255, 255, 255))
        speicalDisplay = font.render(specialText, True, (255, 255, 255))

        screen.blit(offenseDisplay, (offenseInput.x, offenseInput.y))
        screen.blit(defenseDisplay, (defenseInput.x, defenseInput.y))
        screen.blit(speicalDisplay, (specialInput.x, specialInput.y))

        offenseInput.w = max(100, offenseDisplay.get_width() + 10)
        defenseInput.w = max(100, defenseDisplay.get_width() + 10)
        specialInput.w = max(100, speicalDisplay.get_width() + 10)

        if activeText == 4:
            confirmationDisplay = font.render(confirmationText, True, (255,255,255))
            screen.blit(confirmationDisplay, (confirmation.get_width() + 80, screen.get_height() - confirmationDisplay.get_height() - 30))
            confirmationInput.w = max(100, confirmationDisplay.get_width() + 10)

        cursor.draw(screen)

        pygame.display.flip()
            