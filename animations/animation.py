import time
from utility.utility import clear_screen
import random
from diceart.dice_art import diece_pic
import threading
import colorama
import sys
from diceart.dice_art import color_dict

blinking = True
num_blinks = 0
max_blinks = 5 

def animate_text(text,color_combinations):
    
    reset_code = "\033[0m"  
    try:
        for _ in range(1):
            for i, char in enumerate(text):
                color = color_combinations[i % len(color_combinations)]
                fg_color_code = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
                print(f"{fg_color_code}{char}", end='', flush=True)
                time.sleep(0.1)
            print(reset_code)
            print('\n')  
    except Exception as e:
        print("An error occurred:", e)        
      

def animate_dice(pos0=0,pos1=0,pos2=0):
    
    try:
        for _ in range(12):
            clear_screen()
            animated_dice = random.choice(list(diece_pic.keys()))

            if pos0 == 0 and pos1 != 0 and pos2 != 0:   # (0,8,6)
                print(diece_pic[animated_dice])
                print(diece_pic[f'{pos1}'])
                print(diece_pic[f'{pos2}']) 
            elif pos0 != 0 and pos1 == 0 and pos2 != 0:  # (5,0,6)
                print(diece_pic[f'{pos0}'])
                print(diece_pic[animated_dice])
                print(diece_pic[f'{pos2}'])
            elif pos0 != 0 and pos1 != 0 and pos2 == 0:  # (5,8,0)
                print(diece_pic[f'{pos0}'])
                print(diece_pic[f'{pos1}']) 
                print(diece_pic[animated_dice])   

            elif pos0 == 0 and pos1 != 0 and pos2 == 0: # (0,8)
                print(diece_pic[animated_dice])
                print(diece_pic[f'{pos1}'])
                
            elif pos0 != 0 and pos1 == 0 and pos2 == 0: # (5,0)
                print(diece_pic[f'{pos0}'])
                print(diece_pic[animated_dice]) 

            time.sleep(0.5) 

    except IndexError as e:
        print("IndexError occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)        


def position_change(die:tuple,pos:int) -> tuple:   # if user want to roll first position in (5,9,2), called random.randint in first position to get a new tuple (3,9,2)
    
    try:
        if pos < 1 or pos > 3:
            raise ValueError("Position must be between 1 and 3.")
        
        replacement_integer = 0                     
        my_tuple = die
        replacement_integer = random.randint(1, 8)  

        my_list = list(my_tuple)

        if pos == 1:
            index_to_replace = my_list.index(my_list[0])
        elif pos == 2:
            index_to_replace = my_list.index(my_list[1])
        elif pos == 3:
            index_to_replace = my_list.index(my_list[2])    

        my_list[index_to_replace] = replacement_integer
        modified_tuple = tuple(my_list)
        return modified_tuple  
    
    except ValueError as e:
        print("ValueError:", e)
        return die  # Return the original tuple if an error occurs
    except Exception as e:
        print("An unexpected error occurred:", e)
        return die  # Return the original tuple if an error occurs     
    

def roll_dice(input_dice:tuple,posin = 0):

    try:
        print(input_dice)
            
        times = 12
        delay = 0.5
         
        if posin == 0:    # condition which user did not mentioned to roll specific position
            
            for _ in range(times):
                
                clear_screen()
                
                dice1 = random.choice(list(diece_pic.keys()))
                dice2 = random.choice(list(diece_pic.keys()))
                dice3 = random.choice(list(diece_pic.keys()))  

                if len(input_dice) == 2:
                    
                    print(diece_pic[dice1])
                    print(diece_pic[dice2])
                elif len(input_dice) == 3:
                    print(diece_pic[dice1])
                    print(diece_pic[dice2])
                    print(diece_pic[dice3])
            
                time.sleep(delay)

        elif posin == '1':
                modify = position_change(input_dice, int(posin))
                if len(modify) == 3:
                    animate_thread = threading.Thread(target=animate_dice, args=(0,modify[1],modify[2])) #(0,8,6)
                elif len(modify) == 2:
                    animate_thread = threading.Thread(target=animate_dice, args=(0,modify[1],0)) #(0,8)   
                animate_thread.start()
                animate_thread.join()
        elif posin == '2':
                modify = position_change(input_dice, int(posin))
                if len(modify) == 3:
                    animate_thread = threading.Thread(target=animate_dice, args=(modify[0],0, modify[2]))  # (5,0,6)
                elif len(modify) == 2:
                    animate_thread = threading.Thread(target=animate_dice, args=(modify[1],0,0))  # (5,0)
                animate_thread.start()
                animate_thread.join()
        elif posin == '3':
                modify = position_change(input_dice, int(posin))
                if len(modify) == 3:
                    animate_thread = threading.Thread(target=animate_dice, args=(modify[0], modify[1],0))  # (5,8,0)
                animate_thread.start()
                animate_thread.join()    
    except KeyError as e:
        print("KeyError:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)             

           
def simple_animate_text(text):

    try:
        for _ in range(1):  
            for char in text:
                print(char, end='', flush=True)  
                time.sleep(0.1)  
            print('\n')    
    except Exception as e:
        print("An unexpected error occurred:", e)        
               

def blink_text(text,color):

    try:
        global blinking, num_blinks
        while blinking and num_blinks < max_blinks:
            print(color + text + colorama.Style.RESET_ALL, end='\r', flush=True)
            time.sleep(0.5)  
            print(' ' * len(text), end='\r', flush=True)  
            time.sleep(0.5)
            num_blinks += 1
        blinking = False           
    except Exception as e:
        print("An unexpected error occurred:", e)             

def hide_cursor():
    sys.stdout.write("\033[?25l")  

def show_cursor():
    sys.stdout.write("\033[?25h")  

 
      

           



