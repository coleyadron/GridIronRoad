import pygame 
import sys

def kill_game():
    running = False
    pygame.quit()
    sys.exit()

def fieldGoal(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    instruction = font.render("Hold 'SPACE' to charge kick ", True, (255, 255, 255))
    screen.blit(instruction, (0, 600))

    pygame.display.update()

    width = 0
    confirm = False
    switch = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not confirm:
            if width <= 1000 and switch == False:
                width += 2
                if width == 1000:
                    switch = True
                    width -= 1
                    print("Switched True")
            if switch == True:
                print("go back ")
                width -= 3 
                if width == 1:
                    switch = False
                    print("Switched False")

         
        pygame.draw.rect(screen, (255, 0, 0), (50, 650, width, 50))
        pygame.display.update()

    pygame.quit() 

def main():
    pygame.init()
    pygame.display.init()
    fieldGoal(screen = pygame.display.set_mode((1400, 1050)))

main()