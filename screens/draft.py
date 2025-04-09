import pygame
import gridironRoad
import json
from screens import teamOverview

# def kill_game():
#     pygame.quit()
#     quit()

WIDTH, HEIGHT = 1400, 1050
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football Draft Grid")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Grid parameters
GRID_COLS = 7
GRID_ROWS = 3
BOX_WIDTH = 175
BOX_HEIGHT = 200
BOX_SPACING = 10
CORNER_RADIUS = 8

ROUND = 1

PLAYERS_SELECTED = []

# Calculate grid position
BOX_WIDTH = (WIDTH - (GRID_COLS - 1) * BOX_SPACING) // GRID_COLS
BOX_HEIGHT = (HEIGHT - 120 - (GRID_ROWS - 1) * BOX_SPACING) // (GRID_ROWS + 1)

grid_x = 0
grid_y = 100

def load_json():
    try:
        with open("json/draftPlayers.json", "r") as f:
            data = json.load(f)
            # print(data)
            return data
    except FileNotFoundError:
        print("Error finding draftPlayers file")
        return []
    except Exception as e:
        print("Error reading draftPlayers: ", e)
        return []

def draw_rounded_rect(surface, color, rect, radius):
    """Draw a rectangle with rounded corners."""
    x, y, w, h = rect
    pygame.draw.rect(surface, color, (x + radius, y, w - 2 * radius, h))
    pygame.draw.rect(surface, color, (x, y + radius, w, h - 2 * radius))
    pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + w - radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + radius, y + h - radius), radius)
    pygame.draw.circle(surface, color, (x + w - radius, y + h - radius), radius)

