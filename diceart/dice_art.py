
import time
from colorama import init, Fore

init()

def colors():
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;206m'

    return {
        "RESET": RESET,
        "RED": RED,
        "GREEN": GREEN,
        "YELLOW": YELLOW,
        "BLUE": BLUE,
        "PURPLE": PURPLE,
        "CYAN": CYAN,
        "ORANGE": ORANGE,
        "PINK": PINK
    }   

# Font Styles
def styles():
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m' 
    STRIKETHROUGH = '\033[9m'

    return {
        "BOLD": BOLD,
        "ITALIC": ITALIC,
        "UNDERLINE": UNDERLINE,
        "STRIKETHROUGH": STRIKETHROUGH
    }

color_dict = colors()
style_dict = styles()

diceart = '''
    _________                                                                        _________ 
   /\        \\           ____ ___ ____ _____    ____    _    __  __ _____          /\\        \\
  / ●\\    ●   \\         |  _ \\_ _/ ___| ____|  / ___|  / \\  |  \\/  | ____|        / ●\\    ●   \\
 /    \\________\\        | | | | | |   |  _|   | |  _  / _ \\ | |\\/| |  _|         /    \\________\\
 \\    / ●      /        | |_| | | |___| |___  | |_| |/ ___ \\| |  | | |___         \\    / ●      / 
  \\● /    ●   /         |____/___\\____|_____|  \\____/_/   \\_\\_|  |_|_____|         \\● /    ●   /  
   \\/_______●/                                                                      \\/_______●/ 
'''

diece_pic = {  '1':  color_dict["RED"]+ style_dict["BOLD"] +
            """
            ╭─────────╮
            |         |  
            |    ●    |
            |         |         
            ╰─────────╯
            """ + color_dict["RESET"],
            '2': color_dict["GREEN"] + style_dict["BOLD"] +
            """
            ╭─────────╮
            |  ●      |  
            |         |
            |      ●  |         
            ╰─────────╯
            """ + color_dict["RESET"],
            '3': color_dict["RED"] + style_dict["BOLD"] +
            """
            ╭─────────╮
            |  ●      |  
            |    ●    |
            |      ●  |         
            ╰─────────╯
            """ + color_dict["RESET"],
            '4': color_dict["YELLOW"] + style_dict["BOLD"] +
            """
            ╭─────────╮
            |  ●   ●  |  
            |         |
            |  ●   ●  |         
            ╰─────────╯
            """ + color_dict["RESET"],
            '5': color_dict["ORANGE"] + style_dict["BOLD"] +
            """
            ╭─────────╮
            |  ●   ●  |  
            |    ●    |
            |  ●   ●  |         
            ╰─────────╯ 
            """ + color_dict["RESET"],
            '6': color_dict["PINK"] + style_dict["BOLD"] +
            """
            ╭─────────╮
            |  ●   ●  |  
            |  ●   ●  |
            |  ●   ●  |         
            ╰─────────╯
            """ + color_dict["RESET"],
            '7':  color_dict["CYAN"]+ style_dict["BOLD"] +
            """
            ╭─────────╮
            |  ●   ●  |  
            |  ● ● ●  |
            |  ●   ●  |         
            ╰─────────╯
            """ + color_dict["RESET"],
            '8': color_dict["BLUE"] + style_dict["BOLD"] +
            """
            ┌─────────┐
            |  ● ● ●  |  
            |  ●   ●  |
            |  ● ● ●  |         
            ╰─────────╯
            """ + color_dict["RESET"]
            }
              
    
def print_multicolor_text(text, color_combinations):

    try:
        reset_code = "\033[0m"  
        
        for i, char in enumerate(text):
            
            color = color_combinations[i % len(color_combinations)]
            
            fg_color_code = f"\033[38;2;{color[0]};{color[1]};{color[2]}m"
        
            print(f"{fg_color_code}{char}", end="")
    
        print(reset_code)
        print('\n') 
    except Exception as e:
        print("An unexpected error occurred:", e)    
   

def colour_text_plus_blink_effects(text):
    
    try:
        colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA]  
        delay = 1  
        total_duration = 5  
        start_time = time.time()  

        while True:
            for color in colors:
                
                print(color + text)
                time.sleep(delay) 
                print("\033[H\033[J", end="")
            
                
                if time.time() - start_time >= total_duration:
                    break
            else:
                continue
            break  
    except Exception as e:
        print("An unexpected error occurred:", e)    
    




       