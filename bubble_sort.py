def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] >= array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


if __name__ == '__main__':
    array = [2, 3, 1, 6, 5, 7, 8]
    bubble_sort(array)
    print(array)