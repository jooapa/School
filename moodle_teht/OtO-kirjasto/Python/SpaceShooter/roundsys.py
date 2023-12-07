import math, var


def check_round(enemies):
    if len(enemies) == 0 and not var.start_round:
        var.round += 1
        var.cooldown = var.ticks
        var.start_round = True

def calculate_difficulty():
    var.difficulty = math.pow(var.round, var.difficulty_curve) * var.difficulty
    return var.difficulty

def calculate_enemy_spawn_amount():
    enemy_spawn_amount = math.floor(math.sqrt(var.difficulty))
    return enemy_spawn_amount