import time
from music.music_player import initialize_mixer,play_announcement
import pygame
from typing import NoReturn
from dice import D4, D6, D8, Dice
from dice_board import DummyDice
from colors.color import color_combinations1,color_combinations2,color_combinations
import os
import colorama
import threading

from utility.utility import clear_screen
from displayimage.display_image import show_image,shower_congratulation
from animations.animation import animate_text,roll_dice,simple_animate_text,blink_text,hide_cursor,show_cursor
from diceart.dice_art import color_dict,style_dict,print_multicolor_text,diece_pic,diceart,colour_text_plus_blink_effects

colorama.init()

#--------------------------------------------------DiceGame------------------------------------------------------#

class DiceGame:

    def __init__(self, dice_board: DummyDice, player_name: str) -> None:
        self._dice_board: DummyDice = dice_board
        self._player_name: str = player_name
        self.roll_trials: int = 5
        self.initial_roll: int = self.roll_trials

    def is_winner(self) -> bool:
        return self._dice_board.check_winner()
    

    def roll(self, roll_pos: list[int] | None = None) -> None | NoReturn:
       
        print(color_dict["GREEN"] + style_dict["ITALIC"] + "rolling...." + color_dict["RESET"])
       
        if self.roll_trials:
            if roll_pos:
                try:
                    roll = self._dice_board.pos_to_be_rolled(roll_pos)
                    if isinstance(roll,DummyDice):
                        self._dice_board.roll()
                        self.roll_trials -= 1
                    else:
                        print(color_dict["RED"] + '\nPosition cannot be rolled! Out of range' + color_dict["RESET"])    
                except Exception as e:
                    print(e)       
        else:
            pygame.mixer.stop()
            play_announcement(f"Game Over {player_name} ")
            play_announcement("You have exhausted your {self.initial_roll} trials")
           
            raise PermissionError(f"You have exhausted your {self.initial_roll} trials")
        

    def add_dice(self, dice: type[Dice]) -> None:
        self._dice_board + dice

    def draw_dice(self,game):
        print(game)
        clear_screen()
        for dicee in game:
            for key,pic in diece_pic.items():
                try:
                    if str(dicee) == key:
                        print(pic)
                        print('\t')   
                except KeyError:
                    print("Key not found in dictionary.")          

    @property
    def total(self) -> int:
        return self._dice_board.plus(len(self.dice)).total

    @property
    def dice(self):
        return self._dice_board.dice
     
#-----------------------------------------------------__main__-------------------------------------------------------------#

