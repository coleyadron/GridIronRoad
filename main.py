import pygame, sys
from screens import experienceSelection
from screens import draft
from screens import coachingStaff
from screens import teamSelection

if __name__ == "__main__":
    pygame.init()
    pygame.display.init()

info = pygame.display.Info()
screen = pygame.display.set_mode((1400, 1050))

pygame.display.set_caption("GridIron Road")
pygame.display.set_icon(pygame.image.load("assets/images/gridIronLogo.PNG"))

##Sets Font 
font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

img = pygame.image.load("assets/images/gridIronLogo.PNG").convert()

##Renders Text
textSurface = font.render("Press SPACE to Start Game", True, (255, 255, 255))

screen.blit(textSurface, (500, 725))
screen.blit(img, (360, 100))

pygame.display.update()

running = True

def kill_game():
    running = False
    pygame.quit()
    sys.exit()

mainScreen = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kill_game()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Game has been closed")
                kill_game()

            if event.key == pygame.K_SPACE and mainScreen:
                mainScreen = False
                # print("SPACE action, next screen")
                experienceSelection.selectExperience(screen)
                teamSelection.selectTeam(screen)
                coachingStaff.inputStaff(screen)
                draft.draftPlayers(screen)
                

pygame.quit()