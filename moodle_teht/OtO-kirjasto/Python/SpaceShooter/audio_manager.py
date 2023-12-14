import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()

    def load_sound(self, filepath):
        return pygame.mixer.Sound(filepath)

    def play_sound(self, sound):
        sound.play()

    def stop_sound(self, sound):
        sound.stop()

    def pause_sound(self, sound):
        sound.pause()

    def resume_sound(self, sound):
        sound.unpause()

    def set_volume(self, sound, volume):
        sound.set_volume(volume)

