import math


def jump_search(arr,x):
    n = len(arr)
    s = int(math.sqrt(n))

    prev = 0
    while arr[min(s, n)-1]< x:
        prev = s
        s += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < x:
        prev += 1
        if prev == min(s, n):
            return -1

    if arr[prev] == x:
        return prev


if __name__ == "__main__":
    arr = [1, 3, 4, 2, 5, 6, 8]
    x = 9
    result = jump_search(arr=arr, x=x)
    if result != -1:
        print(f"Element {x} in present ")
    else:
        print(f"Element {x} is not Present")
