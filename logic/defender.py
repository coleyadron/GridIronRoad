import pygame
import random

class Defender:
    def __init__(self, screen_width, image=None):
        self.x = random.randint(0, screen_width - 50)
        self.y = 125
        self.speed = random.randint(2, 5)
        self.width = 50
        self.height = 75
        self.image = image

    def update(self):
        self.y += self.speed
    
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def is_offscreen(self, screen_height):
        return self.y > screen_height
    
    def collides_with(self, player_rect):
        defender_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return defender_rect.colliderect(player_rect)