import pygame

class Player:
    def __init__(self, x, y, width=50, height=75):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel_y = 0
        self.jumping = False
        self.sprite = None
        
        try:
            self.sprite = pygame.image.load("assets/images/steelSprites/rightFour.PNG").convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        except:
            print("Couldn't load player sprite - using rectangle instead")

    def jump(self, jump_strength=15):
        if not self.jumping:
            self.vel_y = -jump_strength
            self.jumping = True

    def update(self, gravity=1, ground_height=300):
        self.vel_y += gravity
        self.y += self.vel_y

        if self.y >= ground_height - self.height:
            self.y = ground_height - self.height
            self.vel_y = 0
            self.jumping = False

    def draw(self, screen, camera_x):
        if self.sprite:
            screen.blit(self.sprite, (self.x - camera_x, self.y))
        else:
            pygame.draw.rect(screen, (255, 0, 0), (self.x - camera_x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)