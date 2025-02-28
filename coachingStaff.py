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


    staffOpen = True
    while staffOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
            if event.type == pygame.KEYDOWN and staffOpen:
                if event.key == pygame.K_ESCAPE:
                    print("Game has been closed")
                    kill_game()