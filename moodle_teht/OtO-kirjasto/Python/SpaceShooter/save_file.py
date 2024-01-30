import pygame, sys, os, random, math, time, var
import pickle

# Save variables to a file
def save_variables():
    print("Saving variables... like", var.coins)
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
        var.bg_volume
    ]
    with open("save_file.dat", "wb") as file:
        pickle.dump(variables_to_save, file)
    
# Load variables from a file
def load_variables():
    print("Loading variables...")
    try:
        with open("save_file.dat", "rb") as file:
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
        print("Variables loaded in example:", var.coins)
    except FileNotFoundError:
        print("No save file found")