import pygame
import time

class TextCursor:
    def __init__(self, x, y, fontSize, height, color=(255, 255, 255), blink_speed=0.5):
        self.rect = pygame.Rect(x, y, fontSize, height)  # Thin rectangle for cursor
        self.color = color
        self.blink_speed = blink_speed
        self.last_blink = time.time()
        self.visible = True
        self.active = False

    def update(self, x, y, height):
        """Update cursor position and size"""
        self.rect.x = x
        self.rect.y = y
        self.rect.height = height
        
        # Handle blinking only when active
        if self.active and time.time() - self.last_blink > self.blink_speed:
            self.visible = not self.visible
            self.last_blink = time.time()

    def draw(self, surface):
        """Draw cursor if visible and active"""
        if self.active and self.visible:
            pygame.draw.rect(surface, self.color, self.rect)

    def activate(self):
        """Activate the cursor (make it visible and blinking)"""
        self.active = True
        self.visible = True
        self.last_blink = time.time()

    def deactivate(self):
        """Deactivate the cursor (hide it)"""
        self.active = False
        self.visible = False

    def setX(self, x):
        """Set cursor's x position"""
        self.rect.x = x

    def setY(self, y):
        """Set cursor's y position"""
        self.rect.y = y

    def getX(self):
        """Get cursor's x position"""
        return self.rect.x
    
    def getY(self):
        """Get cursor's y position"""
        return self.rect.y