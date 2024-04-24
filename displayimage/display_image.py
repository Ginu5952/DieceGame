import time
import pygame
from utility.static_msg import draw_static_message
from utility.raining_letters import RainingLetter

def show_image(imge,duration):

    try:
        if imge == 'welcome':
        
            
            screen_width = 800
            screen_height = 600
            screen = pygame.display.set_mode((screen_width, screen_height))
            pygame.display.set_caption("WELCOME")
            image = pygame.image.load("/home/dci-student/Desktop/dice_game/images/dice.jpeg")
            image_width, image_height = image.get_size()
            scaled_image = pygame.transform.scale(image, (screen_width, screen_height))
            screen.blit(scaled_image, (0, 0))
            pygame.display.flip()
            end_time = time.time() + duration
            
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                if time.time() >= end_time:
                    running = False   
    except pygame.error as e:
        print("An error occurred:", e)
    finally:
        pygame.quit()                
           

def shower_congratulation():
    
    try:
        SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Congratulations")
        raining_letters = []

    
        for _ in range(30):
            raining_letters.append(RainingLetter(SCREEN_WIDTH, SCREEN_HEIGHT))

        running = True
        clock = pygame.time.Clock()
        time_limit = 10
        start_time = pygame.time.get_ticks()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        
            screen.fill((0, 0, 0))

        
            draw_static_message(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        
            for letter in raining_letters:
                letter.move(SCREEN_WIDTH, SCREEN_HEIGHT)
                letter.draw(screen)

            pygame.display.flip()
            clock.tick(30)

            if pygame.time.get_ticks() - start_time >= time_limit * 1000:
                running = False

    except pygame.error as e:
            print("An error occurred:", e)
    finally:
        pygame.quit()
        

