import pygame, sys, os, random, math, time, var
import pickle

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

# Save variables to a file
save_file_path = "pig.pkl"
with open(save_file_path, "wb") as file:
    pickle.dump(variables_to_save, file)
    
# Load variables from a file
with open(save_file_path, "rb") as file:
    variables_to_load = pickle.load(file)
    
# Set variables
var.good_ending_completed = variables_to_load[0]
var.very_bad_ending_completed = variables_to_load[1]
var.bad_ending_completed = variables_to_load[2]
var.bought_weapons = variables_to_load[3]
var.current_kakku_sinko_upgrade = variables_to_load[4]
var.current_raka_ase_upgrade = variables_to_load[5]
var.kakku_sinko_explosion_radius = variables_to_load[6]
var.coins = variables_to_load[7]
var.dash_speed = variables_to_load[8]
var.best_round = variables_to_load[9]
var.bg_volume = variables_to_load[10]

