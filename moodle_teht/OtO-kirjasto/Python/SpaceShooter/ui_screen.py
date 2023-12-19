from audio_manager import AudioManager
import var, pygame, random
zeroVar = 0
speaker_channel = None
speaker_audio = None
random_speker_time = 0
speaking = False

def render(screen, img, player):
    render_speaker(screen, img, player)

def render_speaker(screen, speak_image, player):
    global zeroVar, speaker_channel, speaker_audio
    # load image
    speaker_scale = 200
    speaker = pygame.image.load("img/pig_speaker" + str(speak_image) + ".png")
    speaker = pygame.transform.scale(speaker, (speaker_scale, speaker_scale))
    speaker_pos = speaker.get_rect()
    speaker_pos.x = var.screen_width - speaker_scale
    speaker_pos.y = var.screen_height - speaker_scale - 30
    # load type of gun
    gun = player.get_gun()
    if gun == "raka_ase":
        gun_image = pygame.image.load("img/pig_speaker_raka.png")
    elif gun == "kakku_sinko":
        gun_image = pygame.image.load("img/pig_speaker_kakku.png")
    
    gun_image = pygame.transform.scale(gun_image, (speaker_scale, speaker_scale))
    gun_image_pos = gun_image.get_rect()
    gun_image_pos.x = var.screen_width - speaker_scale
    gun_image_pos.y = var.screen_height - speaker_scale - 30
    
    # render image
    screen.blit(speaker, (speaker_pos.x, speaker_pos.y))
    screen.blit(gun_image, (speaker_pos.x, speaker_pos.y))
    if zeroVar == 0:
        speaker_channel = pygame.mixer.Channel(2)
        speaker_audio = AudioManager()
        zeroVar = 1
    
def rando_speaking_sound(speaker_channel, speaker_audio):
    # randomize sound
    sound = random.randint(1, 5)
    # volume
    speaker_channel.set_volume(0.5)
    if sound == 1:
        speaker_channel.play(speaker_audio.load_sound("sfx/oinks/oink1.wav"))
    elif sound == 2:
        speaker_channel.play(speaker_audio.load_sound("sfx/oinks/oink2.wav"))
    elif sound == 3:
        speaker_channel.play(speaker_audio.load_sound("sfx/oinks/oink3.mp3"))
    elif sound == 4:
        speaker_channel.play(speaker_audio.load_sound("sfx/oinks/oink4.mp3"))
    elif sound == 5:
        speaker_channel.play(speaker_audio.load_sound("sfx/oinks/oink5.mp3"))
        
def rando_hit_sound(speaker_channel, speaker_audio):
    # randomize sound
    sound = random.randint(1, 3)
    # volume
    speaker_channel.set_volume(1)
    if sound == 1:
        speaker_channel.play(speaker_audio.load_sound("sfx/hits/hit1.wav"))
    elif sound == 2:
        speaker_channel.play(speaker_audio.load_sound("sfx/hits/hit2.wav"))
    elif sound == 3:
        speaker_channel.play(speaker_audio.load_sound("sfx/hits/hit3.wav"))
        
def pick_random_time_interval():
    time_interval = random.randint(2, 5)
    return time_interval

def hitted():
    global speaker_channel, speaker_audio
    if var.game_running:
        rando_hit_sound(speaker_channel, speaker_audio)
        
    else:
        speaker_channel.stop()
        
def speak():
    global speaker_channel, speaker_audio
    if var.game_running:
        rando_speaking_sound(speaker_channel, speaker_audio)
        
    else:
        speaker_channel.stop()
        
def move_mouth():
    global speaking
    speaking = if_playing()
    if not speaking:
        return 1

    if var.ticks % 0.2 < 0.1:
        return 1
    else:
        return 2
    

def if_playing():
    global speaker_channel
    if speaker_channel is not None and speaker_channel.get_busy():
        return True
    else:
        return False
