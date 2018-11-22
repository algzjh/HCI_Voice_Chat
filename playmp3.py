import pygame
import time
from mutagen.mp3 import MP3

def playMp3(mp3_path):
    audio = MP3(mp3_path)
    duration = audio.info.length
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.play(1, 0.0)
    time.sleep(duration)
    pygame.mixer.stop()