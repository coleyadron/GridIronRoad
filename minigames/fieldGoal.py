import random
import pygame 
import sys

def kill_game():
    pygame.quit()
    sys.exit()

def exec(screen):
    return fieldGoal(screen)

def fieldGoal(screen):
    screen.fill((0, 0, 0))
    BGI = pygame.image.load("assets/images/fieldGoal.png").convert()
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 30)
    football_img = pygame.image.load("assets/images/football.png").convert_alpha()
    football_img = pygame.transform.smoothscale(football_img, (45, 45))
    screen.blit(football_img, (700, 915))
    instruction = font.render("Hold 'SPACE' to charge kick. Press 'SPACE' to enter kick", True, (255, 255, 255))
    screen.blit(instruction, (0, 952))
    screen.blit(BGI, (0, 0))

    pygame.draw.rect(screen, (45, 45, 45), (150, 990, 1050, 50))
    #Draws Space of charge bar
    success = random.randint(550, 870)
    print(success)
    pygame.draw.rect(screen, (255, 0, 0), (success, 990, 150, 50))
    pygame.display.update()

    width = 0
    confirm = False
    switch = False
    running = True
    kicked = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill_game()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not confirm:
            if width <= 1050 and switch == False:
                width += 4
                if width >= 1050:
                    switch = True
                    print("Switched True")
            elif switch:
                width -= 5
                if width <= 0:
                    switch = False
                    print("Switched False")
        elif not keys[pygame.K_SPACE] and not kicked:
            if width > 0:
                width -= 2
                confirm = True
        if keys[pygame.K_SPACE] and confirm:
            if width > success - 150 and width < success + 50:
                ## -50 and +150 is to account for the moved y position of the power bar
                print("Success!")
                print(width)
                animate_field_goal_success(screen, football_img) 
                pygame.time.delay(1000)
                return True
            else:
                print("Fail!") 
                print(width)
                animate_field_goal_fail(screen, football_img)
                pygame.time.delay(1000)
                return False
            kicked = True 

            
        screen.fill((0, 0, 0))
        screen.blit(BGI, (0, 0))
        screen.blit(instruction, (50,952))
        pygame.draw.rect(screen, (45, 45, 45), (150, 987, 1050, 55))
        pygame.draw.rect(screen, (255, 255, 0), (success, 987, 100, 55))
        pygame.draw.rect(screen, (255, 0, 0), (150, 990, width, 50))
        pygame.display.update() 

    pygame.quit() 
        
def animate_field_goal_success(screen, football_img):

    # Animation parameters
    BGI = pygame.image.load("assets/images/fieldGoal.png").convert()
    duration = 2.0  # seconds
    fps = 60
    total_frames = int(duration * fps)
    target_height = 300
    font2 = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    
    # Starting position (at kicker's foot)
    start_x, start_y = 700, 915
    current_y = start_y
    
    # Store original football size
    original_width = football_img.get_width()
    original_height = football_img.get_height()
    
    # Draw initial frame
    screen.blit(BGI, (0, 0))
    pygame.display.flip()
    pygame.time.delay(500)  # Pause before kick
    
    clock = pygame.time.Clock()

    text = font2.render("Success!", True, (255, 0, 0))
    screen.blit(text, (1050, 100))

    for frame in range(total_frames):
        progress = frame / total_frames  # 0 to 1
        
        # Parabolic vertical movement (up then down slightly)
        if progress < 0.8:  # Rising phase
            y_progress = progress / 0.8
            current_y = start_y - (start_y - target_height) * (1 - (1 - y_progress)**2)
        else:  # Falling phase
            fall_progress = (progress - 0.8) / 0.2
            current_y = target_height + 50 * fall_progress**2
        
        # Perspective scaling (smaller as it goes higher)
        scale = 1.0 - (0.7 * progress)  # Reduce size by up to 70%
        scale = max(0.3, scale)  # Don't let it get too small
        
        # Calculate new size
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        
        # Scale the football
        scaled_football = pygame.transform.smoothscale(football_img, (new_width, new_height))
        
        # Position (centered horizontally)
        ball_rect = scaled_football.get_rect(center=(start_x, current_y))
        
        # Draw everything
        screen.blit(BGI, (0, 0))
        text = font2.render("Success!", True, (255, 0, 0))
        screen.blit(text, (640, 975))
        screen.blit(scaled_football, ball_rect)
        
        pygame.display.flip()
        clock.tick(fps)
    
    pygame.time.delay(500)  # Pause at end

def animate_field_goal_fail(screen, football_img):

    # Animation parameters
    BGI = pygame.image.load("assets/images/fieldGoal.png").convert()
    duration = 2.0  # seconds
    fps = 60
    total_frames = int(duration * fps)
    target_height = 300
    font2 = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    
    # Starting position (at kicker's foot)
    start_x, start_y = 700, 915
    current_y = start_y
    current_x = start_x
    
    # Store original football size
    original_width = football_img.get_width()
    original_height = football_img.get_height()
    
    # Draw initial frame
    screen.blit(BGI, (0, 0))
    pygame.display.flip()
    pygame.time.delay(500)  # Pause before kick
    
    clock = pygame.time.Clock()
    text = font2.render("Missed!", True, (255, 0, 0))
    screen.blit(text, (1000, 100))

    for frame in range(total_frames):
        progress = frame / total_frames  # 0 to 1
        
        # Parabolic vertical movement (up then down slightly)
        if progress < 0.8:  # Rising phase
            y_progress = progress / 0.8
            x_progress = progress / 0.8
            current_x = start_x + (start_x - 900) * (1 - (1 - x_progress)**2)
            current_y = start_y - (start_y - target_height) * (1 - (1 - y_progress)**2)
        else:  # Falling phase
            fall_progress = (progress - 0.8) / 0.2
            current_y = target_height + 50 * fall_progress**2
        
        # Perspective scaling (smaller as it goes higher)
        scale = 1.0 - (0.7 * progress)  # Reduce size by up to 70%
        scale = max(0.3, scale)  # Don't let it get too small
        
        # Calculate new size
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        
        # Scale the football
        scaled_football = pygame.transform.smoothscale(football_img, (new_width, new_height))
        
        # Position (centered horizontally)
        ball_rect = scaled_football.get_rect(center=(current_x, current_y))
        
        # Draw everything
        screen.blit(BGI, (0, 0))
        text = font2.render("Missed!", True, (255, 0, 0))
        screen.blit(text, (640, 975))
        screen.blit(scaled_football, ball_rect)
        
        pygame.display.flip()
        clock.tick(fps)
    
    pygame.time.delay(500)  # Pause at end

# def main():
#     pygame.init()
#     pygame.display.init()
#     fieldGoal(screen = pygame.display.set_mode((1400, 1050)))

# main()
