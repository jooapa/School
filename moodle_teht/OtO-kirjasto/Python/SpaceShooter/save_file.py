import pygame, sys, os, random, math, time, var
import pickle

# Save variables to a file
def save_variables():
    print("Saving variables...")
        
    # Variables to save
    variables_to_save = [
        var.good_ending_completed,
        var.very_bad_ending_completed,
        var.bad_ending_completed,
        var.bought_weapons,
        var.current_kakku_sinko_upgrade,
        var.current_raka_ase_upgrade,
        var.kakku_sinko_explosion_radius,
        var.coins,
        var.dash_speed,
        var.best_round,
        var.bg_volume,
        var.invincibility_time_max
    ]
    
    with open("pig", "wb") as file:
        pickle.dump(variables_to_save, file)
    
# Load variables from a file
def load_variables():
    print("Loading variables...")
    try:
        with open("pig", "rb") as file:
            variables = pickle.load(file)
            
        var.good_ending_completed = variables[0]
        var.very_bad_ending_completed = variables[1]
        var.bad_ending_completed = variables[2]
        var.bought_weapons = variables[3]
        var.current_kakku_sinko_upgrade = variables[4]
        var.current_raka_ase_upgrade = variables[5]
        var.kakku_sinko_explosion_radius = variables[6]
        var.coins = variables[7]
        var.dash_speed = variables[8]
        var.best_round = variables[9]
        var.bg_volume = variables[10]
        var.invincibility_time_max = variables[11]
                
    except FileNotFoundError:
        print("No save file found")
        
    
# HISTORY: will append all game information to a history file
# | Date: 29.2.2024 17:3 |
# | Round: 2             |
# | Coins Collected: 0   |
# | Enemies Killed: 0    |

# | needs to be in the same line as the other |'s

def history(round, coins, enemies_killed):
    print("Saving history...")
    with open("history.pig", "a") as file:
        file.write("| Date: " + time.strftime("%d.%m.%Y %H:%M") + " |\n")
        file.write("| Round: " + str(round) + " |\n")
        file.write("| Coins Collected: " + str(coins) + " |\n")
        file.write("| Enemies Killed: " + str(enemies_killed) + " |\n")
        file.write("\n")

def load_history():
    print("Loading history...")
    try:
        with open("history.pig", "r") as file:
            history = file.readlines()
        return history
    except FileNotFoundError:
        print("No history file found")
        return None