if __name__ == "__main__":

    
    initialize_mixer()
    player_dice_count: int = 2
    player_max_dice_count: int = 3

    clear_screen()
    
    print_multicolor_text(diceart, color_combinations1)
    time.sleep(2)
    clear_screen()
    colour_text_plus_blink_effects(diceart)
 
    player_name: str = input(color_dict["PURPLE"] + style_dict["ITALIC"] + "\nPlayer, state your name: " )
   

    text = color_dict["GREEN"] + style_dict["ITALIC"] +  f'\nWelcome {player_name.capitalize()}' + color_dict["RESET"]
    simple_animate_text(text)

    show_image('welcome',3)
  
    play_announcement(f"Welcome {player_name} ","winner")
    play_announcement(f"Welcome to dice game ","winner")

    pygame.init()

    try:
      
        print(f'{os.path.join(os.getcwd())}')
        music_file = os.path.join(os.getcwd(), "bgm_music", "bensound-summer_mp3_music.mp3")
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  
    except pygame.error as e:
        print("Error occurred while playing the music:", e) 

    dice = DummyDice(D4, D6)
    simple_animate_text(color_dict["GREEN"] + style_dict["ITALIC"] + f"The dice game will start with {player_dice_count} dices: " + color_dict["RESET"])
    print(color_dict["BLUE"] + style_dict["BOLD"] + f'{dice}' + color_dict["RESET"])
    game: DiceGame = DiceGame(dice, player_name)
    simple_animate_text(color_dict["GREEN"] + style_dict["ITALIC"] + "You will have more points if you add a third dice, D8" + color_dict["RESET"])
    
    if input(color_dict["YELLOW"] + style_dict["BOLD"] + "Do you want to add a third dice: 'D8'?, yes/no: " ) == "yes":
        game.add_dice(D8)
        player_dice_count += 1
        roll_dice(game.dice,0)
    else:
        roll_dice(game.dice,0)
        game.draw_dice(game.dice)

 #--------------------------------------------------winner--------------------------------------------------------------------#    

    if game.is_winner():
        
        simple_animate_text(color_dict["GREEN"] + style_dict["BOLD"] + f"Winner! {player_name}" + color_dict["RESET"])
        simple_animate_text(color_dict["BLUE"]+ style_dict["ITALIC"] + f"Total points: {game.total}" + color_dict["RESET"])
        text_to_blink = style_dict["ITALIC"] + "CONGRATULATIONS..." + color_dict["RESET"]
        color_to_use = colorama.Fore.GREEN
        hide_cursor()
        blink_thread = threading.Thread(target=blink_text, args=(text_to_blink, color_to_use))
        blink_thread.start()
        blink_thread.join()
        show_cursor()
        pygame.mixer.stop()
        
        play_announcement(f"{player_name.capitalize()} won the game","winner")
        play_announcement(f"{player_name.capitalize()} congratulations","winner")
        play_announcement(f"Total points: {game.total}","winner")
       
        text =  "Thank You Everyone For Watching....." 
        
        animate_text(text, color_combinations1)
        text =  "Special Thanks to Eyong Kevin....." 
        
        animate_text(text, color_combinations2)

        shower_congratulation()
       
    else:
        text = "Sorry! Try again"
        
        animate_text(text, color_combinations)

        while game.roll_trials:

            print(color_dict["RED"] + style_dict["BOLD"] + f"{game.roll_trials} trial left" + color_dict["RESET"])
            roll_pos: list[int] = []
            added_dice: bool = False
            simple_animate_text( color_dict["BLUE"] + style_dict["ITALIC"] + f"The dice game will start with {player_dice_count} dices: " + color_dict["RESET"])
            
            if player_dice_count < player_max_dice_count:

                if input(color_dict["GREEN"] + style_dict["BOLD"] + "Do you want to add a third dice 'D8'?, 'yes/no' " ) == "yes":
                    game.add_dice(D8)
                    player_dice_count += 1
                    added_dice = True
                    roll_dice(game.dice,0)
                else:
                    roll_dice(game.dice,0)    

            if not added_dice:
                
                if input(color_dict["GREEN"] + style_dict["ITALIC"] + "Do you want to roll specific dice? yes/no: " ) == "yes":
                    print('\n')
                    position: str = input(
                       color_dict["YELLOW"] + style_dict["ITALIC"] +  f"Select which dice or dices to roll from {game.dice}. Select your dice:  " + color_dict["RESET"]
                    )
                    roll_dice(game.dice,position)
                    roll_pos = [int(pos) for pos in position.split()]
                   

            game.roll(roll_pos)
            
            print(color_dict["YELLOW"] + style_dict["ITALIC"] + "Dice Combination: " + color_dict["RESET"], game.dice)  # [2,3,4]
            game.draw_dice(game.dice)

            if game.is_winner():

                pygame.mixer.stop()
                play_announcement(f"{player_name.capitalize()} won the game","winner")
                play_announcement(f"{player_name.capitalize()} congratulations","winner")

                simple_animate_text(color_dict["GREEN"] + style_dict["BOLD"] + f"Winner!  {player_name.capitalize()}" + color_dict["RESET"])
                simple_animate_text(color_dict["BLUE"] + style_dict["ITALIC"] + f"Total points: {game.total}" + color_dict["RESET"])

                text_to_blink = style_dict["ITALIC"] + "CONGRATULATIONS..." + color_dict["RESET"]
                color_to_use = colorama.Fore.GREEN
                hide_cursor()
                blink_thread = threading.Thread(target=blink_text, args=(text_to_blink, color_to_use))
                blink_thread.start()
                blink_thread.join()
                show_cursor()

                text = "Thank You Everyone For Watching....." 
                
                animate_text(text, color_combinations1)

                text =  "Special Thanks to Eyong Kevin....." 
               
                animate_text(text, color_combinations2)
                time.sleep(1)
                shower_congratulation()
                break
            else:
                text = "Sorry! Try again...."
                color_combinations = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  
                animate_text(text, color_combinations)

        else:
          
            simple_animate_text(color_dict["RED"] + style_dict["BOLD"] + f"You have exhausted all your {game.initial_roll} trials" + color_dict["RESET"])
            text_to_blink = style_dict["BOLD"] + style_dict["ITALIC"] + "GAME OVER!" + color_dict["RESET"]
            color_to_use = colorama.Fore.RED
            hide_cursor()
            blink_thread = threading.Thread(target=blink_text, args=(text_to_blink, color_to_use))
            blink_thread.start()
            blink_thread.join()
            show_cursor() 

            pygame.mixer.stop()
            play_announcement(f"Game Over! {player_name.capitalize()} ","failed")
            play_announcement("You have exhausted your {self.initial_roll} trials","failed")
            
            text =  "Thank You Everyone For Watching....." 
           
            animate_text(text, color_combinations1)
           
            text =  "Special Thanks to Eyong Kevin....." 
           
            animate_text(text, color_combinations2)
            time.sleep(1)
            shower_congratulation()




            
      
   
           
