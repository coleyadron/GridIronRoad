import pygame
from minigames import puntReturn
from minigames import runPlay
from screens import inGame

def main():
    pygame.init()
    pygame.display.init()

    # Set up the game screen
    screen = pygame.display.set_mode((1400, 1050))
    pygame.display.set_caption("mini game test")

    matchup = {
            "week": 10,
            "opponent": "New York Giants",
            "played": False,
            "score": None,
            "opponent_score": None,
            "game_result": None
    }

    scenarios = [{
        "id": 67,
        "description": "An influencer challenged your team to a TikTok dance-off",
        "effect": {
            "morale": -0.1,
            "performance": 0.1
        }
    }]

    # Create an instance of the PuntReturn class
    inGame.inGame(screen, matchup, scenarios)

if __name__ == "__main__":
    main()
