import pygame

screen_width = 1280
screen_height = 720
camera_offset = pygame.math.Vector2(0, 0)

cooldown_time = 0.2
round = 2
start_round = False
difficulty = 1
difficulty_curve = 0.6

player_speed = 130
player_health = 100
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
buy_rounds = [3, 6, 10, 15, 20, 25, 30, 35, 40, 45, 50]
buy_round = False
buy_tokens = 3

ammo_max = 20
ammo_max_limit = 100
firerate_max = 0.2
firerate_max_limit = 0.05
reload_time_max = 3
reload_time_max_limit = 1
gun_damage = 30
gun_damage_max_limit = 100
invincibility_time_max = 1
invincibility_time_max_limit = 3
player_health_max_limit = 200
coins = 100000

# Dont change these
firerate = 0
reload_time = reload_time_max
ammo = ammo_max
ticks = 0
cooldown = 0
invincibility_time = 0