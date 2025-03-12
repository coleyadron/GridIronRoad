import pygame, sys
import json

def retrieveGameState():
    import main

    state = main.retrieveState()
    return state

def saveGameState(data):
    try:
        with open("json/userState.json", "w") as f:
            pass
    except Exception as e:
        print("Error saving game state: ", e)
    print("Game is saved")

def killgame(screen):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    copy_screen = screen.copy()

    confirmationText = font.render("Are you sure you want to quit the game?", True, (0, 0, 0))
    yesText = font.render("Press SPACE to exit", True, (0, 0, 0))
    
    pygame.draw.rect(screen, (225, 225, 225), (screen.get_width() / 2 -  confirmationText.get_width() * 1.25 / 2,
                                               screen.get_height() / 4,
                                               confirmationText.get_width() * 1.25, screen.get_height() * .5))

    screen.blit(confirmationText, (screen.get_width() / 2 - confirmationText.get_width() / 2, screen.get_height() * .33))
    
    screen.blit(yesText, (screen.get_width() / 2 - yesText.get_width() / 2, screen.get_height() * .66))
        
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                data = retrieveGameState()
                saveGameState(data)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    data = retrieveGameState()
                    saveGameState(data)
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_ESCAPE:
                    screen.blit(copy_screen, (0, 0))
                    pygame.display.update()
                    return