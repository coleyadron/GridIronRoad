import numpy as np
import random 

#Normalizes stats on scale of 0 to 100
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0.5

#calculates teams weighted power rating
def calculate_power(overall, offensive, defensive, special, weights):
    normalized_overall = normalize(overall, 0, 100)
    normalized_offensive = normalize(offensive, 0, 100)
    normalized_defensive = normalize(defensive, 0, 100)
    normalized_special = normalize(special, 0, 100)

    power = weights[0] * normalized_overall + weights[1] * normalized_offensive + weights[2] * normalized_defensive + weights[3] * normalized_special
    return power

def win_probability(power_a, power_b):
    return 1 / (1 + np.exp(-(power_a - power_b)))

def determine_winner(team_a_offense, team_a_defense, team_a_special, 
                     team_b_offense, team_b_defense, team_b_special, 
                     morale_total, performance_total, game_result,
                     weights=(0.5, 0.2, 0.2, 0.1), simulations=1000):
    team_a_wins = 0

    team_a_overall = (team_a_offense + team_a_defense + team_a_special) / 3
    team_b_overall = (team_b_offense + team_b_defense + team_b_special) / 3
    variance_range = ((morale_total / 10), (performance_total / 10))

    for _ in range(simulations):
        power_a = calculate_power(team_a_overall, team_a_offense, team_a_defense, team_a_special, weights) 
        power_b = calculate_power(team_b_overall, team_b_offense, team_b_defense, team_b_special, weights)
        power_a += random.uniform(*variance_range) 
        if game_result:
            power_a += 0.075
        if random.random() < win_probability(power_a, power_b):
            team_a_wins += 1
    
    win_rate_a = team_a_wins / simulations
    #print(win_rate_a, power_a, power_b, variance_range, random.uniform(*variance_range))
    return True if win_rate_a > 0.5 else False

def simulateDrive(
            MY_OFFENSE,
            MY_DEFENSE,
            MY_SPECIAL,
            OPPOSING_OFFENSE,
            OPPOSING_DEFENSE,
            OPPOSING_SPECIAL,
            PERFORMANCE_TOTAL,
            MORALE_TOTAL,
            game_result):
    possible_outcomes = [0, 3, 6, 7]
    weight = (0.30, 0.13, 0.18, 0.39)
    drive_result = determine_winner(MY_OFFENSE, MY_DEFENSE, MY_SPECIAL, OPPOSING_OFFENSE, OPPOSING_DEFENSE, OPPOSING_SPECIAL, MORALE_TOTAL, PERFORMANCE_TOTAL, game_result)
    if drive_result:
        scored = random.choices(possible_outcomes, weights=weight, k=1)
        print(scored[0])
        return scored[0]
    else:
        scored = random.choices([0, -3, -6, -7], weights=weight, k=1)
        print(scored[0])
        return scored[0]

    #will return 0,3,6,7 if won if loss then return negative values

#test
# simulateDrive(
#     MY_OFFENSE = 75,
#     MY_DEFENSE = 80,
#     MY_SPECIAL = 90,
#     OPPOSING_OFFENSE = 75,
#     OPPOSING_DEFENSE = 80,
#     OPPOSING_SPECIAL = 90,
#     PERFORMANCE_TOTAL = -0.6,
#     MORALE_TOTAL = 0.4,
#     game_result = False
# )