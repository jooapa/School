import pygame
import math, functions, var, roundsys, menu_screen, random, intro, outro, shop, save_file
from enemy import Enemy
from player import Player
from audio_manager import AudioManager, MusicManager
from shop import shop_menu_btns
from explosion import Explosion
from roundsys import calculate_enemy_health
import ui_screen

# Initialize pygame
pygame.init()
pygame.display.set_icon(pygame.image.load("img/icon.png"))
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

## ENDING VARIABLES

## SAVING
first_save = False

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
cursor_image = pygame.image.load("img/cursor.png").convert_alpha()
cursor_image = pygame.transform.scale(cursor_image, (50, 50))

# DASH VARS
dash_direction = pygame.math.Vector2(0, 0)
dash_direction.x = 0
dash_direction.y = 0

def random_enemy_image():
    if random.randint(0, 1) == 0:
        return "img/enemy.png"
    else:
        return "img/shooter.png"
    
# ENEMY
def spawn_enemy():
    enemies.append(Enemy(*functions.spawn_enemy(), var.enemy_speed,
                   random_enemy_image(), calculate_enemy_health(), 1, 10))
    
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
    elif song == "bad" and var.current_bg_song != "bad":
        var.current_bg_song = "bad"
        if keep_position:
            bg_audio.play_music(bg_audio.load_music("sfx/bad_ending.mp3"))
            pygame.mixer.music.set_pos(var.total_bg_music_position)
        else:
            bg_audio.play_music(bg_audio.load_music("sfx/bad_ending.mp3"))
        bg_audio.set_volume(bg_audio, var.bg_volume)
    elif song == "good" and var.current_bg_song != "good":
        var.current_bg_song = "good"
        if keep_position:
            bg_audio.play_music(bg_audio.load_music("sfx/good_ending.mp3"))
            pygame.mixer.music.set_pos(var.total_bg_music_position)
        else:
            bg_audio.play_music(bg_audio.load_music("sfx/good_ending.mp3"))
        bg_audio.set_volume(bg_audio, var.bg_volume)
    elif song == "very bad" and var.current_bg_song != "very bad":
        var.current_bg_song = "very bad"
        if keep_position:
            bg_audio.play_music(bg_audio.load_music("sfx/very_bad_ending.mp3"))
            pygame.mixer.music.set_pos(var.total_bg_music_position)
        else:
            bg_audio.play_music(bg_audio.load_music("sfx/very_bad_ending.mp3"))
        bg_audio.set_volume(bg_audio, var.bg_volume)
    elif song == "history" and var.current_bg_song != "history":
        var.current_bg_song = "history"
        if keep_position:
            bg_audio.play_music(bg_audio.load_music("sfx/history.mp3"))
            pygame.mixer.music.set_pos(var.total_bg_music_position)
        else:
            bg_audio.play_music(bg_audio.load_music("sfx/history.mp3"))
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
pygame.mouse.set_visible(False)

# FIRST LOAD
save_file.load_variables()

coins_collected = 0
enemies_killed = 0

on_final_round = False

