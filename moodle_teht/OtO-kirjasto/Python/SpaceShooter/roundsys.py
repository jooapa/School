import math, var

def check_round(enemies):
    if len(enemies) == 0 and not var.start_round and not var.buy_round:
        var.round += 1
        var.cooldown = var.ticks
        var.round_start_interval = var.ticks + 5
        # if var.round in var.buy_rounds:
        #     var.buy_round = True
        #     var.start_round = False
        # else:
        var.start_round = True
def next_round():
    var.start_round = True
    var.round_start_interval = var.ticks + calculate_spawn_interval()
    var.round += 1
        
def calculate_difficulty():
    var.difficulty = var.round * var.difficulty_curve
    if var.enemy_speed < 400:
        var.enemy_speed = var.enemy_speed + 3
        print("Enemy speed: " + str(var.enemy_speed))

def calculate_enemy_spawn_amount():
    enemy_spawn_amount = round(2 * math.sqrt(var.difficulty) * math.log(var.difficulty + 1))
    if var.round == 2:
        return 2
    return max(enemy_spawn_amount, 1)

def calculate_spawn_interval():
    # from 20 to 10 seconds slowly
    spawn_interval = 20 - (var.round * 0.2)
    return max(spawn_interval, 0.5)