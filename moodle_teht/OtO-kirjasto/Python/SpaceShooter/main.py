import pygame
import math, functions, var, roundsys, menu_screen
from enemy import Enemy
from player import Player
from audio_manager import AudioManager
from shop import shop_menu_btns
from explosion import Explosion

# Initialize pygame
pygame.init()
# SETUP PYGAME VARIABLES
clock = pygame.time.Clock()
dt = clock.tick(var.FPS) / 1000

# Set up the display
fullscreen = pygame.FULLSCREEN
screen = pygame.display.set_mode((var.screen_width, var.screen_height), pygame.DOUBLEBUF)
pygame.display.set_caption("PIG Defenders")

# Load SPRITES
enemies    = []
bullets    = []
explosions = []
# PLAYER
player = Player(var.screen_width / 2,
                       var.screen_height / 2, 300, "img/räkä alus.png", var.player_health, "raka_ase", "MK1")
player.set_upgrade("raka_ase", "MK1")

# BG
bg_image = pygame.image.load("img/bg_space.png").convert()
bg_image = pygame.transform.scale(
    bg_image, (var.screen_width*2.3, var.screen_height*2.3))
bg_rect = bg_image.get_rect()
bg_rect.center = (var.screen_width, var.screen_height)

# Crosshair
crosshair_image = pygame.image.load("img/crosshair.png")
crosshair_image = pygame.transform.scale(crosshair_image, (50, 50))

# ENEMY
def spawn_enemy():
    enemies.append(Enemy(*functions.spawn_enemy(), var.enemy_speed, "img/enemy.png", 100, 1, 10))
    
enemies_to_spawn = 1
def spawn_enemies(num):
    for _ in range(num):
        spawn_enemy()

def draw_health_bar(screen, current_health, max_health):
    bar_width = int((current_health / max_health) * 200)
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 200, 20))
    pygame.draw.rect(screen, (0, 255, 0), (50, 50, bar_width, 20))

def draw_enemy_health_bar(screen, current_health, max_health, enemy):
    offset_x = -30
    offset_y = 80
    width = 25
    height = 5
    bar_width = int((current_health / max_health) * width)
    pygame.draw.rect(screen, (255, 0, 0), (enemy.x - offset_x +
                     var.camera_offset.x, enemy.y + var.camera_offset.y + offset_y, width, height))
    pygame.draw.rect(screen, (0, 255, 0), (enemy.x - offset_x + var.camera_offset.x,
                     enemy.y + offset_y + var.camera_offset.y, bar_width, height))
        
# audio
bg_channel = pygame.mixer.Channel(0)
bg_audio = AudioManager()

shots_channel = pygame.mixer.Channel(1)
shots_audio = AudioManager()

def change_bg_music(song):
    if song == "menu" and var.current_bg_song != "menu":
        var.current_bg_song = "menu"
        bg_channel.play(bg_audio.load_sound("sfx/pig_d_1_1.mp3"), -1)
        bg_audio.set_volume(bg_channel, var.bg_volume)
    elif song == "game" and var.current_bg_song != "game":
        var.current_bg_song = "game"
        bg_channel.play(bg_audio.load_sound("sfx/pig_d_3_1.mp3"), -1)
        bg_audio.set_volume(bg_channel, var.bg_volume)
    elif song == "shop" and var.current_bg_song != "shop":
        var.current_bg_song = "shop"
        bg_channel.play(bg_audio.load_sound("sfx/shopkeep.mp3"), -1)
        bg_audio.set_volume(bg_channel, var.bg_volume)

def distance_multiplier(x1, y1, x2, y2):
    return 1 - (math.sqrt((x1 - x2)**2 + (y1 - y2)**2) / var.screen_width)

