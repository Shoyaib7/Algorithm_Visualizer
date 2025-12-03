import pygame
import random
from constants import *
from drawing import draw_bars, draw_menu, draw_text
from algorithms import (bubble_sort, insertion_sort, selection_sort, merge_sort, 
                        quick_sort, heap_sort, radix_sort, shell_sort, bucket_sort,
                        counting_sort, cocktail_shaker_sort)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Algorithm Visualizer")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 18)

    list_size = 50
    
    def generate_new_list():
        return [random.randint(10, 100) for _ in range(list_size)]

    my_data = generate_new_list()
    
    algorithms = {
        "Bubble Sort":          {'func': bubble_sort, 'comp': 'O(n^2)'},
        "Insertion Sort":       {'func': insertion_sort, 'comp': 'O(n^2)'},
        "Selection Sort":       {'func': selection_sort, 'comp': 'O(n^2)'},
        "Merge Sort":           {'func': merge_sort, 'comp': 'O(n log n)'},
        "Quick Sort":           {'func': quick_sort, 'comp': 'O(n log n)'},
        "Heap Sort":            {'func': heap_sort, 'comp': 'O(n log n)'},
        "Radix Sort":           {'func': radix_sort, 'comp': 'O(nk)'},
        "Shell Sort":           {'func': shell_sort, 'comp': 'O(n^2) worst case'},
        "Bucket Sort":          {'func': bucket_sort, 'comp': 'O(n+k) average'},
        "Counting Sort":        {'func': counting_sort, 'comp': 'O(n+k)'},
        "Cocktail Shaker Sort": {'func': cocktail_shaker_sort, 'comp': 'O(n^2)'}
    }
    algo_names = list(algorithms.keys())
    sort_generator = None
    current_algo_info = None
    
    app_state = 'menu'
    user_input = "" 

    running = True
    while running:
        clock.tick(60)
        
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    my_data = generate_new_list()
                    sort_generator = None
                    app_state = 'menu'
                    user_input = ""
                
                if app_state == 'menu':
                    if event.key == pygame.K_RETURN: 
                        try:
                            choice_num = int(user_input)
                            if 1 <= choice_num <= len(algo_names):
                                choice_index = choice_num - 1
                                algo_name = algo_names[choice_index]
                                current_algo_info = {'name': algo_name, 'comp': algorithms[algo_name]['comp']}
                                
                                if algo_name == "Bucket Sort":
                                    my_data = [random.randint(10, 100) for _ in range(list_size)]
                                else:
                                    my_data = generate_new_list()
                                    
                                sort_generator = algorithms[algo_name]['func'](my_data)
                                app_state = 'sorting'
                                user_input = ""
                        except ValueError:
                            user_input = ""
                    
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1] 
                    
                    elif event.unicode.isdigit():
                        user_input += event.unicode 
        
        if app_state == 'menu':
            draw_menu(screen, algo_names, user_input)
        
        elif app_state == 'sorting':
            if sort_generator:
                try:
                    data_for_drawing = next(sort_generator)
                    draw_bars(screen, data_for_drawing)
                except StopIteration:
                    draw_bars(screen, {'list': my_data, 'highlights': {}})
                    sort_generator = None
            else:
                 draw_bars(screen, {'list': my_data, 'highlights': {}})
            
            if current_algo_info:
                draw_text(screen, f"Algorithm: {current_algo_info['name']}", font, WHITE, (10, 10))
                draw_text(screen, f"Time Complexity: {current_algo_info['comp']}", font, WHITE, (10, 35))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
