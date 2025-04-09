import numpy as np
import random 
import json


#Normalizes stats on scale of 0 to 100
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0.5

#calculates teams weighted power rating
def calculate_power(overall, offensive, defensive, special, weights, variance_range=(-0.5, 0.5)):
    normalized_overall = normalize(overall, 0, 100)
    normalized_offensive = normalize(offensive, 0, 100)
    normalized_defensive = normalize(defensive, 0, 100)
    normalized_special = normalize(special, 0, 100)

    power = weights[0] * normalized_overall + weights[1] * normalized_offensive + weights[2] * normalized_defensive + weights[3] * normalized_special
    power += random.uniform(*variance_range)  # Adding random variance
    return power

def win_probability(power_a, power_b):
    return 1 / (1 + np.exp(-(power_a - power_b)))

def determine_winner(team_a, team_b, weights=(0.5, 0.2, 0.2, 0.1), simulations=1000):
    team_a_wins = 0
    team_a_ratings = get_team_ratings(team_a, "json/oppTeams.json")
    team_b_ratings = get_team_ratings(team_b, "json/oppTeams.json")

    for _ in range(simulations):
        power_a = calculate_power(team_a_ratings['overall'], team_a_ratings['offense'], team_a_ratings['defense'], team_a_ratings['special_teams'], weights) 
        power_b = calculate_power(team_b_ratings['overall'], team_b_ratings['offense'], team_b_ratings['defense'], team_b_ratings['special_teams'], weights)
    
        if random.random() < win_probability(power_a, power_b):
            team_a_wins += 1
    
    win_rate_a = team_a_wins / simulations
    return f"'{team_a}' Win" if win_rate_a > 0.5 else f"'{team_b}' Win"

def get_team_ratings(team_name, json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    for team in data["teams"]:
        if team_name == team["name"]:
            ratings = team["ratings"]
            return ratings
            
    
    return f"Team '{team_name}' not found."


# Example usage
result = determine_winner("Thunderhawks", "Blazing Storm")
print(result)
