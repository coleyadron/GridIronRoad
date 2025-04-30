import pygame
import sys
import random
import time

def exec(screen):
    blockPass(screen)

def blockPass(screen):
    # Initialize pygame if not already initialized
    if not pygame.get_init():
        pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 1400, 1050

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # Game variables
    clock = pygame.time.Clock()
    FPS = 60
    game_time = 10  # seconds
    start_time = pygame.time.get_ticks()
    game_active = True
    caught = False

    BGI = pygame.image.load("assets/images/blankField.PNG").convert()
    ball_img = pygame.image.load("assets/images/football.png").convert_alpha()
    hands_img = pygame.image.load("assets/images/hands.png").convert_alpha()
    hands_img = pygame.transform.scale(hands_img, (200, 200))

    ball_rect = ball_img.get_rect()
    ball_rect.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed = [random.choice([-5, 5]), random.choice([-5, 5])]

    hands_rect = hands_img.get_rect()
    hands_rect.center = (WIDTH // 2, HEIGHT - 50)
    hands_speed = 7

    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    instructions = font.render("Use arrow keys to move the hands and block the ball!", True, WHITE)

    def show_message(message, color=BLACK):
        """Display a message on the screen"""
        text = font.render(message, True, color)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)
        pygame.display.flip()

    # Main game loop
    running = True
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
  
        # Clear screen
        screen.fill(WHITE)
        screen.blit(BGI, (0, 0))
        
        if game_active:
            # Calculate remaining time
            current_time = pygame.time.get_ticks()
            elapsed_seconds = (current_time - start_time) // 1000
            remaining_time = max(0, game_time - elapsed_seconds)
            
            # Move ball
            ball_rect.x += ball_speed[0]
            ball_rect.y += ball_speed[1]
            
            # Ball collision with walls
            if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
                ball_speed[0] *= -1
            if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
                ball_speed[1] *= -1
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and hands_rect.left > 0:
                hands_rect.x -= hands_speed
            if keys[pygame.K_RIGHT] and hands_rect.right < WIDTH:
                hands_rect.x += hands_speed
            if keys[pygame.K_UP] and hands_rect.top > 0:
                hands_rect.y -= hands_speed
            if keys[pygame.K_DOWN] and hands_rect.bottom < HEIGHT:
                hands_rect.y += hands_speed
            
            # Draw game elements
            screen.blit(BGI, (0, 0)) 
            screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT - 100))
            screen.blit(ball_img, ball_rect)
            screen.blit(hands_img, hands_rect)
            
            # Display timer
            timer_text = font.render(f"Time: {remaining_time}", True, WHITE)
            screen.blit(timer_text, (10, 10))
            
            # Check if time is up
            if remaining_time <= 0:
                game_active = False
                # Check if hands are on the ball
                if hands_rect.colliderect(ball_rect):
                    caught = True
        else:
            if caught:
                show_message("Success! You blocked the ball!", GREEN)
                time.sleep(1.5)
                running = False
            else:
                show_message("Missed! They caught the ball!", RED)
                time.sleep(1.5)
                running = False
        
        pygame.display.flip()
        clock.tick(FPS)

    return caught

if __name__ == "__main__":
    result = blockPass(screen = pygame.display.set_mode((1400, 1050)))
    print(f"Player caught the ball: {result}")