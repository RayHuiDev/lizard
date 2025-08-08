import sys
import os
import pygame
from pynput import keyboard

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

sound_file = resource_path("lizard-button.mp3")

pygame.mixer.init()

if not os.path.exists(sound_file):
    print("Sound file not found!")
    sys.exit()

def play_sound():
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def on_press(key):
    try:
        if key == keyboard.Key.enter:
            play_sound()
    except:
        pass

print("Listening for Enter key. Press Ctrl+C to exit.")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
