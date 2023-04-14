def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = []
        right = []
        for i in range(1, len(array)):
            if array[i] < pivot:
                left.append(array[i])
            else:
                right.append(array[i])
        return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    array = [4, 3, 2, 4, 5, 7, 8, 12, 76]
    sort = quick_sort(array)
    print(sort)
    