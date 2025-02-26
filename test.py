##This is a test file

import pygame

pygame.init()

screen = pygame.display.set_mode((1400, 1050))

##Sets Font 
font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

img = pygame.image.load("assets/images/gridIronLogo.PNG").convert()

##Renders Text
textSurface = font.render("Start Game", True, (255, 255, 255))

screen.blit(textSurface, (560, 725))
screen.blit(img, (360, 100))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()