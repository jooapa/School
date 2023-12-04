import random, var
spawn_enemy = random.randint(0, 10)

def spawn_enemy():
    spawn_side = random.randint(1, 4)  # 1 = top, 2 = right, 3 = bottom, 4 =
    # spawn_side = 2
    # spawn enemy just outside the screen
    if spawn_side == 1:
        return random.randint(0, var.screen_width) - var.camera_offset.x, -var.enemy_spawn_offset - var.camera_offset.y
    elif spawn_side == 2:
        return var.screen_width + var.enemy_spawn_offset - var.camera_offset.x, random.randint(0, var.screen_height) - var.camera_offset.y
    elif spawn_side == 3:
        return random.randint(0, var.screen_width) - var.camera_offset.x, var.screen_height + var.enemy_spawn_offset - var.camera_offset.y
    elif spawn_side == 4:
        return -var.enemy_spawn_offset - var.camera_offset.x, random.randint(0, var.screen_height) - var.camera_offset.y