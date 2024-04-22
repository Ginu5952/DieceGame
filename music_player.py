import pygame

def initialize_mixer():
    pygame.mixer.init()

def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def quit_mixer():
    pygame.mixer.quit()
