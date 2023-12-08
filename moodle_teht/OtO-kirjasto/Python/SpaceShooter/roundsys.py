import math, var

def check_round(enemies):
    if len(enemies) == 0 and not var.start_round:
        var.round += 1
        var.cooldown = var.ticks
        if var.round in var.buy_rounds:
            var.buy_round = True
        else:
            var.start_round = True

def calculate_difficulty():
    var.difficulty = var.round * var.difficulty_curve
    return var.difficulty

def calculate_enemy_spawn_amount():
    if var.enemy_speed < 400:
        var.enemy_speed = 90 + math.floor(math.sqrt(var.difficulty)) * 10
    enemy_spawn_amount = math.floor(math.sqrt(var.difficulty)) * 2
    return enemy_spawn_amount

