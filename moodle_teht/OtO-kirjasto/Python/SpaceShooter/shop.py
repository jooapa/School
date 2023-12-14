import pygame, var, random
from functions import correct_scale

ticks_in_full_second = var.ticks
keeper = "img/shop1.png"
menu_showing = "main" # main, power_ups, raka_ase, kakku_sinko

def create_shop_buttons():
    if menu_showing == "main":
        buttons, button_rects, button_texts = create_main_shop_buttons()
    elif menu_showing == "power_ups":
        pass
    elif menu_showing == "raka_ase":
        pass
    elif menu_showing == "kakku_sinko":
        pass
    
    return buttons, button_rects, button_texts

def create_main_shop_buttons():
    buttons = ["POWER_UPS", "RAKA_ASE", "KAKKU_SINKO", "BACK"]
    button_pos = []
    button_size = pygame.math.Vector2(200, 100)
    font_size = 20
    button_rects = []
    button_texts = []

    for i in range(len(buttons)):
        button_pos.append(pygame.math.Vector2(
            var.screen_width + 640, var.screen_height / 2 - 200 + 250 * i))
        button_pos[i].x, button_pos[i].y = correct_scale(
            button_pos[i].x, button_pos[i].y)

        button_rects.append(pygame.Rect(0, 0, 0, 0))
        button_rects[i].center = button_pos[i]
        button_rects[i].size = button_size

        text = pygame.font.SysFont("Arial", font_size).render(
            buttons[i], True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rects[i].center)
        button_texts.append((text, text_rect))
    return buttons,button_rects,button_texts


def handle_shop_button_clicks(buttons, button_rects):
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(len(buttons)):
                if button_rects[i].collidepoint(mouse_pos):
                    if buttons[i] == "POWER_UPS":
                        print("POWER_UPS opened")
                        return
                    elif buttons[i] == "RAKA_ASE":
                        print("RAKA_ASE opened")
                        return
                    elif buttons[i] == "KAKKU_SINKO":
                        print("KAKKU_SINKO opened")
                        return
                    elif buttons[i] == "BACK":
                        var.shop_open = False
                        print("Shop closed")
                        return


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


def render_shop_buttons(screen, buttons, button_rects, button_texts):
    for i in range(len(buttons)):
        pygame.draw.rect(screen, (255, 255, 255), button_rects[i])
        screen.blit(button_texts[i][0], button_texts[i][1])


def shop_menu_btns(screen):
    buttons, button_rects, button_texts = create_shop_buttons()

    render_shop_background(screen)
    render_shop_buttons(screen, buttons, button_rects, button_texts)
    
    handle_shop_button_clicks(buttons, button_rects)
