import pygame
import json
from screens import teamOverview
import gridironRoad

WIDTH, HEIGHT = 1400, 1050
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football Draft Grid")

PLAYERS_SELECTED = []

POPUP_OPEN = False

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

BOX_WIDTH = (WIDTH - (GRID_COLS - 1) * BOX_SPACING) // GRID_COLS
BOX_HEIGHT = (HEIGHT - 120 - (GRID_ROWS - 1) * BOX_SPACING) // (GRID_ROWS + 1)

grid_x = 0
grid_y = 100

def killgame():
    pygame.quit()
    quit()

def load_free_agents():
    try:
        with open("json/freeAgents.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("Error finding JSON file")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON file")
        return None
    except Exception as e:
        print("Error reading JSON file: ", e)
        return None
    
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
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    small_font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 24)

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = grid_x + col * (BOX_WIDTH + BOX_SPACING)
            y = grid_y + row * (BOX_HEIGHT + BOX_SPACING)
            rect = (x, y, BOX_WIDTH, BOX_HEIGHT)
            draw_rounded_rect(surface, GRAY, rect, CORNER_RADIUS)

            # Calculate the player index
            player_index = row * GRID_COLS + col
            if player_index < len(playerData["free_agents"]):
                player = playerData["free_agents"][player_index]

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
                rating = player["rating"]
                rating_text = small_font.render(f"Rating: {rating}", True, BLACK)
                rating_rect = rating_text.get_rect(center=(x + BOX_WIDTH // 2, start_y + total_text_height + 10))
                surface.blit(rating_text, rating_rect)
            else:
                # Display placeholder text if no player is available
                pick_text = font.render(f"Pick {player_index + 1}", True, BLACK)
                pick_rect = pick_text.get_rect(center=(x + BOX_WIDTH // 2, y + BOX_HEIGHT // 2))
                surface.blit(pick_text, pick_rect)


def handle_click(mouse_pos, playerData):
    """Handles mouse clicks"""
    global PLAYERS_SELECTED
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = grid_x + col * (BOX_WIDTH + BOX_SPACING)
            y = grid_y + row * (BOX_HEIGHT + BOX_SPACING)
            rect = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)  # Create a Rect object
            if rect.collidepoint(mouse_pos) and not POPUP_OPEN:
                player_index = row * GRID_COLS + col
                if player_index < 18:
                    # check within salary cap
                    player = playerData["free_agents"][player_index]

                    copy_screen = screen.copy()

                    # teamSalary = gridironRoad.getTeamSalary()
                    teamSalary = 279100090
                    salary_cap = 279200000

                    # Create a popup box
                    popup_width = 600
                    popup_height = 450
                    popup_x = (WIDTH - popup_width) // 2
                    popup_y = (HEIGHT - popup_height) // 2

                    if teamSalary + (player["salary"] / int(player["contract"][:1])) > salary_cap:
                        print("Salary cap exceeded")
                        # Display a message
                        font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

                        pygame.draw.rect(screen, WHITE, (popup_x, popup_y, popup_width, popup_height))
                        pygame.draw.rect(screen, BLACK, (popup_x, popup_y, popup_width, popup_height), 3)

                        message_text = font.render("Salary cap exceeded", True, RED)
                        message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                        exit_text = font.render("Press SPACE or ESC to exit", True, BLACK)
                        exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
                        screen.blit(exit_text, exit_rect)
                        screen.blit(message_text, message_rect)
                        pygame.display.update()

                        confirmSalary = True
                        while confirmSalary:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        screen.blit(copy_screen, (0, 0))
                                        pygame.display.update()
                                        print("Exit popup")
                                        confirmSalary = False
                                    elif event.key == pygame.K_ESCAPE:
                                        print("Selection canceled.")
                                        screen.blit(copy_screen, (0, 0))
                                        pygame.display.update()
                                        confirmSalary = False
                                elif event.type == pygame.QUIT:
                                    # gridironRoad.killgame(screen)
                                    killgame()
                        return


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
                    rating_text = font.render(f"Rating: {player["rating"]}", True, BLACK)
                    speed_text = font.render(f"Speed: {player['speed']}", True, BLACK)
                    strength_text = font.render(f"Strength: {player['strength']}", True, BLACK)
                    athleticism_text = font.render(f"Athleticism: {player['athleticism']}", True, BLACK)

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
                                    PLAYERS_SELECTED.append(player)
                                elif event.key == pygame.K_ESCAPE:
                                    print("Selection canceled.")
                                    screen.blit(copy_screen, (0, 0))
                                    pygame.display.update()
                                    confirmPick = False
                            elif event.type == pygame.QUIT:
                                # gridironRoad.killgame(screen)
                                killgame()
                else:
                    print(f"No player available for Pick {player_index + 1}")    
    
def free_agents(screen):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    screen.fill((0, 0, 0))

    titleText = font.render("Available Free Agents", True, (255, 255, 255))
    screen.blit(titleText, (screen.get_width() / 2 - titleText.get_width() / 2, 0))

    teamOverviewText = font.render("Press 1 to view team", True, (255, 255, 255))
    screen.blit(teamOverviewText, (screen.get_width() / 2 - teamOverviewText.get_width() / 2, screen.get_height() - 50))

    free_agents = load_free_agents()

    if free_agents is None:
        print("Error loading free agents")
        return

    draw_grid(screen, free_agents)

    pygame.display.update()

    free_agents_open = True
    while free_agents_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # gridironRoad.killgame(screen)
                killgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    free_agents_open = False
                    return
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    print("1 action, view team")
                    overViewCopy = screen.copy()
                    teamOverview.teamOverview(screen, "free agents")
                    screen.blit(overViewCopy, (0, 0))
                    pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                player = handle_click(mouse_pos, free_agents)
                pygame.display.update()

    return player

def main():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((1400, 1050))
    pygame.display.set_caption("Free Agents")
    screen.fill((0, 0, 0))

    free_agents(screen)

if __name__ == "__main__":
    main()