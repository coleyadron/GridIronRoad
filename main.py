import pygame
from screens import experienceSelection
from screens import draft
from screens import coachingStaff
from screens import teamSelection
import gridironRoad
# from screens.minigames import puntReturn

EXPERIENCE = None
TEAM = None
STAFF = None
DRAFT = None

# def retrieveState():
#     state = {
#         "started": True,
#         "experience": EXPERIENCE,
#         "team": TEAM,
#         "staff": STAFF,
#         "draft": DRAFT
#     }
#     print(state)
#     return state

def main():
    global EXPERIENCE, TEAM, STAFF, DRAFT

    pygame.init()
    pygame.display.init()

    # info = pygame.display.Info()
    screen = pygame.display.set_mode((1300, 950))

    pygame.display.set_caption("GridIron Road")
    pygame.display.set_icon(pygame.image.load("assets/images/gridIronLogo.PNG"))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    mainScreenLogo = pygame.image.load("assets/images/giLogoBorder.png").convert_alpha()
    mainScreenImage = pygame.image.load("assets/images/startScreen.png").convert()
    startText = font.render("Press SPACE to Start Game", True, (255, 255, 255))

    screen.blit(mainScreenImage, (screen.get_width() / 2 - mainScreenImage.get_width() / 2,
                                screen.get_height() / 3 - mainScreenImage.get_height() / 3))

    screen.blit(mainScreenLogo, (screen.get_width() / 2 - mainScreenLogo.get_width() / 2, 
                                screen.get_height() / 10 - mainScreenLogo.get_height() / 10))

    screen.blit(startText, (screen.get_width() / 2 - startText.get_width() / 2, 
                            screen.get_height() - startText.get_height() - 30))

    pygame.display.update()

    running = True

    # def kill_game():
    #     pygame.quit()
    #     sys.exit()

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
                    EXPERIENCE = experienceSelection.selectExperience(screen)
                    # print(EXPERIENCE)
                    gridironRoad.updateGlobalState("experience", EXPERIENCE)

                    TEAM = teamSelection.selectTeam(screen)
                    # print(TEAM)
                    gridironRoad.updateGlobalState("team", TEAM)

                    STAFF = coachingStaff.inputStaff(screen)
                    # print(STAFF)
                    gridironRoad.updateGlobalState("staff", STAFF)

                    DRAFT = draft.draft(screen)
                    # print(DRAFT)
                    gridironRoad.updateGlobalState("draft", DRAFT)

if __name__ == "__main__":
    main()