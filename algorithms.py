# Bubble Sort

def bubble_sort(data_list):
    n = len(data_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
            yield {'list': data_list, 'highlights': {'general': (j, j + 1)}}
    yield {'list': data_list, 'highlights': {}}

# Insertion Sort

def insertion_sort(data_list):
    for i in range(1, len(data_list)):
        key = data_list[i]
        j = i - 1
        while j >= 0 and key < data_list[j]:
            data_list[j + 1] = data_list[j]
            yield {'list': data_list, 'highlights': {'pointers': (i, j)}}
            j -= 1
        data_list[j + 1] = key
        yield {'list': data_list, 'highlights': {'general': (i, j + 1)}}
    yield {'list': data_list, 'highlights': {}}

# Selection Sort

def selection_sort(data_list):
    n = len(data_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data_list[j] < data_list[min_idx]:
                min_idx = j
            yield {'list': data_list, 'highlights': {'pointers': (j, min_idx)}}
        data_list[i], data_list[min_idx] = data_list[min_idx], data_list[i]
        yield {'list': data_list, 'highlights': {'general': (i, min_idx)}}
    yield {'list': data_list, 'highlights': {}}

# Merge Sort

def merge_sort(data_list):
    yield from merge_sort_recursive(data_list, 0, len(data_list) - 1)
    yield {'list': data_list, 'highlights': {}}

def merge_sort_recursive(data_list, left, right):
    if left < right:
        middle = (left + right) // 2
        yield from merge_sort_recursive(data_list, left, middle)
        yield from merge_sort_recursive(data_list, middle + 1, right)
        yield from merge(data_list, left, middle, right)

def merge(data_list, left, middle, right):
    left_copy = data_list[left : middle + 1]
    right_copy = data_list[middle + 1 : right + 1]
    i = j = 0
    k = left
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            data_list[k] = left_copy[i]
            i += 1
        else:
            data_list[k] = right_copy[j]
            j += 1
        yield {'list': data_list, 'highlights': {'general': (k,)}}
        k += 1
    while i < len(left_copy):
        data_list[k] = left_copy[i]
        yield {'list': data_list, 'highlights': {'general': (k,)}}
        i += 1
        k += 1
    while j < len(right_copy):
        data_list[k] = right_copy[j]
        yield {'list': data_list, 'highlights': {'general': (k,)}}
        j += 1
        k += 1

# Quick Sort

def quick_sort(data_list):
    yield from quick_sort_recursive(data_list, 0, len(data_list) - 1)
    yield {'list': data_list, 'highlights': {}}

def quick_sort_recursive(data_list, low, high):
    if low < high:
        pi = yield from partition(data_list, low, high)
        yield from quick_sort_recursive(data_list, low, pi - 1)
        yield from quick_sort_recursive(data_list, pi + 1, high)

def partition(data_list, low, high):
    pivot = data_list[high]
    i = low - 1

    for j in range(low, high):
        if data_list[j] <= pivot:
            i += 1
            data_list[i], data_list[j] = data_list[j], data_list[i]
        
        highlights = {'pivot': [high], 'pointers': [i, j]}
        yield {'list': data_list, 'highlights': highlights}

    data_list[i + 1], data_list[high] = data_list[high], data_list[i + 1]
    yield {'list': data_list, 'highlights': {'pivot': [i + 1]}}
    return i + 1

# Heap Sort

def heapify(data_list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data_list[left] > data_list[largest]:
        largest = left

    if right < n and data_list[right] > data_list[largest]:
        largest = right

    if largest != i:
        data_list[i], data_list[largest] = data_list[largest], data_list[i]
        yield {'list': data_list, 'highlights': {'pointers': (i, largest)}}
        yield from heapify(data_list, n, largest)

def heap_sort(data_list):
    n = len(data_list)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(data_list, n, i)

    for i in range(n - 1, 0, -1):
        data_list[i], data_list[0] = data_list[0], data_list[i]  # swap
        yield {'list': data_list, 'highlights': {'general': (i, 0)}}
        yield from heapify(data_list, i, 0)
    
    yield {'list': data_list, 'highlights': {}}

# Radix Sort

def counting_sort_for_radix(data_list, exp):
    n = len(data_list)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = data_list[i] // exp
        count[index % 10] += 1
        yield {'list': data_list, 'highlights': {'pointers': [i]}}

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = data_list[i] // exp
        output[count[index % 10] - 1] = data_list[i]
        count[index % 10] -= 1
        yield {'list': output, 'highlights': {'general': [i]}}
        i -= 1

    for i in range(n):
        data_list[i] = output[i]
        yield {'list': data_list, 'highlights': {'general': [i]}}

def radix_sort(data_list):
    if not data_list:
        yield {'list': data_list, 'highlights': {}}
        return

    max1 = max(data_list)
    exp = 1

    while max1 // exp > 0:
        yield from counting_sort_for_radix(data_list, exp)
        exp *= 10
    
    yield {'list': data_list, 'highlights': {}}

# Shell Sort

def shell_sort(data_list):
    n = len(data_list)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data_list[i]
            j = i
            while j >= gap and data_list[j - gap] > temp:
                data_list[j] = data_list[j - gap]
                yield {'list': data_list, 'highlights': {'pointers': (j, j - gap)}}
                j -= gap
            data_list[j] = temp
            yield {'list': data_list, 'highlights': {'general': (i, j)}}
        gap //= 2
    
    yield {'list': data_list, 'highlights': {}}

# Bucket Sort

def bucket_sort(data_list):
    if not data_list:
        yield {'list': data_list, 'highlights': {}}
        return

    max_val = max(data_list)
    size = max_val / len(data_list) if len(data_list) > 0 else 1
    bucket_list = [[] for _ in range(len(data_list))]

    for i in range(len(data_list)):
        j = int(data_list[i] / size)
        if j >= len(data_list):
            j = len(data_list) - 1
        bucket_list[j].append(data_list[i])
        yield {'list': data_list, 'highlights': {'pointers': [i]}}

    final_list = []
    for i in range(len(bucket_list)):
        bucket_generator = insertion_sort(bucket_list[i])
        while True:
            try:
                next_state = next(bucket_generator)
                bucket_list[i] = next_state['list']
                current_full_list = final_list + [item for sublist in bucket_list[i:] for item in sublist]
                
                yield {'list': current_full_list, 'highlights': next_state['highlights']}
            except StopIteration:
                break

        final_list.extend(bucket_list[i])

    for i in range(len(final_list)):
        data_list[i] = final_list[i]
        yield {'list': data_list, 'highlights': {'general': [i]}}

    yield {'list': data_list, 'highlights': {}}

# Counting Sort

def counting_sort(data_list):
    if not data_list:
        yield {'list': data_list, 'highlights': {}}
        return

    max_val = max(data_list)
    n = len(data_list)
    output = [0] * n
    count = [0] * (max_val + 1)

    for i in range(n):
        count[data_list[i]] += 1
        yield {'list': data_list, 'highlights': {'pointers': [i]}}

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        output[count[data_list[i]] - 1] = data_list[i]
        count[data_list[i]] -= 1
        yield {'list': output, 'highlights': {'general': [i]}}
        i -= 1

    for i in range(n):
        data_list[i] = output[i]
        yield {'list': data_list, 'highlights': {'general': [i]}}

    yield {'list': data_list, 'highlights': {}}    
