import pygame

screen_width = 1280
screen_height = 720
camera_offset = pygame.math.Vector2(0, 0)

cooldown_time = 4
next_round_cooldown = 15
round = 0
start_round = False
difficulty = 1
difficulty_curve = 0.6
round_start_interval = 0
start_game_animation = False

current_bg_song = None
bg_volume = 0.3

player_speed = 60
player_health = 60
player_max_health = 5

enemy_speed = 80
enemy_max_health = 5

mouse_x = 0
mouse_y = 0
player_pos = pygame.math.Vector2()
enemy_spawn_offset = 500
FPS = 144
play_area = 10
game_running = False # False when player dies, showing the menu
shop_open = False

buy_rounds = [3, 6, 10, 15, 20, 25, 30, 35, 40, 45, 50]
buy_round = False

ammo_max = 20
ammo_max_limit = 100
firerate_max = 0.05
firerate_max_limit = 0.0
reload_time_max = 0
reload_time_max_limit = 1
gun_damage = 30
gun_damage_max_limit = 100

invincibility_time_max = 1
invincibility_time_max_limit = 3
player_health_max_limit = 200
coins = 100000
kakku_sinko_explosion_radius = 100

# Dont change these
firerate = 0
reload_time = reload_time_max
ammo = ammo_max
ticks = 0
cooldown = 0
invincibility_time = 0
start_new_round_in_the_main_menu = False

raka_ase = {
    "MK1": {"Damage": 20, "Fire Rate": 0.5, "Reload Time": 5, "Magazine Size": 10, "Speed": 800, "Cost": None},
    "MK2": {"Damage": 30, "Fire Rate": 0.45, "Reload Time": 4.5, "Magazine Size": 20, "Speed": 900, "Cost": 200},
    "MK3": {"Damage": 30, "Fire Rate": 0.4, "Reload Time": 4.5, "Magazine Size": 30, "Speed": 1000, "Cost": 300},
    "MK4": {"Damage": 40, "Fire Rate": 0.35, "Reload Time": 4, "Magazine Size": 40, "Speed": 1000, "Cost": 500},
    "MK5": {"Damage": 50, "Fire Rate": 0.4, "Reload Time": 3.5, "Magazine Size": 40, "Speed": 1100, "Cost": 600},
}
current_raka_ase_upgrade = "MK1"
raka_ase_ammo = 0

kakku_sinko = {
    "MK1": {"Damage": 50, "Fire Rate": 2.0, "Reload Time": 5, "Magazine Size": 3, "Speed": 300, "Cost": None},
    "MK2": {"Damage": 80, "Fire Rate": 1.8, "Reload Time": 4.5, "Magazine Size": 4, "Speed": 400, "Cost": 300},
    "MK3": {"Damage": 90, "Fire Rate": 1.6, "Reload Time": 4, "Magazine Size": 5, "Speed": 500, "Cost": 400},
    "MK4": {"Damage": 100, "Fire Rate": 1.4, "Reload Time": 3.5, "Magazine Size": 6, "Speed": 600, "Cost": 550},
    "MK5": {"Damage": 150, "Fire Rate": 1.2, "Reload Time": 3, "Magazine Size": 7, "Speed": 700, "Cost": 600},
}
current_kakku_sinko_upgrade = "MK1"
kakku_sinko_ammo = 0