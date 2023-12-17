import math, var

def check_round(enemies):
    if len(enemies) == 0 and not var.start_round and not var.buy_round:
        print("Round " + str(var.round) + " cleared!")
        next_round()
        
def next_round():
    var.cooldown = var.ticks
    var.start_round = True
    var.round_start_interval = var.ticks + calculate_new_round_start_interval()
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
    if var.round == 1:
        return 2
    return max(enemy_spawn_amount, 1)

def calculate_new_round_start_interval():
    # take in the spawn interval and the amount of enemies spwaning in the round
    spawn_interval = calculate_enemy_spawn_amount() * var.cooldown_time + var.next_round_cooldown
    print("Next round in " + str(spawn_interval) + " seconds")
    return spawn_interval