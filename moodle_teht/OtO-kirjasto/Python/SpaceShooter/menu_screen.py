import pygame, var, roundsys
from functions import correct_scale

def start_new_level(player, enemies, bullets):
    var.difficulty = 1
    var.ticks = 0
    var.cooldown = 0
    var.start_round = False
    var.cooldown_time = var.cooldown_time
    var.round = 30
    var.invincibility_time = 0
    var.paused = False

    var.ammo_max = var.ammo_max  # can buy upgrades to increase this
    var.ammo = var.ammo_max
    var.reload_time_max = var.reload_time_max  # can buy upgrades to decrease this
    var.reload_time = var.reload_time_max
    var.firerate_max = var.firerate_max  # can buy upgrades to decrease this
    var.player_health = var.player_health  # can buy upgrades to increase this
    var.gun_damage = var.gun_damage  # can buy upgrades to increase this
    player.set_health(var.player_health)
    player.set_x(var.screen_width / 2)
    player.set_y(var.screen_height / 2)
    player.set_speed(var.player_speed)

    enemies.clear()
    bullets.clear()
    var.start_game_animation = True


def create_buttons():
    buttons = ["TUTORIAL", "START", "SHOP", "QUIT", "FULLSCREEN"]
    button_pos = []
    for i in range(len(buttons)):
        button_pos.append(pygame.math.Vector2(0, 0))
        button_pos[i].x = var.screen_width + \
            400 * i - 300 * (len(buttons) - 1) / 2
        button_pos[i].y = var.screen_height / 2 + 120
        button_pos[i].x, button_pos[i].y = correct_scale(
            button_pos[i].x, button_pos[i].y)
        if buttons[i] == "QUIT":
            button_pos[i].y = var.screen_height - 50
            button_pos[i].x = var.screen_width - 50
        if buttons[i] == "FULLSCREEN":
            button_pos[i].y = 0
            button_pos[i].x = 0

    button_size = pygame.math.Vector2(0, 0)
    button_size.x = 300
    button_size.y = 300
    button_size.x, button_size.y = correct_scale(button_size.x, button_size.y)
    
    button_rects = []
    for i in range(len(buttons)):
        button_rects.append(pygame.Rect(0, 0, 0, 0))
        button_rects[i].center = button_pos[i]
        button_rects[i].size = button_size
        if buttons[i] == "QUIT":
            button_rects[i].size = pygame.math.Vector2(100, 100)
            button_rects[i].center = button_pos[i]
        if buttons[i] == "FULLSCREEN":
            button_rects[i].size = pygame.math.Vector2(100, 100)
            button_rects[i].center = button_pos[i]
            button_rects[i].x = button_pos[i].x
            button_rects[i].y = button_pos[i].y
            
    button_icons = []
    for i in range(len(buttons)):
        button_icons.append(pygame.image.load(
            "img/ico/" + buttons[i] + ".png").convert_alpha())
        button_icons[i] = pygame.transform.scale(
            button_icons[i], (button_rects[i].size[0], button_rects[i].size[1]))
        if buttons[i] == "QUIT":
            button_icons[i] = pygame.transform.scale(
                button_icons[i], (button_rects[i].size[0], button_rects[i].size[1]))

    return buttons, button_rects, button_icons


def render_main_buttons(screen, buttons, button_rects, button_icons):
    for i in range(len(buttons)):
        screen.blit(button_icons[i], button_rects[i])
    
def render_main_title(screen):
    title = pygame.image.load("img/title.png").convert_alpha()
    title = pygame.transform.scale(
        title, (1000, 150))
    title_rect = title.get_rect(center=(var.screen_width / 2, var.screen_height / 2 - 200))
    screen.blit(title, title_rect)
    
def handle_main_screen_buttons(buttons, button_rects, player, enemies, bullets, screen):
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(buttons)):
                if button_rects[i].collidepoint(mouse_pos):
                    if buttons[i] == "START":
                        start_new_level(player, enemies, bullets)
                        print("Round started")
                    elif buttons[i] == "SHOP":
                        var.shop_open = True
                        print("Shop opened")
                    elif buttons[i] == "TUTORIAL":
                        print("Tutorial opened")
                    elif buttons[i] == "QUIT":
                        pygame.quit()
                        quit()
                    elif buttons[i] == "FULLSCREEN":
                        if screen.get_flags() & pygame.FULLSCREEN:
                            pygame.display.set_mode((var.screen_width, var.screen_height), pygame.DOUBLEBUF)
                        else:
                            screen = pygame.display.set_mode(
                                (var.screen_width, var.screen_height), pygame.DOUBLEBUF | pygame.FULLSCREEN)
                    else:
                        print("Button not found")


def main_screen(screen, player, enemies, bullets):
    buttons, button_rects, button_icons = create_buttons()
    background = pygame.image.load("img/bg_space.png").convert_alpha()
    background = pygame.transform.scale(
        background, (var.screen_width, var.screen_height))
    screen.blit(background, (0, 0))
    render_main_title(screen)
    render_main_buttons(screen, buttons, button_rects, button_icons)
    handle_main_screen_buttons(buttons, button_rects, player, enemies, bullets, screen)


def background_zoom_animation(screen):
    bg_image = pygame.image.load("img/bg_space.png").convert()
    zoom_factor = 1
    zoom_speed = 0.05  # Adjust this value to change the speed of the zoom

    target_center = (var.screen_width // 2 + 130, var.screen_height // 1.5 - 50)
    current_center = list(target_center)

    while var.start_game_animation:
        # Interpolate zoom factor
        zoom_factor += zoom_speed
        if zoom_factor >= 2.3:
            zoom_factor = 2.3
        scaled_width = int(var.screen_width * zoom_factor)
        scaled_height = int(var.screen_height * zoom_factor)
        bg_image_scaled = pygame.transform.scale(
            bg_image, (scaled_width, scaled_height))
        bg_rect = bg_image_scaled.get_rect()
        bg_rect.center = current_center

        # Interpolate center
        current_center[0] += (target_center[0] - current_center[0]) * 0.1
        current_center[1] += (target_center[1] - current_center[1]) * 0.1
        
        # Draw the image to the screen
        screen.blit(bg_image_scaled, bg_rect.topleft)

        buttons, button_rects, button_icons = create_buttons()
        render_main_buttons(screen, buttons, button_rects, button_icons)
        render_main_title(screen)
        
        # break when image is big enough
        print(zoom_factor)
        if zoom_factor >= 2.3:
            break
        
        # Update the display
        pygame.display.flip()
        pygame.time.Clock().tick(var.FPS)

    var.game_running = True
    var.start_round = False
