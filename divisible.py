"""Find all the numbers which are divisible by a user input number in the array"""



def divisible_number(arr,num_given):
    divisible_numbers = []
    left_number = []
    for num in arr:
        if num%num_given == 0:
            divisible_numbers.append(num)
        else:
            left_number.append(num)
    print(f'These numbers {left_number} are not divisible by {num_given}')
    return divisible_numbers


if __name__ == '__main__':
    arr = [10, 20, 36, 41, -22, 36, 10, -88, 41, 20, 51, 36, 72, 144, 36, 55]
    num_given = int(input("Enter the Number (1-9) : "))
    numbers = divisible_number(arr=arr, num_given=num_given)
    print(f'These numbers {numbers} are divisible by {num_given}')
