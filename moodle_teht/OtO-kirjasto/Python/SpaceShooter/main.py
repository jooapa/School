import pygame, math, functions
import enemy, var, player, roundsys, time
    
# Initialize pygame
pygame.init()

# Set up the display
fullscreen = pygame.FULLSCREEN
screen = pygame.display.set_mode((var.screen_width, var.screen_height))
FPS = 60
pygame.display.set_caption("PIG Invaders")

# Load SPRITES
enemies = []
bullets = []

# PLAYER
player = player.Player(var.screen_width / 2,
                       var.screen_height / 2, 300, "img/räkä alus.png")

# BG
bg_image = pygame.image.load("img/bg.png")
bg_image = pygame.transform.scale(
    bg_image, (var.screen_width*2, var.screen_height*2))
bg_rect = bg_image.get_rect()
bg_rect.center = (0 , 0)

# Crosshair
crosshair_image = pygame.image.load("img/crosshair.png")
crosshair_image = pygame.transform.scale(crosshair_image, (50, 50))

# ENEMY
def spawn_enemy():
    enemies.append(enemy.Enemy(*functions.spawn_enemy(), 200))
def spawn_enemies(num):
    for _ in range(num):
        spawn_enemy()

# SETUP PYGAME VARIABLES
clock = pygame.time.Clock()
dt = clock.tick(FPS) / 1000

# Game loopww
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
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
    if pygame.mouse.get_pressed()[0]:
        if var.firerate <= 0 and var.ammo > 0:
            var.firerate = var.firerate_max
            var.ammo -= 1
            bullets.append(player.shoot(angle))
            
        
    # CAMERA OFFSET
    var.camera_offset = pygame.math.Vector2(
        var.screen_width // 2 - player.x, var.screen_height // 2 - player.y)
    
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
                    bullets.remove(bullet)
                enemies.remove(_enemy_)
                var.coins += 1
                break

    for _enemy_ in enemies:
        _enemy_.draw(screen)
        _enemy_.update(dt)

    # detect collision between player and enemy
    for _enemy_ in enemies:
        # if enemy plus camera_offset is near player_pos, remove enemy
        enemy_y = _enemy_.get_y()
        enemy_x = _enemy_.get_x()
        player_y = var.player_pos.y
        player_x = var.player_pos.x
        if math.sqrt((enemy_x - player_x)**2 + (enemy_y - player_y)**2) < 90:
            enemies.remove(_enemy_)
            var.coins += 1

    player.draw(screen, player.rect, rotated_player)

    # Draw the mouse
    screen.blit(crosshair_image, (var.mouse_x - crosshair_image.get_width() / 2, var.mouse_y - crosshair_image.get_height() / 2))
    pygame.mouse.set_visible(False)
    
    # FIRERATE
    var.firerate -= dt
    # RELOAD
    if var.ammo <= 0:
        var.reload_time -= dt
        if var.reload_time <= 0:
            var.ammo = var.ammo_max
            var.reload_time = var.reload_time_max

    if var.start_round:
        # round starts when ticks is from the current ticks 5 seconds
        if var.ticks >= var.cooldown + var.cooldown_time:
            prev_ticks = var.ticks
            var.start_round = False
            roundsys.calculate_difficulty()
            roundsys.calculate_enemy_spawn_amount()
            spawn_enemies(roundsys.calculate_enemy_spawn_amount())
            print("Round: ", var.round, " >> Difficulty: ", var.difficulty, " >> Enemy Spawn Amount: ", roundsys.calculate_enemy_spawn_amount())

    print('\r>> Ammo: ', var.ammo, " >> Firerate: ", var.firerate, " >> Reload Time: ", var.reload_time, end='')
    # Update the display
    dt = clock.tick(FPS) / 1000
    var.ticks += 1 / FPS
    pygame.display.set_caption("PIG Invaders - Ticks: " + str(round(var.ticks))+ "prev_ticks: " + str(round(var.cooldown)))
    pygame.display.flip()
    roundsys.check_round(enemies)


# Quit the game
pygame.quit()
