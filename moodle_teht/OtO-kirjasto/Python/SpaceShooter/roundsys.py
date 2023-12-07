import math, var

def check_round(enemies):
    if len(enemies) == 0 and not var.start_round:
        var.round += 1
        var.cooldown = var.ticks
        var.start_round = True

def calculate_difficulty():
    var.difficulty = math.floor(var.difficulty * var.difficulty_curve)
    return var.difficulty

def calculate_enemy_spawn_amount():
    if var.enemy_speed < 400:
        var.enemy_speed += 8
    enemy_spawn_amount = math.floor(math.sqrt(var.difficulty))
    return enemy_spawn_amount

