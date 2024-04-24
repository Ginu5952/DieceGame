import pygame
import random

def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_static_message(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    static_font = pygame.font.Font(None, 48)
    static_message = "Congratulations!"
    static_color = generate_random_color()
    static_surface = static_font.render(static_message, True, static_color)
    static_rect = static_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(static_surface, static_rect)
