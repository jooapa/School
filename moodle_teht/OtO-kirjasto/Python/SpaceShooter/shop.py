import pygame, var, random
from functions import correct_scale

ticks_in_full_second = var.ticks
keeper = "img/shop1.png"
menu_showing = "main" # main, power_ups, raka_ase, kakku_sinko

def return_create_shop_buttons():
    font_size = 24
    if menu_showing == "main":
        buttons = ["POWER_UPS", "RAKA_ASE", "KAKKU_SINKO", "BACK"]
        buttons_text = ["POWER UPS", "Räkä ase", "Kakku sinko", "BACK"]
        buttons_desc = ["Buy power ups", "Buy raka ase", "Buy kakku sinko", "Back to game"]
        button_size = pygame.math.Vector2(200, 100)
        buttons, button_rects, button_texts, buttons_decs = create_shop_buttons(buttons, button_size, 250, font_size, 200, buttons_text, buttons_desc)
        
    elif menu_showing == "power_ups":
        buttons = ["AMMO", "Movement speed", "Invincibility time", "BACK2"]
        buttons_text = ["AMMO", "Movement speed", "Invincibility time", "BACK"]
        buttons_desc = ["Buy ammo", "Buy movement speed", "Buy invincibility time", "Back to main menu"]
        button_size = pygame.math.Vector2(200, 100)
        buttons, button_rects, button_texts, buttons_decs = create_shop_buttons(
            buttons, button_size, 250, font_size, 200, buttons_text, buttons_desc)
        
    elif menu_showing == "raka_ase":
        buttons = ["raka_MK1", "raka_MK2", "raka_MK3",
               "raka_MK4", "raka_MK5", "BACK2"]
        buttons_text = ["Räkä ase [MK1]", "Räkä ase [MK2]", "Räkä ase [MK3]", "Räkä ase [MK4]", "Räkä ase [MK5]", "BACK"]
        buttons_desc = ["Buy MK1", "Buy MK2", "Buy MK3", "Buy MK4", "Buy MK5", "Back to main menu"]
        button_size = pygame.math.Vector2(200, 80)
        buttons, button_rects, button_texts, buttons_decs = create_shop_buttons(
            buttons, button_size, 200, font_size, 250, buttons_text, buttons_desc)
        
    elif menu_showing == "kakku_sinko":
        buttons = ["kakku_MK1", "kakku_MK2", "kakku_MK3", "kakku_MK4", "kakku_MK5", "BACK2"]
        buttons_text = ["Kakku sinko [MK1]", "Kakku sinko [MK2]", "Kakku sinko [MK3]", "Kakku sinko [MK4]", "Kakku sinko [MK5]", "BACK"]
        buttons_desc = ["Buy MK1", "Buy MK2", "Buy MK3", "Buy MK4", "Buy MK5", "Back to main menu"]
        button_size = pygame.math.Vector2(200, 80)
        buttons, button_rects, button_texts, buttons_decs = create_shop_buttons(
            buttons, button_size, 200, font_size, 250, buttons_text, buttons_desc)
    
    return buttons, button_rects, button_texts, buttons_decs

def create_shop_buttons(buttons, button_size, scale, font_size, offset_y, buttons_text, buttons_desc):
    button_pos = []
    button_rects = []
    button_texts = []
    buttons_desc_texts = []
    desc_font_size = 15
    desc_text_color = (155, 155, 155)
    font_color = (0, 0, 0)
    
    for i in range(len(buttons)):
        button_pos.append(pygame.math.Vector2(
            var.screen_width + 640, var.screen_height / 2 - offset_y + scale * i))
        button_pos[i].x, button_pos[i].y = correct_scale(
            button_pos[i].x, button_pos[i].y)

        button_rects.append(pygame.Rect(0, 0, 0, 0))
        button_rects[i].center = button_pos[i]
        button_rects[i].size = button_size

        text = pygame.font.SysFont("Arial", font_size).render(
            buttons_text[i], True, font_color)
        text_rect = text.get_rect(center=button_rects[i].center)
        button_texts.append((text, text_rect))

        desc_text = pygame.font.SysFont("Arial", desc_font_size).render(
            buttons_desc[i], True, desc_text_color)
        desc_text_rect = desc_text.get_rect(
            center=(button_rects[i].centerx, button_rects[i].centery + 20))
        buttons_desc_texts.append((desc_text, desc_text_rect))
        
    return buttons, button_rects, button_texts, buttons_desc_texts

