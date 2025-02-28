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

    screen.blit(experience1, (0, 0))
    screen.blit(experience2, (0, 50))
    screen.blit(experience3, (0, 100))

    inputSelection = font.render("Select your experience:", True, (255, 255, 255))   

    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))

    pygame.display.update()

    experienceOpen = True
    confirmSelection = False
    while experienceOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
            if event.type == pygame.KEYDOWN and experienceOpen:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1 and not confirmSelection:
                    print("Experience 1 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your experience: 1", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(experience1, (0, 0))
                    screen.blit(experience2, (0, 50))
                    screen.blit(experience3, (0, 100))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))
                    pygame.display.update()

                elif event.key == pygame.K_2  or event.key == pygame.K_KP2 and not confirmSelection:
                    print("Experience 2 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your experience: 2", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(experience1, (0, 0))
                    screen.blit(experience2, (0, 50))
                    screen.blit(experience3, (0, 100))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))
                    pygame.display.update()

                elif event.key == pygame.K_3 or event.key == pygame.K_KP3 and not confirmSelection:
                    print("Experience 3 selected")
                    confirmSelection = True

                    inputSelection = font.render("Select your experience: 3", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(experience1, (0, 0))
                    screen.blit(experience2, (0, 50))
                    screen.blit(experience3, (0, 100))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))
                    pygame.display.update()

                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER and confirmSelection:
                    experienceOpen = False
                    print("Enter action, next screen")
                    teamSelection.selectTeam(screen)
                if event.key == pygame.K_ESCAPE:
                    print("Game has been closed")
                    kill_game()
                if event.key == pygame.K_BACKSPACE and confirmSelection:
                    confirmSelection = False
                    print("Backspace action, reselect experience")

                    inputSelection = font.render("Select your experience:", True, (255, 255, 255))
                    screen.fill((0, 0, 0))
                    screen.blit(experience1, (0, 0))
                    screen.blit(experience2, (0, 50))
                    screen.blit(experience3, (0, 100))
                    screen.blit(inputSelection, (0, screen.get_height() - inputSelection.get_height() - 75))
                    pygame.display.update()