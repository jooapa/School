import pygame, sys, var, time

outro_done = False
title_slide = 0 # 0 to 200
outro_type = "" # bad, very bad, good
text_slide = 0

def start(screen, dt):
    global outro_done, title_slide, outro_type, text_slide
    
    if outro_type == "bad":
        background = pygame.image.load("img/pig defenders bad gooding.png")
        background = pygame.transform.scale(
        background, (var.screen_width, var.screen_height))
    elif outro_type == "very bad":
        background = pygame.image.load("img/pig defenders very bad gooding.png")
        background = pygame.transform.scale(
        background, (var.screen_width, var.screen_height))
    elif outro_type == "good":
        background = pygame.image.load("img/pig defenders good gooding.png")
        background = pygame.transform.scale(
        background, (var.screen_width, var.screen_height))
    
    background.set_alpha(0)
    
    if title_slide < 0.3:
        title_slide += dt * 0.045  # Adjust the speed here
        background.set_alpha(title_slide * 260)
    else:
        title_slide = 0.3
        
    if title_slide == 0.3:
        font = pygame.font.SysFont("Arial", 40)
        text = font.render("Bad endiing", True, (255, 255, 255))
        text.set_alpha((title_slide + 1) * 100)
        text_rect = text.get_rect(center=(var.screen_width / 2, var.screen_height / 2))
        
        # fade in
        if text_slide < 0.3:
            text_slide += dt * 0.045
            text.set_alpha(text_slide * 20)
        else:
            text.set_alpha(0.3)
            text_slide = 0.3
        
        screen.blit(text, text_rect)
        
    screen.blit(background, (0, 0))
    print(title_slide, text_slide)
    if title_slide == 0.3 and text_slide == 0.3:
        outro_done = True
        outro_type = ""