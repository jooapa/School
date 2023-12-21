import pygame
import math, functions, var, roundsys, menu_screen, random, intro
from enemy import Enemy
from player import Player
from audio_manager import AudioManager, MusicManager
from shop import shop_menu_btns
from explosion import Explosion
from roundsys import calculate_enemy_health
import ui_screen

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

# SMOKE EFFECT on player spawn
smoke = pygame.image.load("img/smoke.png")
smoke = pygame.transform.scale(
    smoke, (player.rect.width * 1.5, player.rect.height * 1.5))
smoke_rect = smoke.get_rect(center=(player.x, player.y))
smoke_rect.x = player.x
smoke_rect.y = player.y

# BG
bg_image = pygame.image.load("img/bg_space.png").convert()
bg_image = pygame.transform.scale(
    bg_image, (var.screen_width*2.3, var.screen_height*2.3))
bg_rect = bg_image.get_rect()
bg_rect.center = (var.screen_width, var.screen_height)

# Crosshair
crosshair_image = pygame.image.load("img/crosshair.png").convert_alpha()
crosshair_image = pygame.transform.scale(crosshair_image, (50, 50))

# ENEMY
def spawn_enemy():
    enemies.append(Enemy(*functions.spawn_enemy(), var.enemy_speed,
                   "img/enemy.png", calculate_enemy_health(), 1, 10))
    
enemies_to_spawn = 1
def spawn_enemies(num):
    for _ in range(num):
        spawn_enemy()

def draw_health_bar(screen, current_health, max_health, x, y):
    bar_width = int((current_health / max_health) * 170)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 170, 15))
    pygame.draw.rect(screen, (0, 255, 0), (x, y, bar_width, 15))

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
bg_audio = MusicManager()

shots_channel = pygame.mixer.Channel(1)
shots_audio = AudioManager()

def change_bg_music(song, keep_position=False):
    if song == "menu" and var.current_bg_song != "menu":
        var.current_bg_song = "menu"
        if keep_position:
            bg_audio.play_music(bg_audio.load_music("sfx/menu.wav"))
            pygame.mixer.music.set_pos(var.total_bg_music_position)
        else:
            bg_audio.play_music(bg_audio.load_music("sfx/menu.wav"))
        bg_audio.set_volume(bg_audio, var.bg_volume)
    elif song == "game" and var.current_bg_song != "game":
        var.current_bg_song = "game"
        if keep_position:
            bg_audio.play_music(bg_audio.load_music("sfx/pigd4.mp3"))
            pygame.mixer.music.set_pos(var.total_bg_music_position)
        else:
            bg_audio.play_music(bg_audio.load_music("sfx/pigd4.mp3"))
        bg_audio.set_volume(bg_audio, var.bg_volume)
    elif song == "shop" and var.current_bg_song != "shop":
        var.current_bg_song = "shop"
        if keep_position:
            bg_audio.play_music(bg_audio.load_music("sfx/shopkeep.mp3"))
            pygame.mixer.music.set_pos(var.total_bg_music_position)
        else:
            bg_audio.play_music(bg_audio.load_music("sfx/shopkeep.mp3"))
        bg_audio.set_volume(bg_audio, var.bg_volume)
    elif song == "paused" and var.current_bg_song != "paused":
        var.current_bg_song = "paused"
        if keep_position:
            bg_audio.play_music(bg_audio.load_music("sfx/pigd4_2.mp3"))
            pygame.mixer.music.set_pos(var.total_bg_music_position)
        else:
            bg_audio.play_music(bg_audio.load_music("sfx/pigd4_2.mp3"))
        bg_audio.set_volume(bg_audio, var.bg_volume)
    elif song == "intro" and var.current_bg_song != "intro" and not intro.intro_done:
        var.current_bg_song = "intro"
        if keep_position:
            bg_audio.play_music(bg_audio.load_music("sfx/intro.mp3"))
            pygame.mixer.music.set_pos(var.total_bg_music_position)
        else:
            bg_audio.play_music(bg_audio.load_music("sfx/intro.mp3"))
        bg_audio.set_volume(bg_audio, var.bg_volume)


def speaker_speaker(speaker_audio, speaker_channel):
    speaker_channel.play(speaker_audio.load_sound("sfx/oinks/oink" + str(random.randint(1, 5)) + ".wav"))
    
def distance_multiplier(x1, y1, x2, y2):
    return 1 - (math.sqrt((x1 - x2)**2 + (y1 - y2)**2) / var.screen_width)

