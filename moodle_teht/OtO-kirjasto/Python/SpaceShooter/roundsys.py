import math, var

def check_round(enemies):
    if len(enemies) == 0 and not var.start_round and not var.buy_round:
        var.round += 1
        var.cooldown = var.ticks
        if var.round in var.buy_rounds:
            var.buy_round = True
            var.start_round = False
        else:
            var.start_round = True

def calculate_difficulty():
    var.difficulty = var.round * var.difficulty_curve
    if var.enemy_speed < 400:
        var.enemy_speed = var.enemy_speed + 3
        print("Enemy speed: " + str(var.enemy_speed))

def calculate_enemy_spawn_amount():
    enemy_spawn_amount = round(4 * math.sqrt(var.difficulty) * math.log(var.difficulty))
    return max(enemy_spawn_amount, 1)

