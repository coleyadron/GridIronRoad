import pygame
import time

class TextCursor:
    def __init__(self, x, y, height):
        self.rect = pygame.Rect(x, y, 12, height)
        self.color = (255, 255, 255)
        self.blink_interval = 0.5
        self.last_blink = time.time()
        self.visible = True

    def update(self, x, y, height):
        self.rect.x = x
        self.rect.y = y
        self.rect.height = height
        if time.time() - self.last_blink > self.blink_interval:
            self.visible = not self.visible
            self.last_blink = time.time()

    def draw(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.color, self.rect)