# ammo
player.set_kakku_sinko_ammo(
    var.kakku_sinko[player.get_upgrade()]["Magazine Size"])
player.set_raka_ase_ammo(
    var.raka_ase[player.get_upgrade()]["Magazine Size"])
var.ammo_max = var.raka_ase[player.get_upgrade()]["Magazine Size"]
var.ammo = var.ammo_max

# Game loopww
running = True
while running:

    # if music ender
    if pygame.mixer.music.get_busy() == 0:
        print("Music ended")
        if var.current_bg_song == "menu":
            bg_audio.play_music(bg_audio.load_music("sfx/menu.wav"))
        elif var.current_bg_song == "game":
            bg_audio.play_music(bg_audio.load_music("sfx/pigd4.mp3"))
            var.total_bg_music_position = 0
        elif var.current_bg_song == "shop":
            bg_audio.play_music(bg_audio.load_music("sfx/shopkeep.mp3"))
        elif var.current_bg_song == "paused":
            bg_audio.play_music(bg_audio.load_music("sfx/pigd4_2.mp3"))
            var.total_bg_music_position = 0
        elif var.current_bg_song == "intro":
            bg_audio.play_music(bg_audio.load_music("sfx/intro.mp3"))
        bg_audio.set_volume(bg_audio, var.bg_volume)
        
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not intro.intro_done:
                    intro.intro_done = True
                else:
                    var.paused = not var.paused
                    var.bg_music_position = pygame.mixer.music.get_pos() / 1000
                    var.total_bg_music_position += var.bg_music_position
                    
                    if var.paused:
                        change_bg_music("paused", True)
                    else:
                        change_bg_music("game", True)
                        
            if event.key == pygame.K_F11:
                    if screen.get_flags() & pygame.FULLSCREEN:
                        pygame.display.set_mode((var.screen_width, var.screen_height), pygame.DOUBLEBUF)
                
    change_bg_music("intro")
    intro.start(screen, dt)
    
    # Clear the screen
    if var.game_running:
        var.start_game_animation = False # stop zoom animation
        screen.fill((0, 0, 0))
        
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
        if keys[pygame.K_f]:
            print("Playdd")
            var.dt_kerroin_miska_edition = 0.5
        # SWITCH WEAPON
        if keys[pygame.K_1]:
            if player.gun == "kakku_sinko":
                player.set_kakku_sinko_ammo(
                    var.ammo)        
            elif player.gun == "raka_ase":
                player.set_raka_ase_ammo(
                    var.ammo)
            player.set_upgrade("raka_ase", var.current_raka_ase_upgrade)
        if keys[pygame.K_2]:
            if player.gun == "kakku_sinko":
                player.set_kakku_sinko_ammo(
                    var.ammo)
            elif player.gun == "raka_ase":
                player.set_raka_ase_ammo(
                    var.ammo)
            player.set_upgrade("kakku_sinko", var.current_kakku_sinko_upgrade)

        if keys[pygame.K_j]:
            spawn_enemy()
        if keys[pygame.K_k]:
            ui_screen.speak()

        if var.paused:
            var.dt_kerroin_miska_edition = 0
        else:
            var.dt_kerroin_miska_edition = 1
            change_bg_music("game")
            
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
        if pygame.mouse.get_pressed()[0] and not var.buy_round and not var.paused:
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
                            bullet_x  = bullet.get_x() - _enemy_.rect.width / 2
                            bullet_y = bullet.get_y() - _enemy_.rect.height / 2
                            # explosion rect at the center of the explosion
                            explosions.append(
                                Explosion(bullet.get_x(), bullet.get_y(), 200))
                            
                            bullet_damage = bullet.get_damage()
                            # hit the first enemy
                            _enemy_.hitted(bullet.get_damage(
                            ) * distance_multiplier(bullet_x, bullet_y, _enemy_.get_x(), _enemy_.get_y()), bullet)
                            if _enemy_.get_health() <= 0:
                                enemies.remove(_enemy_)
                                var.coins += 5
                                print(str(var.ticks) + str(_enemy_) + " Enemy killed by explosion")
                            else:
                                _enemy_.set_health(_enemy_.get_health() + bullet_damage)
                                
                            # damage enemies in radius
                            for _enemy_2_ in enemies:
                                enemy_x2 = _enemy_2_.get_x()
                                enemy_y2 = _enemy_2_.get_y()
                                if math.sqrt((bullet_x  - enemy_x2)**2 + (bullet_y - enemy_y2)**2) < 200:
                                    print(bullet_x , bullet_y, enemy_x2, enemy_y2, math.sqrt((bullet_x  - enemy_x2)**2 + (bullet_y - enemy_y2)**2))                                  
                                    if _enemy_2_.hitted(bullet.get_damage() * distance_multiplier(bullet_x , bullet_y, enemy_x2, enemy_y2), bullet):
                                        enemies.remove(_enemy_2_)
                                        var.coins += 5
                                        print(str(var.ticks) + str(_enemy_2_) + " Enemy killed by explosion")
                                    else:
                                        print(
                                            str(var.ticks) + str(_enemy_2_) + " Enemy survived explosion")
                                else:
                                    print(str(var.ticks) + str(_enemy_2_) + " Enemy too far away from explosion: " + str(
                                        math.sqrt((bullet_x  - enemy_x2)**2 + (bullet_y - enemy_y2)**2)) + " units")
                                    
                            bullets.remove(bullet)

                    break
                
        # render explosion
        for explosion in explosions:                  
            explosion.draw(screen)
            explosion.update(dt)
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
                player.hitted(_enemy_.get_damage())
                ui_screen.hitted()
        
        if player.is_dead():
            var.game_running = False
            pass
        
        # FOREGROUND
        draw_health_bar(screen, player.get_health(), player.get_max_health(), var.screen_width - 185, var.screen_height - 23)
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
        
        # SMOKE EFFECT first second start fade out
        if var.ticks < 2:
            smoke.set_alpha(255 - (255 / 1) * var.ticks)
            screen.blit(smoke, (smoke_rect.x - var.camera_offset.x - 620, smoke_rect.y - var.camera_offset.y - 420))
            

        
        # RENDER UI
        ui_screen.render(screen, ui_screen.move_mouth(), player)
        
        # speaker speak
        if ui_screen.speaker_channel != None:
            if ui_screen.random_speker_time != 0:
                ui_screen.random_speker_time -= dt
                
            if ui_screen.random_speker_time <= 0:   
                ui_screen.speak()
                ui_screen.random_speker_time = ui_screen.pick_random_time_interval()
        
        screen.blit(crosshair_image, (var.mouse_x - crosshair_image.get_width() / 2, var.mouse_y - crosshair_image.get_height() / 2))
        if var.paused:
            pygame.mouse.set_visible(True)
            info_font = pygame.font.SysFont("Arial", 50)
            info_text = info_font.render("Press ESC to continue", True, (255, 255, 255))
            
            screen.blit(info_text, (var.screen_width / 2 - info_text.get_width() / 2, var.screen_height / 2 - info_text.get_height() / 2 - 100))
        
            # exit button
            exit_button = pygame.Rect(0, 0, 200, 100)
            exit_button.center = (var.screen_width / 2, var.screen_height / 2 + 100)
            pygame.draw.rect(screen, (255, 255, 255), exit_button)
            exit_font = pygame.font.SysFont("Arial", 50)
            exit_text = exit_font.render("EXIT", True, (0, 0, 0))
            screen.blit(exit_text, (exit_button.x + exit_button.width / 2 - exit_text.get_width() / 2, exit_button.y + exit_button.height / 2 - exit_text.get_height() / 2))
            
            # handle exit button
            if pygame.mouse.get_pressed()[0]:
                if exit_button.collidepoint(pygame.mouse.get_pos()):
                    player.set_health(0)
        else:
            pygame.mouse.set_visible(False)
                  
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
        # start new round
        if round(var.ticks,2) == round(var.round_start_interval, 2) and not var.buy_round:
            print("Round start interval: ", var.round_start_interval)
            print("Next round")
            roundsys.next_round()
            # calculate cooldown time, so that the all the enemies are spawned before the next round
            # var.cooldown_time = 1 / roundsys.calculate_enemy_spawn_amount()
            
        if var.start_round and not var.buy_round:
            if var.ticks >= var.cooldown + var.cooldown_time:
                prev_ticks = var.ticks
                var.start_round = False
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
                                     " INTER" + str(round(var.round_start_interval)) + " spawn: " + str(enemies_to_spawn) +
                                     " raka ase: " + var.current_raka_ase_upgrade +
                                        " kakku: " + var.current_kakku_sinko_upgrade
                                    )
    elif var.game_running == False and intro.intro_done:
        if var.start_game_animation:
            menu_screen.background_zoom_animation(screen)
        else:
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
    dt = (clock.tick(var.FPS) / 1000) * var.dt_kerroin_miska_edition
    if not var.paused:
        var.ticks += 1 / var.FPS
    pygame.display.flip()

# Quit the game
pygame.quit()
