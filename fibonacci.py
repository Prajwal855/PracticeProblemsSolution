def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)


input_number = int(input("Enter The Number : \n"))
if __name__ == '__main__':
    for number in range(input_number):
        print(fibonacci(number=number))
