import pygame, var, random, time, save_file
from functions import correct_scale
from ui_screen import render_coin_animation

ticks_in_full_second = time.time() + 0.19
keeper = "img/shop1.png"
menu_showing = "main" # main, power_ups, raka_ase, kakku_sinko

have_tsar_bomba = False

shop_keeper_image = pygame.image.load("img/shop1.png")
shop_keeper_image = pygame.transform.scale(shop_keeper_image, (var.screen_width, var.screen_height))
render_shop_background_image = pygame.image.load("img/shop_bg.png")
render_shop_background_image = pygame.transform.scale(render_shop_background_image, (var.screen_width, var.screen_height))

def return_create_shop_buttons():
    font_size = 24
    if menu_showing == "main":
        buttons = ["POWER_UPS", "RAKA_ASE", "KAKKU_SINKO", "BACK"]
        buttons_text = ["POWER UPS", "Räkä ase", "Kakku sinko", "BACK"]
        buttons_desc = ["Buy power ups", "Buy raka ase", "Buy kakku sinko", "Back to game"]
        button_size = pygame.math.Vector2(200, 100)
        buttons, button_rects, button_texts, buttons_decs = create_shop_buttons(buttons, button_size, 250, font_size, 200, buttons_text, buttons_desc)
        
    elif menu_showing == "power_ups":
        buttons = ["Dash Speed", "Invincibility time", "BACK2"]
        buttons_text = ["Dash Speed", "Invincibility time", "BACK"]
        buttons_desc = ["Buy Dash Speed", "Buy invincibility time", "Back to main menu"]
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
            elif buttons[i] == "Dash Speed":
                show_info_box(screen, "Dash Speed", mouse_pos)
            elif buttons[i] == "Invincibility time":
                show_info_box(screen, "Invincibility time", mouse_pos)
            
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
                    elif buttons[i] == "Dash Speed":
                        buy_upgrade("Dash Speed")
                        return
                    elif buttons[i] == "Invincibility time":
                        buy_upgrade("Invincibility time")
                        return

                    save_file.save_variables()
                    print(buttons[i])

# Function to render background and handle shopkeeper changes
def render_shop_keeper(screen):
    global ticks_in_full_second
    global keeper, shop_keeper_image

    if time.time() > ticks_in_full_second:
        ticks_in_full_second = time.time() + 1.263
        keeper = random_shopkeeper(keeper)
        shop_keeper_image = pygame.image.load(keeper)

    screen.blit(shop_keeper_image, (0, 0))

def render_shop_background(screen):
    global render_shop_background_image
    screen.blit(render_shop_background_image, (0, 0))

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

def render_current_weapon(screen):
    font_size = 30
    font_color = (0, 0, 0)
    x = var.screen_width - 650
    y = 70
    font = pygame.font.SysFont("Arial", font_size)
    text = font.render(f"Räkä Ase: {var.current_raka_ase_upgrade}", True, font_color)
    screen.blit(text, (x, y))
    text = font.render(f"Kakku Sinko: {var.current_kakku_sinko_upgrade}", True, font_color)
    screen.blit(text, (x, y + 30))

def render_tsar_bomba(screen):
    global have_tsar_bomba
    background = pygame.image.load("img/tsar_bomba_shop.png")
    background = pygame.transform.scale(
        background, (var.screen_width, var.screen_height))
    
    # hande cklicks
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
    if pygame.mouse.get_pressed()[0]:
        print(mouse_pos)
        if pygame.Rect(107, 249, 865, 489).collidepoint(mouse_pos):
            print("tsar_bomba bought")
            have_tsar_bomba = True
            return
    screen.blit(background, (0, 0))
        
    
    
def shop_menu_btns(screen):
    
    buttons, button_rects, button_texts, buttons_desc = return_create_shop_buttons()

    render_shop_keeper(screen)
    render_shop_background(screen)
    render_shop_buttons(screen, buttons, button_rects, button_texts, buttons_desc)
    render_coin_animation(screen, 190, 40, (0,0,0))
    render_current_weapon(screen)
    if var.bad_ending_completed and not have_tsar_bomba:
        render_tsar_bomba(screen)
    handle_shop_button_clicks(buttons, button_rects, screen)


def show_info_box(screen, text, mouse_pos):
    upgrades_text = get_upgrade_details(text)
    lines = upgrades_text.split('\n')
    font_size = 24
    font_color = (255, 255, 255)
    font = pygame.font.SysFont("Arial", font_size)
    padding = 10  # Set the padding value here
    y = mouse_pos[1] - 100
    x = var.screen_width - 580  # Set x to a fixed value
        
    # black box behind text
    pygame.draw.rect(screen, (0, 0, 0), (x - padding, y - padding, 330, len(lines) * font_size + padding * 8))
    for line in lines:
        text = font.render(line, True, font_color)
        screen.blit(text, (x, y))
        y += font_size + padding  # Move y down for the next line
        
    
    
def get_upgrade_details(upgrade):
    if upgrade.startswith("raka_"):
        new_upgrade = upgrade[5:]
        gun_type = "raka_ase"
    elif upgrade.startswith("kakku_"):
        new_upgrade = upgrade[6:]
        gun_type = "kakku_sinko"
    elif upgrade == "Dash Speed":
        return " Dash Speed:\n\nCost: 500 \n Dash Speed: " + str(var.dash_speed) + " / 1000"
    elif upgrade == "Invincibility time":
        return " Invincibility time\n\nCost: 200 \n invincibility time: " + str(var.invincibility_time_max) + "s / 6s \n Increases duration of invincibility \n after taking damage: " + str(var.invincibility_time_max) + "s / 6s"
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
    elif upgrade == "Dash Speed":
        cost = 500
        if var.dash_speed < 1000 and var.coins >= cost:
            var.coins -= cost
            var.dash_speed += 100
            print("dash speed increased to", var.dash_speed)
            return "Upgrade bought"
        print("Not enough coins for Dash Speed")
        return "Not enough coins"
    elif upgrade == "Invincibility time":
        cost = 200
        print(var.invincibility_time_max < 6, var.coins >= cost)
        if var.invincibility_time_max != 6 and var.coins >= cost:
            var.coins -= cost
            var.invincibility_time_max += 1
            print("invincibility time increased to", var.invincibility_time_max)
            return "Upgrade bought"
        print("Not enough coins for Invincibility time")
        return "Not enough coins"
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
            save_file.save_variables()         
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