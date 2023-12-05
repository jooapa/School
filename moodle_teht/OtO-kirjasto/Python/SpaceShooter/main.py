import pygame, math, functions
import enemy, var, player
    
# Initialize pygame
pygame.init()


# Set up the display
fullscreen = pygame.FULLSCREEN
screen = pygame.display.set_mode((var.screen_width, var.screen_height))

pygame.display.set_caption("PIG Invaders")

# Load SPRITES
enemys = []
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
for i in range(10):
    enemys.append(enemy.Enemy(*functions.spawn_enemy(), 0))

# SETUP PYGAME VARIABLES
clock = pygame.time.Clock()
dt = clock.tick(60) / 1000


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
    if keys[pygame.K_w] and player.y > 0:
        player.y -= player.speed * dt
    if keys[pygame.K_s] and player.y < var.screen_height - player.image.get_height():
        player.y += player.speed * dt
    if keys[pygame.K_a] and player.x > 0:
        player.x -= player.speed * dt
    if keys[pygame.K_d] and player.x < var.screen_width - player.image.get_width():
        player.x += player.speed * dt

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
        bullets.append(player.shoot(angle))
        
    # CAMERA OFFSET
    var.camera_offset = pygame.math.Vector2(
        var.screen_width // 2 - player.x, var.screen_height // 2 - player.y)
    
    # DRAW SPRITES
    screen.blit(bg_image, (bg_rect.x + var.camera_offset.x, bg_rect.y + var.camera_offset.y))
    for enemy in enemys:
        enemy.draw(screen, var.camera_offset)
        enemy.update(dt)

    for bullet in bullets:
        bullet.draw(screen)
        bullet.update(dt)
        if bullet.x > var.screen_width + 300 or bullet.x < -300 or bullet.y > var.screen_height + 300 or bullet.y < -300:
            bullets.remove(bullet)

    player.draw(screen, player.rect, rotated_player)

    # Draw the mouse
    screen.blit(crosshair_image, (var.mouse_x - crosshair_image.get_width() / 2, var.mouse_y - crosshair_image.get_height() / 2))
    pygame.mouse.set_visible(False)
    # Update the display
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    pygame.display.set_caption("PIG Invaders - FPS: " + str(int(clock.get_fps())))

# Quit the game
pygame.quit()
