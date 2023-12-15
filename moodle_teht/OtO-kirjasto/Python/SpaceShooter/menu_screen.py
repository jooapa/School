import pygame, var
from functions import correct_scale

def start_new_level(player, enemies, bullets):
    var.difficulty = 10
    var.ticks = 0
    var.cooldown = 0
    var.cooldown_time = var.cooldown_time
    var.round = 0
    var.invincibility_time = 0

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
    var.game_running = True
    var.start_round = False


def start_menu_btns():

    buttons, button_rects, button_texts = create_buttons()

    return buttons, button_rects, button_texts


def create_buttons():
    buttons = ["TUTORIAL", "START", "SHOP", "QUIT"]
    button_pos = []
    for i in range(len(buttons)):
        button_pos.append(pygame.math.Vector2(0, 0))
        button_pos[i].x = var.screen_width + \
            400 * i - 400 * (len(buttons) - 1) / 2
        button_pos[i].y = var.screen_height / 2 - 50
        button_pos[i].x, button_pos[i].y = correct_scale(
            button_pos[i].x, button_pos[i].y)
        if buttons[i] == "QUIT":
            button_pos[i].y = var.screen_height - 50
            button_pos[i].x = var.screen_width - 50

    button_size = pygame.math.Vector2(0, 0)
    button_size.x = 300
    button_size.y = 300
    button_size.x, button_size.y = correct_scale(button_size.x, button_size.y)
    font_size = 30

    button_rects = []
    for i in range(len(buttons)):
        button_rects.append(pygame.Rect(0, 0, 0, 0))
        button_rects[i].center = button_pos[i]
        button_rects[i].size = button_size
        if buttons[i] == "QUIT":
            button_rects[i].size = pygame.math.Vector2(100, 100)
            button_rects[i].center = button_pos[i]

    button_texts = []
    for i in range(len(buttons)):
        text = pygame.font.SysFont("Arial", font_size).render(
            buttons[i], True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rects[i].center)
        button_texts.append((text, text_rect))

    return buttons, button_rects, button_texts


def render_buttons(screen, buttons, button_rects, button_texts):
    for i in range(len(buttons)):
        pygame.draw.rect(screen, (255, 255, 255), button_rects[i])
        screen.blit(button_texts[i][0], button_texts[i][1])
    
def handle_main_screen_buttons(buttons, button_rects, player, enemies, bullets):
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


def main_screen(screen, player, enemies, bullets):
    buttons, button_rects, button_texts = start_menu_btns()

    # Only render buttons after creating them
    render_buttons(screen, buttons, button_rects, button_texts)

    # Event handling loop
    handle_main_screen_buttons(buttons, button_rects, player, enemies, bullets)
