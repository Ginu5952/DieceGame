import pygame
import pyttsx3 # type: ignore

voice = pyttsx3.init()

def initialize_mixer():
    pygame.mixer.init()

def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def quit_mixer():
    pygame.mixer.quit()

def play_announcement(text_to_speak,status:str):
    
    try:
        if status == "winner":
            voice.say(text_to_speak) 
            voice.runAndWait()
        elif status == "failed":   
            voice_properties = voice.getProperty('rate')
            voice.setProperty('rate', voice_properties - 40)
            voice.say(text_to_speak) 
            voice.runAndWait()
    except Exception as e:
        print("An error occurred:", e)        

