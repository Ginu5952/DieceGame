import time
from music_player import play_music,stop_music,initialize_mixer
import pygame
import os
import pyttsx3 # type: ignore
import random
from typing import NoReturn
import sys
from dice import D4, D6, D8, Dice
from dice_board import DummyDice

import colorama
import threading


pygame.init()
pygame.mixer.init()
colorama.init()

blinking = True
num_blinks = 0
max_blinks = 5  # Number of times to blink
# Colors

RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
ORANGE = '\033[38;5;208m'
PINK = '\033[38;5;206m'

# Font Styles

BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m' 
STRIKETHROUGH = '\033[9m'
 


class DiceGame:
    def __init__(self, dice_board: DummyDice, player_name: str) -> None:
        self._dice_board: DummyDice = dice_board
        self._player_name: str = player_name
        self.roll_trials: int = 5
        self.initial_roll: int = self.roll_trials

    def is_winner(self) -> bool:
        return self._dice_board.check_winner()
    

    def roll(self, roll_pos: list[int] | None = None) -> None | NoReturn:
       
        print(GREEN + ITALIC + "rolling...." + RESET)
        
        #time.sleep(0.4)
       
        if self.roll_trials:
            if roll_pos:
                try:
                    roll = self._dice_board.pos_to_be_rolled(roll_pos)
                    if isinstance(roll,DummyDice):
                      #  self.roll_dice(times=10,delay=0.5,positn=roll_pos)
                        self._dice_board.roll()
                        self.roll_trials -= 1
                    else:
                        print(RED + '\nPosition cannot be rolled! Out of range' + RESET)    
                except Exception as e:
                    print(e)    
   
           
        else:
            pygame.mixer.stop()
            voice = pyttsx3.init()
            voice_properties = voice.getProperty('rate')
            voice.setProperty('rate', voice_properties - 40)
            voice.say(f"Game Over {player_name} ")
            voice.say("You have exhausted your {self.initial_roll} trials")
            voice.runAndWait()
           

            raise PermissionError(f"You have exhausted your {self.initial_roll} trials")
        

    def add_dice(self, dice: type[Dice]) -> None:
        self._dice_board + dice

    def draw_dice(self,game):
        print(game)
        clear_screen()
        for dicee in game:
            for key,pic in diece_pic.items():
                if str(dicee) == key:
                    print(pic)
                    print('\t')
      
   

    @property
    def total(self) -> int:
        return self._dice_board.plus(len(self.dice)).total

    @property
    def dice(self):
        return self._dice_board.dice
    
def roll_dice(times=10,delay=0.5,positn = 0):
         
        for _ in range(times):
            # Clear the screen
            clear_screen()

            # Randomly select a face
            dice1 = random.choice(list(diece_pic.keys()))
            dice2 = random.choice(list(diece_pic.keys()))
            dice3 = random.choice(list(diece_pic.keys()))  

            if positn == '1':
                
                print(diece_pic[dice1])
            elif positn == '2':
               
                print(diece_pic[dice2])
            elif positn == '3':
               
                print(diece_pic[dice3])
            else:
                print(diece_pic[dice1])
                print(diece_pic[dice2])


            # Pause for a short duration
            time.sleep(delay)

def clear_screen():
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')            



def animate_text(text,color_combinations):
    reset_code = "\033[0m"  # Reset ANSI escape code
    
    for _ in range(1):
        for i, char in enumerate(text):
            # Select color from combinations list, cycling if needed
            color = color_combinations[i % len(color_combinations)]
            # ANSI escape code for foreground color
            fg_color_code = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
            # Print character with foreground color
            print(f"{fg_color_code}{char}", end='', flush=True)
            time.sleep(0.1)
        
        # Reset colors after printing
        print(reset_code)
        print('\n')

def simple_animate_text(text):
    for _ in range(1):  
        for char in text:
            print(char, end='', flush=True)  
            time.sleep(0.1)  
        print('\n')            

def show_image(imge):

    if imge == 'welcome':
       
        # Set up the screen
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("WELCOME...")

        # Load the image
        image = pygame.image.load("/home/dci-student/Desktop/dice_game/images/dice.jpeg")

        # Get the dimensions of the image
        image_width, image_height = image.get_size()

        # Scale the image to fit within the screen
        scaled_image = pygame.transform.scale(image, (screen_width, screen_height))

        # Blit the scaled image onto the screen
        screen.blit(scaled_image, (0, 0))

        # Update the display
        pygame.display.flip()

        # Event loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
       
   
