import pygame
import sys
import time
import random
# import gridironRoad

def kill_game():
    pygame.quit()
    sys.exit()

def exec(screen):
    return puntReturn(screen)

def puntReturn(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    
    instructionText = font.render("Press SPACE to start the punt return, use arrow keys to move", True, (255, 255, 255))

    screen.blit(instructionText, (screen.get_width() / 2 - instructionText.get_width() / 2,
                                  screen.get_height() / 2 - instructionText.get_height() / 2))

    pygame.display.update()


    running = True
    miniGame = False
    win = False

    userX = screen.get_width() / 2
    userY = screen.get_height() - 150

    spriteWidth = 50
    spriteHeight = 75

    defenseX = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    defenseY = [110, 110, 110, 110, 110, 110, 110, 110, 110, 110]

    endzoneY = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
                # gridironRoad.killgame(screen)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # print("Game has been closed")
                    kill_game()
                    # gridironRoad.killgame(screen)

                if event.key == pygame.K_SPACE and not miniGame:
                    miniGame = True
                elif event.key == pygame.K_SPACE and miniGame:
                    if win:
                        print("You won the mini game")
                        running = False
                        return True
                    else:
                        print("You lost the mini game")
                        running = False
                        return False

                if event.key == pygame.K_LEFT and miniGame and userX > 0:
                    userX -= spriteWidth
                    # print("LEFT action")
                elif event.key == pygame.K_RIGHT and miniGame and userX < screen.get_width() - spriteWidth:
                    userX += spriteWidth
                    # print("RIGHT action")
                # elif event.key == pygame.K_UP and miniGame and userY > 0:
                #     userY -= spriteHeight
                #     # print("UP action")
                # elif event.key == pygame.K_DOWN and miniGame and userY < screen.get_height() - spriteHeight:
                #     userY += spriteHeight
                #     # print("DOWN action")
        
        if miniGame:
            screen.fill((0, 0, 0))

            #edit defense positions
            i = 0
            while len(defenseX) > i:
                # negative = random.randint(0, 1)
                # if negative == 0:
                #     defenseX[i] -= random.random()
                # else:
                #     defenseX[i] += random.random()
                defenseX[i] += random.randint(-1, 1)
                defenseY[i] += 1
                i += 1

            #endzone
            pygame.draw.rect(screen, (0, 180, 0), (0, endzoneY, screen.get_width(), 100))
            endzoneY += 1
            #defense
            i = 0
            while len(defenseX) > i:
                pygame.draw.rect(screen, (0, 0, 255), (defenseX[i], defenseY[i], spriteWidth, spriteHeight))
                i += 1
            #user
            pygame.draw.rect(screen, (255, 0, 0), (userX, userY, spriteWidth, spriteHeight))

            pygame.display.update()

            #check if user is in endzone
            if userY == endzoneY + 5:
                time.sleep(.25)
                screen.fill((0, 0, 0))
                instructionText = font.render("You scored a touchdown!", True, (255, 255, 255))

                screen.blit(instructionText, (screen.get_width() / 2 - instructionText.get_width() / 2,
                                            screen.get_height() / 2 - instructionText.get_height() / 2))

                pygame.display.update()

                win = True
                miniGame = False
                running = False
                time.sleep(1)
                return True

            #check if user is tackled
            i = 0
            while len(defenseX) > i:
                if defenseX[i] <= userX and defenseX[i] + spriteWidth >= userX and defenseY[i] <= userY and defenseY[i] + spriteHeight >= userY:
                    time.sleep(.25)
                    screen.fill((0, 0, 0))
                    instructionText = font.render("You were tackled", True, (255, 255, 255))

                    screen.blit(instructionText, (screen.get_width() / 2 - instructionText.get_width() / 2,
                                                screen.get_height() / 2 - instructionText.get_height() / 2))

                    pygame.display.update()

                    win = False
                    miniGame = False
                    running = False
                    time.sleep(1)
                    return False
                    
                i += 1


# def main():
#     pygame.init()
#     pygame.display.init()

#     puntReturn(screen = pygame.display.set_mode((1400, 1050)))

# main()