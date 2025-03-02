import pygame, sys
# import draft

def kill_game():
    pygame.quit()
    sys.exit()

def inputStaff(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    offensiveCoordinator = font.render("Offensive Coordinator: ", True, (255, 255, 255))
    defensiveCoordinator = font.render("Defensive Coordinator: ", True, (255, 255, 255))
    specialTeamsCoordinator = font.render("Special Teams Coordinator: ", True, (255, 255, 255))
    confirmation = font.render("Are these names correct: ", True, (0,0,0))


    screen.blit(offensiveCoordinator, (0, 0))
    screen.blit(defensiveCoordinator, (0, 50))
    screen.blit(specialTeamsCoordinator, (0, 100))

    offenseInput = pygame.Rect(offensiveCoordinator.get_width(), 0, 140, 35)
    defenseInput = pygame.Rect(defensiveCoordinator.get_width(), 50, 140, 35)
    specialInput = pygame.Rect(specialTeamsCoordinator.get_width(), 100, 140, 35)
    confirmationInput = pygame.Rect(confirmation.get_width(), screen.get_height() - confirmation.get_height() - 75, 140, 35)

    pygame.display.update()

    color = pygame.Color('black')

    offenseText = ''
    defenseText = ''
    specialText = ''
    confirmationText = ''

    activeText = 1

    staffOpen = True
    while staffOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
            if event.type == pygame.KEYDOWN and staffOpen:
                if event.key == pygame.K_RETURN:
                    if activeText < 3:
                        activeText += 1
                    elif activeText == 3:
                        activeText += 1

                        confirmation = font.render("Are these names correct: ", True, (255, 255, 255))
                        screen.blit(confirmation, (0, screen.get_height() - confirmation.get_height() - 75))
                        pygame.display.flip()

                    else:
                        print(confirmationText)
                        print(confirmationText.upper())
                        if confirmationText.upper() == 'YES':
                            print("YES CHECK")
                            staffOpen = False
                            return
                            # draft.draft(screen)
                        elif confirmationText.upper() == 'NO':
                            print("NO CHECK")
                            return
                        else:
                            print("RESET")
                            confirmationText = ''

                if event.key == pygame.K_ESCAPE:
                    print("Game has been closed")
                    kill_game()

                if event.key == pygame.K_BACKSPACE:
                    if activeText == 1:
                        offenseText = offenseText[:-1]
                    elif activeText == 2:
                        defenseText = defenseText[:-1]
                    elif activeText == 3:
                        specialText = specialText[:-1]
                    elif activeText == 4:
                        confirmationText = confirmationText[:-1]
                else:
                    if activeText == 1:
                        offenseText += event.unicode
                    elif activeText == 2:
                        defenseText += event.unicode
                    elif activeText == 3:
                        specialText += event.unicode
                    elif activeText == 4:
                        confirmationText += event.unicode

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
            screen.blit(confirmationDisplay, (confirmation.get_width(), screen.get_height() - confirmationDisplay.get_height() - 75))
            confirmationInput.w = max(100, confirmationDisplay.get_width() + 10)


        pygame.display.flip()
            