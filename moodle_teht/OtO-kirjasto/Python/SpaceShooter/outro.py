import pygame, sys, var, time

outro_done = False
title_slide = 0 # 0 to 200
outro_type = "" # bad, very bad, good
text_slide = 0
exit_slide = 0

good_engind_img1_slide = 0
good_engind_img2_slide = 0
good_engind_img3_slide = 0

def good_endings(screen, dt):
    global good_engind_img1_slide, good_engind_img2_slide, good_engind_img3_slide, outro_done, title_slide, outro_type, text_slide, exit_slide
    
    font = pygame.font.SysFont("Arial", 40)
    background1 = pygame.image.load("img/good gooding2.png")
    background2 = pygame.image.load("img/good gooding1.png")
    background3 = pygame.image.load("img/good gooding3.png")
    
    background1 = pygame.transform.scale(
    background1, (var.screen_width, var.screen_height))
    background2 = pygame.transform.scale(
    background2, (var.screen_width, var.screen_height))
    background3 = pygame.transform.scale(
    background3, (var.screen_width, var.screen_height))
    
    background1.set_alpha(0)
    background2.set_alpha(0)
    background3.set_alpha(0)
    
    if good_engind_img1_slide < 0.3:
        good_engind_img1_slide += dt * 0.045
        background1.set_alpha(good_engind_img1_slide * 260)
    else:
        good_engind_img1_slide = 0.3
        
    if good_engind_img1_slide == 0.3:
        if good_engind_img2_slide < 0.3:
            good_engind_img2_slide += dt * 0.045
            background2.set_alpha(good_engind_img2_slide * 260)
        else:
            good_engind_img2_slide = 0.3
            
    if good_engind_img2_slide == 0.3:
        if good_engind_img3_slide < 0.3:
            good_engind_img3_slide += dt * 0.045
            background3.set_alpha(good_engind_img3_slide * 260)
        else:
            good_engind_img3_slide = 0.3
            
    if good_engind_img3_slide == 0.3:
        text = font.render("Good ending", True, (255, 255, 255))
        text.set_alpha((good_engind_img3_slide + 1) * 100)
        text_rect = text.get_rect(center=(var.screen_width / 2, var.screen_height / 2))
        
        # fade in
        if text_slide < 0.3:
            text_slide += dt * 0.045
            text.set_alpha(text_slide * 50)
        else:
            text.set_alpha(1)
            text_slide = 0.3
        
        screen.blit(text, text_rect)
        
    screen.blit(background1, (0, 0))
    screen.blit(background2, (0, 0))
    screen.blit(background3, (0, 0))
    
    if good_engind_img1_slide == 0.3 and good_engind_img2_slide == 0.3 and good_engind_img3_slide == 0.3 and text_slide == 0.3:
            
            # fade in exit text by pressing sapce
            exit_text = font.render("space to exit", True, (255, 255, 255))
            exit_text.set_alpha(0)
            
            if exit_slide < 0.3:
                exit_slide += dt * 0.045
                exit_text.set_alpha(exit_slide * 10)
            else:
                exit_text.set_alpha(0.1)
                exit_slide = 0.1
                
            exit_text_rect = exit_text.get_rect(center=(var.screen_width / 2, exit_text.get_height()))
            screen.blit(exit_text, exit_text_rect)
                
            screen.blit(background1, (0, 0))
            screen.blit(background2, (0, 0))
            screen.blit(background3, (0, 0))
            # if pressed space
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                outro_done = True
                outro_type = ""
                title_slide = 0
                text_slide = 0
                exit_slide = 0
                good_engind_img1_slide = 0
                good_engind_img2_slide = 0
                good_engind_img3_slide = 0
                
                
def start(screen, dt):
    global outro_done, title_slide, outro_type, text_slide, exit_slide
    
    font = pygame.font.SysFont("Arial", 40)
    if outro_type == "bad":
        background = pygame.image.load("img/pig defenders bad gooding.png")
        background = pygame.transform.scale(
        background, (var.screen_width, var.screen_height))
        text = font.render("Bad endiing", True, (255, 255, 255))
    elif outro_type == "very bad":
        background = pygame.image.load("img/pig defenders very bad gooding.png")
        background = pygame.transform.scale(
        background, (var.screen_width, var.screen_height))
        text = font.render("Very bad endiing", True, (255, 255, 255))
    elif outro_type == "good":
        good_endings(screen, dt)
        return
    
    background.set_alpha(0)
    
    if title_slide < 0.3:
        title_slide += dt * 0.045  # Adjust the speed here
        background.set_alpha(title_slide * 260)
    else:
        title_slide = 0.3
        
    if title_slide == 0.3:
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
        
        # fade in exit text by pressing sapce
        exit_text = font.render("space to exit", True, (100, 100, 100))
        exit_text.set_alpha(0)
        
        if exit_slide < 0.3:
            exit_slide += dt * 0.045
            exit_text.set_alpha(exit_slide * 10)
        else:
            exit_text.set_alpha(0.1)
            exit_slide = 0.1
            
        exit_text_rect = exit_text.get_rect(center=(var.screen_width / 2, exit_text.get_height()))
        screen.blit(exit_text, exit_text_rect)
            
        screen.blit(background, (0, 0))
        # if pressed space
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            outro_done = True
            outro_type = ""
            title_slide = 0 # 0 to 200
            text_slide = 0
            exit_slide = 0