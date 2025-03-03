import pygame
import gridironRoad

def selectTeam(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    team1 = font.render("Team 1", True, (255, 255, 255))
    team2 = font.render("Team 2", True, (255, 255, 255))
    team3 = font.render("Team 3", True, (255, 255, 255))

    screen.blit(team1, (0, 0))
    screen.blit(team2, (0, 50))
    screen.blit(team3, (0, 100))

    inputSelection = font.render("Select your team:", True, (255, 255, 255))

    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))

    pygame.display.update()

    teamOpen = True
    confirmSelection = False
    while teamOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN and teamOpen:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1 and not confirmSelection:
                    # print("Team 1 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your team: 1", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(team1, (0, 0))
                    screen.blit(team2, (0, 50))
                    screen.blit(team3, (0, 100))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))
                    pygame.display.update()
                
                elif event.key == pygame.K_2  or event.key == pygame.K_KP2 and not confirmSelection:
                    # print("Team 2 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your team: 2", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(team1, (0, 0))
                    screen.blit(team2, (0, 50))
                    screen.blit(team3, (0, 100))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))
                    pygame.display.update()

                elif event.key == pygame.K_3 or event.key == pygame.K_KP3 and not confirmSelection:
                    # print("Team 3 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your team: 3", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(team1, (0, 0))
                    screen.blit(team2, (0, 50))
                    screen.blit(team3, (0, 100))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))
                    pygame.display.update()
                
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER and confirmSelection:
                    # print("Team selection confirmed")
                    teamOpen = False
                    return
                if event.key == pygame.K_ESCAPE:
                    print("Game has been closed")
                    gridironRoad.killgame(screen)
                if event.key == pygame.K_BACKSPACE and confirmSelection:
                    # print("Team selection cancelled")
                    confirmSelection = False
                    
                    inputSelection = font.render("Select your team:", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(team1, (0, 0))
                    screen.blit(team2, (0, 50))
                    screen.blit(team3, (0, 100))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))
                    pygame.display.update()