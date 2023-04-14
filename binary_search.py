def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [3, 4, 5, 6, 7, 8, 9, 1, 2]
    x = 4
    result = binary_search(arr=arr, x=x)
    if result != -1:
        print(f"Element {x} is present ")
    else:
        print(f"Element {x} is not present Dude")
