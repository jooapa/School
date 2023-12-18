import math, var, random

def check_round(enemies):
    if len(enemies) == 0 and not var.start_round and not var.buy_round:
        print("Round " + str(var.round) + " cleared!")
        next_round()
        
def next_round():
    calculate_difficulty()
    set_cooldown_time()
    var.cooldown = var.ticks
    var.round += 1
    var.round_start_interval = var.ticks + calculate_new_round_start_interval()
    var.start_round = True
        
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
    print("Next round in " + str(spawn_interval) + " seconds", "With cooldown time: " + str(var.cooldown_time) + " seconds")
    return spawn_interval

def set_cooldown_time():
    # decrease the cooldown time using difficulty and make it fast at the start 
    var.cooldown_time = cooldown_time_calculator(var.round)
    print("Cooldown time: " + str(var.cooldown_time) + " seconds")


def cooldown_time_calculator(round_number):
    max_value = 3.0
    # You can adjust this value based on how fast you want the values to decrease
    decay_factor = 0.01

    # This is the formula for the cooldown time
    cooldown_time = max_value * \
        (1 / (1 + math.exp(decay_factor * (round_number - 5))))

    # Ensure the calculated value is not less than 0.8
    return max(cooldown_time, 1)

def calculate_enemy_health():
    min_health = 100
    max_health = 200
    health = min_health * (1 + var.difficulty / 100)
    print("Enemy health: " + str(health))
    return max(min(health, max_health), min_health)
