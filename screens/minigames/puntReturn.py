import pygame, sys

def kill_game():
    pygame.quit()
    sys.exit()

def puntReturn(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    
    instructionText = font.render("Press SPACE to start the punt return, use arrow keys to move", True, (255, 255, 255))

    screen.blit(instructionText, (screen.get_width() / 2 - instructionText.get_width() / 2,
                                  screen.get_height() / 2 - instructionText.get_height() / 2))

    pygame.display.update()


    running = True
    miniGame = False

    userX = screen.get_width() / 2
    userY = screen.get_height() - 150

    userWidth = 50
    userHeight = 75

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Game has been closed")
                    kill_game()

                if event.key == pygame.K_SPACE and not miniGame:
                    miniGame = True
                if event.key == pygame.K_LEFT and miniGame and userX > 0:
                    userX -= userWidth
                    # print("LEFT action")
                elif event.key == pygame.K_RIGHT and miniGame and userX < screen.get_width() - userWidth:
                    userX += userWidth
                    # print("RIGHT action")
                elif event.key == pygame.K_UP and miniGame and userY > 0:
                    userY -= userHeight
                    # print("UP action")
                elif event.key == pygame.K_DOWN and miniGame and userY < screen.get_height() - userHeight:
                    userY += userHeight
                    # print("DOWN action")
        
        if miniGame:
            screen.fill((0, 0, 0))
            #user
            pygame.draw.rect(screen, (255, 0, 0), (userX, userY, userWidth, userHeight))
            pygame.display.update()


def main():
    pygame.init()
    pygame.display.init()

    puntReturn(screen = pygame.display.set_mode((1400, 1050)))

main()