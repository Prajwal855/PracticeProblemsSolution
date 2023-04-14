def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 6, 7, 8, 9]
    x = 1
    result = linear_search(arr=arr, x=x)
    if result != -1:
        print(f"Element {x} is present in the array")
    else:
        print(f"Element {x} is not present")