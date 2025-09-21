#Bubble Sort

def bubble_sort(data_list):
    n = len(data_list)
    for i in range (n):
        for j in range (0, n-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
            yield data_list,(j,j+1)