import pygame
import random

class Defender:
    def __init__(self, screen_width, image=None, x=0, y=125, userX=0, userY=0):
        self.x = x
        self.y = y
        self.speed = 5
        self.width = 50
        self.height = 75
        self.image = image
        if x == 0:
            self.initial_for_punt(screen_width, userX, userY)

    def initial_for_punt(self, screen_width, userX, userY):
        # print("reset ", userX)
            mean = userX
            stddev = screen_width / 10
            x_location = random.gauss(mean, stddev)
            # x_location = max(0, min(27, int(x_location)))
            self.x = x_location
            self.speed = random.randint(4, 8)

            if userY < 300 and abs(self.x - userX) < 200:
                # print("reset y")
                pos_neg = random.choice([-1, 1])
                if pos_neg == -1:
                    self.x = userX - random.randint(60, 300)
                else:
                    self.x = userX + random.randint(60, 300)

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