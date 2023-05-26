arr = [1, 2, 2, 3, 4, 4, 5, 6]

arr1 = [num for num in arr if arr.count(num) > 1]

arr1 = list(set(arr1))

print(arr1)

arr3 = []

# Using Loop
for num in range(len(arr)):
    for num2 in range(num + 1, len(arr)):
        if arr[num] == arr[num2] not in arr3:
            arr3.append(arr[num])


print(arr3)