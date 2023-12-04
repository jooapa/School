import pygame, math, random, functions
import enemy, var
    
# Initialize pygame
pygame.init()


# Set up the display
fullscreen = pygame.FULLSCREEN
screen = pygame.display.set_mode((var.screen_width, var.screen_height))

pygame.display.set_caption("PIG Invaders")

# Load SPRITES
# PLAYER
player_image = pygame.image.load("img/pig.png")
player_image = pygame.transform.scale(player_image, (100, 100))

# PLAYER POSITION
player_x = var.screen_width / 2
player_y = var.screen_height / 2

# BG
bg_image = pygame.image.load("img/bg.png")
bg_image = pygame.transform.scale(
    bg_image, (var.screen_width*2, var.screen_height*2))

# Crosshair
crosshair_image = pygame.image.load("img/crosshair.png")
crosshair_image = pygame.transform.scale(crosshair_image, (50, 50))

# ENEMY
enemys = []
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
    if keys[pygame.K_w] and player_y > 0:
        player_y -= var.player_speed * dt
    if keys[pygame.K_s] and player_y < var.screen_height:
        player_y += var.player_speed * dt
    if keys[pygame.K_a] and player_x > 0:
        player_x -= var.player_speed * dt
    if keys[pygame.K_d] and player_x < var.screen_width:
        player_x += var.player_speed * dt

    # Get mouse position
    var.mouse_x, var.mouse_y = pygame.mouse.get_pos()

    # rotate the player to face the mouse
    player_to_mouse_x = var.mouse_x - player_x
    player_to_mouse_y = var.mouse_y - player_y
    angle = math.atan2(player_to_mouse_y, player_to_mouse_x)
    angle = math.degrees(angle)
    rotated_player = pygame.transform.rotate(player_image, -angle)
    player_rect = rotated_player.get_rect(center=(player_x, player_y))
    
    # CAMERA OFFSET
    var.camera_offset = pygame.math.Vector2(
        var.screen_width // 2 - player_rect.centerx, var.screen_height // 2 - player_rect.centery)
    # DRAW SPRITES
    screen.blit(bg_image, (0, 0), (player_rect.centerx - var.screen_width // 2,
                player_rect.centery - var.screen_height // 2, var.screen_width, var.screen_height))
    for enemy in enemys:
        enemy.draw(screen, var.camera_offset)
    screen.blit(rotated_player, player_rect)

    # Draw the mouse
    screen.blit(crosshair_image, (var.mouse_x - crosshair_image.get_width() / 2, var.mouse_y - crosshair_image.get_height() / 2))
    pygame.mouse.set_visible(False)
    # Update the display
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    pygame.display.set_caption("PIG Invaders - FPS: " + str(player_x) + " | " + str(player_y))

# Quit the game
pygame.quit()
