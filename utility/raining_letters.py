import pygame
import random

def generate_random_letter():
    letters = [chr(i) for i in range(65, 91)]  
    return random.choice(letters)

def generate_random_position(SCREEN_WIDTH, SCREEN_HEIGHT):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(-200, -100)  
    return x, y

def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class RainingLetter:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.letter = generate_random_letter()
        self.x, self.y = generate_random_position(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.speed = random.randint(2, 5)
        self.color = generate_random_color()

    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-200, -100)
            self.x = random.randint(0, SCREEN_WIDTH)
            self.color = generate_random_color()

    def draw(self, screen):
        letter_font = pygame.font.Font(None, 36)
        letter_surface = letter_font.render(self.letter, True, self.color)
        screen.blit(letter_surface, (self.x, self.y))
