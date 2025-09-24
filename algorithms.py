# Bubble Sort

def bubble_sort(data_list):
    n = len(data_list)
    for i in range (n):
        for j in range (0, n-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
            yield data_list,(j,j+1)

# Insertion Sort

def insertion_sort(data_list):
    for i in range(1, len(data_list)):
        key = data_list[i]
        j = i - 1
        while j >= 0 and key < data_list[j]:
            data_list[j + 1] = data_list[j]
            yield data_list, (i, j, -1)
            j -= 1
        data_list[j + 1] = key
        yield data_list, (i, j + 1, -2)
    yield data_list, ()

# Selection Sort

def selection_sort(data_list):
    n = len(data_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data_list[j] < data_list[min_idx]:
                min_idx = j
            yield data_list, (j, min_idx)
        data_list[i], data_list[min_idx] = data_list[min_idx], data_list[i]
        yield data_list, (i, min_idx)
    yield data_list, ()    

# Merge Sort

def merge_sort(data_list):
    yield from merge_sort_recursive(data_list, 0, len(data_list) - 1)
    yield data_list, ()

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
        yield data_list, (k,)
        k += 1

    while i < len(left_copy):
        data_list[k] = left_copy[i]
        yield data_list, (k,)
        i += 1
        k += 1

    while j < len(right_copy):
        data_list[k] = right_copy[j]
        yield data_list, (k,)
        j += 1
        k += 1
