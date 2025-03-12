import pygame
# import gridironRoad
import json

def kill_game():
    pygame.quit()
    quit()

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
GRID_ROWS = 4
BOX_WIDTH = 175
BOX_HEIGHT = 200
BOX_SPACING = 10
CORNER_RADIUS = 8

ROUND = 1

# Calculate grid position
BOX_WIDTH = (WIDTH - (GRID_COLS - 1) * BOX_SPACING) // GRID_COLS
BOX_HEIGHT = (HEIGHT - 120 - (GRID_ROWS - 1) * BOX_SPACING) // GRID_ROWS

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

                # Display player name
                name_text = font.render(player["name"], True, BLACK)
                name_rect = name_text.get_rect(center=(x + BOX_WIDTH // 2, y + BOX_HEIGHT // 2 - 20))
                surface.blit(name_text, name_rect)

                # Calculate and display player rating (average of characteristics)
                rating = sum(player["characteristics"].values()) // len(player["characteristics"])
                rating_text = small_font.render(f"Rating: {rating}", True, BLACK)
                rating_rect = rating_text.get_rect(center=(x + BOX_WIDTH // 2, y + BOX_HEIGHT // 2 + 20))
                surface.blit(rating_text, rating_rect)
            else:
                # Display placeholder text if no player is available
                pick_text = font.render(f"Pick {player_index + 1}", True, BLACK)
                pick_rect = pick_text.get_rect(center=(x + BOX_WIDTH // 2, y + BOX_HEIGHT // 2))
                surface.blit(pick_text, pick_rect)


def handle_click(mouse_pos, playerData):
    """Handles mouse clicks"""
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = grid_x + col * (BOX_WIDTH + BOX_SPACING)
            y = grid_y + row * (BOX_HEIGHT + BOX_SPACING)
            rect = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)  # Create a Rect object
            if rect.collidepoint(mouse_pos):
                player_index = row * GRID_COLS + col
                if player_index < len(playerData["draft_rounds"][ROUND - 1]["players"]):
                    player = playerData["draft_rounds"][ROUND - 1]["players"][player_index]
                    print(f"Player Information for Pick {player_index + 1}:")
                    print(f"Name: {player['name']}")
                    print(f"Position: {player['position']}")
                    print(f"Characteristics: {player['characteristics']}")
                    print(f"Rating: {sum(player['characteristics'].values()) // len(player['characteristics'])}")
                else:
                    print(f"No player available for Pick {player_index + 1}")


def draft(screen):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)


    screen.fill((0, 0, 0))

    draft = font.render("Draft a player: ", True, (255, 255, 255))
    roundText = font.render("Round: " + str(ROUND), True, (255, 255, 255))
    screen.blit(draft, (0, 0))
    screen.blit(roundText, (0, 50))

    playerData = load_json()
    draw_grid(screen, playerData)

    pygame.display.update()


    draftOpen = True
    while draftOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # gridironRoad.killgame(screen)
                kill_game()
            if event.type == pygame.KEYDOWN and draftOpen:
                if event.key == pygame.K_ESCAPE:
                    # gridironRoad.killgame(screen)
                    kill_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                handle_click(mouse_pos, playerData)


def main():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1050))
    draft(screen)

if __name__ == "__main__":
    main()