def handle_shop_button_clicks(buttons, button_rects, screen):
    global menu_showing
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
    
    for i in range(len(buttons)):
        if button_rects[i].collidepoint(mouse_pos):
            if buttons[i] == "raka_MK1":
                show_info_box(screen, "raka_MK1", mouse_pos)
            elif buttons[i] == "raka_MK2":
                show_info_box(screen, "raka_MK2", mouse_pos)
            elif buttons[i] == "raka_MK3":
                show_info_box(screen, "raka_MK3", mouse_pos)
            elif buttons[i] == "raka_MK4":
                show_info_box(screen, "raka_MK4", mouse_pos)
            elif buttons[i] == "raka_MK5":
                show_info_box(screen, "raka_MK5", mouse_pos)
            elif buttons[i] == "kakku_MK1":
                show_info_box(screen, "kakku_MK1", mouse_pos)
            elif buttons[i] == "kakku_MK2":
                show_info_box(screen, "kakku_MK2", mouse_pos)
            elif buttons[i] == "kakku_MK3":
                show_info_box(screen, "kakku_MK3", mouse_pos)
            elif buttons[i] == "kakku_MK4":
                show_info_box(screen, "kakku_MK4", mouse_pos)
            elif buttons[i] == "kakku_MK5":
                show_info_box(screen, "kakku_MK5", mouse_pos)
            
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(buttons)):
                if button_rects[i].collidepoint(mouse_pos):
                    if buttons[i] == "POWER_UPS":
                        menu_showing = "power_ups"
                        print("POWER_UPS opened")
                        return
                    elif buttons[i] == "RAKA_ASE":
                        menu_showing = "raka_ase"
                        print("RAKA_ASE opened")
                        return
                    elif buttons[i] == "KAKKU_SINKO":
                        menu_showing = "kakku_sinko"
                        print("KAKKU_SINKO opened")
                        return
                    elif buttons[i] == "BACK":
                        var.shop_open = False
                        print("Shop closed")
                        return
                    elif buttons[i] == "BACK2":
                        menu_showing = "main"
                    elif buttons[i] == "raka_MK1":
                        buy_upgrade("raka_MK1")
                        return
                    elif buttons[i] == "raka_MK2":
                        buy_upgrade("raka_MK2")
                        return
                    elif buttons[i] == "raka_MK3":
                        buy_upgrade("raka_MK3")
                        return
                    elif buttons[i] == "raka_MK4":
                        buy_upgrade("raka_MK4")
                        return
                    elif buttons[i] == "raka_MK5":
                        buy_upgrade("raka_MK5")
                        return
                    elif buttons[i] == "kakku_MK1":
                        buy_upgrade("kakku_MK1")
                        return
                    elif buttons[i] == "kakku_MK2":
                        buy_upgrade("kakku_MK2")
                        return
                    elif buttons[i] == "kakku_MK3":
                        buy_upgrade("kakku_MK3")
                        return
                    elif buttons[i] == "kakku_MK4":
                        buy_upgrade("kakku_MK4")
                        return
                    elif buttons[i] == "kakku_MK5":
                        buy_upgrade("kakku_MK5")
                        return
                    print(buttons[i])

# Function to render background and handle shopkeeper changes
def render_shop_background(screen):
    global ticks_in_full_second
    global keeper

    if var.ticks > ticks_in_full_second:
        ticks_in_full_second = var.ticks + 0.19
        keeper = random_shopkeeper(keeper)

    background = pygame.image.load(keeper)
    background = pygame.transform.scale(
        background, (var.screen_width, var.screen_height))
    screen.blit(background, (0, 0))


def random_shopkeeper(keeper):
    shopkeeper = random.randint(1, 4)
    if keeper == f"img/shop{shopkeeper}.png":
        shopkeeper = (shopkeeper % 4) + 1

    return f"img/shop{shopkeeper}.png"


def render_shop_buttons(screen, buttons, button_rects, button_texts, buttons_desc):
    for i in range(len(buttons)):
        pygame.draw.rect(screen, (255, 255, 255), button_rects[i])
        screen.blit(button_texts[i][0], button_texts[i][1])
        screen.blit(buttons_desc[i][0], buttons_desc[i][1])


def shop_menu_btns(screen):
    
    buttons, button_rects, button_texts, buttons_desc = return_create_shop_buttons()

    render_shop_background(screen)
    render_shop_buttons(screen, buttons, button_rects, button_texts, buttons_desc)
    
    handle_shop_button_clicks(buttons, button_rects, screen)