while running:
    
        
    # start bad ending
    if var.round == var.bad_ending_round:
        on_final_round = True
        
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
        elif var.current_bg_song == "bad":
            bg_audio.play_music(bg_audio.load_music("sfx/bad_ending.mp3"))
        elif var.current_bg_song == "good":
            bg_audio.play_music(bg_audio.load_music("sfx/good_ending.mp3"))
        elif var.current_bg_song == "very bad":
            bg_audio.play_music(bg_audio.load_music("sfx/very_bad_ending.mp3"))
        elif var.current_bg_song == "history":
            bg_audio.play_music(bg_audio.load_music("sfx/history.mp3"))
    
        bg_audio.set_volume(bg_audio, var.bg_volume)
        
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and outro.outro_type == "" and not var.history_open and not on_final_round and not var.tutorial_open:
                if not shop.have_tsar_bomba:
                    if not intro.intro_done:
                        intro.intro_done = True
                    else:
                        var.paused = not var.paused
                        var.bg_music_position = pygame.mixer.music.get_pos() / 1000
                        var.total_bg_music_position += var.bg_music_position
                        
                        if var.paused:
                            change_bg_music("paused", True)
                            mouse_pos_beffore_pause = pygame.mouse.get_pos()
                        else:
                            change_bg_music("game", True)
                            pygame.mouse.set_pos(mouse_pos_beffore_pause)
                        
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
                var.firerate_max = var.raka_ase[player.get_upgrade()]["Fire Rate"]
                var.firerate = var.firerate_max
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
                var.firerate_max = var.kakku_sinko[player.get_upgrade()]["Fire Rate"]
                var.firerate = var.firerate_max
            player.set_upgrade("kakku_sinko", var.current_kakku_sinko_upgrade)

        if keys[pygame.K_j]:
            spawn_enemy()
        if keys[pygame.K_k]:
            ui_screen.speak()

        if var.paused and not shop.have_tsar_bomba and not on_final_round:
            var.dt_kerroin_miska_edition = 0
        else:
            var.dt_kerroin_miska_edition = 1
            change_bg_music("game")
            
        # Get mouse position
        var.mouse_x, var.mouse_y = pygame.mouse.get_pos()
        if not var.paused:
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
        
        # DASH
        if keys[pygame.K_LSHIFT] and not var.dashing and var.dash_cooldown_max >= var.dash_cooldown_time:
            var.dash_cooldown_max = -1
            var.dashing = True
            dash_direction.x = var.mouse_x - player.x
            dash_direction.y = var.mouse_y - player.y
            dash_direction.normalize_ip()
            dash_direction.x *= var.dash_speed
            dash_direction.y *= var.dash_speed
            
        if var.dashing:
            player.x += dash_direction.x * dt
            player.y += dash_direction.y * dt
            var.camera_offset = pygame.math.Vector2(
                var.screen_width // var.play_area - player.x, var.screen_height // var.play_area - player.y)
            if player.x> var.screen_width or player.x < 0 or player.y > var.screen_height or player.y < 0:
                var.dashing = False
                var.dash_cooldown_max = -1
            player.get_image().set_alpha(100)
        else:
            player.get_image().set_alpha(255)
                
        if var.dashing and var.dash_cooldown_max >= 0:
            var.dashing = False
        
        print(var.dashing, var.dash_cooldown_max, var.dash_indicator_fake_cooldown)
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
                                enemies_killed += 1
                                coins_collected += 5
                            
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
                                enemies_killed += 1
                                coins_collected += 5
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
                                        enemies_killed += 1
                                        coins_collected += 5
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
            # if enemy p
            enemy_y = _enemy_.get_y()
            enemy_x = _enemy_.get_x()
            player_y = var.player_pos.y
            player_x = var.player_pos.x
            if math.sqrt((enemy_x - player_x)**2 + (enemy_y - player_y)**2) < 90 and var.invincibility_time <= 0:
                if not var.dashing:  
                    enemies.remove(_enemy_)
                    player.hitted(_enemy_.get_damage())
                    ui_screen.hitted()
        
        if player.is_dead():
            save_file.history(var.round, coins_collected, enemies_killed)
            var.game_running = False
            var.round -= 1
            var.best_round = max(var.round, var.best_round)
            save_file.save_variables()
            enemies_killed = 0
            coins_collected = 0
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
        
        # DASH INCICATOR FAKE COOLDOWN using arc
        dash_cooldown_color = (255, 255, 255)
        dash_cooldown_radius = 30
        dash_cooldown_thickness = 5
        dash_cooldown_start_angle = 0
        dash_cooldown_end_angle = -2*math.pi * 4 * (var.dash_indicator_fake_cooldown / var.dash_cooldown_time)
        dash_cooldown_center = (var.screen_width - 50, var.screen_height - 50)
        pygame.draw.arc(screen, dash_cooldown_color, (dash_cooldown_center[0] - dash_cooldown_radius, dash_cooldown_center[1] - dash_cooldown_radius, dash_cooldown_radius * 2, dash_cooldown_radius * 2), dash_cooldown_start_angle, dash_cooldown_end_angle, dash_cooldown_thickness)
        
         
        # speaker speak
        if ui_screen.speaker_channel != None:
            if ui_screen.random_speker_time != 0:
                ui_screen.random_speker_time -= dt
                
            if ui_screen.random_speker_time <= 0:   
                ui_screen.speak()
                ui_screen.random_speker_time = ui_screen.pick_random_time_interval()
                
        # AMMO, bottom left corner, ammo / max ammo
        ammo_font = pygame.font.SysFont("Arial", 50)
        ammo_text = ammo_font.render(str(var.ammo) + " / " + str(var.ammo_max), True, (255, 255, 255))
        ammo_text_width = ammo_text.get_width()
        ammo_text_height = ammo_text.get_height()
        ammo_text_x = 10
        ammo_text_y = var.screen_height - ammo_text_height - 10
        screen.blit(ammo_text, (ammo_text_x, ammo_text_y))
        
        round_font = pygame.font.SysFont("Arial", 50)
        round_text = ammo_font.render("Round: " + str(var.round), True, (255, 255, 255))
        round_text_x = 10
        round_text_y = 10
        screen.blit(round_text, (round_text_x, round_text_y))

        ui_screen.render_coin_animation(screen, var.screen_width, 20, (255, 255, 255))
        
        # ENDING----------------------------------------
        if shop.have_tsar_bomba:
            
            var.paused = True
            
            # YEs or No button
            yes_button = pygame.Rect(0, 0, 200, 100)
            yes_button.center = (var.screen_width / 2 - 100, var.screen_height / 2)
            pygame.draw.rect(screen, (255, 255, 255), yes_button)
            yes_font = pygame.font.SysFont("Arial", 50)
            yes_text = yes_font.render("YES", True, (0, 0, 0))
            
            no_button = pygame.Rect(0, 0, 200, 100)
            no_button.center = (var.screen_width / 2 + 100, var.screen_height / 2)
            pygame.draw.rect(screen, (255, 255, 255), no_button)
            no_font = pygame.font.SysFont("Arial", 50)
            no_text = no_font.render("NO", True, (0, 0, 0))
            
            # draw text
            text_font = pygame.font.SysFont("Arial", 50)
            text = text_font.render("Launch Tsar?", True, (255, 255, 255))
            
            screen.blit(text, (var.screen_width / 2 - text.get_width() / 2, var.screen_height / 2 - text.get_height() / 2 - 100))
            screen.blit(yes_text, (yes_button.x + yes_button.width / 2 - yes_text.get_width() / 2, yes_button.y + yes_button.height / 2 - yes_text.get_height() / 2))
            screen.blit(no_text, (no_button.x + no_button.width / 2 - no_text.get_width() / 2, no_button.y + no_button.height / 2 - no_text.get_height() / 2))
            
            # handle buttons
            if pygame.mouse.get_pressed()[0]:
                if yes_button.collidepoint(pygame.mouse.get_pos()):
                    var.paused = False
                    outro.outro_type = "very bad"
                    var.very_bad_ending_completed = True
                    shop.have_tsar_bomba = False
                    change_bg_music("very bad")
                    var.game_running = False
                    outro.start(screen, dt)
                    screen.fill((0, 0, 0))

                elif no_button.collidepoint(pygame.mouse.get_pos()):
                    var.paused = False
                    outro.outro_type = "good"
                    var.good_ending_completed = True
                    shop.have_tsar_bomba = False
                    change_bg_music("good")
                    var.game_running = False
                    outro.start(screen, dt)
                    screen.fill((0, 0, 0))
                    
        if on_final_round:
            var.paused = True
            
            # YEs or No button
            yes_button = pygame.Rect(0, 0, 200, 100)
            yes_button.center = (var.screen_width / 2 - 100, var.screen_height / 2)
            pygame.draw.rect(screen, (255, 255, 255), yes_button)
            yes_font = pygame.font.SysFont("Arial", 50)
            yes_text = yes_font.render("YES", True, (0, 0, 0))
            
            no_button = pygame.Rect(0, 0, 200, 100)
            no_button.center = (var.screen_width / 2 + 100, var.screen_height / 2)
            pygame.draw.rect(screen, (255, 255, 255), no_button)
            no_font = pygame.font.SysFont("Arial", 50)
            no_text = no_font.render("NO", True, (0, 0, 0))
            
            win_text = "Congrats! You have reached round " + str(var.round) + "!\nDo you want to continue?\n"
            # draw text
            text_font = pygame.font.SysFont("Arial", 50)
            text = text_font.render(win_text, True, (255, 255, 255))
            
            screen.blit(text, (var.screen_width / 2 - text.get_width() / 2, var.screen_height / 2 - text.get_height() / 2 - 100))
            screen.blit(yes_text, (yes_button.x + yes_button.width / 2 - yes_text.get_width() / 2, yes_button.y + yes_button.height / 2 - yes_text.get_height() / 2))
            screen.blit(no_text, (no_button.x + no_button.width / 2 - no_text.get_width() / 2, no_button.y + no_button.height / 2 - no_text.get_height() / 2))
            
            # handle buttons
            if pygame.mouse.get_pressed()[0]:
                if yes_button.collidepoint(pygame.mouse.get_pos()):
                    var.paused = False
                    on_final_round = False
                    var.round += 1

                elif no_button.collidepoint(pygame.mouse.get_pos()):
                    save_file.history(var.round, coins_collected, enemies_killed)
                    var.game_running = False
                    var.round -= 1
                    var.best_round = max(var.round, var.best_round)
                    save_file.save_variables()
        
                    enemies_killed = 0
                    coins_collected = 0
                    var.bad_ending_completed = True
                    change_bg_music("bad")
                    outro.outro_type = "bad"
                    var.game_running = False

                    screen.fill((0, 0, 0))
                    
        # ENDING----------------------------------------
          
        if var.paused and not shop.have_tsar_bomba and not on_final_round:
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
            screen.blit(cursor_image, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))            
            # handle exit button
            if pygame.mouse.get_pressed()[0]:
                if exit_button.collidepoint(pygame.mouse.get_pos()):
                    player.set_health(0)
        else:
            if not shop.have_tsar_bomba and not on_final_round:
                screen.blit(crosshair_image, (var.mouse_x - crosshair_image.get_width() / 2, var.mouse_y - crosshair_image.get_height() / 2))
            else:
                screen.blit(cursor_image, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
            # Fire rate bar indicator
            if var.firerate >= 0:
                pygame.draw.arc(screen, (0, 255, 0), (var.mouse_x - 20, var.mouse_y - 20, 40, 40), math.pi / -2, math.pi * var.firerate / var.firerate_max + math.pi / -2, 5)

            # Reload bar indicator
            if var.reload_time != var.reload_time_max:
                # Draw the half circle
                pygame.draw.arc(screen, (255, 255, 0), (var.mouse_x - 20, var.mouse_y - 20, 40, 40), math.pi / 2, math.pi * var.reload_time / var.reload_time_max + math.pi / 2, 5)            
                  
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
            
        # DASH
        if var.dash_cooldown_max <= var.dash_cooldown_time:
            var.dash_cooldown_max += dt * 1.8
        
        # DASH INDICATOR FAKE COOLDOWN
        if var.dashing:
            if var.dash_indicator_fake_cooldown < 1:
                var.dash_indicator_fake_cooldown += dt * 1.8
            else:
                var.dash_indicator_fake_cooldown = 1
        else:
            if var.dash_indicator_fake_cooldown > 0:
                var.dash_indicator_fake_cooldown -= dt * 1.8
            else:
                var.dash_indicator_fake_cooldown = 0
        
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
        if round(var.ticks, 2) >= round(var.round_start_interval, 2) and not var.buy_round:
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
                                        " kakku: " + var.current_kakku_sinko_upgrade +
                                        " Best round" + str(var.best_round)
                                    )
    elif var.game_running == False and intro.intro_done:
        pygame.display.set_caption("PIG Defenders - FPS " + str(round(clock.get_fps())))
        if not outro.outro_type == "":
            outro.start(screen, dt)
        else:
            if var.start_game_animation:
                menu_screen.background_zoom_animation(screen)
            else:
                enemies_to_spawn = 0
                # DRAW MENU
                screen.fill((34, 0, 0))
                if var.shop_open:
                    change_bg_music("shop")
                    shop_menu_btns(screen)
                elif var.history_open:
                    change_bg_music("history")
                    ui_screen.history_screen(screen)
                elif var.tutorial_open:
                    ui_screen.tutorial_screen(screen)
                else:
                    change_bg_music("menu")
                    menu_screen.main_screen(screen, player, enemies, bullets)
                    
        if outro.outro_type == "":
            screen.blit(cursor_image, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        
    # Update the display
    dt = (clock.tick(var.FPS) / 1000) * var.dt_kerroin_miska_edition
    if not var.paused:
        var.ticks += dt
    pygame.display.flip()

# Quit the game
pygame.quit()
