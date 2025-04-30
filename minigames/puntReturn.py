import pygame
import sys
import time
from logic.defender import Defender
# import gridironRoad

def kill_game():
    pygame.quit()
    sys.exit()

def exec(screen):
    return puntReturn(screen)

def puntReturn(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    bgi = pygame.image.load("assets/images/blankField.PNG")
    # bgi = pygame.transform.scale(bgi, (1400, 1050))
    screen.blit(bgi, (0, 0))

    try:
        steelerOffense = pygame.image.load("assets/images/steelSprites/forwardOne.PNG").convert_alpha()
        steelerOffense = pygame.transform.scale(steelerOffense, (75, 75))

        bearDefense = pygame.image.load("assets/images/bearSprites/backwardOne.PNG").convert_alpha()
        bearDefense = pygame.transform.scale(bearDefense, (75, 75))

    except pygame.error as e:
        print("Error loading image:", e)
        steelerOffense = None
        bearDefense = None
    
    instructionText = font.render("Press SPACE to start the punt return, use arrow keys to move", True, (255, 255, 255))

    screen.blit(instructionText, (screen.get_width() / 2 - instructionText.get_width() / 2,
                                  screen.get_height() / 2 - instructionText.get_height() / 2))

    pygame.display.update()


    running = True
    miniGame = False
    win = None

    userX = screen.get_width() / 2
    userY = screen.get_height() - 150

    spriteWidth = 50
    spriteHeight = 75

    # defenseX = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    # defenseY = [110, 110, 110, 110, 110, 110, 110, 110, 110, 110]

    endzoneY = 50

    last_defender_time = 0
    defender_spawn_rate = 750
    defenders = []

    clock = pygame.time.Clock()

    while running:
        current_time = pygame.time.get_ticks()

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
                # elif event.key == pygame.K_SPACE and miniGame:
                #     if win:
                #         print("You won the mini game")
                #         running = False
                #         return True
                #     else:
                #         print("You lost the mini game")
                #         running = False
                #         return False

                if event.key == pygame.K_LEFT and miniGame and userX > 0:
                    userX -= spriteWidth
                    # print("LEFT action")
                elif event.key == pygame.K_RIGHT and miniGame and userX < screen.get_width() - spriteWidth:
                    userX += spriteWidth
                    # print("RIGHT action")
                elif event.key == pygame.K_UP and miniGame and userY > 0:
                    userY -= spriteHeight // 2
                    # print(userY)
                    # print("UP action")
                elif event.key == pygame.K_DOWN and miniGame and userY < screen.get_height() - spriteHeight:
                    userY += spriteHeight // 2
                    # print("DOWN action")
        
        if miniGame:
            screen.fill((0, 0, 0))

            if current_time - last_defender_time > defender_spawn_rate:
                defenders.append(Defender(screen.get_width(), bearDefense, userX=userX, userY=userY))
                last_defender_time = current_time
                defender_spawn_rate = max(300, defender_spawn_rate - 10)

            player_rect = pygame.Rect(userX, userY, spriteWidth, spriteHeight)

            for defender in defenders[:]:
                defender.update()
                if defender.is_offscreen(screen.get_height()):
                    defenders.remove(defender)
                elif defender.collides_with(player_rect):
                    time.sleep(.25)
                    screen.fill((0, 0, 0))
                    bgi = pygame.image.load("assets/images/blankField.PNG")
                    screen.blit(bgi, (0, 0))
                    instructionText = font.render("You were tackled", True, (255, 255, 255))

                    screen.blit(instructionText, (screen.get_width() / 2 - instructionText.get_width() / 2,
                                                screen.get_height() / 2 - instructionText.get_height() / 2))

                    pygame.display.update()

                    win = False
                    miniGame = False
                    running = False
                    time.sleep(1)
                    return False

            screen.fill((0, 0, 0))

            if win is None:
                screen.blit(bgi, (0, 0))

                pygame.draw.rect(screen, (11, 22, 42), (0, 0, screen.get_width(), 125))

                if steelerOffense:
                    screen.blit(steelerOffense, (userX, userY))
                else:
                    pygame.draw.rect(screen, (255, 0, 0), (userX, userY, spriteWidth, spriteHeight))
                
                for defender in defenders:
                    defender.draw(screen)

                pygame.display.flip()

            #check touchdown
            if userY <= endzoneY:
                time.sleep(.25)
                screen.fill((0, 0, 0))
                bgi = pygame.image.load("assets/images/blankField.PNG")
                screen.blit(bgi, (0, 0))
                instructionText = font.render("You scored a touchdown!", True, (255, 255, 255))

                screen.blit(instructionText, (screen.get_width() / 2 - instructionText.get_width() / 2,
                                            screen.get_height() / 2 - instructionText.get_height() / 2))

                pygame.display.update()

                win = True
                miniGame = False
                running = False
                time.sleep(1)
                return True
            
            # else:
            #     result_text = "TOUCHDOWN! You win!" if win else "TACKLED! You lose!"
            #     text = font.render(result_text, True, (0, 255, 0) if win else (255, 0, 0))
            #     screen.blit(text, (screen.get_width()/2 - text.get_width()/2, 
            #                     screen.get_height()/2 - text.get_height()/2))
            #     restart_text = font.render("Press SPACE to play again", True, (255, 255, 255))
            #     screen.blit(restart_text, (screen.get_width()/2 - restart_text.get_width()/2,
            #                             screen.get_height()/2 + 50))
            
            pygame.display.flip()
            clock.tick(60)
    

            # #edit defense positions
            # i = 0
            # while len(defenseX) > i:
            #     # negative = random.randint(0, 1)
            #     # if negative == 0:
            #     #     defenseX[i] -= random.random()
            #     # else:
            #     #     defenseX[i] += random.random()
            #     defenseX[i] += random.randint(-1, 1)
            #     defenseY[i] += 1
            #     i += 1

            # #endzone
            # pygame.draw.rect(screen, (0, 180, 0), (0, endzoneY, screen.get_width(), 100))
            # endzoneY += 1
            # #defense
            # i = 0
            # while len(defenseX) > i:
            #     if bearDefense:
            #         screen.blit(bearDefense, (defenseX[i], defenseY[i]))
            #         i += 1
            #     else:
            #         pygame.draw.rect(screen, (0, 0, 255), (defenseX[i], defenseY[i], spriteWidth, spriteHeight))
            #         i += 1
            # #user
            # if steelerOffense:
            #     screen.blit(steelerOffense, (userX, userY))
            # else:
            #     pygame.draw.rect(screen, (255, 0, 0), (userX, userY, spriteWidth, spriteHeight))

            # pygame.display.update()

            # #check if user is in endzone
            # if userY == endzoneY + 5:
            #     time.sleep(.25)
            #     screen.fill((0, 0, 0))
            #     instructionText = font.render("You scored a touchdown!", True, (255, 255, 255))

            #     screen.blit(instructionText, (screen.get_width() / 2 - instructionText.get_width() / 2,
            #                                 screen.get_height() / 2 - instructionText.get_height() / 2))

            #     pygame.display.update()

            #     win = True
            #     miniGame = False
            #     running = False
            #     time.sleep(1)
            #     return True

            # #check if user is tackled
            # i = 0
            # while len(defenseX) > i:
            #     if defenseX[i] <= userX and defenseX[i] + spriteWidth >= userX and defenseY[i] <= userY and defenseY[i] + spriteHeight >= userY:
            #         time.sleep(.25)
            #         screen.fill((0, 0, 0))
            #         instructionText = font.render("You were tackled", True, (255, 255, 255))

            #         screen.blit(instructionText, (screen.get_width() / 2 - instructionText.get_width() / 2,
            #                                     screen.get_height() / 2 - instructionText.get_height() / 2))

            #         pygame.display.update()

            #         win = False
            #         miniGame = False
            #         running = False
            #         time.sleep(1)
            #         return False
                    
            #     i += 1


def main():
    pygame.init()
    pygame.display.init()

    puntReturn(screen = pygame.display.set_mode((1400, 1050)))

if __name__ == "__main__":
    main()