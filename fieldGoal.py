import random
import pygame 
import sys

def kill_game():
    running = False
    pygame.quit()
    sys.exit()

def fieldGoal(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    instruction = font.render("Hold 'SPACE' to charge kick. Press 'SPACE' to enter kick", True, (255, 255, 255))
    screen.blit(instruction, (0, 600))

    pygame.draw.rect(screen, (45, 45, 45), (50, 650, 1050, 50))
    #Draws Space of charge bar
    success = random.randint(450, 800)
    print(success)
    pygame.draw.rect(screen, (255, 0, 0), (success, 650, 150, 50))
    pygame.display.update()

    width = 0
    confirm = False
    switch = False
    running = True
    kicked = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not confirm:
            if width <= 1050 and switch == False:
                width += 4
                if width >= 1050:
                    switch = True
                    print("Switched True")
            elif switch:
                width -= 5
                if width <= 0:
                    switch = False
                    print("Switched False")
        elif not keys[pygame.K_SPACE] and not kicked:
            if width > 0:
                width -= 2
                confirm = True
        if keys[pygame.K_SPACE] and confirm:
            if width > success - 50 and width < success + 100:
                ## -50 and +150 is to account for the moved y position of the power bar
                print("Success!")
                print(width)
            else:
                print("Fail!")
                print(width)
            kicked = True 

            
        screen.fill((0, 0, 0))
        screen.blit(instruction, (0,600))
        pygame.draw.rect(screen, (45, 45, 45), (50, 650, 1050, 50))
        pygame.draw.rect(screen, (255, 255, 0), (success, 650, 100, 50))
        pygame.draw.rect(screen, (255, 0, 0), (50, 650, width, 50))
        pygame.display.update() 

    pygame.quit() 

def main():
    pygame.init()
    pygame.display.init()
    fieldGoal(screen = pygame.display.set_mode((1400, 1050)))

main()