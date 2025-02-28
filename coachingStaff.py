import pygame, sys

def kill_game():
    pygame.quit()
    sys.exit()

def inputStaff(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    offensiveCoordinator = font.render("Offensive Coordinator:", True, (255, 255, 255))
    defensiveCoordinator = font.render("Defensive Coordinator:", True, (255, 255, 255))
    specialTeamsCoordinator = font.render("Special Teams Coordinator:", True, (255, 255, 255))

    screen.blit(offensiveCoordinator, (0, 0))
    screen.blit(defensiveCoordinator, (0, 50))
    screen.blit(specialTeamsCoordinator, (0, 100))

    pygame.display.update()

    offenseInput = pygame.Rect(offensiveCoordinator.get_width(), -5, 140, 35)
    defenseInput = pygame.Rect(defensiveCoordinator.get_width(), 45, 140, 35)
    specialInput = pygame.Rect(specialTeamsCoordinator.get_width(), 95, 140, 35)

    color = pygame.Color('black')

    offenseText = ''
    defenseText = ''
    specialText = ''

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
                    else:
                        return

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
                else:
                    if activeText == 1:
                        offenseText += event.unicode
                    elif activeText == 2:
                        defenseText += event.unicode
                    elif activeText == 3:
                        specialText += event.unicode

        pygame.draw.rect(screen, color, offenseInput)
        pygame.draw.rect(screen, color, defenseInput)
        pygame.draw.rect(screen, color, specialInput)

        offenseDisplay = font.render(offenseText, True, (255, 255, 255))
        defenseDisplay = font.render(defenseText, True, (255, 255, 255))
        speicalDisplay = font.render(specialText, True, (255, 255, 255))

        screen.blit(offenseDisplay, (offenseInput.x + 5, offenseInput.y + 5))
        screen.blit(defenseDisplay, (defenseInput.x + 5, defenseInput.y + 5))
        screen.blit(speicalDisplay, (specialInput.x + 5, specialInput.y + 5))

        offenseInput.w = max(100, offenseDisplay.get_width() + 10)
        defenseInput.w = max(100, defenseDisplay.get_width() + 10)
        specialInput.w = max(100, speicalDisplay.get_width() + 10)

        pygame.display.flip()
            