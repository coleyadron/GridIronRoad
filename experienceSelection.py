import pygame
import sys
import teamSelection

def kill_game():
    running = False
    pygame.quit()
    sys.exit()

def selectExperience(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    
    experience1 = font.render("Experience 1", True, (255, 255, 255))
    experience2 = font.render("Experience 2", True, (255, 255, 255))
    experience3 = font.render("Experience 3", True, (255, 255, 255))

    screen.blit(experience1, (500, 725))
    screen.blit(experience2, (500, 775))
    screen.blit(experience3, (500, 825))

    inputSelection = font.render("Select your experience:", True, (255, 255, 255))

    screen.blit(inputSelection, (500, 675))

    pygame.display.update()

    experienceOpen = True
    confirmSelection = False
    while experienceOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
            if event.type == pygame.KEYDOWN and experienceOpen:
                if event.key == pygame.K_1:
                    ##Re-Renders text to show selection in red
                    experience1 = font.render("Experience 1", True, (255, 0, 0))
                    experience2 = font.render("Experience 2", True, (255, 255, 255))
                    experience3 = font.render("Experience 3", True, (255, 255, 255))

                    screen.blit(experience1, (500, 725))
                    screen.blit(experience2, (500, 775))
                    screen.blit(experience3, (500, 825))
                    pygame.display.update()
                    print("Experience 1 selected")
                    confirmSelection = True
                elif event.key == pygame.K_2:
                    ##Re-Renders text to show selection in red
                    experience1 = font.render("Experience 1", True, (255, 255, 255))
                    experience2 = font.render("Experience 2", True, (255, 0, 0))
                    experience3 = font.render("Experience 3", True, (255, 255, 255))

                    screen.blit(experience1, (500, 725))
                    screen.blit(experience2, (500, 775))
                    screen.blit(experience3, (500, 825))
                    pygame.display.update()
                    print("Experience 2 selected")
                    confirmSelection = True
                elif event.key == pygame.K_3:
                    ##Re-Renders text to show selection in red
                    experience1 = font.render("Experience 1", True, (255, 255, 255))
                    experience2 = font.render("Experience 2", True, (255, 255, 255))
                    experience3 = font.render("Experience 3", True, (255, 0, 0))

                    screen.blit(experience1, (500, 725))
                    screen.blit(experience2, (500, 775))
                    screen.blit(experience3, (500, 825))
                    pygame.display.update()
                    print("Experience 3 selected")
                    confirmSelection = True
                if event.key == pygame.K_RETURN and confirmSelection:
                    experienceOpen = False
                    print("Enter action, next screen")
                    teamSelection.selectTeam(screen)
                if event.key == pygame.K_ESCAPE:
                    print("Game has been closed")
                    kill_game()