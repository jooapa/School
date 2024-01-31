import pygame, sys, os, random, math, time, var

def render_tutorial(screen):
    screen.fill((0, 0, 0))
    screen.blit(pygame.image.load("img/tutorial.png").convert_alpha(), (0, 0))
    button_rect = pygame.Rect(0, 0, 0, 0)
    button_rect.size = pygame.math.Vector2(100, 100)
    button_rect.center = pygame.math.Vector2(var.screen_width - 50, 50)
    button_icon = pygame.image.load("img/ico/BACK.png").convert_alpha()
    button_icon = pygame.transform.scale(
        button_icon, (button_rect.size[0], button_rect.size[1]))
    screen.blit(button_icon, button_rect)
    return button_rect