def blink_text(text,color):

    global blinking, num_blinks
    while blinking and num_blinks < max_blinks:
        print(color + text + colorama.Style.RESET_ALL, end='\r', flush=True)  # Suppress newline and flush output
        time.sleep(0.5)  # Adjust the blinking speed here
        print(' ' * len(text), end='\r', flush=True)  # Clear the text
        time.sleep(0.5)
        num_blinks += 1
    blinking = False  # Stop blinking after max_blinks

     
   
def print_multicolor_text(text, color_combinations):
    reset_code = "\033[0m"  # Reset ANSI escape code
    
    for i, char in enumerate(text):
        # Select color from combinations list, cycling if needed
        color = color_combinations[i % len(color_combinations)]
        # ANSI escape code for foreground color
        fg_color_code = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
        # Print character with foreground color
        print(f"{fg_color_code}{char}", end="")
    
    # Reset colors after printing
    print(reset_code)
    print('\n') 

def hide_cursor():
    sys.stdout.write("\033[?25l")  # Hide cursor

def show_cursor():
    sys.stdout.write("\033[?25h")  # Show cursor


if __name__ == "__main__":
    # python -m main
    initialize_mixer()
    diece_pic = {  '1': PURPLE + BOLD +
            """
            ╭─────────╮
            |         |  
            |    ●    |
            |         |         
            ╰─────────╯
            """ + RESET,
            '2': GREEN + BOLD +
            """
            ╭─────────╮
            |  ●      |  
            |         |
            |      ●  |         
            ╰─────────╯
            """ + RESET,
            '3': RED + BOLD +
            """
            ╭─────────╮
            |  ●      |  
            |    ●    |
            |      ●  |         
            ╰─────────╯
            """ + RESET,
            '4': YELLOW + BOLD +
            """
            ╭─────────╮
            |  ●   ●  |  
            |         |
            |  ●   ●  |         
            ╰─────────╯
            """ + RESET,
            '5': ORANGE + BOLD +
            """
            ╭─────────╮
            |  ●   ●  |  
            |    ●    |
            |  ●   ●  |         
            ╰─────────╯ 
            """ + RESET,
            '6': PINK + BOLD +
            """
            ╭─────────╮
            |  ●   ●  |  
            |  ●   ●  |
            |  ●   ●  |         
            ╰─────────╯
            """ + RESET,
            '7': CYAN + BOLD +
            """
            ╭─────────╮
            |  ●   ●  |  
            |  ● ● ●  |
            |  ●   ●  |         
            ╰─────────╯
            """ + RESET,
            '8': BLUE + BOLD +
            """
            ┌─────────┐
            |  ● ● ●  |  
            |  ●   ●  |
            |  ● ● ●  |         
            ╰─────────╯
            """ + RESET
            }
              
    
  

    player_dice_count: int = 2
    player_max_dice_count: int = 3

    clear_screen()


    text = '''
    _________                                                                        _________ 
   /\        \\           ____ ___ ____ _____    ____    _    __  __ _____          /\\        \\
  / ●\\    ●   \\         |  _ \\_ _/ ___| ____|  / ___|  / \\  |  \\/  | ____|        / ●\\    ●   \\
 /    \\________\\        | | | | | |   |  _|   | |  _  / _ \\ | |\\/| |  _|         /    \\________\\
 \\    / ●      /        | |_| | | |___| |___  | |_| |/ ___ \\| |  | | |___         \\    / ●      / 
  \\● /    ●   /         |____/___\\____|_____|  \\____/_/   \\_\\_|  |_|_____|         \\● /    ●   /  
   \\/_______●/                                                                      \\/_______●/ 
'''


    color_combinations = [
                                (0, 128, 128),    # Teal
                                (128, 0, 128),    # Purple
                                (0, 0, 128),      # Navy
                                (128, 0, 0),      # Maroon
                                (128, 128, 0),    # Olive
                                (0, 128, 0),      # Green
                                (128, 128, 128)   # Gray
                            ]
    print_multicolor_text(text, color_combinations)
    
    player_name: str = input(PURPLE + ITALIC + "\nPlayer, state your name: " + RESET)
   # print(GREEN + ITALIC + f'\nWelcome {player_name.capitalize()}.'+ RESET)

    text = GREEN + ITALIC +  f'\nWelcome {player_name.capitalize()}' + RESET
    simple_animate_text(text)

    show_image('welcome')
    pygame.quit()
     
    voice = pyttsx3.init()
    voice.say(f"Welcome {player_name} ")
    voice.say(f"Welcome to dice game ")
    voice.runAndWait()

    pygame.init()

    music_file = "/home/dci-student/Downloads/bensound-summer_mp3_music.mp3" 
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely
  
    dice = DummyDice(D4, D6)

   # print(GREEN + ITALIC + f"The dice game will start with {player_dice_count} dices: " + RESET, dice )
    simple_animate_text(GREEN + ITALIC + f"The dice game will start with {player_dice_count} dices: " + RESET)
    print(BLUE + BOLD + f'{dice}' + RESET)
    game: DiceGame = DiceGame(dice, player_name)

    simple_animate_text(GREEN + ITALIC + "You will have more points if you add a third dice, D8" + RESET)
    if input(YELLOW + BOLD + "Do you want to add a third dice: 'D8'?, yes/no: " + RESET) == "yes":
        game.add_dice(D8)
        player_dice_count += 1
    else:
        roll_dice(times=10,delay=0.5,positn=0)
        game.draw_dice(game.dice)
    
     
    if game.is_winner():
        # Call the animate_text function with desired text
        simple_animate_text(GREEN + BOLD + f"Winner! {player_name}" + RESET)
        simple_animate_text(BLUE + ITALIC + f"Total points: {game.total}" + RESET)
        text_to_blink = "CONGRATULATIONS..."
        color_to_use = colorama.Fore.GREEN
        hide_cursor()
        blink_thread = threading.Thread(target=blink_text, args=(text_to_blink, color_to_use))
        blink_thread.start()
        blink_thread.join()
        show_cursor()
        pygame.mixer.stop()
        voice = pyttsx3.init()
        voice.say(f"{player_name.capitalize()} won the game")
        voice.say(f"{player_name.capitalize()} congratulations")
        voice.say(f"Total points: {game.total}")
        voice.runAndWait()
        text =  "Thank You Everyone For Watching....." 
        color_combinations = [
                                (0, 128, 128),    # Teal
                                (128, 0, 128),    # Purple
                                (0, 0, 128),      # Navy
                                (128, 0, 0),      # Maroon
                                (128, 128, 0),    # Olive
                                (0, 128, 0),      # Green
                                (128, 128, 128)   # Gray
                            ]
        animate_text(text, color_combinations)
        text =  "Special Thanks to Eyong Kevin....." 
        color_combinations = [
                                        (255, 0, 0),     # Red
                                        (255, 165, 0),   # Orange
                                        (255, 255, 0),   # Yellow
                                        (0, 255, 0),     # Green
                                        (0, 0, 255),     # Blue
                                        (75, 0, 130),    # Indigo
                                        (128, 0, 128)    # Violet
                                    ]
        animate_text(text, color_combinations)

        show_image('winner')

        
    else:
        text = "Sorry! Try again"
        color_combinations = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # RGB color combinations
        animate_text(text, color_combinations)


        while game.roll_trials:
            print(RED + BOLD + f"{game.roll_trials} trial left" + RESET)

            roll_pos: list[int] = []
            added_dice: bool = False
           # print(GREEN + ITALIC + f"The dice game will start with {player_dice_count} dices: " + RESET, dice)
            simple_animate_text(BLUE + ITALIC + f"The dice game will start with {player_dice_count} dices: " + RESET)
            if player_dice_count < player_max_dice_count:
                if input(GREEN + BOLD + "Do you want to add a third dice 'D8'?, 'yes/no' " + RESET) == "yes":
                    game.add_dice(D8)
                    player_dice_count += 1
                    added_dice = True
                else:
                    roll_dice(times=10,delay=0.5,positn=0)    

            if not added_dice:
                if input(GREEN + UNDERLINE + "Do you want to roll specific dice? yes/no: " + RESET) == "yes":
                    position: str = input(
                       YELLOW + ITALIC +  f"Select which dice or dices to roll from {game.dice}. Select your dice:  " + RESET
                    )
                    roll_dice(times=10,delay=0.5,positn=position)
                    roll_pos = [int(pos) for pos in position.split()]
                   

            game.roll(roll_pos)
            
            print(YELLOW + ITALIC + "Dice Combination: " + RESET, game.dice)  # [2,3,4]
            game.draw_dice(game.dice)

            if game.is_winner():
                pygame.mixer.stop()
                voice = pyttsx3.init()
                voice.say(f"{player_name.capitalize()} won the game")
                voice.say(f"{player_name.capitalize()} congratulations")
                voice.runAndWait()
                simple_animate_text(GREEN + BOLD + f"Winner!  {player_name.capitalize()}" + RESET)
                simple_animate_text(BLUE + ITALIC + f"Total points: {game.total}" + RESET)

                text_to_blink = ITALIC + "CONGRATULATIONS..." + RESET
                color_to_use = colorama.Fore.GREEN
                hide_cursor()
                blink_thread = threading.Thread(target=blink_text, args=(text_to_blink, color_to_use))
                blink_thread.start()
                blink_thread.join()
                show_cursor()

                text = "Thank You Everyone For Watching....." 
                color_combinations = [
                                (0, 128, 128),    # Teal
                                (128, 0, 128),    # Purple
                                (0, 0, 128),      # Navy
                                (128, 0, 0),      # Maroon
                                (128, 128, 0),    # Olive
                                (0, 128, 0),      # Green
                                (128, 128, 128)   # Gray
                            ]
                animate_text(text, color_combinations)

                text =  "Special Thanks to Eyong Kevin....." 
                color_combinations =  [
                                        (255, 0, 0),     # Red
                                        (255, 165, 0),   # Orange
                                        (255, 255, 0),   # Yellow
                                        (0, 255, 0),     # Green
                                        (0, 0, 255),     # Blue
                                        (75, 0, 130),    # Indigo
                                        (128, 0, 128)    # Violet
                                    ]

                animate_text(text, color_combinations)
                time.sleep(1)
                break
            else:
                text = "Sorry! Try again...."
                color_combinations = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # RGB color combinations
                animate_text(text, color_combinations)


        else:
           # music_file = "/home/dci-student/Downloads/bensound-summer_mp3_music.mp3"
           # pygame.mixer.music.load(music_file)
          #  pygame.mixer.music.play(-1)  # -1 means loop indefinitely
            simple_animate_text(RED + BOLD + f"You have exhausted all your {game.initial_roll} trials" + RESET)
            text_to_blink = BOLD + ITALIC + "GAME OVER!" + RESET
            color_to_use = colorama.Fore.RED
            hide_cursor()
            blink_thread = threading.Thread(target=blink_text, args=(text_to_blink, color_to_use))
            blink_thread.start()
            blink_thread.join()
            show_cursor() 

            pygame.mixer.stop()
            voice = pyttsx3.init()
            voice_properties = voice.getProperty('rate')
            voice.setProperty('rate', voice_properties - 40)
            voice.say(f"Game Over! {player_name.capitalize()} ")
            voice.say("You have exhausted your {self.initial_roll} trials")
            voice.runAndWait()
            
            text =  "Thank You Everyone For Watching....." 
            color_combinations = [
                                (0, 128, 128),    # Teal
                                (128, 0, 128),    # Purple
                                (0, 0, 128),      # Navy
                                (128, 0, 0),      # Maroon
                                (128, 128, 0),    # Olive
                                (0, 128, 0),      # Green
                                (128, 128, 128)   # Gray
                            ]
            animate_text(text, color_combinations)
           
            text = "Special Thanks to Eyong Kevin....." 
            color_combinations = [
                                        (255, 0, 0),     # Red
                                        (255, 165, 0),   # Orange
                                        (255, 255, 0),   # Yellow
                                        (0, 255, 0),     # Green
                                        (0, 0, 255),     # Blue
                                        (75, 0, 130),    # Indigo
                                        (128, 0, 128)    # Violet
                                    ]
            animate_text(text, color_combinations)
            time.sleep(1)
           




            
      
   
           
