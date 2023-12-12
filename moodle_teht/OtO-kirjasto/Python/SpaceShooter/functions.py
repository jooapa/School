import random, var, pygame, math
import var
import pygame
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
    

def rando_bullet():
    räkä = random.randint(1, 5)
    if räkä == 1:
        return "img/räkä1.png"
    elif räkä == 2:
        return "img/räkä2.png"
    elif räkä == 3:
        return "img/räkä3.png"
    elif räkä == 4:
        return "img/räkä4.png"
    elif räkä == 5:
        return "img/räkä5.png"
    
def correct_scale(set_x, set_y): # returns the correct scale for the image
    return set_x * var.screen_width / 1920*0.8, set_y * var.screen_height / 1080*0.8


def start_new_level(player, enemies, bullets):
    var.difficulty = 10
    var.ticks = 0
    var.cooldown = 0
    var.cooldown_time = var.cooldown_time
    var.round = 0

    var.ammo_max = var.ammo_max  # can buy upgrades to increase this
    var.ammo = var.ammo_max
    var.firerate_max = var.firerate_max  # can buy upgrades to decrease this
    var.reload_time_max = var.reload_time_max  # can buy upgrades to decrease this
    var.player_health = var.player_health  # can buy upgrades to increase this
    var.gun_damage = var.gun_damage  # can buy upgrades to increase this
    player.set_health(var.player_health)
    player.set_x(var.screen_width / 2)
    player.set_y(var.screen_height / 2)
    player.set_speed(var.player_speed)

    enemies.clear()
    bullets.clear()
    var.game_running = True
    var.start_round = False

def buy_menu(screen, player, enemies, bullets):
    pygame.mouse.set_visible(True)
    
    # buttons to upgrade player, ammo, firerate, reload time, gun damage
    buttons = ["Ammo", "Firerate", "Reload time", "Gun damage", "Health", "START"]

    # button positions
    button_pos = []
    for i in range(len(buttons)):
        # add buttons to te center of the screen
        button_pos.append(pygame.math.Vector2(0, 0))
        button_pos[i].x = var.screen_width - 280
        button_pos[i].y = var.screen_height / 2 - 200 + 150 * i
        button_pos[i].x, button_pos[i].y = correct_scale(button_pos[i].x, button_pos[i].y)
        
        
    # button sizes
    button_size = pygame.math.Vector2(0, 0)
    button_size.x = 400
    button_size.y = 120
    button_size.x, button_size.y = correct_scale(button_size.x, button_size.y)
    font_size = 30
    desc_font_size = 20
    # button rects
    button_rects = []
    for i in range(len(buttons)):
        button_rects.append(pygame.Rect(0, 0, 0, 0))
        button_rects[i].center = button_pos[i]
        button_rects[i].size = button_size
        

    # button texts
    button_texts = []
    for i in range(len(buttons)):
        text = pygame.font.SysFont("Arial", font_size).render(
            buttons[i], True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rects[i].center)
        button_texts.append((text, text_rect))
        
    # button info, for telling how many upgrades you have and you can buy
    # var.ammo_max_limit, var.firerate_max_limit, var.reload_time_max_limit, var.gun_damage_max_limit, var.player_max_health
    button_info = []
    offset_y = -20
    for i in range(len(buttons)):
        if buttons[i] == "Ammo":
            text = pygame.font.SysFont("Arial", desc_font_size).render(
                "Upgrades: " + str(var.ammo_max) + "/" + str(var.ammo_max_limit), True, (0, 0, 0))
            text_rect = text.get_rect(center=button_rects[i].center - pygame.math.Vector2(0, offset_y))
            button_info.append((text, text_rect))
        elif buttons[i] == "Firerate":
            text = pygame.font.SysFont("Arial", desc_font_size).render(
                "Upgrades: " + str(var.firerate_max) + "/" + str(var.firerate_max_limit), True, (0, 0, 0))
            text_rect = text.get_rect(center=button_rects[i].center - pygame.math.Vector2(0, offset_y))
            button_info.append((text, text_rect))
        elif buttons[i] == "Reload time":
            text = pygame.font.SysFont("Arial", desc_font_size).render(
                "Upgrades: " + str(var.reload_time_max) + "/" + str(var.reload_time_max_limit), True, (0, 0, 0))
            text_rect = text.get_rect(center=button_rects[i].center - pygame.math.Vector2(0, offset_y))
            button_info.append((text, text_rect))
        elif buttons[i] == "Gun damage":
            text = pygame.font.SysFont("Arial", desc_font_size).render(
                "Upgrades: " + str(var.gun_damage) + "/" + str(var.gun_damage_max_limit), True, (0, 0, 0))
            text_rect = text.get_rect(center=button_rects[i].center - pygame.math.Vector2(0, offset_y))
            button_info.append((text, text_rect))
        elif buttons[i] == "Health":
            text = pygame.font.SysFont("Arial", desc_font_size).render(
                "Upgrades: " + str(var.player_health) + "/" + str(var.player_health_max_limit), True, (0, 0, 0))
            text_rect = text.get_rect(center=button_rects[i].center - pygame.math.Vector2(0, offset_y))
            button_info.append((text, text_rect))
        elif buttons[i] == "START":
            text = pygame.font.SysFont("Arial", desc_font_size).render(
                "", True, (0, 0, 0))
            text_rect = text.get_rect(center=button_rects[i].center - pygame.math.Vector2(0, offset_y))
            button_info.append((text, text_rect))
    
        
    #if clicked
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(buttons)):
                if button_rects[i].collidepoint(mouse_pos):
                    print("clicked")
                    if buttons[i] == "Ammo":
                        if var.coins >= 1:
                            var.coins -= 1
                            var.ammo_max += 1
                            var.ammo = var.ammo_max
                            print("Ammo upgraded")
                    elif buttons[i] == "Firerate":
                        if var.coins >= 1:
                            var.coins -= 1
                            var.firerate_max -= 0.01
                            print("Firerate upgraded")
                    elif buttons[i] == "Reload time":
                        if var.coins >= 1:
                            var.coins -= 1
                            var.reload_time_max -= 0.1
                            print("Reload time upgraded")
                    elif buttons[i] == "Gun damage":
                        if var.coins >= 1:
                            var.coins -= 1
                            var.gun_damage += 1
                            print("Gun damage upgraded")
                    elif buttons[i] == "Health":
                        if var.coins >= 1:
                            var.coins -= 1
                            var.player_health += 1
                            print("Health upgraded")
                    elif buttons[i] == "START":
                        start_new_level(player, enemies, bullets)
                        print("Round started")
                        return
                            
    # render buttons
    for i in range(len(buttons)):
        pygame.draw.rect(screen, (255, 255, 255), button_rects[i])
        screen.blit(button_texts[i][0], button_texts[i][1])
        screen.blit(button_info[i][0], button_info[i][1])
