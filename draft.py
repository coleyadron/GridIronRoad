import pygame, sys

def kill_game():
    pygame.quit()
    sys.exit()

def draft(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    draft = font.render("Draft a player: ", True, (255, 255, 255))
    screen.blit(draft, (0, 0))

    pygame.display.update()

    draftOpen = True
    while draftOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
            if event.type == pygame.KEYDOWN and draftOpen:
                if event.key == pygame.K_ESCAPE:
                    kill_game()