import pygame, sys
from screens import experienceSelection
from screens import draft
from screens import coachingStaff
from screens import teamSelection
import gridironRoad
# from screens.minigames import puntReturn

if __name__ == "__main__":
    pygame.init()
    pygame.display.init()

info = pygame.display.Info()
screen = pygame.display.set_mode((1400, 1050))

pygame.display.set_caption("GridIron Road")
pygame.display.set_icon(pygame.image.load("assets/images/gridIronLogo.PNG"))

font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

mainScreenImg = pygame.image.load("assets/images/gridIronLogo.PNG").convert()
startText = font.render("Press SPACE to Start Game", True, (255, 255, 255))

screen.blit(mainScreenImg, (screen.get_width() / 2 - mainScreenImg.get_width() / 2, 
                            screen.get_height() / 3 - mainScreenImg.get_height() / 3))

screen.blit(startText, (screen.get_width() / 2 - startText.get_width() / 2, 
                        screen.get_height() - startText.get_height() - 100))

pygame.display.update()

running = True

def kill_game():
    pygame.quit()
    sys.exit()

mainScreen = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gridironRoad.killgame(screen)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # print("Game has been closed")
                gridironRoad.killgame(screen)

            if event.key == pygame.K_SPACE and mainScreen:
                mainScreen = False
                # print("SPACE action, next screen")
                experienceSelection.selectExperience(screen)
                teamSelection.selectTeam(screen)
                coachingStaff.inputStaff(screen)
                draft.draft(screen)
                

pygame.quit()