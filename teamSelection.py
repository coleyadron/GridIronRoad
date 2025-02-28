import pygame
import sys

def kill_game():
    running = False
    pygame.quit()
    sys.exit()

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