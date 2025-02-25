##This is a test file

import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 800))

##Sets Font 
font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 20)

img = pygame.image.load("assets/images/gridIronLogo.PNG").convert()

##Renders Text
textSurface = font.render("Start Game", True, (255, 255, 255))

screen.blit(textSurface, (400, 300))
screen.blit(img, (0, 0))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()