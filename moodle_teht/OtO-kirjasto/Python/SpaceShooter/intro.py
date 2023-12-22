import pygame, sys, var

intro_done = False
time_elapsed = 0
title_slide = 0 # 0 to 200

def start(screen, dt):
    global intro_done, time_elapsed, title_slide
    wait_time = 10150 / 1000

    if time_elapsed < wait_time and not intro_done:
        time_elapsed += dt
        
        if time_elapsed > 2 and time_elapsed < 5:
            # klinoff team image  klinoff team comes from alpha 0 to 1 and little but from top to the middle
            klinoff_team = pygame.image.load("img/klinoff_team.png").convert_alpha()
            # aplha 0 to 1 in 1 second
            klinoff_team.set_alpha((time_elapsed - 2) * 500 / 3)
            if time_elapsed > 4:
                klinoff_team.set_alpha(100 - ((time_elapsed - 4) * 500))
            
            screen.fill((0, 0, 0))
            # slow down the movement
            screen.blit(klinoff_team, (0, ((time_elapsed - 2) * 100 / 3) - 100))
            
        
        if time_elapsed > 5 and time_elapsed < 8:
            # presents text
            font = pygame.font.SysFont("Arial", 20)
            text = font.render("Presents..", True, (255, 255, 255))
            
            text.set_alpha((time_elapsed - 5) * 400 / 3)
            
            if time_elapsed > 7:
                text.set_alpha(100 - ((time_elapsed - 5) * 100))
            
            screen.fill((0, 0, 0))
            screen.blit(text, (var.screen_width // 2, var.screen_height // 2))
        
        if time_elapsed > 8:
            screen.fill((0, 0, 0))
            # logo slide
            title = pygame.image.load("img/title.png").convert_alpha()
            title = pygame.transform.scale(title, (1000, 150))
            title.set_alpha(0)
            
            if title_slide < 1:
                title_slide += dt * (time_elapsed * 0.045)  # Adjust the speed here
                # alpha 0 to 1 in 1 second
                title.set_alpha(title_slide * 260)
            else:
                title_slide = 1

            eased_slide = cubic_ease_out(title_slide) * 200  # Apply the easing function
            title_rect = title.get_rect(center=(var.screen_width / 2, var.screen_height / 2 - eased_slide))
            screen.blit(title, title_rect)
        
    else:
        intro_done = True
        
    
def cubic_ease_out(t):
    t -= 1  
    return t * t * t + 1