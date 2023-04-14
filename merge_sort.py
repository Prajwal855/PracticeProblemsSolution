def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    sorted_arr = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            sorted_arr.append(left_arr[left_idx])
        else:
            sorted_arr.append(right_arr[right_idx])

    sorted_arr += left_arr[left_idx:]
    sorted_arr += right_arr[right_idx:]
    return sorted_arr


if __name__ == '__main__':
    arr = [1, 3, 7, 2, 8, 5, 4, 9]
    sorted_array = merge_sort(arr=arr)
    print(sorted_array)