# Game loopww
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    if var.game_running:
        screen.fill((0, 0, 0))
        
        change_bg_music("game")
        # Draw the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player.y > 0: # UP
            player.y -= player.speed * dt
        if keys[pygame.K_s] and player.y < var.screen_height: # DOWN
            player.y += player.speed * dt
        if keys[pygame.K_a] and player.x > 0: # LEFT
            player.x -= player.speed * dt
        if keys[pygame.K_d] and player.x < var.screen_width: # RIGHT
            player.x += player.speed * dt
        if keys[pygame.K_r] and var.ammo != var.ammo_max:
            var.ammo = 0
        if keys[pygame.K_o]:
            healthed = player.get_health() - 1
            player.set_health(healthed)
        if keys[pygame.K_F11]:
            if screen.get_flags() & pygame.FULLSCREEN:
                pygame.display.set_mode((var.screen_width, var.screen_height), pygame.DOUBLEBUF)
            else:
                screen = pygame.display.set_mode((var.screen_width, var.screen_height), pygame.DOUBLEBUF | fullscreen)
            
        # SWITCH WEAPON
        if keys[pygame.K_1]:
            player.set_upgrade("raka_ase", "MK1")
        if keys[pygame.K_2]:
            player.set_upgrade("kakku_sinko", "MK1")
            
        if keys[pygame.K_4]:
            player.set_upgrade("raka_ase", "MK1")
        if keys[pygame.K_5]:
            player.set_upgrade("raka_ase", "MK2")
        if keys[pygame.K_6]:
            player.set_upgrade("raka_ase", "MK3")
        if keys[pygame.K_7]:
            player.set_upgrade("raka_ase", "MK4")
        if keys[pygame.K_8]:
            player.set_upgrade("raka_ase", "MK5")
        if keys[pygame.K_j]:
            spawn_enemy()
            
        # Get mouse position
        var.mouse_x, var.mouse_y = pygame.mouse.get_pos()

        # rotate the player to face the mouse
        player_to_mouse_x = var.mouse_x - player.x
        player_to_mouse_y = var.mouse_y - player.y
        angle = math.atan2(player_to_mouse_y, player_to_mouse_x)
        angle = math.degrees(angle)
        rotated_player = pygame.transform.rotate(player.image, -angle)
        player.rect = rotated_player.get_rect(center=(player.x, player.y))
        
        # SHOOT
        if pygame.mouse.get_pressed()[0] and not var.buy_round:
            if var.firerate <= 0 and var.ammo > 0:
                var.firerate = var.firerate_max
                var.ammo -= 1
                bullets.append(player.shoot(angle))
                shots_channel.play(shots_audio.load_sound("sfx/laser.mp3"))
                             
        # CAMERA OFFSET
        var.camera_offset = pygame.math.Vector2(
            var.screen_width // var.play_area - player.x, var.screen_height // var.play_area - player.y)
        
        # DRAW SPRITES
        screen.blit(bg_image, (bg_rect.x + var.camera_offset.x, bg_rect.y + var.camera_offset.y))

        for bullet in bullets:
            bullet.draw(screen)
            bullet.update(dt)

            for _enemy_ in enemies:
                # if bullet plus camera_offset collides with enemy, remove bullet and enemy
                bullet_rect = bullet.get_rect()
                enemy_rect = _enemy_.get_rect()
                if bullet_rect.colliderect(enemy_rect):
                    if bullet in bullets:
                        if bullet.get_gun_type() == "raka_ase":
                            bullets.remove(bullet)
                            if _enemy_.hitted(bullet.get_damage(), bullet):
                                enemies.remove(_enemy_)
                                var.coins += 5
                            
                        elif bullet.get_gun_type() == "kakku_sinko":
                            enemy_x = _enemy_.get_x()
                            enemy_y = _enemy_.get_y()
                            explosions.append(Explosion(enemy_x - 80, enemy_y - 50, 100))
                            bullets.remove(bullet)
                            # damage enemies in radius
                            for _enemy_2_ in enemies:
                                enemy_x2 = _enemy_2_.get_x()
                                enemy_y2 = _enemy_2_.get_y()
                                if math.sqrt((enemy_x - enemy_x2)**2 + (enemy_y - enemy_y2)**2) < 180:
                                    if _enemy_2_.hitted(bullet.get_damage() * distance_multiplier(enemy_x, enemy_y, enemy_x2, enemy_y2), bullet):
                                        enemies.remove(_enemy_2_)
                                        var.coins += 5
                                    else:
                                        print(
                                            str(var.ticks) + str(_enemy_2_) + " Enemy survived explosion")
                                else:
                                    print(str(var.ticks) + str(_enemy_2_) + " Enemy too far away from explosion")

                    break
                
        # render explosion
        for explosion in explosions:                  
            explosion.draw(screen)
            explosion.update()
            if explosion.done:
                explosions.remove(explosion)
                
        # detect collision between player and enemy
        for _enemy_ in enemies:
            # if enemy plus camera_offset is near player_pos, remove enemy
            enemy_y = _enemy_.get_y()
            enemy_x = _enemy_.get_x()
            player_y = var.player_pos.y
            player_x = var.player_pos.x
            if math.sqrt((enemy_x - player_x)**2 + (enemy_y - player_y)**2) < 90 and var.invincibility_time <= 0:
                enemies.remove(_enemy_)
                if player.hitted(_enemy_.get_damage()):
                    var.game_running = False
                    print("GAME OVER")
        
        if player.is_dead():
            var.game_running = False
            print("GAME OVER")
            
        # FOREGROUND
        draw_health_bar(screen, player.get_health(), player.get_max_health())
        for _enemy_ in enemies:
            # update and draw, but make sure that enemys cannot overlap with each other
            _enemy_.update(dt, enemies)
            _enemy_.draw(screen)
            draw_enemy_health_bar(screen, _enemy_.get_health(), _enemy_.get_max_health(), _enemy_)
                
        if var.invincibility_time > 0:
            # flash the player
            if var.invincibility_time % 0.1 < 0.05:
                player.draw(screen, player.rect, rotated_player)
        else:
            player.draw(screen, player.rect, rotated_player)

        # BUY ROUND
        if var.buy_round:       
            functions.start_menu_btns(screen)            
        else:
            pygame.mouse.set_visible(False)
            screen.blit(crosshair_image, (var.mouse_x - crosshair_image.get_width() / 2, var.mouse_y - crosshair_image.get_height() / 2))
        
        # # DEBUG
        # # draw rect around player
        # pygame.draw.rect(screen, (255, 0, 0), player.rect, 2)
        # # draw players center
        # pygame.draw.circle(screen, (255, 0, 0), player.get_center(), 2)

        # # draw rect around enemy
        # for _enemy_ in enemies:
        #     pygame.draw.rect(screen, (255, 0, 0), _enemy_.rect, 2)

        # # draw rect around bullet
        # for bullet in bullets:
        #     pygame.draw.rect(screen, (255, 0, 0), bullet.rect, 2)
        #     pygame.draw.circle(screen, (255, 0, 0), bullet.get_center(), 2)

        # INVICIBILITY
        if var.invincibility_time > 0:
            var.invincibility_time -= dt
        
            
        # FIRERATE
        var.firerate -= dt
        # RELOAD
        if var.ammo <= 0:
            var.reload_time -= dt
            if var.reload_time <= 0:
                var.ammo = var.ammo_max
                var.reload_time = var.reload_time_max
        
        # ROUND SYSTEM
        if round(var.ticks,2) == round(var.round_start_interval, 2) and not var.buy_round:
            print("Next round")
            roundsys.next_round()
            
        if var.start_round and not var.buy_round:
            if var.ticks >= var.cooldown + var.cooldown_time:
                prev_ticks = var.ticks
                var.start_round = False
                roundsys.calculate_difficulty()
                enemies_to_spawn += roundsys.calculate_enemy_spawn_amount()
                # spawn_enemies(roundsys.calculate_enemy_spawn_amount())
                print("\nRound: ", var.round, " >> Difficulty: ", var.difficulty, " >> Enemy Spawn Amount: ", roundsys.calculate_enemy_spawn_amount())
                print(enemies_to_spawn, " enemies left to spawn")
                
        
        if enemies_to_spawn > 0:
            if var.ticks >= var.cooldown + var.cooldown_time:
                spawn_enemies(1)
                enemies_to_spawn -= 1
                var.cooldown = var.ticks
                if enemies_to_spawn < 0:
                    enemies_to_spawn += 1
                print("Spawned enemy, ", enemies_to_spawn, " enemies left to spawn")
                
        roundsys.check_round(enemies)
        
        pygame.display.set_caption("PIG Defenders - Ticks: " + 
                                    str(round(var.ticks))+ " FPS: " + 
                                    str(round(clock.get_fps())) + " Round: " + 
                                    str(var.round) + " Difficulty: " + str(var.difficulty) + 
                                    " Enemy Amount: " + str(roundsys.calculate_enemy_spawn_amount()) + 
                                    " Health: " + str(player.get_health()) + " Ammo: " + str(var.ammo) + 
                                    " Firerate: " + str(var.firerate_max) + " Reload: " +
                                    str(round(var.reload_time)) + " Coins: " + str(var.coins) +
                                     " INTER" + str(var.round_start_interval) + " spawn: " + str(enemies_to_spawn)
                                    )
    else:
        if var.start_game_animation:
            menu_screen.background_zoom_animation(screen)
            
        pygame.mouse.set_visible(True)
        enemies_to_spawn = 0
        # DRAW MENU
        screen.fill((34, 0, 0))
        if var.shop_open:
            change_bg_music("shop")
            shop_menu_btns(screen)
        else:
            change_bg_music("menu")
            menu_screen.main_screen(screen, player, enemies, bullets)

        
    # Update the display
    dt = clock.tick(var.FPS) / 1000
    var.ticks += 1 / var.FPS
    pygame.display.flip()

# Quit the game
pygame.quit()