def draw_grid(surface, playerData):
    """Draw the grid of rounded rectangles."""
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 28)
    small_font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 24)

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = grid_x + col * (BOX_WIDTH + BOX_SPACING)
            y = grid_y + row * (BOX_HEIGHT + BOX_SPACING)
            rect = (x, y, BOX_WIDTH, BOX_HEIGHT)
            draw_rounded_rect(surface, GRAY, rect, CORNER_RADIUS)

            # Calculate the player index
            player_index = row * GRID_COLS + col
            if player_index < len(playerData["draft_rounds"][ROUND - 1]["players"]):
                player = playerData["draft_rounds"][ROUND - 1]["players"][player_index]

                # Display player name with wrapping
                name = player["name"]
                words = name.split()
                lines = []
                current_line = []
                
                # Calculate maximum width for text (leave some padding)
                max_width = BOX_WIDTH - 20  # 10px padding on each side
                
                # Build wrapped lines
                for word in words:
                    test_line = ' '.join(current_line + [word])
                    test_width = font.size(test_line)[0]
                    if test_width <= max_width:
                        current_line.append(word)
                    else:
                        lines.append(' '.join(current_line))
                        current_line = [word]
                if current_line:
                    lines.append(' '.join(current_line))
                
                # Render each line of the name
                line_height = font.get_linesize()
                total_text_height = len(lines) * line_height
                start_y = y + (BOX_HEIGHT - total_text_height) // 2  # Adjust vertical position
                
                for i, line in enumerate(lines):
                    name_text = font.render(line, True, BLACK)
                    name_rect = name_text.get_rect(center=(x + BOX_WIDTH // 2, start_y + i * line_height))
                    surface.blit(name_text, name_rect)

                # Calculate and display player rating (average of characteristics)
                rating = sum(player["characteristics"].values()) // len(player["characteristics"])
                rating_text = small_font.render(f"Rating: {rating}", True, BLACK)
                rating_rect = rating_text.get_rect(center=(x + BOX_WIDTH // 2, start_y + total_text_height + 10))
                surface.blit(rating_text, rating_rect)
            else:
                # Display placeholder text if no player is available
                pick_text = font.render(f"Pick {player_index + 1}", True, BLACK)
                pick_rect = pick_text.get_rect(center=(x + BOX_WIDTH // 2, y + BOX_HEIGHT // 2))
                surface.blit(pick_text, pick_rect)


def handle_click(mouse_pos, playerData, ROUND):
    """Handles mouse clicks"""
    global PLAYERS_SELECTED
    currentRoundIndex = ROUND - 1
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = grid_x + col * (BOX_WIDTH + BOX_SPACING)
            y = grid_y + row * (BOX_HEIGHT + BOX_SPACING)
            rect = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)  # Create a Rect object
            if rect.collidepoint(mouse_pos):
                player_index = row * GRID_COLS + col
                if player_index < len(playerData["draft_rounds"][ROUND - 1]["players"]):
                    player = playerData["draft_rounds"][currentRoundIndex]["players"][player_index]

                    copy_screen = screen.copy()

                    # Create a popup box
                    popup_width = 600
                    popup_height = 450
                    popup_x = (WIDTH - popup_width) // 2
                    popup_y = (HEIGHT - popup_height) // 2

                    # Draw the popup background
                    pygame.draw.rect(screen, WHITE, (popup_x, popup_y, popup_width, popup_height))
                    pygame.draw.rect(screen, BLACK, (popup_x, popup_y, popup_width, popup_height), 3)

                    # Display player information in the popup
                    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 24)
                    # small_font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 18)

                    name_text = font.render(f"Name: {player['name']}", True, BLACK)
                    position_text = font.render(f"Position: {player['position']}", True, BLACK)
                    contract_text = font.render(f"Contract: {format(player['salary'])}", True, BLACK)
                    contract_len_text = font.render(f"Contract Length: {player['contract']}", True, BLACK)
                    characteristics_text = font.render("Characteristics:", True, BLACK)
                    rating_text = font.render(f"Rating: {player["characteristics"]["rating"]}", True, BLACK)
                    speed_text = font.render(f"Speed: {player['characteristics']['speed']}", True, BLACK)
                    strength_text = font.render(f"Strength: {player['characteristics']['strength']}", True, BLACK)
                    athleticism_text = font.render(f"Athleticism: {player['characteristics']['athleticism']}", True, BLACK)

                    screen.blit(name_text, (popup_x + 20, popup_y + 20))
                    screen.blit(position_text, (popup_x + 20, popup_y + 60))
                    screen.blit(contract_text, (popup_x + 20, popup_y + 100))
                    screen.blit(contract_len_text, (popup_x + 20, popup_y + 140))
                    screen.blit(characteristics_text, (popup_x + 20, popup_y + 180))
                    screen.blit(rating_text, (popup_x + 40, popup_y + 220))
                    screen.blit(speed_text, (popup_x + 40, popup_y + 260))
                    screen.blit(strength_text, (popup_x + 40, popup_y + 300))
                    screen.blit(athleticism_text, (popup_x + 40, popup_y + 340))

                    # Display confirmation instructions
                    confirm_text = font.render("Press SPACE to confirm or ESC to cancel", True, BLACK)
                    
                    screen.blit(confirm_text, (popup_x + 20, popup_y + 380))

                    pygame.display.update()

                    # Wait for user input (SPACE or ESC)
                    confirmPick = True
                    while confirmPick:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    print(f"Player {player['name']} selected!")
                                    confirmPick = False
                                    ROUND += 1
                                    PLAYERS_SELECTED.append(player)
                                    return ROUND  # Confirm selection
                                elif event.key == pygame.K_ESCAPE:
                                    print("Selection canceled.")
                                    screen.blit(copy_screen, (0, 0))
                                    pygame.display.update()
                                    confirmPick = False
                                    return ROUND  # Cancel selection
                            elif event.type == pygame.QUIT:
                                gridironRoad.killgame(screen)
                                # kill_game()
                else:
                    print(f"No player available for Pick {player_index + 1}")


def draft(screen):
    global ROUND
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)


    screen.fill((0, 0, 0))

    draft = font.render("Draft a player: ", True, (255, 255, 255))
    roundText = font.render("Round: " + str(ROUND), True, (255, 255, 255))
    view_teamText = font.render("Press 1 to view team", True, (255, 255, 255))
    
    screen.blit(draft, (0, 0))
    screen.blit(roundText, (0, 50))
    screen.blit(view_teamText, (0, screen.get_height() - 50))

    playerData = load_json()
    draw_grid(screen, playerData)

    pygame.display.update()


    draftOpen = True
    while draftOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
                # kill_game()
            if event.type == pygame.KEYDOWN and draftOpen:
                if event.key == pygame.K_ESCAPE:
                    gridironRoad.killgame(screen)
                    # kill_game()
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    print("1 action, view team")
                    overViewCopy = screen.copy()
                    teamOverview.teamOverview(screen, 'draft')
                    screen.blit(overViewCopy, (0, 0))
                    pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # prevRound = ROUND
                ROUND = handle_click(mouse_pos, playerData, ROUND)
                # if ROUND > prevRound:
                if ROUND > 3:
                    draftOpen = False
                    print("Draft complete!")
                    for player in PLAYERS_SELECTED:
                        print(player["name"])
                    return PLAYERS_SELECTED
                else:
                    screen.fill((0, 0, 0))
                    draft = font.render("Draft a player: ", True, (255, 255, 255))
                    roundText = font.render("Round: " + str(ROUND), True, (255, 255, 255))
                    screen.blit(draft, (0, 0))
                    screen.blit(roundText, (0, 50))
                    draw_grid(screen, playerData)
                    pygame.display.update()



def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1050))
    draft(screen)

if __name__ == "__main__":
    main()