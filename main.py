import pygame
import random
from constants import *
from drawing import draw_bars, draw_menu
from algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Algorithm Visualizer - Press 'R' to Reset")
    clock = pygame.time.Clock()

    list_size = 50
    
    def generate_new_list():
        return random.sample(range(10, 101), list_size)

    my_data = generate_new_list()
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort
    }
    algo_names = list(algorithms.keys())
    sort_generator = None
    
    app_state = 'menu'

    running = True
    while running:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    my_data = generate_new_list()
                    sort_generator = None
                    app_state = 'menu'
                
                if app_state == 'menu':
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                        choice_index = event.key - pygame.K_1
                        if choice_index < len(algo_names):
                            algo_name = algo_names[choice_index]
                            sort_generator = algorithms[algo_name](my_data)
                            app_state = 'sorting'
        
        if app_state == 'menu':
            draw_menu(screen, algo_names)
        
        elif app_state == 'sorting':
            screen.fill(BLACK)
            if sort_generator:
                try:
                    data_for_drawing = next(sort_generator)
                    draw_bars(screen, data_for_drawing)
                except StopIteration:
                    draw_bars(screen, (my_data, ()))
                    sort_generator = None
            else:
                 draw_bars(screen, (my_data, ()))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
