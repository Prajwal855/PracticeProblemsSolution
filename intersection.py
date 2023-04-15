def find_intersection(arr, arr2):
    for i in range(len(arr)):
        for j in range(len(arr2)):
            if arr[i] == arr2[j]:
                print(arr2[j])
    pass


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    arr2 = [5, 6, 7, 8, 9]
    print(find_intersection(arr=arr, arr2=arr2))