import pygame
from constants import *

def draw_bars(screen, data_info):
    screen.fill(BLACK)
    data_list = data_info[0]
    highlight_indices = data_info[1]
    bar_width = SCREEN_WIDTH / len(data_list)
    
    if not data_list:
        return
        
    max_val = max(data_list)

    for i, val in enumerate(data_list):
        bar_height = (val / max_val) * (SCREEN_HEIGHT * 0.9)
        x_pos = i * bar_width
        y_pos = SCREEN_HEIGHT - bar_height
        
        color = WHITE
        if i in highlight_indices:
            color = RED

        pygame.draw.rect(screen, color, (x_pos, y_pos, bar_width, bar_height))