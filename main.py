import pygame
import random
from constants import *
from drawing import draw_bars
from algorithms import bubble_sort

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Algorithm Visualizer - Press SPACE to Sort, R to Reset")
    clock = pygame.time.Clock()

    list_size = 50
    
    def generate_new_list():
        return random.sample(range(10, 101), list_size)

    my_data = generate_new_list()
    sort_generator = bubble_sort(my_data)
    sorting = False

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                if event.key == pygame.K_r:
                    my_data = generate_new_list()
                    sort_generator = bubble_sort(my_data)
                    sorting = False

        if sorting:
            try:
                data_for_drawing = next(sort_generator)
            except StopIteration:
                sorting = False
        else:
            data_for_drawing = (my_data, ())
        
        draw_bars(screen, data_for_drawing)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()