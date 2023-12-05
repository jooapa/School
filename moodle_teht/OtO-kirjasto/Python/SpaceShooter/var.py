import pygame

screen_width = 1280
screen_height = 720

enemy_spawn_offset = 100
camera_offset = pygame.math.Vector2(0, 0)

mouse_x = 0
mouse_y = 0

ammo_max = 10
firerate_max = 0.1
reload_time_max = 0

firerate = 0
reload_time = reload_time_max
ammo = ammo_max