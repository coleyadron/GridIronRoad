import pygame
import random
import time
from logic.player import Player
from logic.defender import Defender

def checkDefenderSpawnLocation(defender, defenders):
    # Check if the defender's x position is too close to any existing defenders
    for other_defender in defenders:
        if other_defender != defender and abs(defender.x - other_defender.x) < 50:
            return False
    return True

def runMiniGame(screen):
    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    GROUND_HEIGHT = SCREEN_HEIGHT - 100
    PLAYER_START_X = 100
    GAME_SPEED = 5
    JUMP_STRENGTH = 15
    GRAVITY = .5
    
    # Initialize game state
    player = Player(PLAYER_START_X, GROUND_HEIGHT - 80)
    defenders = []
    distance = 0
    game_active = True
    last_defender_time = 0
    defender_spawn_rate = 1500
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    
    try:
        defender_img = pygame.image.load("assets/images/bearSprites/leftFour.PNG").convert_alpha()
        defender_img = pygame.transform.scale(defender_img, (50, 75))
    except:
        defender_img = None


    initate_field = False
    while True:
        current_time = pygame.time.get_ticks()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    player.jump(JUMP_STRENGTH)
                elif event.key == pygame.K_ESCAPE:
                    return False
                # elif event.key == pygame.K_r and not game_active:
                #     return runMiniGame(screen)  # Restart
        
        if game_active:
            if not initate_field:
                for i in range(3):
                    x = random.randint(350, SCREEN_WIDTH - 50)
                    while not checkDefenderSpawnLocation(Defender(SCREEN_WIDTH, defender_img, x=x), defenders):
                        x = random.randint(350, SCREEN_WIDTH - 50)
                    defenders.append(Defender(SCREEN_WIDTH, defender_img, x=x, y=GROUND_HEIGHT - 80))
                initate_field = True
            # Spawn defenders
            if current_time - last_defender_time > defender_spawn_rate:
                defenders.append(Defender(SCREEN_WIDTH, defender_img, x=SCREEN_WIDTH, y=GROUND_HEIGHT - 80))
                last_defender_time = current_time
                defender_spawn_rate = max(800, defender_spawn_rate - 20)
            
            # Update game state
            player.update(GRAVITY, GROUND_HEIGHT)
            distance += GAME_SPEED
            
            # Update defenders and check collisions
            for defender in defenders[:]:
                defender.update_left()
                
                # Remove defenders that go off bottom of screen
                if defender.is_offscreen(SCREEN_HEIGHT):
                    defenders.remove(defender)
                
                # Check collision
                if defender.collides_with(player.get_rect()):
                    game_active = False
                    result = False
            
            # Check for touchdown (run distance)
            if distance >= 2000:  # Adjust as needed
                game_active = False
                result = True
        
        # Drawing
        screen.fill((255, 255, 255))
        
        # Draw ground
        pygame.draw.rect(screen, (0, 128, 0), (0, GROUND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_HEIGHT))
        
        # Draw player and defenders
        player.draw(screen, 0)  # Camera_x not needed for vertical defenders
        for defender in defenders:
            defender.draw(screen)
        
        # Draw UI
        distance_text = font.render(f"Yards: {distance//10}", True, (0, 0, 0))
        screen.blit(distance_text, (10, 10))
        
        if not game_active:
            result_text = "TOUCHDOWN!" if result else "TACKLED!"
            color = (0, 200, 0) if result else (200, 0, 0)
            screen.fill((0, 0, 0))
            text = font.render(f"{result_text}", True, color)
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
            pygame.display.flip()
            time.sleep(1)
            return result
        
        pygame.display.flip()
        clock.tick(60)

def exec(screen):
    return runMiniGame(screen)