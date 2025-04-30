import pygame
import random

class Defender:
    def __init__(self, screen_width, image=None, x=0, y=125):
        self.x = x
        self.y = y
        self.speed = 5
        self.width = 50
        self.height = 75
        self.image = image
        if x == 0:
            mean = 13
            stddev = 8
            x_location = random.gauss(mean, stddev)
            x_location = max(0, min(27, int(x_location)))
            self.x = x_location * 50
            self.speed = random.randint(3, 6)
            self.speed = random.randint(4, 8)

    def update(self):
        self.y += self.speed

    def update_left(self):
        self.x -= self.speed
    
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