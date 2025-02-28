import pygame 
import sys

def kill_game():
    running = False
    pygame.quit()
    sys.exit()

def fieldGoal(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    pygame.display.update()

    width = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("charging kick")
                    width += 1

    pygame.quit() 