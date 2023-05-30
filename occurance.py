"""How many occurrences of a number input by the user. Hint : It can be 0 to upto the size of an array"""
arr = [10, 20, 36, 41, -22, 36, 10, -88, 41, 20, 51, 36, 72, 144, 36, 55]

num = int(input("Enter the Number to check the occurrence :"))

arr2 = []
occurrence = 0

for i in range(len(arr)):
    if arr[i] == num:
        occurrence = occurrence + 1

print(f'The Number {num} which is occurred in the arr is {occurrence} times')

print('-'* 10)
"""Built-in Function"""
print(f' This result is using built- in function called count which gives the count of repeated number in an array{arr.count(num)}')