def show_info_box(screen, text, mouse_pos):
    upgrades = get_upgrade_details(text)
    font_size = 24
    font_color = (255, 255, 255)
    text = pygame.font.SysFont("Arial", font_size).render(
        upgrades, True, font_color)
    text_rect = text.get_rect(center=(var.screen_width - 400, mouse_pos[1]))

    padding = 10
    # Draw box with padding
    pygame.draw.rect(screen, (0, 0, 0), (text_rect.x - padding, text_rect.y - padding, text_rect.width + padding * 2, text_rect.height + padding * 2))
    screen.blit(text, text_rect)
    
    
def get_upgrade_details(upgrade):
    if upgrade.startswith("raka_"):
        new_upgrade = upgrade[5:]
        gun_type = "raka_ase"
    elif upgrade.startswith("kakku_"):
        new_upgrade = upgrade[6:]
        gun_type = "kakku_sinko"
    else:
        return "Invalid upgrade"
    
    if upgrade in var.bought_weapons:
        if gun_type == "raka_ase":
            damage = var.raka_ase[new_upgrade]["Damage"]
            fire_rate = var.raka_ase[new_upgrade]["Fire Rate"]
            reload_time = var.raka_ase[new_upgrade]["Reload Time"]
            magazine_size = var.raka_ase[new_upgrade]["Magazine Size"]
            speed = var.raka_ase[new_upgrade]["Speed"]
        
        elif gun_type == "kakku_sinko":
            damage = var.kakku_sinko[new_upgrade]["Damage"]
            fire_rate = var.kakku_sinko[new_upgrade]["Fire Rate"]
            reload_time = var.kakku_sinko[new_upgrade]["Reload Time"]
            magazine_size = var.kakku_sinko[new_upgrade]["Magazine Size"]
            speed = var.kakku_sinko[new_upgrade]["Speed"]
                    
        return f"You already own this Weapon. \nDamage: {damage}\nFire Rate: {fire_rate}\nReload Time: {reload_time}\nMagazine Size: {magazine_size}\nSpeed: {speed}"
    else:
        if gun_type == "raka_ase":
            damage = var.raka_ase[new_upgrade]["Damage"]
            fire_rate = var.raka_ase[new_upgrade]["Fire Rate"]
            reload_time = var.raka_ase[new_upgrade]["Reload Time"]
            magazine_size = var.raka_ase[new_upgrade]["Magazine Size"]
            speed = var.raka_ase[new_upgrade]["Speed"]
            cost = var.raka_ase[new_upgrade]["Cost"]
        
        elif gun_type == "kakku_sinko":
            damage = var.kakku_sinko[new_upgrade]["Damage"]
            fire_rate = var.kakku_sinko[new_upgrade]["Fire Rate"]
            reload_time = var.kakku_sinko[new_upgrade]["Reload Time"]
            magazine_size = var.kakku_sinko[new_upgrade]["Magazine Size"]
            speed = var.kakku_sinko[new_upgrade]["Speed"]
            cost = var.kakku_sinko[new_upgrade]["Cost"]
        
        return f"You don't own this Weapon. \nDamage: {damage}\nFire Rate: {fire_rate}\nReload Time: {reload_time}\nMagazine Size: {magazine_size}\nSpeed: {speed}\nCost: {cost}"
    
    
def buy_upgrade(upgrade):
    if upgrade.startswith("raka_"):
        new_upgrade = upgrade[5:]
        gun_type = "raka_ase"
    elif upgrade.startswith("kakku_"):
        new_upgrade = upgrade[6:]
        gun_type = "kakku_sinko"
    else:
        return "Invalid upgrade"
    
    if upgrade in var.bought_weapons:
        set_upgrade_to_current(upgrade)
        return "You already own this upgrade"
    else:
        if gun_type == "raka_ase":
            cost = var.raka_ase[new_upgrade]["Cost"]
        elif gun_type == "kakku_sinko":
            cost = var.kakku_sinko[new_upgrade]["Cost"]
        
        if var.coins >= cost:
            var.coins -= cost
            var.bought_weapons.append(upgrade)
            set_upgrade_to_current(upgrade)                
            return "Upgrade bought"
        else:
            return "Not enough coins"
        
def set_upgrade_to_current(upgrade):
    if upgrade.startswith("raka_"):
        new_upgrade = upgrade[5:]
        gun_type = "raka_ase"
    elif upgrade.startswith("kakku_"):
        new_upgrade = upgrade[6:]
        gun_type = "kakku_sinko"
    else:
        return "Invalid upgrade"
    
    if upgrade in var.bought_weapons:
        if gun_type == "raka_ase":
            var.current_raka_ase_upgrade = new_upgrade
        elif gun_type == "kakku_sinko":
            var.current_kakku_sinko_upgrade = new_upgrade
        return "Upgrade set to current"
    else:
        return "You don't own this upgrade"