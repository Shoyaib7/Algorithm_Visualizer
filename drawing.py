import pygame
from constants import *

def draw_text(screen, text, font, color, pos):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def draw_menu(screen, algorithms):
    font = pygame.font.SysFont('Arial', 24)
    title_font = pygame.font.SysFont('Arial', 32, bold=True)

    title_surface = title_font.render("Select an Algorithm:", True, WHITE)
    screen.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 50))

    for i, name in enumerate(algorithms):
        text = f"{i + 1}. {name}"
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 120 + i * 40))    

def draw_bars(screen, data_info):
    data_list = data_info['list']
    highlights = data_info['highlights']
    
    bar_width = SCREEN_WIDTH / len(data_list)
    max_val = max(data_list) if data_list else 1

    for i, val in enumerate(data_list):
        bar_height = (val / max_val) * (SCREEN_HEIGHT * 0.8)
        x_pos = i * bar_width
        y_pos = SCREEN_HEIGHT - bar_height
        
        color = WHITE
        
        if i in highlights.get('pivot', []):
            color = GREEN
        elif i in highlights.get('pointers', []):
            color = BLUE
        elif i in highlights.get('general', []):
            color = RED
            
        pygame.draw.rect(screen, color, (x_pos, y_pos, bar_width, bar_height))
