import pygame
import json
# import gridironRoad

def killgame():
    pygame.quit()
    quit()

def load_team():
    try:
        with open("json/userTeam.json", "r") as file:
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
    
def display_team(screen, team):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    team_name = team["team_name"]

    # Display team name
    name_text = font.render(f"{team_name}", True, (255, 255, 255))
    screen.blit(name_text, (0, 50))

    teamSalary = 0

    # Display players
    players = team["players"]
    y_offset = 100
    for player in players:
        player_text = font.render(f"{player['name']}, {player['position']}, ${format(player['salary'], ",")}", True, (255, 255, 255))
        screen.blit(player_text, (50, y_offset))
        y_offset += 50
        teamSalary += player["salary"]

    y_offset += 25

    # Display current team salary
    current_salary_text = font.render(f"Team Salary: ${format(teamSalary, ",")}", True, (255, 255, 255))
    screen.blit(current_salary_text, (0, y_offset))
    y_offset += 50

    # Display salary cap
    salary_cap = 279200000
    salary_cap_text = font.render(f"Salary Cap: ${format(salary_cap, ",")}", True, (255, 255, 255))
    screen.blit(salary_cap_text, (0, y_offset))

    rect_width = screen.get_width() * .8
    red = (255, 0, 0)
    white = (255, 255, 255)
    rect_height = 50
    rect_x = (screen.get_width() - rect_width) // 2
    rect_y = y_offset + 50


    salary_width = int((teamSalary / salary_cap) * rect_width)

    pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect(screen, white, (rect_x, rect_y, salary_width, rect_height))
    
    
def teamOverview(screen, state):
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)
    screen.fill((0, 0, 0))

    overviewText = font.render("Current Roster", True, (255, 255, 255))
    returnText = font.render(f"Press SPACE to return to the {state}", True, (255, 255, 255))
    screen.blit(overviewText, (0,0))
    screen.blit(returnText, (0, screen.get_height() - 50))

    team = load_team()

    if team is None:
        print("Error loading team data")
        return
    
    #Display team
    display_team(screen, team)

    viewTeamOverview = True
    while viewTeamOverview:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                viewTeamOverview = False
                killgame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    viewTeamOverview = False
                    killgame()
                elif event.key == pygame.K_SPACE:
                    viewTeamOverview = False
        pygame.display.flip()



    

def main():
    screen = pygame.display.set_mode((1400, 1050))
    pygame.display.set_caption("Team Overview")
    screen.fill((0, 0, 0))

    teamOverview(screen)