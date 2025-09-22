#Bubble Sort

def bubble_sort(data_list):
    n = len(data_list)
    for i in range (n):
        for j in range (0, n-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
            yield data_list,(j,j+1)

#Insertion Sort

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
