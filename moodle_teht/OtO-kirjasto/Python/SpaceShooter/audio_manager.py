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

    def seek_to(self, sound, time):
        sound.set_pos(time)
        
class MusicManager:
    def __init__(self):
        pygame.mixer.init()

    def load_music(self, filepath):
        return pygame.mixer.music.load(filepath)

    def play_music(self, music):
        pygame.mixer.music.play()

    def stop_music(self, music):
        pygame.mixer.music.stop()

    def pause_music(self, music):
        pygame.mixer.music.pause()

    def resume_music(self, music):
        pygame.mixer.music.unpause()

    def set_volume(self, music, volume):
        pygame.mixer.music.set_volume(volume)

    def seek_to(self, music, time):
        pygame.mixer.music.set_pos(time)
    
    def music_has_ended(self):
        return pygame.mixer.get_busy() == 0