import pygame, sys

intro_done = False
time_elapsed = 0

def start(dt):
    global intro_done, time_elapsed
    wait_time = 10140 / 1000

    if time_elapsed < wait_time and not intro_done:
        time_elapsed += dt
    else:
        intro_done = True