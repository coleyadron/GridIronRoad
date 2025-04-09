import json
import random

def scheduler():
    try:
        with open("json/schedule.json", "r") as file:
            schedule = json.load(file)
        with open("json/leagueTeams.json", "r") as file:
            teams = json.load(file)
    except FileNotFoundError:
        print("Error finding schedule file")
        return None
    except json.JSONDecodeError:
        print("Error decoding schedule file")
        return None
    except Exception as e:
        print("Error reading schedule file: ", e)
        return None
    
    possibleOpponents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    week = 1
    for week in schedule["schedule"]:
            game = week["game"]
            randomOpponent = random.choice(possibleOpponents)
            possibleOpponents.remove(randomOpponent)
            if randomOpponent == 33:
                game['opponent'] = "Bye"
            for team in teams["teams"]:
                if team["id"] == randomOpponent:
                    game['opponent'] = team["name"]
                    break
            game["result"] = "None"
            game["played"] = False
            print(game)
                
def cleanSchedule():
    try:
        with open("json/schedule.json", "r") as file:
            schedule = json.load(file)
    except FileNotFoundError:
        print("Error finding schedule file")
        return None
    except json.JSONDecodeError:
        print("Error decoding schedule file")
        return None
    except Exception as e:
        print("Error reading schedule file: ", e)
        return None
    
    for week in schedule["week"]:
        game = schedule["game"]
        game["result"] = "None"
        game["played"] = False
        game["opponent"] = ""

scheduler()

    