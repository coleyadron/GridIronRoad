import pygame
from minigames import puntReturn
from minigames import runPlay
from screens import inGame
from screens import coachingStaff



def test_coaching():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1050))
    pygame.display.set_caption("Coaching Staff Input")
    
    # Call the inputStaff function
    staff = coachingStaff.inputStaff(screen)
    print("Coaching Staff:", staff)
    
    pygame.quit()

def test_matchup():
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

    # Create a new instance of the InGame class
    inGame.inGame(screen, matchup, scenarios)



def main():
    test_coaching()

if __name__ == "__main__":
    main()
