import json
import random

def scheduler():
    updatedSchedule = updateSchedule()

    try:
        with open("json/userSeason.json", "w") as file:
            json.dump(updatedSchedule, file, indent=4)
    except Exception as e:
        print("Error updating season: ", e)

def updateSchedule():
    try:
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
    

    updatedSchedule = {
        "regularSeason" :{
            "matchups": [] 
        },
        "postSeason" :{
            "matchups": [] 
        }    
    }
    
    possibleOpponents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    for week in range(18):
            updatedWeek = {
                "week": week + 1,
                "opponent": None,
                "played": False,
                "user_score": None,
                "opponent_score": None,
                "result": None
            }
            week += 1
            randomOpponent = random.choice(possibleOpponents)
            possibleOpponents.remove(randomOpponent)
            if randomOpponent == 33:
                updatedWeek['opponent'] = "Bye"
                print(week)
            for team in teams["teams"]:
                if team["id"] == randomOpponent:
                    updatedWeek['opponent'] = team["name"]
                    break
            updatedSchedule["regularSeason"]["matchups"].append(updatedWeek)

    if {"opponent": "Bye"} not in updatedSchedule["regularSeason"]["matchups"]:
        week = random.randint(5, 16)
        updatedSchedule["regularSeason"]["matchups"][week]["opponent"] = "Bye"
        print("added post make")
    return updatedSchedule

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

    