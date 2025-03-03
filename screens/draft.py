import pygame
import gridironRoad

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
                gridironRoad.killgame(screen)
            if event.type == pygame.KEYDOWN and draftOpen:
                if event.key == pygame.K_ESCAPE:
                    gridironRoad.killgame(screen)